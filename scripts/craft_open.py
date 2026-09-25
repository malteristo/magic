#!/usr/bin/env python3
"""craft_open.py — generated open-backlog view for `. turtle` arrivals.

Evaluation D: arrival reads this view, never `desk/craft/backlog.md` (F-19).
The backlog file is the store (~180 KB). This is the queue (~5K tokens).

F-76: newest 24 stay; every still-open id older than 14 days is listed under
Aging (title only). Those ids cannot hide behind "+N older not shown."

    python3 scripts/craft_open.py              # stdout
    python3 scripts/craft_open.py --self-test  # positive control

Budget is enforced here, not by asking Spirit to remember it (F-66).
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from export_craft_digest import Item, parse_backlog  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
BACKLOG = ROOT / "desk" / "craft" / "backlog.md"

# 5K tokens ≈ 20 KB. Cap items so a fat backlog cannot blow the arrival.
OPEN_BUDGET = 20 * 1024
MAX_ITEMS = 24
AGING_DAYS = 14
TITLE_LIMIT = 90
REST_LIMIT = 140

_NEXT_MARKERS = ("Next:", "Target condition:", "Open for", "Pickup:")


def _rest_after_title(item: Item) -> str:
    title = item.title
    rest = item.body[len(f"**{title}**") :].lstrip(" —-–")
    rest = re.sub(r"\s+", " ", rest).strip()
    for marker in _NEXT_MARKERS:
        idx = rest.find(marker)
        if idx != -1:
            rest = rest[idx:]
            break
    if len(rest) > REST_LIMIT:
        rest = rest[:REST_LIMIT].rsplit(" ", 1)[0] + "…"
    return rest


def _title(item: Item) -> str:
    title = item.title
    if len(title) > TITLE_LIMIT:
        return title[:TITLE_LIMIT].rsplit(" ", 1)[0] + "…"
    return title


def _item_key(item: Item) -> str:
    """Newest-first: ids are dated `YYYY-MM-DD-…`."""
    return item.id


def _is_queue_item(item: Item) -> bool:
    """Drop shipped/dropped rows and the strikethrough leftover the digest parser reads as id `x`."""
    if item.shipped or item.dropped:
        return False
    if item.id in {"", "x", " "}:
        return False
    if item.body.lstrip().startswith("~~"):
        return False
    return True


def item_date(item: Item) -> date | None:
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", item.id)
    if not m:
        return None
    try:
        return date.fromisoformat(m.group(1))
    except ValueError:
        return None


def is_aging(item: Item, today: date) -> bool:
    """Open and older than 14 days, or undated — neither may hide (F-76)."""
    d = item_date(item)
    if d is None:
        return True
    return (today - d).days > AGING_DAYS


def render_open(text: str, today: str | None = None) -> str:
    items, _unknown = parse_backlog(text)
    open_items = [i for i in items if _is_queue_item(i)]
    open_items.sort(key=_item_key, reverse=True)
    today_s = today or date.today().isoformat()
    today_d = date.fromisoformat(today_s)
    shown = open_items[:MAX_ITEMS]
    aging = [i for i in open_items if is_aging(i, today_d)]
    aging.sort(key=_item_key)
    shown_ids = {i.id for i in shown}
    aging_ids = {i.id for i in aging}
    hidden = [i for i in open_items if i.id not in shown_ids and i.id not in aging_ids]

    lines = [
        "# Craft open",
        f"generated: {today_s} · {len(shown)}/{len(open_items)} open · "
        f"{len(aging)} aging · source desk/craft/backlog.md · "
        f"budget {OPEN_BUDGET:,} bytes",
        "",
        "Arrival reads this view, not the backlog file (F-19). "
        "Aging is pressure, not a terminal (F-76).",
        "",
    ]
    for item in shown:
        rest = _rest_after_title(item)
        line = f"- `{item.id}` — **{_title(item)}**"
        if rest:
            line += f" — {rest}"
        lines.append(line)
    if aging:
        lines.append("")
        lines.append(f"## Aging (>{AGING_DAYS}d, still open)")
        lines.append("")
        for item in aging:
            lines.append(f"- `{item.id}` — **{_title(item)}**")
    if hidden:
        lines.append("")
        lines.append(
            f"+{len(hidden)} open under {AGING_DAYS}d not in the newest "
            f"{MAX_ITEMS} — they are not aging yet."
        )
    lines.append("")
    out = "\n".join(lines)
    if len(out.encode("utf-8")) > OPEN_BUDGET:
        raise SystemExit(
            f"craft_open: view is {len(out.encode('utf-8')):,} bytes "
            f"(budget {OPEN_BUDGET:,}). Do not hide aging ids to fit."
        )
    return out


def self_test() -> int:
    """Closed items vanish; a 20-day-old open appears under Aging behind 24 newer."""
    failures: list[str] = []

    planted = """# Craft Backlog
## Open
- [ ] [2026-09-04-visible-open] **Visible open item.** Target condition: the view shows this id.
- [x] [2026-09-04-should-vanish] **Shipped item must not appear.** If this shows, the filter failed.
- [d] [2026-09-04-dropped-open] **Dropped item.** Dropped: grammar check — must not appear as open.
- [ ] [2026-08-01-older-open] **Older open.** Pickup: must appear under Aging.
"""
    view = render_open(planted, today="2026-09-04")
    if "2026-09-04-visible-open" not in view:
        failures.append("planted open item missing")
    if "2026-09-04-should-vanish" in view:
        failures.append("shipped item leaked into the open view")
    if "2026-09-04-dropped-open" in view:
        failures.append("dropped item leaked into the open view")
    if "Target condition:" not in view:
        failures.append("explicit next/target marker was not preferred")
    if "2026-08-01-older-open" not in view or "## Aging" not in view:
        failures.append("20-day-old open did not appear under Aging")

    lines = ["# Craft Backlog", "## Open"]
    lines.append("- [ ] [2026-08-01-aged] **Aged behind a full fresh window.**")
    for i in range(24):
        lines.append(
            f"- [ ] [2026-09-04-keep-{i:02d}] **Keep {i}.** Target condition: keep."
        )
    aged = render_open("\n".join(lines), today="2026-09-04")
    if "2026-08-01-aged" not in aged or "## Aging" not in aged:
        failures.append("aging id hid behind 24 newer rows")
    if "older open not shown" in aged:
        failures.append("omit-line hid an aging id")
    if len(aged.encode("utf-8")) > OPEN_BUDGET:
        failures.append("aging pair exceeded the byte budget")

    live = BACKLOG.read_text(encoding="utf-8") if BACKLOG.is_file() else ""
    if live:
        live_items, _ = parse_backlog(live)
        live_view = render_open(live)
        if len(live_view.encode("utf-8")) > OPEN_BUDGET:
            failures.append("live backlog view exceeds budget")
        for item in live_items:
            if item.shipped and f"`{item.id}`" in live_view:
                failures.append(f"shipped id leaked: {item.id}")
            if item.dropped and f"`{item.id}`" in live_view:
                failures.append(f"dropped id leaked: {item.id}")
            if (
                _is_queue_item(item)
                and is_aging(item, date.today())
                and f"`{item.id}`" not in live_view
            ):
                failures.append(f"aging id hidden: {item.id}")

    if failures:
        for f in failures:
            print(f"SELF-TEST FAIL: {f}")
        return 1
    print("craft_open self-test: ok (open shown, shipped/dropped hidden, aging cannot hide)")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) > 1 and argv[1] in {"-h", "--help"}:
        print(__doc__)
        return 0
    if len(argv) > 1 and argv[1] == "--self-test":
        return self_test()
    if not BACKLOG.is_file():
        print("craft_open: desk/craft/backlog.md missing", file=sys.stderr)
        return 1
    sys.stdout.write(render_open(BACKLOG.read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
