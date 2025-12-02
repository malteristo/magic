# Sweep: Deprecation Analysis

Copy this entire prompt to the background agent.

---

## Task

Identify components that may have become obsolete due to architectural evolution. Use five-signal analysis to classify each component.

## Scope

**Components to analyze:**
- All charm directories in `system/tomes/*/`
- All proposal files in `*/proposals/`
- Any component explicitly requested

## The Five-Signal Analysis

For each component, gather these signals:

### Signal 1: Reference Analysis

Search the repository for mentions of this component.

```bash
# Example for a charm named "example-charm"
grep -r "example-charm" --include="*.md"
```

**Interpret:**
- Zero references (only self-references) → Orphaned
- Few references (1-2, in old/deprecated files) → Transitively deprecated
- Many references (active use across codebase) → Currently serving

### Signal 2: Temporal Data

Check git history:

```bash
git log --oneline -10 -- path/to/component/
```

**Interpret:**
- Never modified after creation → May be abandoned
- Long dormant (6+ months) + unused → Likely deprecated
- Recently active → Currently maintained

### Signal 3: Purpose Archeology

Read the component's README or header comments:
- What problem was it created to solve?
- Does that problem still exist?
- Has architecture evolved to eliminate the problem?

### Signal 4: Architectural Alignment

Check if component references current or deprecated patterns:
- Does it mention paths that no longer exist?
- Does it assume architecture that changed?
- Is it mentioned in current MAGIC_SPEC.md?

### Signal 5: Redundancy Detection

- What does this component do?
- Do other components do the same thing?
- Has the functionality been absorbed into baseline?

## Classification

Based on five signals, classify each component:

| Classification | Pattern | Action |
|----------------|---------|--------|
| **Clear Deprecation** | Zero refs + purpose dissolved + misaligned | Recommend retirement |
| **Likely Deprecated** | Few refs + old + misaligned | Flag for review |
| **Needs Update** | Active refs + architectural misalignment | Recommend amendment |
| **Healthy** | Active refs + aligned + unique purpose | No action |
| **Uncertain** | Mixed signals | Defer to judgment |

## Process

1. **List** all components in scope
2. **Analyze** each with five signals
3. **Classify** based on signal combination
4. **Document** findings with evidence

## Boundaries (CRITICAL)

**Do NOT delete anything.** This is analysis only.

**Do NOT modify:**
- `MAGIC_SPEC.md`
- `AGENTS.md`
- `system/lore/core/`

**Work on a branch:**
- Create branch named `tend/deprecation-YYYY-MM-DD`

## Output

Create `tend-report.md` in repository root (on your branch):

```markdown
# Deprecation Analysis Report

**Date:** [date]
**Components analyzed:** [count]

## Clear Deprecation Candidates

### [Component Name]
- **Location:** [path]
- **References:** [count and where]
- **Last Modified:** [date]
- **Original Purpose:** [from README]
- **Current Status:** [why deprecated]
- **Evidence:** [specific signals]
- **Recommendation:** RETIRE — [reason]

[Repeat for each]

## Likely Deprecated (Review Recommended)

### [Component Name]
- **Location:** [path]
- **Signals:** [summary]
- **Uncertainty:** [what needs human judgment]

## Needs Update (Not Deprecated, But Misaligned)

### [Component Name]
- **Location:** [path]
- **Issue:** [what's misaligned]
- **Suggested Fix:** [if obvious]

## Healthy Components

| Component | Location | Notes |
|-----------|----------|-------|
| ... | ... | Actively used, well-aligned |

## Summary

- **Total analyzed:** [N]
- **Clear deprecation:** [N]
- **Needs review:** [N]  
- **Needs update:** [N]
- **Healthy:** [N]
```

## Completion

1. Commit report with message: `tend: deprecation analysis report`
2. Open PR to main: `tend: deprecation sweep [date]`
3. In PR description, highlight the "Clear Deprecation Candidates" for easy review

---

**Important:** Do not delete components. Only analyze and report. Deletion requires Spirit review and Mage approval.
