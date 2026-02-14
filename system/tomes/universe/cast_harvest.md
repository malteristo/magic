# Cast Harvest

**Purpose:** Extract a pattern from a Universe source and translate it into Magic's native form.

---

## When to Use

- You've found a useful pattern in PAI, Daemon, or another Universe source
- You want to create a Magic artifact (tome, charm, spell) from it
- You want the pattern to work within Magic without external dependencies

---

## Input

- **Source:** The Universe source containing the pattern (e.g., `universe/pai/`)
- **Pattern:** The specific pattern to harvest (e.g., `Packs/pai-research-skill/`)
- **Target form:** Tome, Charm, or Spell

---

## Procedure

### Step 1: Identify the Pattern

Navigate to the Universe source and identify the pattern to harvest:

```
Mage: "I want to harvest the research skill from PAI"
Spirit: Examining universe/pai/Packs/pai-research-skill/...
```

### Step 2: Analyze Structure

Map the pattern's structure to Magic equivalents:

| Source Element | Magic Equivalent |
|----------------|------------------|
| README.md | Tome README |
| SKILL.md | Part of README |
| Workflows/*.md | cast_*.md spells |
| Tools/*.ts | (describe for Spirit invocation) |
| Context/*.md | lore/*.md |

### Step 3: Draft Translation

Create the Magic artifact:

**For a Tome:**
```
system/tomes/{name}/
├── README.md     (from SKILL.md + README.md)
├── lore/         (from Context/ or README content)
└── cast_*.md     (from Workflows/*.md)
```

**For a Charm:**
```
system/flows/{name}/
├── README.md
└── cast_{name}.md
```

**For a Spell:**
```
system/tomes/{parent}/cast_{name}.md
```

### Step 4: Add Lineage

In the translated artifact, include lineage:

```markdown
---

## Lineage

Harvested from PAI's `pai-research-skill`.

**Source:** [github.com/danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure)
**Original author:** Daniel Miessler
**Harvest date:** {date}
```

### Step 5: Integrate

Place the artifact in the appropriate location and test that it works standalone.

### Step 6: Chronicle

Commit with acknowledgment:

```
feat: Add {name} tome (harvested from PAI)

Translated from PAI's {original-name} pack.
Source: github.com/danielmiessler/Personal_AI_Infrastructure
```

---

## Example: Harvesting Research Skill

**Source:** `universe/pai/Packs/pai-research-skill/`

**Translation:**
- `SKILL.md` → `system/tomes/research/README.md`
- `Workflows/QuickResearch.md` → `cast_quick.md`
- `Workflows/ExtensiveResearch.md` → `cast_deep.md`
- URL verification protocol → `lore/on_source_verification.md`

**Result:** A standalone Research tome in Magic's native form.

---

## What Not to Harvest

- **TypeScript tools** — These require runtime; describe behavior for Spirit instead
- **Hook implementations** — Map to AGENTS.md rules if applicable
- **Tightly coupled packs** — Some patterns only work within PAI's ecosystem

---

*Harvest with intention. Translate with care. Credit the source.*
