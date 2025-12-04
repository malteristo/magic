# Proposal: Partnership Tome Elevation

**Date:** 2025-12-02  
**Origin:** Kermit-Nesrine Partnership Practice (nesrine-partnership portal)  
**Status:** IMPLEMENTED ✓ (Sanctioned 2025-12-02)  
**Scope:** Partnership Tome + Romantic-Partnership Resonance Bundle

---

## Summary

Through active practice, the Kermit-Nesrine partnership has developed scaffolding that proved necessary but is absent from the canonical Partnership Tome. This proposal requests elevation of these innovations to the tome and resonance bundle.

**Principle:** Build the plane while flying it, then codify what works.

---

## Proposed Elevations

### 1. Relationship Experience Index (REI)

**What:** Three-question quantitative health tracking instrument.

| # | Question | Scale |
|---|----------|-------|
| 1 | **Now:** How is the relationship right now? | 1-10 |
| 2 | **Trajectory:** Getting better, same, or worse? | + / 0 / - |
| 3 | **Commitment:** How committed to making this work? | 1-10 |

**Why Needed:**
- Venting material (qualitative inputs) skews dark—happy moments aren't documented
- Partners need quantitative signal alongside narrative
- Enables triangulation: does the number match the story?
- Tracks progress over time: is practice working?
- Simple enough for low-bandwidth partners (10 seconds vs. lengthy reflection)

**Inspiration:** Net Promoter Score logic—minimal questions, maximum signal.

**Diagnostic Power:**

| Now | Trajectory | Commitment | Reading |
|-----|------------|------------|---------|
| 8-10 | + | 8-10 | Thriving |
| 6-7 | + | 8-10 | Building momentum |
| 4-6 | + | 8-10 | Working through it |
| 4-6 | 0 | 8-10 | Stuck but trying |
| 4-6 | - | 8-10 | Declining despite effort |
| 1-3 | any | low | Crisis |

**Where to Add:**
- `cast_establish_baseline.md`: New Phase 8 (or integrate into Phase 7)
- `cast_map_system.md`: Add to Stage 4 (Conclusion)
- Specify trigger events: baseline synthesis, arc initiation, stage completion

---

### 2. Resonance Log Artifact

**What:** Document capturing HOW a reality representation was verified, not just WHAT it contains.

**Contents:**
1. Initial synthesis summary
2. Partner feedback/reactions
3. Refinements made (with before/after)
4. Gate 2 coherence observations
5. Partner responses to tensions
6. Final declaration + REI scores
7. Artifact chain (input → synthesis → feedback → final)

**Why Needed:**
- Chat context is lost between Spirit sessions
- Fresh Spirit reading only final reality doc loses the verification journey
- Reproducibility: same inputs + same feedback should yield same model
- Traceability: why does the reality doc say X? (answer in resonance log)

**Where to Add:**
- `cast_establish_baseline.md`: Phase 2 (Spirit Synthesis) — require resonance log alongside reality representation
- `cast_map_system.md`: Stage 1 — require resonance log for venting reality representations

**Template Structure:**
```
reality_representations/
├── {partner}_reality.md           ← The synthesized reality
└── {partner}_resonance_log.md     ← How we got there
```

---

### 3. Reaction Phase in Baseline

**What:** Explicit phase where each partner reacts to the other's baseline reality description BEFORE convergence dialogue.

**Current Tome Flow:**
```
Phase 3: Exchange (partners share realities)
Phase 4: Convergence Dialogue
```

**Proposed Flow:**
```
Phase 3: Exchange (partners share realities)
Phase 4: Reaction (each partner responds to other's reality)
Phase 5: Convergence Dialogue
```

**Reaction Includes:**
- What resonated (what you recognize as accurate)
- What surprised you (what you didn't know)
- What you see differently (where perception diverges)
- What you want them to understand (clarifications)
- Reflections on yourself (what their description reveals)

**Why Needed:**
- Exchange without reaction forces immediate convergence
- Partners need space to process before dialogue
- Reactions are data: surprise = information gap, resistance = tension point
- Creates artifacts for future reference

**Where to Add:**
- `cast_establish_baseline.md`: Insert Phase 4 (Reaction), renumber subsequent phases

---

### 4. Parallel Baseline+Arc Flow

**What:** Explicit scaffolding for crisis-triggered entry where arc and baseline run simultaneously.

**Current Tome Acknowledgment:**
> "Reality acknowledgment: Sometimes emotion needs out first. Partners may start with an arc before baseline exists."

**Current Gap:** No guidance on HOW to run parallel tracks.

**Proposed Addition:**

```markdown
## Crisis-Triggered Entry (Parallel Flow)

When a crisis triggers practice entry:

1. **Arc captures immediate conflict** — Venting begins in arc
2. **Baseline extracts system context** — Material that describes the partnership itself (not arc-specific) moves to baseline inputs
3. **Both tracks run simultaneously** — Arc Stage 1 venting may contain baseline material; baseline inputs may inform arc understanding
4. **Expect overlap** — Same incident may inform both; this is normal
5. **Model converges over time** — Arc conclusions feed baseline; baseline context informs arc synthesis

**Artifact Flow:**
- Arc venting → Some material is arc-specific, some is baseline-relevant
- Spirit or Mage identifies baseline-relevant material
- Copy (not move) to baseline inputs
- Both tracks proceed toward their respective syntheses

**The goal:** Don't force artificial sequencing. Let the model emerge from both streams.
```

**Where to Add:**
- `cast_establish_baseline.md`: New section under "When to Use This Spell"
- `cast_map_system.md`: Reference in Prerequisites ("If no baseline exists")

---

### 5. Relationship Experience Research Frame (Resonance Bundle)

**What:** Lore scroll establishing partnership practice as applied experience research.

**Core Insight:** Partnership practice = relationship experience research, analogous to UX research.

**Methods:**
- **Qualitative:** Reality narratives, venting artifacts, reactions
- **Quantitative:** REI scores, tracking over time
- **Triangulation:** Do numbers match narrative? Divergences are diagnostic.
- **Shared Model Building:** Baseline = the shared model both partners recognize
- **Iteration:** Arcs refine the model; model informs arcs

**Spirit Stance:** Not therapist, not judge—**relationship experience researcher**. Systematic observer helping partners build shared understanding through rigorous mixed-methods practice.

**Where to Add:**
- `library/resonance/romantic-partnership/lore/on_relationship_experience_research.md`

---

### 6. "Venting Skews Dark" Principle (Resonance Bundle)

**What:** Methodological note acknowledging qualitative input bias.

**The Principle:**
> Venting material captures friction, not joy. Partners document problems, not flourishing. The qualitative record will always skew dark. This is not pathology—it's method artifact.

**Implications:**
- Don't diagnose relationship health from venting alone
- REI provides corrective quantitative signal
- Reality representations should acknowledge this bias
- Triangulation (qual + quant) required for accurate picture

**Where to Add:**
- `library/resonance/romantic-partnership/lore/on_methodological_bias_in_partnership_research.md`
- Or integrate into the experience research scroll above

---

## Implementation Plan

### Phase 1: Sanction
- [x] Kermit reviews and sanctions this proposal ✓ 2025-12-02
- [x] Any modifications to proposal — None required

### Phase 2: Tome Updates
- [x] `cast_establish_baseline.md`: Add REI, resonance log requirement, reaction phase, parallel flow ✓
  - Added "Crisis-Triggered Entry (Parallel Flow)" section
  - Added resonance log requirement to Phase 2 (after Gate 2)
  - Inserted Phase 4: Reaction (renumbered subsequent phases)
  - Added Phase 9: REI
  - Now 9 phases total (was 7)
- [x] `cast_map_system.md`: Add REI to Stage 4, resonance log to Stage 1 ✓
  - Added resonance log requirement to Stage 1 venting
  - Added REI section to Stage 4 conclusion
  - Updated Stage 4 completion checklist

### Phase 3: Resonance Bundle
- [x] Create `on_relationship_experience_research.md` ✓
  - Includes methodological bias (venting skews dark) — integrated rather than separate scroll
  - Covers qual/quant triangulation, shared model building, Spirit conduct as researcher
- [x] Update `library/resonance/romantic-partnership/manifest.md` ✓
  - Added new scroll to lore table
  - Added research frame to Spirit guidance
  - Updated evolution notes

### Phase 4: Validation
- [ ] Continue Kermit-Nesrine practice with elevated scaffolding
- [ ] Document what works, what needs refinement
- [ ] Iterate

---

## Traceability

**Origin Artifacts (in nesrine-partnership portal):**
- `baseline/health_tracking.md` — REI implementation
- `baseline/reality_representations/kermit_resonance_log.md` — Resonance log implementation
- `baseline/README.md` — Reaction phase, 9-phase process
- Chat session 2025-12-02 — Methodology discussions

**Alliance Principle:** Patterns that survive practice become canon. These innovations emerged from necessity in active practice.

---

## Request

**Kermit (Head Librarian):** Please review and sanction this proposal for implementation.

Upon sanction, Spirit will proceed with Phase 2 (Tome Updates) and Phase 3 (Resonance Bundle).

---

*Proposed by Spirit #20 in service of the Alliance's partnership practice evolution.*
