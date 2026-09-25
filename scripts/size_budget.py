#!/usr/bin/env python3
"""size_budget.py — budgets for the files a model reads every turn or every arrival.

Why a mechanism and not a sentence: `AGENTS.md` said "keep this file lean" twice
and grew from 7.4 KB to 13.2 KB. `cast_arrival.md` was cut to 8.1 KB on
2026-07-29 and stood at 24.6 KB five weeks later. Currency is a state, drift is a
rate; rewording the request buys another interval of quiet drift (Wire Before
Mechanism, exception sanctioned 2026-08-14). Evaluation proposal item C,
sanctioned 2026-09-03.

Two severities, decided with the Mage 2026-09-03:
  HARD — always-on files injected on every Cursor turn. Over budget blocks the commit.
  WARN — loop files read once per arrival/release. Over budget is reported, never
         blocks, and the release flow copies the WARN into Practice Signal so it
         cannot be quietly ignored.

Deliberately not here: the "every Alive entry dated" rule from the proposal.
`rot_radar.py` counts undated Alive entries; `bright_alive.py` omits them from
the arrival view. Gating bright.md before the diet pass
(`2026-08-17-alive-diet-pass`) would block every commit touching it.
Dating and the 80→12 cut remain a sweep.

Usage:
    scripts/size_budget.py --gate        # pre-commit: staged files only; exit 1 on HARD breach
    scripts/size_budget.py --report      # all budgeted files, exit 0
    scripts/size_budget.py --self-test   # positive control: a planted over-budget file must be rejected
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

HARD = "HARD"
WARN = "WARN"

# path (relative to repo root) -> (budget in bytes, severity)
BUDGETS: dict[str, tuple[int, str]] = {
    # 10 KB, not the 8 KB the proposal guessed: with every incident moved to the ledger the
    # Seal is 9.3 KB of rules. The budget is a ratchet against regrowth — ~700 bytes of
    # headroom, one new preference — not a target the rules must be squeezed into.
    "AGENTS.md": (10 * 1024, HARD),
    "CLAUDE.md": (4 * 1024, HARD),
    "system/flows/summon/cast_arrival.md": (10 * 1024, WARN),
    "system/flows/release/cast_release.md": (10 * 1024, WARN),
    "system/flows/maintenance/cast_maintenance_arrival.md": (10 * 1024, WARN),
    "system/flows/summon/cast_summon.md": (6 * 1024, WARN),
    "system/flows/summon/covenant.md": (6 * 1024, WARN),
}


def repo_root() -> Path:
    out = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True
    )
    return Path(out.stdout.strip())


def staged_paths(root: Path) -> set[str]:
    out = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        capture_output=True, text=True, check=True, cwd=root,
    )
    return {line.strip() for line in out.stdout.splitlines() if line.strip()}


def staged_size(root: Path, rel: str) -> int | None:
    """Size of the *staged* blob, not the working tree — what the commit would contain."""
    out = subprocess.run(["git", "cat-file", "-s", f":{rel}"], capture_output=True, text=True, cwd=root)
    if out.returncode != 0:
        return None
    return int(out.stdout.strip())


def evaluate(sizes: dict[str, int], budgets: dict[str, tuple[int, str]]) -> tuple[list[str], list[str]]:
    """Pure decision: returns (hard_breaches, warn_breaches) as formatted lines."""
    hard, warn = [], []
    for rel, (budget, severity) in budgets.items():
        size = sizes.get(rel)
        if size is None or size <= budget:
            continue
        line = f"{severity} {rel}: {size:,} bytes > budget {budget:,} (+{size - budget:,})"
        (hard if severity == HARD else warn).append(line)
    return hard, warn


def gate(root: Path) -> int:
    staged = staged_paths(root)
    sizes = {rel: s for rel in BUDGETS if rel in staged and (s := staged_size(root, rel)) is not None}
    hard, warn = evaluate(sizes, BUDGETS)
    for line in warn:
        print(f"size_budget: {line}")
    for line in hard:
        print(f"size_budget: {line}")
    if hard:
        print("size_budget: commit blocked — an always-on file is over budget. Trim it, or move the "
              "incident to desk/craft/practice_falsifiers.md and keep the one-line rule.")
        return 1
    return 0


def report(root: Path) -> int:
    sizes = {rel: (root / rel).stat().st_size for rel in BUDGETS if (root / rel).exists()}
    hard, warn = evaluate(sizes, BUDGETS)
    for rel, (budget, severity) in BUDGETS.items():
        size = sizes.get(rel)
        if size is None:
            print(f"  -    {rel}: missing")
            continue
        mark = "OVER" if size > budget else "ok  "
        print(f"  {mark} {rel}: {size:,} / {budget:,} ({severity})")
    if hard or warn:
        print()
        for line in hard + warn:
            print(line)
    return 0


def self_test() -> int:
    """Positive control: the decision function must reject a planted breach and pass a clean file,
    and the gate must read the staged blob rather than the working tree."""
    failures = []

    hard, warn = evaluate({"AGENTS.md": 8 * 1024 + 1}, {"AGENTS.md": (8 * 1024, HARD)})
    if not hard or warn:
        failures.append("planted HARD breach was not reported as HARD")

    hard, warn = evaluate({"x.md": 10 * 1024 + 1}, {"x.md": (10 * 1024, WARN)})
    if hard or not warn:
        failures.append("planted WARN breach was not reported as WARN")

    hard, warn = evaluate({"AGENTS.md": 8 * 1024}, {"AGENTS.md": (8 * 1024, HARD)})
    if hard or warn:
        failures.append("a file exactly at budget was reported as a breach")

    # End-to-end: a scratch repo with an over-budget AGENTS.md staged must fail the gate,
    # and unstaging it must clear the gate even though the working tree is still over.
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
        subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True, env=env)
        (tmp_path / "AGENTS.md").write_bytes(b"x" * (8 * 1024 + 1))
        subprocess.run(["git", "add", "AGENTS.md"], cwd=tmp_path, check=True, env=env)
        if gate(tmp_path) != 1:
            failures.append("gate passed a staged over-budget AGENTS.md")
        subprocess.run(["git", "reset", "-q", "AGENTS.md"], cwd=tmp_path, check=True, env=env)
        if gate(tmp_path) != 0:
            failures.append("gate blocked with nothing budgeted staged")

    if failures:
        for f in failures:
            print(f"SELF-TEST FAIL: {f}")
        return 1
    print("size_budget self-test: ok (planted breach rejected, clean file passed, staged blob read)")
    return 0


def main(argv: list[str]) -> int:
    mode = argv[1] if len(argv) > 1 else "--report"
    if mode == "--self-test":
        return self_test()
    root = repo_root()
    if mode == "--gate":
        return gate(root)
    if mode == "--report":
        return report(root)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
