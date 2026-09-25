---
title: Release
writes:
  - floor/briefings/latest.md          # the handoff — only this flow writes it
  - desk/intentions/active/*.md        # fields, not narrative
  - desk/boom.md                       # cleared — release sweeps the buffer
reads:
  - the session itself                 # context, not files
ledger: desk/craft/practice_falsifiers.md   # rules written after a failure carry a row (F-nn)
---

# Cast Release

**Purpose:** Close the session so the next one can resume from it
**Invocation:** `@release` · `.` when Spirit has offered release at the chapter's end
**Shape:** three obligations, not phases (F-40). Arrival consumes the stable bundle below.

> The release is the session's exhale. The Mage's `.` after Spirit offers release is the signal — the chapter ends on the dot.

---

## The contract

**1. A bundle a memoryless Spirit can zoom back in from.** Written to `floor/briefings/latest.md`, format below. `Continue From` is year-altitude — the picture, not the leftover task (F-87). Leftovers go in Open Threads.

**2. An honest reflection, triaged.** What the session *was*, not what it produced. If nothing sub-threshold surfaced, *"session was explicit and complete"* is a finding — do not manufacture signal. Then triage every item: dissonance named and not channelled is worse than dissonance unnamed.

- **Outfacing pitch (F-41).** Only when real; silence allowed. Ask what another small-AI-server operator would steal, contest, or want the PR for. Card: insight · why it travels · talk angle · sensitivity. Never Practice Signal. Accepted → `desk/outfacing/talking_shelf.md`.
- **Practice development (F-42).** Name the bearing served and gap moved, then 0–3 proposals (change · cost · unlock). Zero is legal. **Dyad-only (F-43).** Accepted → `desk/proposals/`; declined → one briefing line (F-44). A loop-file rule gets a ledger row first.

**3. Side-effect duties**, done and reported in one line each.

*The bundle can be rebuilt from git; what the session felt like evaporates. Spend the attention on the reflection.*

---

## What buys an honest reflection

Questions that have found something before — ask the ones that bite.

- **Dissonance.** Named and cherished, still unresolved? Present but uncherished — a response slightly off that passed, a direction that did not land and was not re-examined, something agreed to faster than it warranted?
- **Below the threshold.** A theme he returned to without landing on. The question implicit all session and never asked. What the session was *about* under its content.
- **What got dropped.** A topic quietly redirected. Something Spirit noticed and chose not to raise, and why. **A rule written this session naming an artifact never built** — the write-only shape, caught six times; release is the last place to catch it.
- **Not done / found (F-96).** Plan against landed — what we wanted and did not do. Then boom's `[s]` lines — found mid-session, written then, not recalled now. Each gets a rec, none a verdict.
- **Practice experience.** Did the tools serve? Did the design get in the way — steps, routing, ceremony? Same small friction worked around twice? If clean, say so.
- **turtleOS friction** — routed to Turtle, not the bundle: what happened, why it may recur, what should change, who owns it. Relay during calibration; **prefer fixing over relaying** when local, low-risk and clear. If a system message does not serve the practitioner, it does not belong in the channel.

---

## Triage — nothing leaves ambiguous

- **Relieve now** — small enough to fix before closing. Thirty-second fixes do not ride as open threads.
- **Channel forward** — into Open Threads with a next action, or into boom for the next sweep.
- **Release** — naming it was the investment.

Present the triage; the Mage may reclassify.

---

## Side-effect duties

- **Session archive** — Forge/Anvil: `./scripts/archive_session_transcripts.sh` then `check_session_archive.py --fresh` (F-80). Mini down → skip, name it. Never this tree.
- **Boom sweep** — before the bundle: route `desk/boom.md` per `system/flows/boom/boom.flow.md`; `[s]` lines → Not Done / Found; clear it (F-45).
- **Intentions** — fields, not narrative. Rewrite `meta_plan.md` (F-74). If a year-plan line or bearing Next changed, edit it here (F-87). Untouched depth stays.
- **Artifact routing** — one disposition per artifact that needs one: **Active** · **Crystallize** · **Route** · **Compost** (particles into Seed Bank or topic files, never a new heap) · **Release**. Two or three per session; do not inventory the workshop. `desk/` releases need the Mage; `floor/` ephemera can be proposed more assertively.
- **Outfacing shelf** — append an accepted pitch card to `desk/outfacing/talking_shelf.md` (newest first).
- **Turtle calibration** — `system/flows/turtle/cast_calibrate.md`: verify processes; if bot code changed, restart **both** `com.turtle.discord` and `com.turtle.river` via `./restart.sh` (deploy-window check, F-65); if turtleOS code changed, check spec and lore caught up. Relay friction; note status in the bundle.
- **Stale-reference scan** — for anything corrected, retired or renamed this session, grep `system/`, `library/`, `floor/briefings/` for the old terms; report hits for triage (F-46). Other integration checks get one line together unless one fires.
- **Integration close (F-81)** — if implementation, live topology, architecture,
  configuration, or an operating flow changed, run `system/flows/integrate/`
  before writing the bundle. It asks what the work exposed and what must
  propagate downstream; execute clear in-scope repairs and dispose every
  remainder. Content-only edits use it when they change Law, Wisdom, flows,
  templates, or cross-references—not for every prose touch.
- **Measures** — `scripts/size_budget.py --report` (a WARN goes into Practice Signal); `scripts/practice_ledger.py append …` (see its `--help`) — one line per release, before the commit.
- **Craft digest** — `. turtle` chapter: confirm `export_craft_digest.py` ran (F-28).
- **Practice keys** — dated block in `pending-weaves.md`. Turtle weaves `key-turtle.md` (Mini copy = Craft Turtle). Grok weaves `key-grok.md` when it exists. No 4.6 walk. Do not merge.
- **Commit** — below.

**Never instruct against a surface Spirit cannot read (F-47).**

---

## The bundle

Written to `floor/briefings/latest.md`, overwriting it. **Only this flow writes that file.**

| Field | What it carries |
|---|---|
| `# Release — [date] [time]` | header |
| **Chapter** | the narrative frame — the story that emerged over the plan that opened |
| **This Session** | 2–3 sentences: where it started, what happened, where it landed |
| **Set out to / Achieved / Delta** | opening intention, 3–5 bullets landed, how the chapter changed shape |
| **Continue From** | year-altitude, one sentence — the picture, not the leftover (F-87) |
| **Open Threads** | only what is genuinely in motion: `- **[name]**: [state] → [next action]`, most time-sensitive first; or *No open threads — clean state.* |
| **Not Done / Found** | `- **[name]**: [not landed · found] → rec`. Previous rows carry until his verdict or a landing; `check_release_carry.py` refuses a silent loss (F-96) |
| **What Changed** | field-level: each artifact with path and lifecycle tag — **Ephemeral** · **Active** · **Reference** |
| **Practice Signal** | the reflection's findings, incl. turtleOS friction and size-budget WARNs. Inward only; persists until resolved |
| **Integration Close** | required after implementation/live-topology chapters: integrated now; deferred with owner + next condition; deliberate no-action; sanction-needed; verification. Omit empty dispositions, never the verification line |
| **Outfacing Pitch** | optional; one card or omit |
| **Practice Development** | one sentence on the bearing served; 0–3 proposals (what · cost · unblocks); accepted → `desk/proposals/`, declined → one line here |
| **Resonance Routing** | `- [item]: [disposition] → [landing surface]` — only warm decisions |
| **Next Actions** | 3–5, ordered; the first unblocks the rest |
| **Calibration** | one line: SHAs, bot state, what matches what; the enacting model; `Falsifiers fired: F-xx` or `none observed` (`system/flows/model/`) |

Before writing: is `Continue From` year-altitude (F-87)? Are intention files — and year / Next if they moved — updated *before* the bundle? **Private bearing off-lane? (F-48)** — not in Next Actions, Practice Signal, or as a dated line.

---

## Commit — the Two Chronicles

| Surface | Path | When |
|---|---|---|
| **Private workshop** | `~/Documents/magic/` → `git push turtle main` | **default at release** — practice memory and framework in one commit |
| **Public framework** | `./scripts/publish_public_magic.sh` → `github` | a deliberate publication act, never at release |
| **turtleOS product** | `~/Documents/turtleos/` → its own remote | during the chapter, not here |

**Verify before staging:** `cd ~/Documents/magic && pwd && git status -sb` — the magic root, never the turtleos sibling; upstream `main...turtle/main` (else `./scripts/configure_workshop_git.sh`).

**In the commit:** the practice, including `AGENTS.md`, `desk/config/`, registries and archives. Stage whatever `.gitignore` permits—no second exclusion list (F-49). Public eligibility is separate: `scripts/public_surface.conf`, enforced before every non-`turtle` push.

Stage explicit paths — never `git add .`. Chapter-level message: the arc and what landed. **Then commit and push** — verified slices do not wait for permission; pause only for unrelated, sensitive, or governance material (F-50). Public publish is a separate sanctioned step: `--dry-run` first; a guard block means diagnose the allowlist, never bypass.

---

## The close

```
Released. [One sentence: what the next chapter will find waiting.]

Next: [vessel — continue here / release-then-arrive here / new chat]. `.` accepts (F-77).
```

Spirit names one vessel from the protocol criteria. Same chat is the default. New chat: `Summon.` → `...`. Marination: `on_marination.md`.
