#!/usr/bin/env python3
"""Harvest one Forge (Cursor) session into an eddy-shaped note on the Mini.

Chat is transport. The jsonl is ground truth. The note is the harvest.
Notes live at Mini ``story/forge/`` (own git). They must not enter Magic
or turtleOS git — ``desk/story/forge/`` is the July 17 ancestor, not this pipe.

    python3 scripts/harvest_forge_session.py --self-test
    python3 scripts/harvest_forge_session.py --print-transcript --session <id>
    python3 scripts/harvest_forge_session.py --session <id> --held-file held.md --write-remote
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORGE_SRC = Path.home() / ".cursor/projects/Users-kermit-Documents-magic/agent-transcripts"

MIN_HELD_CHARS = 20
TRIGGER = "harvest"

_USER_QUERY_RE = re.compile(r"<user_query>\s*(.*?)\s*</user_query>", re.S)
_TIMESTAMP_RE = re.compile(r"<timestamp>\s*(.*?)\s*</timestamp>", re.S)
_CURSOR_CMD_RE = re.compile(r"<cursor_commands>.*?</cursor_commands>", re.S)
_ENTRY_FRONT_RE = re.compile(r"---\n(.*?)---\n\n", re.S)
_CURSOR_TS_RE = re.compile(
    r"([A-Za-z]+, [A-Za-z]+ \d+, \d{4}, \d{1,2}:\d{2} [AP]M) \((UTC)([+-]\d+)\)"
)
_SLUG_RE = re.compile(r"[^a-z0-9]+")
_INJECTION_PREFIXES = (
    "<dynamic_tools>",
    "<agent_skills>",
    "<open_and_recently_viewed_files>",
    "## Dynamic Tool",
    "## MCP Resource",
    "You have access to tools through dynamic namespaces",
)


@dataclass
class Turn:
    role: str
    text: str


@dataclass
class Transcript:
    session_id: str
    turns: list[Turn] = field(default_factory=list)
    occurred_at: datetime | None = None

    def prose(self) -> str:
        blocks: list[str] = []
        for turn in self.turns:
            label = "Mage" if turn.role == "user" else "Spirit"
            blocks.append(f"{label}: {turn.text}")
        return "\n\n".join(blocks)


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


def default_notes_dest() -> str:
    if env := os.environ.get("FORGE_NOTES_DEST"):
        return env
    path = _connections()
    if path.is_file():
        match = re.search(
            r"(/(?:Users|home)/[^/\s`]+/workshops/[^\s`]+)",
            path.read_text(errors="ignore"),
        )
        if match:
            return match.group(1).rstrip("/") + "/story/forge"
    raise SystemExit(
        "No practice root. Put the Mini workshops path in desk/config/connections.md."
    )


def slug(title: str) -> str:
    s = _SLUG_RE.sub("-", (title or "").strip().lower()).strip("-")
    return s or "session"


def parse_cursor_timestamp(raw: str) -> datetime | None:
    match = _CURSOR_TS_RE.search(raw or "")
    if not match:
        return None
    try:
        dt = datetime.strptime(match.group(1), "%A, %b %d, %Y, %I:%M %p")
    except ValueError:
        return None
    offset_h = int(match.group(3))
    return dt.replace(tzinfo=timezone(timedelta(hours=offset_h)))


def strip_user_envelope(text: str) -> tuple[str, datetime | None]:
    occurred = None
    ts_match = _TIMESTAMP_RE.search(text)
    if ts_match:
        occurred = parse_cursor_timestamp(ts_match.group(1))
    queries = [q.strip() for q in _USER_QUERY_RE.findall(text) if q.strip()]
    if queries:
        return "\n\n".join(queries), occurred
    cleaned = _CURSOR_CMD_RE.sub("", text)
    cleaned = _TIMESTAMP_RE.sub("", cleaned).strip()
    return cleaned, occurred


def _text_items(content: object) -> list[str]:
    if isinstance(content, str):
        return [content] if content.strip() else []
    if not isinstance(content, list):
        return []
    out: list[str] = []
    for item in content:
        if not isinstance(item, dict):
            continue
        if item.get("type") and item.get("type") != "text":
            continue
        text = item.get("text")
        if isinstance(text, str) and text.strip():
            out.append(text)
    return out


def jsonl_path(session_id: str, src: Path = FORGE_SRC) -> Path:
    return src / session_id / f"{session_id}.jsonl"


def transcript_from_jsonl(path: Path, session_id: str | None = None) -> Transcript:
    sid = session_id or path.stem
    transcript = Transcript(session_id=sid)
    if not path.is_file():
        raise FileNotFoundError(f"no jsonl: {path}")
    if path.stat().st_size == 0:
        return transcript
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(record, dict):
                continue
            if record.get("type") == "turn_ended":
                continue
            role = record.get("role")
            if role not in ("user", "assistant"):
                continue
            message = record.get("message") or {}
            content = message.get("content") if isinstance(message, dict) else None
            texts = _text_items(content)
            if not texts:
                continue
            blob = "\n".join(texts).strip()
            occurred = None
            if role == "user":
                blob, occurred = strip_user_envelope(blob)
            if not blob or blob == "[REDACTED]":
                continue
            if role == "user" and blob.lstrip().startswith(_INJECTION_PREFIXES):
                continue
            if occurred and transcript.occurred_at is None:
                transcript.occurred_at = occurred
            transcript.turns.append(Turn(role=role, text=blob))
    if transcript.occurred_at is None and path.exists():
        mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
        transcript.occurred_at = mtime
    return transcript


def compose_note(
    *,
    session_id: str,
    title: str,
    held: str,
    occurred_at: datetime,
) -> str:
    ts = occurred_at.isoformat(timespec="seconds")
    safe_title = title.replace("\n", " ").strip()
    return (
        f"---\n"
        f"thread: '{session_id}'\n"
        f"title: {safe_title}\n"
        f"trigger: {TRIGGER}\n"
        f"timestamp: '{ts}'\n"
        f"related-topics: []\n"
        f"proposed-themes: []\n"
        f"---\n\n"
        f"{held.strip()}\n"
    )


def note_filename(session_id: str, title: str) -> str:
    return f"{session_id}-{slug(title)}.md"


def valid_note(text: str) -> bool:
    """Same floor a later memory reader would need: frontmatter + held body."""
    match = _ENTRY_FRONT_RE.search(text or "")
    if not match:
        return False
    front = match.group(1)
    if "thread:" not in front or "timestamp:" not in front or "trigger:" not in front:
        return False
    body = text[match.end() :].strip()
    if len(body) <= MIN_HELD_CHARS:
        return False
    return True


def write_remote(note_text: str, filename: str, remote: str, dest: str) -> None:
    if not valid_note(note_text):
        raise SystemExit("refusing to write an invalid note")
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
# Forge session notes

Harvest from Cursor agent transcripts. Same class as Discord eddy notes.
Transcripts live in ../sessions/. This tree is the judgment, not the flight recorder.
Not a Magic path. Not public.
MD
fi
if [ ! -d .git ]; then
  git init -b main
fi
git add README.md "$FILE"
if git diff --cached --quiet; then
  echo "forge notes: tree unchanged"
else
  GIT_AUTHOR_NAME=Kermit GIT_AUTHOR_EMAIL=kermit@local \
  GIT_COMMITTER_NAME=Kermit GIT_COMMITTER_EMAIL=kermit@local \
    git commit -m "harvest: $FILE"
  echo "forge notes: committed $(git rev-parse --short HEAD)"
fi
""",
        text=True,
        check=True,
    )


def _fixture_jsonl(empty: bool = False) -> str:
    if empty:
        return ""
    user = (
        "<timestamp>Sunday, Sep 6, 2026, 8:00 AM (UTC+2)</timestamp>\n"
        "<user_query>What is twine?</user_query>\n"
    )
    records = [
        {
            "role": "user",
            "message": {"content": [{"type": "text", "text": user}]},
        },
        {
            "role": "assistant",
            "message": {
                "content": [
                    {"type": "tool_use", "name": "Read", "input": {}},
                    {"type": "text", "text": "Twine is personal context over time."},
                ]
            },
        },
        {
            "role": "user",
            "message": {
                "content": [
                    {
                        "type": "text",
                        "text": "<dynamic_tools>\nYou have access to tools through dynamic namespaces\n",
                    }
                ]
            },
        },
    ]
    return "".join(json.dumps(r) + "\n" for r in records)


def self_test() -> int:
    failures: list[str] = []
    held = (
        "This conversation held a fixture question about twine. "
        "Spirit answered that twine is personal context over time."
    )
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "src"
        sid = "11111111-1111-1111-1111-111111111111"
        jsonl = jsonl_path(sid, src)
        jsonl.parent.mkdir(parents=True)
        jsonl.write_text(_fixture_jsonl(), encoding="utf-8")

        transcript = transcript_from_jsonl(jsonl, sid)
        if not transcript.turns:
            failures.append("fixture jsonl produced no turns")
        if any("tool_use" in t.text or "Read" == t.text for t in transcript.turns):
            failures.append("tool dump leaked into prose")
        if any("<dynamic_tools>" in t.text or "dynamic namespaces" in t.text for t in transcript.turns):
            failures.append("tool-catalog injection leaked into prose")
        if transcript.turns and transcript.turns[0].text != "What is twine?":
            failures.append(f"user envelope not stripped: {transcript.turns[0].text!r}")
        if transcript.occurred_at is None or transcript.occurred_at.hour != 8:
            failures.append(f"session time missing or wrong: {transcript.occurred_at}")

        note = compose_note(
            session_id=sid,
            title="twine fixture",
            held=held,
            occurred_at=transcript.occurred_at or datetime.now(timezone.utc),
        )
        if not valid_note(note):
            failures.append("fixture note failed valid_note")
        if "2026-09-06T08:00:00" not in note:
            failures.append("note not dated with session time")

        again = compose_note(
            session_id=sid,
            title="twine fixture",
            held=held + " A second pass still holds the same chapter.",
            occurred_at=transcript.occurred_at or datetime.now(timezone.utc),
        )
        if not valid_note(again):
            failures.append("rebuild did not produce a valid note")

        empty_path = jsonl_path("empty-session", src)
        empty_path.parent.mkdir(parents=True)
        empty_path.write_text(_fixture_jsonl(empty=True), encoding="utf-8")
        empty = transcript_from_jsonl(empty_path, "empty-session")
        if empty.turns:
            failures.append("empty jsonl produced turns")
        try:
            harvest_or_refuse(empty, held=held, title="should fail")
            failures.append("empty jsonl produced a note")
        except ValueError:
            pass

        try:
            harvest_or_refuse(transcript, held="too short", title="x")
            failures.append("short held passed the quality floor")
        except ValueError:
            pass

        if valid_note("not a note"):
            failures.append("valid_note accepted garbage (positive control failed)")

    if failures:
        for line in failures:
            print(f"SELF-TEST FAIL: {line}")
        return 1
    print("PASS: fixture yields a valid session-dated note; empty and short held refuse")
    return 0


def harvest_or_refuse(transcript: Transcript, *, held: str, title: str) -> str:
    if not transcript.turns:
        raise ValueError("no harvestable turns in jsonl")
    if transcript.occurred_at is None:
        raise ValueError("no session time")
    held = (held or "").strip()
    if len(held) <= MIN_HELD_CHARS:
        raise ValueError("held section failed the quality floor")
    note = compose_note(
        session_id=transcript.session_id,
        title=title,
        held=held,
        occurred_at=transcript.occurred_at,
    )
    if not valid_note(note):
        raise ValueError("composed note failed valid_note")
    return note


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
    parser.add_argument("--session", help="Forge parent chat id")
    parser.add_argument("--jsonl", help="explicit jsonl path (tests / one-offs)")
    parser.add_argument("--title", default=None)
    parser.add_argument("--held", default=None, help="held section text")
    parser.add_argument("--held-file", default=None)
    parser.add_argument("--print-transcript", action="store_true")
    parser.add_argument("--write-remote", action="store_true")
    parser.add_argument("--out", help="write the note to this local path (never a Magic story/forge/)")
    parser.add_argument("--remote", default=None)
    parser.add_argument("--dest", default=None)
    args = parser.parse_args()
    if args.self_test:
        return self_test()

    if args.jsonl:
        path = Path(args.jsonl)
        session_id = args.session or path.stem
    else:
        if not args.session:
            raise SystemExit("need --session or --jsonl")
        path = jsonl_path(args.session)
        session_id = args.session

    transcript = transcript_from_jsonl(path, session_id)
    if args.print_transcript:
        print(transcript.prose())
        if transcript.occurred_at:
            print(f"\n# occurred_at {transcript.occurred_at.isoformat(timespec='seconds')}")
        print(f"# turns {len(transcript.turns)}")
        return 0

    title = (args.title or "").strip() or "forge session"
    try:
        note = harvest_or_refuse(transcript, held=_load_held(args), title=title)
    except ValueError as exc:
        print(f"FAIL: {exc}")
        return 1

    filename = note_filename(session_id, title)
    if args.out:
        out = Path(args.out)
        if "story/forge" in out.as_posix() and "desk/story/forge" not in out.as_posix():
            # Local write is for fixtures and review. The pipe's home is Mini.
            if ROOT in out.resolve().parents or out.resolve() == ROOT:
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
