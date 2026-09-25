#!/usr/bin/env python3
"""Classify craft-frontier dialogue failures from existing bot log lines.

Arrival reads this so a credit miss is a class, not a forwarded apology.
Uses the lines ``dialogue_turn.py`` already prints — no new log format.

    python3 scripts/check_dialogue_failures.py            # Mini discord.log
    python3 scripts/check_dialogue_failures.py --file F   # a log excerpt
    python3 scripts/check_dialogue_failures.py --self-test

Silence is unmeasured, not healthy (F-79). Timeout is a different class
from credit / auth / overload.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REMOTE_LOG = "~/turtleos/logs/discord.log"
WINDOW_HOURS = 36

TS = re.compile(r"^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]\s*")
ERROR = re.compile(r"Dialogue error \(([^)]+)\):\s*(.*)$")
GAVE_UP = re.compile(r"Dialogue gave up \[(\d+)\]")

CLASSES = ("credit", "auth", "overload", "timeout", "other")


def remote_host() -> str:
    override = os.environ.get("REMOTE")
    if override:
        return override
    from workshop_paths import config_file

    from turtle_remote import reachable_remote_from

    if remote := reachable_remote_from(config_file("connections.md", ROOT)):
        return remote
    raise SystemExit(
        "No Turtle remote configured. Put a `turtle@<host>` line in "
        "desk/config/connections.md, or set REMOTE."
    )


def classify(body: str) -> str:
    """One Dialogue-error payload → a class. Order is the test."""
    low = body.lower()
    if "credit balance is too low" in low or "purchase credits" in low:
        return "credit"
    if any(
        tok in low
        for tok in (
            "invalid x-api-key",
            "invalid api key",
            "authentication",
            "unauthorized",
            "error code: 401",
        )
    ):
        return "auth"
    if "overloaded" in low or "error code: 529" in low:
        return "overload"
    if "readtimeout" in low or "timeout" in low:
        return "timeout"
    return "other"


@dataclass
class Hit:
    when: datetime | None
    model: str
    cls: str
    body: str


def parse_lines(text: str, *, now: datetime, window: timedelta) -> list[Hit]:
    hits: list[Hit] = []
    cutoff = now - window
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        ts = None
        stamped = TS.match(line)
        if stamped:
            ts = datetime.strptime(stamped.group(1), "%Y-%m-%d %H:%M:%S")
            line = line[stamped.end() :]
        err = ERROR.search(line)
        if not err:
            continue
        if ts is None or ts < cutoff:
            continue
        hits.append(
            Hit(when=ts, model=err.group(1), cls=classify(err.group(2)), body=err.group(2))
        )
    return hits


def render(hits: list[Hit], *, hours: int, reachable: bool) -> str:
    if not reachable:
        return "dialogue failures: Mini log unreachable — skipped"
    if not hits:
        return (
            f"dialogue failures ({hours}h): no Dialogue error lines — "
            "unmeasured, not healthy"
        )
    counts = Counter(h.cls for h in hits)
    parts = []
    for cls in CLASSES:
        n = counts.get(cls, 0)
        if not n:
            continue
        last = max((h.when for h in hits if h.cls == cls and h.when), default=None)
        bit = f"{cls} ×{n}"
        if last:
            bit += f" last {last:%Y-%m-%d %H:%M}"
        parts.append(bit)
    return f"dialogue failures ({hours}h): " + " · ".join(parts)


def fetch_remote() -> tuple[bool, str]:
    host = remote_host()
    proc = subprocess.run(
        [
            "ssh",
            "-o",
            "ConnectTimeout=8",
            host,
            f"grep -E 'Dialogue error|Dialogue gave up' {REMOTE_LOG} || true",
        ],
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    if proc.returncode != 0:
        return False, proc.stderr
    return True, proc.stdout


def self_test() -> int:
    now = datetime(2026, 9, 5, 15, 30, 0)
    window = timedelta(hours=WINDOW_HOURS)
    planted = """
[2026-09-05 08:34:35] Dialogue error (claude-sonnet-4-6): BadRequestError: Error code: 400 - credit balance is too low
[2026-09-05 09:11:00] Dialogue error (gemma4:31b): ReadTimeout:
[2026-09-05 10:00:00] Dialogue error (claude-sonnet-4-6): InternalServerError: Error code: 529 - overloaded_error
[2026-09-04 01:00:00] Dialogue error (claude-sonnet-4-6): BadRequestError: credit balance is too low
bot started
"""
    hits = parse_lines(planted, now=now, window=window)
    by = Counter(h.cls for h in hits)
    failures: list[str] = []
    if by.get("credit") != 1:
        failures.append(f"planted credit not counted as 1 (got {by.get('credit')})")
    if by.get("timeout") != 1:
        failures.append(f"planted timeout not a different class (got {by})")
    if by.get("overload") != 1:
        failures.append(f"planted overload missed (got {by})")
    # Outside the window must not inflate.
    if len(hits) != 3:
        failures.append(f"window leaked historical lines: {hits}")

    credit_body = (
        "BadRequestError: Error code: 400 - {'type': 'error', 'error': "
        "{'type': 'invalid_request_error', 'message': "
        "'Your credit balance is too low to access the Anthropic API. "
        "Please go to Plans & Billing to upgrade or purchase credits.'}}"
    )
    if classify(credit_body) != "credit":
        failures.append("live credit string classified as " + classify(credit_body))
    if classify("ReadTimeout: ") != "timeout":
        failures.append("timeout classified as " + classify("ReadTimeout: "))
    if classify("AuthenticationError: invalid x-api-key") != "auth":
        failures.append("auth plant missed")

    silent = render([], hours=WINDOW_HOURS, reachable=True)
    if "healthy" in silent.lower() and "not healthy" not in silent.lower():
        failures.append(f"silence reported as healthy: {silent}")
    if "unmeasured" not in silent:
        failures.append(f"silence not marked unmeasured: {silent}")

    timeout_only = parse_lines(
        "[2026-09-05 12:00:00] Dialogue error (gemma4:31b): ReadTimeout: \n",
        now=now,
        window=window,
    )
    timeout_line = render(timeout_only, hours=WINDOW_HOURS, reachable=True)
    if "credit" in timeout_line:
        failures.append(f"timeout line reported as credit: {timeout_line}")
    if "timeout ×1" not in timeout_line:
        failures.append(f"timeout not named: {timeout_line}")

    if failures:
        for line in failures:
            print(f"SELF-TEST FAIL: {line}")
        return 1
    print("check_dialogue_failures self-test: ok (credit / timeout / overload / silence)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", type=Path)
    parser.add_argument("--hours", type=int, default=WINDOW_HOURS)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()

    if args.file:
        reachable, text = True, args.file.read_text(encoding="utf-8", errors="replace")
    else:
        try:
            reachable, text = fetch_remote()
        except SystemExit as exc:
            print(f"dialogue failures: {exc}")
            return 0

    hits = parse_lines(
        text,
        now=datetime.now(),
        window=timedelta(hours=args.hours),
    )
    print(render(hits, hours=args.hours, reachable=reachable))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
