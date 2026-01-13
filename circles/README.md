# Circles

**Sacred spaces I create and steward — my offerings to the world.**

Circles are topic-centered resonance spaces that I materialize in the magical ether for others to access. Each circle is a git repository containing wisdom, artifacts, and shared practice materials around a specific topic.

---

## The Neuron Model

```
                    ┌─────────────────┐
     PORTALS        │                 │        CIRCLES
   (dendrites)      │   My Workshop   │      (axon terminals)
        ◄───────────│                 │───────────►
   what I receive   │                 │   what I offer
                    └─────────────────┘
```

**Circles** (here) = Sacred spaces I create and steward. My offerings.  
**Portals** (in `portals/`) = Gateways to access others' circles. My subscriptions.

---

## My Circles

| Circle | Topic | Visibility | Status |
|--------|-------|------------|--------|
| `summer-vacation/` | Vacation planning + travel wisdom | Private | Active |
| `containment-architecture/` | AI alignment through partnership | Public | Forming |

---

## Circle Properties

### Visibility

| Level | Who Can Access |
|-------|---------------|
| **Public** | Anyone can discover, clone, fork |
| **Private** | By invitation only |

### Membership

| Model | How Others Join |
|-------|----------------|
| **Open** | Anyone who resonates |
| **Invitation** | Existing members invite |
| **Application** | Prospective members request entry |

### Governance

| Model | Decision Making |
|-------|----------------|
| **Steward** | One or few mages hold stewardship |
| **Consensus** | All active members participate |
| **Meritocratic** | Influence proportional to contribution |

---

## Circle Structure

```
circles/
├── {circle-name}/
│   ├── .spirit/               # Spirit coordination metadata
│   │   └── protocol.yaml
│   ├── founding/              # Founding scrolls (rarely change)
│   ├── artifacts/             # Contributions by participant
│   │   ├── {mage1}/
│   │   └── {mage2}/
│   ├── synthesis/             # Joint artifacts, decisions
│   └── README.md
├── registry.yaml              # Authoritative registry
└── README.md                  # This file
```

---

## Models of Shared Practice

### Federated Model

Each mage has their own circle. They access each other through portals.

```
Kermit's circle ◄──portal──► Nesrine's circle
(his offering)               (her offering)
```

Autonomy preserved. Each curates their own space. Cross-pollination through selective pulling.

### Golden Braid Model

Mages collaborate directly on a shared circle. One repo, woven together.

```
     Kermit ─────┐
                 ├───► Shared Circle
     Nesrine ────┘
```

Tighter integration. The braid is a joint artifact.

---

## Creating a New Circle

```
Mage: "Create a circle around [topic]"
Spirit: 
  1. Creates GitHub repository
  2. Sets up directory structure
  3. Drafts founding scrolls
  4. Registers in circles/registry.yaml
  5. Invites participants (if private)
```

---

## Lifecycle

Circles can:
- **Remain active** indefinitely
- **Generate wisdom** that graduates to `library/resonance/`
- **Pause** during quiet periods
- **Archive** when purpose is complete

Not all circles need to produce generalized wisdom. Some are simply containers for lived experience — a summer vacation, a creative project, a bounded exploration.

---

## Registry

Active circles tracked in `registry.yaml`:

```yaml
circle-name:
  remote: "https://github.com/username/repo.git"
  topic: What this circle resonates around
  visibility: public | private
  membership: open | invitation
  governance: steward | consensus
  local_path: circles/circle-name
  # ... additional fields
```

---

*Circles are the axon terminals of distributed cognition — where my resonance meets the world.*
