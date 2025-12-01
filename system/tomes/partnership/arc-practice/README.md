# Arc Practice

**The Four-Stage Arc Ritual for Partnership System Mapping**

This directory contains the core rituals for arc-based partnership practice—processing specific situations through systematic system mapping.

---

## Core Capability

Arc practice implements the **Shared Practice Facilitation** core capability (`system/lore/core/capabilities/shared-practice-facilitation/`) for the partnership domain.

The core capability provides:
- Portal architecture (how shared spaces work)
- Artifact transmission (how contributions flow)
- Facilitation principles (Spirit conduct)

This directory provides **partnership-specific implementation**:
- The Four-Stage Arc Ritual
- Shared truth extraction
- Arc-specific templates

---

## Prerequisites

### Baseline Must Exist

Before arc work can be properly contextualized, partners need a shared systems model.

**See:** `../baseline/cast_establish_baseline.md`

### Portal Must Exist

Arc practice requires a partnership portal.

**Create via:** `@meta/portal create partnership`

### Safety Bundle for High-Stakes Work

Before system mapping involving conflict, power imbalances, or clinical patterns:

**Load:** `library/resonance/safety/` bundle

---

## The Rituals

| Ritual | Purpose |
|--------|---------|
| `cast_map_system.md` | **Core ritual.** Four-Stage Arc: Venting → Reaction → System Mapping → Conclusion |
| `cast_extract_shared_truth.md` | Cylinder extraction—finding the pattern that makes both perspectives valid |
| `cast_facilitate.md` | Operational orchestration—portal detection, contribution, synthesis coordination |

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
[SAFETY ASSESSMENT - load safety bundle if needed]
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

## Arc Directory Structure (in Portal)

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

## Templates

Arc-specific templates for various artifact types:

| Template | Purpose |
|----------|---------|
| `cognitive_architecture_template.md` | Partner cognitive profile |
| `conversation_thread_template.md` | Threaded dialogue structure |
| `practice_log_template.md` | Session logging |
| `protocols_template.md` | Agreed protocols |
| `synthesis_template.md` | Bi-weekly synthesis structure |
| `weekly_reflection_template.md` | Individual reflection |

---

## Related Lore

**Practice lore:** `../lore/practice/`
- `on_arc_structure.md` — How arcs provide bounded episodes
- `on_shared_truth_finding.md` — Philosophy of finding shared truth
- `on_dual_spirit_synthesis.md` — Validation through independent observers
- `on_artifact_transmission.md` — Partnership-specific transmission patterns

**Spirit conduct:** `../lore/stances/`
- `spirit_facilitation_guide.md` — Partnership-specific facilitation

---

*The goal is not to find truth. The goal is to understand the system.*

