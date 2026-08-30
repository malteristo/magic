#!/usr/bin/env python3
"""rot_radar.py — mechanical pass over the workshop's decay signals.

`cast_tend_workshop.md` §4b describes a rot radar as a table of signals to scan
by hand. Scanning it by hand is how a signal gets missed on a tired evening, and
how an action item with a deadline three months past keeps reading as live. This
is the same table, executed.

It reports. It does not fix anything, and it never edits `desk/`.

    ./scripts/rot_radar.py             # full pass
    ./scripts/rot_radar.py --quiet     # findings only, no clean lines
    ./scripts/rot_radar.py --json      # machine-readable
    ./scripts/rot_radar.py --self-test # positive control on the date parser

Exit 0 always: a radar is not a gate.
"""

import ast
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

# --- 4. Crucible keeper dormancy (RETIRED 2026-08-10) ----------------------
# Living crucibles moved to desk/boom/_retired/crucibles/. Seed Bank + topics
# carry the long-horizon role. Do not reintroduce cold/unmeasured checks unless
# a new accumulative shelf is deliberately opened.

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

# --- 10. Superseded surfaces ------------------------------------------------
# The class: a canonical surface moves, the new home gets written, and every
# file that *routes* readers to the old one keeps routing. No single file is
# wrong — the practice just keeps answering a question that was retired. It is
# invisible precisely because each router reads as confident and correct.
#
# Found 2026-08-25: `mage_seal.md.template` still told every new Mage to keep a
# connected-services inventory in their Seal, seven months after that inventory
# moved to connections.md, in a workshop where `mage_seal.md` no longer exists.
# Five more files still pointed at the dead surface, including the self-check,
# which asked Spirit to confirm awareness of "Open Portals as defined in
# AGENTS.md" — where they had not lived since the August lean.
#
# Wire-before-mechanism does not apply here, by the 2026-08-14 exception: the
# wire asks a reader to *remember* that a surface moved, and remembering is the
# thing that decays. A row costs one line. Not having the row cost seven months.
#
# Add a row whenever you supersede a surface or retire a name.
SUPERSEDED = [
    # (pattern, what it wrongly teaches, where the truth lives now)
    (r"open portals",
     "a connected-service inventory living in the Seal / AGENTS.md",
     "desk/config/connections.md § MCP Topology"),
    # Not `\bRube\b`. The boundary has to reject letters on both sides but
    # allow `_`, or `rube_mcp_integration` reads as a word break and passes.
    # It must still reject "Rubedo" — the alchemical term, which is a real word
    # in this library and has nothing to do with the gateway. Both cases were
    # live in the tree on 2026-08-25 and the naive pattern got each one wrong.
    (r"(?<![A-Za-z])Rube(?![A-Za-z])",
     "the pre-2026 name of the Composio gateway (sunset May 2026)",
     "Composio"),
    # Composio was Forge's MCP gateway until 2026-08-26, when Cursor shipped a
    # plugin marketplace and he moved Gmail and X onto native plugins, then
    # disabled the gateway. **Corrected at his read the same afternoon:** the
    # first version of this row said Perplexity search and the GitHub MCP
    # "went with it." They did not — he had disabled both on Composio well
    # before, and neither was missed (built-in WebSearch had improved; GitHub
    # runs through the `gh` CLI). Only Gmail and X moved on 08-26. The stale
    # lines below are still stale; the cause was mine to get wrong, and a
    # shared date is not a shared reason.
    #
    # Deliberately NOT a bare `Composio`. The word has to keep working in the
    # file that explains the migration and in prose about what Composio used
    # to do — "Composio is disabled", "the Composio path", "Composio's Gmail
    # surface" are all correct sentences. Only the *routing* forms are stale:
    # a scroll telling a reader to reach a capability through it.
    # Slug branch is the real tool prefixes, not `COMPOSIO_[A-Z]`. The broad
    # form matched `composio_integration` — a field name in a portal manifest,
    # which routes nobody anywhere — because the whole table runs IGNORECASE.
    (r"(?i)(?:via|through|using|Forge's)\s+Composio"
     r"|Composio\s+(?:MCP|GitHub|Gmail|Search|gateway)"
     r"|COMPOSIO_(?:SEARCH|MULTI|EXECUTE|MANAGE|WAIT|GET|REMOTE)",
     "a capability reachable through the Composio gateway — disabled on Forge "
     "2026-08-26 (retained, not deleted, by his decision)",
     "desk/config/connections.md § MCP Topology — Gmail and X via Cursor "
     "Marketplace plugins; GitHub via `gh` CLI (Cursor's native GitHub "
     "integration as account-level fallback); web search via built-in "
     "WebSearch"),
]

# Paths whose job is to hold the old words: the record of what was, not
# instruction about what is. A chronicle that stopped saying "Rube" would be a
# falsified chronicle.
FOSSIL = ("archive/", "floor/archive/", "floor/chronicles/", "desk/archive/",
          "desk/sessions/", "desk/research/", "box/", "desk/outfacing/twitter/",
          "desk/proposals/archived/", "desk/intentions/archive/")

# Surfaces that *instruct*: the ones a stranger learns the practice from.
def instruction_surfaces():
    seen, out = set(), []
    for pat in ("AGENTS.md", "CLAUDE.md", "ONBOARDING.md", "*.template",
                "system/**/*.md", "library/**/*.md", "scripts/*.py"):
        for p in ROOT.glob(pat):
            if p.is_file() and p not in seen:
                seen.add(p)
                out.append(p)
    return sorted(out)

stale_routes = []
for p in instruction_surfaces():
    rel = str(p.relative_to(ROOT))
    if any(rel.startswith(f) or f"/{f}" in f"/{rel}" for f in FOSSIL):
        continue
    if rel == "scripts/rot_radar.py":  # this file names the patterns it hunts
        continue
    lines = read(p).splitlines()
    for i, line in enumerate(lines, 1):
        # A supersession note is the correct way to leave a dead word behind:
        # it teaches the reader that the word is dead. Exempt it, so that
        # documenting a move is never the thing that trips the check.
        #
        # Window, not line: prose wraps. The first run of this check flagged
        # its own supersession note in mage_seal.md.template, because the word
        # "superseded" landed one line below the word being superseded.
        lo, hi = max(0, i - 4), min(len(lines), i + 3)
        if any("supersed" in l.lower() for l in lines[lo:hi]):
            continue
        for pat, teaches, now in SUPERSEDED:
            if re.search(pat, line, re.IGNORECASE):
                stale_routes.append(f"{rel}:{i} — teaches {teaches}; now: {now}")
if stale_routes:
    add("Superseded surfaces",
        f"{len(stale_routes)} line(s) in instruction surfaces still route to a retired surface or name",
        stale_routes[:10], "HIGH")

# --- 12. Bearings whose Next has a date already past ------------------------
# `bearings.md` calls itself "the one orientation surface — read first at every
# arrival, on every substrate", and nothing checked it. Section 7 scans bright
# and active intentions; bearings sits in desk/intentions/ and fell between.
#
# Found 2026-08-25: the health bearing's Next read "Tuesday 18.08, 15:00 —
# first appointment" seven days after it happened, still in the future tense, on
# the most load-bearing private bearing there is. Section 7 would have missed it
# twice over — no deadline keyword ("first appointment" is not "due"), and a
# German date it cannot parse.
#
# He writes this file; Spirit drafts and never silently edits. So this reports
# and the line stays his.
BEARINGS = ROOT / "desk/intentions/bearings.md"

# `[k]` 2026-08-13 is provenance — when he wrote the line, not a deadline in it.
# Without stripping these, every bearing reports as overdue on the day after it
# was written, and the check gets ignored inside a week.
PROVENANCE = re.compile(r"`\[[^\]]*\]`\s*\d{4}-\d{2}-\d{2}(?:\s*/\s*\d{2}-\d{2})*")

# German dates, conservatively. `18.08.` (trailing dot) and `18.08.2026` are
# unambiguous. Bare `18.08` is only read as a date when the line also carries a
# clock time — otherwise "1.5 years" and version numbers parse as spring dates.
# Deliberate: a bare day.month with no other signal is left unmatched rather
# than guessed at. Better a missed line than a check nobody trusts.
DE_DATE = re.compile(r"(?<!\d)(\d{1,2})\.(\d{1,2})\.?(\d{4})?(?!\d)")
CLOCK = re.compile(r"\b\d{1,2}:\d{2}\b")
ISO = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")

# Paths and code spans carry dates that are names, not deadlines. The health
# bearing points at `desk/mirror/2026-08-18-ersteinschaetzung-anker.md`, and the
# first version of this check reported that filename as the overdue move — right
# answer, wrong reason, and it would have fired on any bearing citing a dated
# file. The control caught it; the live run did not, because the live run had a
# genuinely stale bearing sitting underneath the false match.
CODE_OR_PATH = re.compile(r"`[^`]*`|\S*/\S*")

def _bearing_dates(line: str):
    """Every date in a Next line, provenance removed. Year-less → this year."""
    clean = CODE_OR_PATH.sub(" ", PROVENANCE.sub("", line))
    out = []
    for y, m, d in ((y, m, d) for y, m, d in ISO.findall(clean)):
        try:
            out.append(date(int(y), int(m), int(d)))
        except ValueError:
            pass
    bare_ok = bool(CLOCK.search(clean))
    for d, m, y in DE_DATE.findall(clean):
        if not y and not bare_ok:
            continue
        try:
            out.append(date(int(y) if y else TODAY.year, int(m), int(d)))
        except ValueError:
            pass
    return out

# Positive control, kept rather than performed once. This parser has already
# been wrong in a way a live run could not show: it reported the right date for
# the wrong reason (an ISO date inside a filename) while silently failing to
# read the German date that was actually stale. A clean live run proved nothing,
# because a genuinely stale bearing sat underneath the false match.
#   ./scripts/rot_radar.py --self-test
_BEARING_CASES = [
    ("provenance only", "- **Next** — Reception, in the room. `[k]` 2026-08-09", []),
    ("provenance with range", "- **Next** — Eval design `[k]` 2026-08-08 / 08-13", []),
    ("german bare + clock",
     "- **Next** — **Tuesday 18.08, 15:00 — first appointment.** confirmed 12.08. `[k]`",
     ["2026-08-18", "2026-08-12"]),
    ("fraction, no clock", "- **Next** — for 1.5 years I was busy `[k]`", []),
    ("iso future", "- **Next** — deadline 2026-11-11 `[k]` 2026-08-13", ["2026-11-11"]),
    ("german with year", "- **Next** — Termin am 19.11.2026 `[k]`", ["2026-11-19"]),
    ("date inside a path", "- **Next** — see desk/mirror/2026-08-18-anker.md `[k]`", []),
    ("date inside a code span", "- **Next** — see `notes/2026-01-01.md` `[k]`", []),
]

if "--self-test" in sys.argv:
    ok = True
    for why, line, want in _BEARING_CASES:
        got = sorted(d.isoformat() for d in _bearing_dates(line))
        good = got == sorted(want)
        ok &= good
        print(f"  {'ok  ' if good else 'FAIL'} {why}: {got}")
    print(f"\n{'self-test passed' if ok else 'SELF-TEST FAILED'}")
    sys.exit(0 if ok else 1)

stale_bearings = []
if BEARINGS.exists():
    current = None
    for i, line in enumerate(read(BEARINGS).splitlines(), 1):
        if line.startswith("### "):
            current = line[4:].strip()
        if not line.lstrip("- ").startswith("**Next**"):
            continue
        # One entry per Next line, not per date: "Tuesday 18.08 … confirmed
        # 12.08" is a single stale move with a supporting date beside it, and
        # reporting it twice is how a HIGH row starts getting skimmed.
        past = sorted({d for d in _bearing_dates(line) if d < TODAY - timedelta(days=1)})
        if past:
            newest = past[-1]
            extra = f" (also names {', '.join(d.isoformat() for d in past[:-1])})" if len(past) > 1 else ""
            stale_bearings.append(
                f"{current or '?'} — bearings.md:{i} names {newest.isoformat()} "
                f"({(TODAY - newest).days}d past) as its next move{extra}")
if stale_bearings:
    add("Bearing next past",
        f"{len(stale_bearings)} bearing(s) point at a date that has already gone",
        stale_bearings, "HIGH")

# --- 11. The radar's own documentation --------------------------------------
# `cast_tend_workshop.md` §4b says "the table below is what it checks", and a
# reader believes it. Twice now it has been false. On 2026-08-01 it promised
# four checks that did not exist and omitted six that did — Alive went unwatched
# for four months while the report came back tidy. On 2026-08-25 a new check was
# added and its row was not, by the same Spirit, in the same hour, during work
# whose entire finding was that documentation keeps answering retired questions.
#
# Remembering is what failed both times. So the script reads its own signal
# names out of its own AST and checks them against the table. Prose about a
# script is part of the script when the prose is what a human acts on.
SIGNAL_DOC = ROOT / "system/flows/maintenance/cast_tend_workshop.md"

# Signals deliberately folded into a grouped row instead of getting their own.
# Written down so "decided" stays distinguishable from "forgot" — that being the
# distinction whose absence made the 2026-08-01 defect invisible.
DOC_GROUPED = {
    "Missing state": "Stale/missing state",
    "Stale state": "Stale/missing state",
}

try:
    _self = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    emitted = {
        n.args[0].value
        for n in ast.walk(_self)
        if isinstance(n, ast.Call)
        and getattr(n.func, "id", None) == "add"
        and n.args
        and isinstance(n.args[0], ast.Constant)
        and isinstance(n.args[0].value, str)
    }
except (OSError, SyntaxError):
    emitted = set()

doc_text = read(SIGNAL_DOC)
if doc_text:
    undocumented = sorted(s for s in emitted if DOC_GROUPED.get(s, s) not in doc_text)
    if undocumented:
        add("Radar undocumented",
            f"{len(undocumented)} signal(s) the script can emit are absent from "
            f"the §4b table in {SIGNAL_DOC.relative_to(ROOT)}",
            undocumented, "HIGH")

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
