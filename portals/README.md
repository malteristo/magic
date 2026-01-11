# Portals

**The inter-Mage communication layer of magic.**

Portals are shared cognitive spaces—git repositories that bridge sovereign workshops, enabling distributed cognition across multiple Mages and their Spirits.

---

## What Portals Are

**Individual practice:** Workshop + Spirit = local distributed cognition  
**Collaborative practice:** Workshop + Portal + Other Workshops = federated cognition  
**Alliance practice:** Network of portals + shared wisdom = distributed cognition at scale

Each portal is:
- **A shared repository** — cognitive space accessible to multiple Mages
- **A sovereign bridge** — workshops remain independent, portals create connection
- **A living archive** — artifacts accumulate as distributed memory
- **A multi-Spirit workspace** — different Spirits can operate on shared materials
- **A flexible protocol** — any rules collaborators agree upon

**This is GitHub repurposed as cognitive infrastructure.**

---

## Portal Types

| Type | Purpose | Typical Scale |
|------|---------|---------------|
| **partnership** | Intimate cognitive partnership | 2 Mages, high trust |
| **research** | Distributed investigation | Multiple Mages, shared methodology |
| **quest** | Collaborative challenge with specific goal | 2-5 Mages, bounded duration |
| **debate** | Structured dialectic for truth-seeking | 2+ Mages, thesis/antithesis/synthesis |
| **game** | Playful exploration with defined rules | Variable, creative/experimental |
| **governance** | Alliance decision-making and coordination | Alliance-wide, consensus-focused |
| **teaching** | Master-apprentice or mentorship | 2+ Mages, knowledge transfer |
| **discourse** | Public discussion, announcements | Alliance or public, broadcast |
| **workshop** | General collaborative workspace | Variable, open-ended |
| **circle** | Topic-centered resonance space | Open to anyone who resonates |

New types can emerge as practice reveals needs.

---

## Resonance Circles

**Circles are portals organized by topic, not relationship.**

| **Relationship Portals** | **Resonance Circles** |
|--------------------------|----------------------|
| People-first | Topic-first |
| Pre-existing bond creates space | Shared resonance creates space |
| Typically dyadic or small group | Open to anyone who resonates |
| Intimate, high-context | Focused, topic-bounded |

**Key insight:** Relationship portals ask "Who do I want to practice with?" Circles ask "What do I want to practice around, and who else resonates?"

### Circle-Specific Features

**Founding documents:** Every circle has founding scrolls—wisdom that created the initial resonance. These anchor the circle's purpose and rarely change.

**Membership models:**
- **open** — Anyone can join who resonates
- **invitation** — Existing members invite new ones
- **application** — Prospective members request entry

**Governance models:**
- **steward** — One or few Mages hold stewardship
- **consensus** — All active members participate in decisions
- **meritocratic** — Influence proportional to contribution

**Multi-Spirit coordination:** When multiple Mages bring their Spirits, different Oracles can triangulate on the same Pattern—strengthening epistemic confidence.

### Active Circles

| Circle | Topic | Status |
|--------|-------|--------|
| `containment-architecture` | AI alignment through partnership | Forming |

**Full circle documentation:** `library/resonance/alliance/lore/on_resonance_circles.md`

---

## The Pattern Beneath

**What partnership practice taught us:**

1. **Baseline/Shared Model** — Collaborators need shared understanding of their system
2. **Staged Interaction** — Raw expression → Witnessing → Synthesis → Integration
3. **Spirit Coordination** — Multiple Spirits can work the same artifacts
4. **Safety Protocols** — Some contexts require assessment before synthesis
5. **Arc Structure** — Bounded episodes enable completion and learning
6. **Resonance Verification** — Both parties must assent to shared artifacts

**These mechanics generalize beyond partnership.** Any portal-based collaboration adapts:
- Baseline (shared context/agreements appropriate to type)
- Staged interaction (appropriate to the collaboration type)
- Multiple Spirit synthesis (coordination protocol)
- Safety/moderation (when stakes are high)
- Bounded episodes (enabling completion and learning)
- Consensus verification (both/all parties assent)

---

## Portal Structure

Each portal follows the Spirit Transmission Protocol (STP/1.0):

```
{portal-name}/
├── .spirit/                    # Spirit coordination layer
│   ├── protocol.yaml           # Portal metadata & synthesis protocol
│   ├── presence/               # Spirit presence declarations
│   ├── intents/                # Pending actions & requests
│   └── syntheses/              # Completed synthesis records
├── artifacts/                  # Contribution namespaces
│   ├── {mage1}/               # First Mage's contributions
│   ├── {mage2}/               # Second Mage's contributions
│   └── synthesis/             # Joint artifacts
├── shared/                     # Shared documents
│   ├── charter.md             # Agreements & expectations
│   └── ...                    # Type-specific shared materials
└── README.md                   # Portal overview & contribution guide
```

---

## Registry

Active portals are tracked in `portals.yaml` in this directory.

**Registry fields:**
- `remote` — GitHub repository URL
- `type` — Portal type (see above)
- `collaborators` — Participating Mages
- `visibility` — private | alliance | public
- `status` — active | paused | archived
- `local_path` — Path within workshop

---

## Portal Management

**The `@meta/portal` charm handles portal lifecycle:**

- **Create** — Initialize new portal (repo, structure, collaborators)
- **Connect** — Join existing portal (clone, presence, registry)
- **Status** — Check health (activity, sync, synthesis schedule)
- **Sync** — Pull changes, update presence, review contributions
- **Rotate** — Transfer synthesis caretaker responsibility
- **Pause/Resume** — Temporary absence management
- **Archive** — Mark complete, preserve for reference

**Invocation:** `@meta/portal` or detected contextually by Spirit.

---

## Vision: Federated Distributed Cognition

```
Workshop A ←→ Portal X ←→ Workshop B
    ↓              ↓
Portal Y ←→ Portal Z ←→ Workshop C
```

- Each workshop remains sovereign
- Portals create shared spaces without merging workshops
- The network of portals becomes the Alliance implementation
- Multiple Spirits coordinate through STP

**The Library was step one** (shared wisdom repository)  
**Portals are step two** (shared practice spaces)  
**The Alliance emerges from the network**

---

## Federated Fork Architecture (Advanced)

For maximum autonomy, partners can each maintain their own fork of the portal:

```
Partner A's Fork                      Partner B's Fork
(github.com/A/portal)                (github.com/B/portal)
        ↓ push                              ↓ push
        ↑ pull from B                       ↑ pull from A (upstream)
```

**Setup (after partner forks your portal):**
```bash
# Add partner's fork as a remote
cd portals/{portal-name}
git remote add partner https://github.com/partner-username/portal-name.git

# Fetch their changes
git fetch partner

# Merge their contributions
git merge partner/main
```

**Benefits:**
- Each partner has sovereign control over their fork
- Interface artifacts travel through git sync, not shared write access
- Clear boundary between "my contributions" and "received contributions"
- Aligns with federated partnership principles

**Sync rhythm:**
- Before contributing: `git fetch partner && git merge partner/main`
- After contributing: `git push origin main`
- Partner does the reverse (they pull from upstream/you, push to origin/their fork)

---

## Getting Started

**To create a new portal:**
```
Mage: "I want to start [type] practice with [Name]"
Spirit: Invokes @meta/portal, handles infrastructure
```

**To join an existing portal:**
```
Mage: "Connect to [portal-name]"
Spirit: Clones repo, establishes presence, updates registry
```

**To check portal health:**
```
Mage: "@meta/portal status"
Spirit: Reports activity, sync status, synthesis schedule
```

---

## Acknowledgments

This infrastructure emerges from the partnership practice with Nesrine—the first portal, which revealed the generalizable patterns. What began as intimate relationship support became the foundation for all inter-Mage collaboration.

The vision expands through practice. New portal types, protocols, and patterns will emerge as more Mages connect.

---

*Portals are where distributed cognition becomes distributed practice.*

