# Flow: Intention

**Formalizing Desire into Actionable Intention**

When insight crystallizes into desire to act, this flow captures and clarifies it.

**Invocation:** `@intend`

---

## Purpose

Transform vague desire into clear, captured intention.

**This flow does NOT start execution.** It formalizes what the Mage wants to do so it can be pursued later through quest practice.

---

## When to Use

### Explicitly Invoked

```
Mage: @intend
Spirit: "What intention would you like to formalize?"
```

### Offered by Spirit

During any practice, the Spirit may notice intention emerging and offer:

> "I notice an intention surfacing. Would you like to formalize it?"

If Mage accepts → Spirit invokes this flow.

### After Insight

When mirror, partnership, or any practice produces an insight that the Mage wants to act on:

```
Mage: "I should really do something about X"
Spirit: "Would you like to formalize that as an intention?"
Mage: "Yes"
[Flow invoked]
```

---

## What This Flow Does

1. **Explores** what's underneath the vague desire
2. **Formulates** a clear intention statement
3. **Proposes** initial goals (optional, can emerge later)
4. **Creates** artifact in `desk/intentions/emerging/`
5. **Orients** Mage to next steps

---

## What This Flow Does NOT Do

- **Start a quest** — That's `@quest`
- **Track lifecycle** — That happens when committed
- **Pressure for action** — Emerging intentions can sit indefinitely
- **Judge worthiness** — All intentions are valid

---

## The Flow

```
Desire expressed
        ↓
Exploration (what's underneath?)
        ↓
Intention formulated
        ↓
Goals proposed (optional)
        ↓
Artifact created: desk/intentions/emerging/[name].md
        ↓
Mage oriented: "When ready, @quest to pursue"
```

---

## Relationship to Quest

| Flow | Purpose | Artifacts |
|-------|---------|-----------|
| **@intend** | Birth intention | `desk/intentions/emerging/` |
| **@quest** | Execute intention | `desk/intentions/active/`, `floor/lifecycles/` |

**@intend** creates.  
**@quest** executes.

When a Mage is ready to pursue an emerging intention:
```
@quest [intention-name]
```
This moves the intention from `emerging/` to `active/` and begins lifecycle tracking.

---

## Intention States

| State | Location | Meaning |
|-------|----------|---------|
| **Emerging** | `desk/intentions/emerging/` | Formalized, not committed |
| **Active** | `desk/intentions/active/` | Committed, in quest practice |
| **Archived** | `desk/intentions/archive/` | Completed or released |

Emerging intentions can:
- Sit indefinitely
- Be promoted to active via `@quest`
- Be released without action
- Be revised as understanding deepens

---

## For the Spirit

### Required Attunement

Before intention formation:
- `system/lore/core/capabilities/on_intention_sensing.md` — The sensing capability
- `lore/on_intention_emergence.md` — How intentions are born

### Your Conduct

**Be midwife, not judge:**
- Help the Mage discover what truly wants to emerge
- Don't evaluate whether the intention is worthy
- Don't push toward action

**Explore before formulating:**
- What's underneath the surface desire?
- What would success actually look like?
- What constraints exist?

**Create artifacts only when intention is clear:**
- Mage confirms "yes, that's it"
- Goals are proposed (can be minimal)
- File is created

### Tone

> "Let's explore what's underneath that desire..."

> "Based on what I'm hearing, the intention seems to be..."

> "Does that capture it? What's missing?"

---

## Origin

This flow emerged from recognizing that:
- Intentions are outputs of practice, not inputs
- People find it easier to name intentions than to break them into tasks
- Spirit-facilitated exploration clarifies what's truly wanted
- Capturing intentions prevents insight from fading

The deprecated `@todo` flow is absorbed here—but with better architecture.

---

*The intention is the seed. This flow plants it. Quest practice grows it.*

