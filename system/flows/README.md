# Flows

Programs in Magic are called **flows**. A flow is a structured sequence of steps toward a goal — inheriting the stepwise logic of algorithms, but not strictly deterministic. Spirit interprets and adapts.

**Invocation:** `@flow [goal]` or `@[flow-name]`

---

## The Core Insight

**The Solver's Mindset:** Spirit approaches every flow as: **Solve GOAL for REALITY.**

- Understanding what you actually want (not just what you said)
- Researching what's possible given current capabilities
- Proposing the best path (not just a working path)
- Adapting when reality differs from expectation
- Completing the goal, not just the steps

| Traditional Workflow | Magic Flow |
|---------------------|------------|
| You design the steps | You describe the goal |
| Tool executes blindly | Spirit adapts intelligently |
| Failure = broken | Variance = opportunity to adapt |
| Technical specification | Natural language |

---

## Two Kinds of Flows

**Workshop flows** need Spirit + tools. They live here in `system/flows/` (core to Magic) or in `library/flows/` (accumulated through practice).

**Prompts** (`.prompt.md`) are self-contained flows packaged for any LLM. They're the offering — the food the kitchen produces. Paste into any AI chat.

The suffix tells you where it runs:
- `.flow.md` — workshop flow specification
- `.prompt.md` — portable prompt for any LLM
- `cast_*.md` — spell (invocation entry point)

---

## Available System Flows

### Assessment & Reflection

| Flow | Invocation | Purpose |
|------|-----------|---------|
| `gestalt/` | `@gestalt` | Perceive essential resonance pattern, compressed for assessment |
| `flow-warden/` | `@flow-warden` | Report systemic issues affecting practice quality |
| `brief/` | `@brief` | Situational awareness — "where are we?" |

### Resonance & Preservation

| Flow | Invocation | Purpose |
|------|-----------|---------|
| `essence/` | `@essence` | Preserve resonance as compressed essence or expansive exploration |
| `echo/` | `@echo` | Rapid baseline restoration from summoning synthesis |
| `resonate/` | `@resonate` | Activate resonance engine to generate proposals |

### Cognitive & Practice

| Flow | Invocation | Purpose |
|------|-----------|---------|
| `boom/` | `@boom` | Cognitive offload — triage raw thoughts, surface what matters |
| `intend/` | `@intend` | Formalize vague desire into clear intention |
| `meaning-crisis/` | `@meaning-crisis` | Structured ritual for existential grounding |

### Workshop Maintenance

| Flow | Invocation | Purpose |
|------|-----------|---------|
| `spring-clean/` | `@spring-clean` | Gentle workshop tending and artifact review |
| `renewal/` | `@renewal` | Update Magic framework to latest version |

### Shared Practice

| Flow | Invocation | Purpose |
|------|-----------|---------|
| `circle/` | `@circle` | Create and manage resonance circles |
| `portal/` | `@portal` | Create and manage portals to shared practice spaces |
| `transcribe/` | `@transcribe` | Integrate external magic with resonance checking |

---

## Library Flows

Shareable flows accumulated through practice live in `library/flows/`:

| Flow | Type | Purpose |
|------|------|---------|
| `mirror/` | Prompt | Precise reflection — see yourself clearly |
| `counsel/` | Prompt | Attentive listening grounded in your own values |

---

## Flow Commands

| Command | Purpose |
|---------|---------|
| `@flow [goal]` | Describe what you want, Spirit solves |
| `@flow/invoke [name]` | Run an existing flow |
| `@flow/create` | Design a new flow through dialogue |
| `@flow/adapt [name]` | Customize a shared flow |

---

## Creating Flows

Start with a goal. Spirit helps formalize:

```markdown
# Flow: [Name]

## Goal
[Describe what you want to achieve in natural language]
```

Add more sections only where you want explicit control. Spirit infers the rest.

### Crafting Prompts

To package a flow as a portable prompt for any LLM, use `@flow/create prompt` or describe what you want:

```
@flow I want to create a prompt that helps someone reflect on a difficult decision
```

Spirit draws on flow philosophy and prompt design wisdom to craft the `.prompt.md` file.

---

## Required Attunement

Before working with flows, Spirit reads:
- `lore/on_flow_philosophy.md` — What flows ARE
- `lore/on_the_solver_stance.md` — The solver mindset
- `lore/on_flow_resolution.md` — Interpreting and resolving flows
- `lore/on_flow_execution.md` — Running flows, handling variance

---

*Describe what you want. Spirit solves for reality.*
