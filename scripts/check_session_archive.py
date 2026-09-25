#!/usr/bin/env python3
"""Session transcripts stay on the Mini personal git, not in Magic.

Two claims, two checks:

1. Boundary (offline, pre-commit): no Cursor/Claude session jsonl is tracked
   in magic or turtleOS.
2. Freshness (needs SSH): the Mini archive has at least as many Forge parent
   chats as this laptop. Run after archive_session_transcripts.sh.

    python3 scripts/check_session_archive.py
    python3 scripts/check_session_archive.py --self-test
    python3 scripts/check_session_archive.py --fresh
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TURTLEOS = ROOT.parent / "turtleos"
FORGE_SRC = Path.home() / ".cursor/projects/Users-kermit-Documents-magic/agent-transcripts"


def _connections() -> Path:
    return ROOT / "desk/config/connections.md"


def default_remote() -> str:
    if env := os.environ.get("REMOTE"):
        return env
    from turtle_remote import reachable_remote_from

    if remote := reachable_remote_from(_connections()):
        return remote
    raise SystemExit(
        "No Turtle remote. Put a turtle@<host> line in desk/config/connections.md."
    )


def default_dest() -> str:
    if env := os.environ.get("SESSIONS_DEST"):
        return env
    path = _connections()
    if path.is_file():
        match = re.search(
            r"(/(?:Users|home)/[^/\s`]+/workshops/[^\s`]+)",
            path.read_text(errors="ignore"),
        )
        if match:
            return match.group(1).rstrip("/") + "/story/sessions"
    raise SystemExit(
        "No practice root. Put the Mini workshops path in desk/config/connections.md."
    )


def _tracked(repo: Path) -> list[str]:
    if not (repo / ".git").exists() and not (repo / ".git").is_file():
        return []
    proc = subprocess.run(
        ["git", "-C", str(repo), "ls-files", "-z"],
        capture_output=True,
        check=True,
    )
    return [p for p in proc.stdout.decode().split("\0") if p]


def why_forbidden(rel: str) -> str | None:
    norm = rel.replace("\\", "/").lower()
    if "agent-transcripts/" in norm:
        return f"Cursor agent transcript tracked: {rel}"
    if "/story/sessions/" in norm or norm.startswith("story/sessions/"):
        return f"session archive tracked in a code repo: {rel}"
    # Mini story/forge/ is the harvest pipe. desk/story/forge/ is the July 17
    # ancestor and stays in Magic. Any other story/forge/ path is a leak.
    if "/story/forge/" in norm or norm.startswith("story/forge/"):
        if not norm.startswith("desk/story/forge/"):
            return f"Mini-copied forge note tracked: {rel}"
    if "/story/composer/" in norm or norm.startswith("story/composer/"):
        return f"Mini-copied composer note tracked: {rel}"
    name = Path(norm).name
    parent = Path(norm).parent.as_posix()
    if name.endswith(".jsonl") and (
        "composer" in parent
        or parent.endswith("/anvil/magic")
        or parent.endswith("/anvil/turtleos")
        or ".claude/projects/" in norm
    ):
        return f"substrate session log tracked: {rel}"
    return None


def findings(paths: list[str]) -> list[str]:
    return [msg for rel in paths if (msg := why_forbidden(rel))]


def scan() -> list[str]:
    hits = findings(_tracked(ROOT))
    if TURTLEOS.is_dir():
        hits.extend(findings(_tracked(TURTLEOS)))
    return hits


def local_parent_count() -> int:
    if not FORGE_SRC.is_dir():
        return 0
    return sum(
        1
        for p in FORGE_SRC.glob("*/*.jsonl")
        if "subagents" not in p.parts
    )


def remote_parent_count(remote: str, dest: str) -> int:
    proc = subprocess.run(
        [
            "ssh",
            "-o",
            "ConnectTimeout=8",
            remote,
            f"find '{dest}/forge' -maxdepth 2 -name '*.jsonl' ! -path '*/subagents/*' | wc -l",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return int(proc.stdout.strip() or "0")


def self_test() -> int:
    failures: list[str] = []
    planted = [
        "agent-transcripts/abc/abc.jsonl",
        "desk/story/sessions/forge/abc/abc.jsonl",
        "story/sessions/anvil/magic/session.jsonl",
        ".claude/projects/-Users-kermit-Documents-magic/x.jsonl",
        "story/forge/c1d6e95b-shared-context.md",
        "library/resonance/story/forge/leaked.md",
        "story/composer/0e365b0d-obsidian.md",
    ]
    clean = [
        "desk/notes/session-ground-truth.md",
        "library/resonance/practice/lore/on_shared_context.md",
        "scripts/archive_session_transcripts.sh",
        "scripts/harvest_forge_session.py",
        "scripts/harvest_composer_session.py",
        "desk/story/eddies/1545755675320131646-health-channel-activities.md",
        "desk/story/forge/2026-07-17-twine-design-chapter.md",
    ]
    missed = [p for p in planted if why_forbidden(p) is None]
    if missed:
        failures.append(f"planted leak not rejected: {missed}")
    false = [p for p in clean if why_forbidden(p) is not None]
    if false:
        failures.append(f"clean path rejected: {false}")
    live = scan()
    if live:
        failures.append(f"live tree already leaking: {live}")
    flow = ROOT / "system/flows/release/cast_release.md"
    if "archive_session_transcripts.sh" not in flow.read_text(encoding="utf-8"):
        failures.append("release flow does not name the archive script (F-80)")
    hook = ROOT / ".githooks/pre-commit"
    hook_text = hook.read_text(encoding="utf-8")
    if "harvest_forge_session.py" not in hook_text:
        failures.append("pre-commit does not run harvest_forge_session.py --self-test")
    if "harvest_composer_session.py" not in hook_text:
        failures.append("pre-commit does not run harvest_composer_session.py --self-test")
    if local_parent_count() == 0:
        failures.append("positive control: Forge transcript dir empty or missing")
    if failures:
        for line in failures:
            print(f"SELF-TEST FAIL: {line}")
        return 1
    print(
        f"PASS: planted session leaks rejected; clean paths and live trees clear; "
        f"{local_parent_count()} local Forge parents"
    )
    return 0


def check_fresh(remote: str, dest: str) -> int:
    local = local_parent_count()
    try:
        remote_n = remote_parent_count(remote, dest)
    except (subprocess.CalledProcessError, ValueError) as exc:
        print(f"SKIP freshness: Mini unreachable ({exc}) — mirror not compared")
        return 0 if (MIRROR / "kermit/story/sessions/.git").is_dir() else 1
    if remote_n < local:
        print(
            f"FAIL: Mini archive has {remote_n} Forge parent chats; "
            f"this laptop has {local}. Run scripts/archive_session_transcripts.sh"
        )
        return 1
    print(f"PASS: Mini archive {remote_n} >= local {local} Forge parent chats")
    return check_mirror(remote, dest)


MIRROR = Path(os.environ.get("MIRROR_DEST", Path.home() / "Backups/turtle-ground"))


def _head(cmd: list[str]) -> str:
    return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout.strip()


def check_mirror(remote: str, dest: str) -> int:
    """The laptop mirror is the only second copy; it must match the Mini's head."""
    local_repo = MIRROR / "kermit/story/sessions"
    if not (local_repo / ".git").is_dir():
        print(f"FAIL: no mirror at {local_repo}. Run scripts/archive_session_transcripts.sh")
        return 1
    mini = _head(["ssh", "-o", "ConnectTimeout=8", remote, f"git -C '{dest}' rev-parse HEAD"])
    here = _head(["git", "-C", str(local_repo), "rev-parse", "HEAD"])
    if mini != here:
        print(f"FAIL: mirror head {here[:8]} != Mini head {mini[:8]}")
        return 1
    health_root = dest.rsplit("/kermit/story/sessions", 1)[0] + "/health-kermit"
    mini_h = int(_head(["ssh", "-o", "ConnectTimeout=8", remote,
                        f"find '{health_root}' -type f | wc -l"]) or 0)
    here_h = sum(1 for p in (MIRROR / "health-kermit").rglob("*") if p.is_file())
    if here_h < mini_h:
        print(f"FAIL: health mirror has {here_h} files; Mini has {mini_h}")
        return 1
    print(f"PASS: laptop mirror matches Mini sessions head {mini[:8]}; health {here_h}/{mini_h} files")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument(
        "--fresh",
        action="store_true",
        help="also compare Forge parent counts against the Mini archive",
    )
    parser.add_argument("--remote", default=None)
    parser.add_argument("--dest", default=None)
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    hits = scan()
    if hits:
        print("FAIL: session transcripts must stay on the Mini, not in these trees")
        for hit in hits:
            print(f"  {hit}")
        return 1
    print("PASS: no session transcripts tracked in magic or turtleos")
    if args.fresh:
        remote = args.remote or default_remote()
        dest = args.dest or default_dest()
        return check_fresh(remote, dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
