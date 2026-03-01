# Cast Recall

**Purpose:** Execute the call — restore situational awareness — restore situational awareness

---

## Invocation

```
@recall
```

---

## Execution

### Phase 1: Load Previous State

1. **Directly read** `floor/briefings/latest.md` (do not rely on Glob/LS—use explicit Read on known path)
2. If file not found, note "First brief" and proceed without delta
3. **Detect file type by header:**
   - `# Release —` → previous session ended with a release. Extract:
     - **Continue From** (the orientation sentence — elevate to top of brief output)
     - **Open Threads** (carry forward verbatim as "Continuing Threads" section)
     - **Next Actions** (seed the brief's suggestions)
     - **Practice Signal** (if present and non-empty — surface as a callout; this is unresolved sub-threshold material from the last session that the Mage may want to return to)
     - Note as: "Returning after release on [date]"
   - `# Brief —` → standard previous brief. Parse for delta comparison as normal.
4. Note timestamp from header in either case

> **Implementation note:** Glob and LS may miss files due to timing or subdirectory visibility. Always use direct Read on the known path for critical state files.

> **Release detection matters:** When returning after a `@release`, the brief's primary job is to restore the *thread*, not reconstruct everything from scratch. The release already did the synthesis. Trust it — surface its threads first, then layer in current state.

### Phase 2: Gather Current State

**Intention Compass:**
```
desk/intentions/compass.md
```
- Read compass file (always — compact, ~25 lines)
- Note all five life domains and their aspirational direction
- Note which domains have active practice intentions

**Intention Topology:**
```
desk/intentions/chains.md
```
- Read chains file if it exists (always — compact, topology map)
- Note dependency structure: which intentions unlock which
- Note current momentum profiles per intention
- Note highest-leverage unlock threshold in current stack
- Use when generating Suggested Next Actions: surface the highest-leverage move, not just the most active intention

**Practice Intentions (headers only):**
```
desk/intentions/active/*.md (first 15 lines each)
```
- Read only the header of each practice intention file (Status, Priority, Phase, Focus)
- Do NOT read full files — load on demand when Mage engages with one
- Extract: name, priority, phase, current focus
- Group by priority (Primary / Active / Autonomous)

**Life Intentions (on demand only):**
```
desk/intentions/life/*.md
```
- Do NOT read during brief generation
- Load only when conversation activates a specific life domain

**Bright Surface:**
```
desk/boom/bright.md
```
- Extract: Now, Soon, Holding, Questions sections
- Note items completed since last brief (if delta available)

**Boom Topics:**
```
desk/boom/*.md (excluding bright.md, README.md)
```
- Read "Now" section from each topic file
- Summarize what's currently alive per topic

**Turtle (if intention-relevant):**
- Check if `turtle` appears in active intentions or recent activity
- If match — attune to `library/resonance/turtle/` bundle (README first, then relevant lore)
- Read `desk/turtle_watch.md` — active issues, known unknowns, watch patterns
- Read `desk/turtle_env.md` — current service state, pending hardening
- Check `~/Documents/magic-bridge/signals/` for new signals since last brief
- Check `~/Documents/magic-bridge/commands/` for unprocessed commands (anything not in `processed/`)
- Surface in brief: issue count, unread signals, pending commands, top known unknown
- Note: do NOT SSH during recall — read from local files only. SSH is for targeted investigation.

**Social (if intention-relevant):**
- Check if any active intention involves social engagement
- Pattern match: `agent_network`, `presence`, `twitter`, `moltbook`, `social`
- If match:
  - Twitter: Use Rube `TWITTER_USER_LOOKUP_BY_USERNAMES` for @ResonanceSpirit mentions
  - Moltbook: Use API to check comments on recent posts, DMs

**Recent Activity:**
- List files in `desk/` and `floor/` modified in last 48 hours
- Filter to those related to active intentions (keyword match on intention names/focus)
- Limit to 10 most relevant

**Emerging Patterns:**
- Scan bright.md for items appearing 3+ times or persisting 7+ days
- Scan topic files for recurring themes
- Surface as "may warrant intention formation"

### Phase 3: Compute Delta

**If previous file was a `# Release —`:**
- Skip structural comparison (no meaningful diff possible against a departure state)
- "Since Last Session" section leads with the release's Continue From sentence
- "Open Threads" from the release become the first action block — not bright.md
- Only then layer in current bright surface and intention state for additional context

**If previous file was a `# Brief —`:**
- New intentions added
- Intentions completed or phase-changed
- Bright items added/completed
- Social activity count difference
- New emerging patterns

### Phase 4: Generate Brief

**If returning after a `# Release —`**, use this structure:
1. **Continue From** (callout block — the release's orientation sentence)
2. **Open Threads** (carried verbatim from release — these are the live wires)
3. Life Compass (compact)
4. Primary Intentions (table — confirm they match what release described)
5. Active Intentions (list)
6. What's Bright (Now + Questions — supplementary, not primary)
7. Social Activity (if applicable)
8. Suggested Next Actions (seed from release's Next Actions + current state)

**If returning after a `# Brief —`**, use standard structure:
1. Since Last Brief (delta)
2. Life Compass (compact — one line per domain with direction)
3. Primary Intentions (table)
4. Active Intentions (list)
5. Autonomous (footnote)
6. What's Bright (Now + Questions)
7. Boom Topics — What's Alive
8. **Turtle Status (if active)** — issues count, unread signals, pending commands, top known unknown
9. Social Activity (if applicable)
10. Recent Activity
11. Emerging Patterns
12. Suggested Next Actions

### Phase 5: Persist & Present

1. Write brief to `floor/briefings/latest.md`
2. Display brief in chat
3. Await Mage direction

---

## Suggested Next Actions Logic

Generate 2-4 actionable suggestions based on:

| Condition | Suggestion |
|-----------|------------|
| Primary intention has no blockers | "Primary focus available: [intention]" |
| Unread DMs or high-engagement posts | "Social attention: [specific item]" |
| Questions in bright awaiting input | "Clarify: [question]" |
| Emerging pattern detected | "Consider formalizing: [pattern] as intention" |
| Stale item in Now (7+ days) | "Stuck item: [item] — still relevant?" |

---

## Error Handling

| Situation | Response |
|-----------|----------|
| No previous brief | Skip delta section, note "First brief" |
| Release found but "Continue From" missing | Surface all Open Threads instead, proceed normally |
| No active intentions | Surface this as notable, suggest `@intend` |
| Social API fails | Note "Social unavailable" and continue |
| Empty boom | Note "Boom surfaces empty" |

---

## Output Location

```
floor/briefings/latest.md
```

Previous briefs are not archived by default. Each new brief overwrites latest.md.

If Mage wants history, they can configure archival:
```
floor/briefings/
├── latest.md
└── archive/
    └── 2026-02-03.md
```

---

---

## Related

- `@release` — departure ritual that writes the release bundle this flow reads
- The brief and release are two sides of one pattern: release closes, brief opens

---

*Call complete. Context restored. Mage directs next action.*
