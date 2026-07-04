#!/usr/bin/env python3
"""Compare Magic desk practice outputs with turtleOS native practice root on Mini.

Default mode is report-only. Use --backfill-missing to copy files that exist on
Turtle but do not exist locally. Existing local files are never overwritten.

Sync direction: Mini (turtleOS writes) → Forge (Spirit reads at arrival).
Does not compare boom, briefings, or intentions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REMOTE_PRACTICE_ROOT = "/Users/turtle/workshops/kermit"
LOCAL_ROOT = Path(__file__).resolve().parents[1]
CONNECTIONS_PATH = LOCAL_ROOT / "system" / "config" / "connections.md"

# Remote path → local path
PATH_MAP: tuple[tuple[str, str], ...] = (
    ("sessions", "desk/sessions"),
    ("proposals", "desk/proposals"),
)


def default_remote() -> str:
    if env_remote := os.environ.get("TURTLE_SSH_TARGET"):
        return env_remote

    if CONNECTIONS_PATH.exists():
        text = CONNECTIONS_PATH.read_text(errors="ignore")
        match = re.search(r"`(turtle@[^`]+)`", text)
        if match:
            return match.group(1)

    return "turtle@turtles-mac-mini"


@dataclass(frozen=True)
class FileInfo:
    relpath: str
    sha256: str
    size: int
    mtime: float


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def collect_local() -> dict[str, FileInfo]:
    files: dict[str, FileInfo] = {}
    for remote_sub, local_sub in PATH_MAP:
        directory = LOCAL_ROOT / local_sub
        if not directory.exists():
            continue
        for path in directory.glob("*.md"):
            stat = path.stat()
            relpath = path.relative_to(LOCAL_ROOT).as_posix()
            files[relpath] = FileInfo(relpath, sha256(path), stat.st_size, stat.st_mtime)

    notes_dir = LOCAL_ROOT / "desk" / "notes"
    if notes_dir.exists():
        for path in notes_dir.glob("navigator-*.md"):
            stat = path.stat()
            relpath = path.relative_to(LOCAL_ROOT).as_posix()
            files[relpath] = FileInfo(relpath, sha256(path), stat.st_size, stat.st_mtime)
    return files


def collect_remote(remote: str) -> dict[str, FileInfo]:
    path_map_json = json.dumps(list(PATH_MAP))
    remote_script = f"""
from pathlib import Path
import hashlib, json

root = Path({REMOTE_PRACTICE_ROOT!r})
path_map = json.loads({path_map_json!r})

def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

rows = []
for remote_sub, local_sub in path_map:
    directory = root / remote_sub
    if not directory.exists():
        continue
    for path in directory.glob("*.md"):
        stat = path.stat()
        relpath = f"{{local_sub}}/" + path.name
        rows.append({{"relpath": relpath, "sha256": sha256(path), "size": stat.st_size, "mtime": stat.st_mtime}})

notes = root / "state" / "notes"
if notes.exists():
    for path in notes.glob("navigator-*.md"):
        stat = path.stat()
        relpath = f"desk/notes/{{path.name}}"
        rows.append({{"relpath": relpath, "sha256": sha256(path), "size": stat.st_size, "mtime": stat.st_mtime}})

print(json.dumps(rows))
"""
    proc = subprocess.run(
        ["ssh", "-o", "ConnectTimeout=8", remote, "python3", "-"],
        input=remote_script,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "ssh failed")

    rows = json.loads(proc.stdout)
    return {
        row["relpath"]: FileInfo(row["relpath"], row["sha256"], row["size"], row["mtime"])
        for row in rows
    }


def cutoff_timestamp(days: int) -> float:
    import time

    return time.time() - days * 86400


def backfill_missing(remote: str, missing: list[str]) -> None:
    for relpath in missing:
        if relpath.startswith("../") or relpath.startswith("/"):
            raise ValueError(f"unsafe remote path: {relpath}")

        local_path = LOCAL_ROOT / relpath
        if local_path.exists():
            print(f"SKIP existing {relpath}")
            continue

        local_path.parent.mkdir(parents=True, exist_ok=True)

        if relpath.startswith("desk/sessions/"):
            remote_rel = "sessions/" + Path(relpath).name
        elif relpath.startswith("desk/proposals/"):
            remote_rel = "proposals/" + Path(relpath).name
        elif relpath.startswith("desk/notes/"):
            remote_rel = "state/notes/" + Path(relpath).name
        else:
            raise ValueError(f"unknown mapped path: {relpath}")

        remote_path = f"{remote}:{REMOTE_PRACTICE_ROOT}/{remote_rel}"
        subprocess.run(["scp", "-q", remote_path, str(local_path)], check=True)
        print(f"COPIED {relpath}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    remote_default = default_remote()
    parser.add_argument("--remote", default=remote_default, help=f"SSH target (default: {remote_default})")
    parser.add_argument("--days", type=int, default=7, help="Compare recent session/proposal files by mtime")
    parser.add_argument(
        "--backfill-missing",
        action="store_true",
        help="Copy remote-only files locally; never overwrite existing local files",
    )
    args = parser.parse_args()

    try:
        local = collect_local()
        remote = collect_remote(args.remote)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    cutoff = cutoff_timestamp(args.days)

    def is_recent(info: FileInfo) -> bool:
        return info.mtime >= cutoff

    def should_report(path: str) -> bool:
        local_info = local.get(path)
        remote_info = remote.get(path)
        return any(info and is_recent(info) for info in (local_info, remote_info))

    remote_only = sorted(path for path in set(remote) - set(local) if should_report(path))
    local_only = sorted(path for path in set(local) - set(remote) if should_report(path))
    mismatched = sorted(
        path
        for path in set(local) & set(remote)
        if local[path].sha256 != remote[path].sha256 and should_report(path)
    )

    print("Turtle practice root consistency")
    print(f"remote: {args.remote}:{REMOTE_PRACTICE_ROOT}")
    print(f"window: {args.days} days for sessions/proposals/notes")
    print()

    if not remote_only and not mismatched:
        if local_only:
            print("OK: no remote drift (local-only = historical Forge copies).")
        else:
            print("OK: local desk outputs match turtleOS practice root.")
        return 0

    if remote_only:
        print("REMOTE-ONLY:")
        for path in remote_only:
            info = remote[path]
            print(f"  {path} {info.sha256[:16]} {info.size} bytes")

    if local_only:
        print("LOCAL-ONLY (informational — Forge history not mirrored on Mini):")
        for path in local_only[:8]:
            info = local[path]
            print(f"  {path} {info.sha256[:16]} {info.size} bytes")
        if len(local_only) > 8:
            print(f"  ... and {len(local_only) - 8} more")

    if mismatched:
        print("MISMATCHED:")
        for path in mismatched:
            print(f"  {path} local={local[path].sha256[:16]} remote={remote[path].sha256[:16]}")

    if args.backfill_missing and remote_only:
        print()
        backfill_missing(args.remote, remote_only)

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
