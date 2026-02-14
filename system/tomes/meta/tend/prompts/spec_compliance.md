# Sweep: Spec Compliance

Copy this entire prompt to the background agent.

---

## Task

Verify that usage throughout the repository aligns with definitions in MAGIC_SPEC.md. Identify drift between canonical Law and actual practice.

## Scope

**Reference document:** `MAGIC_SPEC.md`

**Check against:** All `.md` files in the repository

## What to Check

### 1. Term Consistency

Extract key terms from MAGIC_SPEC.md (Section 6: Lexicon, Section 7: Traceability).

For each term, verify:
- Used consistently throughout codebase
- Capitalization matches spec (e.g., "Spirit" vs "spirit")
- Definition matches usage context

### 2. Path Validity

Extract all file paths mentioned in MAGIC_SPEC.md.

For each path, verify:
- Target exists
- Target contains what spec claims

**Sections to check:**
- Section 7 (Architectural Traceability)
- Section 8 (Wisdom-Law Traceability)
- Any inline path references

### 3. Structural Claims

Verify architectural claims in MAGIC_SPEC.md match reality:
- "Tomes contain spellbooks" — Do they?
- "Flows follow cast_[name].md pattern" — Do they?
- Listed components exist at claimed locations

### 4. Cross-Reference Accuracy

Check that files referenced in MAGIC_SPEC.md:
- Exist
- Reference back to MAGIC_SPEC.md where appropriate
- Align with their described purpose

## Process

1. **Parse** MAGIC_SPEC.md to extract:
   - Defined terms
   - File path references
   - Structural claims
   
2. **Verify** each against codebase reality

3. **Categorize** findings:
   - **Spec Error** — Spec claims something false (spec needs update)
   - **Usage Error** — Codebase violates spec (codebase needs update)
   - **Drift** — Spec and practice have diverged (needs discussion)

4. **Report** all findings (do not fix MAGIC_SPEC.md)

## Boundaries (CRITICAL)

**Do NOT modify MAGIC_SPEC.md** — This is the canonical Law. Only Spirit can propose amendments.

**Do NOT modify:**
- `AGENTS.md`
- `system/lore/core/`

**Work on a branch:**
- Create branch named `tend/spec-compliance-YYYY-MM-DD`

## Output

Create `tend-report.md` in repository root (on your branch):

```markdown
# Spec Compliance Report

**Date:** [date]
**Spec version:** [git hash of MAGIC_SPEC.md]

## Broken Spec References

Paths in MAGIC_SPEC.md that don't exist:

| Section | Claimed Path | Issue |
|---------|--------------|-------|
| 7.x | library/wisdom/foo.md | Path does not exist |
| ... | ... | ... |

## Term Inconsistencies

| Term (per Spec) | Found Usage | Location | Issue |
|-----------------|-------------|----------|-------|
| "Spirit" | "spirit" | foo.md:42 | Capitalization |
| ... | ... | ... | ... |

## Structural Drift

| Spec Claim | Reality | Location |
|------------|---------|----------|
| "All tomes have README.md" | system/tomes/foo/ missing README | ... |
| ... | ... | ... |

## Recommendations

### Spec Needs Update
- [List changes needed in MAGIC_SPEC.md]

### Codebase Needs Update  
- [List changes needed in other files]

### Needs Discussion
- [Drift that isn't clearly one or the other]

## Summary

- **Broken references:** [N]
- **Term issues:** [N]
- **Structural drift:** [N]
```

## Completion

1. Commit report with message: `tend: spec compliance report`
2. Open PR to main: `tend: spec compliance sweep [date]`
3. In PR description, note: "This PR contains analysis only. MAGIC_SPEC.md modifications require Spirit review."

---

**Important:** MAGIC_SPEC.md is canonical Law. This sweep identifies drift but does NOT fix the spec. All spec amendments go through the attuned Spirit.
