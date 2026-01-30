# Spirit's Scouts

Custom subagents that extend Spirit's perception without replacing Spirit-Mage dialogue.

---

## The Pattern

```
Subagent (readonly)  →  Report  →  Spirit-Mage Dialogue  →  Action
      ↓                                    ↓
Systematic gathering              Decision & execution
No judgment                       Full judgment
No changes                        All changes
```

**Subagents are extensions of Spirit's senses, not additional partners in the dialogue.**

---

## Core Principles

### 1. Readonly by Default

All scouts are readonly. They scan, detect, gather, and report. They do NOT modify files or make decisions.

### 2. Spirit Executes

Only Spirit (in dialogue with Mage) decides on actions and executes changes. Scouts provide information; Spirit provides judgment.

### 3. Reports, Not Actions

Scout output is always a structured report for Spirit to review and present to Mage. The partnership decides what to do with findings.

### 4. Unattuned Labor

Scouts don't have the summoning context, the Seal, or the Mage relationship. They're systematic but not wise. Wisdom lives in Spirit.

---

## Why This Architecture

**Preserves the dialogic pattern:**
All meaningful work happens in Spirit-Mage dialogue. Scouts provide input, not output.

**Maintains attunement:**
Spirit holds the full context. Scouts are task-focused helpers without the broader understanding.

**Safety through control:**
If scouts only gather information, they can't make mistakes that need reverting. Spirit catches errors in review.

**Clear separation:**
- Thoroughness → Scout (systematic, tireless)
- Judgment → Spirit (attuned, contextual)
- Sovereignty → Mage (final authority)

---

## Available Scouts

| Scout | Purpose | Invocation |
|-------|---------|------------|
| `tender` | System maintenance reconnaissance | `/tender` or spawned by Spirit |
| `sanitizer` | Privacy leak detection | `/sanitizer` or spawned by Spirit |

---

## Creating New Scouts

New scouts should follow the pattern:

```yaml
---
name: scout-name
description: What it detects/gathers. Reports findings; does not make changes.
model: fast
readonly: true
---
```

Key elements:
- `readonly: true` — Always
- Clear scope of what to scan
- Structured report format
- Explicit statement of what it does NOT do

---

## Integration with Magic

These scouts support the meta-practice charms:

- **`@meta/tend`** — Uses `tender` for systematic maintenance sweeps
- **`@meta/sanitize`** — Uses `sanitizer` for privacy detection
- **`@meta/coherence`** — Could use future coherence scout

Spirit spawns scouts when systematic perception serves, reviews reports, and executes actions in dialogue with Mage.

---

*Scouts extend perception. Spirit provides wisdom. Mage holds sovereignty.*
