#!/usr/bin/env python3
"""rot_radar.py — mechanical pass over the workshop's decay signals.

`cast_tend_workshop.md` §4b describes a rot radar as a table of signals to scan
by hand. Scanning it by hand is how a signal gets missed on a tired evening, and
how an action item with a deadline three months past keeps reading as live. This
is the same table, executed.

It reports. It does not fix anything, and it never edits `desk/`.

    ./scripts/rot_radar.py            # full pass
    ./scripts/rot_radar.py --quiet    # findings only, no clean lines
    ./scripts/rot_radar.py --json     # machine-readable

Exit 0 always: a radar is not a gate.
"""

import json
import re
import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(
    subprocess.run(["git", "rev-parse", "--show-toplevel"],
                   capture_output=True, text=True).stdout.strip() or "."
)

# Thresholds, in days. Tuned to the practice's own rhythms: a week of sessions,
# a fortnight for a proposal to find its home, a month for a draft to prove it
# is still wanted.
STALE_SWEEP = 7
STALE_PROPOSAL = 14
STALE_DRAFT = 30
STALE_STATE = 3

TODAY = date.today()
QUIET = "--quiet" in sys.argv
AS_JSON = "--json" in sys.argv

RED, YEL, GRN, DIM, NC = "\033[0;31m", "\033[0;33m", "\033[0;32m", "\033[2m", "\033[0m"
findings = []


def add(signal, detail, items=None, severity="MEDIUM"):
    findings.append({"signal": signal, "detail": detail,
                     "items": items or [], "severity": severity})


def age_days(p: Path):
    try:
        return (TODAY - date.fromtimestamp(p.stat().st_mtime)).days
    except OSError:
        return None


def read(p: Path):
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


# --- 1. Chronicle -----------------------------------------------------------
out = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT,
                     capture_output=True, text=True).stdout.strip()
if out:
    lines = out.splitlines()
    add("Uncommitted work", f"{len(lines)} path(s) not committed",
        [l.strip() for l in lines[:8]], "LOW")

# --- 2. State freshness -----------------------------------------------------
state = ROOT / "desk/state.md"
a = age_days(state)
if a is None:
    add("Missing state", "desk/state.md does not exist", severity="LOW")
elif a > STALE_STATE:
    add("Stale state", f"desk/state.md is {a}d old (arrival is its primary writer)",
        severity="LOW")

# --- 3. Bright sweep age ----------------------------------------------------
bright = ROOT / "desk/boom/bright.md"
btxt = read(bright)
m = re.search(r"Last swept:\s*(\d{4}-\d{2}-\d{2})", btxt)
sweep_date = None
if m:
    sweep_date = date.fromisoformat(m.group(1))
    a = (TODAY - sweep_date).days
    if a > STALE_SWEEP:
        add("Bright unswept", f"last swept {m.group(1)} — {a}d ago")

# --- 3b. Stale Alive --------------------------------------------------------
# The sweep age above reads bright's header and never looks inside the file.
# For four months that reported a tidy "unswept Nd" while Alive held 120
# entries, 54 of them last dated April and 57 carrying no date at all — the
# section whose whole contract is "re-chosen each sweep or released". The
# header is not the content; a file swept yesterday can be full of items
# nobody has re-chosen since spring.
ALIVE_STALE_DAYS = 60

alive = ""
mm = re.search(r"^## Alive\b(.*?)^## ", btxt, re.S | re.M)
if mm:
    alive = mm.group(1)

if alive:
    entries = [l for l in alive.splitlines() if l.startswith("**")]
    stale, undated = [], 0
    for e in entries:
        found = re.findall(r"20\d{2}-\d{2}-\d{2}", e)
        if not found:
            undated += 1
            continue
        try:
            newest = max(date.fromisoformat(d) for d in found)
        except ValueError:
            continue
        a = (TODAY - newest).days
        if a > ALIVE_STALE_DAYS:
            title = re.match(r"\*\*(.+?)\*\*", e)
            stale.append(f"{(title.group(1) if title else e[:60])[:70]} ({a}d)")

    if stale:
        add("Stale Alive", f"{len(stale)} of {len(entries)} Alive entr(ies) not re-chosen in "
                           f"{ALIVE_STALE_DAYS}d", sorted(stale, key=lambda s: -int(s.rsplit("(",1)[1][:-2])))
    if undated:
        # Undated entries cannot age, so no staleness rule will ever reach
        # them. Report the count rather than letting them sit outside every
        # check — an item exempt from measurement is not an item that passed.
        add("Undated Alive", f"{undated} of {len(entries)} Alive entr(ies) carry no date — "
                             f"unageable, invisible to every staleness check",
            severity="LOW")

# --- 3c. Seed Bank review ---------------------------------------------------
# The Seed Bank is deliberately not on the sweep clock — sitting still is its
# job, and the Stale/Undated checks above deliberately stop before it. That
# exemption is only honest if something still looks at it on its own cadence.
# An exempt section with no check is just the old problem with a better label.
SEED_REVIEW_DAYS = 90

ms = re.search(r"^## Seed Bank\b.*?Last reviewed:\s*(\d{4}-\d{2}-\d{2})", btxt, re.S | re.M)
if ms:
    a = (TODAY - date.fromisoformat(ms.group(1))).days
    if a > SEED_REVIEW_DAYS:
        add("Seed Bank unreviewed", f"last reviewed {ms.group(1)} — {a}d ago "
                                    f"(quarterly cadence)", severity="LOW")
elif "## Seed Bank" in btxt:
    add("Seed Bank undated", "Seed Bank exists but carries no 'Last reviewed' date — "
                             "exempt from the sweep clock and from every other check too", severity="HIGH")

# --- 4. Crucible keeper dormancy -------------------------------------------
# Until 2026-08-01 this globbed desk/boom/*.md — the eight TOPIC files — and
# reported them under the name "Crucibles unstirred". The eight actual
# crucibles are one directory down, in desk/boom/crucibles/, and this check
# had never looked at them. Stirring a crucible left the output byte-identical.
#
# It also reads the `Last stirred:` header the crucible keeper maintains,
# not mtime: mtime moves on any edit, including a typo fix, so it would
# report a crucible tended when nothing had been added to it.
STALE_CRUCIBLE = 30   # crucibles accumulate slowly on purpose — "the heat is time"

cold, unreadable = [], []
for p in sorted((ROOT / "desk/boom/crucibles").glob("*.md")):
    if p.name == "README.md":
        continue
    mc = re.search(r"Last stirred:\**\s*(\d{4}-\d{2}-\d{2})", read(p))
    if not mc:
        # No parseable header means unmeasured, which is not the same as fresh.
        unreadable.append(p.name)
        continue
    a = (TODAY - date.fromisoformat(mc.group(1))).days
    if a > STALE_CRUCIBLE:
        cold.append(f"{p.name} ({a}d)")

if cold:
    add("Crucibles cold", f"{len(cold)} of 8 crucible(s) unstirred >{STALE_CRUCIBLE}d", cold)
if unreadable:
    add("Crucibles unmeasured", f"{len(unreadable)} crucible(s) have no parseable "
                                f"'Last stirred' header — not checked, not clean",
        unreadable, "HIGH")

# The topic files are a separate surface with a separate cadence — they are
# where buffer material lands between sweeps, not where particles accumulate.
if sweep_date:
    dormant = []
    for p in sorted((ROOT / "desk/boom").glob("*.md")):
        if p.name in ("bright.md", "README.md"):
            continue
        a = age_days(p)
        if a is not None and a > STALE_SWEEP:
            dormant.append(f"{p.name} ({a}d)")
    if dormant:
        add("Topic files cold", f"{len(dormant)} topic file(s) older than {STALE_SWEEP}d",
            dormant, "LOW")

# --- 5. Proposal spores -----------------------------------------------------
stale_props = []
for p in sorted((ROOT / "desk/proposals").glob("*.md")):
    a = age_days(p)
    if a is not None and a > STALE_PROPOSAL:
        stale_props.append(f"{p.name} ({a}d)")
if stale_props:
    add("Proposal spores", f"{len(stale_props)} loose proposal(s) older than {STALE_PROPOSAL}d",
        stale_props)

# --- 6. Floor zombies -------------------------------------------------------
stale_drafts = []
for p in sorted((ROOT / "floor/drafts").glob("*.md")):
    a = age_days(p)
    if a is not None and a > STALE_DRAFT:
        marker = " [SUPERSEDED]" if "SUPERSEDED" in read(p)[:4000].upper() else ""
        stale_drafts.append(f"{p.name} ({a}d){marker}")
if stale_drafts:
    add("Floor zombies", f"{len(stale_drafts)} draft(s) older than {STALE_DRAFT}d",
        stale_drafts)

# --- 7. Expired deadlines ---------------------------------------------------
# The signal a human eye slides over: a sentence that was true when written and
# quietly became false. "Rube MCP sunsetting May 15, 2026" read as live for two
# and a half months after the date passed.
# The boundary has to be on BOTH sides. With `\b` only after the group,
# "Depends on" matched "ends" and reported a completed milestone as an overdue
# deadline. Bare "by" and "end" are dropped as too common to carry signal.
DEADLINE = re.compile(
    r"\b(before|until|deadline|expires?|sunsett?ing|due)\b[^.\n]{0,60}?"
    r"(\d{4}-\d{2}-\d{2}|"
    r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4})",
    re.IGNORECASE)

def parse_when(s):
    s = s.strip().rstrip(",")
    for fmt in ("%Y-%m-%d", "%b %d %Y", "%B %d %Y", "%b %d, %Y", "%B %d, %Y"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None

expired = []
scan_files = [bright] + sorted((ROOT / "desk/intentions/active").glob("*.md"))
for p in scan_files:
    for i, line in enumerate(read(p).splitlines(), 1):
        if len(line) > 600:
            continue
        for kw, when in DEADLINE.findall(line):
            # `(2026-04-11)` in this practice means "captured on", not "due by".
            # Without this, every dated bright entry containing the word
            # "before" reads as an overdue commitment.
            if f"({when})" in line:
                continue
            d = parse_when(when)
            if d and d < TODAY - timedelta(days=1):
                expired.append(f"{p.relative_to(ROOT)}:{i} — {kw} {when} ({(TODAY-d).days}d past)")
if expired:
    add("Expired deadlines", f"{len(expired)} line(s) reference a date already passed",
        expired[:10], "HIGH")

# --- 9. Zombie habitats -----------------------------------------------------
dormant_names = {p.stem for p in (ROOT / "desk/intentions/dormant").glob("*.md")}
dormant_names |= {p.stem for p in (ROOT / "desk/intentions/completed").glob("*.md")}
# Only the sections that assert something is current. Resolved and Box Routed
# are the record of what was retired, and retiring an entry properly means
# naming the dormant intention it went to — so scanning the whole file turns
# every correct retirement into a permanent hit. A check that fires at the act
# of tidying teaches you to stop recording destinations, or to stop reading the
# check. Line numbers stay true because this is a prefix, not a filter.
active_region = btxt.split("\n## Resolved", 1)[0]

zombies = []
for name in sorted(dormant_names):
    hits = [f"{i}" for i, line in enumerate(active_region.splitlines(), 1)
            if re.search(rf"\b{re.escape(name)}\b", line)]
    if hits:
        zombies.append(f"{name} — bright.md lines {', '.join(hits[:4])}")
if zombies:
    add("Zombie habitats", f"{len(zombies)} dormant/completed intention(s) still named in bright",
        zombies)

# --- report -----------------------------------------------------------------
if AS_JSON:
    print(json.dumps({"date": TODAY.isoformat(), "findings": findings}, indent=2))
    sys.exit(0)

print(f"Rot radar — {TODAY.isoformat()}")
print()
if not findings:
    print(f"{GRN}Clean. No decay signals.{NC}")
    sys.exit(0)

order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
for f in sorted(findings, key=lambda x: order.get(x["severity"], 1)):
    col = RED if f["severity"] == "HIGH" else (YEL if f["severity"] == "MEDIUM" else DIM)
    print(f"{col}[{f['severity']}] {f['signal']}{NC} — {f['detail']}")
    for it in f["items"][:6]:
        print(f"    {it}")
    if len(f["items"]) > 6:
        print(f"    {DIM}… and {len(f['items']) - 6} more{NC}")
    print()

print(f"{len(findings)} signal group(s). Nothing was changed — routing is the Mage's.")
sys.exit(0)
