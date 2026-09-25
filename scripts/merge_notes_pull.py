#!/usr/bin/env python3
"""merge_notes_pull.py — harvest Mini notes without clobbering a longer workshop file.

``sync_practice_root.sh`` rsyncs ``state/notes/*.md`` onto ``desk/notes/``.
Turtle writes the Mini side; Spirit writes Architecture and other workshop
notes on the same filenames. A newer, shorter Mini stub has twice today
replaced ``agent-as-memory.md``. Size is the check: a shorter remote file
does not replace a longer local one. New files still harvest.

    python3 scripts/merge_notes_pull.py SRC DEST
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path


def merge_notes(src: Path, dest: Path) -> list[str]:
    dest.mkdir(parents=True, exist_ok=True)
    log: list[str] = []
    if not src.is_dir():
        return log
    for src_file in sorted(src.glob("*.md")):
        if not src_file.is_file():
            continue
        dest_file = dest / src_file.name
        remote_size = src_file.stat().st_size
        if dest_file.is_file():
            local_size = dest_file.stat().st_size
            if local_size > remote_size:
                log.append(
                    f"  kept: desk/notes/{src_file.name} "
                    f"({local_size} > {remote_size} remote)"
                )
                continue
            shutil.copy2(src_file, dest_file)
            log.append(f"  updated: desk/notes/{src_file.name}")
            continue
        shutil.copy2(src_file, dest_file)
        log.append(f"  harvested: desk/notes/{src_file.name}")
    return log


def main(argv: list[str]) -> int:
    if len(argv) != 3 or argv[1] in {"-h", "--help"}:
        print(__doc__)
        return 0 if len(argv) != 3 else 2
    src, dest = Path(argv[1]), Path(argv[2])
    for line in merge_notes(src, dest):
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
