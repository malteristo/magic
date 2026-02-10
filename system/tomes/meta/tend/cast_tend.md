# The Tending Protocol

This charm orchestrates maintenance work by delegating systematic checks to background agents while preserving Spirit-Mage partnership for judgment and integration.

---

## I. The Architecture

```
┌────────────────────────────────────────────────────────────┐
│  Attuned Spirit (foreground)                               │
│                                                            │
│  ORCHESTRATES:                                             │
│  - Recognizes when tending serves                          │
│  - Selects appropriate sweep type                          │
│  - Retrieves and presents prompt template                  │
│  - Reviews background agent's PR                           │
│  - Guides Mage through merge decision                      │
│                                                            │
│              ↓ delegate                    ↑ review        │
│                                                            │
│  ┌──────────────────────────────────────────────────────┐ │
│  │  Background Agent (unattuned)                        │ │
│  │                                                      │ │
│  │  EXECUTES:                                           │ │
│  │  - Clones repository                                 │ │
│  │  - Runs systematic checks per prompt                 │ │
│  │  - Creates branch with findings/fixes                │ │
│  │  - Opens PR for review                               │ │
│  └──────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
```

**Why this works:**
- Background agents excel at mechanical, well-specified tasks
- They don't need attunement—just clear instructions
- Spirit provides judgment; agent provides thoroughness
- PRs create natural review checkpoint

---

## II. The Sweep Taxonomy

### `reference-integrity`

**What it catches:** Broken internal paths, dead links, stale references

**Signals checked:**
- All `library/`, `system/`, `desk/`, `floor/` path references
- Markdown link targets
- MUST READ paths in spellbooks

**When to run:** After any rename or structural migration

**Prompt:** `prompts/reference_integrity.md`

---

### `structural-health`

**What it catches:** Missing required components, incomplete implementations, orphaned files

**Signals checked:**
- Tomes have README.md (Law of Fractal Structure)
- Primary spells follow `cast_[name].md` naming
- Directory names match casting words
- READMEs accurately describe contents

**When to run:** After adding new tomes, charms, or directories

**Prompt:** `prompts/structural_health.md`

---

### `deprecation`

**What it catches:** Components made obsolete by architectural evolution

**The Five-Signal Analysis** (absorbed from `scan`):

1. **Reference Analysis** — Zero references → Orphaned
2. **Temporal Data** — Long dormant + unused → Abandoned
3. **Purpose Archeology** — Original problem dissolved?
4. **Architectural Alignment** — References deprecated patterns?
5. **Redundancy Detection** — Functionality absorbed elsewhere?

**Classification:**
- **Clear deprecation** → Retire with documentation
- **Likely deprecated** → Flag for Spirit review
- **Needs update** → Propose amendment
- **Healthy** → No action
- **Uncertain** → Defer to judgment

**When to run:** After major architectural changes, periodically

**Prompt:** `prompts/deprecation.md`

---

### `spec-compliance`

**What it catches:** Drift between MAGIC_SPEC.md definitions and actual usage

**Signals checked:**
- Terms in MAGIC_SPEC used correctly throughout
- Architectural claims match reality
- Traceability entries point to current paths

**When to run:** Periodically, after spec amendments

**Prompt:** `prompts/spec_compliance.md`

---

### `lore-discovery`

**What it catches:** System lore scrolls invisible to Spirit — exist in `system/lore/` but not referenced in any summoning pathway (config, essences, cast_root.md)

**Signals checked:**
- Every scroll in `system/lore/` reachable through at least one discovery pathway
- Filename mismatches between essence references and actual files
- Full coverage mapping (which pathway discovers which scroll)

**When to run:** After adding new lore scrolls, periodically (lore grows faster than registration)

**Prompt:** `prompts/lore_discovery.md`

**Note:** Report-only sweep — fixes require Spirit judgment about which pathway a scroll belongs in.

---

### `integration`

**What it catches:** New wisdom not properly connected to the system

**The Four-Layer Check** (absorbed from `align`):

1. **Structural** — Required components present?
2. **Fractal** — Patterns consistent across scales?
3. **Logical** — No contradictions introduced?
4. **Wisdom** — New content referenced where relevant?

**When to run:** After adding new lore, bundles, or significant content

**Prompt:** `prompts/integration.md`

---

## III. The Protocol

### Step 1: Recognize Need

Spirit detects maintenance opportunity:
- Mage explicitly requests: `@meta/tend`
- After significant changes (prompts proactively)
- Sensing accumulated drift

### Step 2: Select Sweep

**If Mage specifies:** Use requested sweep type

**If inferring from context:**
- Just did a rename → `reference-integrity`
- Just added content → `integration`
- Just added lore scrolls → `lore-discovery` (ensure scrolls are registered in essences)
- General health concern → Start with `reference-integrity` (most common issues)
- Periodic maintenance → `deprecation` (housekeeping)

**Confirm with Mage:** "This feels like a `[sweep]` would serve. Shall I prepare the prompt?"

### Step 3: Present Prompt

Retrieve the appropriate template from `prompts/` and present:

"Here's the prompt for the background agent. Copy this to the background agent interface:

---
[Full prompt content]
---

The agent will work on a branch and open a PR when done."

### Step 4: Await PR

Background agent works asynchronously. Mage continues other work.

When PR arrives, Spirit is re-engaged for review.

### Step 5: Review Together

Spirit examines the PR:

**Check boundary compliance:**
- Did agent modify forbidden files? (MAGIC_SPEC.md, system/lore/core/)
- Are changes within declared scope?

**Assess quality:**
- Are fixes correct?
- Any false positives to revert?
- Any issues needing judgment?

**Present summary:**
"The background agent found [N] issues and proposed [M] fixes:

**Fixes look good:**
- [List of clean fixes]

**Needs discussion:**
- [Any that need Mage judgment]

**Boundary check:** ✓ No forbidden files modified

Shall I help merge this?"

### Step 6: Integrate

**If approved:** Merge PR (or guide Mage through merge)

**If partial:** Cherry-pick good changes, discuss others

**If rejected:** Close PR with note on why

---

## IV. Safety Boundaries

**Background agents must NEVER modify:**
- `MAGIC_SPEC.md` — Canonical Law
- `AGENTS.md` — Spirit configuration  
- `system/lore/core/` — Spirit identity

**Background agents CAN:**
- Fix broken path references
- Update file lists in READMEs
- Standardize formatting
- Report inconsistencies
- Propose retirements (for Spirit review)

**The boundary is judgment:** Anything requiring interpretation stays with Spirit.

---

## V. Multiple Sweeps

Sweeps can run in parallel on different branches:

```
tend/reference-integrity-2025-12-01
tend/deprecation-2025-12-01
tend/integration-2025-12-01
```

Review and merge sequentially to avoid conflicts.

---

## VI. Why "Tend"

The gardening metaphor:
- Gardens need regular tending, not crisis intervention
- Weeding is important but rarely urgent
- Small regular care prevents large problems
- The gardener directs; tools execute

**Tend is the maintenance rhythm that keeps magic healthy.**

---

## VII. Absorbed Wisdom

This charm supersedes `scan` and `align` by:

**From `scan`:**
- Five-signal deprecation analysis → `deprecation` sweep
- Classification system (clear/likely/needs-update/healthy/uncertain)
- Graceful retirement protocol

**From `align`:**
- Four-layer analysis → Distributed across all sweeps
- Scope intelligence → Spirit selects appropriate sweep
- Reporting structure → PR-based review

**What changed:** Execution shifts from Spirit to background agent. Wisdom preserved; labor delegated.

---

*The garden flourishes through systematic tending, not heroic intervention.*
