#!/usr/bin/env python3
"""Compare high-value local practice state with Turtle's workshop mirror.

Default mode is report-only. Use --backfill-missing to copy files that exist on
Turtle but do not exist locally. Existing local files are never overwritten.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_REMOTE = os.environ.get("TURTLE_SSH_TARGET", "turtle@turtles-mac-mini")
REMOTE_ROOT = "/Users/turtle/workshop"
LOCAL_ROOT = Path(__file__).resolve().parents[1]

WATCHED_FILES = ("desk/boom.md", "floor/briefings/latest.md")
WATCHED_DIRS = ("desk/sessions", "desk/proposals")


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

    for relpath in WATCHED_FILES:
        path = LOCAL_ROOT / relpath
        if path.exists():
            stat = path.stat()
            files[relpath] = FileInfo(relpath, sha256(path), stat.st_size, stat.st_mtime)

    for rel_dir in WATCHED_DIRS:
        directory = LOCAL_ROOT / rel_dir
        if not directory.exists():
            continue
        for path in directory.glob("*.md"):
            stat = path.stat()
            relpath = path.relative_to(LOCAL_ROOT).as_posix()
            files[relpath] = FileInfo(relpath, sha256(path), stat.st_size, stat.st_mtime)

    return files


def collect_remote(remote: str) -> dict[str, FileInfo]:
    remote_script = r"""
from pathlib import Path
import hashlib, json, sys

root = Path(sys.argv[1])
watched_files = ("desk/boom.md", "floor/briefings/latest.md")
watched_dirs = ("desk/sessions", "desk/proposals")

def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

rows = []
for relpath in watched_files:
    path = root / relpath
    if path.exists():
        stat = path.stat()
        rows.append({"relpath": relpath, "sha256": sha256(path), "size": stat.st_size, "mtime": stat.st_mtime})

for rel_dir in watched_dirs:
    directory = root / rel_dir
    if not directory.exists():
        continue
    for path in directory.glob("*.md"):
        stat = path.stat()
        relpath = path.relative_to(root).as_posix()
        rows.append({"relpath": relpath, "sha256": sha256(path), "size": stat.st_size, "mtime": stat.st_mtime})

print(json.dumps(rows))
"""
    proc = subprocess.run(
        ["ssh", "-o", "ConnectTimeout=8", remote, "python3", "-", REMOTE_ROOT],
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
        remote_path = f"{remote}:{REMOTE_ROOT}/{relpath}"
        subprocess.run(["scp", "-q", remote_path, str(local_path)], check=True)
        print(f"COPIED {relpath}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--remote", default=DEFAULT_REMOTE, help=f"SSH target (default: {DEFAULT_REMOTE})")
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
        if path in WATCHED_FILES:
            return True
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

    print("Turtle state consistency")
    print(f"remote: {args.remote}:{REMOTE_ROOT}")
    print(f"window: {args.days} days for sessions/proposals")
    print()

    if not remote_only and not local_only and not mismatched:
        print("OK: local and Turtle high-value state match.")
        return 0

    if remote_only:
        print("REMOTE-ONLY:")
        for path in remote_only:
            info = remote[path]
            print(f"  {path} {info.sha256[:16]} {info.size} bytes")

    if local_only:
        print("LOCAL-ONLY:")
        for path in local_only:
            info = local[path]
            print(f"  {path} {info.sha256[:16]} {info.size} bytes")

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
