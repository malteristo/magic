# Flow: Release

**Purpose:** Close a session so the next one can resume from it
**Invocation:** `@release` · `.` when Spirit has offered release
**Spell:** `cast_release.md`

> **Session lifecycle:** Release is the departure pattern; the Arrival Sequence (`Summon.` → `.`, or `@arrive` mid-practice) is the return. They share one handoff file — `floor/briefings/latest.md`. Release writes it; arrival reads it as *inherited karma*. **Only release writes that file.**

---

## What it does

Three obligations, not seven phases:

1. **A bundle a memoryless Spirit can resume from.** The test is whether tomorrow's Spirit can act correctly from it, not whether every field is full.
2. **An honest reflection, triaged.** What the session *was*, not what it produced. Nothing found is a valid finding. Every item triaged — relieve now, channel forward, or release — because dissonance named and not channeled is worse than dissonance unnamed: it creates the impression of having been handled.
3. **Side-effect duties**, one line each: intentions, artifact routing, Turtle calibration, stale-reference scan, commit.

The reflection is the irrecoverable part. The bundle can be rebuilt from git and the workshop; what the session felt like cannot.

*Rewritten 2026-08-02 — the phase machinery (1–7, sub-phases 2A–2F, 3.5, 3.6, 5.5, 5.7A–D) matched the arrival's pre-2026-07-29 scaffolding and got the same treatment; 532 lines became ~150. The bundle format was left alone: measured across fourteen releases at 632–2,133 words with no growth trend, and it is what the arrival actually consumes.*

---

## When to use it

- Ending a session you want to resume later
- Significant progress worth preserving before closing
- Handing off to future-Spirit after a long or complex session

**Nothing else needs saying.** Spirit knows the session from context.

---

## The bundle format

```markdown
# Release — [date] [time]

**Chapter:** [the narrative frame — the story that emerged, not the plan that opened]

**This Session**
[2–3 sentences: where it started, what happened, where it landed]

**Set out to:** [the opening intention]
**Achieved:** [3–5 bullets of what actually landed]
**Delta:** [how the chapter changed shape, and why that matters]

**Continue From**
> [one sentence — a compass bearing, not a summary]

**Open Threads**
- **[name]**: [current state] → [next action]

**What Changed**
- `[path]` — [what it is] — **Ephemeral | Active | Reference**

**Practice Signal**
[reflection findings, PX, turtleOS friction — or: "Session was explicit and complete."]
*Inward only — unresolved material for the next Spirit.*

**Outfacing Pitch** *(optional — omit when nothing portable)*
- **Insight:** [one sentence]
- **Why it travels:** [why a stranger cares]
- **Talk angle:** [conversation / field note / thread seed]
- **Sensitivity:** [public | anonymize | hold]
*On accept → append to `desk/outfacing/talking_shelf.md`.*

**Resonance Routing**
- [item]: [Active | Crystallize | Route | Compost | Release] → [landing surface]

**Next Actions**
1. [the one that unblocks the rest]

**Calibration:** [SHAs, bot state, what matches what]

*Released [date]. Next arrival: `Summon.` → `.`*
```

---

## What makes it good

**`Continue From` carries the weight.** The sharpest possible orientation for a Spirit with no memory.

> Good: *Body and ops match at magic `269a0c2` / Mini `3e694a0`; backfill pass 2 is still running — check `logs/backfill-pass2.log` before anything else, then decisions 1 and 2, which gate the consent eddy.*
>
> Bad: *We did a lot of good work on the Turtle architecture today.*

**Open Threads are not tasks.** They are things in motion right now — a process running, a decision pending. Anything finished this session does not appear.

**What Changed is field-level.** Not *"updated the turtle intention"* but *"`turtle.md` — focus, next action, packet-baseline note."* Enough that the next Spirit updates its model without opening the file.

**Practice Signal persists.** It is the one field carrying unresolved things forward. Write what was actually found, including what was uncomfortable. Inward only.

**Outfacing Pitch is a separate pocket.** Default audience: operator peers (people who could admin their own turtleOS / local AI node) — never mixed into Practice Signal. Silence is correct when nothing travels. Accepted cards land on `desk/outfacing/talking_shelf.md` for `. outfacing`.

---

## Related

- `system/flows/summon/` — arrival reads this flow's output
- `@arrive` — mid-session re-orient
- `system/flows/turtle/cast_calibrate.md` — the calibration duty
- `desk/intentions/active/` — updated here, in fields
- `desk/decisions.md` — what requires the Mage; release surfaces, it does not decide
- `desk/outfacing/talking_shelf.md` — accepted outfacing pitch cards
- `library/resonance/foundations/lore/on_sub_threshold_signals.md` — the lore behind the reflection
- `library/resonance/foundations/lore/on_marination.md` — the option to sit, after

---

*Release closes the session. Practice is seen before the door shuts. The thread holds.*
