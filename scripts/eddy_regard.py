#!/usr/bin/env python3
"""eddy_regard.py — which craft eddies owe an arrival regard note (F-94).

A note goes in each *new* craft eddy since the last arrival stamp, and each
*existing* eddy that had further *practitioner* speech after that stamp.
Turtle answering a regard note does not re-owe. Quiet leftovers stay quiet.

    python3 scripts/eddy_regard.py --self-test
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

STAMP = "desk/craft/last_arrival.yaml"


@dataclass(frozen=True)
class EddyWindow:
    thread_id: str
    created_at: datetime
    last_exchange_at: datetime | None = None


def qualify(eddies: list[EddyWindow], cutoff: datetime) -> list[str]:
    """Return thread ids that owe a regard note this arrival."""
    owed: list[str] = []
    for eddy in eddies:
        if eddy.created_at > cutoff:
            owed.append(eddy.thread_id)
        elif eddy.last_exchange_at is not None and eddy.last_exchange_at > cutoff:
            owed.append(eddy.thread_id)
    return owed


def self_test() -> int:
    cutoff = datetime(2026, 9, 15, 16, 16, tzinfo=timezone.utc)
    later = datetime(2026, 9, 15, 17, 8, tzinfo=timezone.utc)
    earlier = datetime(2026, 9, 15, 13, 0, tzinfo=timezone.utc)
    eddies = [
        EddyWindow("new", created_at=later),
        EddyWindow("moved", created_at=earlier, last_exchange_at=later),
        EddyWindow("quiet", created_at=earlier, last_exchange_at=earlier),
        EddyWindow("bar-only", created_at=earlier, last_exchange_at=None),
        EddyWindow("turtle-reply", created_at=earlier, last_exchange_at=None),
    ]
    got = qualify(eddies, cutoff)
    failures: list[str] = []
    if "new" not in got:
        failures.append("new eddy after cutoff was not owed")
    if "moved" not in got:
        failures.append("existing eddy with later practitioner speech was not owed")
    if "quiet" in got:
        failures.append("quiet existing eddy was owed — the scarcity rule failed")
    if "bar-only" in got:
        failures.append("River-bar-only existing eddy was owed")
    if "turtle-reply" in got:
        failures.append("Turtle reply to a regard note was owed — the loop")
    if failures:
        for f in failures:
            print(f"SELF-TEST FAIL: {f}")
        return 1
    print("eddy_regard self-test: ok (new + moved owed; quiet, bar-only, turtle-reply excluded)")
    return 0


if __name__ == "__main__":
    import sys

    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    print("Usage: python3 scripts/eddy_regard.py --self-test")
    raise SystemExit(2)
