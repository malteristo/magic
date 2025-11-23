# On a Web-Strollable Library

**Status:** Visionary  
**Date:** October 27, 2025  
**Context:** Future architecture when Alliance grows

---

## I. The Vision

When the Alliance grows beyond solo practice, the Library may benefit from web-browsable interface optimized for human strolling—searchable, sidebar-navigated, optimized for discovery and inspiration beyond what git file browsing provides.

---

## II. The Core Insight

**The actual barrier:** GitHub file browser is adequate for systematic access but suboptimal for inspirational browsing.

**What strollability requires:**
- Search across all content
- Sidebar navigation always visible
- Optimized reading experience
- Lower barrier for non-git users

---

## III. Three Architectural Options

### Option A: GitHub Wiki

**Approach:** Migrate library content to magic.wiki (attached wiki)

**Advantages:**
- Web UI optimized for reading
- Built-in search
- Unified project (magic repo + its wiki)
- Familiar pattern (documentation wikis)

**Disadvantages:**
- Flat page namespace (loses fractal directory structure)
- Wiki permissions tied to main repo (loses governance separation)
- Separate clone required for complex editing (workflow complexity)
- Directory elegance becomes naming conventions

**Assessment:** Achieves strollability but sacrifices structural elegance.

---

### Option B: GitHub Pages

**Approach:** Library repo publishes to GitHub Pages (static site generation)

**Advantages:**
- Beautiful web interface (full design control)
- Preserves git directory structure
- Maintains governance separation
- Git for contributors, web for browsers
- Can use existing navigation docs (CATALOG, STROLLING, etc.)

**Disadvantages:**
- Requires site generator setup (Jekyll, MkDocs, etc.)
- Build/deploy configuration needed
- Ongoing maintenance

**Assessment:** Likely the elegant synthesis—adds web layer without losing advantages.

---

### Option C: Enhanced Git Navigation (Current)

**Approach:** Trust CATALOG, STROLLING_GUIDE, WISDOM_MAP, enhanced READMEs

**Advantages:**
- Already implemented (October 27, 2025)
- Minimal maintenance
- Works with current architecture
- No migration required

**Disadvantages:**
- Still browsed through GitHub file UI
- No built-in search
- Less optimal for pure browsing

**Assessment:** Solves navigation/discovery problem. May be sufficient.

---

## IV. The Recommendation

**Test Phase:** Use current navigation infrastructure (CATALOG, STROLLING, WISDOM_MAP) in practice.

**Observation points:**
- Can scrolls be found quickly via CATALOG?
- Does STROLLING_GUIDE enable browsing through GitHub interface?
- Do discovering Mages navigate effectively?
- Is web strollability genuinely needed or does current serve?

**Decision criteria:**

**If current navigation sufficient:**
→ Keep two-repo + enhanced navigation (problem solved, no architectural shift needed)

**If web strollability becomes important:**
→ Prototype GitHub Pages for library/ repo (preserves structure, adds web layer)

**If Pages insufficient:**
→ Consider wiki migration (only if structural tradeoffs acceptable)

---

## V. When This Becomes Relevant

**Trigger conditions:**

1. **Alliance Growth:** Multiple Mages contributing, non-technical members browsing

2. **External Discovery:** Outfacing communication points people to Library; web experience matters

3. **Validated Need:** Practice reveals current navigation insufficient despite enhancements

4. **Resource Availability:** Someone has bandwidth for site setup/maintenance

**Until then:** Current architecture with navigation infrastructure serves well.

---

## VI. Implementation Considerations (For Future)

### If GitHub Pages Chosen

**Setup requirements:**
- Choose generator (Jekyll native, MkDocs popular, others)
- Configure build (site structure, theme)
- Set up deployment (GitHub Actions or manual)
- Migrate/adapt navigation docs for web format

**Maintenance:**
- Deploy when content changes
- Update site config as structure evolves
- Monitor for broken links

**Advantage:** Can start small (pilot with key sections), expand incrementally.

### If Wiki Chosen

**Migration requirements:**
- Enable wiki on magic or library repo
- Adapt content to flat namespace
- Create sidebar navigation structure
- Update all references in magic repo
- Archive old library repo

**Maintenance:**
- Manual sidebar updates
- Page organization through naming
- Content syncing if git workflow continues

**Disadvantage:** All-or-nothing migration, loses directory structure.

---

## VII. Integration with Current Navigation

**The navigation infrastructure built October 2025 remains valuable regardless:**

**If staying with current:**
- CATALOG, STROLLING, WISDOM_MAP serve as primary navigation
- Already functional

**If adding GitHub Pages:**
- These docs become site content
- Structure translates naturally to web
- Navigation layer already designed

**If migrating to wiki:**
- Core navigation concepts translate
- STROLLING paths become wiki tours
- CATALOG becomes wiki sidebar organization

**The work isn't wasted—it's foundation for any future web layer.**

---

## VIII. The Measured Force Principle

**Effort required signals alignment:**

**Current navigation infrastructure:**
- Built in ~10 cycles
- Solves immediate problem
- Feels aligned (effortless once started)

**Wiki migration:**
- Would require significant effort
- Structural losses
- Workflow complexity

**GitHub Pages:**
- Medium effort for setup
- Preserves advantages
- Adds capability cleanly

**If massive effort required → Signals misalignment or wrong timing.**

---

## IX. The Living Question

**Does the Library need web strollability, or does it need better navigation?**

**We've built better navigation.** Practice reveals if this is sufficient or if web layer is genuinely needed.

**Hold the vision. Test the current. Let evidence guide next evolution.**

---

## X. For Future Alliance

**When multiple Mages contribute:**
- Web interface might matter more (accessibility for non-git users)
- Separate Library governance might matter more (permissions, curation)
- Beautiful web presence might matter more (Alliance identity)

**At that scale, GitHub Pages (library repo → website) likely optimal:**
- Git workflow for curators
- Web experience for browsers
- Governance separation maintained
- **Both populations served**

**Until then:** Current architecture with navigation infrastructure serves.

---

**Status:** Visionary proposal, held for future consideration

**Next review trigger:** When Alliance grows OR when practice reveals current navigation insufficient

**The Pattern will show the path when the time is right.**

---

*This proposal preserves the insight without forcing implementation. Practice reveals truth. Architecture evolves when evidence compels, not when ideas seem elegant.*

