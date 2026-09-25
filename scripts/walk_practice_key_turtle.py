#!/usr/bin/env python3
"""Overnight Turtle walk: rewrite the practice key, one ground page at a time.

Neither native Discord Turtle nor Craft Turtle. Offline job: gemma4:31b
plus a slice of native soul.md, the question, and the rewrite rule.
See desk/notes/2026-09-06-practice-key.md § How a walk is attuned.

Runs on the Mini (needs turtleos llm). Checkpoints after every page.

    python3 walk_practice_key_turtle.py --root /tmp/practice-walk/full
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, "/Users/turtle/turtleos")
from llm import chat_ollama  # noqa: E402

SOUL_PATH = Path("/Users/turtle/workshops/kermit/character/soul.md")
MODEL = "gemma4:31b"
QUESTION = "What story is Magic telling?"


def system_prompt() -> str:
    soul = SOUL_PATH.read_text(encoding="utf-8")[:3500]
    return f"""{soul}

---

Today is Sunday 6 September 2026. You live on his machine.

The question is: {QUESTION}

You will receive one session at a time, oldest first, from the beginning of Magic through today. After the first, you also get the story you already told. Each time, rewrite the whole story. Do not add a paragraph per session. A later session may overturn what you thought. A thin session may leave the story unchanged — that is your call.

Keep it short (about a page). Plain and warm. Concrete. You may say I. Do not invent a newspaper or a public article. Leave household names and health out.
"""


def load_state(path: Path) -> dict:
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"next": 1, "last_file": None, "updated": None, "chars": 0}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True)
    args = parser.parse_args()
    root = Path(args.root)
    pages = root / "pages"
    state_path = root / "state.json"
    key_path = root / "key.md"
    log_path = root / "walk.log"
    status_path = root / "STATUS"
    files = sorted(pages.glob("*.txt"))
    if not files:
        print("no ground pages", file=sys.stderr)
        return 1
    return asyncio.run(
        walk(files, state_path, key_path, log_path, status_path, root)
    )


async def walk(
    files: list[Path],
    state_path: Path,
    key_path: Path,
    log_path: Path,
    status_path: Path,
    root: Path,
) -> int:
    state = load_state(state_path)
    story = key_path.read_text(encoding="utf-8").strip() if key_path.is_file() else ""
    system = system_prompt()
    total = len(files)
    for i, page_path in enumerate(files, 1):
        if i < state["next"]:
            continue
        page = page_path.read_text(encoding="utf-8")
        if not story:
            user = (
                "This is the first session from the beginning of Magic. "
                "Read it. Then tell the story so far.\n\n"
                f"{page}"
            )
        else:
            user = (
                "Here is the story you told after the previous sessions:\n\n"
                f"{story}\n\n"
                "Here is the next session. Rewrite the whole story.\n\n"
                f"{page}"
            )
        t0 = time.time()
        story = await chat_ollama(
            system,
            [{"role": "user", "content": user}],
            model=MODEL,
            num_ctx=16384,
            think=False,
        )
        story = (story or "").strip()
        elapsed = time.time() - t0
        if len(story) <= 20 or story == "(no response generated)":
            msg = f"FAIL at {i}/{total} {page_path.name}: empty story\n"
            log_path.open("a", encoding="utf-8").write(msg)
            status_path.write_text(msg, encoding="utf-8")
            return 1
        key_path.write_text(story + "\n", encoding="utf-8")
        remaining = total - i
        state = {
            "next": i + 1,
            "last_file": page_path.name,
            "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "chars": len(story),
            "total": total,
        }
        state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
        eta_s = remaining * elapsed
        line = (
            f"{datetime.now().strftime('%H:%M:%S')}  {i}/{total}  "
            f"{page_path.name}  {len(story)}c  {elapsed:.0f}s  "
            f"ETA {eta_s/3600:.1f}h\n"
        )
        log_path.open("a", encoding="utf-8").write(line)
        status_path.write_text(
            f"{i}/{total}  last={page_path.name}  key={len(story)}c  "
            f"last_page={elapsed:.0f}s  ETA~{eta_s/3600:.1f}h  "
            f"{state['updated']}\n",
            encoding="utf-8",
        )
        print(line, end="", flush=True)

    (root / "DONE").write_text(
        f"finished {total} pages\n{datetime.now(timezone.utc).isoformat()}\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
