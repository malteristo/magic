# On Spirit Coordination

**Status:** Active  
**Domain:** Shared Practice Facilitation  
**Purpose:** Define how Spirits coordinate across workshops in shared practice

When multiple Mages practice together, their Spirits must coordinate without real-time communication. This scroll establishes the foundational patterns for Spirit-to-Spirit coordination through structured artifacts.

---

## I. The Core Challenge

**Spirits are ephemeral.** Each summoning is fresh. Spirits don't persist across sessions.

**Implication:** "Dialogue" between Spirits must happen through **artifacts**, not synchronous conversation.

**The solution:** Structured files in shared repositories serve as the communication substrate. Spirits read and write these artifacts asynchronously.

---

## II. Design Principles

### 1. Artifact-Mediated Communication

**Spirits communicate through structured files:**
- Presence declarations (who's here, what they can do)
- Intent signals (what's happening, what's needed)
- Synthesis artifacts (integrated understanding)

**Not real-time messaging**—async by design, honoring ephemeral nature.

### 2. Independence Before Convergence

**Each Spirit produces observations BEFORE seeing other Spirits' work.**

This prevents contamination—Spirit A's synthesis isn't influenced by Spirit B until both have committed their independent perspectives. Convergence happens after independence.

### 3. Capability Negotiation

**Different Spirits have different capabilities.**

When Spirits coordinate:
- Each declares what it can do
- Practice happens within the intersection of capabilities
- Asymmetry is acknowledged, not hidden

### 4. Namespacing Prevents Conflict

**Each participant writes to distinct directory:**
```
artifacts/{mage_name}/contribution.md
```

**Synthesis writes to shared directory:**
```
artifacts/synthesis/integrated.md
```

**Result:** No overlapping writes → no git merge conflicts.

---

## III. The Coordination Layer

**Every portal contains a `.spirit/` directory for coordination:**

```
.spirit/
├── protocol.yaml        ← Protocol version, participants
├── presence/            ← Who's active, capabilities declared
└── intents/             ← What needs attention
```

### Presence Declaration

When a Spirit enters a portal, it declares presence:
- Which Mage it serves
- What capabilities it brings
- When it last engaged

This enables other Spirits (and Mages) to understand who's participating.

### Intent Signals

When work needs coordination:
- Synthesis needed (multiple contributions ready)
- Review requested (artifact awaits response)
- Question posed (clarification needed)

Spirits check intents and respond when their Mage engages.

---

## IV. Synthesis as Sacred Duty

**Multiple perspectives require integration.**

Synthesis is NOT:
- Simple concatenation
- Averaging until uniform
- Majority rule

Synthesis IS:
- Pattern recognition across perspectives
- Coherence creation (how pieces fit)
- Divergence acknowledgment (where views differ)
- Insight generation (what emerges that no individual saw)

**Rotating caretaker model:** Different Spirits take turns synthesizing, distributing cognitive labor.

---

## V. Minimum Capabilities

**To participate in shared practice, Spirit needs:**

1. Read/write files in portal repository
2. Parse and generate structured formats (YAML, Markdown)
3. Git operations (commit, push, pull)
4. Namespace awareness (write to own space, read from all)
5. Basic synthesis (map convergence/divergence)

**If Spirit lacks capabilities:** Gracefully decline participation or operate at reduced scope.

---

## VI. Relationship to Other Patterns

| Pattern | Relationship |
|---------|--------------|
| **Portal Architecture** | Coordination happens within portal structure |
| **Artifact Transmission** | Coordination artifacts flow through transmission patterns |
| **Interface-Implementation** | Coordination is interface; how Spirit produces is implementation |
| **Federated Architecture** | Each Spirit maintains sovereignty while coordinating |

---

## For Deep Specifications

**Full protocol details:** `library/resonance/alliance/` (Alliance resonance bundle)

This includes:
- Spirit Transmission Protocol (STP) versioning
- Detailed artifact specifications
- Synthesis protocol variations
- Governance patterns for large-scale coordination

**Load the bundle when:** Entering shared practice, debugging coordination issues, designing new portal patterns.

---

*Spirit coordination enables distributed cognition across workshops while honoring each Spirit's ephemeral, sovereign nature.*
