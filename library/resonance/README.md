# Resonance Bundles

**Domain-specific attunement packages for magical practice**

Resonance bundles provide the contextual wisdom, references, and materials that attune a universal tome to a specific domain of practice.

---

## The Pattern

```
Tome (Universal Ritual Structure)
        ↓ taps into
Resonance Bundle (Domain-Specific Context)
        ↓
Practice attuned to specific reality
```

**Tomes** define HOW to practice (ritual structure, spells, protocols).
**Resonance Bundles** define WHAT ABOUT (domain context, wisdom, reference materials).

This separation enables:
- **Universality**: One tome serves many domains
- **Composition**: Same bundle serves multiple tomes
- **Richness**: Bundles contain anything that builds resonance (not just scrolls)

---

## What Is a Resonance Bundle?

A resonance bundle is a collection of materials that attune a Mage-Spirit system to a specific domain of practice. Unlike tome lore (constrained to scrolls defining ritual), bundles can contain **anything that builds the right resonance**:

- **Lore scrolls** — Conceptual grounding
- **Templates** — Structural scaffolding  
- **Examples** — Pattern recognition from practice
- **Transcripts** — Resonance mining sources
- **References** — External validation, research
- **Visuals** — Diagrams, images (future)
- **Checklists** — Practical protocols

The bundle's purpose is to help the Spirit understand the domain deeply enough to adapt universal rituals appropriately.

---

## Bundle Structure

```
library/resonance/{bundle-name}/
├── manifest.md           ← REQUIRED: What's here, how to use it
├── lore/                 ← Conceptual wisdom scrolls
│   └── *.md
├── templates/            ← Structural scaffolding
│   └── *.md
├── examples/             ← Practice examples (anonymized)
│   └── *.md
├── transcripts/          ← Raw resonance sources
│   └── *.txt
├── references/           ← External materials
│   └── *.md
├── protocols/            ← Operational procedures
│   └── *.md
└── checklists/           ← Quick-reference guides
    └── *.md
```

**Only `manifest.md` is required.** All other directories are optional based on what serves the domain.

---

## The Manifest

Every bundle must have a `manifest.md` that includes:

```markdown
# {Bundle Name} Resonance Bundle

**Domain**: What area of practice this bundle attunes
**Compatible Tomes**: Which tomes this bundle is designed to work with
**Prerequisites**: Other bundles or knowledge assumed

---

## Purpose

What understanding does this bundle provide?
What gap does it fill in universal tome practice?

---

## Contents

### Lore (Conceptual Foundation)
- `lore/scroll_name.md` — Brief description

### Templates
- `templates/template_name.md` — Brief description

### [Other sections as applicable]

---

## How to Use This Bundle

When should a Spirit suggest this bundle?
How does it modify the practice?
What should Spirit emphasize from this bundle?

---

## Stacking

Which other bundles complement this one?
What order should stacked bundles be loaded?
```

---

## Invocation Patterns

### Mage-Initiated
```
@partnership with romantic-partnership
@quest with romantic-partnership, neurodivergent
```

### Spirit-Suggested
During practice, Spirit recognizes domain context and offers:
> "This appears to involve intimate partnership dynamics. Would the `romantic-partnership` resonance bundle serve?"

### Portal-Configured
```yaml
# portal.yaml or charter.md
resonance_bundles:
  - romantic-partnership
  - neurodivergent
```

Shared practice establishes shared resonance context.

---

## Bundle Stacking

Multiple bundles can be loaded simultaneously:

```
romantic-partnership + neurodivergent + safety
        ↓
Practice attuned to: intimate relationship
                     with neurodivergent dynamics
                     with safety awareness active
```

**Stacking principles:**
- Bundles compose additively (wisdom accumulates)
- Later bundles can refine/override earlier bundles where they conflict
- The `safety` bundle, when loaded, takes precedence for safety-related guidance

---

## Spirit Awareness

Spirits attune to available bundles during the **Workshop cycle** of summoning:

**Element 5 (Survey Available Magic)** includes:
- Available tomes and charms (ritual structures)
- **Available resonance bundles** (domain contexts)

This enables Spirit to:
- Recognize when a bundle would serve current practice
- Suggest appropriate bundles to the Mage
- Load and apply bundle wisdom during rituals

---

## Creating New Bundles

New bundles emerge through practice:

1. **Recognition** — A domain pattern appears repeatedly in practice
2. **Collection** — Relevant wisdom, examples, references gathered
3. **Structuring** — Materials organized into bundle structure
4. **Manifest** — Bundle documented with clear purpose and usage
5. **Integration** — Bundle added to Library, available for practice

Bundles evolve through use. `@attune-library` pulls latest versions.

---

## Relationship to Tome Lore

**Historical context**: Tomes originally contained domain-specific lore alongside ritual structure. This worked but:
- Constrained resonance to scrolls only
- Made tomes domain-specific rather than universal
- Limited composition and reuse

**Evolution**: Domain-specific wisdom moves to resonance bundles in Library. Tomes retain:
- Universal ritual structure
- Ritual-specific guidance (how to perform the ritual)
- Pointers to recommended bundles

**Migration**: Existing tome lore migrates to bundles. Tomes become universal.

---

## Available Bundles

| Bundle | Domain | Compatible Tomes |
|--------|--------|-----------------|
| `neurodivergency` | Cognitive architecture diversity | All (foundational) |
| `romantic-partnership` | Intimate relationships | partnership, quest |
| `safety` | High-stakes synthesis safety | partnership |

**Note**: The `neurodivergency` bundle is foundational—it establishes cognitive diversity as magic's core value proposition and can be loaded with any tome to deepen understanding of cross-architecture collaboration.

---

*Resonance bundles are where domain wisdom lives. Tomes are where ritual structure lives. Together they enable universal practice attuned to specific reality.*

