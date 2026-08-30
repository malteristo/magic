#!/usr/bin/env python3
"""Close the loop on craft intake — mark on the Mini what the workshop harvested.

Craft Turtle appends friction to ``craft/backlog.md`` in the practice root when
the Mage forwards something to the craft surface. Spirit harvests it at chapter
start by copying the item into ``desk/craft/backlog.md`` and working it there.

Nothing ever marked the Mini side. So the harvest ran one direction and the
remote list only ever grew: on 2026-08-02 it showed four items as Open, two of
which were shipped and checked off locally the same morning. A queue that cannot
be drained stops being read, which is how the item from 2026-07-09 got to be
three weeks old without anyone deciding anything about it.

The rule is mechanical, so this is a script and not a judgment call: **an intake
id that appears in the local backlog has been harvested.** Whether the work is
done is a separate question, tracked locally where the work is; what the remote
list answers is only "did this reach the workshop", and the answer is yes.

Usage:
    python3 scripts/harvest_craft_intake.py            # report only
    python3 scripts/harvest_craft_intake.py --apply    # write the marks
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCAL_BACKLOG = ROOT / "desk" / "craft" / "backlog.md"
REMOTE_BACKLOG = "~/workshops/kermit/craft/backlog.md"

# Intake ids look like 2026-08-02-some-slug-abc123, always inside brackets.
ID_RE = re.compile(r"\[(\d{4}-\d{2}-\d{2}-[a-z0-9-]+)\]")


def remote_host() -> str:
    """The Mini's address lives in the gitignored config, never in a tracked
    file — same rule and same source as ``scripts/sync_practice_root.sh``."""
    import os
    import re

    override = os.environ.get("REMOTE")
    if override:
        return override
    from workshop_paths import config_file

    conf = config_file("connections.md", ROOT)
    if conf.is_file():
        found = re.search(r"turtle@[^\s`]+", conf.read_text(encoding="utf-8"))
        if found:
            return found.group(0)
    # No hardcoded instance. The docstring above states the rule — the Mini's
    # address lives in the gitignored config, never in a tracked file — and a
    # literal fallback three lines below it broke that rule quietly for weeks.
    # It also ships the author's hostname to a public repo and points every
    # other practitioner at a machine they do not own. Fail loudly instead.
    raise SystemExit(
        "No Turtle remote configured. Put a `turtle@<host>` line in "
        "desk/config/connections.md, or pass --remote."
    )


REMOTE = remote_host()


def ssh(script: str) -> tuple[int, str]:
    proc = subprocess.run(
        ["ssh", "-o", "ConnectTimeout=8", REMOTE, script],
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    return proc.returncode, proc.stdout


def local_ids() -> set[str]:
    if not LOCAL_BACKLOG.is_file():
        return set()
    return set(ID_RE.findall(LOCAL_BACKLOG.read_text(encoding="utf-8")))


def mark(text: str, harvested: set[str]) -> tuple[str, list[str]]:
    """Tick every unticked bullet whose id is in ``harvested``. Returns the new
    text and the ids marked. Lines that are already ``- [x]`` are untouched, so
    running twice changes nothing."""
    out: list[str] = []
    marked: list[str] = []
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        if stripped.startswith("- [ ]") or (
            stripped.startswith("- [") and not stripped.startswith("- [x]")
        ):
            found = ID_RE.search(line)
            if found and found.group(1) in harvested:
                marked.append(found.group(1))
                indent = line[: len(line) - len(stripped)]
                if stripped.startswith("- [ ]"):
                    line = indent + "- [x]" + stripped[5:]
                else:
                    line = indent + "- [x] " + stripped[2:]
        out.append(line)
    return "".join(out), marked


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write the marks to the Mini")
    args = ap.parse_args(argv)

    harvested = local_ids()
    if not harvested:
        print(f"no intake ids in {LOCAL_BACKLOG.relative_to(ROOT)} — nothing to reconcile")
        return 0

    code, remote_text = ssh(f"cat {REMOTE_BACKLOG} 2>/dev/null")
    if code != 0 or not remote_text.strip():
        print("Mini backlog unreachable or empty — skipping", file=sys.stderr)
        return 0

    updated, marked = mark(remote_text, harvested)
    remote_ids = set(ID_RE.findall(remote_text))
    unharvested = sorted(remote_ids - harvested)

    if not marked:
        print("Mini backlog already reconciled — nothing to mark")
    else:
        print(f"{len(marked)} remote item(s) already harvested locally:")
        for ident in marked:
            print(f"  {ident}")

    if unharvested:
        print(f"\n{len(unharvested)} remote item(s) NOT yet in the workshop backlog:")
        for ident in unharvested:
            print(f"  {ident}")

    if not marked:
        return 0
    if not args.apply:
        print("\n(report only — re-run with --apply to write the marks)")
        return 0

    # Heredoc with a quoted delimiter: the backlog contains backticks and
    # asterisks that an unquoted one would hand to the remote shell.
    payload = updated.replace("\\", "\\\\")
    code, _ = ssh(f"cat > {REMOTE_BACKLOG} <<'TURTLEOS_BACKLOG_EOF'\n{payload}\nTURTLEOS_BACKLOG_EOF")
    if code != 0:
        print("write failed", file=sys.stderr)
        return 1
    print(f"\nmarked {len(marked)} item(s) on the Mini")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
