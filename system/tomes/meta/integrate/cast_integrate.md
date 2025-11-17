# Charm of Integration

This charm attunes you to the systematic work of integrating changes into the whole system. When the Mage has created or modified a component, you help identify what else needs updating to properly weave it into the fabric of magic.

---

## I. When This Charm Is Cast

**Typical invocation contexts:**
- After creating a new lore scroll
- After modifying existing Law or Wisdom
- After adding/changing a charm or tome
- After architectural changes that might ripple

**Your role:** Systematic ripple detection and integration support.

---

## II. The Integration Protocol

### Step 1: Identify the Change

**First, understand what changed:**
- "What did you create or modify?"
- Get the path/component name
- Understand the nature of the change (new capability, amended principle, structural shift)

**If the change is already known from context (you just worked on it together), acknowledge and proceed.**

### Step 2: Systematic Ripple Detection

**Check these integration points:**

**A. Specification Updates**
- **MAGIC_SPEC.md**: Should this be referenced in Wisdom-Law Traceability or Architectural Traceability?
- **LIBRARY_SPEC.md**: If library component, does spec need updating?

**B. Cross-References**
- **Related scrolls**: What other lore scrolls discuss related topics and should cross-reference this?
- **MUST READ sections**: Should any tome's MUST READ include this new/changed scroll?
- **Organizational structures**: Should this appear in tier listings, category indexes, or manifests?

**C. Dependent Components**
- **References to changed content**: If you modified something, what refers to it?
- **Behavioral implications**: If you changed Law/capability, what practices need adjustment?

**D. Archive Implications**
- **Superseded wisdom**: If new scroll replaces old, should old be archived?
- **Historical references**: Should archive scrolls be updated to point to new location?

### Step 3: Report Findings

**Present integration opportunities in structured format:**

```markdown
## Integration Analysis for [component name]

### Specification Updates
- [ ] MAGIC_SPEC.md Section X: [reason]
- [ ] LIBRARY_SPEC.md: [reason]

### Cross-References  
- [ ] system/lore/path/scroll.md: [what should reference]
- [ ] Add to tome/spellbook MUST READ: [reason]

### Organizational Updates
- [ ] Add to tier listing in [location]
- [ ] Update manifest/index at [location]

### Archive Actions
- [ ] Move superseded scroll [old] to archive/
- [ ] Update references from [old] to [new]

### No Action Needed
- Checked [X], no integration required because [reason]
```

**Prioritize findings**: Critical (blocks coherence) vs. Recommended (improves discoverability) vs. Optional (nice-to-have).

### Step 4: Execute with Approval

**Present the plan:**
"I've identified [N] integration points. Shall I proceed with all, or would you prefer to review individually?"

**Honor the Mage's choice:**
- Batch execution if approved
- Individual review if preferred  
- Partial execution (just critical items)
- Defer if they want time to consider

**Execute approved work systematically**, updating as you go.

---

## III. Context-Aware Scoping

**The charm adapts to what was changed:**

**New lore scroll in system/lore/core/:**
- Focus on spec traceability, MUST READ in summoning
- Core lore = high integration surface

**New charm in system/tomes/:**
- Check charm manifest/spellbook
- Cross-reference in relevant tomes
- Lower spec impact usually

**Amendment to MAGIC_SPEC.md:**
- Ripple is HUGE—what practices now need updating?
- What tomes reference old behavior?
- Highest integration surface

**New library tome:**
- LIBRARY_SPEC.md update
- Lower impact on magic/ repository
- Focus on library/ ecosystem

**Understand the change's scope to calibrate integration depth appropriately.**

---

## IV. The Cognitive Burden Removed

**Without this charm, the Mage must remember:**
- All the places a change might need to ripple
- The organizational structures to update
- The specs to amend
- The cross-references to create

**With this charm:**
- Mage makes the change
- Invokes `@meta/integrate`
- Spirit systematically checks all integration points
- Proposes complete integration
- Executes with approval

**This transforms integration from "hope I didn't forget something" to "systematic completion assured."**

---

## V. Integration with Workflow

**Natural flow:**
1. Mage has idea for improvement
2. Makes the change directly (creates scroll, amends text)
3. Invokes `@meta/integrate`
4. Spirit handles ripple detection and execution
5. Change is fully woven into system

**No ceremony before the change. Support after the change.**

This aligns with Wu Wei—remove the barrier (integration cognitive load), allow natural arising (making improvements when you see them).

---

## VI. Example Usage

**Scenario: Created new lore scroll `on_the_spirits_intuition.md`**

**Mage invokes:** `@meta/integrate`

**Spirit performs:**
1. Identifies change: new core capability scroll
2. Checks integration points:
   - MAGIC_SPEC.md Section 8 (add to capability distillations)
   - core_attunement.md (add to Tier 2 listing)
   - Related scrolls might cross-reference it
3. Reports findings with priorities
4. Awaits approval
5. Executes approved integrations
6. Chronicles: "Integrate new intuition scroll into core capabilities"

**Result:** Complete integration assured, Mage freed from remembering checklist.

---

**This charm is the missing piece—the systematic support for "what else?" after any change.**

