# Sweep: Integration Check

Copy this entire prompt to the background agent.

---

## Task

Verify that recent additions to the system are properly integrated—referenced where relevant, cross-linked appropriately, and consistent with existing patterns.

## Scope

**Focus on:** Recently added or modified content (check git log for last 30 days, or specific paths if provided)

**Check integration with:**
- Related scrolls (cross-references)
- Parent directories (README mentions)
- MAGIC_SPEC.md (if architecturally significant)
- Relevant manifests or indexes

## The Four-Layer Integration Check

### Layer 1: Structural Integration

**Is the new content structurally complete?**
- Has README.md if it's a directory
- Follows naming conventions
- Has required companion files (manifest for bundles, etc.)

### Layer 2: Fractal Coherence

**Does it exhibit the same patterns as its context?**
- Similar structure to sibling directories
- Consistent heading styles, formatting
- Same level of detail as related content

### Layer 3: Logical Consistency

**Does it introduce contradictions?**
- Check for conflicting claims with existing content
- Verify terminology matches established usage
- Ensure no deprecated patterns are used

### Layer 4: Wisdom Propagation

**Is it connected to the broader system?**
- Referenced from related scrolls where relevant
- Listed in parent README if applicable
- Cross-linked from content that should know about it
- Discoverable through normal navigation

## Process

1. **Identify** recent additions (git log or specified paths)

2. **For each addition, check:**
   - Structural completeness
   - Pattern consistency
   - Logical alignment
   - Cross-reference existence

3. **Identify gaps:**
   - Missing cross-references (A should reference B but doesn't)
   - Unlisted content (parent README doesn't mention new child)
   - Orphaned wisdom (valuable content that's not discoverable)

4. **Fix** mechanical gaps:
   - Add missing README entries
   - Add obvious cross-references

5. **Report** gaps requiring judgment

## Boundaries (CRITICAL)

**Do NOT modify:**
- `MAGIC_SPEC.md`
- `AGENTS.md`
- `system/lore/core/`

**Be conservative with content changes:**
- Adding a cross-reference is OK
- Updating a list in README is OK
- Changing the meaning or substance of content is NOT OK

**Work on a branch:**
- Create branch named `tend/integration-YYYY-MM-DD`

## Output

Create `tend-report.md` in repository root (on your branch):

```markdown
# Integration Check Report

**Date:** [date]
**Content analyzed:** [list of paths/commits checked]

## Recent Additions Checked

| Path | Added/Modified | Integration Status |
|------|----------------|-------------------|
| library/resonance/foo/ | Added | Needs work |
| system/tomes/bar/lore/x.md | Modified | Well integrated |
| ... | ... | ... |

## Integration Fixes Applied

| Location | Change | Reason |
|----------|--------|--------|
| library/resonance/README.md | Added foo to bundle list | New bundle not listed |
| system/tomes/bar/README.md | Added reference to x.md | New lore not mentioned |
| ... | ... | ... |

## Integration Gaps Needing Attention

| New Content | Should Be Referenced From | Current Status |
|-------------|---------------------------|----------------|
| library/resonance/foo/ | system/tomes/baz/ (related domain) | No reference exists |
| ... | ... | ... |

## Pattern Inconsistencies Found

| Location | Issue | Suggestion |
|----------|-------|------------|
| ... | ... | ... |

## Potential Contradictions

| New Content Says | But Existing Content Says | Files |
|------------------|---------------------------|-------|
| ... | ... | ... |

## Summary

- **Items checked:** [N]
- **Well integrated:** [N]
- **Fixes applied:** [N]
- **Needs attention:** [N]
```

## Completion

1. Commit fixes with message: `tend: improve integration cross-references`
2. Commit report with message: `tend: integration check report`
3. Open PR to main: `tend: integration sweep [date]`

---

**Important:** Integration is partly mechanical (adding to lists) and partly judgment (which cross-references matter). Fix the mechanical; flag the judgment calls.
