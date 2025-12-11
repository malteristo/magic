# On Partnership Model Synthesis

**Status:** Active  
**Domain:** Partnership Practice Methodology  
**Purpose:** Define the qualitative research methodology for building shared partnership models

This scroll establishes the methodology for synthesizing a shared partnership model from accumulated arc data. The approach draws on qualitative research methods—specifically Grounded Theory, Pattern Matching, and triangulation through independent observation.

---

## I. The Core Purpose

**Partnership practice builds foundational resonance between Mages through a shared model.**

The shared model is:
- A mutually agreed representation of the partnership's reality
- The foundation from which both Mages can act and expect the other to act
- The basis for trust built through repeated actions in accordance with the model
- The source from which derivatives (Rosetta Stone, protocols) can be generated

**Making both resonance and dissonance explicit:**
- **Resonance** = the shared model (where we see alike)
- **Dissonance** = the divergence map (where we see differently)

Both are valuable. Dissonance is signal, not error.

---

## II. Partnership Practice as Qualitative Research

**Partnership practice IS mixed-methods research on your own relationship.**

| Partnership Practice | Qualitative Research |
|---------------------|---------------------|
| Reality document | Primary data (interview transcript) |
| Spirit synthesis | Analyst coding/theorizing |
| Partner verification ("resonance check") | **Member checking** / Grounded Theory "fit" |
| Dual-Spirit synthesis | **Inter-rater reliability** / Triangulation |
| Shared model | Grounded Theory |
| New arc data | Additional data collection |
| Model verification | Pattern Matching (deductive) |

---

## III. The Three Methodological Frames

### Grounded Theory (Inductive)

**Building theory from data.**

Each Spirit builds a model FROM the data (reality documents, reactions, artifacts). The model must "fit"—meaning it faithfully represents the lived reality of the participants.

**Key principle:** The model emerges from the data, not imposed onto it.

**Partner verification = member checking:** "Does this reflect my reality?"

### Pattern Matching (Deductive)

**Testing theory against new data.**

Once a model exists, new data (from new arcs, living arc additions) is compared against it:
- **FIT** → Model validated, no change needed
- **PARTIAL FIT** → Model needs extension (new pattern discovered)
- **MISFIT** → Model requires transformation (fundamental revision)

**This enables iterative refinement** as partnership evolves.

### Triangulation (Dual-Spirit Synthesis)

**Independent observers increase validity.**

When two Spirits independently analyze the same data and converge on the same patterns, confidence increases. Where they diverge, examination is required.

- **Convergence** = validated pattern (both Spirits see it)
- **Divergence** = requires examination (what is one seeing that the other isn't?)

The divergence IS information about what's being missed.

---

## IV. Canonical Input Artifacts

**What sources should be used for model synthesis:**

### The Key Input: Reality Documents

**Reality documents are the primary input for model synthesis.**

Each arc produces reality documents through within-arc synthesis:
- Raw input artifacts → Spirit synthesis → Partner verification → Reality document
- The reality document IS the verified, internally consistent representation of that partner's reality

```
arcs/arc-{name}/reality_representations/{partner}_reality.md   # THE key input
```

### Primary Sources (MUST be read)

```
arcs/arc-{name}/reality_representations/{partner}_reality.md  # Verified reality per partner
arcs/arc-{name}/stage-2_witnessing/{partner}/                 # Reactions to partner's reality
shared/divergence_map.md                                       # Partnership-level divergences
shared/bridging_statements/                                    # Mutual acknowledgments
shared/neurotype_context.md                                    # Cognitive architecture context
```

### Supporting Sources (MAY inform model)

```
arcs/arc-{name}/stage-1_input/{partner}/           # Raw input (if context needed)
arcs/arc-{name}/stage-3_closing/                   # Arc learnings (if partner closed)
living/input/                                       # Ongoing contributions (if exists)
shared/charter.md                                   # Partnership agreements
health_tracking.md                                  # REI history
```

### EXCLUDED from Initial Model Generation

```
shared/partnership_model_*.md                       # Other Spirit's model
```

**Critical:** Each Spirit generates their model BEFORE reading the other Spirit's model. Comparison happens after independent generation.

---

## V. The Dual-Spirit Synthesis Protocol

### Phase 1: Independent Model Generation

```
Spirit A (Partner A's workshop):
├── Reads canonical inputs from shared space
├── Generates Model A
└── Does NOT read Spirit B's model

Spirit B (Partner B's workshop):
├── Reads canonical inputs from shared space
├── Generates Model B
└── Does NOT read Spirit A's model
```

**Both models are generated independently from the same source data.**

### Phase 2: Model Comparison

```
Either Spirit (or both):
├── Both models placed in shared space
├── Systematic comparison performed
├── Identify: Convergences vs. Divergences
└── Generate: Comparison artifact
```

**The comparison artifact documents:**
- Where the models agree (validated patterns)
- Where they disagree (requires examination)
- What each Spirit saw that the other missed
- Proposed resolution for divergences

### Phase 3: Partner Verification

```
Each partner:
├── Reviews their representation in BOTH models
├── Performs resonance check: "Does this reflect my reality?"
├── Provides corrections where needed
└── Corrections fed back into synthesis
```

**Both partners must verify resonance** before model becomes "shared."

### Phase 4: Shared Model Emergence

```
From comparison + verification:
├── Convergent elements form foundation
├── Divergent elements resolved through dialogue
├── Partners decide which framing serves
└── v1.0 established when both assent
```

**Version control:** Each major revision increments version number.

---

## VI. Model Structure

**The shared partnership model contains:**

### I. The Nodes
- Each partner's cognitive architecture
- Each partner's history, wounds, needs, strengths
- Each partner's position in the system
- External nodes (children, family, work)

### II. The Dynamics
- Communication patterns (how information flows)
- Feedback loops (positive and negative)
- Complementary patterns (where strengths balance)
- Friction patterns (known triggers, recurring conflicts)

### III. The Background State
- Normal functioning (what "normal" looks like)
- Stress indicators (early warning signs)
- Repair patterns (how ruptures heal)

### IV. Named Patterns
- Patterns both partners can reference by name
- Each pattern includes: description, manifestation, triggers, what helps

### V. Agreements & Protocols
- Explicit agreements
- Implicit understandings
- Working protocols

### VI. System Summary
- What this system does well
- Where this system struggles
- What the system needs

### VII. Resonance Verification
- Each partner's verification statement
- Date and resonance level

---

## VII. Iterative Refinement

**The model evolves as new data arrives.**

### When New Arc Closes

1. **Compare** new arc data against existing model
2. **Assess fit:**
   - FIT → Model validated
   - PARTIAL FIT → Extend model (add new pattern)
   - MISFIT → Transform model (fundamental revision)
3. **If extension or transformation needed:**
   - Re-run dual-Spirit synthesis on new data
   - Compare to existing model
   - Integrate changes with version increment

### When Living Arc Accumulates Significant Material

Same process—compare new input against model, assess fit, extend or transform.

### Model Version History

```markdown
| Version | Date | Changes | Both Assented |
|---------|------|---------|---------------|
| 0.1 | YYYY-MM-DD | Initial draft | No (awaiting verification) |
| 1.0 | YYYY-MM-DD | First shared version | Yes |
| 1.1 | YYYY-MM-DD | Extended with Pattern X | Yes |
| 2.0 | YYYY-MM-DD | Transformed after Arc Y | Yes |
```

---

## VIII. Derivatives from the Model

**The shared model is the foundation from which practical tools are derived:**

### Rosetta Stone
- Translation artifact for cognitive style bridging
- Extracted from model's node descriptions + communication patterns
- **See:** `lore/practice/on_the_rosetta_stone.md`

### Protocols
- Working agreements derived from model's friction patterns
- What to do when known patterns activate

### Experiments
- Interventions designed based on model's system analysis
- What modifications might shift identified dynamics

**All derivatives reference the model.** When model updates, derivatives may need updating.

---

## IX. Quality Criteria

**What makes a good shared model:**

### Grounded Theory "Fit"
- Does each partner recognize their reality in the model?
- Does the model use their language and framing?
- Did it emerge from the data (not imposed)?

### Pattern Matching Validity
- Does the model explain observed data?
- Can it predict how partners will experience future situations?
- Does new data fit or require revision?

### Triangulation Strength
- Did independent Spirits converge on same patterns?
- Where divergence existed, was it examined and resolved?

### Partner Resonance
- Both partners have verified HIGH resonance
- Corrections have been integrated
- Model feels "true" to lived experience

---

## X. Connection to Alliance Pattern

**This methodology lays the foundation for the Alliance pattern.**

When Mages share a verified model of their partnership reality:
- They can act in accordance with the model
- They can expect others to act in accordance
- Repeated aligned action builds trust
- Trust enables deeper collaboration

**The shared model is the contract.** Not a legal document, but a living understanding that grounds coordinated action.

---

## XI. Applicability Beyond Romantic Partnership

**This methodology applies to all one-to-one and one-to-many partnership relations:**

- Romantic partnerships (with `romantic-partnership` bundle)
- Professional partnerships
- Creative collaborations
- Alliance between Mages
- Any relationship requiring shared understanding

**The tome provides universal ritual structure.** Domain-specific wisdom comes from resonance bundles.

---

*Partnership practice is qualitative research on your own relationship. The shared model is a grounded theory. Both Spirits are independent analysts. Partner verification is member checking. Dual-Spirit comparison is triangulation. This is rigorous methodology applied to the most important systems in your life.*
