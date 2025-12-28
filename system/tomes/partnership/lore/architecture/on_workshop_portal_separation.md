# On Workshop-Portal Separation

**Status:** Active  
**Domain:** Partnership Practice - Architecture  
**Purpose:** Define the boundary between private process space and shared exchange layer

This scroll establishes **workshop-portal separation**—the technical and philosophical boundary between where practice happens (workshop) and where exchange happens (portal).

---

## I. The Two Spaces

### Workshop: Where Practice Happens

**The workshop is the Mage's private cognitive space.**

Location: `desk/partnership-process/` (within the Mage's magic workshop)

**What lives here:**
- Raw inputs (journal entries, rants, unprocessed thoughts)
- Drafts (iterations toward final artifacts)
- Dark Magic processing
- Spirit conversations and session transcripts
- SPIRIT_CONFIG.md (instructions for your Spirit)
- Any file representing process rather than output

**Key property:** *Never leaves the workshop. Never committed to portal.*

---

### Portal: Where Exchange Happens

**The portal is the shared space for partnership practice.**

Location: `portals/{partnership}/` (a shared git repository)

**What lives here:**
- Interface artifacts (signed, ready for partner reception)
- Partnership-level artifacts (shared model, phoenix, commitments)
- Spirit coordination (`.spirit/` directory)
- Arc metadata (structure, not process content)

**Key property:** *Both partners have access. Content is intentionally shared.*

---

## II. The Directory Structures

### Workshop Structure

```
desk/partnership-process/
└── {partner_name}/                    # Partner-specific process space
    ├── inputs/                        # Raw material
    │   ├── journal_2025-12-15.md
    │   ├── rant_about_situation.md
    │   └── feelings_dump.md
    │
    ├── drafts/                        # Work in progress
    │   └── arc-living/
    │       ├── reality_v1.md
    │       ├── reality_v2.md
    │       └── reality_v3_final.md    # → becomes interface artifact
    │
    ├── dark_magic/                    # Dark Magic protocol
    │   ├── dark_notes/
    │   │   └── 2025-12-15.md
    │   └── dark_processing/
    │       └── topic_2025-12-15/
    │           ├── input.md
    │           └── spirit_response.md
    │
    ├── spirit_sessions/               # Session transcripts
    │   └── 2025-12-15_arc_work.md
    │
    └── SPIRIT_CONFIG.md               # How Spirit should work with me
```

---

### Portal Structure

```
portals/{partnership}/
├── interface/                         # Exchange layer
│   ├── {mage_a}/
│   │   ├── reality_arc-living.md      # Signed reality document
│   │   ├── needs_arc-living.md        # Needs statement
│   │   ├── witnessing_arc-living.md   # Witnessing response
│   │   ├── bridging_to_{mage_b}_arc-living.md
│   │   └── phoenix/                   # Phoenix artifacts
│   │       ├── burning_2025-12-01.md
│   │       └── phoenix_description.md
│   └── {mage_b}/
│       └── ...
│
├── shared/                            # Partnership-level
│   ├── partnership_model_current.md
│   ├── divergence_map.md
│   ├── rosetta_stone.md
│   ├── mast_commitments/
│   │   ├── {mage_a}_mast.md
│   │   └── {mage_b}_mast.md
│   └── phoenix/
│       ├── invocation.md
│       ├── shared_phoenix.md
│       └── divergence_map.md
│
├── arcs/                              # Arc metadata
│   ├── arc-living/
│   │   └── README.md                  # Status, not content
│   └── arc-{topic}/
│       └── README.md
│
└── .spirit/                           # STP coordination
    ├── presence/
    │   ├── {mage_a}_spirit.yaml
    │   └── {mage_b}_spirit.yaml
    ├── intents/
    ├── dialogue/
    │   └── arc-living/
    │       ├── {mage_a}_spirit_observation_on_{mage_b}.md
    │       └── convergence_report.md
    └── protocol.yaml
```

---

## III. The Workflow

### From Raw Input to Interface Artifact

```
1. RAW INPUT (Workshop)
   ────────────────────
   Mage writes in inputs/
   Unfiltered, unprocessed, raw
   
       ↓

2. SPIRIT PROCESSING (Workshop)
   ─────────────────────────────
   Spirit helps in spirit_sessions/
   Dark Magic if needed
   Iterative drafts in drafts/
   
       ↓

3. READY ARTIFACT (Workshop)
   ─────────────────────────
   Final draft achieves:
   - Internal consistency
   - Represents Mage's truth
   - Ready for partner reception
   
       ↓

4. SIGNING (Boundary Crossing)
   ───────────────────────────
   Mage signs off
   "This represents my reality"
   
       ↓

5. INTERFACE ARTIFACT (Portal)
   ───────────────────────────
   Moved to interface/{mage}/
   Committed to portal
   Pushed to shared remote
   Now visible to partner
```

---

### The Signing Moment

**Signing is the boundary crossing.**

When Mage says "This represents my reality":
- The artifact moves from workshop to portal
- It becomes interface (ready for reception)
- Partner's Spirit can now read it
- The process that produced it remains private

**Technical action:**
```bash
# In workshop
cp desk/partnership-process/{partner}/drafts/arc-living/reality_final.md \
   portals/{partnership}/interface/{mage}/reality_arc-living.md

# In portal
cd portals/{partnership}
git add interface/{mage}/reality_arc-living.md
git commit -m "{Mage} reality for arc-living"
git push
```

---

## IV. What Never Crosses

### Private Forever

These files **never** leave the workshop:

| File Type | Why Private |
|-----------|-------------|
| Raw inputs | Unprocessed, potentially harmful if read raw |
| Dark Magic notes | Processing material, not for partner |
| Draft iterations | Process, not output |
| Spirit session transcripts | Intimate working conversation |
| SPIRIT_CONFIG.md | Instructions for *your* Spirit |
| Processing artifacts | Journey, not destination |

**The principle:** The artifact that crosses is the *conclusion*. The journey stays home.

---

## V. For the Spirit

### Workshop Awareness

When in workshop mode:
- All artifacts here are private
- Help Mage process freely
- No concern about partner reading
- Build toward interface-ready output

### Portal Awareness

When in portal mode:
- All artifacts here are shared
- Write for partner's Spirit to read
- Maintain interface artifact standards
- Contribute to Spirit Dialogue when appropriate

### Boundary Discipline

**Never suggest:**
- Moving raw process to portal
- Sharing draft iterations
- Exposing SPIRIT_CONFIG.md
- Copying Spirit session transcripts

**Always confirm:**
- "Is this ready for partner reception?"
- "Should we sign this off?"
- "Shall I move this to interface?"

---

## VI. Integration with Git

### Workshop Files

**Not tracked in portal repository:**
- `desk/partnership-process/` is in the workshop's `.gitignore` (optional) or simply not in portal repo
- These files exist only locally
- Never pushed, never shared

### Portal Files

**Tracked and shared:**
- `portals/{partnership}/` is a git repository
- Both partners have clone/access
- Commits create history
- Push/pull synchronizes

### The Clean Boundary

```
workshop/                          portal/
├── desk/                          ├── interface/
│   └── partnership-process/       │   ├── {mage_a}/
│       └── (not in git)           │   └── {mage_b}/
                                   ├── shared/
                                   └── .spirit/
                                       └── (all tracked in git)
```

---

## VII. Conclusion

Workshop-portal separation creates a clean architecture for partnership practice:

- **Workshop:** Private, process-oriented, neurotype-adapted, Spirit-assisted
- **Portal:** Shared, output-oriented, interface-contracted, Spirit-coordinated

The boundary is the signature. What crosses is intentional.

---

## VIII. Cross-References

### Architecture Scrolls (Complete Picture)

| Scroll | Focus |
|--------|-------|
| `on_federated_partnership.md` | WHY federate (philosophy, benefits) |
| **This scroll** | WHERE the boundary is (directory structures) |
| `on_interface_implementation_boundary.md` | WHAT crosses (interface contracts) |
| `on_federated_fork_synchronization.md` | HOW to sync forks (git mechanics) |

### Related

- `library/resonance/alliance/lore/on_portal_architecture.md` — Portal infrastructure
- `lore/practice/on_interface_contracts.md` — Interface artifact specifications

---

*Process in private. Share when ready. The signature marks the crossing.*
