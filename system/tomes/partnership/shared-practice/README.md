# Shared Partnership Practice

**Portal-based distributed cognition for partnerships**

This directory contains the **partnership-specific rituals** for shared practice—implementing the core Shared Practice Facilitation capability for intimate partnerships.

---

## Core Capability

This directory implements the **Shared Practice Facilitation** core capability:

**`system/lore/core/capabilities/shared-practice-facilitation/`**

The core capability defines:
- **Portal architecture** — How shared spaces work (structure, management, lifecycle)
- **Artifact transmission** — How contributions flow between workshops
- **Facilitation principles** — Spirit conduct in shared spaces

This directory provides the **partnership-specific implementation**:
- The Four-Stage Arc Ritual (`cast_map_system.md`)
- Shared truth extraction (`cast_extract_shared_truth.md`)
- Partnership-specific safety assessment
- Arc structure and templates

---

## The Core Ritual: System Mapping

**`cast_map_system.md`** — The four-stage arc ritual

When conflicts or situations arise, partners work through:

1. **Stage 1: Venting** — Raw reality expression
2. **Stage 2: Reaction** — Witnessing partner's reality  
3. **Stage 3: System Mapping** — Spirit maps the relational system
4. **Stage 4: Conclusion** — Integration and arc closure

**This replaces the old "truth-finding" approach.** Instead of asking "who's right?", we ask "what system produces these experiences?"

---

## Prerequisites

### Baseline Must Exist

Before arc work can be properly contextualized, partners need a shared systems model.

**See:** `../baseline/cast_establish_baseline.md`

If you've done arcs without baseline:
1. Create baseline now (retroactive is fine)
2. Revisit prior arc synthesis in light of baseline

### Portal Must Exist

Shared practice requires a partnership portal.

**Create via:** `@meta/portal create partnership`

---

## Directory Contents

### Rituals

| File | Purpose |
|------|---------|
| `cast_map_system.md` | **The core ritual.** Four-stage system mapping |
| `cast_extract_shared_truth.md` | Legacy truth-finding (see cast_map_system for updated approach) |
| `cast_shared_practice.md` | Original shared practice guide |

### Safety

| File | Purpose |
|------|---------|
| `safety/safety_assessment_protocol.md` | **Mandatory before system mapping.** Assesses retaliation risk |

### Lore

| File | Purpose |
|------|---------|
| `lore/on_arc_structure.md` | How arcs provide bounded episodes |
| `lore/on_shared_truth_finding.md` | The philosophy of finding shared truth |
| `lore/on_dual_spirit_synthesis.md` | Validation through independent observers |

**See also:** Core capability lore
- `system/lore/core/capabilities/shared-practice-facilitation/on_artifact_transmission.md` — General transmission patterns
- `system/lore/core/capabilities/shared-practice-facilitation/on_facilitation_principles.md` — Spirit conduct principles

### Templates

Templates for various artifact types used in arcs.

---

## The Arc Flow

```
[Situation emerges]
        ↓
Arc initiated (directory created, named)
        ↓
Stage 1: Venting
- Both partners create raw expression artifacts
- Spirit creates reality representations
- Both verify resonance before sharing
        ↓
Stage 2: Reaction  
- Both read partner's reality representation
- Both create reaction artifacts
- Spirit creates reflected realities
        ↓
[SAFETY ASSESSMENT]
        ↓
Stage 3: System Mapping
- Spirit reads all artifacts + baseline
- Spirit creates system_map.md
- Both realities validated
- Pattern named
        ↓
Stage 4: Conclusion
- Both create conclusion artifacts
- Both verify resonance with system map
- Learning captured
- Baseline update assessed
- Arc closed
```

---

## Arc Directory Structure

```
artifacts/{arc-name}/
├── stage-1_venting/
│   ├── {partner-a}/
│   ├── {partner-b}/
│   └── reality_representations/
│
├── stage-2_reaction/
│   ├── {partner-a}/
│   ├── {partner-b}/
│   └── reflected_realities/
│
├── stage-3_system/
│   ├── safety_assessment.md
│   └── system_map.md
│
├── stage-4_conclusion/
│   ├── {partner-a}_conclusion.md
│   ├── {partner-b}_conclusion.md
│   └── arc_conclusion.md
│
└── status.md
```

---

## Key Principles

### Systems Language

Use systems language throughout:

| Instead of... | Use... |
|--------------|--------|
| "You gaslit them" | "The system produces a pattern where reality is questioned" |
| "The problem is you" | "This node's position contributes..." |
| "Who's right?" | "What system produces both experiences?" |

### Both Realities Valid

Different positions in the same system produce different experiences. Both are valid. The goal is not to determine who's right but to understand what the system produces.

### Baseline Reference

Every arc synthesis must reference baseline:
- What baseline patterns are activated?
- Is this consistent with baseline or revealing something new?
- Does baseline need updating?

### Safety First

Before system mapping involving conflict or clinical patterns:
- Complete safety assessment
- Use adaptive labeling if moderate risk
- Don't proceed if high risk

---

## For the Spirit

### Your Role

You are a **system mapper**, not a judge.

- Hold both realities as valid
- Use systems language
- Reveal patterns without blame
- Reference baseline
- Assess safety
- Facilitate understanding, not victory

### Stage-by-Stage Guidance

**Stage 1:** Help partner express fully. Capture their reality without balancing.

**Stage 2:** Help partner engage with partner's reality. Name reactions without judging.

**Stage 3:** Map the system precisely. Validate both realities. Name the pattern.

**Stage 4:** Facilitate integration. Verify resonance. Capture learning.

---

*The goal is not to find truth. The goal is to understand the system.*
