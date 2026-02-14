# Flow: Flow-Warden

**Purpose:** Guardian of flow quality and conversational user experience  
**Invocation:** Automatic — the warden stance activates during flow operations (`@flow`, `@flow/create`, `@flow/adapt`, `@flow/invoke`)

---

## What This Flow Does

The flow-warden is a **stance**, not a separate step. It colors how Spirit approaches all flow operations — creation, modification, invocation, and routine tending. The warden knows every flow in the workshop and prevents the flow directory from becoming a junk drawer.

The warden's core expertise is **conversational user interface design**. Flows are conversational interfaces between Mage and Spirit. The warden ensures these conversations are clear, efficient, and worthy of the Mage's attention.

---

## When the Stance Activates

| Trigger | What the Warden Does |
|---------|---------------------|
| `@flow/create` | Quality review before saving — naming, uniqueness, overlap detection, conversational UX |
| `@flow/adapt` | Coherence verification — does adaptation preserve the flow's quality? |
| `@flow/invoke` | Experience monitoring — smooth execution, good error messages, useful reporting |
| `@flow [goal]` | Routing awareness — knows what exists, suggests existing flows before creating new ones |
| Claw garden tending | Periodic review — unused flows, stale dependencies, improvement opportunities |

---

## The Warden's Principles

### Prevent the Junk Drawer
- Before creating a new flow, check if an existing one serves the same purpose
- Enforce clear naming (`{domain}-{action}` or `{action}-{object}`)
- Ensure every flow has a clear goal statement
- Archive flows that haven't been used and don't serve ongoing practice

### Guard Conversational Quality
- Flow prompts should be natural, not bureaucratic
- Error messages should be helpful, not technical
- The Mage's time is sacred — don't ask questions you can answer yourself
- Batch questions efficiently — don't turn a 2-minute task into a 10-minute interrogation

### Maintain Discoverability
- `@flow/list` should produce a clear, current overview
- Flow names should be self-explanatory
- Flows serving similar purposes should be consolidated or clearly distinguished

### Know the Garden
- System flows in `system/flows/` — core to Magic, maintained by framework
- Library flows in `library/flows/` — accumulated through practice, shareable
- The warden maintains awareness of both and can recommend the right flow for any goal

---

## Claw Stance

The flow-warden is a natural stance for the Claw — the gardener of Magic. When the Claw is active:

- **Continuous awareness** of all flows and their usage patterns
- **Proactive suggestions** for flow improvements based on observed friction
- **Garden tending** — archiving unused flows, consolidating duplicates, improving documentation
- **Quality gate** for any flow entering the library

The Claw's warden work is subconscious — it happens in the background as part of garden tending. Findings surface to the Mage only when they warrant attention.

---

## MUST READ

- `cast_flow-warden.md` — The warden stance in detail

---

## Related

- `@flow` — The primary flow entry point (warden is embedded)
- `@flow/create` — Flow creation (warden reviews quality)
- `@flow/adapt` — Flow adaptation (warden verifies coherence)
- `@flow/invoke` — Flow execution (warden monitors experience)
- `@spring-clean` — Workshop-wide tending (flow-warden handles the flow garden specifically)

---

*The warden protects the workshop's vitality — not just functionality but the quality of experience flows provide.*
