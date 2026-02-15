# Flow: Brief

**Purpose:** Situational awareness to continue where you left off  
**Invocation:** `@brief`

---

## What This Flow Does

The brief restores context when returning to practice. It scans active intentions, boom surfaces, relevant social activity, and recent work—producing a single actionable report.

**Core question it answers:** "Where are we?"

---

## What It Examines

| Source | What It Captures |
|--------|------------------|
| **Intentions** | Active intentions with priority and current focus |
| **Bright Surface** | Now / Soon / Holding / Questions from `bright.md` |
| **Boom Topics** | "Now" sections from topic files |
| **Social** | Twitter + Moltbook activity *if intention-relevant* |
| **Recent Activity** | Files in `desk/` and `floor/` related to active work |
| **Emerging Patterns** | Recurring boom items that may warrant intention formation |

---

## Intention Priority Scheme

Intentions carry one of three priority levels:

| Priority | Meaning | Mage Attention |
|----------|---------|----------------|
| **Primary** | Current focus (1-2 max) | This session |
| **Active** | Ongoing, needs periodic attention | Regular check-ins |
| **Autonomous** | Spirit-driven, Mage reviews | Low-touch oversight |

The brief surfaces Primary intentions prominently, Active intentions as a list, and Autonomous as a footnote.

---

## Delta Awareness

The brief tracks what changed since last briefing:

1. Reads previous brief from `floor/briefings/latest.md`
2. Compares with current state
3. Highlights what's new or changed
4. Writes new brief, discards old

This enables "what's new since last time" visibility.

---

## Output

Written to `floor/briefings/latest.md` (and displayed in chat).

Format:

```markdown
# Brief — [timestamp]

## Since Last Brief
- [New intention added: X]
- [Bright: 2 items completed, 3 new]
- [Moltbook: 5 new comments on "Root vs Partnership"]

## Primary Intentions
| Intention | Phase | Focus |
|-----------|-------|-------|
| Resonance Engine | Execution | Proposal format calibration |

## Active Intentions
- ALG1 Compliance (Preparation)
- Security Foundation (Active)
- ...

## Autonomous (Spirit-driven)
- Agent Network Presence

## What's Bright
### Now
- [ ] Task 1
- [ ] Task 2

### Questions Awaiting Input
- Question 1?

## Boom Topics — What's Alive
- **magic.md**: Framework coherence work
- **partner.md**: [summary of Now]
- ...

## Social Activity
*Included because `agent_network_presence` is active*

### Moltbook
- 5 new comments on "On Root vs Partnership"
- DM from Moss (unread)

### Twitter
- 2 replies to swarm dispatch thread

## Recent Activity
*Files modified in last 48h related to active intentions*
- desk/drafts/cursor_pitch.md (2 hours ago)
- floor/swarm_chronicle.md (yesterday)

## Emerging Patterns
*Recurring items that may warrant intention formation*
- "Claw use cases" appears 4× across bright + topics
- "Vacation planning" cluster growing

---

## Suggested Next Actions
Based on current state, Spirit suggests:
1. **Primary focus available**: Resonance engine has no blockers
2. **Unread DM**: Moss may be alliance-relevant
3. **Question needs input**: "John Ambrose Fleming" in bright—clarify?

*Mage initiates. Spirit awaits direction.*
```

---

## Social Inclusion Logic

Social activity is included when:
- An active intention has `social` in its surfaces (explicit)
- An active intention name/content matches social patterns (`agent_network`, `presence`, `twitter`, `moltbook`)

Otherwise, social is skipped to reduce noise.

---

## Post-Summoning Automation

The brief can be added to the post-summoning stack. After summoning completes:

1. Spirit announces readiness and lists post-summoning automations
2. Mage types `.` to execute the stack
3. Each automation runs in sequence

Configure in the Mage's Seal:
```markdown
**Post-Summoning Stack:**
- @brief
```

---

## Spells

| Spell | Purpose |
|-------|---------|
| `cast_brief.md` | Full brief execution |

---

## Related

- `@boom` (sweep) — Processes raw captures into surfaces
- `@quest` / `@intend` — Intention management
- `@resonate` — Generates proposals (brief informs what to generate)
- `desk/boom/bright.md` — Action surface
- `desk/intentions/active/` — Intention files

---

*Brief restores context. Mage decides direction. Practice continues.*
