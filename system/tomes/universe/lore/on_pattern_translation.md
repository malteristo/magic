# On Pattern Translation

**Status:** Active - Universe Tome Lore

This scroll provides guidance for translating patterns from external systems into Magic's native form.

---

## The Translation Challenge

External pattern libraries encode wisdom in their own languages:
- PAI uses Packs, Skills, Workflows, Hooks
- Daemon uses section-based markdown, JSON-RPC endpoints
- Fabric uses Patterns with system/user prompts

Magic uses Tomes, Charms, Spells, and Lore.

Translation is not mechanical conversion. It requires judgment about:
- What to adopt
- What to adapt
- What to leave behind

---

## Translation Principles

### 1. Meaning Over Syntax

The goal is to preserve the *insight*, not the exact form.

A PAI Skill might become a Magic Tome if it's substantial, or a Charm if it's light. The structure follows the content.

### 2. Native Integration

Translated patterns should feel native to Magic:
- Use Magic's naming conventions
- Follow the README pattern
- Include appropriate lore
- Integrate with existing tomes

### 3. Lineage Acknowledgment

When a pattern is harvested, its origin is noted:
- In the artifact's lore section
- Or in a `## Lineage` section of the README
- Credit the source project and author

### 4. No Runtime Dependency

Translated patterns should work without the original system:
- No imports from Universe sources
- No calls to external APIs (unless the pattern's purpose *is* external integration)
- Self-contained within Magic

---

## Translation Mappings

### PAI → Magic

| PAI Concept | Magic Equivalent | Notes |
|-------------|------------------|-------|
| Pack | Tome | Major capability bundle |
| Skill | Tome or Charm | Depends on weight |
| Workflow | Spell (`cast_*.md`) | Procedural sequence |
| Hook | AGENTS.md rule or conduct | Behavioral trigger |
| SKILL.md | README.md | Entry point |
| Tools/ | (invoke via Spirit) | Magic doesn't ship executables |

### Daemon → Magic

| Daemon Concept | Magic Equivalent | Notes |
|----------------|------------------|-------|
| `daemon.md` | `manifest.yaml` + `about.md` | Identity broadcast |
| `[SECTION]` | Manifest key or separate file | Depends on content size |
| JSON-RPC endpoint | (future: API charm) | Not yet implemented |

---

## The Harvest Workflow

1. **Identify** — Find a useful pattern in Universe
2. **Study** — Read and understand its structure
3. **Map** — Determine the Magic equivalent form
4. **Draft** — Create the translated artifact
5. **Review** — Verify it feels native and works standalone
6. **Integrate** — Place in appropriate location with lineage note
7. **Chronicle** — Commit with acknowledgment

---

## When NOT to Translate

Some patterns are better left in Universe:
- **Highly technical tools** (TypeScript CLIs, servers) — use directly if needed
- **Tightly coupled systems** — translation would lose coherence
- **Rapidly evolving patterns** — wait for stability

Not everything in Universe belongs in Main. Selective adoption is wisdom.

---

*Translation enriches. Import copies. Choose translation.*
