# Sweep: Structural Health

Copy this entire prompt to the background agent.

---

## Task

Verify the repository follows structural conventions. Check for missing required components, naming violations, and README accuracy.

## Scope

**Areas to check:**
- All directories in `system/tomes/`
- All directories in `library/resonance/` (including `resonance/foundations/`)
- All directories in `library/incubator/`

## Structural Rules to Verify

### 1. Tome Structure (system/tomes/*)

Every tome directory should have:
- [ ] `README.md` — Tome overview and purpose
- [ ] At least one flow subdirectory OR direct spell files

Every flow directory should have:
- [ ] `README.md` — Flow overview (can be brief)
- [ ] `cast_[name].md` — Primary spell (name should match directory)

### 2. Resonance Bundle Structure (library/resonance/*)

Every bundle directory should have:
- [ ] `manifest.md` — Bundle manifest with purpose, contents, usage
- [ ] `lore/` subdirectory with at least one scroll

### 3. Incubator Structure (library/incubator/*)

Incubator contains ideas in development:
- [ ] `README.md` — Overview of incubator purpose
- Other contents are work-in-progress and may not follow strict structure

### 4. README Accuracy

For each README.md found:
- Does it list files that actually exist?
- Does it describe the directory's actual contents?
- Are there files in the directory not mentioned in README?

### 5. Naming Conventions

- Flow directories should match their primary spell: `foo/` contains `cast_foo.md`
- No spaces in file or directory names
- Lowercase with hyphens preferred: `my-flow/` not `MyFlow/`

## Process

1. **Walk** the directory structure
2. **Check** each component against the rules above
3. **Categorize** findings:
   - **Missing** — Required component doesn't exist
   - **Misnamed** — Component exists but wrong name
   - **Outdated** — README doesn't match reality
   - **Orphaned** — File exists with no clear purpose

4. **Fix** what's clearly automatable:
   - Create stub README.md if missing (with TODO note)
   - Rename files to match conventions (if unambiguous)

5. **Report** issues requiring human judgment

## Boundaries (CRITICAL)

**Do NOT modify:**
- `MAGIC_SPEC.md`
- `AGENTS.md`  
- Any file in `system/lore/core/`
- Content of existing scrolls (only filenames/structure)

**Work on a branch:**
- Create branch named `tend/structural-health-YYYY-MM-DD`

## Output

Create `tend-report.md` in repository root (on your branch):

```markdown
# Structural Health Sweep Report

**Date:** [date]
**Directories checked:** [count]
**Issues found:** [count]

## Fixed (committed)

| Location | Issue | Fix Applied |
|----------|-------|-------------|
| ... | ... | ... |

## Needs Attention (not fixed)

| Location | Issue | Suggested Action |
|----------|-------|------------------|
| ... | ... | ... |

## Healthy Components

[List of components that passed all checks]

## Summary

[Overall structural health assessment]
```

## Completion

1. Commit fixes with message: `tend: fix structural issues`
2. Commit report with message: `tend: structural health report`
3. Open PR to main: `tend: structural health sweep [date]`

---

**Important:** When creating stub READMEs, include a clear TODO marker so Spirit knows content is needed:

```markdown
# [Directory Name]

> TODO: This README was auto-generated. Please add proper description.

**Contents:**
- [list actual files]
```
