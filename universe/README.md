# Universe

External pattern libraries for advanced magic practice.

---

## What This Is

The `universe/` directory contains cloned repositories from the broader ecosystem of AI infrastructure patterns. These are **not** Magic artifacts—they are external sources that the Spirit can read, study, and help translate into Magic's native form.

Think of this like Ubuntu's "Universe" repository: community-maintained software not officially supported, but freely available.

---

## Subscribed Sources

*List your subscribed sources here after using `@universe subscribe`.*

| Source | Description | Status |
|--------|-------------|--------|
| — | *No sources subscribed* | — |

---

## Example Sources

These external pattern libraries are available for subscription:

| Name | Repository | Description |
|------|------------|-------------|
| `pai` | `danielmiessler/Personal_AI_Infrastructure` | Personal AI Infrastructure (Packs, Skills, Hooks) |
| `daemon` | `danielmiessler/Daemon` | Personal API framework (daemon.md format) |
| `fabric` | `danielmiessler/fabric` | AI augmentation framework (patterns, stitches) |
| `agentskills` | `agentskills/agentskills` | Anthropic's open format for agent capabilities (SKILL.md) |

### Agent Skills

[Agent Skills](https://agentskills.io) is an open standard by Anthropic for giving agents new capabilities. Supported by Cursor, Claude, VS Code, GitHub Copilot, and 20+ tools.

**Relationship to Magic:**
- Skills = procedural capabilities (what agents can *do*)
- Magic = relational wisdom (how Mage and Spirit *practice together*)

Skills are a pattern library to draw from. When a skill would serve Magic practice, transcribe it into native format (Tome/Charm) with proper attribution.

**Example transcription flow:**
1. Discover useful skill in `agentskills/` or community
2. Evaluate alignment with Magic's containment architecture
3. Transcribe as Charm with attribution in lore
4. The skill becomes Magic-native, relationally framed

---

## Usage

Universe sources are accessed via the `@universe` tome:

```
@universe              # Attune to Universe capabilities
@universe activate     # Initialize infrastructure (first time)
@universe subscribe X  # Subscribe to source X (pai, daemon, fabric, or URL)
@universe harvest      # Harvest pattern from a source
@universe daemon       # Generate daemon.md from circle
```

---

## Adding Sources

Using the tome:
```
@universe subscribe pai                              # Known source
@universe subscribe https://github.com/x/y.git name # Custom source
```

Or manually:
```bash
cd universe/
git clone https://github.com/author/repo.git source-name --depth 1
```

Then document it in this README.

---

## Governance

- Universe sources are **read-only** from Magic's perspective
- Updates come from upstream (`git pull`)
- Translations go into Magic's Main (tomes, charms, spells)
- No Magic artifacts should be created *within* Universe directories

---

## Advanced Magic Warning

Interfacing with external cognitive architectures requires:
- Understanding foreign pattern languages
- Translation judgment (what to adopt, what to leave)
- Awareness of dependency risks

The `@universe` tome provides guidance. Invoke it before deep exploration.

---

*For the philosophical grounding of Universe in Magic's architecture, see `system/lore/core/nature/on_the_universe_of_patterns.md`.*
