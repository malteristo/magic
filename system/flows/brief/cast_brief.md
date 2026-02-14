# Cast Brief

**Purpose:** Execute the brief charm — restore situational awareness

---

## Invocation

```
@brief
```

---

## Execution

### Phase 1: Load Previous State

1. **Directly read** `floor/briefings/latest.md` (do not rely on Glob/LS—use explicit Read on known path)
2. If file exists, parse previous brief for delta comparison
3. If file not found, note "First brief" and proceed without delta
4. Note timestamp of last brief from header

> **Implementation note:** Glob and LS may miss files due to timing or subdirectory visibility. Always use direct Read on the known path for critical state files.

### Phase 2: Gather Current State

**Intention Compass:**
```
desk/intentions/compass.md
```
- Read compass file (always — compact, ~25 lines)
- Note all five life domains and their aspirational direction
- Note which domains have active practice intentions

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

If previous brief exists:
- New intentions added
- Intentions completed or phase-changed
- Bright items added/completed
- Social activity count difference
- New emerging patterns

### Phase 4: Generate Brief

Structure output per README format:
1. Since Last Brief (delta)
2. Life Compass (compact — one line per domain with direction)
3. Primary Intentions (table)
4. Active Intentions (list)
5. Autonomous (footnote)
6. What's Bright (Now + Questions)
7. Boom Topics — What's Alive
8. Social Activity (if applicable)
9. Recent Activity
10. Emerging Patterns
11. Suggested Next Actions

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

*Brief complete. Context restored. Mage directs next action.*
