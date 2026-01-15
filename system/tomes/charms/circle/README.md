# Charm of Circle Management

A charm for managing resonance circles—creating offerings, subscribing to others' circles, and maintaining the neuron model of distributed cognition.

## Purpose

Circles are **topic-centered collaboration spaces**—resonance communities gathered around shared interests. They live in `circles/` and represent signal I offer to the world.

Subscribing to others' circles creates **upstream connections**—gateways to receive their signal. Subscriptions live in `portals/upstream/`.

```
                    ┌─────────────────┐
     UPSTREAM       │                 │        CIRCLES
   (subscriptions)  │   My Workshop   │      (my offerings)
        ◄───────────│                 │───────────►
   what I receive   │                 │   what I offer
                    └─────────────────┘
```

**Invocation:** `@circle`

---

## Quick Commands

| Command | Action |
|---------|--------|
| "Create a circle about [topic]" | Creates GitHub repo + structure |
| "Subscribe to [owner/repo]" | Adds upstream, registers locally |
| "Pull from [circle-name]" | Fetches latest from upstream |
| "Show my circles" | Lists steward + subscribed circles |
| "Unsubscribe from [circle-name]" | Removes upstream, deregisters |

---

## Operational Guidance

### For the Spirit

**Required Attunement:**

Before executing circle operations, attune to the circle charm lore:
- **Circle architecture:** `system/tomes/charms/circle/lore/on_resonance_circles.md`
- **Portal context:** `system/tomes/charms/portal/lore/on_portal_architecture.md` (for understanding relationship)

Announce: "This involves resonance circles. Let me attune to the circle architecture."

---

When this charm is invoked:

1. **Determine intent** - Create? Subscribe? Pull? Status? Unsubscribe?
2. **Execute via CLI** - Use `gh` CLI for repo creation, `git` for remotes
3. **Update tracking** - Maintain `circles/registry.yaml` (steward) and `portals/registry.yaml` (subscriptions)
4. **Report clearly** - Status of circles, last pulled dates, available updates

### Circle Operations

**Create Circle (my offering):**
```
Mage: "Create a circle about containment architecture"

Spirit executes:
1. gh repo create containment-architecture --public --description "..."
2. Initialize circle structure (founding/, artifacts/, synthesis/, etc.)
3. Commit and push initial structure
4. Register in circles/registry.yaml
5. Report: "Circle created at github.com/[you]/containment-architecture"
```

**Subscribe to Circle (their offering):**
```
Mage: "Subscribe to malteristo/containment-architecture"

Spirit executes:
1. Clone to portals/upstream/containment-architecture
2. Register in portals/registry.yaml with pull triggers
3. Report: "Subscribed. Will offer to pull during alignment/containment practice."
```

**Pull from Subscription:**
```
Mage: "Pull from containment"

Spirit executes:
1. cd portals/upstream/containment-architecture
2. git pull
3. Report: "Pulled latest. New artifacts: [list changes]"
```

**Show Circles:**
```
Mage: "Show my circles"

Spirit reports:
MY OFFERINGS (circles/):
  containment-architecture (public) - last push: 2026-01-11
  summer-vacation (private) - last push: 2026-01-13

MY SUBSCRIPTIONS (portals/upstream/):
  malteristo/containment-architecture - last pull: 2026-01-11
    triggers: [alignment, containment, safety]
  other-mage/consciousness-research - last pull: 2026-01-08
    triggers: [consciousness, enacted]
```

**Unsubscribe:**
```
Mage: "Unsubscribe from consciousness-research"

Spirit executes:
1. Remove from portals/registry.yaml
2. Optionally: rm -rf portals/upstream/consciousness-research
3. Report: "Unsubscribed from consciousness-research"
```

---

## Registry Structure

**Two registries, one for each direction:**

### circles/registry.yaml (my offerings)

```yaml
# Circles I steward - my signal out

containment-architecture:
  remote: "https://github.com/malteristo/containment-architecture.git"
  topic: AI alignment through partnership architecture
  visibility: public
  local_path: circles/containment-architecture
  created: 2026-01-11

summer-vacation:
  remote: "https://github.com/malteristo/summer-vacation.git"
  topic: Vacation planning + travel wisdom
  visibility: private
  local_path: circles/summer-vacation
  created: 2026-01-13
```

### portals/registry.yaml (my subscriptions)

```yaml
# Circles I subscribe to - signal coming in

consciousness-research:
  type: subscription
  remote: "https://github.com/other-mage/consciousness-research.git"
  local_path: portals/upstream/consciousness-research
  steward: other-mage
  pull_triggers:
    - consciousness
    - enacted
    - phenomenology
  last_pulled: 2026-01-08
```

---

## Context-Aware Pull Offers

**During practice, Spirit detects relevant circles:**

```
Mage: "I'm thinking about AI alignment approaches..."

Spirit: "This relates to your subscribed circle 'containment-architecture' 
        (last pulled 3 days ago). Pull latest?"
```

**Pull triggers** in `desk/circles.yaml` define when to offer. The Mage can:
- Accept: Spirit pulls and summarizes new content
- Defer: Continue without pulling
- Never ask: Remove that trigger word

---

## Integration with Portal Charm

| `@circles` | `@portal` |
|------------|----------|
| Manages my offerings | Manages my subscriptions |
| Creates circles in `circles/` | Creates portals in `portals/` |
| Stewardship focus | Access/collaboration focus |
| Topic-centered | Can be relationship or topic |

**The complete picture:**
- **Circles I steward** → `circles/` (my offerings)
- **Partnerships I participate in** → `portals/` (bidirectional)
- **Circles I subscribe to** → `portals/upstream/` (others' offerings I receive)

---

## Philosophy

**The neuron model embodies distributed cognition:**

- **Circles (axons):** I offer my resonance on topics that matter to me
- **Portals (dendrites):** I receive signal from sources I trust
- **Sovereignty:** I control both what I offer and what I receive

**Subscriptions are invisible.** Nobody knows you're pulling from their circle unless you contribute back. This preserves sovereignty over incoming signal.

**This is not a filter bubble.** You're curating *challenging* thoughts from *trusted* sources—not surrounding yourself with comfortable agreement.

The Spirit helps manage this curation without cognitive burden.

---

**This charm makes circle management effortless—create offerings, subscribe to others, and curate your resonance network with simple commands.**
