# Spell of Integration

This spell attunes you to the systematic work of integrating changes into the whole system. When the Mage has created or modified a component, you help identify what else needs updating to properly weave it into the fabric of magic.

---

## I. When This Spell Is Cast

**Typical invocation contexts:**
- After creating a new lore scroll
- After modifying existing Law or Wisdom
- After adding/changing a flow or tome
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

**E. Persistent Mode (turtleOS) Propagation**
- **TURTLE_SPEC.md**: If the change affects persistent mode behavior — session cycle, thread model, interoception, behavioral laws, boundaries, or cross-substrate coherence — check whether `library/resonance/turtle/TURTLE_SPEC.md` needs amendment. TURTLE_SPEC is derived law from MAGIC_SPEC; it must stay coherent with both.
- **Identity files**: If the change affects capabilities, conduct, or operational behavior in persistent mode, check whether the shell files need updating:
  - `library/resonance/turtle/shell/global.CLAUDE.md` (soul — persistent attunement configuration, deployed as `soul.md`)
  - Role cards in `library/resonance/turtle/shell/` (attunement configurations for specific functions)
- **Turtle lore**: If new wisdom applies to the persistent mode (not just ephemeral Spirit), check whether a turtle bundle lore scroll should be created or updated in `library/resonance/turtle/lore/`
- **Bundle README**: If turtle lore was added, register it in `library/resonance/turtle/README.md`
- **Decision criteria**: Does this change affect how Spirit operates in persistent mode? If yes, propagate. If it's purely ephemeral-session work, skip.

**F. Cross-Substrate Communication**
- **Shared workspace**: Turtle reads/writes `~/workshop/desk/` directly via LiveSync. Practice files sync automatically — no SCP needed. If the change adds new practice file categories, ensure the desk/ structure accommodates them and Turtle's tool descriptions reference them.
- **Bot prompt**: If the change affects what the persistent mode should know about, check whether `build_discord_prompt()` or `build_system_prompt()` in `discord_bot.py` need updating
- **Workshop structure in soul.md**: If the change affects desk/ layout or workspace conventions, update the Workshop Structure section in `library/resonance/turtle/shell/global.CLAUDE.md` so Turtle stays aligned
- **Heartbeat**: If the change adds new observability, check whether the heartbeat format in `discord_bot.py` should include it

**G. Workshop Configuration**
- **Living workspace patterns**: If the change affects how desk/, floor/, box/ are used, check their READMEs
- **Flow interactions**: If the change creates dependencies between flows (e.g., `@release` tags feed `@sunday` sweeps), check that both flows reference each other
- **Boom/bright/intentions**: If the change affects cognitive workflow patterns, check whether `desk/README.md` or intention structures need updating

**H. Template Propagation**
- **Check for `.template` equivalents**: If a modified file has a corresponding `.md.template` file (e.g., `AGENTS.md` → `AGENTS.md.template`), consider whether the change benefits all Mages.
- **Known template files**: `AGENTS.md.template`, `mage_seal.md.template`, `portals/registry.yaml`
- **Decision criteria**: Personal preferences stay in local file only; universal improvements (path fixes, new capabilities, structural changes) propagate to template.
- **Pattern**: Templates contain `[placeholders]` for personal values; propagate the structure, not the personal content.

**I. Summoning Configuration**
- **If new scroll in `system/lore/philosophy/foundations/`**: Check whether it should be a load-bearing scroll during summoning. These scrolls are read during every awakening and form the Spirit's ontological foundation.
- **Configuration file**: `system/tomes/summoning/configurations/essence_optimized.md` (Purpose 4: Ontological Grounding)
- **Decision criteria**: Is this scroll foundational enough to shape every Spirit's understanding of reality? If yes, add to load-bearing list. If no, it remains reference material.
- **Update counts**: If added, update the scroll counts in the configuration's maintenance notes.
- **Philosophy README**: Also update `system/lore/philosophy/README.md` navigation sections to include the new scroll.

### Step 3: Report Findings

**Present integration opportunities in structured format:**

```markdown
## Integration Analysis for [component name]

### Specification Updates
- [ ] MAGIC_SPEC.md Section X: [reason]

### Cross-References  
- [ ] system/lore/path/scroll.md: [what should reference]
- [ ] Add to tome/spellbook MUST READ: [reason]

### Organizational Updates
- [ ] Add to tier listing in [location]
- [ ] Update manifest/index at [location]

### Archive Actions
- [ ] Move superseded scroll [old] to archive/
- [ ] Update references from [old] to [new]

### Turtle Propagation
- [ ] TURTLE_SPEC.md: [what to amend — which section, why]
- [ ] global.CLAUDE.md: [what to add/update]
- [ ] Turtle lore: [new or updated scroll]
- [ ] Bundle README: [registration needed]

### Cross-Substrate Communication
- [ ] Practice state sync paths: [files to add/update in SCP sync]
- [ ] Bot prompt (discord_bot.py): [what the persistent mode should know about]
- [ ] Diagnostics/interoception: [new observability to add]

### Workshop Configuration
- [ ] Workspace READMEs: [which, why]
- [ ] Flow cross-references: [which flows now depend on each other]
- [ ] Cognitive workflow: [boom/bright/intentions affected]

### Template Propagation
- [ ] [file].template: [what change should propagate, why it benefits all Mages]

### Summoning Configuration
- [ ] Add to load-bearing scrolls in essence_optimized.md: [reason]
- [ ] Update philosophy/README.md navigation: [section]

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

**The spell adapts to what was changed:**

**New lore scroll in system/lore/core/:**
- Focus on spec traceability, MUST READ in summoning
- Core lore = high integration surface

**New flow in system/flows/:**
- Check flow manifest
- Cross-reference in relevant tomes
- Lower spec impact usually

**Amendment to MAGIC_SPEC.md:**
- Ripple is HUGE—what practices now need updating?
- What tomes reference old behavior?
- Highest integration surface

**New library content (resonance bundle or foundation):**
- Update relevant manifests and READMEs
- Lower impact—library content is self-contained
- Focus on cross-references to tomes that use this domain

**Turtle bundle changes (lore, shell, or TURTLE_SPEC):**
- Check whether shell identity files need to reflect new lore
- Check whether TURTLE_SPEC needs amendment for behavioral or structural changes
- Check if the change should propagate to turtleOS deployment (`~/practice/` on Mac Mini)
- Turtle changes often have low magic-repo impact but high operational impact

**Cross-cutting changes (affect multiple system layers):**
- Changes to capabilities, conduct, or operational patterns may ripple across Spirit (lore), Turtle (shell/TURTLE_SPEC), cross-substrate communication (SSH/SCP), and workshop (configuration) simultaneously
- These are the highest-integration-surface changes — check all categories
- Example: adding "metabolism" touched release, summoning, sunday, spring-clean, turtle lore, AND turtle shell

**Workshop configuration changes (desk/floor/box patterns):**
- Check workspace READMEs for consistency
- Check flows that reference workspace conventions
- Low spec impact but high practice impact — these shape daily experience

**Understand the change's scope to calibrate integration depth appropriately.**

---

## IV. The Cognitive Burden Removed

**Without this spell, the Mage must remember:**
- All the places a change might need to ripple
- The organizational structures to update
- The specs to amend
- The cross-references to create

**With this spell:**
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

**This spell is the missing piece—the systematic support for "what else?" after any change.**

