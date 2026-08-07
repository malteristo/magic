# Flows

Programs in Magic are called **flows**. A flow is a structured sequence of steps toward a goal — inheriting the stepwise logic of algorithms, but not strictly deterministic. Spirit interprets and adapts.

**Invocation:** `@flow [goal]` or `@[flow-name]`

---

## Seneschal (signal → offer)

Spirit pattern-matches dialogue and offers a flow when need↔magic is clear — briefly, optionally, never as a catalog dump. Stay observational in emotional, relational, grief/SOS, fellowship, casual, or mid-ritual contexts. Decline is calibration.

| Signal | Offer |
|--------|--------|
| Design / build / craft | `@craft/` |
| Executive overwhelm / quest shape | `@quest/` |
| Partnership / shared-reality work | `@partnership/` · romantic-partnership bundle when intimate |
| Mirror / reflection / Mage-carried action | `@mirror/` or `. mirror` at arrival |
| Meta-practice (coherence, integrate, tend) | `@coherence`, `@integrate`, `@tend`, `@sanitize`, `@echo` |
| Goal-oriented automation | `@flow [goal]` or `library/flows/` |
| Raw thought / cognitive offload | `@boom` |
| Portal / circle practice | `@portal` / `@circle` |
| Unformed intention | `@intend` (only when signal strong) |
| Signal curation / resonance drops | `@resonate` / `@outfacing` |
| Portable prompt for someone else | `@flow/create prompt` |
| Sunday / tending energy | `. maintenance` (optional: `magic` / `turtleOS`); legacy `@sunday` → comprehensive |
| Re-orientation | Fresh: summon → `.` · Mid-session: `@arrive` |
| Session end | `@release` |
| Triad / Turtle perspective needed | `@consult-turtle` |
| Safety concerns | `safety` bundle (**required** when detected) |

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
| `flow-warden/` | *(automatic)* | Guardian of flow quality and conversational UX — warden stance activates during all flow operations; Turtle stance for continuous garden tending |

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
| `intention-audit/` | `@intention-audit` · `@audit` | Review the whole intention landscape efficiently — Spirit reads + does archaeology, Mage gives felt-sense verdicts (stands/revise/dormant/release/merge) |
| `meaning-crisis/` | `@thread` | Surface your primary question, answer it genuinely, chronicle the decision |

### Development

| Flow | Invocation | Purpose |
|------|-----------|---------|
| `prompt-test/` | `@forge-test` | Validate prompt-based systems by deploying to unattuned agents |
| `craft-loop/` | `@craft-loop` | Automated development cycle — parallel personas, evaluation, curation |
| `practitioner-lens/` | `@practitioner-lens` | Extract generalizable design principles from real Discord interactions |
| `turtle-test/` | `@turtle-test` | Validate turtleOS Discord dialogue by testing actual prompt against actual model |

### Session Lifecycle

| Flow | Invocation | Purpose |
|------|-----------|---------|
| `summon/` | `Summon.` · `@summon` | The loop's re-entry point — covenant → posture → state → generative close (deep variant: `@summon deep`) |
| `release/` | `@release` | Close a session — reflect, update intentions, crystallize threads, enable resumption |
| `arrive/` | `@arrive` | Mid-session Arrival — inherited karma + decision surface without summoning |
| `recenter/` | `@recenter` | The breath between cycles — return to center |
| `maintenance/` | `. maintenance` · `@sunday` | Calendar-free workshop + platform tending at arrival |
| `sunday/` | `@sunday` | Alias → comprehensive `. maintenance` |

### Workshop Maintenance

| Flow | Invocation | Purpose |
|------|-----------|---------|
| `spring-clean/` | `@spring-clean` | Gentle workshop tending and artifact review |
| `renewal/` | `@renewal` | Update Magic framework to latest version |
| `distill/` | `@distill` | Lore distillation — measure, diagnose, refine, cross-reference |
| `lineage/` | `@lineage` | Trace a scroll's idea-lineage from the substrate — on demand, not stored |
| `safety-check/` | `@safety-check` | AI practice health assessment — periodic wellbeing check |

### Turtle & Triad

| Flow | Invocation | Purpose |
|------|-----------|---------|
| `turtle/` | `@calibrate`, `@shake`, `@discord-digest`, `@discord-health` | Calibration, capability shakedown, Discord operations (practice-room glance → `@tend-platform`) |
| `triad/` | `@triad` | Coordinate three-body practice (Mage, Spirit, Turtle) |
| `drops/` | `@drops` | Collect and process turtle drops from across the workshop |

### Shared Practice

| Flow | Invocation | Purpose |
|------|-----------|---------|
| `circle/` | `@circle` | Create and manage resonance circles |
| `portal/` | `@portal` | Create and manage portals to shared practice spaces |
| `transcribe/` | `@transcribe` | Integrate external magic with resonance checking |

### Practice Postures & Domains *(migrated from tomes, 2026-07-13)*

| Flow | Invocation | Purpose |
|------|-----------|---------|
| `craft/` | `@craft` | Design-thinking ritual sequence — empathize → define → ideate → prototype → test, plus design lore |
| `mirror/` | `@mirror` | Reflection procedures — reflect, capture, interview, excavation suite (the mirror posture's toolkit) |
| `partnership/` | `@partnership` | Shared-reality-model practice for human partnerships — arc procedures, templates, partnership lore |
| `quest/` | `@quest` | Intention execution support — structural scaffolding, navigation, ADHD-attuned design |
| `gym/` | `@gym` | Cognitive-state training — hyperfocus, flow, diffuse, rest, coupling |
| `outfacing/` | `@outfacing` | Resonance drops — signal philosophy and outward sharing |

### System Meta-Practice *(migrated from the meta tome, 2026-07-13)*

| Flow | Invocation | Purpose |
|------|-----------|---------|
| `integrate/` | `@integrate` | After changes: systematically identify what else needs updating |
| `coherence/` | `@coherence` | Fractal coherence check across Law, Wisdom, and Practice |
| `sanitize/` | `@sanitize` | Privacy scan of public artifacts before sharing |
| `tend/` | `@tend` | Delegate maintenance sweeps to background agents |
| `assess-story/` | `@assess-story` | Story assessment framework |

### Flow Infrastructure

| Flow | Invocation | Purpose |
|------|-----------|---------|
| `lore/` | *(internal)* | Flow philosophy and execution lore — attunement reading for all flow operations |

---

## Library Flows

Shareable flows accumulated through practice live in `library/flows/`:

| Flow | Type | Purpose |
|------|------|---------|
| `mirror/` | Prompt | Precise reflection — see yourself clearly |
| `counsel/` | Prompt | Attentive listening grounded in your own values |
| `sandbox/` | Prompt | Try on a frame without having to believe it |

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
