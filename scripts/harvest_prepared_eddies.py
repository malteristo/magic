#!/usr/bin/env python3
"""Report prepared eddies ready for harvest that have not yet reached bright.

A prepared eddy's return path: Turtle marks disposition ``ready`` (and writes
``## Determination`` into the workspace); Spirit folds that determination into
``desk/boom/bright.md`` (rewrite or release) and any named destinations, then
marks ``harvested``. Hand-editing bright from chat memory is the craft-intake
defect again — this script is the checkable gate.

A ready entry is harvested when its thread id **or** surface slug appears in
``desk/boom/bright.md`` *and* the sidecar says ``harvested``. Until then it
prints as NOT yet folded.

The sidecar is Mini-canonical. Prefer ``desk/craft/prepared_eddies.yaml`` after
``sync_practice_root.sh pull``; fall back to SSH when the local copy is absent.

Usage:
    python3 scripts/harvest_prepared_eddies.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRIGHT = ROOT / "desk" / "boom" / "bright.md"
LOCAL_SIDECAR = ROOT / "desk" / "craft" / "prepared_eddies.yaml"
SURFACES = ROOT / "desk" / "craft" / "surfaces"
from workshop_paths import config_file

CONNECTIONS = config_file("connections.md", ROOT)

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore


def _remote() -> str:
    import os

    override = os.environ.get("REMOTE")
    if override:
        return override
    from turtle_remote import reachable_remote_from

    if remote := reachable_remote_from(CONNECTIONS):
        return remote
    raise SystemExit(
        "No Turtle remote configured. Put a `turtle@<host>` line in "
        "desk/config/connections.md, or set REMOTE."
    )


def _load_sidecar() -> dict:
    if yaml is None:
        print("PyYAML required", file=sys.stderr)
        sys.exit(2)
    if LOCAL_SIDECAR.is_file():
        return yaml.safe_load(LOCAL_SIDECAR.read_text(encoding="utf-8")) or {}
    remote = _remote()
    practice = "/Users/turtle/workshops/kermit"
    path = f"{practice}/thread-state/prepared_eddies.yaml"
    try:
        raw = subprocess.check_output(
            ["ssh", remote, f"cat {path}"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("No prepared_eddies sidecar locally or on Mini — nothing to harvest.")
        return {}
    return yaml.safe_load(raw) or {}


def _determination(surface_rel: str) -> str:
    name = Path(surface_rel).name
    path = SURFACES / name
    if not path.is_file():
        return "(workspace not on workshop yet — pull surfaces)"
    text = path.read_text(encoding="utf-8")
    m = re.search(
        r"^## Determination\s*\n+(.*?)(?=\n## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not m:
        return "(no ## Determination in workshop copy)"
    body = m.group(1).strip()
    return body.splitlines()[0][:120] if body else "(empty Determination)"


def main() -> int:
    data = _load_sidecar()
    prepared = data.get("prepared") or {}
    if not prepared:
        print("No prepared eddies recorded.")
        return 0

    bright = BRIGHT.read_text(encoding="utf-8") if BRIGHT.is_file() else ""

    ready = []
    for tid, entry in prepared.items():
        if not isinstance(entry, dict):
            continue
        if entry.get("disposition") != "ready":
            continue
        surface = entry.get("surface") or ""
        slug = Path(str(surface)).stem
        in_bright = tid in bright or (slug and slug in bright)
        ready.append((tid, entry, in_bright, slug))

    if not ready:
        print("No prepared eddies in disposition: ready.")
        return 0

    unharvested = [r for r in ready if not r[2]]
    if not unharvested:
        print(
            f"All {len(ready)} ready prepared eddy(ies) already cited in bright — "
            "mark sidecar harvested after folding destinations."
        )
        for tid, entry, _, slug in ready:
            print(f"  {tid}  {entry.get('surface')}  [{slug}]")
        return 0

    print(
        f"{len(unharvested)} prepared eddy(ies) READY but NOT yet folded into bright "
        f"({len(ready) - len(unharvested)} already cited):"
    )
    for tid, entry, _, slug in unharvested:
        one = entry.get("determination_one_liner") or _determination(str(entry.get("surface") or ""))
        print(f"  {tid}  {entry.get('surface')}")
        print(f"    → {one}")
    print(
        "  Fold each into desk/boom/bright.md (rewrite or release the spun-off entry), "
        "route named next moves, then set disposition: harvested on the Mini sidecar."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
