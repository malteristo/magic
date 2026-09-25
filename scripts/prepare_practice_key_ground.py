#!/usr/bin/env python3
"""Write the ground pages for a full Turtle key walk.

Composer parents from the first Magic day through the day before Agent,
then Forge Agent parents, oldest first. One store per era. Mechanical
cap — identical bytes for any mouth. Pages stay off the Magic tree.

    python3 scripts/prepare_practice_key_ground.py --dest /tmp/practice-walk/full/pages
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from harvest_composer_session import DEFAULT_DB, transcript_from_db
from harvest_forge_session import FORGE_SRC, jsonl_path, transcript_from_jsonl

MAGIC_START = datetime(2025, 9, 3, tzinfo=timezone.utc)
AGENT_START = datetime(2026, 2, 20, tzinfo=timezone.utc)
MAX = 14000
HEAD = 6500
TAIL = 6500
SPIRIT_TRIM = 180


def _dt(ms: object) -> datetime | None:
    if ms is None:
        return None
    if isinstance(ms, str) and ms.isdigit():
        ms = int(ms)
    if not isinstance(ms, (int, float)):
        return None
    return datetime.fromtimestamp(ms / 1000 if ms > 1e12 else ms, tz=timezone.utc)


def composer_ids(db: Path = DEFAULT_DB) -> list[tuple[datetime, str]]:
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        rows = con.execute(
            "SELECT composerId, value FROM composerHeaders WHERE isSubagent=0"
        ).fetchall()
    finally:
        con.close()
    out: list[tuple[datetime, str]] = []
    for cid, val in rows:
        o = json.loads(val if isinstance(val, str) else val.decode())
        dt = _dt(o.get("createdAt"))
        if dt is None or dt < MAGIC_START or dt >= AGENT_START:
            continue
        out.append((dt, cid))
    out.sort()
    return out


def agent_ids(src: Path = FORGE_SRC) -> list[tuple[datetime, str]]:
    out: list[tuple[datetime, str]] = []
    if not src.is_dir():
        return out
    for path in src.glob("*/*.jsonl"):
        if "subagents" in path.parts:
            continue
        sid = path.parent.name
        transcript = transcript_from_jsonl(path, sid)
        dt = transcript.occurred_at or datetime.fromtimestamp(
            path.stat().st_mtime, tz=timezone.utc
        )
        out.append((dt, sid))
    out.sort()
    return out


def cap_prose(transcript) -> tuple[str, str]:
    full = transcript.prose()
    if len(full) <= MAX:
        return full, "full"
    blocks: list[str] = []
    for turn in transcript.turns:
        name = "Mage" if turn.role == "user" else "Spirit"
        body = turn.text
        if turn.role != "user" and len(body) > SPIRIT_TRIM:
            body = body[: SPIRIT_TRIM - 3] + "..."
        blocks.append(f"{name}: {body}")
    mid = "\n\n".join(blocks)
    if len(mid) <= MAX:
        return mid, "spirit-trimmed"
    text = (
        mid[:HEAD]
        + "\n\n--- [same cut for every mouth; middle omitted] ---\n\n"
        + mid[-TAIL:]
    )
    return text, "spirit-trimmed+head-tail"


def write_page(
    dest: Path,
    index: int,
    store: str,
    sid: str,
    dt: datetime,
    transcript,
) -> Path:
    body, how = cap_prose(transcript)
    name = f"{index:04d}-{store}-{sid[:8]}.txt"
    path = dest / name
    header = (
        f"# {store} {sid}\n"
        f"# {dt.isoformat(timespec='seconds')}\n"
        f"# turns {len(transcript.turns)} · ground {how} · {len(body)} chars\n\n"
    )
    path.write_text(header + body + "\n", encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", required=True)
    parser.add_argument("--db", default=None)
    args = parser.parse_args()
    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)
    db = Path(args.db) if args.db else DEFAULT_DB

    composers = composer_ids(db)
    agents = agent_ids()
    manifest = dest.parent / "manifest.tsv"
    lines = ["index\tstore\tid\tdate\tturns\tfile"]
    n = 0
    for dt, cid in composers:
        n += 1
        t = transcript_from_db(cid, db)
        path = write_page(dest, n, "composer", cid, dt, t)
        lines.append(
            f"{n}\tcomposer\t{cid}\t{dt.date()}\t{len(t.turns)}\t{path.name}"
        )
        if n % 50 == 0:
            print(f"composer {n}/{len(composers)}", flush=True)
    print(f"composer done: {len(composers)}", flush=True)
    for dt, sid in agents:
        n += 1
        t = transcript_from_jsonl(jsonl_path(sid), sid)
        path = write_page(dest, n, "agent", sid, dt, t)
        lines.append(
            f"{n}\tagent\t{sid}\t{dt.date()}\t{len(t.turns)}\t{path.name}"
        )
        if (n - len(composers)) % 50 == 0:
            print(f"agent {n - len(composers)}/{len(agents)}", flush=True)
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(
        f"wrote {n} pages ({len(composers)} composer + {len(agents)} agent) → {dest}"
    )
    if n < 600:
        print("FAIL: expected ~669 pages", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
