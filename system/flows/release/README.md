# Flow: Release

**Purpose:** Close a session cleanly — reflect on what the session was, update intentions, crystallize threads, integrate artifacts, enable seamless resumption  
**Invocation:** `@release`

> **Session lifecycle:** Release is the departure pattern. Recall (`@recall`) is the arrival pattern. They share a single handoff file: `floor/briefings/latest.md`. When you say `@release`, Spirit distills the session into a resumable bundle. When you say `@recall` in the next session, that bundle orients the opening.

---

## What This Flow Does

Release does five things, in order:

**1. Surveys the session** — from context: what was touched, what was completed, what is in motion.

**2. Reflects on the session as practice** — looks at how the session moved, not just what was built. Surfaces sub-threshold signals: dissonances that went uncherished, patterns that were present below the naming threshold, deflections, what seemed to matter more than the words indicated. These signals would evaporate without this pass; the act of looking invests tokens into them so they can emerge.

**3. Updates intentions** — writes what actually changed to the intention files. Not a narrative summary. Actual field updates: current focus, next action, blockers, completed goals. The intention files should reflect this session's end state, not where they were at the start.

**4. Writes the release bundle** — a structured artifact in `floor/briefings/latest.md` that includes a "Practice Signal" field carrying any sub-threshold findings into the next session. Compact, dense, oriented toward resumption.

**5. Checks system integration** — for any new lore, flows, or structural artifacts created this session, runs a lightweight ripple check (what else in the system needs to know this exists?). Invokes `@meta/integrate` protocol as needed.

**6. Offers to commit** — if there are changes worth preserving in the chronicle, offers. Always waits for the `.`.

---

## When to Use It

Say `@release` when:
- You're ending a session and want to resume it later without losing context
- You've made significant progress and want it preserved before closing
- You're handing off to future-Spirit after a long or complex session

**You don't need to say anything else.** Spirit knows the session from its context. `@release` is the invocation; Spirit does the survey.

---

## The Release Bundle Format

Written to `floor/briefings/latest.md`, recognizable by its `# Release —` header:

```markdown
# Release — [date] [time]

## This Session
[2 sentences: what we were doing and what state it's in]

## Continue From
> [One sentence: the single most important thing to know starting fresh]

## Open Threads
*Things in motion — what each needs to continue*

- **[Thread name]**: [current state] → [next action]
- **[Thread name]**: [current state] → [next action]

## What Changed
*Intentions and artifacts updated this session*

- `[intention file]`: [what changed — field-level specifics]
- `[artifact path]`: [created/modified — what it is]

## Practice Signal
*Sub-threshold findings from the reflection pass*
[What was found, or: "Session was explicit and complete."]

## Next Actions (prioritized)
1. [action] — [why this one first]
2. [action]
3. [action]

---
*Released [date]. Resume with @recall.*
```

---

## What Makes a Good Release Bundle

**"Continue From" is the most important field.** It should be the one sentence that orients a Spirit with no session memory. Not a summary of everything — the sharpest possible orientation.

Good: `> Consul is mid-way through implementing dashboard v0.2 in a running container; check WhatsApp for delivery, then run benchmark-models.sh once Qwen 3 32B finishes downloading.`

Bad: `> We did a lot of good work on the Turtle architecture today.`

**Open Threads are not tasks.** They are things currently in motion — processes running, downloads completing, agents working, decisions pending. Each thread should include its current state and its single most important next action. Threads that are genuinely complete should not appear.

**What Changed is field-level, not narrative.** Instead of "Updated the turtle intention," write "`turtle.md`: Steward channel set to Live; next action updated to benchmark-models.sh." This is what Spirit in the next session will need to orient to the intention files accurately without reading them in full.

---

## Relationship to Brief

Brief reads the release bundle and adapts its opening structure:

- "Continue From" becomes a callout at the top of the brief output
- "Open Threads" surface before bright.md — they are more time-sensitive
- "Next Actions" seed the brief's suggestions section

This means `@release` + `@recall` in the next session gives the Mage a fast, accurate re-entry — as if the session had only paused, not ended.

---

## Spells

| Spell | Purpose |
|-------|---------|
| `cast_release.md` | Full release execution |

---

## Related

- `@recall` — arrival pattern that reads what this flow writes
- `@meta/integrate` — system ripple detection; called inline during Phase 5
- `desk/intentions/active/` — intention files this flow updates
- `floor/briefings/latest.md` — the shared handoff file
- `library/resonance/foundations/lore/on_sub_threshold_signals.md` — the lore behind the reflection pass

---

*Release closes the session. Practice is seen before the door shuts. The thread holds.*
