#!/usr/bin/env python3
"""Report craft moves that have not yet reached the workshop backlog.

A *move* is one backlog item changing state, written by the Mage in a
craft-turtle eddy — pushing something forward, refining what it should be,
retiring it, splitting it. The point of moves is that development can happen
without a Forge or Anvil session: half an hour on a phone is enough to decide
something, and the decision has to survive that.

Surviving means being read. This is the same failure the intake reconciler was
written for and the same failure the boom buffer had for months: a queue nobody
can drain stops being read, and then the thinking in it was never done at all.
So the rule here is mechanical rather than a judgment call, and identical in
shape to ``harvest_craft_intake.py``:

    **A move is harvested when its slug appears in desk/craft/backlog.md.**

That is deliberately weak — it says the move reached the workshop record, not
that the work is done. Whether the work is done is tracked in the backlog item
itself, where work is always tracked. What this answers is only "did anyone
read what the Mage decided at the doctor's office", and an unharvested move is
a decision that fell on the floor.

Usage:
    python3 scripts/harvest_craft_moves.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BACKLOG = ROOT / "desk" / "craft" / "backlog.md"
MOVES = ROOT / "desk" / "craft" / "moves"

FRONT_ITEM_RE = re.compile(r"^item:\s*(?P<item>.+?)\s*$", re.MULTILINE)
FRONT_MOVE_RE = re.compile(r"^move:\s*(?P<move>.+?)\s*$", re.MULTILINE)


def summarize(path: Path) -> tuple[str, str]:
    """(referenced item, move kind) — best effort, never raises on a free-form file."""
    try:
        head = path.read_text(encoding="utf-8")[:1200]
    except OSError:
        return ("?", "?")
    item = FRONT_ITEM_RE.search(head)
    move = FRONT_MOVE_RE.search(head)
    return (
        item.group("item") if item else "—",
        move.group("move") if move else "—",
    )


def main() -> int:
    if not MOVES.is_dir():
        print("No craft moves directory yet — nothing has been written from an eddy.")
        return 0

    files = sorted(MOVES.glob("*.md"))
    if not files:
        print("No craft moves recorded.")
        return 0

    backlog = BACKLOG.read_text(encoding="utf-8") if BACKLOG.is_file() else ""

    unharvested = [p for p in files if p.stem not in backlog]
    harvested = len(files) - len(unharvested)

    if not unharvested:
        print(f"All {len(files)} craft move(s) reached the backlog — nothing to fold in.")
        return 0

    print(f"{len(unharvested)} craft move(s) NOT yet in the workshop backlog "
          f"({harvested} already folded in):")
    for path in unharvested:
        item, move = summarize(path)
        print(f"  {path.stem}  [{move} → {item}]")
    print("  Fold each into desk/craft/backlog.md — cite the move slug so this stops reporting it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
