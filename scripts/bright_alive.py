#!/usr/bin/env python3
"""bright_alive.py — generated Alive view for arrivals.

Evaluation D: arrival reads this view, never `desk/boom/bright.md`.
The store keeps every entry (the diet pass is a sweep, not this script).
The view is capped at 12 — the number decided 2026-08-12 — newest dated first.
Undated entries are counted and omitted: they cannot age, so they cannot rank.

    python3 scripts/bright_alive.py              # stdout
    python3 scripts/bright_alive.py --self-test
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRIGHT = ROOT / "desk" / "boom" / "bright.md"

ALIVE_CAP = 12
ALIVE_BUDGET = 12 * 1024
TITLE_LIMIT = 90
REST_LIMIT = 140
DATE_RE = re.compile(r"20\d{2}-\d{2}-\d{2}")


def alive_region(text: str) -> str:
    m = re.search(r"^## Alive\b(.*?)^## ", text, re.S | re.M)
    return m.group(1) if m else ""


def parse_entries(region: str) -> list[tuple[str, date | None, str]]:
    """Return (title, newest_date_or_None, rest) for each `**…**` lead line."""
    out: list[tuple[str, date | None, str]] = []
    for line in region.splitlines():
        if not line.startswith("**"):
            continue
        title_m = re.match(r"\*\*(.+?)\*\*", line)
        title = title_m.group(1) if title_m else line[:80]
        newest = None
        found = DATE_RE.findall(line)
        if found:
            try:
                newest = max(date.fromisoformat(d) for d in found)
            except ValueError:
                newest = None
        rest = line[len(f"**{title}**") :].lstrip(" —-–")
        rest = re.sub(r"\s+", " ", rest).strip()
        out.append((title, newest, rest))
    return out


def _clip(s: str, limit: int) -> str:
    if len(s) <= limit:
        return s
    return s[:limit].rsplit(" ", 1)[0] + "…"


def render_alive(text: str, today: str | None = None) -> str:
    entries = parse_entries(alive_region(text))
    dated = [(t, d, r) for t, d, r in entries if d is not None]
    undated = len(entries) - len(dated)
    dated.sort(key=lambda row: row[1], reverse=True)
    shown = dated[:ALIVE_CAP]
    omitted = len(dated) - len(shown)
    today = today or date.today().isoformat()

    lines = [
        "# Alive",
        f"generated: {today} · {len(shown)}/{len(dated)} dated · "
        f"{undated} undated omitted · cap {ALIVE_CAP} · budget {ALIVE_BUDGET:,} bytes",
        "",
        "Arrival reads this view, not `desk/boom/bright.md` (evaluation D).",
        "",
    ]
    for title, when, rest in shown:
        line = f"- **{_clip(title, TITLE_LIMIT)}** · {when.isoformat()}"
        if rest:
            line += f" — {_clip(rest, REST_LIMIT)}"
        lines.append(line)
    extra = []
    if omitted:
        extra.append(f"{omitted} older dated")
    if undated:
        extra.append(f"{undated} undated")
    if extra:
        lines.append("")
        lines.append("+{} stay in bright.md — the diet pass is a sweep.".format(
            " and ".join(extra)
        ))
    lines.append("")
    out = "\n".join(lines)
    if len(out.encode("utf-8")) > ALIVE_BUDGET:
        raise SystemExit(
            f"bright_alive: view is {len(out.encode('utf-8')):,} bytes "
            f"(budget {ALIVE_BUDGET:,})."
        )
    return out


def self_test() -> int:
    failures: list[str] = []
    planted = """# Bright
## Alive
**Fresh item** — (2026-09-01) keep this.
**Older item** — (2026-01-01) should rank below.
**Undated item** — no date here, omit from the twelve.
## Seed Bank
**Seed** — (2026-09-02) must not appear; wrong section.
"""
    view = render_alive(planted, today="2026-09-04")
    if "Fresh item" not in view:
        failures.append("dated Alive entry missing")
    if "Undated item" in view:
        failures.append("undated entry leaked into the view")
    if "Seed" in view:
        failures.append("Seed Bank entry leaked into the Alive view")
    if "2026-09-01" not in view:
        failures.append("date not shown")

    fat = ["# Bright", "## Alive"]
    for i in range(20):
        fat.append(f"**Title {i}** — (2026-08-{(i % 28) + 1:02d}) " + ("word " * 40))
    fat.append("## Next")
    fat_view = render_alive("\n".join(fat), today="2026-09-04")
    if len(fat_view.encode("utf-8")) > ALIVE_BUDGET:
        failures.append("fat Alive exceeded budget")
    if fat_view.count("\n- **") > ALIVE_CAP:
        failures.append("fat Alive exceeded the cap")
    if "stay in bright.md" not in fat_view:
        failures.append("omitted rows not named")

    if BRIGHT.is_file():
        live = render_alive(BRIGHT.read_text(encoding="utf-8"))
        if len(live.encode("utf-8")) > ALIVE_BUDGET:
            failures.append("live Alive view exceeds budget")
        if live.count("\n- **") > ALIVE_CAP:
            failures.append("live Alive view exceeded the cap")

    if failures:
        for f in failures:
            print(f"SELF-TEST FAIL: {f}")
        return 1
    print("bright_alive self-test: ok (dated shown, undated/seeds hidden, cap held)")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) > 1 and argv[1] in {"-h", "--help"}:
        print(__doc__)
        return 0
    if len(argv) > 1 and argv[1] == "--self-test":
        return self_test()
    if not BRIGHT.is_file():
        print("bright_alive: desk/boom/bright.md missing", file=sys.stderr)
        return 1
    sys.stdout.write(render_alive(BRIGHT.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
