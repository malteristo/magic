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

LOCAL_ROOT = Path(__file__).resolve().parents[1]
CONNECTIONS_PATH = LOCAL_ROOT / "system" / "config" / "connections.md"


def remote_practice_root() -> str:
    """The Mini-side practice root, from the gitignored config.

    Was the literal ``/Users/turtle/workshops/kermit`` in tracked source until
    2026-08-07 — an absolute path that carries the host account *and* the
    Mage's handle, in a file that ships to a public repo. Same rule as the
    remote address: instance facts live in ``connections.md``.
    """
    if CONNECTIONS_PATH.exists():
        text = CONNECTIONS_PATH.read_text(errors="ignore")
        match = re.search(r"(/(?:Users|home)/[^/\s`]+/workshops/[^\s`]+)", text)
        if match:
            return match.group(1).rstrip("/")
    raise SystemExit(
        "No Turtle practice root configured. Put the Mini-side "
        "`/Users/<account>/workshops/<key>` path in "
        "system/config/connections.md (gitignored)."
    )

# Remote path → local path
PATH_MAP: tuple[tuple[str, str], ...] = (
    ("sessions", "desk/sessions"),
    ("story/daily", "desk/story/daily"),
    ("story/eddies", "desk/story/eddies"),
    ("proposals", "desk/proposals"),
)

# Every path the pull carries, including the ones this script does not compare
# file-by-file. Used only by the unmapped-writer sweep below.
CARRIED: frozenset[str] = frozenset(
    {
        "sessions",
        "story",
        "proposals",
        "craft",
        "state/notes",
        "thread-state",
    }
)

# Deliberately not carried, and why. A path here is a decision; a path in
# neither this map nor CARRIED is the thing the sweep exists to find. Keep the
# reasons — "we decided not to" and "we never got to" look identical in a tree.
NOT_CARRIED: dict[str, str] = {
    "state": "runtime state (current/alive/packets); read in place, too hot to mirror",
    "chronicle": "append-only ledgers; queried on the Mini, not reviewed on Forge",
    "dialogue": "raw transcripts; Discord is the durable copy",
    "thread-archive": "closed-thread bodies; story notes are the reviewed form",
    "readiness": "dimension telemetry; surfaces through the ops report",
    "signals": "act-offer and turn signals; the ledger is the reviewed form",
    "link-resonance": "saved-link derivations; reached through the shelf",
    "character": "attunement files the Mini owns; Forge edits would fight the writer",
    "flows": "flow definitions ship from the turtleOS repo, not back from it",
    "native-runtime": "task/audit state for the host",
    "outfacing": "draft queue; signals reach Forge through desk/outfacing",
    "share": "share staging",
    "campaign": "play-state",
    "box": "practitioner pastes; intake carries what matters",
    "notes": "legacy pre-native location, superseded by state/notes",
    "sessions-archive": "historical",
}


def default_remote() -> str:
    if env_remote := os.environ.get("TURTLE_SSH_TARGET"):
        return env_remote

    if CONNECTIONS_PATH.exists():
        text = CONNECTIONS_PATH.read_text(errors="ignore")
        match = re.search(r"`(turtle@[^`]+)`", text)
        if match:
            return match.group(1)

    # No hardcoded instance. The docstring above states the rule — the Mini's
    # address lives in the gitignored config, never in a tracked file — and a
    # literal fallback three lines below it broke that rule quietly for weeks.
    # It also ships the author's hostname to a public repo and points every
    # other practitioner at a machine they do not own. Fail loudly instead.
    raise SystemExit(
        "No Turtle remote configured. Put a `turtle@<host>` line in "
        "system/config/connections.md (gitignored), or pass --remote."
    )


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
        for path in notes_dir.glob("*.md"):
            stat = path.stat()
            relpath = path.relative_to(LOCAL_ROOT).as_posix()
            files[relpath] = FileInfo(relpath, sha256(path), stat.st_size, stat.st_mtime)
    return files


def collect_remote(remote: str) -> dict[str, FileInfo]:
    path_map_json = json.dumps(list(PATH_MAP))
    remote_script = f"""
from pathlib import Path
import hashlib, json

root = Path({remote_practice_root()!r})
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
    for path in notes.glob("*.md"):
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


def collect_remote_dirs(remote: str, days: int) -> dict[str, float]:
    """Top-level practice-root directories with a file written inside the window.

    The pull is an allowlist: each mapping was added when the writer that fills
    it was built, so a *new* writer produces artifacts no reader collects, and
    nothing says so. That is not hypothetical — `state/notes/` was the save
    tool's destination for months while the pull took one filename prefix from
    it, and the guard globbed the same prefix, so neither could see the nine
    files sitting there. Rewording the mapping table would only ask the next
    builder to remember; this asks the Mini instead.
    """
    remote_script = f"""
from pathlib import Path
import json, time

root = Path({remote_practice_root()!r})
cutoff = time.time() - {days} * 86400
rows = {{}}
for entry in root.iterdir():
    if not entry.is_dir() or entry.name.startswith("."):
        continue
    newest = 0.0
    for path in entry.rglob("*"):
        if path.is_file():
            newest = max(newest, path.stat().st_mtime)
            if newest >= cutoff:
                break
    if newest >= cutoff:
        rows[entry.name] = newest
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
        return {}
    return json.loads(proc.stdout or "{}")


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
        elif relpath.startswith("desk/story/daily/"):
            remote_rel = "story/daily/" + Path(relpath).name
        elif relpath.startswith("desk/story/eddies/"):
            remote_rel = "story/eddies/" + Path(relpath).name
        elif relpath.startswith("desk/proposals/"):
            remote_rel = "proposals/" + Path(relpath).name
        elif relpath.startswith("desk/notes/"):
            remote_rel = "state/notes/" + Path(relpath).name
        else:
            raise ValueError(f"unknown mapped path: {relpath}")

        remote_path = f"{remote}:{remote_practice_root()}/{remote_rel}"
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
        # A note Turtle saved and the workshop never received does not become
        # acceptable by aging: `state/notes/` is where the save tool writes when
        # Turtle tells a practitioner it kept something "for review", so the
        # unharvested case is reported without a window. Everything else keeps
        # one — including local-only notes, since desk/notes/ also holds
        # Forge-authored files that were never on the Mini.
        if path.startswith("desk/notes/") and path in remote and path not in local:
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

    unmapped = sorted(
        name
        for name in collect_remote_dirs(args.remote, args.days)
        if name not in CARRIED and name not in NOT_CARRIED
    )

    print("Turtle practice root consistency")
    print(f"remote: {args.remote}:{remote_practice_root()}")
    print(f"window: {args.days} days for sessions/story/proposals/notes")
    print()

    if not remote_only and not mismatched and not unmapped:
        if local_only:
            print("OK: no remote drift (local-only = historical Forge copies).")
        else:
            print("OK: local desk outputs match turtleOS practice root.")
        return 0

    if unmapped:
        print("UNMAPPED WRITER (active on the Mini, no reader on Forge):")
        for name in unmapped:
            print(f"  {name}/ — carry it in sync_practice_root.sh, or record why not in NOT_CARRIED")
        print()

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
