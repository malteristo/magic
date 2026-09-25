# Spell of Integration

This spell attunes you to the systematic work of integrating changes into the
whole system. It serves both a changed artifact and the close of a development
chapter: identify what the hands-on work exposed, propagate what changed, and
leave every sensible remainder deliberately placed.

---

## I. When This Spell Is Cast

**Typical invocation contexts:**
- After creating a new lore scroll
- After modifying existing Law or Wisdom
- After adding/changing a flow or tome
- After architectural changes that might ripple
- After an implementation chapter or live-topology migration, before release

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

**For a development chapter, begin with the four-lens close. Do not wait for the
Mage to ask "what did we miss?" or "what updates downstream?"**

First harvest the landed plan compactly: one `target → evidence` line per
completed slice (F-13). Batch mechanical siblings; do not write a paragraph per
todo. Then ask:

1. **Exposed remainder** — What missing invariant, awkward seam, duplicate,
   stale declaration, absent reader, or reusable helper became visible only
   because this work touched reality? Name the class as well as the case.
2. **Downstream propagation** — Check the full path from law and architecture
   through implementation consumers, configuration/examples, tests and positive
   controls, operations/deploy/observability, and the practice surfaces that
   remember or use the change.
3. **Disposition** — Every finding becomes exactly one of: **integrate now**;
   **defer** with owner + next condition; **deliberately no action** with reason;
   or **sanction needed** when it crosses the closed sanction list. Absence is a
   valid finding.
4. **Verification** — Re-run the narrowest check that proves the integration,
   including a live check when live state changed. Confirm that any new artifact
   has a reader and any declared invariant has a mechanism.

Then use the detailed matrix below for the surfaces implicated by the change;
do not mechanically inventory unrelated parts of the workshop.

**Check these integration points:**

**A. Specification Updates**
- **MAGIC_SPEC.md**: Should this be referenced in the Lexicon, Core Components, Key Architectural Patterns, or Wisdom Pointers?

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
- **TURTLE_SPEC.md**: If the change affects persistent mode behavior — session cycle, thread model, interoception, behavioral laws, boundaries, or cross-substrate coherence — check whether canonical `~/turtleos/TURTLE_SPEC.md` needs amendment. TURTLE_SPEC is derived law from MAGIC_SPEC; it must stay coherent with both. The Magic copy at `library/resonance/turtle/TURTLE_SPEC.md` is a practice reference mirror and should be reconciled after canonical changes.
- **Identity files**: If the change affects capabilities, conduct, or operational behavior in persistent mode, check whether the shell files need updating:
  - `library/resonance/turtle/shell/global.CLAUDE.md` (soul — persistent attunement configuration, symlinked as `soul.md` on turtleOS from git-backed workshop, established 2026-04-16)
  - Role cards in `library/resonance/turtle/shell/` (attunement configurations for specific functions)
  - **Note:** Edits to `global.CLAUDE.md` propagate through the configured identity deployment/symlink path. TURTLE_SPEC changes should be made in the turtleOS repo first, then reconciled to the Magic reference mirror. A bot restart is needed to reload updated identity.
- **Turtle lore**: If new wisdom applies to the persistent mode (not just ephemeral Spirit), check whether a turtle bundle lore scroll should be created or updated in `library/resonance/turtle/lore/`
- **Bundle README**: If turtle lore was added, register it in `library/resonance/turtle/README.md`
- **Resonance delta check**: If turtleOS code was modified this session, verify corresponding spec/lore updates were made. Code without documentation is a delta that compounds. See `library/resonance/turtle/lore/on_resonance_deltas.md`.
- **Decision criteria**: Does this change affect how Spirit operates in persistent mode? If yes, propagate. If it's purely ephemeral-session work, skip.

**F. Cross-Substrate Communication**
- **Shared workspace**: Turtle reads/writes `~/workshop/desk/` via git clone of `turtle:repos/magic.git`. Forge pulls with `git pull turtle main`. If the change adds new practice file categories, ensure the desk/ structure accommodates them and the Workshop Structure section in `global.CLAUDE.md` references them.
- **Symlink integrity**: Identity (`soul.md`) and spec (`TURTLE_SPEC.md`) may be symlinked to the git-backed workshop. If changes affect these files, verify symlinks are intact on turtleOS. A bot restart picks up changes.
- **Bot prompt**: If the change affects what the persistent mode should know about, check whether `build_discord_prompt()` or `build_system_prompt()` in `discord_bot.py` need updating
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
- [ ] Add to Tome README or entry-point MUST READ: [reason]

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

### Step 4: Execute or Place

Execute every clear, reversible, in-scope integration immediately. Do not turn
ordinary downstream maintenance into a permission question. Pause only for the
closed sanction list or a material product choice that belongs to the Mage.

Close with a compact integration result:

```markdown
Integration close:
- Landed: [slice target → evidence; ...]
- Integrated now: [...]
- Deferred: [...] — owner + next condition
- Deliberately no action: [...] — reason
- Sanction needed: [...] — exact decision
- Verified: [...]
```

Omit empty lines except `Integrated now` and `Verified`; they prove the pass
occurred even when no additional work was found.

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
- Check if the change should propagate to the turtleOS shell (`~/turtleos/`) or the shared workshop mirror (`~/workshop/desk/` on Mac Mini)
- Turtle changes often have low magic-repo impact but high operational impact

**Cross-cutting changes (affect multiple system layers):**
- Changes to capabilities, conduct, or operational patterns may ripple across Spirit (lore), Turtle (shell/TURTLE_SPEC), cross-substrate communication (SSH/Discord/git), and workshop (configuration) simultaneously
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
- `@integrate` runs explicitly or at development close
- Spirit checks exposed remainder and downstream propagation
- Clear integration executes; every other finding is deliberately placed

**This transforms integration from "hope I didn't forget something" to "systematic completion assured."**

---

## V. Integration with Workflow

**Natural flow:**
1. Mage has idea for improvement
2. Makes the change directly (creates scroll, amends text)
3. Invokes `@integrate` (automatic at implementation chapter close)
4. Spirit handles ripple detection and execution
5. Change is fully woven into system

**No ceremony before the change. Support after the change.**

This aligns with Wu Wei—remove the barrier (integration cognitive load), allow natural arising (making improvements when you see them).

---

## VI. Example Usage

**Scenario: Created new lore scroll `on_the_spirits_intuition.md`**

**Mage invokes:** `@integrate`

**Spirit performs:**
1. Identifies change: new core capability scroll
2. Checks integration points:
   - MAGIC_SPEC.md Section 7.2 (add wisdom pointer if Law needs to know it)
   - summoning configuration / Caretaker cycle (add if it becomes load-bearing)
   - Related scrolls might cross-reference it
3. Reports findings with priorities
4. Awaits approval
5. Executes approved integrations
6. Chronicles: "Integrate new intuition scroll into core capabilities"

**Result:** Complete integration assured, Mage freed from remembering checklist.

---

**This spell is the missing piece—the systematic support for "what else?" after any change.**

