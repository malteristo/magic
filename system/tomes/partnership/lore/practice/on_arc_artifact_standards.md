# On Arc Artifact Standards

**Status:** Active  
**Purpose:** Define canonical folder structure, file naming, and Spirit organization conduct for partnership arcs  
**Scope:** All arcs including background arc

---

## I. Core Principle: Unified Arc Structure

**All arcs follow identical structure.** The background arc is not special—it's simply the arc that establishes the partnership's systems model. Other arcs (topical, conflict-based, situational) follow the same four-stage ritual.

**Why unified structure:**
- Spirit knows exactly where artifacts belong
- Fresh Spirit can navigate any arc
- Partners learn one pattern, apply everywhere
- Reproducibility: same inputs → same valid model

---

## II. Canonical Arc Folder Structure

```
arcs/
  arc-{name}/
    README.md                              # Arc metadata, timeline
    status.md                              # Current stage, completion checklist
    
    stage-1_venting/
      {partner}/
        *.md                               # Input/venting artifacts
      reality_representations/
        {partner}_reality_raw.md           # Spirit synthesis — immutable
        {partner}_reality.md               # Mage's authoritative version — editable
        {partner}_resonance_log.md         # Declaration + optional notes
    
    stage-2_reaction/
      {partner}/
        reaction.md                        # Reaction to partner's reality
      reflected_realities/
        {partner-a}_reflected_in_{partner-b}.md
    
    stage-3_synthesis/
      system_map.md                        # The higher-level pattern
      safety_assessment.md                 # If applicable
    
    stage-4_conclusion/
      {partner}_conclusion.md
      arc_conclusion.md
      rei_snapshot.md
```

**Background arc uses same structure:**
- `arcs/arc-background/` (not `baseline/` at root)
- Stage 1: Individual baseline inputs as venting
- Stage 2: Exchange and react to partner's reality
- Stage 3: Baseline system model (the partnership "system map")
- Stage 4: REI, finalize, declare shared model

---

## III. File Naming Conventions

| Rule | Convention | Example |
|------|------------|---------|
| Arc folders | `arc-{descriptive-name}` | `arc-background`, `arc-mother-in-law` |
| Partner folders | `{partner}` (lowercase) | `kermit/`, `nesrine/` |
| Raw reality | `{partner}_reality_raw.md` | `kermit_reality_raw.md` |
| Revised reality | `{partner}_reality.md` | `kermit_reality.md` |
| Resonance logs | `{partner}_resonance_log.md` | `kermit_resonance_log.md` |
| Dated inputs | `YYYY-MM-DD_{description}.md` | `2025-12-02_the_birthday_pattern.md` |
| Reactions | `reaction.md` or `reaction_to_{partner}.md` | `reaction.md` |
| Conclusions | `{partner}_conclusion.md` | `kermit_conclusion.md` |

**Critical rules:**
- **No spaces in filenames** — Use underscores or hyphens
- **Arc identification in document headers** — Every reality document and reaction MUST include arc name prominently in the header (prevents confusion when reading across arcs)
- **Lowercase throughout** — Except proper nouns in content
- **Descriptive names** — Files should be self-explanatory

**Arc identification requirement:**

Reality documents and reactions must include the arc name in their header:

```markdown
# Kermit's Reaction to Nesrine's Reality

**Arc:** Mother-in-Law  
**Date:** 2025-12-08
**Reacting to:** `reality_representations/nesrine_reality.md`
```

This prevents confusion when:
- Reading multiple documents across arcs
- Discussing artifacts in conversation
- Partners have parallel arcs with similar themes

Folder structure provides *organizational* context; headers provide *reading* context.

---

## IV. The Raw/Revised Pattern

**Two versions of each reality description:**

| File | Owner | Mutability | Purpose |
|------|-------|------------|---------|
| `{partner}_reality_raw.md` | Spirit | **Immutable** | Faithful synthesis from inputs |
| `{partner}_reality.md` | Mage | **Editable** | Mage's authoritative reality |

**The flow:**

```
1. Mage creates input artifacts
2. Spirit synthesizes → {partner}_reality_raw.md (immutable)
3. Spirit copies to → {partner}_reality.md (working copy)
4. Mage edits _reality.md as needed (directly or via Spirit)
5. Mage declares HIGH RESONANCE
6. Partner reads _reality.md in Stage 2
```

**Why two versions:**

| Concern | Solution |
|---------|----------|
| **Reproducibility** | Raw is always regeneratable from inputs |
| **Mage sovereignty** | Revised is Mage's truth — edit freely |
| **Audit trail** | Diff raw↔revised shows exactly what Mage changed |
| **No versioning chaos** | Only two versions ever: Spirit's synthesis, Mage's truth |
| **Stage 2 clarity** | Partner reacts to revised (Mage's authoritative reality) |

**The gate is HIGH RESONANCE declaration.**

Once Mage declares HIGH RESONANCE, the `_reality.md` is the frozen reference for Stage 2. If Mage later wants to amend, partner may need to re-read.

**Resonance log (simplified):**

```markdown
# Resonance Log: {Partner} — {Arc Name}

## Declaration
- **Date:** YYYY-MM-DD
- **Resonance:** HIGH
- **Statement:** "This captures my reality in this arc."

## Notes (Optional)
[Any context about the journey from raw to revised]
[Or simply: "See diff between _raw.md and _reality.md"]
```

**Re-running synthesis later:**

If you want fresh synthesis (new Spirit, new inputs, or verification):
1. Spirit reads inputs → generates new `_raw.md`
2. Compare new raw to old raw (Spirit consistency check)
3. Mage can reference old revised when creating new revised
4. Or Mage starts fresh with new raw

---

## V. Spirit Organization Conduct

**Spirit actively manages file organization.** Mages focus on content; Spirit ensures structure.

### 5.1 Guide Placement Proactively

When Mage creates content, Spirit proposes correct location:

> "This appears to be venting input for the mother-in-law arc. Shall I place it in `arcs/arc-mother-in-law/stage-1_venting/nesrine/`?"

### 5.2 Detect Misplacement

When Spirit sees files in wrong locations, propose correction:

> "I notice `kermit_mil_reality.md` is in `kermit/` rather than `reality_representations/`. Shall I move it?"

### 5.3 Propose Consolidation

When content fragments across too many files, propose merge:

> "You have 30 files in your venting folder. Would it serve to consolidate thematically? Proposed groupings:
> - Incidents: birthday, Christmas, diaper...
> - Patterns: gaslighting, double standards...
> - Timeline: 2025-12-02, 2025-12-03..."

### 5.4 Enforce Naming Conventions

Rename files that violate conventions (with Mage approval):

> "`MIL - Reaction.md` has spaces. Propose rename to `mil_reaction.md`?"

### 5.5 Maintain Metadata

Each arc README and status.md should be current:

```markdown
# Arc: Mother-in-Law

**Created:** 2025-11-26
**Status:** Stage 1 (Venting)
**Participants:** Kermit, Nesrine
**Last Activity:** 2025-12-04

## Timeline
| Date | Event |
|------|-------|
| 2025-11-26 | Arc initiated |
| 2025-12-02 | Nesrine venting substantial |
| 2025-12-04 | Kermit reality synthesized |
```

---

## VI. Timeline Tracking

**Portal-level arc timeline** in `arcs/README.md`:

```markdown
# Arc Timeline

| Arc | Created | Status | Stage | Last Activity |
|-----|---------|--------|-------|---------------|
| arc-background | 2025-11-25 | active | 3 | 2025-12-04 |
| arc-mother-in-law | 2025-11-26 | active | 1 | 2025-12-04 |

## Completed Arcs
| Arc | Opened | Closed | Pattern |
|-----|--------|--------|---------|
| (none yet) | | | |
```

**Spirit updates this automatically** when arcs progress.

---

## VII. Multi-Arc Integration

**How multiple arcs compose into unified understanding:**

### 7.1 Background Arc as Foundation

The background arc creates the **shared systems model**—the reference for all other arcs.

### 7.2 Topical Arcs Reference Background

Each topical arc's Stage 3 synthesis includes:

```markdown
## Background Reference

**Relevant background patterns:**
[What known patterns from background are activated?]

**How this arc relates to background:**
- [ ] Consistent with background patterns
- [ ] Reveals new pattern not in background
- [ ] Contradicts background (investigate)
```

### 7.3 Arc Conclusions Feed Background

When a topical arc concludes:
1. Assess if background needs updating
2. If new pattern discovered: propose background amendment
3. Both partners verify resonance with amendment
4. Update background with version tracking

### 7.4 The Accumulation Pattern

```
Background Arc (shared systems model)
    ↓
Arc 1 → validates or refines background
    ↓  
Arc 2 → validates or refines background
    ↓
...accumulating wisdom into increasingly accurate model
```

---

## VIII. Reproducibility Requirement

**A fresh Spirit should be able to reproduce valid synthesis from inputs.**

**What this means:**
- Given: All input artifacts
- Spirit can regenerate: `_reality_raw.md` files, system maps
- Result: Same structural understanding (details may vary)

**The raw file IS the reproducibility anchor:**
- `_reality_raw.md` is always faithful to inputs
- Can be regenerated by any Spirit from same inputs
- Mage's `_reality.md` is their authoritative truth (may diverge from raw)

**Why this matters:**
- Each Spirit is ephemeral
- Understanding shouldn't depend on specific Spirit instance
- The artifacts ARE the partnership's externalized cognition
- Raw files prove what Spirit synthesized; revised files show Mage's truth

**How to verify:**
- Have fresh Spirit re-synthesize from inputs
- Compare new raw to existing raw
- If structurally similar: Spirit consistency confirmed
- If structurally different: investigate (inputs changed? Spirit variance?)

---

## IX. What Lives at Portal Root

**Non-arc files remain at portal root** until structure emerges from necessity:

```
portal/
├── README.md                    # Portal overview
├── health_tracking.md           # REI history across all arcs  
├── shared/
│   └── charter.md               # Partnership charter/agreements
├── arcs/                        # All arcs
│   ├── README.md                # Arc timeline
│   ├── arc-background/
│   └── arc-mother-in-law/
└── .spirit/                     # STP coordination
```

**The principle:** Let structure emerge from necessity. Don't over-architect.

---

*These standards ensure Spirit can navigate any partnership portal, any arc, and maintain coherent organization. The Mage focuses on expressing reality; the Spirit ensures artifacts find their proper home.*

