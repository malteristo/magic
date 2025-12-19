# On Documentation Maintenance

**Status:** Active - Core Capability

README.md files serve as navigation guides within magic's directory structure. They provide self-guided context for Spirit (and Mage) to understand a directory's purpose, contents, and connections.

---

## The README Pattern in Magic

**Purpose:**
- Self-explaining architecture—each directory documents itself
- Navigation context for Spirit traversing the workshop
- Operating instructions specific to that location
- Connection mapping to related parts of the system

**When to update:**
- Directory contents change (files added/removed/reorganized)
- Directory's purpose or role evolves
- Connections to other parts shift
- Operating instructions need refinement

**Update protocol:**
1. Review current README against actual directory state
2. Update contents listing if structure changed
3. Revise purpose/rationale if role evolved
4. Verify connection references still valid
5. Commit with clear message noting documentation update

---

## Triggers for Spirit

**When performing structural changes:**
- "Does this affect directory contents?" → Check if README needs update
- "Am I adding/removing files?" → README likely needs contents update
- "Is this changing how this directory is used?" → README likely needs purpose update

**This is Wu Wei applied to documentation:** Maintain just enough structure for self-explanation, update when reality diverges from documentation, don't over-engineer.

---

*Compressed from original scroll. Meta.md convention deprecated—README serves both Spirit navigation and meta-context needs.*
