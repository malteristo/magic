"""Resolve live workshop config.

Personal instance files live in ``desk/config/``. Templates stay in
``system/config/``. Look at desk first; fall back to the old system path
so a half-migrated tree still runs.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def config_file(name: str, root: Path | None = None) -> Path:
    root = root or ROOT
    live = root / "desk" / "config" / name
    legacy = root / "system" / "config" / name
    if live.is_file():
        return live
    if legacy.is_file():
        return legacy
    return live
