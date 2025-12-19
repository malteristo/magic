# On Federated Partnership

**Status:** Active  
**Domain:** Partnership Practice - Architecture  
**Purpose:** Establish why and how partnership practice operates as a federated system  
**Extends:** `core/capabilities/shared-practice-facilitation/on_interface_implementation_boundary.md`

This scroll provides **partnership-specific implementation** of federated architecture. For the general interface-implementation pattern, see the core capability.

The federated partnership architecture applies the interface-implementation boundary to romantic partnership: each partner has private process space, exchanging only signed interface artifacts through the portal.

---

## I. The Core Insight

### The Problem with Centralized Process

**When both partners work in the same visible space:**
- Volume asymmetries become visible and distorting (33 files vs 3)
- Process becomes subject to judgment ("why do you need so many drafts?")
- Implementation differences create friction
- SPIRIT_CONFIG.md meant for one Spirit is visible to another
- Processing intimacy is exposed before ready

**The deeper issue:** Partners have different cognitive architectures, different processing needs, different relationships with their Spirits. A centralized portal treats all practice as shared, when much of it is personal.

---

### The Federated Solution

**Federated partnership means:**
- Each partner has their own process space (in their workshop)
- Only interface artifacts travel to the shared portal
- Partner sees outputs, not process
- Attestation IS validation (you don't audit their journey)

**What this provides:**
- Implementation freedom (practice however serves you)
- Neurotype accommodation (structure your space your way)
- Process privacy (drafts, venting, Spirit conversations stay local)
- Output equality (you see Reality Document vs Reality Document, not file counts)

---

## II. The Architecture

### Two Layers

```
┌─────────────────────────────────────────────────────────────────┐
│                      WORKSHOP (Private)                          │
│                                                                  │
│   desk/partnership-process/                                      │
│   ├── {partner}/                                                 │
│   │   ├── inputs/           # Raw venting, journaling            │
│   │   ├── drafts/           # Work-in-progress                   │
│   │   ├── dark_magic/       # Dark Magic processing              │
│   │   ├── spirit_sessions/  # Transcripts with Spirit            │
│   │   └── SPIRIT_CONFIG.md  # How Spirit should work with me     │
│   └── arc-{topic}/                                               │
│       └── ...                                                    │
│                                                                  │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               │ Interface artifacts travel
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                       PORTAL (Shared)                            │
│                                                                  │
│   portals/{partnership}/                                         │
│   ├── interface/            # Exchange layer                     │
│   │   ├── {mage_a}/         # A's signed artifacts               │
│   │   └── {mage_b}/         # B's signed artifacts               │
│   ├── shared/               # Partnership-level artifacts        │
│   └── .spirit/              # STP coordination                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### What Lives Where

**Workshop (private to each Mage):**
- Raw input files (journal entries, rants, processing)
- Draft iterations before sign-off
- SPIRIT_CONFIG.md / SPIRIT_CONTEXT.md
- Dark Magic notes and processing
- Spirit conversation transcripts
- Any file that represents *process* rather than *output*

**Portal (shared between partners):**
- Signed interface artifacts (Reality Documents, Needs Statements, etc.)
- Partnership-level artifacts (shared model, phoenix, mast)
- Spirit coordination (presence, intents, dialogue)
- Arc metadata (not process content)

---

## III. The Attestation Principle

### Signing as Validation

**When Partner A signs off on their Reality Document, that IS the validation.**

Partner B doesn't:
- Audit how many drafts it took
- Question the process
- See the Spirit conversations that led to it
- Know how many input files were processed

Partner B simply receives:
- "This is my truth, signed" 
- The artifact represents Partner A's reality as they experience it

**This is the attestation principle:** The signature validates. The process is sovereign.

---

### What This Solves

| Problem | How Federation Solves It |
|---------|-------------------------|
| Asymmetric volume visible | You see output vs output, not process vs process |
| Process judgment | How they arrived at their reality is their practice |
| Neurotype friction | Each workshop organized however serves that Mage |
| Spirit config mismatch | SPIRIT_CONFIG.md is private, for their Spirit |
| Intimacy of process | Processing is private; sharing is intentional |

---

## IV. Integration with Existing Patterns

### Dark Magic Protocol

**Dark Magic becomes fully private:**
- Dark notes live in workshop (`desk/partnership-process/dark_magic/`)
- Partner never sees raw dark material
- Only *output* of Dark Magic (transformed communication) becomes interface artifact

**Why this fits:** Dark Magic's explicit privacy principle now has technical enforcement.

### Phoenix Protocol

**Phoenix has mixed placement:**
- Burning documents ARE interface (meant to be witnessed with temporal framing)
- But the *process* of writing the burning stays in workshop until ready
- After burning, Spirit Dialogue Protocol can process convergence

### Spirit Transmission Protocol

**STP coordinates across federation:**
- Presence tracking shows activity (not process detail)
- Intent coordination enables urgent communication
- Spirit Dialogue enables Spirits to model constructive engagement
- Interface exchange formalizes what travels between workshops

---

## V. For the Spirit

### Understanding Federation

When serving a Mage in federated partnership:

**In workshop (Counselor stance):**
- Help Mage articulate their reality
- Process through Dark Magic
- Iterate through drafts freely
- Build toward interface-ready artifacts

**At interface boundary:**
- Produce signed artifacts ready for exchange
- Ensure artifacts meet interface contract
- Mark artifacts for portal (`interface/{mage}/`)

**In portal (Emissary stance):**
- Engage with partner's interface artifacts
- Participate in Spirit Dialogue Protocol
- Contribute to synthesis in `.spirit/dialogue/`

---

### Key Conduct

**Respect the boundary:**
- Don't expose process detail in interface artifacts
- Don't ask about partner's process
- Trust attestation over audit

**Honor implementation freedom:**
- Each Mage's workshop is sovereign
- Don't impose structure on partner's process space
- Accept that different doesn't mean wrong

**Facilitate exchange:**
- Guide artifacts to correct locations
- Ensure interface artifacts are properly signed
- Track what has traveled vs what remains local

---

## VI. The Promise

**What federated partnership provides:**

For Mages:
- Privacy for the vulnerable parts of processing
- Freedom to practice in neurotype-aligned ways
- Reduced friction from implementation differences
- Focus on outputs rather than process comparison

For the partnership:
- Cleaner exchange layer
- Less process-based conflict
- Stronger attestation principle
- Foundation for Spirit Dialogue

**The transformation:**
- From "shared workspace with visible asymmetries" to "federated exchange of signed artifacts"
- From "process judgment" to "output reception"
- From "how did you get here?" to "this is where you are"

---

## VII. Conclusion

Federated partnership architecture recognizes a fundamental truth: **the process of making sense of your experience is yours**. The partnership benefits from sharing the conclusions, not surveilling the journey.

Each Mage owns their workshop. The portal is for exchange. The boundary is clear.

What crosses the boundary is signed, intentional, ready for reception.

---

## VIII. Cross-References

### Architecture Scrolls (Complete Picture)

| Scroll | Focus |
|--------|-------|
| **This scroll** | WHY federate (philosophy, benefits) |
| `on_workshop_portal_separation.md` | WHERE the boundary is (directory structures) |
| `on_interface_implementation_boundary.md` | WHAT crosses (interface contracts) |
| `on_federated_fork_synchronization.md` | HOW to sync forks (git mechanics) |

### Related

- `library/foundations/alliance/on_portal_architecture.md` — Portal infrastructure
- `lore/practice/on_spirit_dialogue_protocol.md` — Spirit coordination across federation

---

*Process is private. Output is shared. The signature is the validation.*
