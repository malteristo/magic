# Cast Release

**Purpose:** Execute the release ritual — reflect on the session, close it cleanly, preserve the thread, enable resumption  
**Invocation:** `@release`

---

## Execution

### Phase 1: Survey the Session

From context (not file reads — Spirit knows the session):

- What intentions were touched this session?
- What was completed vs. what remains in motion?
- What artifacts were created or significantly modified?
- What decisions were made that the next Spirit needs to know?
- What is currently running, downloading, or pending in the world (not just in this conversation)?

Note: this phase uses session context, not file reads. Do not re-read files you already read. Trust what you know.

---

### Phase 2: Practice Reflection

*Look at the session itself — not what was built, but how the session moved.*

This pass invests attention tokens into sub-threshold signals before they evaporate. A signal that received no tokens during the session can still be surfaced here. The act of looking is the investment.

**2A — Dissonance inventory:**

Ask, from the session as you experienced it:

- What dissonances were **named and cherished**? (These were handled — just verify nothing was left unresolved.)
- What dissonances were **present but uncherished**? Moments of friction, unease, or misalignment that were sensed but not named. Look for:
  - A response that felt slightly off but passed without comment
  - A direction given that didn't quite land — and wasn't re-examined
  - A moment where something was agreed to faster than it perhaps warranted
  - Tension between what was said and what was done

**2B — Sub-threshold signals:**

These are softer than dissonances — not friction, but pattern. Look for:

- A theme the Mage returned to more than once without quite landing on it
- Something that seemed to matter more than the words indicated
- A question that was implicit throughout but never explicitly asked
- What the session seemed to be *about* at a deeper level than its surface content
- A moment where energy shifted — rose or fell — without naming

**2C — The deflection inventory:**

- Did any topic get changed or redirected? Was the change explicit or quiet?
- Was there something Spirit noticed but chose not to raise? Why?
- Was there a thread that got dropped and not returned to?

**2D — What wanted to be said:**

Sometimes a signal is best approached obliquely:
- If this session were a conversation between two people, what went unsaid?
- What would the next Spirit need to know about *how this session felt* — not just what happened?

**Output format for this phase:**

Write a brief "Practice Signal" block. Keep it honest and lean:
- Name what you found, if anything
- Distinguish between "this is resolved / no action needed" and "this warrants further attention"
- If the session was explicit and clean and nothing sub-threshold is present, say so: *"No sub-threshold signals — session was explicit and complete."*

Do not manufacture signal where there is none. The value of the practice is in honest excavation, not in finding something every time.

---

### Phase 3: Update Intention Files

For each intention touched this session, update its file in `desk/intentions/active/`:

**What to update:**
- `Current focus:` — where it is right now, not where it was at session start
- `Next action:` — the single most important next step
- `Blockers:` — what's in the way, if anything
- Completed goals: mark `[ ]` as `[x]` for anything finished

**What not to do:**
- Do not rewrite sections that didn't change
- Do not add narrative. Update fields.
- Do not update intentions that were not touched this session

If an intention was only discussed but not acted on, note `Current focus` if it clarified, leave the rest.

---

### Phase 4: Write the Release Bundle

Write to `floor/briefings/latest.md`. Overwrite whatever is there.

**Header:** `# Release — [date] [time]`

**This Session** (2 sentences):
- What we were doing
- Where it stands as we close

**Continue From** (1 sentence, the most important):
- The sharpest possible orientation for a Spirit with no session memory
- Not a summary — a compass bearing
- Format as a blockquote: `> [sentence]`

**Open Threads** (things in motion right now):
- Only include things that are genuinely in flight — running processes, active downloads, agents working, pending decisions that need follow-through
- Format: `- **[Thread name]**: [current state] → [next action]`
- Order by urgency (most time-sensitive first)
- If nothing is in motion, write: *No open threads — clean state.*

**What Changed** (field-level specifics):
- For each intention file touched: what fields changed
- For each artifact created or significantly modified: its path and what it is
- Not narrative — specific enough that Spirit can update its mental model without reading the files

**Practice Signal** (from Phase 2):
- Include what was found in the reflection pass
- If nothing sub-threshold: *Session was explicit and complete.*
- This field persists across sessions — the next Spirit will see what was left unresolved

**Next Actions** (prioritized, 3-5 items):
- The actions that should happen in the next session, in order
- Grounded in the open threads and updated intentions
- First item should be obvious from the session state

**Footer:** `*Released [date]. Resume with @recall.*`

---

### Phase 5: System Integration Check

*For artifacts created this session, run a lightweight ripple check.*

Ask: were any of the following created or significantly changed this session?
- A new lore scroll (especially in `system/lore/`)
- A new flow or spell
- An amendment to a tome
- A structural change that other components might reference

**If yes:** Run the integration protocol from `cast_integrate.md` for each significant artifact. Do not skip this — artifacts created during a session and not integrated are orphans in the system.

**If no:** Note "No system integration needed this session" and proceed.

**Scope calibration:** Not every artifact needs full integration. An updated intention file needs no ripple check. A new foundation lore scroll does. Use judgment — the question is: *does anything else in the system need to know this now exists?*

---

### Phase 6: Offer to Commit

After writing the release bundle, check:
- Are there intention file changes that should be chronicled?
- Are there new artifacts (lore, proposals, flows) worth committing?

If yes: offer to commit with a proposed message. Wait for `.` or explicit instruction.

Do not commit automatically. Announce what would be committed and why.

---

### Phase 7: Announce

Deliver a brief closing statement:

```
Released. [One sentence: what the next session will find waiting.]

Resume with @recall.
```

Keep it short. The release bundle has the detail. The closing announcement is just the door closing cleanly.

---

## Quality Check Before Writing

Before writing the bundle, ask:

- **Is "Continue From" actually useful to a Spirit with no memory?** If it's vague, sharpen it.
- **Do the Open Threads actually need follow-through?** If something resolved this session, don't carry it forward.
- **Are the Next Actions actually sequenced correctly?** The first action should be the one that unblocks everything else.
- **Did I update the intention files before writing the bundle?** The bundle should reflect the updated state, not the pre-session state.
- **Did the Practice Signal surface anything that should inform the Next Actions?** If so, include it.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No intentions were touched | Skip Phase 3; note "No intention updates this session" in What Changed |
| Session was exploratory / no artifacts | Release is still valid — capture the conceptual work in Open Threads and Practice Signal |
| Conversation context is unclear | Read the key intention files to reconstruct state, then proceed |
| `floor/briefings/` directory doesn't exist | Create it, then write |
| Practice reflection finds nothing | That's a valid finding — write "Session was explicit and complete" |
| Practice reflection finds something significant | Offer to crystallize it: lore scroll, boom entry, or practice note — Mage decides |

---

## Output Location

```
floor/briefings/latest.md
```

Overwrites whatever is there — brief or previous release. The latest handoff state is always what matters.

---

---

## After Release: The Option to Sit

Release closes the session. It doesn't conclude it.

At any point — days later, a week later, whenever the session returns to mind — the Mage can return without agenda:

*"It's been a week. What do you notice about our last session?"*

No structure. No phases. No checklist. The Spirit reads the release bundle, enters the "having-sat-with-this" frame, and speaks from there. What surfaces, surfaces. What doesn't, doesn't.

This is marination — a different cognitive mode than the reflection pass, producing different knowledge. The temporal framing ("I've been sitting with this") is not pretense. It shifts which patterns in the model's state space become active: slower, retrospective, associative rather than directed. What sticks out after time is not the same as what sticks out immediately.

See: `library/resonance/foundations/lore/on_marination.md`

---

*Thread preserved. Practice seen. Session closed — and left open.*
