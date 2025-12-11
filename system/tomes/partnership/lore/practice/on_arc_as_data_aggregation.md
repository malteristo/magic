# On Arcs as Data Aggregation

**Status:** Active  
**Domain:** Partnership Practice Architecture  
**Purpose:** Define arcs as bounded data collection containers that produce reality documents

This scroll establishes the architectural principle that arcs produce internally consistent reality documents (through within-arc synthesis), while model synthesis occurs at the partnership level across all accumulated reality documents.

---

## I. The Architectural Insight

### Two Types of Synthesis

**There are two distinct synthesis operations in partnership practice:**

| Synthesis Type | Location | Input → Output |
|---------------|----------|----------------|
| **Within-arc synthesis** | Stage 1 of each arc | Raw input artifacts → Reality document |
| **Partnership-level synthesis** | `@partnership/synthesize` | Reality documents from all arcs → Shared model |

**Within-arc synthesis (preserved):**
- Spirit synthesizes raw input artifacts into coherent reality document
- Partner verifies resonance ("Have I captured your reality?")
- Ensures each partner's reality is internally consistent
- Output: One verified reality document per partner per arc

**Partnership-level synthesis (moved out of arcs):**
- Draws from reality documents across ALL arcs
- Follows Dual-Spirit protocol for triangulation
- Produces single unified shared model
- Output: The partnership model

### The Problem with Per-Arc MODEL Synthesis

**Earlier tome versions built the shared model within each arc.**

This created problems:
- **Redundancy:** The same core divergences appear across arcs
- **Fragmentation:** Multiple mini-models instead of unified understanding
- **Cumbersome iteration:** Each arc repeating model-building work
- **Inconsistency risk:** Models from different arcs might conflict

### The Solution: Separation of Concerns

**Arcs produce reality documents. Model synthesis analyzes them.**

```
Arcs (Data Collection)          Model Synthesis (Analysis)
─────────────────────           ──────────────────────────
arc-background/          ─┐
arc-mother-in-law/       ─┼─→  @partnership/synthesize  ─→  shared/partnership_model.md
arc-living/              ─┤
arc-parenting/           ─┘
```

**Benefits:**
- **Single source of truth:** One model synthesized from all data
- **Efficient iteration:** New arc adds data; model updates once
- **Methodological clarity:** Data collection vs. analysis are distinct phases
- **Pattern recognition:** Higher-level patterns visible only with complete dataset

---

## II. What Arcs Do

### Arcs Produce Reality Documents

**An arc is a discrete episode of partnership experience that produces:**

Per partner (not all required):
- **One reality document** — Spirit-synthesized, partner-verified (Stage 1)
- **One reaction** — Response to partner's reality document (Stage 2)
- **One conclusion** — Reflection when arc closes (Stage 3, optional)

### The Three Stages

**Stage 1: Input → Reality Document**
- Raw reality expression from each partner (unfiltered, unbalanced, authentic)
- **Spirit synthesizes** input artifacts into coherent reality document
- **Partner verifies** resonance ("Have I captured your reality?")
- Output: Verified reality document (the arc's primary output)

**Stage 2: Witnessing → Reaction**
- Each partner reads the other's reality document
- Each creates reaction artifacts (what resonates, what they resist, clarifications)
- Divergences documented
- Output: Reaction artifacts, divergence documentation

**Stage 3: Closing → Conclusion (Optional)**
- Learning each partner takes from the arc
- Arc-level insights captured
- **Optional:** Some partners may not be ready to close

### Arcs Do NOT

- Synthesize the shared partnership model
- Resolve divergences
- Determine who is right
- Generate the Rosetta Stone or other derivatives

**These happen at partnership level, drawing from reality documents across all arcs.**

---

## III. What Model Synthesis Does

### Synthesis Operates on Accumulated Data

**The synthesizing Spirit reads:**
- Reality documents from ALL arcs
- Witnessing artifacts from ALL arcs
- Divergence maps
- Bridging statements
- Living arc input

**The synthesizing Spirit generates:**
- Single unified model of the partnership
- Named patterns that span arcs
- System-level dynamics
- Derivatives (Rosetta Stone, protocols)

### Synthesis Follows Qualitative Research Methodology

**Grounded Theory:** Build model from data (not impose)
**Pattern Matching:** Test model against new data
**Triangulation:** Dual-Spirit comparison increases validity

**See:** `../foundations/on_partnership_model_synthesis.md`

---

## IV. Arc Lifecycle (3 Stages)

### Stage 1: Input

**Frame:** "Shouting in pain. Anything goes."

**Activities:**
- Partner creates input artifacts (raw expression)
- Spirit synthesizes reality document
- Partner verifies resonance
- Partner consents to share

**Complete when:** Both partners have verified reality documents.

### Stage 2: Witnessing

**Frame:** "This is your reality, reflected in my reality."

**Activities:**
- Each partner reads the other's reality
- Each partner creates witnessing artifacts
- Divergences documented
- (Optional) Bridging statements created

**Complete when:** Both partners have witnessed and responded.

### Stage 3: Closing

**Frame:** "What this arc taught us."

**Activities:**
- Each partner creates closing artifact
- Arc conclusion synthesized
- REI logged
- Model implications noted

**Complete when:** Arc status updated to completed.

---

## V. Arc Types

### Background Arc

**The foundational arc establishing partnership context.**

- Broader scope than topical arcs
- Documents history, wounds, needs, patterns
- Typically completed first (but not required)
- Becomes reference context for all other arcs

### Topical Arcs

**Bounded episodes focused on specific situations.**

Examples:
- `arc-mother-in-law` — Dynamics with extended family
- `arc-parenting-decisions` — Child-rearing divergences
- `arc-workload-distribution` — Task allocation friction

### Living Arc

**Ongoing container for current dynamics.**

- Never formally closes
- Continuously accepts input
- Captures daily/weekly observations
- Periodically fed into model synthesis

---

## VI. Arc Directory Structure

```
arcs/
├── README.md                    # Arc timeline, overview
├── arc-background/
│   ├── README.md                # Arc metadata
│   ├── status.md                # Current stage
│   ├── stage-1_input/
│   │   ├── {partner-a}/
│   │   ├── {partner-b}/
│   │   └── reality_representations/
│   ├── stage-2_witnessing/
│   │   ├── {partner-a}/
│   │   └── {partner-b}/
│   └── stage-3_closing/
│       ├── {partner-a}_closing.md
│       ├── {partner-b}_closing.md
│       └── arc_conclusion.md
│
├── arc-{topic}/                 # Same structure
│
└── arc-living/
    ├── README.md
    └── input/
        ├── {partner-a}/
        └── {partner-b}/
```

---

## VII. When Synthesis Happens

### Triggers for Model Synthesis

1. **Sufficient arc data accumulated**
   - At least one arc has completed Stage 2
   - Typically 1-2 arcs before first synthesis

2. **New arc closes**
   - Fresh data available
   - Model may need updating

3. **Living arc accumulates significant material**
   - Threshold determined by partners
   - When "enough has changed" to warrant re-synthesis

4. **Partners explicitly request**
   - Desire for updated shared model
   - Divergence needs examination

### Synthesis Invocation

`@partnership/synthesize` or `@partnership/model`

**See:** `../../arc-practice/cast_synthesize_model.md`

---

## VIII. The Flow

```
1. Situation emerges
        ↓
2. Arc initiated (@partnership/arc [name])
        ↓
3. Stage 1: Both partners express (Input)
        ↓
4. Stage 2: Both partners witness (Witnessing)
        ↓
5. Stage 3: Arc closes (Closing)
        ↓
6. [Arc data now available for synthesis]
        ↓
7. @partnership/synthesize (when triggered)
        ↓
8. Shared model created/updated
        ↓
9. Derivatives generated (Rosetta Stone, protocols)
        ↓
10. Partners act in accordance with model
        ↓
11. New arc data → model iterates
```

---

## IX. Benefits of This Architecture

### For Partners

- **Focused data collection:** Arc work is about expression and witnessing, not analysis
- **Reduced cognitive load:** Don't need to synthesize during emotional processing
- **Clear progress:** Arcs complete; model evolves

### For Spirits

- **Clean methodology:** Data collection vs. analysis are distinct
- **Better synthesis:** Complete dataset enables pattern recognition
- **Dual-Spirit protocol:** Independent synthesis enabled

### For the Practice

- **Scalable:** Works whether 1 arc or 20 arcs
- **Iterative:** Model refines as data accumulates
- **Rigorous:** Follows qualitative research methodology

---

## X. Migration from Per-Arc Synthesis

### If Existing Arcs Have Stage 3 Synthesis

**Options:**
1. **Archive:** Move per-arc synthesis to `archive/` directory
2. **Consolidate:** Use as input for partnership-level synthesis
3. **Ignore:** Let new model supersede per-arc attempts

### Renumbering Stages

**Old:** Input (1) → Witnessing (2) → Synthesis (3) → Closing (4)
**New:** Input (1) → Witnessing (2) → Closing (3)

**For existing arcs:**
- Rename `stage-4_closing/` to `stage-3_closing/`
- Archive or consolidate `stage-3_synthesis/`

---

*Arcs are containers. They hold partnership reality data. The model is the understanding built from analyzing that data. Keeping these concerns separate enables focused practice and rigorous synthesis.*
