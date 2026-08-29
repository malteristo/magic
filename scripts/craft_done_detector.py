#!/usr/bin/env python3
"""Which cold craft eddies already produced their outcome — computed, with citations.

`cold` is a residue category. It currently conflates four things: an eddy whose
work shipped, one waiting on the Mage, one that was never developed, and one
that was abandoned. `waiting` got its own state on 2026-08-17. This answers the
first: **has this eddy's outcome landed anywhere in the practice record?**

**It is a join, not a judgement.** An eddy is done when its result exists — a
ticked backlog entry, a harvested prepared surface, a design chapter, a bright
entry. All of those name the thread id, because craft intake has recorded the
origin eddy since July. So this asks a question a grep can answer, and does not
ask a model anything. The Mage named the two obvious cases by eye
(`extract youtube video transcripts`, `searching with an agent search engine`);
the point of a detector is to find the ones nobody would name by eye, and to be
wrong in a way someone can check.

**Every verdict carries its evidence.** A boolean with no citation is the shape
this practice keeps getting burned by — a number that reads as a finding and
cannot be audited. `shipped` here always prints the record that says so.

**Three verdicts, and the middle one matters most.**

``shipped``  a record that is closed names this eddy. Dissolve candidate.
``landed``   a record names it but is not closed — the eddy reached the practice
             and the work is still open. **Not** a dissolve candidate: the eddy
             may still be the only place the reasoning lives.
``untraced`` nothing anywhere names it. Either it never produced anything, or it
             produced something by a route that does not record thread ids. The
             detector cannot tell those apart and does not pretend to.

Usage:
    python3 scripts/craft_done_detector.py              # every craft eddy
    python3 scripts/craft_done_detector.py --cold-only  # the 20 in question
    python3 scripts/craft_done_detector.py --self-check # controls, both directions
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TURTLEOS = ROOT.parent / "turtleos"

sys.path.insert(0, str(ROOT / "scripts"))
from export_craft_digest import parse_backlog  # noqa: E402 — one parser for one file

try:
    import yaml
except ImportError:  # pragma: no cover
    # Measured here on 2026-08-17, and already documented in
    # `sync_practice_root.sh`: an interactive shell may alias `python3` to a
    # version that has the deps and a script run does not inherit the alias, so
    # this fails only when something else invokes it — which is the case that
    # matters. Name the fix rather than the symptom.
    print(
        "PyYAML required. An interactive `python3` may have it while a scripted "
        "one does not — run with an interpreter that does, e.g.\n"
        "  python3.11 scripts/craft_done_detector.py --self-check",
        file=sys.stderr,
    )
    raise SystemExit(2)

SHIPPED, LANDED, UNTRACED = "shipped", "landed", "untraced"

# Surfaces that record an outcome, and whether appearing there means *closed*.
# `bright.md` is deliberately "not closed": a bright entry means the thought is
# alive in the practice, which is the opposite of finished.
# A file that names many eddies is an **index**, not an outcome record, and
# counting it turns "this eddy was once listed on a board" into "this eddy
# produced something". Measured on the first run: `2026-08-11-craft-eddy-handoff-check.md`
# is a triage table naming 11 of the 20 cold eddies, and it alone accounted for
# most of the `landed` verdicts. The rule is deliberately about shape rather
# than filename — a future index under a different name is covered, and an
# excluded file is always printed so the exclusion can be argued with.
INDEX_THRESHOLD = 5

PROSE_SURFACES: tuple[tuple[str, bool], ...] = (
    ("desk/boom/bright.md", False),
    ("desk/craft/handoffs", False),
    ("../turtleos/docs/chapters", False),
    ("../turtleos/docs/learnings.md", False),
)


@dataclass
class Verdict:
    thread_id: str
    name: str
    verdict: str = UNTRACED
    evidence: list[str] = field(default_factory=list)


def _board() -> list[dict]:
    from craft_readiness_board import _on_mini  # reuse the one SSH wrapper

    return json.loads(_on_mini(["--json"]))


def _backlog_hits() -> dict[str, list[tuple[bool, str]]]:
    """thread id → [(shipped, item id)], from the workshop backlog."""
    text = (ROOT / "desk" / "craft" / "backlog.md").read_text(encoding="utf-8")
    items, _unknown = parse_backlog(text)
    hits: dict[str, list[tuple[bool, str]]] = {}
    for item in items:
        # Continuations carry the indented follow-on lines of an entry, and the
        # eddy id is as likely to sit there as in the first line.
        blob = "\n".join([item.body, *item.continuations])
        for tid in set(re.findall(r"\b(\d{17,20})\b", blob)):
            hits.setdefault(tid, []).append((item.shipped, item.id))
    return hits


def _sidecar_hits() -> dict[str, str]:
    """thread id → disposition, from the prepared-eddy sidecar."""
    path = ROOT / "desk" / "craft" / "prepared_eddies.yaml"
    if not path.is_file():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {
        str(tid): str(entry.get("disposition") or "")
        for tid, entry in (data.get("prepared") or {}).items()
        if isinstance(entry, dict)
    }


def _prose_hits(*, report: list[str] | None = None) -> dict[str, list[tuple[str, bool]]]:
    """thread id → [(where, means_closed)] across the prose surfaces."""
    hits: dict[str, list[tuple[str, bool]]] = {}
    for rel, closed in PROSE_SURFACES:
        target = (ROOT / rel).resolve()
        files = (
            sorted(target.rglob("*.md")) if target.is_dir() else [target] if target.is_file() else []
        )
        for path in files:
            try:
                text = path.read_text(encoding="utf-8")
            except OSError:
                continue
            found = set(re.findall(r"\b(\d{17,20})\b", text))
            if len(found) >= INDEX_THRESHOLD:
                if report is not None:
                    report.append(f"{path.name} names {len(found)} eddies — read as an index, not evidence")
                continue
            for tid in found:
                hits.setdefault(tid, []).append((path.name, closed))
    return hits


def classify(rows: list[dict], *, report: list[str] | None = None) -> list[Verdict]:
    backlog, sidecar = _backlog_hits(), _sidecar_hits()
    prose = _prose_hits(report=report)
    out: list[Verdict] = []
    for row in rows:
        tid = row["thread_id"]
        v = Verdict(thread_id=tid, name=row.get("name", ""))

        for shipped, item_id in backlog.get(tid, []):
            v.evidence.append(f"backlog {'[x]' if shipped else '[ ]'} {item_id}")
            v.verdict = SHIPPED if shipped else (v.verdict if v.verdict == SHIPPED else LANDED)

        disposition = sidecar.get(tid)
        if disposition:
            v.evidence.append(f"prepared sidecar: {disposition}")
            if disposition == "harvested":
                v.verdict = SHIPPED
            elif v.verdict == UNTRACED:
                v.verdict = LANDED

        for where, closed in prose.get(tid, []):
            v.evidence.append(f"named in {where}")
            if closed:
                v.verdict = SHIPPED
            elif v.verdict == UNTRACED:
                v.verdict = LANDED

        out.append(v)
    return out


def self_check(verdicts: list[Verdict]) -> int:
    """Controls in both directions. A detector that finds nothing looks clean.

    The positive control is the case the Mage named by eye; the negative is an
    eddy the record genuinely does not mention. Without the second, a join that
    matched everything would pass the first.
    """
    by_name = {v.name: v for v in verdicts}
    failures: list[str] = []

    positive = by_name.get("extract youtube video transcripts")
    if not positive or positive.verdict != SHIPPED:
        failures.append(
            "positive control: 'extract youtube video transcripts' should read "
            f"shipped, read {positive.verdict if positive else 'MISSING'}"
        )

    untraced = [v for v in verdicts if v.verdict == UNTRACED]
    if not untraced:
        failures.append(
            "negative control: every eddy matched something, which means the join "
            "is matching on too little — check the id pattern before believing this"
        )

    shipped = [v for v in verdicts if v.verdict == SHIPPED]
    if len(shipped) == len(verdicts):
        failures.append("negative control: everything reads shipped")

    # Structural, and it is what makes the index rule safe to be crude: prose
    # surfaces are all non-closing, so they can only ever produce `landed`.
    # Every `shipped` verdict therefore rests on a ticked backlog entry or a
    # harvested sidecar row — precise records — and excluding a file as an index
    # can never turn a dissolve candidate into a non-candidate or back. If a
    # closing prose surface is ever added, that guarantee is gone and the
    # threshold becomes a judgement about what may be deleted.
    if any(closed for _rel, closed in PROSE_SURFACES):
        failures.append(
            "a prose surface is marked closing — the index threshold can now "
            "change a dissolve verdict, which it must not"
        )
    for v in shipped:
        if not any(e.startswith("backlog [x]") or e == "prepared sidecar: harvested" for e in v.evidence):
            failures.append(f"{v.name}: shipped without a closing record — {v.evidence}")

    for line in failures:
        print(f"  FAIL {line}")
    if not failures:
        print(
            f"  controls pass · {len(shipped)} shipped, "
            f"{len([v for v in verdicts if v.verdict == LANDED])} landed, "
            f"{len(untraced)} untraced"
        )
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cold-only", action="store_true")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()

    rows = _board()
    if args.cold_only:
        rows = [r for r in rows if r.get("temperature") == "cold"]
    excluded: list[str] = []
    verdicts = classify(rows, report=excluded)
    for line in dict.fromkeys(excluded):
        print(f"  (excluded: {line})")

    if args.self_check:
        return self_check(verdicts)

    order = {SHIPPED: 0, LANDED: 1, UNTRACED: 2}
    for v in sorted(verdicts, key=lambda x: (order[x.verdict], x.name)):
        print(f"  {v.verdict:9} {v.name[:52]:52} {v.thread_id}")
        for line in v.evidence:
            print(f"            ↳ {line}")
    counts = {k: sum(1 for v in verdicts if v.verdict == k) for k in (SHIPPED, LANDED, UNTRACED)}
    print(f"\n  {counts[SHIPPED]} shipped · {counts[LANDED]} landed · {counts[UNTRACED]} untraced")
    print("  shipped = dissolve candidate · landed = still open, do not dissolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
