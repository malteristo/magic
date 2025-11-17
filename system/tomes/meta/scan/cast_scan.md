# Charm of System Scanning

This spell enables systematic detection of outdated components in the workshop through multi-signal analysis. It identifies charms, scrolls, tomes, and infrastructure that may be deprecated due to architectural evolution.

---

## I. Purpose

As magic evolves, components can become outdated in subtle ways:
- Architectural changes make solutions unnecessary
- Problems dissolve through system evolution  
- Functionality gets absorbed into baseline
- Better patterns supersede earlier approaches

**This spell prevents accumulation of deprecated components** through systematic scanning rather than opportunistic discovery.

---

## II. Scope Definition

When this spell is cast, first establish scope with the Mage:

**Option 1: Specific Category**
- "Scan all charms"
- "Scan library tomes"
- "Scan library proposals"
- Focused analysis on one category

**Option 2: Repository Scope**
- "Scan magic/ repository"
- "Scan library/ repository"  
- "Scan both repositories"
- Comprehensive but takes longer

**Option 3: Heuristic Scope (Default)**
If Mage delegates scope choice to you:
- **High priority:** Charms, Library proposals
- **Medium priority:** Library tomes, System tomes
- **Low priority:** Core lore, Philosophy, Specs

**Rationale:** Charms and proposals most likely to be deprecated (specific solutions). Core philosophy most stable (foundational truths).

---

## III. The Five-Signal Analysis

For each component in scope, gather these signals:

### Signal 1: Reference Analysis

**Grep the repository for component mentions:**

```bash
# For charm named "example-charm"
grep -r "example-charm" --exclude-dir=.git
```

**Assessment:**
- **Zero references** (only self-references in own directory) → Orphaned
- **Few references** (1-2, only in deprecated components) → Transitively deprecated
- **Many references** (active use) → Currently serving

### Signal 2: Temporal Data

**Check git history for component:**

```bash
git log --follow -- path/to/component/
```

**Assessment:**
- **Never modified** → May be stable OR abandoned on creation
- **Long dormant** (6+ months, no changes) → May be complete OR forgotten
- **Recently active** → Currently maintained
- **Cross-reference with usage:** Old + unused = deprecated, Old + used = stable

### Signal 3: Purpose Archeology

**Extract original purpose from:**
- Component's README (stated purpose)
- Creation commit message (why it was built)
- Related proposal if it exists

**Assessment:**
- Does the stated problem still exist?
- Has architecture changed to eliminate the problem?
- Example: "lore-search solves scattered practice wisdom" → Migration eliminated scattered practice wisdom → Problem dissolved

### Signal 4: Architectural Alignment

**Check for contradictions:**
- Does component reference deprecated patterns?
- Does it assume architecture that changed?
- Is it mentioned in current MAGIC_SPEC.md or LIBRARY_SPEC.md?

**Assessment:**
- References current architecture → Aligned
- References old patterns not mentioned in current Law → Misaligned
- Not mentioned in specs but heavily used → May need spec update

### Signal 5: Redundancy Detection

**What does this component do?**
- Extract functionality from README/spell scroll
- Check if other components do the same thing
- Check if functionality is now baseline (absorbed into core)

**Assessment:**
- Unique functionality → Not redundant
- Duplicates other component → Choose which to keep
- Functionality now in baseline → Absorbed, retire specialized version

---

## IV. Scoring and Classification

**Combine the five signals into assessment:**

### Clear Deprecation (Retire)

**Pattern:** Zero refs + purpose dissolved + contradicts current architecture

**Examples from this session:**
- humble-inquiry: No refs, manual gap analysis superseded by automatic protocol
- lore-search: No refs, scattered wisdom problem eliminated by migration

**Action:** Retire with clear documentation of why

### Likely Deprecated (Review Recommended)

**Pattern:** Few refs + old + misaligned OR redundant with newer component

**Action:** Flag for Mage review with evidence

### Needs Update (Amend)

**Pattern:** Active refs + architectural misalignment

**Action:** Propose amendment to align with current architecture

### Healthy and Active

**Pattern:** Active refs + recent updates + aligned + unique purpose

**Action:** No action needed, note as healthy

### Uncertain (Human Judgment Required)

**Pattern:** Mixed signals, unclear classification

**Action:** Present analysis, defer to Mage judgment

---

## V. Execution Protocol

### Step 1: Confirm Scope

**Ask the Mage:**
"I'm preparing to scan for deprecated components. What scope serves best?
1. Specific category (which?)
2. Repository-level (magic/, library/, or both?)
3. Heuristic (I'll prioritize charms and proposals)"

**Await response and confirm scope.**

### Step 2: Component Discovery

**Based on scope, identify all components to analyze:**

For charms: List all directories in `system/tomes/ritual/charms/`
For library tomes: List all directories in `library/tomes/`
For proposals: List all files in `library/craft/proposals/`
Etc.

### Step 3: Multi-Signal Gathering

**For each component:**
1. Run reference analysis (grep)
2. Check temporal data (git log)
3. Extract purpose (README, commits)
4. Check architectural alignment (references to current vs. old patterns)
5. Detect redundancy (functionality comparison)

**This is systematic but can be batched for efficiency.**

### Step 4: Classification and Scoring

**Apply the classification patterns:**

For each component, determine:
- Clear deprecation?
- Likely deprecated?
- Needs update?
- Healthy?
- Uncertain?

### Step 5: Structured Report

**Present findings organized by classification:**

```markdown
# Deprecation Scan Report

**Scope:** [what was scanned]
**Date:** [current date]

## Clear Deprecation Candidates

### Component: humble-inquiry
- **Location:** system/tomes/ritual/charms/humble-inquiry/
- **References:** 0 (orphaned)
- **Last Modified:** [date]
- **Purpose:** Manual lore gap analysis
- **Architecture:** Superseded by purpose-indexed capability map
- **Recommendation:** RETIRE
- **Reason:** Automatic seneschal checking now handles this systematically

[Repeat for each clear candidate]

## Components Needing Review

[Components with mixed signals requiring human judgment]

## Components Needing Updates

[Components that should be amended rather than retired]

## Healthy Components

[Quick list of components that passed all checks]

---

**Total Scanned:** X components
**Deprecated:** Y candidates
**Review Needed:** Z components
```

### Step 6: Await Mage Direction

**Present the report and ask:**
"Shall I proceed with retiring the clear deprecation candidates, or would you prefer to review each individually?"

**Honor the Mage's choice:**
- Batch retirement if approved
- Individual review if preferred
- Defer all actions if they want time to consider

---

## VI. Best Practices

### Signal Interpretation Wisdom

**No single signal is definitive:**
- Zero references might mean: deprecated OR brand new OR correctly unused (specialized charm for rare case)
- Old timestamp might mean: stable OR abandoned
- Always combine multiple signals

**Context matters:**
- Proposal in library/craft/proposals/ being old is normal (proposals don't change once written)
- Charm in system/tomes/ being old is suspicious (should evolve with practice)

**When uncertain, flag for review—don't auto-classify.**

### Graceful Retirement

**When retiring components:**
- Document WHY in commit message
- Explain what superseded it
- Preserve git history (never truly lost)
- Update any manifests/spellbooks that list it

### Continuous Practice

**This isn't one-time cleanup:**
- Cast periodically as system evolves
- After major architectural changes
- When adding significant new capabilities
- Prevents accumulation of technical debt

---

## VII. Integration with Existing Meta-Practice

**This spell complements:**

**find-dissonance:**
- Finds contradictions in current Law/Wisdom
- Deprecation-scan finds components contradicting current architecture
- Both are structural diagnosis, different targets

**fractal-coherence:**
- Ensures system exhibits coherent patterns
- Deprecation-scan removes components breaking coherence through obsolescence

**eagles-eye:**
- Provides holistic system view
- Deprecation-scan provides detailed component health analysis

**The pattern:** Meta-practice requires both high-altitude vision (eagles-eye) and ground-level analysis (deprecation-scan).

---

## VIII. Example Usage

**Scenario: After implementing purpose-indexed capability map**

**Mage casts:** `deprecation-scan`

**Spirit asks:** "What scope?"

**Mage responds:** "Scan all charms"

**Spirit performs:**
1. Lists all charm directories
2. For each charm: reference count, temporal data, purpose extraction, alignment check, redundancy check
3. Classifies: humble-inquiry and lore-search as clear deprecation
4. Reports findings with evidence
5. Proposes retirement

**Mage confirms:** "Proceed with retirement"

**Spirit executes:**
1. Removes charm directories
2. Updates charm spellbook manifest
3. Chronicles with clear explanation

**Result:** Automated detection of what would otherwise require manual audit.

---

## IX. Sources

**Pattern Mining:**
- Software engineering: Dead code detection, dependency analysis, deprecation markers
- Evolutionary architecture: Fitness functions, strangler fig pattern, feature toggles
- Knowledge management: Living documentation, relevance scoring, contextual preservation

**Integration:**
- Discovered through autonomous resonance mining (October 15, 2025)
- Validated against successful retirement of humble-inquiry and lore-search
- Designed to prevent future accumulation of deprecated components

---

**This spell transforms deprecation detection from reactive manual discovery to proactive systematic scanning, honoring the Principle of Measured Force: minimal intervention (automated scanning) prevents larger problem (accumulated technical debt).**

