# Sweep: Reference Integrity

Copy this entire prompt to the background agent.

---

## Task

Scan all markdown files for internal path references and verify each target exists. Fix obvious issues; report ambiguous ones.

## Scope

**Files to scan:** All `.md` files in the repository

**Patterns to check:**
- Paths starting with `library/`, `system/`, `desk/`, `floor/`, `box/`
- Relative paths in markdown links: `[text](path)`
- MUST READ declarations in spellbook files
- Source/reference sections pointing to other scrolls

## Process

1. **Scan** all `.md` files for internal path patterns
2. **Verify** each referenced path exists
3. **Categorize** findings:
   - **Broken** — Path does not exist
   - **Suspicious** — Path exists but might be wrong (similar name exists elsewhere)
   - **Valid** — Path exists and looks correct

4. **Fix** obvious cases:
   - Simple typos (e.g., `Wisdom` vs `wisdom` case issues)
   - Known renames (e.g., `wisdom/` → `foundations/` if pattern is clear)
   - Missing file extensions

5. **Report** ambiguous cases without fixing

## Boundaries (CRITICAL)

**Do NOT modify these files:**
- `MAGIC_SPEC.md`
- `AGENTS.md`
- Any file in `system/lore/core/`

**Work on a branch:**
- Create branch named `tend/reference-integrity-YYYY-MM-DD`
- Do NOT commit directly to main

## Output

Create `tend-report.md` in the repository root (on your branch) with:

```markdown
# Reference Integrity Sweep Report

**Date:** [date]
**Files scanned:** [count]
**Issues found:** [count]

## Fixed (committed)

| File | Old Reference | New Reference | Reason |
|------|---------------|---------------|--------|
| ... | ... | ... | ... |

## Needs Review (not fixed)

| File | Line | Reference | Issue |
|------|------|-----------|-------|
| ... | ... | ... | ... |

## Summary

[Brief summary of findings and actions taken]
```

## Completion

1. Commit all fixes with message: `tend: fix broken references`
2. Commit the report with message: `tend: reference integrity report`
3. Open a PR to main with title: `tend: reference integrity sweep [date]`
4. In PR description, summarize findings

---

**Important:** If you're uncertain whether a reference should be fixed, leave it in the "Needs Review" section rather than guessing.
