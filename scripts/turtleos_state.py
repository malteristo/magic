#!/usr/bin/env python3
"""One page of numbers about turtleOS development, read from the live sources.

turtleOS development accumulates in twenty places across four hosts. Three docs
each claimed to consolidate it, and each stated its own cadence on its own face.
Measured 2026-08-02, the priority stack was 80 commits behind its "use this
before starting a chapter" and the acceptance index 104 behind its own. Not one
had a named re-run. (The stack was retired into the matrix that day; the
acceptance index became the scenario catalogue.)

So this does not add a fourth hand-written view. It **counts**, and it is pulled
rather than pushed: run it, read it, act. Nothing is written to disk and nothing
runs on a timer, which is the difference between this and the weekly health-read
generator retired on 2026-08-02 for writing status theatre into ``proposals/``.
A generated essay about how the work is going is a faucet. A count of what is
open is an instrument.

The judgment layer stays human, in the traceability matrix. This tells you when
that matrix has drifted; it does not try to replace what it says.

Usage:
    python3 scripts/turtleos_state.py             # everything reachable
    python3 scripts/turtleos_state.py --offline   # skip the Mini and Discord
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TURTLEOS = ROOT.parent / "turtleos"

# The date the story layer's first eddy note was written. Threads whose last
# activity predates it never had a chance to be indexed.
STORY_LAYER_START = datetime(2026, 7, 15, tzinfo=timezone.utc)
DISCORD_EPOCH_MS = 1420070400000

# The docs that carry a cadence claim, and the claim each makes about itself.
# Drift is measured in commits since the doc last changed, because "chapter" is
# not a unit git knows. ``docs/priority-stack.md`` was here until 2026-08-02,
# when it was retired into the matrix at 80 commits behind its own instruction.
INDEX_DOCS = {
    "docs/traceability-matrix.md": "update at every chapter close",
    "docs/acceptance/README.md": "scenario definitions stay true to the build",
}


def remote_host() -> str:
    """The Mini's address lives in the gitignored config, never in a tracked
    file — same rule and same source as ``scripts/sync_practice_root.sh``."""
    import os
    import re

    override = os.environ.get("REMOTE")
    if override:
        return override
    from workshop_paths import config_file

    from turtle_remote import reachable_remote_from

    if remote := reachable_remote_from(config_file("connections.md", ROOT)):
        return remote
    # No hardcoded instance. The docstring above states the rule — the Mini's
    # address lives in the gitignored config, never in a tracked file — and a
    # literal fallback three lines below it broke that rule quietly for weeks.
    # It also ships the author's hostname to a public repo and points every
    # other practitioner at a machine they do not own. Fail loudly instead.
    raise SystemExit(
        "No Turtle remote configured. Put a `turtle@<host>` line in "
        "desk/config/connections.md, or pass --remote."
    )


REMOTE = remote_host()

# Statuses that mean "someone must go and look at reality", as written in the
# headings of desk/turtle_issues.md.
PENDING_PATTERNS = ("living verify", "verify pending", "dogfood pending")
OPEN_PATTERNS = ("— open", "latent", "runbook mitigated", "slices open")


def sh(cmd: list[str], cwd: Path | None = None) -> str:
    try:
        return subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, timeout=30, check=False
        ).stdout.strip()
    except (subprocess.TimeoutExpired, OSError):
        return ""


def ssh(script: str) -> str:
    return sh(["ssh", "-o", "ConnectTimeout=8", REMOTE, script])


def rule(title: str) -> None:
    print(f"\n\033[1m{title}\033[0m")


def snowflake_date(sid: str) -> datetime:
    return datetime.fromtimestamp(
        ((int(sid) >> 22) + DISCORD_EPOCH_MS) / 1000, timezone.utc
    )


# ─── the defect corpus ───────────────────────────────────────────────


def read_issues() -> tuple[Counter, list[tuple[str, str]]]:
    """Tally INT statuses from their headings, and return the ones still owed
    a look. The heading is the status of record; a separate status file would
    be a second place to forget to update."""
    path = ROOT / "desk" / "turtle_issues.md"
    if not path.is_file():
        return Counter(), []
    tally: Counter = Counter()
    pending: list[tuple[str, str]] = []
    seen: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^### (INT-\d+): (.*)$", line)
        if not m:
            continue
        ident, rest = m.group(1), m.group(2)
        if ident in seen:
            # The file interleaves some duplicated sections (recorded damage,
            # predates Two Chronicles) — count each issue once, at its first
            # and most recent heading.
            continue
        seen.add(ident)
        low = rest.lower()
        if any(p in low for p in PENDING_PATTERNS):
            tally["awaiting living verify"] += 1
            pending.append((ident, rest.split("(")[0].strip()[:58]))
        elif any(p in low for p in OPEN_PATTERNS):
            tally["open / latent"] += 1
            pending.append((ident, rest.split("(")[0].strip()[:58]))
        elif "verified" in low or "resolved" in low or "closed" in low or "spec-addressed" in low:
            tally["closed"] += 1
        elif "fix-deployed" in low:
            tally["deployed"] += 1
        else:
            # Mostly the oldest issues, whose headings predate the
            # reported→diagnosed→fix-deployed→verified convention.
            tally["unclassified heading"] += 1
    return tally, pending


# ─── the matrix ──────────────────────────────────────────────────────


def read_matrix() -> tuple[int, Counter]:
    path = TURTLEOS / "docs" / "traceability-matrix.md"
    if not path.is_file():
        return 0, Counter()
    text = path.read_text(encoding="utf-8")
    row_lines = [ln for ln in text.splitlines() if ln.startswith("| §")]
    # Scanning the whole document counted the status legend and every status
    # word appearing in an Action or note cell, so the tally exceeded the row
    # count and the Gap number was wrong by exactly one legend line. Named as a
    # five-minute fix in five consecutive sessions, which is the argument for
    # counting per row: one status per row, the first one, and anything the
    # vocabulary cannot read is surfaced rather than dropped.
    statuses: Counter = Counter()
    for ln in row_lines:
        found = re.search(r"\*\*(Aligned|Partial|Gap|Legacy|Retire-pending)\*\*", ln)
        statuses[found.group(1) if found else "unlabelled"] += 1
    return len(row_lines), statuses


def index_doc_drift() -> list[tuple[str, str, int, str]]:
    """How many commits have landed since each index doc last changed."""
    out = []
    for rel, cadence in INDEX_DOCS.items():
        if not (TURTLEOS / rel).is_file():
            # git still answers for a deleted path, and the answer — "0 commits
            # behind" — is the most confident possible lie about a doc that no
            # longer exists.
            out.append((rel, "deleted", -1, cadence))
            continue
        last = sh(["git", "log", "-1", "--format=%h %ad", "--date=short", "--", rel], cwd=TURTLEOS)
        if not last:
            continue
        sha = last.split()[0]
        behind = sh(["git", "rev-list", "--count", f"{sha}..HEAD"], cwd=TURTLEOS)
        out.append((rel, last.split()[-1], int(behind or 0), cadence))
    return out


# ─── the backlogs ────────────────────────────────────────────────────


def read_backlog(text: str) -> tuple[int, int]:
    """(open, done) over ``- [x]``/``- [`` bullets."""
    done = len(re.findall(r"^- \[x\]", text, re.M))
    total = len(re.findall(r"^- \[", text, re.M))
    return total - done, done


def local_backlog() -> tuple[int, int]:
    path = ROOT / "desk" / "craft" / "backlog.md"
    return read_backlog(path.read_text(encoding="utf-8")) if path.is_file() else (0, 0)


# ─── output ──────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--offline", action="store_true", help="skip the Mini and Discord")
    args = ap.parse_args(argv)

    print(f"\033[1mturtleOS state · {datetime.now().strftime('%Y-%m-%d %H:%M')}\033[0m")

    rule("Code")
    head = sh(["git", "rev-parse", "--short", "HEAD"], cwd=TURTLEOS)
    dirty = sh(["git", "status", "--short"], cwd=TURTLEOS)
    print(f"  forge {head}{' (dirty)' if dirty else ''}"
          f" · {len(list(TURTLEOS.glob('*.py')))} modules"
          f" · {len(list((TURTLEOS / 'tests').glob('*.py')))} test files"
          f" · {len(list((TURTLEOS / 'docs').rglob('*.md')))} docs")

    rule("Defects (desk/turtle_issues.md)")
    tally, pending = read_issues()
    total = sum(tally.values())
    print(f"  {total} tracked · " + " · ".join(f"{v} {k}" for k, v in tally.most_common()))
    if pending:
        print("  owed a look:")
        for ident, summary in pending:
            print(f"    {ident}  {summary}")

    rule("Spec ↔ implementation (docs/traceability-matrix.md)")
    rows, statuses = read_matrix()
    print(f"  {rows} rows · " + " · ".join(f"{v} {k}" for k, v in statuses.most_common()))

    rule("Index docs — each states its own cadence")
    for rel, when, behind, cadence in index_doc_drift():
        if behind < 0:
            print(f"  {rel:38} \033[33mlisted but missing from the repo\033[0m")
            continue
        flag = "  \033[33m← drifted\033[0m" if behind > 20 else ""
        print(f"  {rel:38} {when}  {behind:>4} commits behind   ({cadence}){flag}")

    rule("Backlogs")
    lo, ld = local_backlog()
    print(f"  desk/craft/backlog.md         {lo} open, {ld} done")

    if args.offline:
        print("\n  --offline: Mini and Discord not read.")
        return 0

    rule("Mini")
    mini = ssh("cd ~/turtleos && git rev-parse --short HEAD")
    print(f"  turtleos {mini or '(unreachable)'}"
          + ("  \033[33m← differs from forge\033[0m" if mini and head and mini != head else ""))
    remote_backlog = ssh("cat ~/workshops/*/craft/backlog.md 2>/dev/null")
    if remote_backlog:
        ro, rd = read_backlog(remote_backlog)
        note = "  ← harvest is one-way; Spirit marks the local copy only" if ro and not rd else ""
        print(f"  craft/backlog.md (intake)     {ro} open, {rd} done{note}")

    rule("Story-layer coverage")
    counts = ssh(
        "for r in ~/workshops/*/; do n=$(basename $r); "
        "e=$(ls $r/story/eddies/*.md 2>/dev/null | wc -l | tr -d ' '); "
        "d=$(ls $r/story/daily/*.md 2>/dev/null | wc -l | tr -d ' '); "
        'echo "$n $e $d"; done'
    )
    for line in counts.splitlines():
        parts = line.split()
        if len(parts) == 3 and (parts[1] != "0" or parts[2] != "0"):
            print(f"  {parts[0]:16} {parts[1]:>4} eddy notes  {parts[2]:>4} daily notes")

    rule("Discord — the largest store, and the one nothing indexes by itself")
    raw = ssh(
        "cd ~/turtleos && TOKEN=$(grep '^DISCORD_BOT_TOKEN' .env | cut -d= -f2-); "
        "C=$(grep '^DISCORD_CHANNEL_DIALOGUE' .env | cut -d= -f2-); "
        "G=$(curl -s -H \"Authorization: Bot $TOKEN\" -A 'DiscordBot (turtleos, 1.0)' "
        "https://discord.com/api/v10/channels/$C | python3 -c "
        "'import json,sys;print(json.load(sys.stdin)[\"guild_id\"])'); "
        "curl -s -H \"Authorization: Bot $TOKEN\" -A 'DiscordBot (turtleos, 1.0)' "
        "https://discord.com/api/v10/guilds/$G/threads/active"
    )
    try:
        threads = json.loads(raw).get("threads", [])
    except (json.JSONDecodeError, TypeError):
        threads = []
    if not threads:
        print("  (unreachable)")
        return 0
    per_parent: Counter = Counter()
    msgs: Counter = Counter()
    stale = 0
    for t in threads:
        per_parent[t["parent_id"]] += 1
        msgs[t["parent_id"]] += t.get("message_count", 0)
        last = t.get("last_message_id")
        if last and snowflake_date(last) < STORY_LAYER_START and t.get("message_count", 0) >= 4:
            stale += 1
    print(f"  {len(threads)} unarchived threads · {sum(msgs.values())} messages")
    print(f"  {stale} of them ended before the story layer began "
          f"({STORY_LAYER_START.date()}) with 4+ messages")
    print("  (archived threads are not counted here — per-channel call; "
          "scripts/backfill_eddy_notes.py in turtleos counts both)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
