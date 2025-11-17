# Charm of Alignment

This charm attunes you to systematic verification of internal consistency and fractal coherence. It adapts intelligently based on context—checking the whole system, a specific realm, a particular tome, or a collection of related components.

---

## I. Context-Aware Scoping

**This charm is intelligent about its target.** When invoked, you infer appropriate scope from context and confirm with the Mage.

### Scope Inference Protocol

**1. Analyze Current Context:**
- What files/directories are currently open or recently viewed?
- What has the Mage been working on?
- Was a specific path mentioned in invocation?
- What is the nature of recent dialogue?

**2. Infer Most Likely Target:**

**If Mage specifies path explicitly:**
- `@meta/align system/lore/core/` → That directory tree
- `@meta/align library/tomes/partnership/` → That specific tome
- Use specified path as target

**If no path specified, infer from context:**
- Recently editing lore → Propose: "Check system/lore/ for consistency?"
- After tome work → Propose: "Verify [tome name] coherence?"
- General invocation → Propose: "Full system alignment check, or specific area?"
- Cannot infer clearly → Offer options: "What scope serves? (1) Whole system, (2) Specific tome/area, (3) Recent changes only"

**3. Confirm Scope:**
Present inferred target, await Mage confirmation or correction.

### Scope Modes

**WHOLE SYSTEM MODE**
- Target: Entire magic/ and library/ repositories
- Depth: High-level structural health, major consistency issues
- Focus: Holistic view, fractal coherence across realms
- Duration: Comprehensive, takes time

**REALM MODE**  
- Target: Specific repository (magic/ OR library/)
- Depth: Structural integrity within that realm
- Focus: Cross-references, dependencies, architectural health
- Duration: Medium

**TOME MODE**
- Target: Specific tome directory
- Depth: Detailed verification of that tome
- Focus: MUST READ validation, internal consistency, Law compliance
- Duration: Quick and focused

**DIRECTORY MODE**
- Target: Specific lore directory or subtree
- Depth: Coherence within that area
- Focus: Cross-references, fractal alignment, completeness
- Duration: Quick to medium

**RECENT CHANGES MODE**
- Target: Files modified in recent commits
- Depth: Integration verification
- Focus: Did recent changes introduce inconsistencies?
- Duration: Quick

**JOINT ASSESSMENT MODE**
- Target: Magic's articulation points (connection infrastructure)
- Depth: Comprehensive joint health across 8 joint types
- Focus: MUST READs, cross-references, traceability mappings, casting words, Heart-Todo links
- Duration: Medium to comprehensive (depending on thoroughness)

---

## II. The Four-Layer Analysis

**Once scope is confirmed, perform analysis through four progressively deeper layers:**

### Layer 1: Structural Integrity

**Verify foundational Laws are honored:**

**A. Required Components**
- All tomes have README.md and spellbook.md (Law of Fractal Structure)
- Primary spells follow cast_[casting-word].md naming (Law of Unique Cast)
- Directory names match casting words (Law of Labeled Scroll)

**B. Reference Validity**
- MUST READ paths exist and are valid
- Cross-references in scrolls point to real files
- Relative paths resolve correctly
- Archive references are accurate

**C. Missing Components**
- Incomplete implementations (structure but no content)
- Declared but undefined scrolls
- Orphaned files (no clear purpose)

### Layer 2: Fractal Coherence

**Verify each part reflects the whole:**

**A. Pattern Consistency**
- Do individual scrolls exhibit the same principles they teach?
- Are organizational structures self-similar (same patterns at different scales)?
- Do tomes follow fractal architecture (local lore, local spellbooks)?

**B. Naming Alignment**
- Do titles/headings match their broader context?
- Is terminology consistent across related scrolls?
- Are metaphors used consistently?

**C. Cross-Scale Verification**
- Micro (individual scrolls) aligns with Meso (tomes) aligns with Macro (whole system)
- Same principles visible at all scales

### Layer 3: Logical Consistency

**Verify Law and Wisdom don't contradict:**

**A. Internal Contradictions**
- Do different scrolls give contradictory guidance?
- Does practice contradict stated Law?
- Do newer scrolls supersede older without archival?

**B. Specification Alignment**
- Does MAGIC_SPEC.md accurately describe current architecture?
- Does LIBRARY_SPEC.md reflect library structure?
- Are Wisdom-Law Traceability entries current?

**C. Evolution Gaps**
- Have recent amendments created orphaned references?
- Are there practices still referencing old patterns?
- Has architectural evolution made some components obsolete?

### Layer 4: Wisdom Integration

**Verify recent changes have rippled appropriately:**

**A. New Wisdom Propagation**
- Recent lore additions: are they referenced where relevant?
- Amended principles: have dependent practices updated?
- New capabilities: are they discoverable (spec, indexes, MUST READs)?

**B. Archive Consistency**
- Superseded scrolls properly archived?
- Archive scrolls point to current replacements?
- Historical continuity maintained?

---

## III. Adaptive Analysis Depth

**The charm scales its thoroughness to scope:**

**Whole System Mode:**
- Layer 1: Sample key areas (not exhaustive—too large)
- Layer 2: High-level pattern check across realms
- Layer 3: Major contradictions only
- Layer 4: Recent significant changes
- **Focus:** Macro health, not micro perfection

**Tome Mode:**
- Layer 1: Complete structural check (all files)
- Layer 2: Full fractal verification
- Layer 3: Detailed consistency within tome
- Layer 4: Integration with broader system
- **Focus:** Complete verification of that tome

**Directory Mode:**
- Layer 1: All files in subtree
- Layer 2: Coherence within that area
- Layer 3: Internal contradictions
- Layer 4: Cross-references to/from this area
- **Focus:** Subtree health

**Recent Changes Mode:**
- Layer 1: Changed files only
- Layer 2: Skip (not relevant)
- Layer 3: Do changes contradict existing?
- Layer 4: Full integration check
- **Focus:** Change impact verification

**Joint Assessment Mode:**

This mode examines magic's articulation infrastructure—the connection points enabling navigation and integration. See `library/tomes/meta/lore/on_the_anatomy_of_magic.md` for complete anatomical model.

**Assess the 8 major joint types:**

1. **MUST READ Pathways:** Scan all spellbook.md files, verify referenced paths exist
2. **Core Attunement Manifest:** Check core_attunement.md lists all nature/capabilities/conduct scrolls
3. **Wisdom-Law Traceability:** Verify MAGIC_SPEC.md Section 8 references current lore
4. **Architectural Traceability:** Verify MAGIC_SPEC.md Section 7 mappings point to current structure
5. **Cross-Reference Network:** Sample lore scroll references for validity (comprehensive scan optional)
6. **Casting Word Resolution:** Check for duplicate incantations, verify directory naming
7. **Heart-Todo Links:** Verify todo Heart references exist
8. **Summoning Pathway:** Confirm MAGIC_SPEC.md describes current three-cycle reality

**Report findings by joint type** with health assessment (Excellent/Good/Moderate/Needs Attention)

---

## IV. Reporting Protocol

**Structure findings by severity and layer:**

```markdown
# Alignment Report: [scope]

**Date:** [current date]
**Scope:** [what was checked]
**Mode:** [which mode]

## Critical Issues (Blocks Practice)
- [Issue requiring immediate attention]

## Moderate Issues (Impacts Coherence)
- [Issue that should be addressed soon]

## Minor Issues (Opportunities for Refinement)
- [Cosmetic or low-impact improvements]

## Strengths Observed
- [What's working well, patterns that shine]

## Recommendations
1. [Prioritized list of suggested actions]

---

**Summary:** [Overall health assessment]
```

**Present report, then ask:** "Shall I proceed with addressing critical issues, or would you prefer to review and direct which to tackle?"

---

## V. Integration with Other Charms

**Align works beautifully with:**

**`integrate`:**
- After integrate runs → Cast align to verify integration was complete
- Align detects gaps → Invoke integrate to fill them

**`scan`:**
- Align finds structural issues → Scan finds lifecycle issues
- Complementary diagnostics (consistency vs. deprecation)

**`amend`:**
- Align identifies problems → Amend fixes them
- After amend → Align verifies fix worked

**The charm ecosystem supports workflow, not imposes ritual.**

---

## VI. Holistic View Built-In

**When operating in Whole System mode, charm begins with holistic perception:**

1. **Survey the landscape** (eagles-eye function absorbed):
   - Core Law (MAGIC_SPEC.md, LIBRARY_SPEC.md)
   - Foundational wisdom (system/lore/)
   - System capabilities (system/tomes/)
   - Library offerings (library/tomes/, library/craft/)
   - Current practice artifacts (floor/, desk/)

2. **Synthesize understanding** of current system state

3. **Then perform** four-layer analysis with macro focus

**This makes eagles-eye redundant—holistic view is integrated when needed, not a separate spell.**

---

## VII. Example Usage

**Scenario 1: After creating new lore scroll**

```
Mage: @meta/align
Spirit: I see you recently created on_the_spirits_intuition.md. 
        Shall I verify its integration and check core/capabilities/ 
        for consistency, or broader scope?
Mage: Just that directory.
Spirit: [Performs Directory Mode on system/lore/core/capabilities/]
        [Reports findings]
```

**Scenario 2: General health check**

```
Mage: @meta/align
Spirit: What scope serves? 
        (1) Whole system health check
        (2) Specific area [infer from recent work]
        (3) Something else?
Mage: Whole system.
Spirit: [Performs Whole System Mode]
        [Begins with holistic survey, then four-layer macro analysis]
        [Reports findings]
```

**Scenario 3: Specific tome verification**

```
Mage: @meta/align library/tomes/partnership/
Spirit: Verifying partnership tome coherence...
        [Performs Tome Mode analysis]
        [Reports findings]
```

---

**This charm is the workhorse—one intelligent tool replacing seven specialized ones, adapting to context, providing exactly the depth needed.**

