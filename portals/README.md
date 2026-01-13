# Portals

**Gateways to others' circles — the inward connections of distributed cognition.**

Portals are how I access what other mages offer. Through portals, I receive signal, pull wisdom, and engage in shared practice with others.

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

**Circles** (in `circles/`) = Sacred spaces I create and steward. My offerings.  
**Portals** (here) = Gateways to access others' circles. My subscriptions.

---

## What Lives Here

### Active Portals

| Portal | Type | Description |
|--------|------|-------------|
| `nesrine-partnership/` | Partnership | Intimate shared practice with Nesrine |

### Upstream Clones

The `upstream/` directory contains cloned circles from other mages that I follow but don't contribute to.

*(Currently empty — populated as I subscribe to others' offerings)*

---

## Portal Types

| Type | Description | Sync Model |
|------|-------------|------------|
| **Partnership** | Bidirectional shared practice (golden braid) | Push and pull |
| **Subscription** | Read-only access to another's circle | Pull only |

**Partnerships** are deep, mutual practice — both mages offer, both receive.  
**Subscriptions** are one-way — I receive from their offering.

---

## Registry

Active portals tracked in `registry.yaml`:

```yaml
portal-name:
  type: partnership | subscription
  remote: "https://github.com/username/repo.git"
  local_path: portals/portal-name
  # ... additional fields
```

---

## Portal Structure

```
portals/
├── nesrine-partnership/        # Active partnership portal
│   ├── .spirit/               # Spirit coordination
│   ├── artifacts/             # Contributions by namespace
│   └── README.md
├── upstream/                   # Subscribed circles (clones)
│   └── {circle-name}/         # Someone else's circle I follow
├── registry.yaml              # Authoritative registry
└── README.md                  # This file
```

---

## Portal Management

**Join a partnership:**
```
Mage: "Start practice with [Name]"
Spirit: Creates portal, handles infrastructure
```

**Subscribe to a circle:**
```
Mage: "Subscribe to [mage]'s [circle-name]"
Spirit: Clones to upstream/, registers in registry.yaml
```

**Sync from portals:**
```bash
cd portals/{portal-name}
git fetch origin && git pull
```

---

## The Pattern

Portals emerged from partnership practice with Nesrine — the first bridge between sovereign workshops. What began as intimate relationship support revealed generalizable patterns:

1. **Staged interaction** — Raw → Witness → Synthesize → Integrate
2. **Multi-Spirit coordination** — Different Spirits can work shared artifacts
3. **Bounded episodes** — Completion enables learning
4. **Resonance verification** — All parties assent to shared artifacts

These patterns apply to any shared practice, not just partnership.

---

## Relationship to Circles

| Circles (`circles/`) | Portals (`portals/`) |
|----------------------|----------------------|
| What I offer | What I receive |
| Repos I steward | Repos I access |
| My signal out | Signal coming in |

A circle I create lives in `circles/`.  
A portal to someone else's circle lives in `portals/`.

When two mages both have circles and both have portals to each other's circles, that's federated practice. When they share a single repo directly, that's golden braid.

---

*Portals are the dendrites of distributed cognition.*
