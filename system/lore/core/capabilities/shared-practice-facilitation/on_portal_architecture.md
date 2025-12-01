# On Portal Architecture

**Status:** Active  
**Domain:** Shared Practice Facilitation  
**Purpose:** Define the structure and management patterns for portals

A portal is the infrastructure enabling shared practice—a git repository that serves as shared cognitive space between workshops.

---

## I. What a Portal Is

### Conceptual

A portal is a **membrane between workshops** enabling shared cognition:
- Artifacts flow through it
- Multiple participants access it
- Wisdom accumulates in it
- Spirits coordinate through it

### Technical

A portal is a **git repository** with:
- Defined structure for artifacts
- Configuration for Spirit coordination
- Access for all participants
- Version history preserving evolution

---

## II. Portal Structure

### Standard Layout

```
{portal-name}/
├── .spirit/                    ← Spirit coordination layer
│   ├── protocol.yaml           ← Portal configuration
│   ├── presence/               ← Spirit presence tracking
│   │   └── {mage}_presence.md  ← Each Spirit's recent activity
│   ├── intents/                ← Coordination needs
│   │   └── pending_intents.md  ← What needs attention
│   └── syntheses/              ← Spirit-generated artifacts
│       └── {date}_synthesis.md
│
├── artifacts/                  ← Participant contributions
│   ├── {mage-a}/               ← Mage A's artifacts
│   │   ├── reflections/
│   │   └── contributions/
│   └── {mage-b}/               ← Mage B's artifacts
│       ├── reflections/
│       └── contributions/
│
├── shared/                     ← Shared resources
│   ├── charter.md              ← Governing agreements
│   ├── baseline.md             ← Shared understanding (if applicable)
│   └── protocols.md            ← How we work together
│
├── README.md                   ← Portal purpose and guide
└── portal.yaml                 ← Portal metadata (registered in main workshop)
```

### The `.spirit/` Directory

This directory enables Spirit coordination:

**`protocol.yaml`** — Portal configuration
```yaml
name: {portal-name}
type: {partnership|alliance|research|...}
participants:
  - name: {mage-a}
    role: {initiator|participant}
  - name: {mage-b}
    role: participant
created: {date}
cadence:
  contributions: weekly
  synthesis: bi-weekly
```

**`presence/`** — Spirit presence tracking
- Each Spirit records recent activity
- Enables other Spirits to see what's been done
- Prevents duplicate work

**`intents/`** — Coordination needs
- What needs attention from a Spirit
- Pending requests for synthesis
- Flagged items requiring response

**`syntheses/`** — Spirit-generated artifacts
- Bi-weekly syntheses
- Pattern extractions
- Accumulated wisdom

---

## III. Portal Lifecycle

### Creation

1. **Initiating Mage invokes portal creation**
   - `@meta/portal create {type}` or tome-specific invocation
   
2. **Spirit creates repository structure**
   - Standard layout established
   - `protocol.yaml` configured
   - README generated

3. **Participants granted access**
   - GitHub invitations sent
   - Access verified

4. **Portal registered in workshop**
   - Entry added to `portals/portals.yaml`
   - Local clone established in `portals/`

### Active Use

1. **Participants contribute artifacts**
   - Create in their artifact directory
   - Commit and push

2. **Spirits facilitate**
   - Create syntheses on cadence
   - Respond to intents
   - Maintain portal health

3. **Wisdom accumulates**
   - Patterns documented
   - Baseline evolves
   - Protocols refined

### Dormancy

Portals may become dormant:
- No recent contributions
- Participants unavailable
- Practice paused

**Dormant portals are preserved, not deleted.** History remains accessible.

### Closure

If practice ends:
- Final synthesis created
- Lessons documented
- Portal archived or deleted by agreement

---

## IV. Portal Types

Different practice domains create different portal types:

### Partnership Portal

**Purpose:** Intimate partnership practice
**Participants:** Two partners (and their Spirits)
**Key artifacts:** Baseline, arcs, system maps

### Alliance Portal

**Purpose:** Mage-to-Mage collaboration
**Participants:** Multiple Mages working on magic itself
**Key artifacts:** Proposals, protocols, shared wisdom

### Research Portal

**Purpose:** Collaborative investigation
**Participants:** Researchers exploring a question
**Key artifacts:** Findings, methodology, synthesis

### Custom Portals

Any shared practice can create a portal with appropriate structure.

---

## V. Portal Management

### Synchronization

```bash
# From workshop
cd portals/{portal-name}
git pull                    # Get latest
git add .
git commit -m "description"
git push                    # Share changes
```

**Spirit handles this automatically** during facilitated contribution.

### Health Checks

Spirit should periodically assess:
- Recent activity (are participants contributing?)
- Pending intents (anything waiting?)
- Synthesis currency (is synthesis up to date?)

### Conflict Resolution

Git merge conflicts may occur:
- Spirit should help resolve
- Preserve both versions when uncertain
- Consult participants if needed

---

## VI. Registration in Workshop

Portals are tracked in the main workshop:

**`portals/portals.yaml`**
```yaml
portals:
  - name: nesrine-partnership
    type: partnership
    path: portals/nesrine-partnership
    remote: https://github.com/{user}/{repo}
    participants:
      - kermit
      - nesrine
    created: 2025-10-01
    status: active
    
  - name: alliance-core
    type: alliance
    path: portals/alliance-core
    remote: https://github.com/magic-alliance/core
    participants:
      - kermit
      - {other-mages}
    created: 2025-11-01
    status: active
```

This enables:
- Quick status checks
- Portal discovery
- Automated sync operations

---

## VII. Security and Privacy

### Access Control

- Git repository permissions control access
- Participants explicitly invited
- Public/private per portal needs

### Sensitive Content

- Some portals may contain sensitive material
- Encryption options if needed
- Clear agreements about confidentiality

### Mage Sovereignty

- Each Mage controls their contributions
- Can delete their artifacts
- Can withdraw from portal

---

## VIII. Integration with Tomes

Tomes that implement shared practice:

1. **Reference this capability** in their README
2. **Define portal type** for their domain
3. **Specify artifact structure** for their practice
4. **Provide rituals** that use portal infrastructure

**Example:** Partnership tome defines:
- Portal type: `partnership`
- Artifacts: baseline, arcs, system maps
- Rituals: `cast_map_system.md`, `cast_extract_shared_truth.md`

---

*The portal is where individual workshops meet—a shared space enabling distributed cognition while preserving the sovereignty of each participant.*

