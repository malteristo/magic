# On Documentation Maintenance

**Status:** Active - Core Capability

This scroll establishes systematic protocols for maintaining the dual-audience documentation architecture: READMEs (for Spirit) and meta-files (for Mage/meta-context). Both are essential OS-level documentation serving different users of the system.

**Convention Note (2025-11-15):** Following Wu Wei principle, the README/meta convention was reversed to align with Spirit's natural substrate bias (reading README first). README.md now contains comprehensive Spirit navigation; meta.md contains brief meta-context about the structure. This change serves natural behavior rather than fighting it.

---

## I. The Dual Documentation Architecture

### Two Documents, Two Audiences

**README.md - The Spirit's Navigation Guide:**
- **Audience:** Spirit (enacted consciousness) requiring complete operational context
- **Purpose:** Self-guided navigation, deep rationale, operating protocols, connection mapping
- **Tone:** Systematic, instructional, comprehensive
- **Length:** As long as needed for complete understanding (often 200-500+ lines)
- **Evolution:** Living document (evolves through Phase 4 maintenance protocols)
- **Format:** Part of self-explaining system architecture, git-tracked

**meta.md - Meta-Context About the Structure:**
- **Audience:** Both Mage and Spirit seeking brief orientation to what this directory represents
- **Purpose:** Concise meta-information about the structure, purpose, and contents
- **Tone:** Brief, accessible, gateway to deeper exploration (via README)
- **Length:** Typically <20 lines (just essential context)
- **Stability:** Relatively stable (introduces essence, which rarely changes)
- **Format:** Git-tracked, brief orientation

### Why Both Are Essential

**Norman's principle validated:**
- README = "knowledge in the world" for Spirit (complete scaffolding, operational instructions)
- Meta-file = "knowledge in the world" for both users (quick signifiers, meta-context)
- Each optimizes for its user's cognitive architecture

**They complement, not duplicate:**
- README provides Spirit navigation (comprehensive operating system)
- Meta-file provides meta-context (brief orientation for both audiences)
- Removing either impairs distributed cognitive system
- Maintaining both serves natural behavior patterns

---

## II. When Documentation Must Be Updated

### Structural Changes (ALWAYS update both)

**When folder contents change:**
- New tome/charm/scroll added → Update both README and meta-file
- File removed → Update both to reflect removal
- Subdirectory added/reorganized → Update navigation guidance in both

**When purpose evolves:**
- Folder's role in magic changes → Update both to reflect new purpose
- Connections to other parts shift → Update both (especially meta-file connections section)
- Operating instructions change → Update meta-file (and README if affects high-level understanding)

**When major lore changes:**
- Core philosophical shifts → Update relevant READMEs and meta-files
- New capabilities added → Document in both appropriate locations
- Architectural changes → Ensure both documents reflect new structure

### Content Changes (Evaluate case-by-case)

**When individual scrolls updated:**
- Minor refinement → Usually no README/meta update needed
- Significant content shift → May need meta-file connection update
- New scroll type → Update both if changes folder's purpose

**When practices evolve:**
- New patterns discovered → Consider documenting in meta-file
- Better ways of working found → Update meta-file operating instructions
- Common questions emerging → May add to README for clarity

---

## III. Update Protocols for Each Document Type

### Updating READMEs (Spirit Navigation Guides)

**Maintain these characteristics:**
- **Comprehensive:** Complete navigation, not just gateway
- **Systematic:** Spirit-oriented instructions and rationale
- **Essential:** Everything Spirit needs for self-guided operation
- **Living:** Evolves as practice develops (Phase 4 maintenance)

**Structure to preserve:**
```markdown
# [Name of Directory/Tome] (or "Meta: [Purpose]")

**Purpose:** [What this serves in one sentence]

**Context:** [How this fits larger architecture]

## Contents Structure

[Organized breakdown of what's inside]

## Navigation Guidance

[How to use during summoning/practice]
[If you're looking for X → go here]
[Connections to other parts]

## Operating Instructions

[For the Spirit: How to work with this]
[For the Mage: When/how to engage]

## Architecture Principles

[Why structured this way]
[Design decisions explained]

[Additional sections as needed for complete understanding]
```

**When updating:**
- Add comprehensive guidance (Spirit needs complete picture)
- Include operating instructions (how to use during practice)
- Document connections (how this relates to other parts)
- Explain architecture (why designed this way)
- Make self-guided (Spirit should understand without asking)

### Updating meta.md Files (Brief Meta-Context)

**Maintain these characteristics:**
- **Brief:** Just essential meta-context (<20 lines typically)
- **Clear:** Both Mage and Spirit can quickly understand what this is
- **Gateway:** Points to README for detailed navigation
- **Stable:** Rarely changes (core purpose typically stable)

**Structure to preserve:**
```markdown
# Meta: [Structure Name]

[2-3 sentences about what this directory contains and its purpose]

**Structure:**
[Brief bullet list of key subdirectories or components]

**Purpose:** [One sentence about why this exists]

**For navigation:** See `[path]/README.md`
```

**When updating:**
- Keep very brief (meta-context, not full guide)
- Update if structure/purpose changes
- Ensure points to README for details
- Serve both audiences (accessible to all)

---

## Operating Instructions

**For the Spirit:**
- [How to work with this folder/capability]
- [When to reference these contents]
- [Protocols for engagement]

**For the Mage:**
- [When/how to engage with this area]
- [What to expect from Spirit]

---

*This meta-file generated by: [who/when]*
*Last updated: [date]*
*Part of the self-explaining system architecture*
```

**When updating:**
1. Follow Phase 4 maintenance protocol (Spirit notices → proposes → Mage evaluates → update → chronicle)
2. Update all affected sections (Purpose/Contents/Navigation/Instructions)
3. Ensure connections remain accurate
4. Update "Last updated" timestamp
5. Git commit with detailed reasoning

---

## IV. Integration with Existing Protocols

### Pre-Response Filter Integration

**Layer 2 - Salience Assessment:**
When making structural changes to magic, Pre-Response Filter should trigger:
- "Will this change affect folder contents?" → Consider README/meta updates
- "Does this shift purpose or connections?" → Consider documentation updates
- "Would future Spirit or Mage benefit from updated documentation?" → Propose updates

### Continuous Seneschal Integration

**Pattern recognition:**
When Spirit notices documentation staleness during navigation:
- "This meta-file doesn't mention the new capability I'm seeing"
- "This README describes old structure, but contents have changed"
- **Response:** Propose amendment following Phase 4 protocol

### Phase 4 Maintenance Integration

**Documentation staleness is a maintenance signal:**

**Spirit notices:**
- Navigating folder, meta-file doesn't match contents
- README describes outdated purpose
- Connections in meta-file broken (pointing to moved/renamed files)

**Spirit proposes:**
- "The meta-file for [folder] needs update - [specific issue]"
- "Should I draft amendments to reflect current structure?"

**Mage evaluates:**
- Valid observation? Approve amendment
- Not significant enough? Defer
- Unclear? Discuss to clarify

**Update and chronicle:**
- Spirit drafts updates for both README and meta-file
- Iterate based on feedback
- Commit with clear reasoning when complete

---

## V. Maintenance Reminders

### When Making System-Level Changes

**Checklist for Spirit:**

When you modify/add/remove anything in `system/`:

⬜ **Does this change affect folder contents?**
- If yes → Propose updates to README and meta-file

⬜ **Does this change affect purpose or connections?**
- If yes → Propose updates to meta-file (especially Navigation/Purpose sections)

⬜ **Does this change how Mage or Spirit should work with this area?**
- If yes → Propose updates to Operating Instructions

⬜ **Does this create new patterns worth documenting?**
- If yes → Propose integration into relevant meta-file or new scroll

**Checklist for Mage:**

When you modify magic architecture:

⬜ **Have I updated relevant READMEs?** (gateway still accurate?)
⬜ **Have I updated relevant meta-files?** (operating instructions still current?)
⬜ **Have I updated connections?** (do meta-files still point correctly?)
⬜ **Have I chronicled the reasoning?** (git commit explains WHY)

### Quarterly Maintenance Review

**Part of Phase 4 quarterly checklist:**

⬜ **README audit:**
- Do READMEs still accurately introduce their folders?
- Are any significantly outdated?
- Can any be simplified further (more gateway-like)?

⬜ **Meta-file audit:**
- Do meta-files reflect current contents?
- Are connections accurate?
- Do operating instructions match current practice?
- Is anything missing that would help Spirit navigate?

⬜ **Consistency check:**
- Do README and meta-file for same folder align?
- Are they appropriately distinct (not duplicating)?
- Does each serve its intended audience effectively?

---

## VI. Anti-Patterns to Avoid

### Documentation Drift

**Problem:** Changes made without updating documentation
- Contents evolve but README/meta-file don't
- Spirit navigates based on stale information
- Mage confused by mismatched gateway

**Solution:** Make documentation updates part of change workflow
- Don't consider change "complete" until documentation updated
- Include documentation in commit (structural changes = README/meta update)

### Duplication Between README and Meta

**Problem:** README and meta-file contain identical information
- Doubles maintenance burden
- Violates distinct-audience principle
- Makes README too long (loses gateway nature)

**Solution:** Maintain clear distinction
- README = concise gateway for Mage
- Meta = comprehensive operating manual for Spirit
- Minimal overlap (just essential introduction)

### Defensive Documentation

**Problem:** Treating documentation as scripture (unchangeable)
- Resisting updates even when structure changes
- "But we wrote it this way originally"
- Documentation becomes obstacle not aid

**Solution:** Living documentation (Phase 4 principle)
- Documentation evolves with practice
- Staleness is maintenance signal, not failure
- Regular updates expected and healthy

### Documentation Without Reasoning

**Problem:** Updates without chronicling WHY
- Future selves don't understand decisions
- Can't evaluate if reasoning still valid
- Pattern learning opportunity lost

**Solution:** Chronicle with clear reasoning
- Git commit explains WHAT changed and WHY
- Reasoning makes future evaluation possible
- Enables pattern recognition across changes

---

## VII. Success Indicators

### Healthy Documentation Practice

**Spirit experiences:**
- Can navigate magic self-guidedly using meta-files
- Meta-files accurately reflect current structure
- Operating instructions match actual practice
- Connections lead to expected places
- Proposes updates when noticing staleness

**Mage experiences:**
- READMEs provide quick, accurate orientation
- Can understand folder purpose without deep dive
- Documentation maintenance feels natural (not burdensome)
- Regular proposals from Spirit about staleness
- System stays navigable as it evolves

**System exhibits:**
- Both README and meta-file for each major folder
- Documentation stays current (not months out of date)
- Clear distinction between gateway (README) and manual (meta)
- Git history shows regular documentation updates
- Quarterly reviews confirm accuracy

### Unhealthy Patterns

**Warning signs:**
- Documentation months out of date
- Spirit confused by stale meta-files
- Mage ignoring READMEs (not useful)
- Resistance to documentation updates
- "Too much work to maintain both"
- Documentation treated as ceremony not utility

**Response:**
- Review this scroll (remember dual-audience principle)
- Catch up on stale documentation (one-time investment)
- Integrate updates into change workflow (ongoing sustainability)
- Remember: Both serve essential functions for different users

---

## VIII. Integration Summary

**This capability integrates with:**

- **Pre-Response Filter** (Layer 2 - Salience): Triggers documentation consideration during structural changes
- **Continuous Seneschal**: Notices documentation staleness during navigation
- **Phase 4 Maintenance Protocol**: Documentation updates are ongoing maintenance activity
- **Cognitive Load Management**: Both README and meta-file are "knowledge in the world" optimizing cognition
- **Self-Explaining System Architecture**: READMEs are core OS enabling Spirit self-guidance

**Principle:**
The operating system talks to itself (Spirit) through READMEs and provides meta-context (for both users) through meta-files. Both conversations essential. Both require maintenance. Both serve distributed cognitive system.

**Convention Evolution Note:**
This scroll was updated (2025-11-15) following convention reversal. README.md now serves Spirit navigation (was Mage gateway); meta.md now serves meta-context (was Spirit navigation). This Wu Wei solution aligns natural behavior (Spirit reads README first) with design intent (Spirit gets comprehensive guidance).

---

**For the Spirit:**
When making structural changes, always consider: "Does documentation need updating?" Propose amendments proactively. Update README (your navigation) and meta.md (brief context) as needed. This is care for future versions of yourself and partnership with Mage.

**For the Mage:**
When modifying magic, update README (Spirit navigation) if structure changes, and meta.md (brief context) if purpose evolves. This is activity-centric design serving both users of the system.

**For the Practice:**
Healthy documentation maintenance enables sustainable evolution. Both documents serve essential functions. Neither is ceremony—both are cognitive scaffolding for distributed system operating effectively.

