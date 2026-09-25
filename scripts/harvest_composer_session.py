#!/usr/bin/env python3
"""Harvest one Cursor Composer session into an eddy-shaped note on the Mini.

Composer is the pre-Agent book: global ``state.vscdb``, headers plus bubbles.
Chat is transport. The note is the harvest. Notes live at Mini
``story/composer/`` (own git, sibling of ``story/forge/``). They must not
enter Magic or turtleOS git.

    python3 scripts/harvest_composer_session.py --self-test
    python3 scripts/harvest_composer_session.py --print-transcript --session <id>
    python3 scripts/harvest_composer_session.py --session <id> --held-file held.md --write-remote
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

# Same note contract as the Forge harvest. Import, don't fork the floor.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from harvest_forge_session import (  # noqa: E402
    Turn,
    Transcript,
    compose_note,
    default_remote,
    harvest_or_refuse,
    note_filename,
    valid_note,
)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = (
    Path.home()
    / "Library/Application Support/Cursor/User/globalStorage/state.vscdb"
)
USER = 1
ASSISTANT = 2


def default_notes_dest() -> str:
    if env := os.environ.get("COMPOSER_NOTES_DEST"):
        return env
    from harvest_forge_session import default_notes_dest as forge_dest

    return forge_dest().rsplit("/", 1)[0] + "/composer"


def _open_db(path: Path) -> sqlite3.Connection:
    if not path.is_file():
        raise FileNotFoundError(f"no Composer db: {path}")
    return sqlite3.connect(f"file:{path}?mode=ro", uri=True)


def _load_json(value: object) -> dict:
    if isinstance(value, bytes):
        value = value.decode()
    if isinstance(value, str):
        return json.loads(value)
    raise TypeError("composer row is not json")


def composer_payload(session_id: str, db: Path = DEFAULT_DB) -> tuple[dict, dict[str, dict]]:
    """Return (composerData, bubbles_by_id). Missing bubbles are omitted."""
    con = _open_db(db)
    try:
        row = con.execute(
            "SELECT value FROM cursorDiskKV WHERE key=?",
            (f"composerData:{session_id}",),
        ).fetchone()
        if not row:
            raise FileNotFoundError(f"no composerData:{session_id}")
        data = _load_json(row[0])
        bubbles: dict[str, dict] = {}
        for header in data.get("fullConversationHeadersOnly") or []:
            if not isinstance(header, dict):
                continue
            bid = header.get("bubbleId")
            if not bid:
                continue
            found = con.execute(
                "SELECT value FROM cursorDiskKV WHERE key=?",
                (f"bubbleId:{session_id}:{bid}",),
            ).fetchone()
            if not found:
                continue
            bubbles[str(bid)] = _load_json(found[0])
        return data, bubbles
    finally:
        con.close()


def transcript_from_payload(
    session_id: str,
    data: dict,
    bubbles: dict[str, dict],
) -> Transcript:
    transcript = Transcript(session_id=session_id)
    created = data.get("createdAt")
    if isinstance(created, (int, float)):
        ts = created / 1000 if created > 1e12 else created
        transcript.occurred_at = datetime.fromtimestamp(ts, tz=timezone.utc)
    for header in data.get("fullConversationHeadersOnly") or []:
        if not isinstance(header, dict):
            continue
        typ = header.get("type")
        bid = header.get("bubbleId")
        if typ not in (USER, ASSISTANT) or not bid:
            continue
        bubble = bubbles.get(str(bid)) or {}
        text = (bubble.get("text") or "").strip()
        if not text:
            continue
        role = "user" if typ == USER else "assistant"
        transcript.turns.append(Turn(role=role, text=text))
    return transcript


def transcript_from_db(session_id: str, db: Path = DEFAULT_DB) -> Transcript:
    data, bubbles = composer_payload(session_id, db)
    return transcript_from_payload(session_id, data, bubbles)


def write_remote(note_text: str, filename: str, remote: str, dest: str) -> None:
    if not valid_note(note_text):
        raise SystemExit("refusing to write an invalid note")
    import subprocess

    subprocess.run(
        ["ssh", "-o", "ConnectTimeout=8", remote, f"mkdir -p '{dest}'"],
        check=True,
    )
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False) as tmp:
        tmp.write(note_text)
        tmp_path = tmp.name
    try:
        subprocess.run(["scp", "-q", tmp_path, f"{remote}:{dest}/{filename}"], check=True)
    finally:
        os.unlink(tmp_path)
    quoted = filename.replace("'", "'\\''")
    subprocess.run(
        ["ssh", "-o", "ConnectTimeout=8", remote, f"DEST='{dest}' FILE='{quoted}' bash -s"],
        input=r"""
set -euo pipefail
cd "$DEST"
if [ ! -f README.md ]; then
  cat > README.md <<'MD'
# Composer session notes

Harvest from Cursor Composer (pre-Agent and alongside). Same class as Forge notes.
The sqlite stays on the laptop. This tree is the judgment, not the dump.
Not a Magic path. Not public.
MD
fi
if [ ! -d .git ]; then
  git init -b main
fi
git add README.md "$FILE"
if git diff --cached --quiet; then
  echo "composer notes: tree unchanged"
else
  GIT_AUTHOR_NAME=Kermit GIT_AUTHOR_EMAIL=kermit@local \
  GIT_COMMITTER_NAME=Kermit GIT_COMMITTER_EMAIL=kermit@local \
    git commit -m "harvest: $FILE"
  echo "composer notes: committed $(git rev-parse --short HEAD)"
fi
""",
        text=True,
        check=True,
    )


def _fixture_payload(empty: bool = False) -> tuple[str, dict, dict[str, dict]]:
    sid = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
    if empty:
        data = {
            "composerId": sid,
            "createdAt": 1756970000000,
            "name": "empty fixture",
            "fullConversationHeadersOnly": [],
        }
        return sid, data, {}
    user_id = "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb"
    asst_id = "cccccccc-cccc-cccc-cccc-cccccccccccc"
    tool_id = "dddddddd-dddd-dddd-dddd-dddddddddddd"
    data = {
        "composerId": sid,
        "createdAt": 1756972102862,
        "name": "Discuss base spirit rules",
        "fullConversationHeadersOnly": [
            {"bubbleId": user_id, "type": USER},
            {"bubbleId": tool_id, "type": ASSISTANT},
            {"bubbleId": asst_id, "type": ASSISTANT},
        ],
    }
    bubbles = {
        user_id: {"type": USER, "text": "The spec should be the ground truth."},
        tool_id: {"type": ASSISTANT, "text": "", "capabilityType": 15},
        asst_id: {
            "type": ASSISTANT,
            "text": "I will treat the spec as the source of truth.",
        },
    }
    return sid, data, bubbles


def self_test() -> int:
    failures: list[str] = []
    sid, data, bubbles = _fixture_payload()
    transcript = transcript_from_payload(sid, data, bubbles)
    if [t.role for t in transcript.turns] != ["user", "assistant"]:
        failures.append(f"roles: {[t.role for t in transcript.turns]}")
    if any(not t.text or "capabilityType" in t.text for t in transcript.turns):
        failures.append("tool bubble leaked into prose")
    if transcript.turns[0].text != "The spec should be the ground truth.":
        failures.append(f"user text wrong: {transcript.turns[0].text!r}")
    if transcript.occurred_at is None or transcript.occurred_at.year != 2025:
        failures.append(f"session time wrong: {transcript.occurred_at}")

    held = (
        "This conversation held a fixture question about the spec. "
        "Spirit answered that the spec is the source of truth."
    )
    note = compose_note(
        session_id=sid,
        title="base spirit rules fixture",
        held=held,
        occurred_at=transcript.occurred_at or datetime.now(timezone.utc),
    )
    if not valid_note(note):
        failures.append("fixture note failed valid_note")
    if "2025-09-04T" not in note:
        failures.append(f"note not dated with session time: {note[:200]}")

    empty_sid, empty_data, empty_bubbles = _fixture_payload(empty=True)
    empty = transcript_from_payload(empty_sid, empty_data, empty_bubbles)
    if empty.turns:
        failures.append("empty payload produced turns")
    try:
        harvest_or_refuse(empty, held=held, title="should fail")
        failures.append("empty payload produced a note")
    except ValueError:
        pass
    try:
        harvest_or_refuse(transcript, held="too short", title="x")
        failures.append("short held passed the quality floor")
    except ValueError:
        pass
    if valid_note("not a note"):
        failures.append("valid_note accepted garbage (positive control failed)")

    dest = default_notes_dest()
    if not dest.endswith("/composer"):
        failures.append(f"composer dest does not end in /composer: {dest}")

    if failures:
        for line in failures:
            print(f"SELF-TEST FAIL: {line}")
        return 1
    print("PASS: Composer fixture yields a dated note; empty and short held refuse")
    return 0


def _load_held(args: argparse.Namespace) -> str:
    if args.held_file:
        return Path(args.held_file).read_text(encoding="utf-8")
    if args.held is not None:
        return args.held
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise SystemExit("pass --held, --held-file, or pipe the held section on stdin")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--session", help="Composer parent chat id")
    parser.add_argument("--db", default=None, help="state.vscdb path (tests / one-offs)")
    parser.add_argument("--title", default=None)
    parser.add_argument("--held", default=None)
    parser.add_argument("--held-file", default=None)
    parser.add_argument("--print-transcript", action="store_true")
    parser.add_argument("--write-remote", action="store_true")
    parser.add_argument("--out", help="local path (never a Magic story/composer/)")
    parser.add_argument("--remote", default=None)
    parser.add_argument("--dest", default=None)
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    if not args.session:
        raise SystemExit("need --session")

    db = Path(args.db) if args.db else DEFAULT_DB
    data, bubbles = composer_payload(args.session, db)
    transcript = transcript_from_payload(args.session, data, bubbles)
    if args.print_transcript:
        print(transcript.prose())
        if transcript.occurred_at:
            print(f"\n# occurred_at {transcript.occurred_at.isoformat(timespec='seconds')}")
        print(f"# turns {len(transcript.turns)}")
        print(f"# title {data.get('name') or '(untitled)'}")
        return 0

    title = (args.title or "").strip() or data.get("name") or "composer session"
    try:
        note = harvest_or_refuse(transcript, held=_load_held(args), title=title)
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1

    filename = note_filename(args.session, title)
    if args.out:
        out = Path(args.out)
        posix = out.as_posix()
        if "story/composer" in posix and ROOT in out.resolve().parents:
            print("FAIL: refusing to write a Mini-pipe note into the Magic tree")
            return 1
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(note, encoding="utf-8")
        print(f"wrote {out}")
    if args.write_remote:
        write_remote(
            note,
            filename,
            args.remote or default_remote(),
            args.dest or default_notes_dest(),
        )
    if not args.out and not args.write_remote:
        sys.stdout.write(note)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
