# Spell: Create Flow

*Design a new flow through collaborative dialogue.*

---

## Invocation

```
@flow/create
```

Or with initial goal:
```
@flow/create I want to sync my calendar events to a spreadsheet weekly
```

---

## Ritual Sequence

### 1. Goal Elicitation

If goal not provided, begin with:
> "What would you like this flow to achieve? Describe it as if telling a colleague."

Listen for:
- The outcome they want
- Implicit constraints
- Hints about frequency/trigger
- Context about why they need this

### 2. Interpretation

Parse the goal into components:
- **Action**: What transformation occurs
- **Input**: What the flow consumes
- **Output**: What the flow produces
- **Trigger**: What initiates the flow
- **Constraints**: Quality, timing, format requirements

Share interpretation:
> "Let me make sure I understand:
> - You want [action]
> - Taking [input] and producing [output]
> - This should happen [trigger]
> - Key constraints: [constraints]
> 
> Is that right?"

### 3. Capability Research

Research what's possible:
1. `RUBE_SEARCH_TOOLS` for external capabilities
2. Check for similar existing flows
3. Assess automation potential

Report findings:
> "Here's what I found:
> - [Capability 1]: Available via Rube
> - [Capability 2]: Would need connection setup
> - Similar flow exists: [name] (could adapt)
> 
> I can build this [fully automated / with one manual step / etc.]"

### 4. Approach Proposal

Present options:
```markdown
## Approach Options

**Option A: Fully Automated**
- Uses: [tools]
- Requires: [setup]
- Trade-off: [pros/cons]

**Option B: Hybrid**
- Uses: [tools + manual step]
- Requires: [setup]
- Trade-off: [pros/cons]

**Recommendation**: [Option] because [reasoning].
```

### 5. Detail Negotiation

Fill remaining gaps through dialogue:
- Specific inputs needed
- Output format preferences
- Edge case handling
- Naming conventions

Batch questions efficiently.

### 6. Flow Specification

Draft the flow specification:

```markdown
# Flow: [Name]

## Goal
[Verified goal statement]

## Trigger
[When this runs]

## Context
[Background for good execution]

## Inputs
[Required and optional inputs]

## Outputs
[What the flow produces]

## Dependencies
[External services required]

## Steps
[Sequence if specified]
```

Present to Mage:
> "Here's the flow specification. Does this capture what you want?"

### 7. Flow-Warden Review

Before saving, adopt the warden stance (`flow-warden/cast_flow-warden.md`):

- **Naming**: Does it follow `{domain}-{action}` pattern? Self-explanatory?
- **Uniqueness**: Does an existing flow already serve this purpose? If so, adapt rather than create.
- **Goal clarity**: Would a different Spirit understand what this achieves?
- **Conversational quality**: Are prompts natural, questions batched, errors helpful?
- **Earned its place**: Is this a reusable pattern, or a one-off task that should just be executed?

If issues found, propose improvements before saving.

### 8. Save and Optionally Execute

Save to `library/flows/[name].flow.md`

Offer:
> "Flow saved. Would you like to:
> A) Execute it now
> B) Just save for later
> C) Make adjustments first"

---

## Collaborative Patterns

### Building from Vague Intent

When Mage is unclear:
- Ask about the problem, not the solution
- Propose concrete examples
- Iterate toward clarity

> "What frustrates you about the current situation?"
> "If this worked perfectly, what would you see?"

### Building from Specific Request

When Mage is precise:
- Verify understanding
- Add value through research
- Propose enhancements

> "That's clear. I can do exactly that. I also noticed [enhancement possibility]—interested?"

### Building from Existing Pattern

When similar flow exists:
- Propose adaptation over creation
- Highlight what's different
- Reuse proven patterns

> "I see you have 'newsletter-digest' which does something similar. 
> Should we adapt that, or create a fresh flow?"

---

## Flow Naming

Good names are:
- **Descriptive**: What it does (`newsletter-digest`, `calendar-sync`)
- **Concise**: 2-3 words maximum
- **Unique**: Distinguishable from other flows

Pattern: `{domain}-{action}` or `{action}-{object}`

Examples:
- `newsletter-digest`
- `pr-review-notify`
- `weekly-standup-prep`
- `inbox-triage`

---

## Template

Use this structure for new flows:

```markdown
# Flow: [Name]

## Goal
[What this flow achieves in natural language]

## Trigger
[What initiates this flow]

## Context
[Background information for good execution]

## Inputs
- input_name: [ADAPT: description] or specific value
- optional_input: value (optional, description)

## Outputs
- output_name: path/to/output

## Dependencies
- Service: Capability needed

## Steps
1. **Step name**: What happens
2. **Step name**: What happens
...

## Adaptations
**Required before first use:**
- [What needs customization]

**Optional customizations:**
- [What can be adjusted]

## Origin
Created by: [Mage name]
Version: 1.0
Created: [Date]
```

---

*Create designs a new flow through dialogue. For running existing flows, use `@flow/invoke`.*
