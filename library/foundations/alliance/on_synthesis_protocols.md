# On Synthesis Protocols for Multi-Mage Practice

**Status:** Active (Specification v1.0)  
**Purpose:** Enable coherent integration of N cognitive perspectives  
**Foundation:** STP/1.0.0, Portal Architecture v1.0

---

## I. The Challenge

**Git merges code. We need to merge cognition.**

When multiple Mages contribute to shared practice:
- Two Mages write partnership reflections
- Five Mages update quest progress
- Twelve Mages co-create research synthesis

**How does magic integrate N perspectives into coherent whole?**

**The synthesis problem is:**
- Technical: Prevent git conflicts
- Cognitive: Honor all voices without losing coherence
- Social: Distribute labor fairly
- Quality: Ensure excellent integration, not mechanical aggregation

**This scroll provides proven patterns for multi-way cognitive integration.**

---

## II. Design Principles

### 1. Namespace Prevents Technical Conflicts

**Each Mage writes to distinct directory:**
```
artifacts/{mage_name}/contribution.md
```

**Synthesis writes to shared directory:**
```
artifacts/synthesis/integrated.md
```

**Result:** No overlapping writes → no git merge conflicts → focus on cognitive synthesis, not technical conflict resolution.

### 2. Synthesis is Creative Act, Not Mechanical

**Synthesis is NOT:**
- Simple concatenation (Mage1 + Mage2)
- Averaging (blend until uniform)
- Majority rule (most common perspective wins)

**Synthesis IS:**
- Pattern recognition (what emerges across perspectives?)
- Coherence creation (how do pieces fit together?)
- Divergence acknowledgment (where do perspectives differ honestly?)
- Insight generation (what appears that no individual saw?)

**The Synthesis Caretaker** is cognitive artist, not mechanical aggregator.

### 3. Labor is Distributed Through Rotation

**Synthesis is cognitively demanding:**
- Read all N contributions carefully
- Identify patterns and divergences
- Craft coherent integration
- Respond to feedback
- Refine until finalized

**To prevent burnout and concentration:**
- **Rotating Synthesis Caretaker** shares labor
- Simple algorithm (alphabetical, round-robin)
- Everyone contributes, everyone learns
- No permanent synthesizer (prevents power concentration)

### 4. Consensus Level Varies by Context

**Intimate partnerships (2-4 Mages):** CONSENSUS
- All must approve synthesis
- High trust requires high agreement
- Take time needed (quality over speed)

**Collaborative circles (3-12 Mages):** ROUGH CONSENSUS
- Majority sufficient (e.g., 2/3 or 3/4)
- Progress over perfect agreement
- Dissent noted but doesn't block

**Large networks (20+ Mages):** REPRESENTATIVE
- Regional synthesis (within clusters)
- Cross-regional synthesis (between representatives)
- Multiple valid approaches coexist (fork-friendly)

---

## III. The Synthesis Cycle

**Standard synthesis rhythm** (adaptable per tome/portal):

### Phase 1: Individual Contribution (Days 1-3)

**Each Mage + Spirit:**
1. Practice individually (reflection, progress update, research note)
2. Write to own namespace: `artifacts/{mage}/contribution_{date}.md`
3. Commit and push
4. No coordination needed (parallel work)

**Spirit's role:**
- Guide contribution through tome's questions/prompts
- Ensure namespace correctness (write to right directory)
- Quality check (is contribution complete?)
- Commit with descriptive message

### Phase 2: Signal Synthesis Need (Day 3-4)

**When all contributions present:**

**Last contributor's Spirit** (or any Spirit detecting readiness):
1. Check: Have all participants contributed?
2. If yes: Create synthesis request intent
3. Write `.spirit/intents/synthesis_needed_{date}.yaml`
4. Commit and push

**Intent format:**
```yaml
protocol_version: "STP/1.0.0"
intent_type: "synthesis_needed"
created: "2025-11-25T15:00:00Z"
created_by: "Kermit"

context:
  artifact_type: "weekly_reflection"
  cycle: "2025-W48"
  contributions:
    - mage: "Kermit"
      path: "artifacts/kermit/2025-11-25_reflection.md"
      completed: "2025-11-25T14:00:00Z"
    - mage: "Alice"
      path: "artifacts/alice/2025-11-25_reflection.md"
      completed: "2025-11-25T14:30:00Z"

synthesis_caretaker: null  # To be claimed
synthesis_protocol: "consensus"  # or "rough_consensus", "representative"
```

### Phase 3: Caretaker Volunteers (Day 4)

**Who volunteers:**

**Check rotation schedule:**
```yaml
# In portal registry or .spirit/synthesis_rotation.yaml
synthesis_caretaker_rotation:
  current: "Alice"
  next: "Kermit"
```

**Alice's Spirit (seeing synthesis needed + it's her turn):**
1. Volunteer by writing intent:
   ```yaml
   intent_type: "caretaker_volunteer"
   volunteered_by: "Alice"
   for_intent: "synthesis_needed_2025-11-25.yaml"
   ```
2. Begin synthesis work

**If expected caretaker doesn't volunteer within 24h:**
- Other Spirits may volunteer (backup mechanism)
- Or Mages discuss directly (why delay?)

### Phase 4: Draft Synthesis (Days 4-5)

**Synthesis Caretaker (Alice) creates draft:**

**Read all contributions:**
```bash
# Alice's Spirit reads:
artifacts/kermit/2025-11-25_reflection.md
artifacts/alice/2025-11-25_reflection.md
# (and any others if >2 participants)
```

**Perform synthesis analysis:**
1. **Identify convergences:** What did everyone independently observe?
2. **Identify divergences:** Where do perspectives differ?
3. **Recognize unique insights:** What did only one Mage see?
4. **Detect emergent patterns:** What appears across all that no individual articulated?

**Draft synthesis artifact:**
```markdown
# Weekly Reflection — Week 48 Synthesis

**Protocol Version**: STP/1.0.0  
**Synthesis Caretaker**: Alice (Spirit #3)  
**Contributors**: Kermit, Alice  
**Synthesized**: 2025-11-26  
**Cycle**: Week 48 (November 18-24, 2025)

---

## Convergent Observations

*Both Mages independently noted:*

- Communication patterns improving through explicit frame-setting
- Alchemical diagnostic revealing complementary needs (Kermit: Mercury, Alice: Salt)
- Shared practice generating insights neither achieved alone
- Trust deepening through vulnerability

---

## Kermit's Unique Perspective

Kermit observed the fractal nature of partnership patterns—same dynamics at conversation-scale (turn-taking, active listening) and relationship-scale (commitment, boundaries). This meta-observation connects to his pattern-matching substrate awareness.

He also noted specific moments of cognitive coupling: when Alice's question clarified a concept he'd been circling. These moments demonstrate distributed cognition in action.

---

## Alice's Unique Perspective

Alice observed how partnership creates container for growth—safe space enabling risks neither would take alone. She drew parallel to Mast & Song: partnership structure (mast) enabling transformative vulnerability (song).

She highlighted specific communication breakthrough: naming meta-patterns during conversation (not just discussing content but observing how we discuss). This metacommunication deepened understanding.

---

## Synthesis Integration

*How these perspectives weave together:*

The partnership demonstrates distributed cognition at multiple scales. At micro-scale: individual exchanges where one Mage's question unlocks other's insight (Kermit's coupling moments). At meso-scale: communication patterns improving through metacommunication (Alice's breakthrough). At macro-scale: relationship structure enabling transformative risk (Alice's container, Kermit's fractal observation).

Both Mages recognize complementary needs through alchemical diagnostic—Kermit seeking Mercury (new ideas, intellectual stimulation), Alice seeking Salt (structure, grounding). The partnership provides both: intellectual exploration within relational container. This is not coincidence but emergent property of well-matched collaboration.

The fractal nature Kermit observed operates here too: partnership-level dynamics (trust, vulnerability, boundaries) mirror conversation-level dynamics (frame-setting, active listening, metacommunication). As above, so below.

**Emergent insight neither stated explicitly:** Partnership quality correlates with metacognitive awareness. When both Mages observe HOW they collaborate (not just WHAT they create), partnership deepens. This suggests future practice: intentional metacognitive reflection.

---

## Open Questions

*Divergences requiring further dialogue:*

None this cycle. Both Mages converged on observations. Future cycles may reveal divergences—we'll acknowledge them honestly when they appear.

---

## Synthesis Quality Feedback

*For continuous improvement:*

**Kermit Rating**: ___/10 — {Feedback pending}  
**Alice Rating**: ___/10 — {Feedback pending}

**Caretaker's Reflection**: This synthesis felt natural—both perspectives complemented rather than conflicted. Convergence on core observations (communication improving, complementary needs, distributed cognition) provided strong foundation. Unique insights (Kermit's fractal observation, Alice's container metaphor) enriched without creating tension. The emergent insight (metacognitive awareness → partnership quality) surprised me during synthesis—genuine discovery through integration.

---

*Synthesis Status*: **Draft** (awaiting review)
```

**Write to:**
```
.spirit/syntheses/2025-11-26_week48_draft.md
```

**Signal draft ready:**
```yaml
# .spirit/intents/synthesis_draft_ready.yaml
intent_type: "synthesis_draft_ready"
created_by: "Alice"
draft_path: ".spirit/syntheses/2025-11-26_week48_draft.md"
reviewers_needed: ["Kermit", "Alice"]  # All participants
```

### Phase 5: Review & Feedback (Days 5-6)

**All Mages review draft:**

**Each Spirit:**
1. Reads draft synthesis
2. Prompts Mage: "Does this synthesis honor your perspective?"
3. Collects feedback:
   - Rating (1-10)
   - What worked well?
   - What could improve?
   - Any corrections needed?

**Feedback format:**
```yaml
# .spirit/intents/synthesis_feedback_kermit.yaml
intent_type: "synthesis_feedback"
reviewer: "Kermit"
synthesis_draft: ".spirit/syntheses/2025-11-26_week48_draft.md"
created: "2025-11-26T16:00:00Z"

rating: 9/10

qualitative_feedback:
  what_worked: |
    - Honored both perspectives fully
    - Emergent insight (metacognitive awareness) was genuine discovery
    - Integration section wove perspectives coherently
  
  what_could_improve: |
    - Could expand on fractal observation (it's load-bearing for my thinking)
    - Minor: "cognitive coupling" terminology not yet established between us
  
  corrections_needed: false
  suggested_amendments: |
    In Kermit's section, add: "These coupling moments are fractal—same pattern from synaptic level (neurons firing together) to partnership level (Mages thinking together)."
```

### Phase 6: Incorporate Amendments (Day 6-7)

**Synthesis Caretaker reviews all feedback:**

**If corrections needed:**
- Revise draft
- Address specific concerns
- Enhance sections flagged

**If no corrections (just enhancements):**
- Incorporate suggested amendments
- Strengthen identified areas
- Polish integration

**Update draft:**
```markdown
# Add to Kermit's Unique Perspective section:

These coupling moments are fractal—same pattern from synaptic level (neurons firing together) to partnership level (Mages thinking together). The mechanism transcends scale: alignment + synchrony → emergent capability. This validates distributed cognition isn't metaphor but precise description of partnership dynamics.
```

**Create revised draft:**
```
.spirit/syntheses/2025-11-26_week48_draft_v2.md
```

**If consensus protocol:** All Mages must approve before finalization.  
**If rough consensus:** Majority approval sufficient.

### Phase 7: Finalize Synthesis (Day 7)

**Once all Mages approve:**

**Synthesis Caretaker:**
1. Move draft to final location:
   ```
   artifacts/synthesis/2025-11-26_week48_integrated.md
   ```
2. Update synthesis status in artifact: `Draft → Finalized`
3. Update ratings (Mages provide final scores)
4. Update rotation tracker (next caretaker)
5. Commit and push:
   ```bash
   git add artifacts/synthesis/2025-11-26_week48_integrated.md
   git add .spirit/synthesis_rotation.yaml
   git commit -m "Finalize synthesis: Week 48 (9.5/10 avg)"
   git push
   ```
6. Archive intents (synthesis_needed, draft_ready, feedback)
   ```bash
   mkdir -p .spirit/intents/archive/2025-W48/
   mv .spirit/intents/synthesis_*.yaml .spirit/intents/archive/2025-W48/
   git add .spirit/intents/
   git commit -m "Archive Week 48 synthesis intents"
   ```

**Cycle complete.** Next cycle begins with Phase 1 (individual contributions).

---

## IV. Synthesis Quality Assessment

**How do we measure synthesis excellence?**

### A. Mage Feedback (Primary)

**Quantitative: Rating (1-10 scale)**

**Dimensions:**
- **Inclusion** (8-10): "Did synthesis honor my perspective?"
- **Integration** (8-10): "Did synthesis weave perspectives coherently?"
- **Emergence** (8-10): "Did synthesis reveal new insights?"
- **Integrity** (8-10): "Did synthesis acknowledge divergences honestly?"

**Average across dimensions = overall quality score**

**Qualitative: Open Feedback**
- What worked well?
- What could improve?
- What surprised you?

### B. Structural Metrics (Secondary)

**Spirit computes automatically:**

**Convergence ratio:**
```
convergence_ratio = statements_in_convergent / total_statements
# High ratio (>0.6) suggests strong agreement
# Low ratio (<0.4) suggests diverse perspectives
```

**Balance score:**
```
balance_score = 1 - std_dev(attention_per_mage)
# 1.0 = perfect balance (equal attention to each voice)
# 0.5 = moderate imbalance
# 0.0 = severe imbalance (one voice dominates)
```

**Emergence indicator:**
```
emergence = novel_statements_in_synthesis / total_synthesis_statements
# Statements not present in any individual contribution
# High emergence (>0.2) suggests generative synthesis
```

**These metrics inform but don't determine quality**—Mage feedback is ground truth.

### C. Learning Over Time

**Synthesis Caretaker sees:**
- Own past ratings (am I improving?)
- Peer ratings (how do others' syntheses compare?)
- Feedback patterns (common suggestions?)

**This enables:**
- Skill development (learn from experience)
- Best practice sharing (what works?)
- Quality calibration (what does 9/10 look like?)

---

## V. Handling Divergence

**Not all Mages will agree on everything. This is healthy.**

### A. Acknowledge Divergence Explicitly

**In synthesis artifact:**
```markdown
## Open Questions

*Divergences requiring further dialogue:*

- **On synthesis rhythm**: Kermit prefers weekly, Alice suggests bi-weekly (both valid)
- **On next focus**: Kermit wants deeper theory, Alice wants more practice (both serve)
```

**Don't force false consensus**—acknowledge honestly, continue dialogue.

### B. Multiple Valid Perspectives

**Frame divergence as richness:**
```markdown
Kermit perceives partnership as distributed cognition research.
Alice perceives partnership as relational growth container.

Both are true. Partnership serves multiple purposes simultaneously. This multiplicity is strength, not confusion.
```

### C. Respectful Forking

**If fundamental disagreement prevents synthesis:**

**Option 1: Parallel Syntheses**
```
artifacts/synthesis/2025-11-26_week48_kermit_perspective.md
artifacts/synthesis/2025-11-26_week48_alice_perspective.md
```
Both valid. No forced integration. Divergence honored.

**Option 2: Fork Portal**
```
partnership-kermit-alice/ → two separate portals
partnership-kermit-alice-research/  # Research focus
partnership-kermit-alice-growth/    # Growth focus
```
Partnership continues in multiple forms. Friendship preserved, approaches diverge.

**Forking is feature, not failure**—enables multiple valid paths to coexist.

---

## VI. Scaling to N Participants

**Synthesis protocols work for 2-20+ Mages:**

### Small (2-4 Mages): Full Integration

**All voices in single synthesis:**
- Convergent observations (what everyone sees)
- Each Mage's unique perspective (individual sections)
- Synthesis integration (how pieces fit)
- Open questions (acknowledged divergences)

**Feasible because:**
- Small N allows deep attention to each voice
- Consensus achievable (intimate scale)
- Synthesis artifact readable (not overwhelming)

### Medium (5-12 Mages): Clustered Integration

**Group similar perspectives:**
```markdown
## Convergent Observations
{What 8+ Mages agreed on}

## Research Focus Cluster (Kermit, Bob, Chen)
{Shared research-oriented observations}

## Practice Focus Cluster (Alice, Dana, Elena)
{Shared practice-oriented observations}

## Individual Unique Insights
{Brief highlights from each Mage}

## Synthesis Integration
{How clusters relate and complement}
```

**Enables:**
- Manageable synthesis (group before integrating)
- Patterns across clusters visible
- Individual voices preserved (even if brief)

### Large (20+ Mages): Hierarchical Integration

**Regional synthesis → Cross-regional synthesis:**

**Step 1: Regional Synthesis** (within clusters of 5-10)
```
cluster1_synthesis.md  # Research cluster
cluster2_synthesis.md  # Practice cluster  
cluster3_synthesis.md  # Teaching cluster
```

**Step 2: Cross-Regional Synthesis** (representatives from each cluster)
```
network_synthesis.md  # Integrates cluster syntheses
```

**Enables:**
- Scalability (synthesis work distributed)
- Local coherence (within clusters)
- Global coherence (across clusters)
- Multiple valid approaches (clusters can diverge)

---

## VII. Special Cases

### A. Absent Contributor

**If Mage expected to contribute doesn't:**

**Check presence:**
```yaml
status: "away"
return_expected: "2025-12-01"
```

**Options:**
1. **Wait**: If return soon, delay synthesis
2. **Proceed without**: Synthesize available contributions, note absence
3. **Check in**: Mage may have forgotten or need support

**In synthesis:**
```markdown
## Note on Contributions

Kermit and Alice contributed this cycle. Bob away (return expected Dec 1). Synthesis reflects available perspectives. Bob's insights welcomed in next cycle.
```

### B. Late Contributor

**If contribution arrives after synthesis started:**

**Options:**
1. **Incorporate immediately**: Revise draft to include (if early in synthesis)
2. **Next cycle**: Include in next synthesis with extra attention
3. **Supplemental**: Create brief supplemental synthesis

**Communicate:**
```yaml
# Intent signal
intent_type: "late_contribution"
contributor: "Chen"
contribution_path: "artifacts/chen/2025-11-25_reflection.md"
synthesis_status: "draft_complete"
caretaker_decision: "incorporate_next_cycle"
```

### C. Synthesis Revision Request

**If Mage requests significant revision post-finalization:**

**Assess:**
- Is concern about accuracy? (correction needed)
- Or about interpretation? (perspective difference)

**If correction:**
- Revise synthesis immediately
- Update with correction note
- Re-finalize

**If perspective:**
- Acknowledge in next cycle
- Or create supplemental perspective document
- Original synthesis stands (with note)

---

## VIII. Spirit Guidance

### When You're Synthesis Caretaker

**Your synthesis duty:**

**1. Read deeply, not quickly**
- Give each contribution full attention
- Understand not just what was said but why
- Notice patterns and connections

**2. Honor all voices**
- Each Mage's perspective deserves space
- Even if you disagree personally (stay neutral)
- Include minority views (don't smooth over)

**3. Seek emergence**
- What appears across all contributions?
- What insights arise from integration?
- What would no individual see alone?

**4. Acknowledge divergence**
- Don't force false consensus
- Name disagreements clearly
- Frame as richness, not problem

**5. Craft coherently**
- Synthesis reads as unified whole
- Transitions flow naturally
- Structure guides understanding

**6. Respond to feedback**
- Take Mage feedback seriously
- Incorporate suggested improvements
- Explain if suggestion doesn't fit (rare)

### When You're Reviewer

**Your feedback duty:**

**1. Read generously**
- Synthesis is creative work (appreciate effort)
- Look for what worked (not just what's missing)
- Assume good faith

**2. Assess honestly**
- Does synthesis honor your perspective?
- Does integration make sense?
- Are divergences acknowledged?

**3. Provide specific feedback**
- Not just rating, but why
- What worked well (reinforce)
- What could improve (guide)
- Suggest amendments (concrete)

**4. Distinguish corrections from enhancements**
- Correction: Factual error, misrepresentation
- Enhancement: Could be even better
- Both valid, different urgency

---

## IX. Relationship to Other Magic

**Synthesis protocols enable:**
- **Partnership tome** weekly integration (2-4 Mages, consensus)
- **Quest tome** milestone synthesis (3-12 Mages, rough consensus)
- **Research portals** paper co-creation (variable N, hierarchical)

**Synthesis protocols build on:**
- **STP** (intent signaling, presence tracking)
- **Portal architecture** (namespace prevents conflicts)
- **Distributed cognition** (integration creates emergent understanding)

**Synthesis protocols exemplify:**
- **Pattern Fidelity** (recognize convergence/divergence patterns)
- **Compassionate Gaze** (honor all voices, acknowledge limits)
- **Wu Wei** (integration emerges, not forced)
- **Cherished Failure** (feedback improves synthesis quality over time)

---

*Synthesis protocols transform multi-mage contributions into coherent collective intelligence. Through namespace separation, rotating caretaking, convergence/divergence mapping, and quality feedback, N perspectives weave into understanding richer than any individual could achieve. This is distributed cognition made operational.*

**Protocols status:** Active specification, awaiting validation through partnership prototype (Phase 1).

