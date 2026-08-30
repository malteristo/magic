#!/usr/bin/env python3
"""Project the turtleOS development record onto the Mini, for craft-turtle.

Why this exists
---------------
`sync_practice_root.sh` is pull-only by design — "Magic stays on Forge;
turtleOS is sovereign." That principle is about the *practice*: the compass,
health, relationships, the family. None of that should land on a machine that
hosts other practitioners' rivers.

But the turtleOS development record is not that. It is the backlog of a piece
of software, and craft-turtle cannot help think about what to build next while
it is the only participant who cannot see what is open. This script is the
narrow, deliberate exception: **the development record crosses; nothing else
does.**

Selection, not mirror
---------------------
The source is `desk/craft/backlog.md` and nothing else. Briefings and bright
interleave turtleOS with family, health, and relational material, so they are
not sources here and must not become sources later — a digest is a thing you
choose line by line, and the moment it becomes a directory copy this file has
failed.

The destination is the operator's own practice root, operator-only on the
artifact viewer. It is not a public surface, and `--check` refuses to export if
the digest picks up a heading it does not recognise.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKLOG = ROOT / "desk" / "craft" / "backlog.md"

REMOTE_DEFAULT = None  # resolved from connections.md; no tracked instance
from workshop_paths import config_file

CONNECTIONS_PATH = config_file("connections.md", ROOT)


def practice_root() -> str:
    """The Mini-side practice root, from the gitignored config.

    Was the literal ``/Users/turtle/workshops/kermit`` in tracked source until
    2026-08-07 — an absolute path carrying the host account *and* the Mage's
    handle, in a script that ships to a public repo. Instance facts live in
    ``connections.md``; resolved lazily so ``--help`` works without it.
    """
    if CONNECTIONS_PATH.is_file():
        found = re.search(
            r"(/(?:Users|home)/[^/\s`]+/workshops/[^\s`]+)",
            CONNECTIONS_PATH.read_text(encoding="utf-8"),
        )
        if found:
            return found.group(1).rstrip("/")
    raise SystemExit(
        "No Turtle practice root configured. Put the Mini-side "
        "`/Users/<account>/workshops/<key>` path in "
        "desk/config/connections.md."
    )
# `craft/backlog.md` on the Mini is the *intake* backlog the reconciler owns.
# This is a different file on purpose — overwriting that one would destroy the
# record of which Mage reports have reached the workshop.
REMOTE_REL = "craft/development.md"

_ITEM_RE = re.compile(r"^- \[(?P<mark>[ x])\] \[(?P<id>[^\]]+)\] (?P<body>.*)$")
_UNTAGGED_RE = re.compile(r"^- \[(?P<id>[^\]]+)\] (?P<body>.*)$")

SHIPPED_SUMMARY_CHARS = 240


class Item:
    def __init__(self, item_id: str, body: str, shipped: bool) -> None:
        self.id = item_id
        self.body = body
        self.shipped = shipped
        self.continuations: list[str] = []

    @property
    def title(self) -> str:
        m = re.match(r"\*\*(?P<t>.+?)\*\*", self.body)
        return m.group("t") if m else self.body[:80]

    def summary(self, limit: int) -> str:
        """Title plus enough prose to know what the thing was."""
        rest = self.body[len(f"**{self.title}**"):].lstrip(" —-–")
        rest = re.sub(r"\s+", " ", rest).strip()
        if len(rest) > limit:
            rest = rest[:limit].rsplit(" ", 1)[0] + "…"
        return f"**{self.title}** — {rest}" if rest else f"**{self.title}**"

    def full(self) -> str:
        lines = [f"- [{self.id}] {self.body}"]
        lines.extend(self.continuations)
        return "\n".join(lines)


def parse_backlog(text: str) -> tuple[list[Item], list[str]]:
    """Return (items, unrecognised-headings).

    Unrecognised headings are the guard: the backlog grows sections over time,
    and a new one may carry material that should not cross. Rather than
    silently exporting whatever appears, the export names what it did not
    expect and lets a human decide.
    """
    # Matched by prefix rather than exact text, deliberately: one heading names
    # a practitioner, and embedding it here would write a real person's name
    # into a tracked script for the sake of a string compare. Prefixes are
    # specific enough to catch a genuinely new section, which is the job.
    known_heading_prefixes = (
        "# Craft Backlog",
        "## Open",
        "## UX research track",
        "## Resolved",
    )
    items: list[Item] = []
    unknown: list[str] = []
    current: Item | None = None
    in_open = False

    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("#"):
            if not line.startswith(known_heading_prefixes):
                unknown.append(line)
            in_open = line == "## Open"
            current = None
            continue
        if not in_open:
            continue

        m = _ITEM_RE.match(line)
        if m:
            current = Item(m.group("id"), m.group("body"), m.group("mark") == "x")
            items.append(current)
            continue
        m = _UNTAGGED_RE.match(line)
        if m:
            current = Item(m.group("id"), m.group("body"), False)
            items.append(current)
            continue
        if current is not None and line.startswith("  "):
            current.continuations.append(line)

    return items, unknown


HEADER = """# turtleOS — Development Digest

> Projected from the workshop backlog on {today}. **Read-only here**: editing
> this file changes nothing, because the worked copy lives in Magic. To change
> something, say so in an eddy — that is what travels back.

This is what is open and what has shipped on turtleOS, so a conversation about
what to build next can start from the real state rather than from memory.

## Moving an item

Say it in a craft-turtle eddy. The intake path carries it to the workshop with
the surrounding conversation attached, which is more context than a form would
have captured. *(A file-based `craft/moves/` channel existed from 2026-08-06 to
2026-08-12 and recorded nothing in six days, while the same span produced five
intakes — the traffic was never missing, it was in the eddies all along.)*

What is worth saying, whether or not you say it in this order:

- **item** — the id from below, or that it is not on the list yet
- **move** — push it forward, refine what it should be, retire it, or split it
- **what should exist** — in terms of what a member would experience
- **why** — what it is for
- **how we would know it worked** — the observable difference

That is deliberately the shape of a specification someone else can build from,
because that is usually who builds it.
"""


def render(items: list[Item], today: str) -> str:
    open_items = [i for i in items if not i.shipped]
    shipped = [i for i in items if i.shipped]

    out = [HEADER.format(today=today), ""]
    out.append(f"## Open ({len(open_items)})")
    out.append("")
    out.append("*Full text — this is the material for deciding what to push forward.*")
    out.append("")
    for item in open_items:
        out.append(item.full())
    out.append("")
    out.append(f"## Shipped ({len(shipped)})")
    out.append("")
    out.append(
        "*Compressed. Here so a proposal does not re-propose something that "
        "already exists — ask for the detail on any of these and it can be read "
        "from the code and the chapter docs.*"
    )
    out.append("")
    for item in shipped:
        out.append(f"- [{item.id}] {item.summary(SHIPPED_SUMMARY_CHARS)}")
    out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="render and validate, do not push")
    ap.add_argument("--out", help="write the digest locally to this path as well")
    ap.add_argument("--remote", default=None, help="override turtle@host")
    args = ap.parse_args()

    if not BACKLOG.is_file():
        print(f"No backlog at {BACKLOG}", file=sys.stderr)
        return 1

    items, unknown = parse_backlog(BACKLOG.read_text(encoding="utf-8"))
    if unknown:
        print("Unrecognised backlog headings — refusing to export:", file=sys.stderr)
        for heading in unknown:
            print(f"  {heading}", file=sys.stderr)
        print(
            "A new section may carry material that should not cross to the Mini.\n"
            "Add it to known_headings in this script once you have read it.",
            file=sys.stderr,
        )
        return 2

    if not items:
        print("Backlog parsed to zero items — refusing to export an empty digest.", file=sys.stderr)
        return 2

    today = date.today().isoformat()
    digest = render(items, today)
    open_n = sum(1 for i in items if not i.shipped)

    if args.out:
        Path(args.out).write_text(digest, encoding="utf-8")

    if args.check:
        print(f"OK: {len(items)} items ({open_n} open), {len(digest)} chars. Not pushed.")
        return 0

    remote = args.remote or _remote_from_connections() or REMOTE_DEFAULT
    tmp = ROOT / ".craft-digest.tmp.md"
    tmp.write_text(digest, encoding="utf-8")
    try:
        subprocess.run(
            ["ssh", remote, f"mkdir -p {practice_root()}/craft"],
            check=True,
        )
        subprocess.run(
            ["rsync", "-az", str(tmp), f"{remote}:{practice_root()}/{REMOTE_REL}"],
            check=True,
        )
    finally:
        tmp.unlink(missing_ok=True)

    print(f"Pushed {open_n} open / {len(items) - open_n} shipped → {remote}:{practice_root()}/{REMOTE_REL}")
    return 0


def _remote_from_connections() -> str | None:
    cfg = config_file("connections.md", ROOT)
    if not cfg.is_file():
        return None
    m = re.search(r"turtle@[^\s`]+", cfg.read_text(encoding="utf-8"))
    return m.group(0) if m else None


if __name__ == "__main__":
    raise SystemExit(main())
