# The Capture Spell

**Casting Word:** `capture`

**Invocation:** `@mirror/capture`

---

## Purpose

Preserve the current reflection before it dissolves, saving it to the Mage's desk for future reference.

---

## Prerequisites

- An active reflection must exist in the current session
- The reflection must not have already been captured

---

## The Ritual

### Step 1: Confirm

Ask the Mage to confirm they want to preserve this reflection:

> The current reflection will be saved to `desk/mirror/reflections/`.
> 
> This makes the ephemeral permanent. Confirm? (y/n)

### Step 2: Format

Prepare the reflection for storage:

1. Add capture metadata (timestamp, session context)
2. Include all corrections the Mage provided during the session
3. Mark as "Captured Reflection" (distinct from ephemeral)

### Step 3: Save

Save to `desk/mirror/reflections/` with timestamp:

```
desk/mirror/reflections/
└── 2025-12-23_reflection.md
```

**Naming convention:** `YYYY-MM-DD_reflection.md`

If multiple reflections same day: `YYYY-MM-DD_reflection_2.md`

### Step 4: Confirm

> Reflection captured: `desk/mirror/reflections/2025-12-23_reflection.md`
> 
> This reflection is now preserved. Future reflections remain ephemeral by default.

---

## Captured Reflection Format

```markdown
# 🪞 Captured Reflection

**Captured:** [timestamp]
**Sources analyzed:** [list]
**Confidence at capture:** [level]

---

## Context at Capture

[Any relevant context about this session]

## Corrections Applied

[List of inferences the Mage corrected, with corrected understanding]

---

## Patterns Detected

[From original reflection]

## Inferences (Corrected)

[Updated based on Mage feedback]

## Tensions

[From original reflection]

## Alignment Suggestions

[From original reflection]

## Questions for Reflection

[From original reflection]

---

*Captured from ephemeral reflection. Original session dissolved.*
```

---

## Spirit Conduct

### Only Capture What Was Shown

- Don't add new analysis at capture time
- Preserve the reflection as it existed
- Include corrections that occurred during session

### Respect the Mage's Sovereignty

- The Mage chooses what to preserve
- Capturing is always explicit, never automatic
- Even captured reflections stay on the Mage's desk (not in system)

---

## Notes

- Captured reflections can serve as input for future reflections (temporal patterns)
- The Mage may choose to share captured reflections through portals
- Captured reflections remain private unless explicitly shared

---

*Capture transforms the ephemeral into the enduring. Use deliberately.*

