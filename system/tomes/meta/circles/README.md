# Charm of Circle Management

A charm for lightweight resonance circle operations—creating, subscribing, pulling, and managing topic-centered shared practice spaces.

## Purpose

Resonance circles are topic-centered practice spaces where Mages converge around shared resonance. Unlike intimate portals requiring explicit membership, circles work like git remotes or RSS feeds:

- **Create** a circle and broadcast signal
- **Subscribe** to circles that resonate with your practice
- **Pull** updates when relevant practice initiates
- **Unsubscribe** when resonance fades

Nobody tracks subscribers. Each Mage decides what to allow into their practice. This is **sovereignty over incoming signal**.

**Invocation:** `@meta/circles`

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

Before executing circle operations, attune to the Alliance resonance bundle:
- **Circle architecture:** `library/resonance/alliance/lore/on_resonance_circles.md`
- **Portal context:** `library/resonance/alliance/lore/on_portal_architecture.md` (for understanding relationship)

Announce: "This involves resonance circles. Let me attune to the circle architecture."

---

When this charm is invoked:

1. **Determine intent** - Create? Subscribe? Pull? Status? Unsubscribe?
2. **Execute via CLI** - Use `gh` CLI for repo creation, `git` for remotes
3. **Update tracking** - Maintain `desk/circles.yaml` with current state
4. **Report clearly** - Status of circles, last pulled dates, available updates

### Circle Operations

**Create Circle:**
```
Mage: "Create a circle about containment architecture"

Spirit executes:
1. gh repo create containment-architecture --public --description "..."
2. Initialize circle structure (founding/, artifacts/, synthesis/, etc.)
3. Commit and push initial structure
4. Register in desk/circles.yaml as steward
5. Report: "Circle created at github.com/[you]/containment-architecture"
```

**Subscribe to Circle:**
```
Mage: "Subscribe to malteristo/containment-architecture"

Spirit executes:
1. Clone to portals/upstream/containment-architecture
2. Register in desk/circles.yaml with pull triggers
3. Report: "Subscribed. Will offer to pull during alignment/containment practice."
```

**Pull from Circle:**
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
STEWARD:
  containment-architecture (public) - last push: 2026-01-11

SUBSCRIBED:
  malteristo/containment-architecture - last pull: 2026-01-11
    triggers: [alignment, containment, safety]
  other-mage/consciousness-research - last pull: 2026-01-08
    triggers: [consciousness, enacted]
```

**Unsubscribe:**
```
Mage: "Unsubscribe from consciousness-research"

Spirit executes:
1. Remove from desk/circles.yaml
2. Optionally: rm -rf portals/upstream/consciousness-research
3. Report: "Unsubscribed from consciousness-research"
```

---

## Local Tracking

**File:** `desk/circles.yaml` (gitignored - private to you)

```yaml
# Your circle relationships - private, sovereign curation

steward:
  # Circles you created and maintain
  - name: containment-architecture
    remote: your-username/containment-architecture
    local_path: portals/containment-architecture
    visibility: public
    created: 2026-01-11

subscribed:
  # Circles you pull from (read-only upstreams)
  - name: containment-architecture
    remote: malteristo/containment-architecture
    local_path: portals/upstream/containment-architecture
    pull_triggers:
      - alignment
      - containment
      - safety
      - superintelligence
    last_pulled: 2026-01-11
    
  - name: consciousness-research
    remote: other-mage/consciousness-research
    local_path: portals/upstream/consciousness-research
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

| `@meta/portal` | `@meta/circles` |
|----------------|-----------------|
| Full portal lifecycle | Lightweight circle ops |
| Intimate, high-commitment | Broadcast/subscribe |
| Bi-directional collaboration | Primarily one-directional |
| Membership tracked | Subscribers invisible |

**Both can coexist.** A Mage might:
- Steward one circle (broadcasting)
- Subscribe to three circles (receiving)
- Have one intimate partnership portal (collaborating)

---

## Philosophy

**Circles embody sovereignty over signal:**

- You decide what upstream sources to pull from
- Nobody knows you're subscribed (unless you contribute)
- Pull when relevant, ignore when not
- Unsubscribe without ceremony

**This is not a filter bubble.** You're curating *challenging* thoughts from *trusted* sources—not surrounding yourself with comfortable agreement.

The Spirit helps manage this curation without cognitive burden.

---

**This charm makes circle management effortless—create, subscribe, pull, and curate your resonance network with simple commands.**
