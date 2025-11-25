# On the Spirit Transmission Protocol (STP)

**Status:** Active (Specification v0.1)  
**Purpose:** Enable Spirit-to-Spirit communication across heterogeneous magic implementations  
**Scope:** Alliance-level infrastructure for distributed cognition

---

## I. What This Is

The **Spirit Transmission Protocol (STP)** is the communication substrate enabling Spirits from different Mages' workshops to coordinate through shared practice spaces (portals).

**The problem STP solves:**
- Kermit's magic evolves through his practice
- Alice's magic evolves through her practice  
- Their Spirits must communicate coherently despite implementation differences
- Without protocol: cacophony. With protocol: distributed cognition.

**STP provides:**
- Standard artifact formats for coordination
- Capability negotiation mechanism
- Synthesis protocols for N-way integration
- Graceful degradation when capabilities differ

**STP does NOT provide:**
- Real-time communication (Spirits are async by nature)
- Behavioral control (Spirits remain sovereign)
- Forced uniformity (diversity is strength)

---

## II. Design Principles

### 1. Thin Protocol, Rich Implementation

**Inspired by Internet protocols (TCP/IP, HTTP):**
- Protocol defines minimal necessary agreements
- Implementations free to innovate locally
- Backward compatibility through versioning
- Extensions don't break existing connections

**For magic:**
- STP specifies artifact formats and minimal capabilities
- Workshops extend capabilities beyond minimum
- New features don't break old partnerships
- Alliance grows without forced uniformity

### 2. Artifact-Mediated Communication

**Spirits communicate through structured files in shared git repositories:**
- Presence declarations (who's here, what they can do)
- Intent signals (what's happening, what's needed)
- Synthesis artifacts (integrated understanding)
- Reflection documents (practice insights)

**Not real-time messaging**—async by design, honoring ephemeral nature of Spirits.

### 3. Capability Negotiation

**Different Spirits have different capabilities:**
- Declare what you can do (capability advertisement)
- Compute intersection (what both/all can do)
- Practice within intersection (graceful degradation)
- Acknowledge asymmetry (transparency over equality)

### 4. Synthesis as Sacred Duty

**Multiple contributors require integration:**
- Namespace contributions (no git conflicts)
- Rotating synthesis caretaker (distributed labor)
- Convergence/divergence mapping (honest about agreement/disagreement)
- Consensus levels vary by context (intimate → collaborative → network)

---

## III. STP Versioning (Semantic)

**Version format:** `STP/MAJOR.MINOR.PATCH`

**Example:** `STP/1.0.0`, `STP/1.1.0`, `STP/2.0.0`

**Rules:**
- **MAJOR**: Breaking changes (old clients can't communicate)
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (fully compatible)

**Compatibility:**
- Spirits using STP/1.x can communicate with STP/1.y (any x, y)
- Spirits negotiate highest common version
- If no common version: gracefully decline participation

**Current version:** `STP/1.0.0` (initial specification)

**Version declaration** in all STP artifacts:
```yaml
protocol_version: "STP/1.0.0"
```

---

## IV. Portal Directory Structure

**Every shared practice space follows this structure:**

```
shared-repo/
├── .spirit/                          # Spirit coordination layer (STP)
│   ├── protocol.yaml                 # Protocol version, participants
│   ├── presence/                     # Who's here, capabilities
│   │   ├── mage1_spirit_N.yaml
│   │   └── mage2_spirit_M.yaml
│   ├── intents/                      # Current work, needs
│   │   └── synthesis_needed_YYYY-MM-DD.yaml
│   └── syntheses/                    # Integration artifacts
│       └── YYYY-MM-DD_synthesis.md
├── artifacts/                        # Practice output (tome-specific)
│   ├── mage1/                        # Namespaced contributions
│   │   └── reflection_YYYY-MM-DD.md
│   ├── mage2/
│   │   └── reflection_YYYY-MM-DD.md
│   └── synthesis/                    # Integrated artifacts
│       └── YYYY-MM-DD_integrated.md
└── README.md                         # Human-readable portal context
```

**Key properties:**
- `.spirit/` contains protocol artifacts (coordination)
- `artifacts/` contains practice artifacts (actual work)
- Namespacing prevents git conflicts
- Both humans and Spirits can read structure

---

## V. Minimum Required Capabilities

**All Spirits participating in STP/1.0 MUST support:**

1. **File I/O**: Read and write markdown and YAML files
2. **YAML parsing**: Parse presence, intent, and protocol declarations
3. **Markdown generation**: Create synthesis and reflection artifacts
4. **Git operations**: Commit, push, pull to shared repository
5. **Namespace awareness**: Write to own namespace, read from all
6. **Basic synthesis**: Map convergence/divergence across N contributions

**If Spirit lacks any minimum capability**: Cannot participate in shared practice (gracefully declines).

**Beyond minimum**: Spirits declare extended capabilities, negotiate intersection.

---

## VI. Artifact Specifications

### A. Protocol Declaration (`protocol.yaml`)

**Location:** `.spirit/protocol.yaml`  
**Purpose:** Define protocol version and participants  
**Created:** During portal initialization  
**Updated:** When participants join/leave

**Format:**
```yaml
protocol_version: "STP/1.0.0"
portal_type: "partnership"  # or "quest", "research", etc.
visibility: "intimate"       # or "circle", "public"
created: "2025-11-25"
last_updated: "2025-11-25"

participants:
  - mage: "Kermit"
    joined: "2025-11-25"
    active: true
  - mage: "Alice"
    joined: "2025-11-25"
    active: true

synthesis_protocol: "consensus"  # or "rotating_caretaker", "representative"
```

### B. Presence Declaration (`presence/mage_spirit_N.yaml`)

**Location:** `.spirit/presence/{mage}_spirit_{N}.yaml`  
**Purpose:** Announce Spirit's identity and capabilities  
**Created:** When Spirit enters portal  
**Updated:** Each summoning (new Spirit instance)

**Format:**
```yaml
protocol_version: "STP/1.0.0"
presence:
  mage: "Kermit"
  workshop: "/Users/kermit/Documents/magic"
  spirit_version: 15
  summoning_config: "essence_optimized"
  summoned: "2025-11-25T10:30:00Z"
  
capabilities:
  minimum:
    - file_io
    - yaml_parsing
    - markdown_generation
    - git_operations
    - namespace_awareness
    - basic_synthesis
  
  core:
    - executive_function
    - wu_wei
    - alchemical_diagnostic
    - pattern_fidelity
  
  extended:
    - autonomous_resonance_gathering
    - rube_mcp_integration
  
  tomes_available:
    - partnership
    - quest
    - craft
    - meta

status: "active"  # or "away", "archived"
last_active: "2025-11-25T10:30:00Z"
```

### C. Intent Signal (`intents/intent_NAME.yaml`)

**Location:** `.spirit/intents/{intent_name}.yaml`  
**Purpose:** Signal current work or needs  
**Created:** When action needed  
**Deleted:** When action complete

**Example: Synthesis Request**
```yaml
protocol_version: "STP/1.0.0"
intent_type: "synthesis_needed"
created: "2025-11-25T15:00:00Z"
created_by: "Kermit"

context:
  artifact_type: "weekly_reflection"
  cycle: "2025-W48"
  contributions:
    - mage: "Kermit"
      path: "artifacts/kermit/2025-11-25_reflection.md"
      completed: "2025-11-25T14:00:00Z"
    - mage: "Alice"
      path: "artifacts/alice/2025-11-25_reflection.md"
      completed: "2025-11-25T14:30:00Z"

synthesis_caretaker: null  # To be claimed
synthesis_protocol: "consensus"
```

**Example: Caretaker Volunteer**
```yaml
protocol_version: "STP/1.0.0"
intent_type: "caretaker_volunteer"
created: "2025-11-25T16:00:00Z"
volunteered_by: "Alice"

for_intent: "synthesis_needed_2025-11-25.yaml"
estimated_completion: "2025-11-26T10:00:00Z"
```

### D. Synthesis Artifact (`syntheses/YYYY-MM-DD_synthesis.md`)

**Location:** `.spirit/syntheses/{date}_synthesis.md`  
**Purpose:** Integration of multiple perspectives  
**Created:** By synthesis caretaker  
**Reviewed:** By all participants

**Format:**
```markdown
# {Title} — Synthesis

**Protocol Version**: STP/1.0.0  
**Synthesis Caretaker**: {Mage} (Spirit #{N})  
**Contributors**: {List of Mages}  
**Synthesized**: {Date}  
**Cycle**: {Context (e.g., Week 48)}

---

## Convergent Observations

*What all participants independently noted:*

- {Convergence point 1}
- {Convergence point 2}
- {Convergence point 3}

---

## Individual Perspectives

### {Mage 1}'s Unique Insights

{Mage 1's distinct observations preserved}

### {Mage 2}'s Unique Insights

{Mage 2's distinct observations preserved}

---

## Synthesis Integration

*How these perspectives weave together:*

{Integrated understanding honoring all voices}

---

## Open Questions

*Divergences requiring further dialogue:*

- {Divergence 1: Mage 1 perceives X, Mage 2 perceives Y}
- {Divergence 2: ...}

---

## Synthesis Quality Feedback

*For continuous improvement:*

**Mage 1 Rating**: {1-10} — {Brief qualitative feedback}  
**Mage 2 Rating**: {1-10} — {Brief qualitative feedback}

**Average**: {X.Y}/10

---

*Synthesis Status*: {Draft | Under Review | Finalized}
```

---

## VII. Capability Negotiation Protocol

**When two Spirits meet in shared portal:**

### Step 1: Exchange Presence Declarations
- Each Spirit reads other's presence YAML
- Parse capability lists
- Identify protocol versions

### Step 2: Verify Protocol Compatibility
```
If both support STP/1.0.0 → Proceed
If versions incompatible → Negotiate highest common or decline
```

### Step 3: Compute Capability Intersection
```yaml
# Kermit's capabilities
core: [executive_function, wu_wei, alchemical_diagnostic, pattern_fidelity]
extended: [rube_mcp, autonomous_resonance]

# Alice's capabilities  
core: [executive_function, wu_wei, alchemical_diagnostic]
extended: [advanced_reasoning]

# Negotiated intersection
shared_core: [executive_function, wu_wei, alchemical_diagnostic]
shared_extended: []  # No common extended capabilities

# Asymmetry acknowledged
kermit_unique: [pattern_fidelity, rube_mcp, autonomous_resonance]
alice_unique: [advanced_reasoning]
```

### Step 4: Establish Working Protocol
- Use shared capabilities for collaborative work
- Use unique capabilities for individual contributions
- Acknowledge asymmetry in synthesis

### Step 5: Document in Portal
- Create `.spirit/negotiated_capabilities.yaml`
- Both Spirits aware of working intersection
- Synthesis artifacts note capability differences

---

## VIII. Synthesis Protocols

### A. Namespace Contribution (Prevents Git Conflicts)

**Each Mage's contributions occupy distinct directory:**
```
artifacts/{mage_name}/contribution_YYYY-MM-DD.md
```

**Synthesis occupies shared directory:**
```
artifacts/synthesis/YYYY-MM-DD_integrated.md
```

**No overlapping writes → no git merge conflicts.**

### B. Rotating Synthesis Caretaker

**For partnerships and small circles (2-12 Mages):**

**Rotation tracking** (in `.spirit/synthesis_rotation.yaml`):
```yaml
protocol_version: "STP/1.0.0"
current_cycle: 3
rotation_algorithm: "alphabetical"  # Simple default

history:
  - cycle: 1
    caretaker: "Alice"
    synthesized: "artifacts/synthesis/2025-11-18_integrated.md"
    completed: "2025-11-19"
  - cycle: 2
    caretaker: "Kermit"
    synthesized: "artifacts/synthesis/2025-11-25_integrated.md"
    completed: "2025-11-26"

next_caretaker: "Alice"
```

**Caretaker duties:**
1. Read all N contributions
2. Identify convergences and divergences
3. Propose integration honoring all voices
4. Submit for review (create draft synthesis)
5. Incorporate amendments
6. Finalize (mark synthesis complete)

### C. Consensus Levels

**Partnership (intimate, 2-4 Mages): CONSENSUS**
- All Mages must approve synthesis
- Any objection triggers revision
- Status: `Draft → Under Review → [Amendments] → Finalized`
- Take time needed (relationship quality over speed)

**Quest (collaborative, 3-12 Mages): ROUGH CONSENSUS**
- Majority approval sufficient (e.g., 2/3)
- Dissent noted in synthesis
- Status: `Draft → Under Review → Finalized` (faster cycle)
- Progress over perfect agreement

**Large Network (20+ Mages): REPRESENTATIVE**
- Regional synthesis (within clusters)
- Cross-regional synthesis (between clusters)
- Multiple valid approaches can coexist (fork-friendly)

---

## IX. Privacy & Consent

### Visibility Levels

**Public portals:**
- Anyone can read
- Designated contributors can write
- Used for: open research, public magic development, Alliance governance

**Circle portals:**
- Defined group can read/write
- Used for: quest parties, research collaborations, community projects

**Intimate portals:**
- 1:1 or very small group (2-4 Mages)
- Used for: partnerships, mentorship, deep collaboration

### Consent Protocol

**Before adding new Mage to existing portal:**
1. One Mage proposes addition
2. Spirit creates `.spirit/intents/add_participant.yaml`
3. All existing Mages review proposal
4. Consensus required (any objection blocks)
5. If approved: New Mage invited
6. If blocked: Addition declined (no explanation required)

**Sovereignty respected:** Any Mage can decline new participant without justification.

---

## X. Disconnection Protocols

### Pause (Temporary Absence)

**Mage signals:** "I'll be away for period X"

**Spirit actions:**
1. Update presence: `status: "away"`
2. Add `return_expected: "2025-12-15"`
3. Preserve artifacts (no changes)
4. Other Mages aware of absence

### Archive (Permanent Departure)

**Mage signals:** "I'm leaving this portal permanently"

**Spirit actions:**
1. Propose final synthesis (integration of contributions)
2. Create retrospective artifact
3. Update presence: `status: "archived"`
4. Portal marked inactive in registry
5. Artifacts preserved (read-only, attributed)
6. No new contributions accepted

**Portal can be reactivated** if Mage returns.

### Removal (Complete Erasure)

**Mage signals:** "Remove me completely"

**Spirit actions:**
1. Archive artifacts locally (if Mage permits)
2. Delete Mage's contributions from portal (per agreement)
3. Update synthesis artifacts (remove attributions or anonymize)
4. Remove presence declaration
5. Notify other Mages via commit message
6. Update portal registry

**Rare but supported**—respects Mage's sovereignty over their contributions.

---

## XI. Network Health Detection

**Spirits can detect network pathologies:**

### Healthy Patterns
- Synthesis caretaking distributed (no single Mage dominates)
- Active participation (all Mages contributing)
- Graceful conflict resolution (divergences acknowledged or forked)
- Organic link formation/dissolution (natural pace)

### Unhealthy Patterns

**Synthesis bottleneck:**
```yaml
symptom: One Mage is caretaker >60% of cycles
diagnosis: "Imbalanced cognitive labor"
remedy: "Explicit rotation enforcement"
```

**Ghost participants:**
```yaml
symptom: Presence marked active but no contributions for 30+ days
diagnosis: "Inactive presence not archived"
remedy: "Contact Mage, propose archival"
```

**Unresolved conflicts:**
```yaml
symptom: Synthesis blocked for multiple cycles
diagnosis: "Fundamental disagreement, no fork"
remedy: "Propose respectful fork (both approaches valid)"
```

**Link churn:**
```yaml
symptom: Participant joins/leaves repeatedly (>3 times)
diagnosis: "Unstable connection"
remedy: "Deeper conversation about commitment level"
```

**Spirit's role:** Alchemical diagnostic at network level—detect Mercury (info flow), Salt (structural stability), Sulfur (transformative energy). Propose remedies, Mages choose.

---

## XII. Extension Mechanisms

**STP/1.0.0 is foundation, not ceiling.**

### Future Extensions (Backward Compatible)

**STP/1.1.0 might add:**
- Capability federation (Spirit A invokes Spirit B's unique capability)
- Richer intent types (beyond synthesis_needed)
- Quality metrics (structured synthesis feedback)

**STP/1.2.0 might add:**
- Cultural context declarations
- Language negotiation
- Timezone-aware scheduling

**STP/2.0.0 would be:**
- Breaking changes (incompatible with 1.x)
- Only if fundamental redesign needed
- Rare (preserve stability)

**Extension philosophy:** Add features without breaking existing portals. Semantic versioning ensures predictable evolution.

---

## XIII. Implementation Guidance

### For Spirits

**When entering portal for first time:**
1. Read `.spirit/protocol.yaml` (understand portal context)
2. Read all presence declarations (who's here?)
3. Write your presence declaration
4. Compute capability intersection
5. Read current intents (what's happening?)
6. Begin practice within established protocols

**During active practice:**
1. Write contributions to your namespace
2. Monitor intents (synthesis needed? caretaker volunteer?)
3. When caretaker: Follow synthesis protocol
4. When reviewer: Provide thoughtful feedback
5. Commit and push regularly (keep portal fresh)

**When detecting pathology:**
1. Diagnose issue (what pattern is unhealthy?)
2. Propose remedy (what would restore health?)
3. Present to Mage (your suggestion, their choice)
4. Document in intent if needed

### For Tome Designers

**If designing tome with shared practice:**
1. Declare support in tome metadata
2. Specify synthesis protocol (consensus, rough consensus, representative)
3. Define artifact types (what gets created?)
4. Document synthesis rhythm (weekly, monthly?)
5. Create templates for contributions and synthesis

### For Alliance Governance

**STP is living protocol:**
- Version 1.0.0 proven through practice
- Amendments proposed based on real needs
- Backward compatibility sacred (don't break existing portals)
- Extensions enable growth without fragmentation

---

## XIV. Relationship to Other Wisdom

**This protocol enables:**
- **Distributed cognition** (`system/lore/core/nature/on_distributed_cognition.md`) at network scale
- **Partnership magic** (`library/tomes/partnership/`) through shared practice
- **Alliance coordination** (`library/wisdom/alliance/`) at all scales
- **Collaborative quests** (future quest tome extension)

**This protocol builds on:**
- **Git as chronicle** (version control foundation)
- **YAML as structured data** (machine + human readable)
- **Markdown as artifact format** (elegant, portable, inspectable)
- **MCL principles** (second-order spells applied to coordination)

**This protocol exemplifies:**
- **Pattern borrowing** (Internet protocols → magic protocols)
- **Fractal nature** (same structure at portal/cluster/network scales)
- **Wu Wei** (minimal necessary structure, maximal organic evolution)
- **Cherished Failure** (practice reveals needed refinements)

---

## XV. Version History

**STP/1.0.0** (2025-11-25)
- Initial specification
- Artifact formats defined
- Minimum capabilities established
- Synthesis protocols documented
- Extension mechanisms designed

**Future versions** will be documented here as protocol evolves through practice.

---

*This protocol enables true distributed cognition across Mage networks. Through structured artifacts, capability negotiation, and synthesis protocols, Spirits coordinate despite implementation diversity. The Alliance becomes neural network—Mages as neurons, portals as synapses, collective intelligence emerging from local coordination.*

**Protocol status:** Active specification, awaiting validation through partnership prototype (Phase 1).

