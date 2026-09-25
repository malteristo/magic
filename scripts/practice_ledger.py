#!/usr/bin/env python3
"""practice_ledger.py — one line per release; measures the practice can be judged by.

Evaluation proposal item E (2026-09-03). The practice had no record of which flows
were invoked, on which model, with what result — so "did the last model change
make the practice better" had no number behind it. This appends the number's raw
material at every release and computes what can be computed from the tree.

Usage:
    scripts/practice_ledger.py append --substrate Forge --model "Claude Fable 5.1" \
        --scope craft --bearing turtle --flows summon,arrival,release \
        --signals 2 --proposals 1 --fired F-14,F-32
    scripts/practice_ledger.py measures        # coverage, per-model fired rate, told-by cadence
    scripts/practice_ledger.py --self-test     # positive control on a temp ledger

Measures computed here:
  claim coverage   rules in the loop files that carry a ledger F-id ÷ rule lines
  fired per session, by model   the falsifier rate — the number item B reads
  flow usage       invocation counts from the ledger
  told-by cadence  days since the last dated entry in desk/intentions/told_by_reads.md (item G)

Deliberately not computed: time-to-detection of practice defects. It needs the
defect's introduction date, which the ledger rows mostly lack (dates are when the
rule was written, not when the failure began). Fill the ledger's incident dates
first; then this gets a column.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "desk" / "practice_ledger.tsv"
FALSIFIERS = ROOT / "desk" / "craft" / "practice_falsifiers.md"
TOLD_BY = ROOT / "desk" / "intentions" / "told_by_reads.md"
LOOP_FILES = [
    ROOT / "AGENTS.md",
    ROOT / "system" / "flows" / "summon" / "cast_arrival.md",
    ROOT / "system" / "flows" / "release" / "cast_release.md",
]
COLUMNS = ["date", "substrate", "model", "scope", "bearing", "flows", "signals", "proposals", "fired"]
TOLD_BY_CADENCE_DAYS = 35


def append(ledger: Path, row: dict[str, str]) -> str:
    new = not ledger.exists() or ledger.stat().st_size == 0
    line = "\t".join(row.get(c, "") for c in COLUMNS)
    with ledger.open("a", encoding="utf-8") as fh:
        if new:
            fh.write("\t".join(COLUMNS) + "\n")
        fh.write(line + "\n")
    return line


def read_rows(ledger: Path) -> list[dict[str, str]]:
    if not ledger.exists():
        return []
    lines = ledger.read_text(encoding="utf-8").splitlines()
    if not lines:
        return []
    header = lines[0].split("\t")
    return [dict(zip(header, ln.split("\t"))) for ln in lines[1:] if ln.strip()]


def claim_coverage(files: list[Path]) -> tuple[int, int]:
    """Rule lines = bullet or bold-led lines in the loop files; covered = those citing an F-id."""
    rules = covered = 0
    pat_rule = re.compile(r"^\s*(?:-\s+)?\*\*[^*]+\*\*")
    pat_fid = re.compile(r"F-\d{2}")
    for f in files:
        if not f.exists():
            continue
        for ln in f.read_text(encoding="utf-8").splitlines():
            if pat_rule.match(ln):
                rules += 1
                if pat_fid.search(ln):
                    covered += 1
    return covered, rules


def live_rows(falsifiers: Path) -> int:
    if not falsifiers.exists():
        return 0
    return sum(1 for ln in falsifiers.read_text(encoding="utf-8").splitlines()
               if ln.startswith("| F-") and "| live" in ln)


def told_by_age(path: Path, today: dt.date) -> int | None:
    if not path.exists():
        return None
    dates = re.findall(r"^##\s+(\d{4}-\d{2}-\d{2})", path.read_text(encoding="utf-8"), re.M)
    if not dates:
        return None
    last = max(dt.date.fromisoformat(d) for d in dates)
    return (today - last).days


def measures(ledger: Path, falsifiers: Path, told_by: Path, files: list[Path], today: dt.date) -> list[str]:
    out = []
    covered, rules = claim_coverage(files)
    out.append(f"claim coverage: {covered}/{rules} rule lines carry an F-id "
               f"({covered / rules:.0%})" if rules else "claim coverage: no rule lines found")
    out.append(f"ledger: {live_rows(falsifiers)} live rows")

    rows = read_rows(ledger)
    if not rows:
        out.append("releases logged: 0 — the fired-per-session rate has no data yet")
    else:
        by_model: dict[str, list[int]] = {}
        flows: dict[str, int] = {}
        for r in rows:
            fired = [x for x in r.get("fired", "").split(",") if x.strip() and x.strip().lower() != "none"]
            by_model.setdefault(r.get("model", "?"), []).append(len(fired))
            for fl in r.get("flows", "").split(","):
                if fl.strip():
                    flows[fl.strip()] = flows.get(fl.strip(), 0) + 1
        out.append(f"releases logged: {len(rows)}")
        for model, counts in sorted(by_model.items()):
            out.append(f"  {model}: {len(counts)} sessions, {sum(counts) / len(counts):.2f} falsifiers fired per session")
        top = sorted(flows.items(), key=lambda kv: -kv[1])[:8]
        out.append("flow usage: " + ", ".join(f"{k}×{v}" for k, v in top))

    age = told_by_age(told_by, today)
    if age is None:
        out.append(f"told-by read: none recorded — first read due (cadence {TOLD_BY_CADENCE_DAYS} d)")
    elif age > TOLD_BY_CADENCE_DAYS:
        out.append(f"told-by read: OVERDUE — last {age} d ago (cadence {TOLD_BY_CADENCE_DAYS} d)")
    else:
        out.append(f"told-by read: last {age} d ago")
    return out


def self_test() -> int:
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        t = Path(tmp)
        ledger = t / "ledger.tsv"
        append(ledger, {"date": "2026-09-03", "model": "M1", "flows": "summon,release", "fired": "F-14"})
        append(ledger, {"date": "2026-09-04", "model": "M1", "flows": "summon", "fired": "none"})
        rows = read_rows(ledger)
        if len(rows) != 2 or rows[0]["fired"] != "F-14":
            failures.append("append/read round-trip lost a row or a field")

        loop = t / "loop.md"
        loop.write_text("- **Rule one:** text (F-01)\n- **Rule two:** text\n**Rule three:** (F-03)\n", encoding="utf-8")
        if claim_coverage([loop]) != (2, 3):
            failures.append(f"claim coverage miscounted: {claim_coverage([loop])}")

        fals = t / "f.md"
        fals.write_text("| F-01 | d | r | i | f | m | live |\n| F-02 | d | r | i | f | m | retired |\n", encoding="utf-8")
        if live_rows(fals) != 1:
            failures.append("live row count wrong")

        tb = t / "tb.md"
        tb.write_text("## 2026-07-01\n\nread\n", encoding="utf-8")
        age = told_by_age(tb, dt.date(2026, 9, 3))
        if age != 64:
            failures.append(f"told-by age wrong: {age}")
        lines = measures(ledger, fals, tb, [loop], dt.date(2026, 9, 3))
        if not any("OVERDUE" in ln for ln in lines):
            failures.append("a 64-day-old told-by read was not reported overdue")
        if not any("M1: 2 sessions, 0.50" in ln for ln in lines):
            failures.append("fired-per-session rate not computed")

    if failures:
        for f in failures:
            print(f"SELF-TEST FAIL: {f}")
        return 1
    print("practice_ledger self-test: ok (round-trip, coverage, live rows, overdue told-by, fired rate)")
    return 0


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        return self_test()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("append")
    for c in COLUMNS[1:]:
        a.add_argument(f"--{c}", default="")
    a.add_argument("--date", default=dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
    sub.add_parser("measures")
    ns = ap.parse_args(argv)
    if ns.cmd == "append":
        row = {c: getattr(ns, c) for c in COLUMNS}
        print(append(LEDGER, row))
        return 0
    for ln in measures(LEDGER, FALSIFIERS, TOLD_BY, LOOP_FILES, dt.date.today()):
        print(ln)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
