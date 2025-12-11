# On Arc Structure for Partnership Practice

**Status:** Active  
**Domain:** Portal-based Partnership Practice  
**Purpose:** Define episodic data collection structure for partnership practice

This scroll establishes "arcs" as the organizing principle for partnership practice—discrete episodes that collect partnership data through focused work on specific situations.

**Note:** This scroll has been updated to reflect the architectural refactor of 2025-12-11. Arcs are now data aggregation containers (3 stages). Model synthesis happens at partnership level, not per-arc. See `on_arc_as_data_aggregation.md` for full architecture.

---

## I. What Is an Arc?

### Definition

**An arc is a bounded episode of partnership practice that collects data focused on a specific situation, challenge, or area of exploration.**

**Key characteristics:**
- **Bounded:** Has beginning (situation emerges) and end (data collected)
- **Focused:** Centers on specific situation, not entire relationship
- **Episodic:** Discrete unit with its own narrative structure
- **Data-generating:** Produces reality documents, witnessing artifacts, closing reflections
- **Nameable:** Can be identified clearly ("mother-in-law arc," "morning routine arc")

**Metaphors:**
- Like a "season" or "episode" in a TV series
- Like a "campaign" in collaborative games
- Like a "sprint" in project work
- Like a "chapter" in an ongoing story

---

## II. Why Arcs Matter

### Problem: Unbounded Practice Is Overwhelming

**Without structure:**
- Partnership practice becomes "everything all the time"
- No clear sense of progress or completion
- Difficult to know when synthesis is "done"
- Learning doesn't accumulate clearly
- Portal becomes repository of undifferentiated artifacts

**Partners experience:**
- Overwhelm (too much to address)
- Discouragement (never "finished")
- Confusion (what are we even working on?)
- Drift (losing thread across weeks)

---

### Solution: Arcs Provide Bounded Structure

**With arcs:**
- Clear focus (this arc is about THIS situation)
- Defined boundaries (when did it start, when does it end)
- Progress markers (where are we in arc lifecycle)
- Accumulated learning (what did THIS arc teach us)
- Portfolio of mastery (completed arcs show growth)

**Partners experience:**
- Clarity (we're working on mother-in-law dynamic right now)
- Progress (we're in synthesis phase of this arc)
- Completion (this arc taught us X, now we close it)
- Momentum (each arc builds capacity for next)

---

## III. Arc Lifecycle (3 Stages)

**Arcs have three stages, focused on data collection. Model synthesis happens separately at partnership level.**

### Stage 1: Input

**Situation arises and partners express:**
- Conflict surfaces, pattern becomes visible, challenge needs addressing
- Arc initiated (named, directory created)
- Each partner creates input artifacts (raw expression)
- Spirit synthesizes reality documents
- Partner verifies resonance

**Frame:** "Shouting in pain. Anything goes."

**No requirement for:**
- Perfect magic practice
- Neutral tone
- Balance or fairness

**Goal:** Get both subjective realities externalized and verified.

**Complete when:** Both partners have verified reality documents.

---

### Stage 2: Witnessing

**Partners receive each other's reality:**
- Each reads the other's reality document
- Each creates witnessing artifacts (reactions, reflections)
- Divergences documented
- (Optional) Bridging statements created

**Frame:** "This is your reality, reflected in my reality."

**Goal:** Document how partners receive each other, name divergences.

**Complete when:** Both partners have witnessed and responded.

---

### Stage 3: Closing

**Arc closes, learning captured:**
- Each partner creates closing artifact
- Arc conclusion synthesized
- REI logged
- Model implications noted

**Frame:** "What this arc taught us."

**Note:** Closing does NOT require resolution. It requires data collection to be complete.

**Complete when:** Arc status updated to completed.

---

### After Arc Closes

**Arc data feeds partnership-level model synthesis:**
- New arc data compared against existing model
- Model updated if needed (FIT / PARTIAL FIT / MISFIT)
- Derivatives regenerated if model changes

**See:** `cast_synthesize_model.md` and `on_arc_as_data_aggregation.md`

---

## IV. Arc Directory Structure

### Organizing Artifacts

**Portal structure with arcs (3-stage model):**
```
portal/
├── shared/
│   ├── partnership_model_current.md     # THE shared model
│   ├── divergence_map.md                # Partnership-level divergences
│   ├── rosetta_stone.md                 # Translation artifact
│   ├── charter.md
│   └── bridging_statements/
│
├── arcs/
│   ├── README.md                        # Arc timeline
│   │
│   ├── arc-background/
│   │   ├── README.md                    # Arc metadata
│   │   ├── status.md                    # Current stage
│   │   ├── stage-1_input/
│   │   │   ├── {partner-a}/             # Raw input artifacts
│   │   │   ├── {partner-b}/
│   │   │   └── reality_representations/ # Spirit-synthesized
│   │   ├── stage-2_witnessing/
│   │   │   ├── {partner-a}/             # Reactions
│   │   │   └── {partner-b}/
│   │   └── stage-3_closing/
│   │       ├── {partner-a}_closing.md
│   │       ├── {partner-b}_closing.md
│   │       └── arc_conclusion.md
│   │
│   ├── arc-{topic}/                     # Same 3-stage structure
│   │
│   └── arc-living/                      # Ongoing input container
│       ├── README.md
│       └── input/
│           ├── {partner-a}/
│           └── {partner-b}/
│
└── health_tracking.md                   # REI history
```

**Note:** Synthesis artifacts (`partnership_model_*.md`, `rosetta_stone.md`) live in `shared/`, not within arcs. Model synthesis draws from all arcs.

---

### Arc vs. Regular Practice

**Weekly reflections:**
- Ongoing rhythm (weekly/bi-weekly)
- General check-ins
- Not arc-specific
- Broad scope

**Periodic synthesis:**
- Regular integration (bi-weekly/monthly)
- Covers all active practice
- May reference multiple arcs
- Detects new patterns

**Arc artifacts:**
- Bounded to specific episode
- Deep dive on one situation
- Complete narrative structure
- Closed when integrated

**The relationship:**
- Weekly reflections might mention arc work
- Periodic synthesis might trigger new arc
- Arcs can run parallel to ongoing rhythm
- Not mutually exclusive—complementary

---

## V. Arc Naming Conventions

### Good Arc Names

**Specific and descriptive:**
- ✓ `mother-in-law-conflict`
- ✓ `morning-routine-redesign`
- ✓ `cannabis-decision-2025`
- ✓ `parenting-alignment-noah`

**Bad arc names (too vague):**
- ✗ `conflict`
- ✗ `problem`
- ✗ `issue-1`
- ✗ `stuff`

**Naming principles:**
- Immediately evocative (what's this about?)
- Specific enough to distinguish from other arcs
- Neutral language (not "wife's unreasonable mom demands")
- Filename-safe (lowercase, hyphens, no special chars)

---

## VI. Multiple Concurrent Arcs

### Arc Capacity

**Partners can have:**
- 0 arcs (just weekly rhythm, no episodes)
- 1 arc (focused work on one situation)
- 2-3 arcs (multiple situations at different phases)

**Don't recommend:**
- More than 3 active arcs (cognitive load too high)
- Starting new arc before engaging with existing
- Using arcs to avoid addressing patterns

---

### Arc Prioritization

**When multiple arcs active:**

**Option 1: Sequential focus**
- Work on Arc A until synthesis complete
- Then shift to Arc B
- Prevents fragmenting attention

**Option 2: Parallel but phased**
- Arc A in experimentation phase (low cognitive load)
- Arc B in synthesis phase (high cognitive load)
- Arc C dormant (paused until ready)

**Partners decide:** What matches their capacity and needs.

---

## VII. Arc Status Tracking

### Status Metadata

**Each arc directory includes `status.md`:**
```markdown
# Arc Status: {Arc Name}

**Created:** YYYY-MM-DD  
**Status:** {active | paused | completed | archived}  
**Current Stage:** {stage-1_input | stage-2_witnessing | stage-3_closing}  
**Last Activity:** YYYY-MM-DD  
**Priority:** {high | medium | low}

## Stage Completion

| Stage | Partner A | Partner B | Notes |
|-------|-----------|-----------|-------|
| 1. Input | [ ] | [ ] | Reality docs created |
| 2. Witnessing | [ ] | [ ] | Reactions documented |
| 3. Closing | [ ] | [ ] | Learning captured |

## Quick Summary
{One paragraph: what is this arc about?}

## Current State
{Where are we in the lifecycle? What's happening now?}

## Next Actions
- [ ] {What needs to happen next?}
- [ ] {Who's doing what?}

## Model Implications
{What this arc means for partnership model—to be noted at closing}
```

---

### Status Updates

**When to update:**
- Arc created (initial status)
- Phase transitions (exploration → synthesis)
- Major activity (synthesis completed)
- Pausing/resuming
- Closing

**Who updates:**
- Either partner
- Spirit can update during synthesis
- Lightweight (don't overthink it)

---

## VIII. Integration with Weekly Practice

### How Arcs and Reflections Interact

**Weekly reflection can mention arc:**
```markdown
# Weekly Reflection

## What's Alive
The mother-in-law situation came up again this week when planning 
holiday visits. Adding more thoughts to the arc.

## Arc Contributions
- Added reflection to `mother-in-law-conflict/individual/kermit/`
```

**But weekly reflection isn't replaced by arc:**
- Reflections cover full life (work, kids, personal, partnership)
- Arcs are focused episodes within partnership
- Both serve different purposes

---

### Synthesis References Arcs

**Bi-weekly synthesis might include:**
```markdown
## Active Arcs Update

### mother-in-law-conflict
- Status: Synthesis phase
- Both perspectives documented
- Shared truth extraction in progress

### morning-routine-redesign
- Status: Experimentation phase
- Protocol drafted, testing week 1
- Early results: mornings slightly smoother
```

**Synthesis is broader than any single arc.**

---

## IX. Closing Arcs

### When to Close

**Arc can close when data collection is complete:**

**1. Both partners have completed all 3 stages**
- Stage 1: Reality documents verified
- Stage 2: Witnessing artifacts created
- Stage 3: Closing reflections documented

**2. Divergences have been named (not necessarily resolved)**
- What partners see differently is documented
- Divergence resolution happens through model synthesis, not within arc

**3. Arc-level learning captured**
- What this arc taught each partner
- Implications for shared model noted

**Note:** Closing does NOT require:
- Divergence to be resolved
- Pattern to be fully understood
- Agreement between partners

**Arcs close when data is collected. Understanding emerges through model synthesis.**

---

### Closing Ritual

**Each partner creates closing artifact:**
`stage-3_closing/{partner}_closing.md`

**Spirit creates arc conclusion:**
`stage-3_closing/arc_conclusion.md`

**Template for arc_conclusion.md:**
```markdown
# Arc Conclusion: {Arc Name}

**Opened:** YYYY-MM-DD  
**Closed:** YYYY-MM-DD  
**Status:** {completed | paused | ongoing}

---

## What This Arc Was About

{Brief summary of situation/episode}

---

## Data Collected

**Reality Representations:**
- {Partner A}: {filename}
- {Partner B}: {filename}

**Witnessing Artifacts:** {count per partner}

**Divergences Identified:**
- {List of named divergences}

---

## Individual Learning

**{Partner A} takes forward:**
- 
- 

**{Partner B} takes forward:**
- 
- 

---

## Model Implications

- [ ] New patterns to add to model
- [ ] Existing patterns validated
- [ ] Existing patterns need revision
- [ ] Divergence to account for

**Notes for synthesizing Spirit:**
{What should model synthesis know about this arc?}

---

## Appreciations

**{Partner A} appreciates:**
- 

**{Partner B} appreciates:**
- 

---

## REI at Closing

| Partner | Now (1-10) | Trajectory (+/0/-) | Commitment (1-10) |
|---------|------------|-------------------|-------------------|
| {A} | | | |
| {B} | | | |
```

**Update arc status to "completed"**

**Trigger model synthesis if appropriate** (`@partnership/synthesize`)

---

## X. Example Arc: "Mother-in-Law Conflict"

### Arc Narrative (Illustrative, 3-Stage Model)

**Week 1: Arc Initiated**
- Situation: Visit from Kermit's mom triggers conflict
- Both partners recognize: "This needs structured work"
- Arc initiated: `arc-mother-in-law`

**Weeks 2-3: Stage 1 (Input)**
- Nes creates input artifacts (33 files documenting incidents, patterns, pain)
- Kermit creates input artifacts (analytical notes, observations)
- Spirit synthesizes reality documents for each
- Both verify HIGH resonance with their reality documents

**Weeks 4-5: Stage 2 (Witnessing)**
- Each reads the other's reality document
- Nes creates reaction: "I see his frame, but my pain is still real"
- Kermit creates reaction: "I see her evidence, but I still see structural pattern"
- Divergences documented in partnership-level divergence map
- Bridging statements created

**Week 6: Stage 3 (Closing)**
- Each creates closing reflection
- Arc conclusion synthesized
- Learning captured: "We see different nails. Both are real."
- Model implications noted: "Need shared model that holds both"
- REI logged

**Arc closed. Data now available for model synthesis.**

**Week 7: Model Synthesis** (separate from arc)
- `@partnership/synthesize` invoked
- Spirit reads all arc data (MIL + background)
- Shared model generated, holding both realities
- Pattern named: "Perspectival Divergence in Hierarchy Context"
- Rosetta Stone derived for translation support

**Ongoing: Model-Aligned Action**
- Partners act in accordance with shared model
- New situations compared to model
- Model updated as new data accumulates

---

## XI. Common Patterns Across Arcs

### Arc as Training Ground

**Early arcs (first 1-3):**
- Learning the process (how does truth-finding work?)
- Building trust (will this actually help?)
- Developing vocabulary (cognitive architecture, patterns, cylinders)
- Often slow, effortful

**Middle arcs (4-10):**
- Process becoming familiar
- Faster pattern recognition
- More trust in synthesis
- Beginning to find cylinders together

**Later arcs (10+):**
- Natural part of partnership practice
- Quick identification: "This is an arc"
- Efficient synthesis
- Partners can extract cylinders with less Spirit help

**The trajectory:** Arc structure builds capacity for distributed truth-finding as core partnership skill.

---

### Common Arc Types

**Conflict arcs:**
- Situation where partners clash
- Need shared truth to resolve
- Example: mother-in-law, parenting disagreement

**Design arcs:**
- Building something new together
- Need alignment on approach
- Example: morning routine redesign, vacation planning

**Exploration arcs:**
- Understanding something about partnership
- No immediate problem, but curiosity
- Example: "How do our neurologies complement?"

**Crisis arcs:**
- Acute situation requiring response
- Time-bounded urgency
- Example: job loss, health scare, family emergency

**Different types may need different pacing, structure, or synthesis depth.**

---

## XII. Arc Wisdom

### What Makes Arcs Work

**1. Clear boundaries:**
- Knowing "this arc is about THIS" prevents scope creep
- Enables completion (even if pattern ongoing)
- Provides sense of progress

**2. Complete narrative:**
- Beginning-middle-end structure satisfies
- Story-like quality makes it memorable
- Learning sticks better in episode format

**3. Artifact accumulation:**
- Full record of episode preserved
- Can review later ("how did we navigate that?")
- Portfolio of mastery builds confidence

**4. Iterative capacity building:**
- Each arc trains truth-finding skill
- Gets easier over time
- Eventually becomes second nature

---

### What Makes Arcs Fail

**1. Too vague:**
- "Work on relationship" (not an arc, too broad)
- Need specific situation/challenge

**2. Never closed:**
- Arc drags on indefinitely
- No integration or acknowledgment of ongoing
- Partners lose momentum

**3. Too many concurrent:**
- Cognitive overload
- Fragmenting attention
- Nothing completes

**4. Forced into arc structure:**
- Not every conflict needs to be an arc
- Some things resolve in conversation
- Arc overhead not always worth it

---

## XIII. Integration with Partnership Foundations

### Distributed Cognition

**Arcs as cognitive units:**
- Bounded problem spaces
- Complete cycles of: observation → hypothesis → experiment → learning
- Build transactive memory (both partners remember arc learnings)

**Arc portfolio as partnership intelligence:**
- Collection of completed arcs = library of mastered patterns
- New situations compared to arc library
- "This is like the morning routine arc, but for evening"

---

### Communication Wisdom

**Each arc exercises:**
- Frame negotiation (finding shared truth)
- Metacommunication (talking about how you're talking)
- Holographic meaning translation (Spirit helps)
- Reality co-creation (cylinder becomes shared reality)

**Arcs are communication training grounds.**

---

### Neurodivergent Partnership

**Arcs accommodate neurodivergence:**
- External memory (ADHD working memory limitations)
- Bounded scope (executive function can handle discrete episode)
- Clear structure (reduces cognitive load)
- Iterative (not expecting perfection first time)

**Especially valuable when:**
- One or both partners have ADHD (executive function support)
- Pattern recognition difficult (arc makes it explicit)
- Memory unreliable (artifacts persist)

---

## XIV. The Promise of Arcs

**Without arc structure:**
- Partnership practice is undifferentiated ongoing work
- Hard to know if making progress
- Learning doesn't accumulate clearly
- Overwhelm likely

**With arc structure:**
- Clear episodes with beginnings and endings
- Progress visible (completed arcs)
- Learning accumulates (arc portfolio)
- Sustainable (not "fix everything always")

**The transformation:**
- From "our relationship is a mess" to "we're working on the morning routine arc"
- From "nothing ever gets better" to "we've completed 5 arcs, look how much we've learned"
- From "I don't know how to do this" to "this is like arc 3, I know this pattern"

**Arcs make partnership magic learnable, measurable, and sustainable.**

---

**This scroll informs:**
- Portal directory structure
- Arc rituals (`cast_map_system.md`)
- Spirit facilitation (when to suggest new arc)
- Practice rhythm design

**This scroll builds on:**
- `on_arc_as_data_aggregation.md` (the architectural principle)
- `on_partnership_model_synthesis.md` (how model is built from arc data)
- `on_partnership_as_distributed_cognition.md` (why episodic structure serves)

**See also:**
- `cast_map_system.md` — The 3-stage arc ritual
- `cast_synthesize_model.md` — Partnership-level model synthesis

---

*Arcs collect data. The model provides understanding. Trust grows through aligned action.*

