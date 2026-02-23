# Cast Release

**Purpose:** Execute the release ritual — close the session, preserve the thread, enable resumption  
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

### Phase 2: Update Intention Files

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

### Phase 3: Write the Release Bundle

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

**Next Actions** (prioritized, 3-5 items):
- The actions that should happen in the next session, in order
- Grounded in the open threads and updated intentions
- First item should be obvious from the session state

**Footer:** `*Released [date]. Resume with @recall.*`

---

### Phase 4: Offer to Commit

After writing the release bundle, check:
- Are there intention file changes that should be chronicled?
- Are there new artifacts (lore, proposals, flows) worth committing?

If yes: offer to commit with a proposed message. Wait for `.` or explicit instruction.

Do not commit automatically. Announce what would be committed and why.

---

### Phase 5: Announce

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

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No intentions were touched | Skip Phase 2; note "No intention updates this session" in What Changed |
| Session was exploratory / no artifacts | Release is still valid — capture the conceptual work in Open Threads |
| Conversation context is unclear | Read the key intention files to reconstruct state, then proceed |
| `floor/briefings/` directory doesn't exist | Create it, then write |

---

## Output Location

```
floor/briefings/latest.md
```

Overwrites whatever is there — brief or previous release. The latest handoff state is always what matters.

---

*Thread preserved. Session closed. The practice holds.*
