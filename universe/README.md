# Universe

External pattern libraries for advanced magic practice.

---

## What This Is

The `universe/` directory contains cloned repositories from the broader ecosystem of AI infrastructure patterns. These are **not** Magic artifacts—they are external sources that the Spirit can read, study, and help translate into Magic's native form.

Think of this like Ubuntu's "Universe" repository: community-maintained software not officially supported, but freely available.

---

## Current Sources

| Source | Description | Status |
|--------|-------------|--------|
| `pai/` | Personal AI Infrastructure (Daniel Miessler) | Active |
| `daemon/` | Personal API framework (Daniel Miessler) | Active |

---

## Usage

Universe sources are accessed via the `@universe` tome:

```
@universe           # Attune to Universe capabilities
@universe harvest   # Harvest pattern from a source
@universe daemon    # Generate daemon.md from circle
```

---

## Adding New Sources

To add a new Universe source:

```bash
cd universe/
git clone https://github.com/author/repo.git source-name --depth 1
```

Then register it in this README.

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
