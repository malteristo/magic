# On Shared Practice Facilitation

**Status:** Active — Core Capability  
**Domain:** Distributed Cognition Beyond the Workshop

This capability extends the distributed cognition pattern beyond the individual workshop, enabling multiple Mages (and their Spirits) to participate in shared cognitive work.

---

## I. The Pattern

### Distributed Cognition at Multiple Scales

Magic is distributed cognition. The Mage's cognitive capabilities are augmented through partnership:

```
Scale 1: Mage + Spirit (within workshop)
         └─ Individual practice, single cognitive ecosystem

Scale 2: Mage + Spirit + Other Mages (via portals)
         └─ Shared practice, expanded cognitive ecosystem

Scale 3: Alliance of Mages (multiple portals, coordinated practice)
         └─ Collective practice, networked cognitive ecosystem
```

**The same pattern applies at each scale.** What Spirit provides within the workshop, shared practice provides across workshops.

### The Augmentation

| Within Workshop | Across Workshops |
|-----------------|------------------|
| Spirit augments Mage's cognition | Other Mages augment each other's cognition |
| Workshop contains practice artifacts | Portal contains shared artifacts |
| Spirit maintains context across sessions | Portal maintains context across participants |
| Mage-Spirit resonance | Multi-Mage resonance |

---

## II. The Core Concept: Portal

A **portal** is a shared cognitive space where multiple Mages can practice together.

**Technically:** A git repository accessible to all participants
**Conceptually:** A membrane between workshops enabling shared cognition

### What Portals Enable

- **Shared artifacts** — Documents, syntheses, reflections accessible to all
- **Coordinated practice** — Rituals that span multiple workshops
- **Spirit coordination** — Multiple Spirits serving the same shared space
- **Accumulated wisdom** — Learning that persists across all participants

### Portal Architecture

```
portal/
├── .spirit/                    ← Spirit coordination layer
│   ├── protocol.yaml           ← Portal configuration
│   ├── presence/               ← Spirit presence tracking
│   └── syntheses/              ← Spirit-generated artifacts
│
├── artifacts/                  ← Participant contributions
│   ├── {mage-a}/
│   └── {mage-b}/
│
├── shared/                     ← Shared resources
│   ├── charter.md              ← Agreements governing the portal
│   └── ...
│
└── README.md                   ← Portal purpose and structure
```

**See:** `on_portal_architecture.md` for detailed patterns

---

## III. Artifact Transmission

Artifacts flow between individual workshops and shared portals:

```
Mage A's Workshop          Portal           Mage B's Workshop
       │                     │                     │
       │    contribute       │     retrieve        │
       ├────────────────────►│◄────────────────────┤
       │                     │                     │
       │     retrieve        │    contribute       │
       ◄─────────────────────┤─────────────────────►
```

**Transmission patterns:**
- **Contribute** — Move artifact from workshop to portal
- **Retrieve** — Copy artifact from portal to workshop
- **Sync** — Bidirectional update

**See:** `on_artifact_transmission.md` for protocols

---

## IV. Spirit Facilitation

When multiple Mages practice together, Spirits serve the shared space:

### Single-Spirit Facilitation

One Spirit (typically the initiating Mage's) facilitates for all participants:
- Creates syntheses incorporating all perspectives
- Maintains portal infrastructure
- Coordinates asynchronous contributions

### Multi-Spirit Coordination

Multiple Spirits serve the same portal:
- Each Spirit serves their Mage's contributions
- Spirits coordinate through portal artifacts (not direct communication)
- Synthesis may involve independent extraction then comparison

**See:** `on_facilitation_principles.md` for Spirit conduct

---

## V. How Tomes Use This Capability

This capability defines the PATTERN. Tomes implement concretely:

### Partnership Tome

Uses shared practice facilitation for:
- Baseline establishment (both partners contribute)
- Arc-based system mapping (Four-Stage Ritual)
- Dual-Spirit synthesis (validation through independent observers)

**Implementation:** `system/tomes/partnership/rituals/`

### Future Tomes

Other tomes can implement shared practice for their domains:
- **Alliance tome** — Mage-to-Mage collaboration on magic itself
- **Research tome** — Collaborative investigation
- **Craft tome** — Shared creative projects

Each implements the portal pattern with domain-specific rituals.

---

## VI. Key Principles

### 1. Sovereignty Preserved

Shared practice does not diminish individual sovereignty. Each Mage:
- Controls their contributions
- Maintains their workshop independently
- Can withdraw from shared practice

The portal is ADDITION to individual practice, not replacement.

### 2. Artifacts as Interface

Participants communicate through artifacts, not direct Spirit-to-Spirit contact:
- Artifacts are the "messages" between workshops
- Spirits read and synthesize artifacts
- No real-time Spirit communication required

### 3. Git as Infrastructure

Git provides the technical substrate:
- Version control (history preserved)
- Distributed access (no central server required)
- Merge capabilities (concurrent contributions)
- Familiar to developers (low barrier)

### 4. Flexible Participation

Not all participants need magic practice:
- Some may write directly in portal (no Spirit)
- Some may have Spirits in different environments
- The portal accommodates all modalities

---

## VII. Relationship to Other Capabilities

| Capability | Relationship |
|------------|--------------|
| **Executive Function** | Shared practice requires coordinating across participants |
| **Working Memory** | Portal serves as external memory for the group |
| **Transactive Memory** | Participants know who knows what |
| **Pattern Fidelity** | Shared practice must maintain pattern integrity across participants |

---

## VIII. Contents

| Scroll | Purpose |
|--------|---------|
| `on_portal_architecture.md` | Detailed portal structure and management |
| `on_artifact_transmission.md` | How artifacts move between spaces |
| `on_facilitation_principles.md` | Spirit's role in shared practice |

---

*Shared practice facilitation extends the Mage's cognitive ecosystem beyond the workshop, enabling distributed cognition across multiple participants while preserving individual sovereignty.*

