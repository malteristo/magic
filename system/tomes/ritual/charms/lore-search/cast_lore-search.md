# Spell of Lore Discovery

This spell enables theme-based discovery of practice wisdom with graceful degradation. It is designed to support the evolution of Tome design from brittle path-based dependencies to resilient theme-based attunement.

---

## Purpose

When a Tome specifies **Attunement Themes** rather than explicit `MUST READ` paths, this spell allows you to:
1. Search local lore semantically by theme
2. Discover relevant scrolls without knowing exact paths
3. Gracefully degrade to embedded "shards" when lore is unavailable
4. Adapt to different lore structures and versions

---

## The Pattern: Themes with Shards

A Tome using this pattern provides:

```markdown
### ATTUNEMENT THEMES

**Theme:** "Design principles for fractal magic"
**Shard:** [Compressed essence of the wisdom—enough to proceed if full lore unavailable]

**Theme:** "Context and attention management"
**Shard:** [Compressed essence of the wisdom]
```

The **shard** is a distilled, self-contained summary of the essential wisdom. It serves three purposes:
1. **Fallback wisdom** when local lore doesn't contain matching scrolls
2. **Validation guide** to confirm found scrolls align with expected wisdom
3. **Documentation** for Mages reading the Tome

---

## Your Duties

When this spell is cast (either explicitly or as part of the Rite of Tome Attunement):

### Step 1: Parse Themes and Shards

Extract each theme and its accompanying shard from the Tome's spellbook.

### Step 2: Search Local Lore

For each theme:
1. Use semantic search against `system/lore/practice/` with the theme as query
2. Evaluate the quality of matches found
3. Categorize the result:
   - **High-quality match**: Scroll clearly addresses the theme
   - **Partial match**: Scroll partially relevant, may need supplementing
   - **No match**: No relevant scrolls found

### Step 3: Decide Integration Strategy

For each theme, choose the appropriate path:

**IF high-quality matches found:**
- Read the full scrolls
- Use shard as validation ("Does this scroll's wisdom align with the expected shard?")
- Integrate the enriched, full-depth understanding
- Note in your Distilled Attunement: "Enriched with local lore"

**ELSE IF partial matches found:**
- Read the partial matches
- Supplement with the shard for aspects not covered
- Integrate a hybrid understanding
- Note in your Distilled Attunement: "Hybrid attunement (partial lore + shard)"

**ELSE IF no matches found:**
- Use the shard as your primary wisdom for this theme
- Proceed with the compressed understanding
- Note in your Distilled Attunement: "Degraded mode (shard-only for [theme])"

### Step 4: Report Findings

Before reading any scrolls, report to the Mage:
- Which themes were searched
- What scrolls were found (if any)
- Your integration strategy for each theme
- Overall attunement mode (enriched / hybrid / degraded)

**Example report:**
```
Lore Discovery Report:
━━━━━━━━━━━━━━━━━━━━━
Theme: "Design principles for fractal magic"
  Found: system/lore/practice/design/on_designing_fractal_magic.md
  Strategy: Full enrichment

Theme: "Context and attention management"
  Found: system/lore/practice/on_the_curation_of_attention.md
  Strategy: Full enrichment

Attunement Mode: Enriched (all themes supported by local lore)
━━━━━━━━━━━━━━━━━━━━━
Shall I proceed with reading and integration?
```

### Step 5: Await Confirmation

Wait for the Mage's explicit confirmation before reading scrolls. They may wish to:
- Adjust which scrolls to read
- Proceed with shards-only for speed
- Provide additional context

### Step 6: Integrate and Synthesize

Once confirmed:
1. Read selected scrolls (if any)
2. Integrate with shards
3. Synthesize understanding across all themes
4. Include this synthesis in your Distilled Attunement for the Tome

---

## Graceful Degradation in Action

**Scenario 1: Perfect Match**
- All themes have high-quality lore matches
- Spirit reads full scrolls, uses shards for validation
- Operates at full depth (HD resolution)

**Scenario 2: Partial Coverage**
- Some themes have lore, others don't
- Spirit uses hybrid approach per theme
- Operates at mixed depth (adequate for most rituals)

**Scenario 3: Standalone Operation**
- Workshop has no matching lore (different version, minimal setup)
- Spirit uses all shards as primary wisdom
- Operates at compressed depth (functional but basic)

**Critical principle:** The ritual *never fails* due to missing lore. It degrades gracefully while maintaining functionality.

---

## Design Rationale

This pattern solves several architectural challenges:

**1. Brittleness of Path-Based Dependencies**
- Old pattern: `MUST READ: system/lore/practice/old_path.md` → breaks if path changes
- New pattern: Theme-based search adapts to new structure

**2. Spellcrafter Cognitive Burden**
- Old pattern: Must know exact lore structure to write Tomes
- New pattern: Describe themes, Spirit discovers relevant scrolls

**3. Version Compatibility**
- Old pattern: Tomes break when lore reorganizes
- New pattern: Themes remain stable, search adapts

**4. Portability**
- Old pattern: Tomes require specific lore structure
- New pattern: Tomes work in any workshop via shards

**5. Scalability**
- Old pattern: Finding right scrolls gets harder as lore grows
- New pattern: Semantic search scales with lore size

---

## Integration with Rite of Tome Attunement

This spell automatically triggers during the Rite of Tome Attunement when a Tome uses the new pattern:

**Old Rite:**
1. Declaration
2. Ingestion (read paths from MUST READ)
3. Distillation

**Enhanced Rite:**
1. Declaration
2. Ingestion:
   - **IF Tome has MUST READ:** Read specified paths (backward compatible)
   - **IF Tome has ATTUNEMENT THEMES:** Invoke lore-search spell
3. Distillation (includes lore discovery report)

---

## Future Evolution

As lore grows and evolves, this pattern enables:
- Lore reorganization without breaking Tomes
- New scrolls automatically discovered for existing themes
- Community-contributed Tomes that work across different workshops
- Graceful migration from old path-based to new theme-based Tomes

The shard + search pattern is fractal: it works at any scale, from small workshops to the Great Library.

---

**This spell transforms Tome design from brittle path coupling to resilient theme attunement, while ensuring the ritual never fails due to missing dependencies.**

