#!/usr/bin/env python3
"""check_meta_plan.py — every live bearing has a section; craft names serve/wait/defer.

The meta-plan is Spirit-maintained and rewritten at release. A file that asks
to be kept current without a check becomes chains.md (39 days of a contradicted
diagram). This is the check.

    python3 scripts/check_meta_plan.py           # exit 1 on gaps
    python3 scripts/check_meta_plan.py --self-test
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BEARINGS = ROOT / "desk/intentions/bearings.md"
META = ROOT / "desk/intentions/meta_plan.md"

HEADING = re.compile(r"^### (\S+)")
CRAFT_HEADING = re.compile(r"^### (\S+).*·\s*craft")
STATUS = re.compile(r"(?im)^\s*[-*]?\s*\*?\*?Status\*?\*?\s*[—:-]\s*(serve|wait|defer)\b")


def live_slugs(text: str) -> list[str]:
    return [m.group(1) for line in text.splitlines() if (m := HEADING.match(line))]


def craft_slugs(text: str) -> list[str]:
    return [m.group(1) for line in text.splitlines() if (m := CRAFT_HEADING.search(line))]


def sections(text: str) -> dict[str, str]:
    found: dict[str, list[str]] = {}
    current: str | None = None
    for line in text.splitlines():
        m = HEADING.match(line)
        if m:
            current = m.group(1)
            found[current] = []
            continue
        if current is not None:
            found[current].append(line)
    return {k: "\n".join(v) for k, v in found.items()}


def check(bearings: str, meta: str) -> list[str]:
    errors: list[str] = []
    if "## Alignment" not in meta:
        errors.append("meta-plan has no ## Alignment section")
    slugs = live_slugs(bearings)
    if not slugs:
        errors.append("bearings.md has no ### slugs")
        return errors
    have = sections(meta)
    for slug in slugs:
        if slug not in have:
            errors.append(f"missing ### {slug}")
            continue
        if slug in craft_slugs(bearings) and not STATUS.search(have[slug]):
            errors.append(f"{slug}: no Status: serve|wait|defer")
    return errors


def self_test() -> int:
    bearings = (
        "### turtle · craft\n- **Next** — x\n"
        "### outfacing · craft\n- **Next** — y\n"
        "### partner · family\n- **Next** — z\n"
    )
    good = (
        "## Alignment\ncraft serves family.\n"
        "### turtle\n- Status: serve\n"
        "### outfacing\n- Status: wait\n"
        "### partner\n- Status: wait\n"
    )
    failures: list[str] = []
    if check(bearings, good):
        failures.append("complete meta-plan was rejected")
    missing = check(bearings, "## Alignment\n### turtle\n- Status: serve\n### partner\n")
    if "missing ### outfacing" not in missing:
        failures.append(f"missing craft slug not named: {missing}")
    no_status = check(bearings, good.replace("- Status: wait\n", "- no status\n"))
    if not any("outfacing" in e and "Status" in e for e in no_status):
        failures.append(f"craft without Status not named: {no_status}")
    if failures:
        for f in failures:
            print(f"SELF-TEST FAIL: {f}")
        return 1
    print("check_meta_plan self-test: ok")
    return 0


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        return self_test()
    bearings = BEARINGS.read_text(encoding="utf-8") if BEARINGS.is_file() else ""
    meta = META.read_text(encoding="utf-8") if META.is_file() else ""
    if not META.is_file():
        print("meta-plan missing: desk/intentions/meta_plan.md")
        return 1
    errors = check(bearings, meta)
    if errors:
        print("meta-plan gaps:")
        for e in errors:
            print(f"  {e}")
        return 1
    print(f"meta-plan ok — {len(live_slugs(bearings))} bearings, "
          f"{len(craft_slugs(bearings))} craft with Status")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
