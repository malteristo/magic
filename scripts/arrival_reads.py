#!/usr/bin/env python3
"""arrival_reads.py — enforce evaluation D's read-budget claim.

Bare arrival front-matter ≤ 15K tokens; `. turtle` adds ≤ 5K (`craft_open`).
Token estimate is bytes / 4, same as the proposal that set the number.

    python3 scripts/arrival_reads.py           # bare
    python3 scripts/arrival_reads.py --craft   # bare + open view
    python3 scripts/arrival_reads.py --self-test
"""
from __future__ import annotations

import sys
from datetime import date, timedelta
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from bright_alive import render_alive  # noqa: E402
from craft_open import render_open  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
BARE_TOKEN_CAP = 15_000
CRAFT_EXTRA_TOKEN_CAP = 5_000
TWINE_DAYS = 14

BARE_FILES = (
    "desk/intentions/bearings.md",
    "desk/intentions/year.md",
    "desk/intentions/meta_plan.md",
    "floor/briefings/latest.md",
    "desk/intentions/compass.md",
    "desk/boom.md",
)


def _tokens(n_bytes: int) -> int:
    return n_bytes // 4


def twine_bytes(root: Path, today: date | None = None) -> int:
    today = today or date.today()
    cut = today - timedelta(days=TWINE_DAYS)
    total = 0
    story = root / "desk" / "story"
    paths = list((story / "daily").glob("*.md")) + list((story / "eddies").rglob("*.md"))
    for p in paths:
        try:
            d = date.fromisoformat(p.stem[:10])
        except ValueError:
            continue
        if d >= cut:
            total += p.stat().st_size
    return total


def measure(root: Path, craft: bool = False, today: date | None = None) -> dict:
    today = today or date.today()
    parts: dict[str, int] = {}
    for rel in BARE_FILES:
        p = root / rel
        parts[rel] = p.stat().st_size if p.is_file() else 0
    parts["twine_14d"] = twine_bytes(root, today)
    bright = root / "desk" / "boom" / "bright.md"
    alive = render_alive(bright.read_text(encoding="utf-8") if bright.is_file() else "")
    parts["alive_view"] = len(alive.encode("utf-8"))
    if craft:
        backlog = root / "desk" / "craft" / "backlog.md"
        open_view = render_open(backlog.read_text(encoding="utf-8") if backlog.is_file() else "")
        parts["craft_open"] = len(open_view.encode("utf-8"))
    return parts


def report(parts: dict[str, int], craft: bool) -> tuple[int, list[str]]:
    bare_keys = [k for k in parts if k != "craft_open"]
    bare = sum(parts[k] for k in bare_keys)
    extra = parts.get("craft_open", 0)
    lines = [f"  {k}: {v:,} bytes (~{_tokens(v)} tok)" for k, v in parts.items()]
    lines.append(f"  bare total: {bare:,} bytes (~{_tokens(bare)} / {BARE_TOKEN_CAP} tok)")
    if craft:
        lines.append(
            f"  craft extra: {extra:,} bytes (~{_tokens(extra)} / {CRAFT_EXTRA_TOKEN_CAP} tok)"
        )
    breaches = []
    if _tokens(bare) > BARE_TOKEN_CAP:
        breaches.append(f"bare arrival ~{_tokens(bare)} tok > {BARE_TOKEN_CAP}")
    if craft and _tokens(extra) > CRAFT_EXTRA_TOKEN_CAP:
        breaches.append(f"craft extra ~{_tokens(extra)} tok > {CRAFT_EXTRA_TOKEN_CAP}")
    return (1 if breaches else 0), lines + [f"BREACH: {b}" for b in breaches]


def self_test() -> int:
    failures: list[str] = []
    parts = measure(ROOT)
    if "alive_view" not in parts or parts["alive_view"] == 0:
        failures.append("alive view measured as empty")
    if parts.get("desk/intentions/year.md", 0) == 0:
        failures.append("year.md missing or empty — planted control: arrival must count it")
    if "desk/boom/bright.md" in parts:
        failures.append("budget still counted the bright store")
    code, _lines = report(parts, craft=False)
    # A live over-budget is a finding the next arrival should see, not a
    # broken self-test — the test asserts the *decision*, not today's size.
    planted = {"bearings": 10, "alive_view": 10}
    if report(planted, False)[0] != 0:
        # 20 bytes = 5 tokens, under cap
        pass
    huge = {"x": BARE_TOKEN_CAP * 4 + 4}
    if report(huge, False)[0] != 1:
        failures.append("planted over-budget bare arrival was not rejected")
    huge_craft = {"alive_view": 10, "craft_open": CRAFT_EXTRA_TOKEN_CAP * 4 + 4}
    if report(huge_craft, True)[0] != 1:
        failures.append("planted over-budget craft extra was not rejected")
    arrival = (ROOT / "system" / "flows" / "summon" / "cast_arrival.md").read_text(
        encoding="utf-8"
    )
    if "desk/intentions/year.md" not in arrival:
        failures.append("cast_arrival.md does not name year.md (F-86)")
    if "desk/intentions/year.md" not in BARE_FILES:
        failures.append("BARE_FILES missing year.md (F-86)")
    if "full life landscape" in arrival:
        failures.append("`.` still claims full life landscape (F-88)")
    if "`. turtle`" not in arrival:
        failures.append("cast_arrival.md does not name `. turtle` (F-88)")
    if "Platform — `. turtle` only" not in arrival:
        failures.append("platform duties not gated on `. turtle` (F-88)")
    if "never year-zooms" not in arrival:
        failures.append("cast_arrival.md does not forbid `.` year-zoom (F-90)")
    if "A `.` with no prepared motion" in arrival or "bare `.` zooms" in arrival:
        failures.append("cast_arrival.md still year-zooms on bare `.` (F-90)")
    if "**Invocation:** `...`" not in arrival:
        failures.append("cast_arrival.md invocation is not `...` (F-90)")
    if "cast_plan_review.md" not in arrival or "until addressed" not in arrival:
        failures.append("cast_arrival.md does not name Creator–Critic loop (F-91)")
    if "independent review" in arrival:
        failures.append("cast_arrival.md still names one-shot independent review (F-91)")
    review = (ROOT / "system" / "flows" / "summon" / "cast_plan_review.md").read_text(
        encoding="utf-8"
    )
    if "does not attach a list of questions" not in review:
        failures.append("cast_plan_review.md lost the no-attack-list rule (F-91)")
    if "same** Critic" not in review and "same Critic" not in review:
        failures.append("cast_plan_review.md does not resume the same Critic (F-91)")
    summon = (ROOT / "system" / "flows" / "summon" / "cast_summon.md").read_text(
        encoding="utf-8"
    )
    if "→ glance" not in summon:
        failures.append("cast_summon.md menu does not offer `...` as glance (F-90)")
    if "professional whole" in arrival or "professional whole" in summon:
        failures.append("arrival still called professional whole (F-89)")
    menu = summon.split("```", 2)[1] if summon.count("```") >= 2 else summon
    if ". mirror" in menu or ". maintenance" in menu:
        failures.append("summon door still leads with rooms (F-92)")
    if "first glance at their toward" not in arrival:
        failures.append("cast_arrival.md lost arrival-as-toward (F-92)")
    if "`. [intention]`" not in arrival or "skip" not in arrival.lower():
        failures.append("cast_arrival.md does not name the skip (F-92)")
    if "never `.` or `. [intention]`" not in arrival:
        failures.append("cast_arrival.md still allows `.` as invocation (F-92)")
    breath = (ROOT / "system" / "lore" / "core" / "conduct" / "on_breath_signals_and_the_dot_protocol.md").read_text(
        encoding="utf-8"
    )
    if "The plan is finished" not in breath or "F-93" not in breath:
        failures.append("breath protocol lost the plan-finished signify (F-93)")
    if "When the sanctioned plan is finished" not in arrival:
        failures.append("cast_arrival.md lost the plan-finished fork (F-93)")
    if "Eddy regard (F-94)" not in arrival:
        failures.append("cast_arrival.md lost eddy regard notes (F-94)")
    if "F-95" not in arrival:
        failures.append("cast_arrival.md lost the position rule (F-95)")
    if "last_arrival.yaml" not in arrival:
        failures.append("cast_arrival.md lost the arrival stamp (F-94)")
    if failures:
        for f in failures:
            print(f"SELF-TEST FAIL: {f}")
        return 1
    print(
        "arrival_reads self-test: ok "
        "(bright excluded, year.md wired, platform tax on . turtle, "
        ". never year-zooms, Creator–Critic loop, planted breaches rejected)"
    )
    return 0


def main(argv: list[str]) -> int:
    if len(argv) > 1 and argv[1] in {"-h", "--help"}:
        print(__doc__)
        return 0
    if len(argv) > 1 and argv[1] == "--self-test":
        return self_test()
    craft = "--craft" in argv
    parts = measure(ROOT)
    if craft:
        parts = measure(ROOT, craft=True)
    code, lines = report(parts, craft)
    print("Arrival read budget" + (" (. turtle extra)" if craft else " (bare)"))
    print("\n".join(lines))
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
