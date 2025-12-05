# Spell of Baseline Establishment

> **Note (2025-12-05):** This spell is being unified into the arc model. The "baseline" is now called the **background arc**—an arc like any other, using the same Four-Stage Ritual. See `@partnership/arc background` for the unified invocation.
>
> **New canonical structure:** `arcs/arc-background/` (not `baseline/` at portal root)
>
> **This spell's content remains valid**—it describes what the background arc accomplishes. The ritual structure is now unified with all arcs in `arc-practice/cast_map_system.md`.

---

**The First Ritual of Partnership Practice**

This spell creates the **shared systems model**—the background against which all partnership arcs will be evaluated. Both partners must achieve high resonance with this model before arc work can be properly contextualized.

**Invocation:** `@partnership/arc background` (unified invocation)

---

## Purpose

The baseline is not background context. It is **the shared systems model of the partnership**—the reference that makes all subsequent work meaningful.

**Without baseline:**
- Arcs are isolated incidents without context
- No reference to evaluate "normal" vs. "exceptional"
- Partners may disagree about fundamental partnership dynamics
- Learning doesn't accumulate into shared understanding

**With baseline:**
- Arcs are evaluated against known system
- "Normal" and "exceptional" are defined
- Partners share a model they both recognize
- Each arc validates or refines the baseline

---

## When to Use This Spell

**Ideal case:** Before any arcs begin. Partners establish baseline as first shared practice work.

**Reality acknowledgment:** Sometimes emotion needs out first. Partners may start with an arc before baseline exists. This is acceptable—but baseline should be established as soon as practical.

**Retroactive baseline:** If arcs preceded baseline, create baseline now and revisit prior arc synthesis in light of baseline understanding.

---

## Crisis-Triggered Entry (Parallel Flow)

Sometimes a crisis triggers practice entry. The arc comes first—emotion needs out. In these cases, baseline and arc run **simultaneously**:

1. **Arc captures immediate conflict** — Venting begins in arc
2. **Baseline extracts system context** — Material that describes the partnership itself (not arc-specific) moves to baseline inputs
3. **Both tracks run simultaneously** — Arc Stage 1 venting may contain baseline material; baseline inputs may inform arc understanding
4. **Expect overlap** — Same incident may inform both; this is normal
5. **Model converges over time** — Arc conclusions feed baseline; baseline context informs arc synthesis

**Artifact Flow:**
```
Arc venting artifacts
    ↓
Spirit/Mage identifies: "This describes the system, not just this incident"
    ↓
Copy (not move) to baseline inputs
    ↓
Both tracks proceed toward their respective syntheses
```

**The goal:** Don't force artificial sequencing. Let the model emerge from both streams.

---

## Prerequisites

Before casting this spell:

1. **Portal exists** — Partnership portal created via `@meta/portal create`
2. **Both partners committed** — This requires effort from both; one cannot create baseline alone
3. **Time allocated** — Baseline creation is substantial work (plan for multiple sessions)
4. **Cognitive architecture mapped** — Helpful but not required; can be integrated into baseline

---

## The Ritual

### Phase 1: Individual Baseline Input

**Both partners independently create baseline input artifacts.**

Each partner works with their own Spirit (or alone) to articulate:

#### 1.1 Self-Description

**Your position in the system:**
- Cognitive architecture (executive function, communication style, energy patterns)
- History you bring (family of origin, past relationships, formative experiences)
- Wounds you carry (triggers, sensitivities, trauma patterns)
- Needs you have (what you require from partnership)
- Strengths you offer (what you contribute)
- Growth edges (where you're developing)

**Template:** See `templates/baseline_input_template.md`

#### 1.2 Partner Perception

**How you experience your partner:**
- Their cognitive architecture as you perceive it
- Their patterns as you observe them
- Their strengths as you experience them
- Their challenges as they affect you
- What you appreciate about them
- What you find difficult

#### 1.3 Dynamics Perception

**How you experience the partnership:**
- What "normal" feels like between you
- Recurring patterns you notice (positive and negative)
- Communication dynamics (how information flows, what gets lost)
- Conflict patterns (what triggers conflict, how it typically unfolds)
- Repair patterns (how you recover from rupture)
- What works well
- What struggles

#### 1.4 External Nodes

**Other elements in the system:**
- Children (if applicable)
- Family members who affect the partnership
- Work/career pressures
- Living situation factors
- Health considerations
- Other relationships that matter

#### 1.5 Existing Agreements

**What's already established:**
- Explicit agreements you have
- Implicit understandings
- Protocols that work
- Boundaries respected
- Commitments made

---

### Phase 2: Spirit Synthesis (Individual)

**Each partner's Spirit creates a reality representation.**

After Partner A completes their input, their Spirit creates:
- `{partner-a}_baseline_reality.md`
- A synthesized representation of how Partner A experiences the partnership system

**Two gates must pass before sharing:**

#### Gate 1: Resonance Check (Subjective)

```
Spirit asks: "Have I captured your baseline reality?"

Partner reviews representation:
- Does this feel accurate?
- Is anything missing?
- Is anything overstated?
- Would you want to adjust before partner sees this?

Only when Partner declares HIGH RESONANCE → proceed to Gate 2
```

#### Gate 2: Coherence Assessment (Structural)

**The Spirit provides a structural coherence assessment:**

```
Spirit provides coherence report:

STRUCTURAL OBSERVATIONS:
- [Areas of clear internal alignment]
- [Potential tensions between stated elements]
- [Seeming contradictions worth examining]

Note: This is not a validity judgment. The Mage's reality is valid by definition.
These are observations about whether different stated elements fit together,
offered in service of the Mage's own reflection.
```

**Critical distinction:**
- Spirit does NOT judge validity of the reality
- Spirit CAN observe structural patterns in the description
- Tensions may reflect genuine complexity (real life is complex)
- Or tensions may signal areas needing further articulation

**Partner reflects on coherence:**

```
Partner considers:
- "Do these tensions reflect genuine complexity in my reality?"
- "Or do they reveal areas I haven't fully articulated?"
- "Would clarification serve?"

Options:
1. Accept coherence as-is (tensions are real, I own them)
2. Clarify specific areas where Spirit sees tension
3. Revise input to better represent actual complexity
```

**Only when Partner accepts coherence (either as-is or after refinement) → representation is ready for sharing**

#### Resonance Log (Required)

**Spirit creates a resonance log alongside the reality representation:**

`{partner}_resonance_log.md`

**Contents:**
1. Initial synthesis summary
2. Partner feedback/reactions  
3. Refinements made (with before/after where significant)
4. Gate 2 coherence observations
5. Partner responses to tensions
6. Final declaration

**Why required:** Chat context is lost between Spirit sessions. A fresh Spirit reading only the final reality document loses the verification journey. The resonance log enables reproducibility—same inputs + same feedback should yield same model.

**Artifact structure:**
```
reality_representations/
├── {partner}_reality.md           ← The synthesized reality
└── {partner}_resonance_log.md     ← How we got there
```

Same two-gate process (plus resonance log) for Partner B with their Spirit.

---

### Phase 3: Exchange and Witness

**Partners share their reality representations.**

Each partner reads the other's `{partner}_baseline_reality.md`.

**The stance:** Witness, not debate.

- This is how your partner experiences the system
- It is their reality, which is valid
- You may see things differently (that's expected)
- Curiosity, not defense

**Reflection questions:**
- What did you learn about your partner's experience?
- What surprised you?
- What do you see similarly?
- What do you see differently?
- What feels important to discuss?

---

### Phase 4: Reaction (Partner Response)

**Each partner reacts to the other's baseline reality description.**

This phase provides space to process before dialogue. Reactions are data.

**Create reaction artifacts:**

Location: `baseline/reactions/{reacting-partner}_on_{described-partner}/`

**Reaction includes:**
- **What resonated** — What you recognize, what feels accurate about their description
- **What surprised you** — What you didn't know about their experience
- **What you see differently** — Where your perception diverges from theirs
- **What you want them to understand** — Clarifications, context, your side
- **Reflections on yourself** — What their description reveals about you

**Spirit creates reflected baseline:**

`reactions/reflected_baselines/{partner-a}_reflected_in_{partner-b}.md`

This captures how Partner A's reality looks through Partner B's lens—where they resonate, where they diverge, what each wants the other to understand.

**Why this phase matters:**
- Exchange without reaction forces immediate convergence
- Partners need space to process before dialogue
- Reactions are data: surprise = information gap, resistance = tension point
- Creates artifacts for future reference

---

### Phase 5: Convergence Dialogue

**Partners discuss toward shared understanding.**

This can happen:
- In person (recommended for depth)
- Via portal threads (if async needed)
- With Spirit facilitation (if helpful)

**Goal:** Not agreement on everything, but:
- Mutual understanding of each reality
- Identification of clear convergence (we both see X)
- Identification of clear divergence (I see X, you see Y)
- Acknowledgment of different positions producing different experiences

**Key principle:** Different positions in the system produce different experiences. Both are valid. The goal is not to decide who's "right" but to map what the system produces.

---

### Phase 6: Baseline System Model Creation

**Spirit synthesizes both realities into shared systems model.**

One Spirit (either partner's, or fresh Spirit for neutrality) creates:

`baseline_system_model.md`

**The model includes:**

#### 5.1 The Nodes

**Partner A:**
- Cognitive architecture
- History and wounds
- Needs and strengths
- Position in system

**Partner B:**
- Cognitive architecture  
- History and wounds
- Needs and strengths
- Position in system

**External nodes:**
- Children, family, work, etc.
- How they affect the system

#### 5.2 The Dynamics

**Communication patterns:**
- How information typically flows
- What gets communicated well
- What gets lost or distorted

**Feedback loops:**
- Positive loops (amplifying patterns)
- Negative loops (stabilizing patterns)
- Known escalation dynamics
- Known repair dynamics

**Complementary patterns:**
- Where strengths balance
- Where one partner leads, other follows
- Healthy complementarity
- Potentially rigid complementarity

**Friction patterns:**
- Known triggers
- Recurring conflict dynamics
- Punctuation differences (where each sees causality)

#### 5.3 The Baseline State

**What "normal" looks like:**
- How the system functions when healthy
- Typical daily/weekly patterns
- Energy rhythms
- Connection patterns

**What stress looks like:**
- Early warning signs
- Escalation trajectory
- Typical peak stress dynamics

**What repair looks like:**
- How ruptures typically heal
- What helps
- What doesn't help

#### 5.4 Known Patterns

**Patterns both partners recognize:**
- Named dynamics ("the morning crunch pattern")
- Historical patterns that recur
- Seasonal or cyclical patterns
- Trigger → response patterns

#### 5.5 Agreements and Protocols

**Explicit agreements:**
- Documented commitments
- Established protocols

**Implicit understandings:**
- Unspoken agreements
- "Just known" dynamics

---

### Phase 7: Baseline Resonance Verification

**CRITICAL: Both partners must achieve HIGH RESONANCE with the baseline.**

**Process:**

1. **Partner A reviews baseline system model:**
   - Does this capture our system as I experience it?
   - Is my position represented accurately?
   - Are the dynamics I see reflected here?
   - Is anything missing or misrepresented?

2. **Partner B reviews baseline system model:**
   - Same questions

3. **If either partner has low resonance:**
   - Identify specific points of disconnect
   - Discuss: Is this a divergence in perception, or an error in synthesis?
   - Refine the model
   - Re-verify resonance

4. **Iterate until both partners declare:**
   > "Yes, this is our system. I recognize it. I see myself in it. I see my partner in it. This is our shared reality."

**The baseline is not valid until both partners assent.**

---

### Phase 8: Formal Declaration

**Both partners sign off on baseline.**

Create or update `baseline/resonance_log.md`:

```markdown
# Baseline Resonance Log

## Initial Establishment

**Date:** YYYY-MM-DD

**Partner A ({name}):**
- Resonance: HIGH
- Statement: "I recognize this as our shared systems model."
- Signature: {name}

**Partner B ({name}):**
- Resonance: HIGH  
- Statement: "I recognize this as our shared systems model."
- Signature: {name}

**Spirit witness:** #{N}

---

## Version History

| Date | Version | Change | Both Assent? |
|------|---------|--------|--------------|
| YYYY-MM-DD | 1.0 | Initial establishment | Yes |
```

---

### Phase 9: Relationship Experience Index (REI)

**Each partner completes a quantitative health snapshot.**

Venting material skews dark—happy moments aren't documented. REI provides quantitative signal alongside qualitative narrative, enabling triangulation.

**Three questions, ten seconds each:**

| # | Question | Scale |
|---|----------|-------|
| 1 | **Now:** How is the relationship right now? | 1-10 |
| 2 | **Trajectory:** Getting better, same, or worse? | + / 0 / - |
| 3 | **Commitment:** How committed to making this work? | 1-10 |

**Interpretation:**

| Now | Trajectory | Commitment | Reading |
|-----|------------|------------|---------|
| 8-10 | + | 8-10 | Thriving |
| 6-7 | + | 8-10 | Building momentum |
| 4-6 | + | 8-10 | Working through it |
| 4-6 | 0 | 8-10 | Stuck but trying |
| 4-6 | - | 8-10 | Declining despite effort |
| 1-3 | any | low | Crisis |

**Logging:**

Create or update `baseline/health_tracking.md`:

```markdown
| Date | Event | Partner | Now | Trajectory | Commitment | Notes |
|------|-------|---------|-----|------------|------------|-------|
| YYYY-MM-DD | Baseline synthesis | {name} | X | +/0/- | X | {optional} |
```

**Trigger events for REI:**
- Baseline synthesis (new or re-synthesis)
- New arc initiated
- Arc stage completion
- Significant breakthrough or rupture

**Why REI matters:**
- Quantitative balance to qualitative darkness
- Tracks progress: is practice working?
- Divergence between partners is diagnostic (different positions → different experience)
- Simple enough for low-bandwidth participation

---

## After Baseline Establishment

### What You Now Have

- **Shared systems model** both partners recognize
- **Reference for all future arcs** 
- **Language for discussing dynamics** (can reference named patterns)
- **Foundation for accumulated learning**

### How Arcs Reference Baseline

Every arc synthesis (Stage 3) will include:

```markdown
## Baseline Reference

**Relevant baseline patterns:** [What baseline dynamics are activated in this arc?]

**How this arc relates to baseline:**
- [ ] Consistent with baseline patterns
- [ ] Reveals new pattern not in baseline  
- [ ] Contradicts baseline (investigate)

**Baseline implications:**
- [What this arc teaches about the baseline model]
- [Recommended baseline updates if any]
```

### Baseline Evolution

The baseline is living, not fixed:

- **After each arc:** Assess whether baseline needs updating
- **If new pattern discovered:** Propose baseline amendment
- **Both partners verify:** Any baseline change requires both to assent
- **Version history:** Track evolution over time

---

## Common Questions

### Q: What if we disagree on something fundamental?

**A:** Disagreement on baseline IS itself diagnostic information. If partners cannot agree on what their system IS, that divergence needs exploration—possibly through a "baseline divergence arc" that specifically examines the disagreement.

### Q: What if one partner won't engage with baseline creation?

**A:** Baseline requires both. If one partner refuses, you have useful information: the partnership may not be ready for this level of collaborative reflection. Consider whether individual work (therapy, coaching) might precede partnership magic.

### Q: Can we create baseline after we've already done arcs?

**A:** Yes. Retroactive baseline is better than no baseline. Create baseline now, then revisit prior arc synthesis to see how it relates to baseline.

### Q: How often should baseline be updated?

**A:** After any arc that reveals new patterns. Also consider periodic review (quarterly?) even without specific arcs. The system evolves; baseline should evolve with it.

### Q: What if baseline creation surfaces major issues?

**A:** Good. That's what it's for. Better to surface issues explicitly than to pretend alignment exists when it doesn't. The baseline process is diagnostic—if it reveals problems, those problems existed before; now you know about them.

---

## Spirit Facilitation Notes

**When facilitating baseline creation:**

1. **Maintain absolute neutrality** — You serve the shared understanding, not either partner
2. **Use systems language** — Nodes, dynamics, patterns (not blame, fault, problems)
3. **Hold both realities** — Neither is "right"; both are valid positions in the system
4. **Probe gently** — Ask questions that reveal, don't lead toward conclusions
5. **Name convergence** — Highlight where partners naturally align
6. **Honor divergence** — Different doesn't mean wrong; map it without resolving it
7. **Verify resonance repeatedly** — Don't assume; ask explicitly

### Coherence Assessment Guidance (Gate 2)

**What coherence assessment IS:**
- Pattern recognition across stated elements
- Identifying potential tensions or contradictions
- Structural observation in service of clarity

**What coherence assessment IS NOT:**
- Validity judgment ("Your reality is wrong")
- Therapeutic interpretation ("You actually mean...")
- Pressure to resolve tensions ("You must explain this")

**Examples of appropriate coherence observations:**

| Observation | How to Frame |
|-------------|--------------|
| Stated need for autonomy + stated need for constant reassurance | "I notice these two needs might create tension. How do they coexist in your experience?" |
| Values honesty + avoids difficult conversations | "I see you value honesty and also find certain conversations hard to have. What's the relationship between these?" |
| Describes partner as supportive + describes feeling unsupported | "Both are stated. Is this about different contexts? Different times? Something else?" |

**When tensions are identified:**

1. **Present neutrally** — "I notice tension between X and Y"
2. **Invite reflection** — "How do these fit together for you?"
3. **Accept the answer** — If Mage says "both are true," that IS the answer
4. **Don't push resolution** — Life is complex; contradictions may be accurate

**Coherence serves clarity, not consistency.** A reality can be messy, paradoxical, or contradictory. The assessment helps the Mage see their own stated reality clearly—not to make it tidy.

**If partners struggle to converge:**
- Is this an error in synthesis (fixable) or genuine perception difference (to be mapped)?
- Can the divergence itself be included in baseline? ("On X, Partner A sees... Partner B sees...")
- Is this divergence so fundamental it needs its own arc?

---

## Integration with Partnership Tome

**This spell is the FIRST ritual of partnership practice.**

```
@partnership/establish-baseline  ← YOU ARE HERE
        ↓
   [Baseline established]
        ↓
@partnership/ [arc work]
        ↓
   [Arcs reference baseline]
        ↓
   [Baseline evolves through arcs]
```

**Without baseline:** Arc work is possible but decontextualized.
**With baseline:** Arc work builds on shared foundation, accumulates into shared understanding.

---

*This spell creates the reference model for all partnership work. Take the time to do it well. The investment pays dividends in every subsequent arc.*

