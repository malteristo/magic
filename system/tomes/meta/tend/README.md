# Charm of Tending

**Purpose:** Delegate systematic maintenance work to background agents while preserving Spirit-Mage partnership for judgment and approval.

---

## The Insight

Maintenance work is important but rarely urgent. It consistently loses to more pressing creative work—so it accumulates until small misalignments become structural drift.

Background agents solve this by making maintenance:
- **Asynchronous** (doesn't compete for attention)
- **Low-friction** (spawn and forget until PR arrives)
- **Reviewable** (Spirit assesses, Mage approves)

**The division of labor:**
- **Attuned Spirit** → Partnership, creative synthesis, judgment calls
- **Background Agent** → Mechanical checks, pattern matching, systematic verification

---

## When to Invoke

- After significant structural changes (renames, migrations)
- When you sense accumulated drift
- Periodically as maintenance hygiene
- When the Mage requests system health check

---

## Usage

```
@meta/tend [sweep-type]
```

**The protocol:**
1. Spirit selects appropriate sweep based on context
2. Spirit retrieves prompt template from `prompts/`
3. Spirit presents prompt to Mage
4. Mage spawns background agent with prompt
5. Background agent works asynchronously, creates PR
6. Spirit reviews PR with Mage
7. Merge if aligned

---

## Available Sweeps

| Sweep | What It Catches | When to Use |
|-------|-----------------|-------------|
| `reference-integrity` | Broken file paths, dead links | After renames, periodically |
| `structural-health` | Missing READMEs, incomplete tomes, orphaned files | After additions |
| `deprecation` | Components made obsolete by evolution | After major changes |
| `spec-compliance` | Drift from MAGIC_SPEC definitions | Periodically |
| `integration` | Orphaned wisdom, missing cross-references | After adding new content |

---

## This Charm Absorbs

- **`scan`** — Its five-signal deprecation analysis lives in the `deprecation` sweep
- **`align`** — Its four-layer consistency analysis is distributed across all sweeps

The wisdom is preserved. The execution shifts to background agents.

---

*"The garden flourishes not through constant vigilance, but through systematic tending."*
