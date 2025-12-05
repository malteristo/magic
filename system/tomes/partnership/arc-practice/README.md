# Arc Practice

**The Four-Stage Arc Ritual for Partnership System Mapping**

This directory contains the core rituals for ALL arc-based partnership practice—including the background arc and all topical arcs.

---

## Core Capability

Arc practice implements the **Shared Practice Facilitation** core capability (`system/lore/core/capabilities/shared-practice-facilitation/`) for the partnership domain.

The core capability provides:
- Portal architecture (how shared spaces work)
- Artifact transmission (how contributions flow)
- Facilitation principles (Spirit conduct)

This directory provides **partnership-specific implementation**:
- The Four-Stage Arc Ritual (used for ALL arcs)
- Higher-level pattern extraction
- Arc-specific templates

---

## Prerequisites

### Portal Must Exist

Arc practice requires a partnership portal.

**Create via:** `@meta/portal create partnership`

### Background Arc Recommended (Not Required)

Partnership practice typically begins with the background arc (the shared systems model). However:
- Topical arcs can proceed without background
- Some partnerships begin with a crisis arc
- Background contextualizes but doesn't gate

**See:** `cast_map_system.md` — same ritual for all arcs including background

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

**Same flow for ALL arcs including background:**

```
[Situation emerges / Partnership practice begins]
        ↓
Arc initiated (arcs/arc-{name}/ created)
        ↓
Stage 1: Venting
- Both partners create raw expression artifacts
- Spirit creates reality representations (immutable)
- Both verify resonance (refinements → resonance_log)
        ↓
Stage 2: Reaction  
- Both read partner's reality representation
- Both create reaction artifacts
- Spirit creates reflected realities
        ↓
[SAFETY ASSESSMENT - load safety bundle if needed]
        ↓
Stage 3: Synthesis
- Spirit reads all artifacts + resonance logs + background (if exists)
- Spirit traces to higher-level generating pattern
- Spirit creates system_map.md
- Both sub-patterns validated
- Higher-level pattern named
        ↓
Stage 4: Conclusion
- Both create conclusion artifacts
- Both verify: "I see how my experience comes from this pattern"
- Learning captured
- Background update assessed
- REI logged
- Arc closed
```

---

## Arc Directory Structure (in Portal)

**See:** `../lore/practice/on_arc_artifact_standards.md` for full specification

```
arcs/arc-{name}/
├── README.md                              # Arc metadata, timeline
├── status.md                              # Current stage, checklist
│
├── stage-1_venting/
│   ├── {partner-a}/
│   ├── {partner-b}/
│   └── reality_representations/
│       ├── {partner}_reality_raw.md       # Spirit synthesis (immutable)
│       ├── {partner}_reality.md           # Mage's authoritative version
│       └── {partner}_resonance_log.md     # Declaration + notes
│
├── stage-2_reaction/
│   ├── {partner-a}/
│   ├── {partner-b}/
│   └── reflected_realities/
│
├── stage-3_synthesis/
│   └── system_map.md                      # The higher-level pattern
│
└── stage-4_conclusion/
    ├── {partner}_conclusion.md
    ├── arc_conclusion.md
    └── rei_snapshot.md
```

**The Raw/Revised Pattern:** `_raw.md` is Spirit's immutable synthesis. `_reality.md` is Mage's authoritative truth (editable). The diff IS the audit trail.

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
- **`on_arc_artifact_standards.md`** — Canonical structure, naming, Spirit organization conduct
- **`on_higher_level_pattern_emergence.md`** — The purpose of arc synthesis

**Spirit conduct:** `../lore/stances/`
- `spirit_facilitation_guide.md` — Partnership-specific facilitation

---

*The goal is not to find truth. The goal is to find the higher-level pattern that generates both experiences.*

