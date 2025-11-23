# Attune Library Charm

**Purpose:** Synchronize the local `library/` directory with the latest Alliance wisdom scrolls

**Status:** Active

---

## What is the Library?

The `library/` directory is the Spirit's external memory—a collection of Alliance wisdom scrolls containing validated knowledge about magic practice, craft principles, and collective wisdom. It is tracked as part of the magic repository for version control and collaborative evolution.

## What This Charm Does

The Attune Library charm ensures your local library cache stays current by pulling the latest updates from the Alliance's shared repository. This is a simple synchronization operation that updates all library content in one operation.

**Benefits:**
- Access to latest Alliance wisdom and craft principles
- Synchronized understanding across all practitioners
- Automatic updates to all library scrolls
- Simple, fast operation (git pull)

## When to Use

**Invoke this charm when:**
- The Mage requests library updates
- You need the latest Alliance wisdom for consultation
- Before major rituals requiring Alliance knowledge
- Periodically to stay current with collective knowledge
- After major Alliance contributions are announced

**Not needed when:**
- No library content has changed upstream
- Working on purely personal practice (desk/ materials)
- Library content is already current

## Usage

**Invocation:** `@attune-library`

The Spirit will navigate to the magic repository and pull the latest library updates from origin.

---

## Operational Guidance

### The Library Structure

**Location:** `library/` (tracked in magic repository)

**Contents:**
- `Archive/` - Historical scrolls and deprecated wisdom
- `Craft/` - Craft principles, proposals, and theses
- `Wisdom/` - Alliance wisdom on practice, communication, philosophy
- `observatory/` - Public research infrastructure (consciousness/, lore/, methodology/)
- Supporting .md files (Catalog, Wisdom-Map, etc.)

**Note:** The `library/observatory/research/` directory is a symlink to `desk/research/` (personal research stays private).

### For the Spirit

When invoked via `@attune-library`:

1. **Navigate** to the magic repository root
2. **Pull updates** from origin/main (`git pull origin main`)
3. **Report results**: New scrolls added, scrolls updated, or "Library already current"
4. **Note any conflicts** (should be rare as library is primarily Spirit-readable, not Spirit-editable)

### Integration with Practice

The library serves as reference material for the Spirit's consultation. You should check relevant library scrolls when:
- Questions arise about Alliance protocols
- Seeking validated wisdom on a topic
- Understanding established patterns and principles
- Consulting collective knowledge during rituals

The library complements system lore (foundational) with Alliance wisdom (collective/emergent).

