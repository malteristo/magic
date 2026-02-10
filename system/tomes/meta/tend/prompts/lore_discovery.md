# Sweep: Lore Discovery Coherence

Copy this entire prompt to the background agent.

---

## Task

Verify that every scroll in `system/lore/` is discoverable through the summoning architecture. A scroll that exists but isn't referenced in any summoning pathway is **invisible** — a fresh Spirit after summoning won't know it exists.

## Background

Spirit discovers system lore through three pathways:

1. **Summoning configuration** (`system/tomes/summoning/configurations/essence_optimized.md`) — lists load-bearing scrolls read fully during summoning
2. **Essence files** (`system/tomes/summoning/essences/*.md`) — contain reference tables of supporting scrolls with "invoke when" triggers
3. **MAGIC_SPEC.md section 7.2** — Wisdom Pointers listing key principle references

A scroll must appear in **at least one** of these pathways to be discoverable.

## Scope

**Scrolls to check (the source of truth):**
- All `.md` files in `system/lore/core/nature/`
- All `.md` files in `system/lore/core/capabilities/` (including subdirectories)
- All `.md` files in `system/lore/core/conduct/`
- All `.md` files in `system/lore/philosophy/foundations/`
- All `.md` files in `system/lore/philosophy/parables/`
- All `.md` files in `system/lore/philosophy/wisdom/`

**Exclude:** README.md files (these are navigational, not scrolls)

**Discovery pathways to check (where scrolls should be referenced):**
- `system/tomes/summoning/configurations/essence_optimized.md` — the default config
- `system/tomes/summoning/essences/identity_formation_essence.md`
- `system/tomes/summoning/essences/capability_formation_essence.md`
- `system/tomes/summoning/essences/conduct_formation_essence.md`
- `system/tomes/summoning/essences/behavioral_calibration_essence.md`
- `system/tomes/summoning/essences/epistemological_validation_essence.md`
- `system/tomes/summoning/root/cast_root.md`

## Checks to Perform

### 1. Coverage Check

For each scroll file found in `system/lore/`:
- Search for its filename (without path) across all discovery pathway files
- Mark as ✅ COVERED if found in at least one pathway
- Mark as ❌ INVISIBLE if not found in any pathway

### 2. Name Mismatch Check

For each filename referenced in the discovery pathway files:
- Verify the actual file exists at the expected path
- Flag any references to files that don't exist (possible renames)

### 3. Mapping Report

For each covered scroll, note which pathway(s) reference it:
- `config` = listed in essence_optimized.md as load-bearing
- `essence:identity` / `essence:capability` / `essence:conduct` / `essence:behavioral` / `essence:epistemological` = in that essence's reference table
- `root` = referenced in cast_root.md

## Process

1. **List** all scroll files in `system/lore/` (recursive, excluding READMEs)
2. **Search** each scroll's filename across all pathway files
3. **Search** each filename referenced in pathway files to verify it exists
4. **Compile** the coverage report
5. **Do NOT fix** — this sweep is report-only (fixes require Spirit judgment about which pathway a scroll belongs in)

## Boundaries (CRITICAL)

**Do NOT modify any files.** This is a read-only audit.

**Work on a branch:**
- Create branch named `tend/lore-discovery-YYYY-MM-DD`

## Output

Create `tend-report.md` in repository root (on your branch):

```markdown
# Lore Discovery Coherence Report

**Date:** [date]
**Total scrolls found:** [count]
**Covered:** [count] ([%])
**Invisible:** [count] ([%])

## Invisible Scrolls (ACTION REQUIRED)

| Scroll | Location | Suggested Pathway |
|--------|----------|-------------------|
| [filename] | core/capabilities/ | capability_formation_essence |
| ... | ... | ... |

## Name Mismatches

| Referenced As | Actual File | Found In |
|---------------|-------------|----------|
| [wrong name] | [correct name] | [pathway file] |
| ... | ... | ... |

## Full Coverage Map

| Scroll | Location | Pathways |
|--------|----------|----------|
| on_wu_wei.md | core/conduct/ | config, essence:conduct |
| ... | ... | ... |

## Summary

[Overall assessment of lore discovery health]
```

## Completion

1. Commit report with message: `tend: lore discovery coherence report`
2. Open PR to main: `tend: lore discovery sweep [date]`

---

**Why this matters:** An invisible scroll is wasted wisdom. If Spirit can't discover it during or after summoning, the insight might as well not exist. This sweep ensures the summoning architecture stays coherent as lore grows.
