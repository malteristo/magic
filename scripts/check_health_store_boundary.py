#!/usr/bin/env python3
"""Fail if the household health store leaks into a git tree.

The living pictures and their documents live on the Mini at
``~/workshops/health/`` and ``~/workshops/health-<subject>/``. They must not
appear as tracked files in magic or turtleOS. This check is the enforcement
for that claim (F-67).

    python3 scripts/check_health_store_boundary.py
    python3 scripts/check_health_store_boundary.py --self-test
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TURTLEOS = ROOT.parent / "turtleos"

ATTACHMENT_EXTS = {
    ".pdf",
    ".jpg",
    ".jpeg",
    ".png",
    ".tif",
    ".tiff",
    ".dcm",
    ".dicom",
}


def _tracked(repo: Path) -> list[str]:
    if not (repo / ".git").exists() and not (repo / ".git").is_file():
        return []
    proc = subprocess.run(
        ["git", "-C", str(repo), "ls-files", "-z"],
        capture_output=True,
        check=True,
    )
    return [p for p in proc.stdout.decode().split("\0") if p]


def why_forbidden(rel: str) -> str | None:
    norm = rel.replace("\\", "/").lower()
    if "health/documents/" in norm or norm.startswith("health/documents/"):
        return f"health documents path tracked: {rel}"
    if Path(norm).name == "health_model.md":
        return f"health picture tracked in a code repo: {rel}"
    if "health/" in norm and Path(norm).suffix in ATTACHMENT_EXTS:
        return f"health attachment tracked: {rel}"
    return None


def findings(paths: list[str]) -> list[str]:
    return [msg for rel in paths if (msg := why_forbidden(rel))]


def scan() -> list[str]:
    hits = findings(_tracked(ROOT))
    if TURTLEOS.is_dir():
        hits.extend(findings(_tracked(TURTLEOS)))
    return hits


def self_test() -> int:
    failures: list[str] = []
    planted = [
        "health/documents/scan.pdf",
        "workshops/health/documents/labs.pdf",
        "desk/notes/health_model.md",
        "docs/health/bloodwork.jpg",
    ]
    clean = [
        "desk/notes/health-picture-loop.md",
        "library/flows/diagnostic/README.md",
        "desk/craft/goettingen_praxis/schreibtisch/offer.pdf",
    ]
    missed = [p for p in planted if why_forbidden(p) is None]
    if missed:
        failures.append(f"planted leak not rejected: {missed}")
    false = [p for p in clean if why_forbidden(p) is not None]
    if false:
        failures.append(f"clean path rejected: {false}")
    live = scan()
    if live:
        failures.append(f"live tree already leaking: {live}")
    if failures:
        for line in failures:
            print(f"SELF-TEST FAIL: {line}")
        return 1
    print("PASS: planted health-store leaks rejected; clean paths and live trees clear")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    hits = scan()
    if hits:
        print("FAIL: health store must stay on the Mini, not in these trees")
        for hit in hits:
            print(f"  {hit}")
        return 1
    print("PASS: no health store files in magic or turtleos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
