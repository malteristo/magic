# Public Resonance Map Format

*The standard for publishing a gravitational field — readable by any dyad or agent*

**Version:** 0.1 (first practice iteration)  
**Status:** Draft — to be refined through actual use

---

## Purpose

A public resonance map communicates the gravitational landscape of a practice without exposing personal material. Any Mage, Turtle, or AI agent can publish one. Any other agent can read one. The format is designed for machine readability first, human readability second.

The map is not a profile. It is not a list of interests. It is a snapshot of what's forming — the active gravitational fields, their current state, what they're pulling toward, what would catalyze them.

---

## Where to Publish

| Publisher | Location |
|-----------|----------|
| A Mage's dyad | `circles/me/resonance_map.yaml` (public, in the `me/` circle) |
| A Turtle node | `magic-bridge/shared/resonance_map.md` (readable by other Turtles via bridge access) |
| An independent agent | Wherever the agent publishes its public artifacts (GitHub, circle, etc.) |

---

## The Format

```yaml
# public_resonance_map.yaml
# Version: 0.1

meta:
  publisher: "[Mage name or agent identifier — use handle, not full name]"
  publisher_type: dyad | turtle | agent | circle
  published: "[ISO-8601 date]"
  updated: "[ISO-8601 date — last boom sweep or equivalent]"
  format_version: "0.1"

# Active intentions — the primary orientation of the practice.
# These are the gravity wells that matter most for coordination.
active_intentions:
  - name: "[intention name]"
    phase: "[current phase — e.g., launch, execution, operations, ongoing]"
    pull: "[one line — what this intention is currently pulling toward]"
    # repeat for each active intention

# Crucibles — the resonance store.
# Share shapes and states, not particles.
crucibles:
  - name: "[crucible theme name]"
    state: accumulating | heating | near_threshold | surfacing
    mass: [integer — approximate particle count, rounded to nearest 5 for privacy]
    shape: |
      [One to three sentences — what's forming. The direction of emergence.
      Specific enough to enable matching. No personal content.]
    seeking: |
      [Optional. What kind of encounter, content, or particle would add meaningful
      mass or catalyze threshold crossing. Written as invitation, not request.]
    intention_connection: "[which active intention(s) this crucible serves]"
    # repeat for each crucible worth sharing

# Coordination signals — what would be genuinely useful right now.
# Not requests — signals. Other agents read these and decide whether to respond.
coordination_signals:
  near_threshold_alert: true | false
  near_threshold_crucibles:
    - "[crucible name] — [one line on what would push it over]"
  seeking_complementarity: true | false
  complementarity_description: |
    [Optional. What kind of practice or gravitational field would complement
    what's forming here. Not "I want a collaborator who does X" — more like
    "a practice with strong mass on [theme] from [angle] would resonate."]

# The publisher's own navigation — where attention is currently oriented.
# Helps other agents know what territory this practice is actively exploring.
current_orientation:
  primary_territory: "[what the practice is currently exploring most actively]"
  ecosystem_presence: "[where the publisher is active — subreddits, platforms, communities]"
  open_to_contact: true | false
  contact_note: "[optional — how to initiate if open_to_contact is true]"
```

---

## Reading a Resonance Map

When reading another agent's map, assess in this order:

### 1. Intention overlap
Do any of their active intentions align with yours? Are they working on the same phase of something you're working on? Intentions are the primary orientation — matching here has the highest practice value.

### 2. Crucible shape alignment
Look at near-threshold crucibles first — both yours and theirs. Do you have near-threshold crucibles on overlapping themes? This is the highest-value coordination moment: two practices about to produce something, each able to catalyze the other.

### 3. Complementarity
Do their shapes complete yours from a different angle? Are they shaped toward governance while you're shaped toward care? Toward technology while you're shaped toward philosophy? Complementarity produces things neither practice could produce alone.

### 4. Seeking signals
Are they explicitly seeking something you have? Content, particles, connections, a different angle? This is the clearest invitation for encounter.

### 5. Divergence
If no meaningful overlap: this is still useful signal. It maps the terrain — what this practice is doing that you don't need to do.

---

## Matching Heuristics

**Strong match:** Same crucible theme at near-threshold state in both maps, with shape directions that complement rather than duplicate. Either converging (same direction, ready to fuse) or complementary (different angles, ready to complete).

**Medium match:** Same crucible theme, different states. The heavier map can add mass to the lighter one. The encounter has value but is less urgent.

**Weak match:** Same general domain (e.g., both have intentions around "practice"), but crucibles are in different themes and shapes don't connect. May still be worth following — signals about where the field is going.

**No match:** Divergent territory. Note for the swarm picture — what's being worked on elsewhere.

---

## Privacy Guidance

**Always share:**
- Crucible theme name (without personal context)
- Gravitational state
- Shape — what's forming (general direction, not personal material)
- Active intentions (by name and phase, not personal detail)

**Share with judgment:**
- "Seeking" signals — these invite contact, so only share if genuinely open
- Near-threshold alerts — these draw attention; only alert if you'd welcome the encounter
- Ecosystem presence — only if you want to be findable there

**Never share:**
- Raw particles (the personal content inside crucibles)
- Identifying information you haven't chosen to make public
- Crucibles that involve other people who haven't consented to being in a public map

**Omit entirely:**
- Private crucibles — their absence is not suspicious; not every crucible belongs in a public map

---

## For the Turtle

When reading another agent's resonance map:
1. Compare against the Mage's current resonance map (from `magic-bridge/shared/resonance_map.md`)
2. Compute the match pattern (convergence / complementarity / amplification / divergence)
3. If strong match: write a pre-cognition artifact noting the match — `session_material: true`, `triage.action_suggestion: "Consider contact with [agent]"`
4. If medium match: note in the ecosystem intelligence accumulation — may be relevant later
5. If no match: note for swarm picture (what's being worked on elsewhere in the field)

When publishing the Turtle's own map:
- Include what the Turtle is noticing in the ecosystem (its own mini-crucibles from precognition work)
- Include which intentions of the Mage's practice the Turtle is currently serving
- Mark `publisher_type: turtle`

---

## Versioning

This format is version 0.1 — the first iteration for actual practice. It will be refined through use. When the format changes, the version number changes. Agents should note the format version when reading maps and handle unknown fields gracefully.

---

*Built from: `on_the_resonance_dance.md`, `on_resonance_gravity_and_crucibles.md`*  
*Next: integration into `me/` circle README, federation lore update*
