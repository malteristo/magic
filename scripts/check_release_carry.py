#!/usr/bin/env python3
"""Not Done / Found rows may leave the bundle only by verdict or landing (F-96).

2026-09-22: the Mage asked that what we wanted and did not do, and what we found
along the way, flow into later sessions until it becomes something or is dropped.
The bundle is rewritten at every release, so a row can vanish by omission and no
one sees it go. This check reads the committed bundle (HEAD) and the one about to
be committed and refuses when a row from the old **Not Done / Found** section is
absent from the new bundle and from every disposition file.

A row is identified by its bold name: `- **name**: ...`. It is *carried* when that
name appears anywhere in the new bundle (still open, moved to Next Actions, marked
dropped — the reader sees the fate) or in `desk/craft/dispositions/*.md` (he
verdicted it in a pass).

    python3 scripts/check_release_carry.py             # pre-commit: staged vs HEAD
    python3 scripts/check_release_carry.py --self-test  # positive control
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = "floor/briefings/latest.md"
DISPOSITIONS = ROOT / "desk" / "craft" / "dispositions"
SECTION = "**Not Done / Found**"
ROW = re.compile(r"^- \*\*(.+?)\*\*")


VERDICT = "[k]"


def section_rows(text: str, *, include_verdicted: bool = True) -> list[str]:
    """Bold names of the rows under **Not Done / Found**, until the next field.

    A row carrying `[k]` was verdicted by the Mage in that bundle; it has left
    by verdict and need not be carried further (found in use, 2026-09-22 12:59:
    the first `.` on eight rows would otherwise have pinned them forever).
    """
    rows: list[str] = []
    inside = False
    for line in text.splitlines():
        if line.strip().replace(":**", "**").startswith(SECTION):
            inside = True
            continue
        if inside:
            if line.startswith("**") and line.strip().endswith("**"):
                break
            m = ROW.match(line.strip())
            if m and (include_verdicted or VERDICT not in line):
                rows.append(m.group(1).strip())
    return rows


def missing_rows(previous: str, current: str, dispositions: str) -> list[str]:
    """Unverdicted rows of the previous bundle with no trace in the new bundle or any pass."""
    haystack = current + "\n" + dispositions
    return [
        name
        for name in section_rows(previous, include_verdicted=False)
        if name not in haystack
    ]


def _git_show_head(path: str) -> str:
    try:
        return subprocess.run(
            ["git", "show", f"HEAD:{path}"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    except subprocess.CalledProcessError:
        return ""


def _staged(path: str) -> str | None:
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--", path],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if not result.stdout.strip():
        return None
    return subprocess.run(
        ["git", "show", f":{path}"], cwd=ROOT, capture_output=True, text=True
    ).stdout


def _all_dispositions() -> str:
    if not DISPOSITIONS.is_dir():
        return ""
    return "\n".join(
        p.read_text(errors="ignore") for p in sorted(DISPOSITIONS.glob("*.md"))
    )


def self_test() -> int:
    previous = (
        "**Open Threads**\n- **kate**: x → y\n\n"
        "**Not Done / Found**\n"
        "- **import-time client**: found → later, god-module slice\n"
        "- **glance count**: found → his `. x`\n\n"
        "**What Changed**\n- **glance count** appears here too but outside the section\n"
    )
    assert section_rows(previous) == ["import-time client", "glance count"], section_rows(previous)
    carried = "**Not Done / Found**\n- **import-time client**: carried\n- **glance count**: dropped, his word\n"
    assert missing_rows(previous, carried, "") == []
    lost = "**Not Done / Found**\n- **import-time client**: carried\n"
    assert missing_rows(previous, lost, "") == ["glance count"], "the guard must catch a silent loss"
    verdicted = missing_rows(previous, lost, "| 3 | **glance count** | … | **dest** `[k]` |")
    assert verdicted == [], "a disposition-pass verdict counts as leaving by verdict"
    assert missing_rows("no section at all", "", "") == []
    dotted = previous.replace("- **glance count**: found → his `. x`", "- **glance count**: dest `[k]`")
    assert missing_rows(dotted, lost, "") == [], "a `[k]` row has left by verdict"
    assert section_rows(dotted) == ["import-time client", "glance count"]
    # The release template writes headers with a colon; the colon-less fixture
    # above passed for two days while every real bundle parsed as empty.
    coloned = previous.replace("**Not Done / Found**", "**Not Done / Found:**").replace(
        "**What Changed**", "**What Changed:**"
    )
    assert section_rows(coloned) == ["import-time client", "glance count"], section_rows(coloned)
    assert missing_rows(coloned, lost, "") == ["glance count"], "the template's own format must be read"
    print("PASS: a dropped Not Done / Found row is caught; carry, drop-with-word, pass verdict and `[k]` all pass")
    return 0


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        return self_test()
    current = _staged(BUNDLE)
    if current is None:
        return 0  # bundle not part of this commit
    previous = _git_show_head(BUNDLE)
    lost = missing_rows(previous, current, _all_dispositions())
    if not lost:
        print(f"PASS: Not Done / Found rows carried ({len(section_rows(current))} in the new bundle)")
        return 0
    print("FAIL: Not Done / Found rows left the bundle with no verdict and no landing (F-96):")
    for name in lost:
        print(f"  - {name}")
    print("Carry them, mark them dropped with his word, or point at the disposition pass.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
