#!/usr/bin/env python3
"""Which craft eddies have become work — read at `. craft`, before the backlog.

The craft backlog is Spirit's record of what Spirit did. The readiness board is
what the Mage confirmed in a conversation, and it is the surface the arrival
should read first, for the same reason craft intake is read before the briefing:
the agenda comes from what he sent, not from what we last wrote down.

**What a row means.** A `ready` row is an eddy where the Mage pressed confirm on
a target condition — one sentence saying what is true when the work is done.
That sentence is the readiness test: if Spirit can meet it without asking him a
question, the eddy is a session's worth of work. If Spirit cannot, the honest
move is `--refuse` (records the gap on this board) or `--post-gap` (records it
**and** tells the eddy). The board labels which happened, because a refusal
reached two ways described one way is how this surface was wrong before.

**Refusing is a first-class outcome, not an error path.** It is the arrival's own
readiness evaluation, which is separate from his — he decides the conversation
is finished, Spirit decides whether the artifact is actionable, and the two are
allowed to disagree. Nothing is refused silently: the gap is required.

**`--waiting` is not `--refuse`.** A refusal says *this artifact is not
actionable*; a wait says *this artifact is finished and someone is holding it* —
the conversation ended on a question to him, or on a trigger it named. Three of
the five warm craft eddies on the first real triage were waits, and filing them
as refusals would have made the board lie about all three.

Usage:
    python3 scripts/craft_readiness_board.py                 # the board
    python3 scripts/craft_readiness_board.py --refuse ID --gap "..."
    python3 scripts/craft_readiness_board.py --waiting ID --on "practitioner"
    python3 scripts/craft_readiness_board.py --acted ID      # a session took it
    python3 scripts/craft_readiness_board.py --triage        # every eddy, with heat
    python3 scripts/craft_readiness_board.py --read ID       # the conversation
    python3 scripts/craft_readiness_board.py --propose ID --target "..."
    python3 scripts/craft_readiness_board.py --post-gap ID --gap "..."
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCAL_SIDECAR = ROOT / "desk" / "craft" / "prepared_eddies.yaml"
CONNECTIONS = ROOT / "system" / "config" / "connections.md"
REMOTE_SIDECAR = "thread-state/prepared_eddies.yaml"

try:
    import yaml
except ImportError:  # pragma: no cover - environment guard
    print("PyYAML required", file=sys.stderr)
    raise SystemExit(2)


def _remote() -> str:
    import os

    override = os.environ.get("REMOTE")
    if override:
        return override
    if CONNECTIONS.is_file():
        match = re.search(r"turtle@[^\s`]+", CONNECTIONS.read_text(encoding="utf-8"))
        if match:
            return match.group(0)
    raise SystemExit(
        "No Turtle remote configured. Put a `turtle@<host>` line in "
        "system/config/connections.md (gitignored), or set REMOTE."
    )


def _runtime_dir() -> str:
    """The Mini's runtime dir, where the sidecar lives. Read from the remote once."""
    remote = _remote()
    out = subprocess.run(
        ["ssh", remote, "cd /Users/turtle/turtleos && ./venv/bin/python3 -c "
         "'import sys; sys.path.insert(0, \".\"); from mage import get_runtime_dir; "
         "print(get_runtime_dir())'"],
        capture_output=True,
        text=True,
        timeout=60,
    )
    path = (out.stdout or "").strip().splitlines()[-1:] or [""]
    if not path[0]:
        raise SystemExit(f"could not resolve runtime dir on {remote}: {out.stderr.strip()}")
    return path[0]


def _load_rows() -> dict:
    """Readiness rows. Prefer the local copy the pull leaves behind; else SSH."""
    if LOCAL_SIDECAR.is_file():
        data = yaml.safe_load(LOCAL_SIDECAR.read_text(encoding="utf-8")) or {}
    else:
        remote = _remote()
        runtime = _runtime_dir()
        out = subprocess.run(
            ["ssh", remote, f"cat {runtime}/{REMOTE_SIDECAR}"],
            capture_output=True,
            text=True,
            timeout=60,
        )
        data = yaml.safe_load(out.stdout or "") or {}
    rows = data.get("readiness")
    return rows if isinstance(rows, dict) else {}


def _thread_url(thread_id: str) -> str:
    return f"https://discord.com/channels/1479425103954448396/{thread_id}"


def print_board(rows: dict) -> int:
    ready = [(t, e) for t, e in rows.items() if isinstance(e, dict) and e.get("state") == "ready"]
    proposed = [(t, e) for t, e in rows.items() if isinstance(e, dict) and e.get("state") == "proposed"]
    refused = [(t, e) for t, e in rows.items() if isinstance(e, dict) and e.get("state") == "refused"]
    waiting = [(t, e) for t, e in rows.items() if isinstance(e, dict) and e.get("state") == "waiting"]

    if not rows:
        # Distinguish "nothing confirmed" from "the instrument is not reading" —
        # the cold-start lie this practice has now paid for twice.
        print("  No readiness rows at all — either nothing has gone idle in craft")
        print("  since the noticer shipped, or it is not running. Check the log")
        print("  before reading this as 'nothing is ready'.")
        return 0

    if ready:
        print(f"  {len(ready)} eddy(s) READY — target condition confirmed by the Mage:")
        for tid, entry in ready:
            print(f"    - {entry.get('target_condition', '(no condition!)')}")
            history = entry.get("target_history") or []
            if history:
                kept = not any(r.get("kind") == "replace" for r in history)
                print(
                    f"      ({len(history)} revision(s), "
                    f"{'held its direction' if kept else 'changed direction'})"
                )
            print(f"      {_thread_url(tid)}")
    else:
        print("  Nothing confirmed ready.")

    if proposed:
        print(f"  {len(proposed)} proposed, awaiting his confirm (do not plan work against these):")
        for tid, entry in proposed:
            print(f"    - {entry.get('target_condition', '')[:90]}")
    if waiting:
        print(f"  {len(waiting)} waiting — someone is holding it:")
        for tid, entry in waiting:
            if entry.get("spark"):
                print(f"    - ✦ sparked ×{entry.get('spark_count', 1)}: {entry['spark'][:80]}")
            else:
                print(f"    - on {entry.get('waiting_on', '?')} · {_thread_url(tid)}")
    if refused:
        print(f"  {len(refused)} refused:")
        for tid, entry in refused:
            # A refusal is reachable two ways and they are not equivalent, so the
            # render must not describe both the same way — the earlier version of
            # this line said "not posted" about every gap, including posted ones.
            where = "told the eddy" if entry.get("gap_posted_at") else "board only"
            print(f"    - [{where}] {entry.get('gap', '')[:80]}")
    return len(ready)


def _mutate(
    thread_id: str, *, refuse_gap: str | None, acted: bool, waiting_on: str | None = None
) -> None:
    """Apply a transition on the Mini, through the module that owns the rules.

    Deliberately not a local YAML edit. The state machine refuses a refusal with
    no gap and refuses acting on something merely proposed, and re-implementing
    those rules here would be a second copy of a gate — which is how the two
    ledger bugs in this practice both happened.
    """
    remote = _remote()
    if waiting_on is not None:
        call = f'mark_waiting(rt, {thread_id}, on={waiting_on!r}, by="spirit")'
    elif refuse_gap is not None:
        call = f'refuse(rt, {thread_id}, gap={refuse_gap!r}, by="spirit")'
    elif acted:
        call = f"mark_acted(rt, {thread_id})"
    else:
        return
    # Piped on stdin rather than passed as `-c "..."`. The argument form put the
    # script through two levels of shell quoting, so `by="spirit"` arrived as a
    # bare name and every transition died with NameError — and it was invisible
    # because the living verify ran a script *on* the Mini instead of running
    # the command the arrival actually uses. Verify the wrapper, not the thing
    # the wrapper calls.
    script = (
        "import sys; sys.path.insert(0, '.')\n"
        "from mage import get_runtime_dir\n"
        "from core.craft_readiness import refuse, mark_acted, mark_waiting\n"
        "rt = get_runtime_dir()\n"
        f"print({call})\n"
    )
    out = subprocess.run(
        ["ssh", remote, "cd /Users/turtle/turtleos && ./venv/bin/python3 -"],
        input=script,
        capture_output=True,
        text=True,
        timeout=60,
    )
    if out.returncode != 0:
        raise SystemExit(f"transition failed:\n{out.stderr.strip()}")
    print(out.stdout.strip())
    _refresh_local_sidecar(remote)


def _refresh_local_sidecar(remote: str) -> None:
    """Pull the sidecar back after a write, or the board contradicts the write.

    Transitions go over SSH to the Mini, which owns the file; the board prefers
    the local copy the pull left behind. So marking two rows `acted` and then
    printing the board showed both still `ready` until the next arrival — the
    tool reading its own write from a cache that write never touched. Found
    2026-08-18 by doing exactly that.
    """
    try:
        out = subprocess.run(
            ["ssh", remote, f"cat {_runtime_dir()}/{REMOTE_SIDECAR}"],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if out.returncode == 0 and out.stdout.strip():
            LOCAL_SIDECAR.write_text(out.stdout, encoding="utf-8")
    except Exception as exc:  # noqa: BLE001 — the transition already landed
        print(f"  (local board copy not refreshed: {exc}; next pull will)")


INTAKE_PORT = 8742


def _post_to_bot(path: str, payload: dict) -> dict:
    """Call the bot's craft write endpoint over SSH → localhost.

    Spirit cannot type in Discord, and the two candidates for a write path were a
    command the Mage types — the marking act that has now failed twice — and the
    intake server, which already runs inside the bot process holding a live
    client. It is local-only, so the SSH hop *is* the authentication.

    Posting in-process is also what makes the confirm button work: a view the
    running client sends is registered in that client's view store. A component
    posted over REST from here would render a button that does nothing.
    """
    body = json.dumps(payload)
    out = subprocess.run(
        [
            "ssh",
            _remote(),
            f"curl -s -X POST -H 'Content-Type: application/json' "
            f"--data-binary @- http://127.0.0.1:{INTAKE_PORT}{path}",
        ],
        input=body,
        capture_output=True,
        text=True,
        timeout=120,
    )
    raw = (out.stdout or "").strip()
    if not raw:
        raise SystemExit(
            f"no response from the bot's {path} — is the intake server up? "
            f"stderr: {out.stderr.strip()}"
        )
    try:
        return json.loads(raw)
    except ValueError:
        # An HTML error page or an aiohttp text response, not JSON. Show it: the
        # 403/404 text is the actual answer.
        raise SystemExit(f"{path} refused: {raw[:400]}") from None


def _on_mini(args: list[str]) -> str:
    """Delegate to `turtleos/scripts/craft_board.py`, which owns the platform read.

    The registry, the sidecar and the bot token all live on the Mini, and the
    workshop should not grow a second copy of any of them. This is a render, not
    a reimplementation.
    """
    out = subprocess.run(
        ["ssh", _remote(), "cd /Users/turtle/turtleos && ./venv/bin/python3 scripts/craft_board.py "
         + " ".join(args)],
        capture_output=True,
        text=True,
        timeout=180,
    )
    if out.returncode != 0:
        raise SystemExit(f"craft board failed:\n{out.stderr.strip()}")
    return out.stdout


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refuse", metavar="THREAD_ID", help="not actionable — requires --gap")
    parser.add_argument("--gap", help="what is missing; goes back to the eddy")
    parser.add_argument("--acted", metavar="THREAD_ID", help="a session took this eddy")
    parser.add_argument(
        "--waiting",
        metavar="THREAD_ID",
        help="the conversation put the ball in someone's court — see --on",
    )
    parser.add_argument(
        "--on",
        default="practitioner",
        help="'practitioner', or the trigger in the conversation's own words",
    )
    parser.add_argument(
        "--propose",
        metavar="THREAD_ID",
        help="propose readiness and post the confirm into the eddy — requires --target",
    )
    parser.add_argument("--target", help="the target condition: what is true when it is done")
    parser.add_argument("--evidence", default="", help="the phrase in the eddy that says so")
    parser.add_argument(
        "--post-gap",
        metavar="THREAD_ID",
        help="refuse AND tell the eddy — requires --gap",
    )
    parser.add_argument(
        "--spark",
        metavar="THREAD_ID",
        help="post the delta to a buildable target — requires --text",
    )
    parser.add_argument("--text", help="the delta: what would have to be settled")
    parser.add_argument(
        "--revise",
        metavar="THREAD_ID",
        help="sharpen or replace a confirmed target — requires --target; --kind refine|replace",
    )
    parser.add_argument("--kind", default="refine", choices=("refine", "replace"))
    parser.add_argument(
        "--cool",
        metavar="THREAD_ID",
        help="retire an eddy whose work is done — requires --reason. Cool, not dissolve",
    )
    parser.add_argument("--reason", help="why this eddy is done; cite the record that says so")
    parser.add_argument(
        "--triage", action="store_true", help="every craft eddy with its temperature"
    )
    parser.add_argument(
        "--read",
        metavar="THREAD_ID",
        help="the conversation itself — the readiness test needs the thread, not its summary",
    )
    args = parser.parse_args()

    if args.read:
        print(_on_mini(["--read", args.read]))
        return 0
    if args.triage:
        print(_on_mini([]))
        return 0

    if args.spark:
        if not (args.text or "").strip():
            parser.error("--spark requires --text: the delta is the whole point")
        print(_post_to_bot("/craft/spark", {"thread_id": args.spark, "spark": args.text}))
        return 0
    if args.revise:
        if not (args.target or "").strip():
            parser.error("--revise requires --target")
        print(_post_to_bot("/craft/revise", {
            "thread_id": args.revise,
            "target_condition": args.target,
            "kind": args.kind,
        }))
        return 0
    if args.cool:
        if not (args.reason or "").strip():
            parser.error("--cool requires --reason: an eddy retired with no reason is one that was dropped")
        print(_post_to_bot("/craft/cool", {"thread_id": args.cool, "reason": args.reason}))
        return 0
    if args.propose:
        if not (args.target or "").strip():
            parser.error("--propose requires --target: readiness with no target condition is not readiness")
        print(_post_to_bot("/craft/ready", {
            "thread_id": args.propose,
            "target_condition": args.target,
            "evidence": args.evidence,
        }))
        return 0
    if args.post_gap:
        if not (args.gap or "").strip():
            parser.error("--post-gap requires --gap")
        print(_post_to_bot("/craft/gap", {"thread_id": args.post_gap, "gap": args.gap}))
        return 0
    if args.waiting:
        _mutate(args.waiting, refuse_gap=None, acted=False, waiting_on=args.on)
        return 0
    if args.refuse:
        if not (args.gap or "").strip():
            parser.error("--refuse requires --gap: a refusal with no gap is a silence")
        _mutate(args.refuse, refuse_gap=args.gap, acted=False)
        return 0
    if args.acted:
        _mutate(args.acted, refuse_gap=None, acted=True)
        return 0

    print_board(_load_rows())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
