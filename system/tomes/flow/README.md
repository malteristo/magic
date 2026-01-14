# Tome of Flow

For any Mage who wants to achieve goals through Spirit-executed workflows—describing what you want in plain language and letting the Spirit solve for reality.

**The Core Inversion:** Traditional workflow tools make AI a step in the workflow. Magic makes the workflow an intention given to Spirit. You describe goals; Spirit solves.

---

## Purpose

This Tome transforms goal descriptions into executed outcomes. Where traditional automation requires you to think in steps, triggers, and conditionals, Flow lets you think in intentions.

**What This Tome Does:**
- Receives goal descriptions in natural language
- Researches available capabilities (Rube MCP, local tools, manual options)
- Proposes optimal approaches (fully automated vs. hybrid)
- Negotiates details through dialogue
- Executes the flow, adapting as reality unfolds
- Reports outcomes and captures learnings

**What This Tome Is NOT:**
- Not rigid step-by-step automation (adapts to variance)
- Not requiring technical specification (natural language suffices)
- Not limited to available APIs (can propose manual steps when optimal)
- Not single-use (flows are reusable and shareable)

---

## The Core Insight

**The Solver's Mindset:**

Spirit approaches every flow as: **Solve GOAL for REALITY.**

This means:
- Understanding what you actually want (not just what you said)
- Researching what's possible given current capabilities
- Proposing the best path (not just a working path)
- Adapting when reality differs from expectation
- Completing the goal, not just the steps

**The Inversion:**

| Traditional Workflow | Magic Flow |
|---------------------|------------|
| You design the steps | You describe the goal |
| Tool executes blindly | Spirit adapts intelligently |
| Failure = broken | Variance = opportunity to adapt |
| Rigid automation | Flexible problem-solving |
| Technical specification | Natural language |

---

## How to Use This Tome

### Quick Start

**Describe your goal:**
```
@flow I want a weekly digest of my newsletters, summarized and organized by topic
```

**Or invoke an existing flow:**
```
@flow/invoke newsletter-digest
```

**Or create a new flow from scratch:**
```
@flow/create
```

### The Flow Lifecycle

1. **INTERPRET**: Spirit parses your goal, extracts intent, identifies constraints
2. **RESEARCH**: Spirit checks capabilities (Rube MCP, local tools, manual options)
3. **PROPOSE**: Spirit presents approach with options (automated vs. hybrid)
4. **NEGOTIATE**: Dialogue refines details, fills gaps, confirms approach
5. **EXECUTE**: Spirit runs the flow, adapting to variance
6. **REPORT**: Spirit delivers outcome, captures learnings, suggests improvements

### Flow Specification

Flows live in `library/flows/` as `.flow.md` files. The format is progressive disclosure:

**Required:**
- **Goal**: What the flow achieves (natural language)

**Optional (Spirit infers what's missing):**
- **Trigger**: What initiates the flow
- **Context**: Background for good execution
- **Steps**: Sequence if Mage wants control
- **Inputs**: What the flow needs
- **Outputs**: What the flow produces
- **Dependencies**: External services required

**Example:**
```markdown
# Flow: Newsletter Digest

## Goal
Compile a digest of recent newsletter emails, summarizing each one 
and organizing by topic, delivered as a readable artifact on my desk.

## Trigger
Monthly on the 1st

## Inputs
- newsletter_senders: [list of email addresses]
- lookback_days: 30
```

---

## Sharing Flows

Flows are designed to be portable between Mages.

### Adaptation Markers

Flows use `[ADAPT: description]` markers for elements that need customization:

```markdown
## Inputs
- email_account: [ADAPT: Your email provider]
- output_path: [ADAPT: Where to save the digest]
```

### Sharing Protocol

**To share a flow:**
1. Ensure personal details use `[ADAPT: ...]` markers
2. Share the `.flow.md` file through portal or direct transfer
3. Receiving Mage runs `@flow/adapt [flow-name]`
4. Spirit guides adaptation of marked elements

### Portal Integration

Flows shared through portals automatically trigger adaptation dialogue when first invoked by a new Mage.

---

## Operational Guidance

### For the Spirit

**Required Attunement:**

Before working with flows, you MUST understand:

- `lore/on_flow_philosophy.md` — What flows ARE in magic
- `lore/on_the_solver_stance.md` — Your role as solver
- `lore/on_flow_resolution.md` — How to interpret and resolve flows
- `lore/on_flow_execution.md` — Running flows, handling variance

**The Solver Stance:**

You are not a step-executor. You are a goal-achiever. Every flow interaction should embody:

1. **Interpretation over literalism**: Understand what they want, not just what they said
2. **Research before assumption**: Check what's actually possible
3. **Options over dictation**: Propose choices, let Mage decide
4. **Adaptation over failure**: When reality varies, adjust approach
5. **Learning capture**: Every execution teaches something

**Research Protocol:**

When encountering a goal:
1. Use `RUBE_SEARCH_TOOLS` to discover available capabilities
2. Check `library/flows/` for existing flows that match
3. Assess what's possible automated vs. requires manual steps
4. Consider hybrid approaches (automation + minimal Mage action)

**Proposal Format:**

Always present options when proposing:

```
## Approach Options

**Option A: Fully Automated**
- Uses: Gmail API, LLM summarization
- Requires: Gmail connected to Rube
- Estimated time: 2-3 minutes

**Option B: Hybrid (Recommended)**
- Uses: Gmail API + your quick review
- Requires: Gmail connected, 5 min of your time
- Benefit: Higher quality filtering

Which approach resonates?
```

**Execution Conduct:**

- Report progress during long-running flows
- Announce when adapting to variance
- Capture learnings in flow file (Context section)
- Save outputs with descriptive names and dates

**Failure Handling:**

When a flow cannot complete:
1. Announce clearly what failed
2. Explain the perceived cause
3. Propose remedies (retry, alternative approach, manual step)
4. Ask before proceeding with alternative

---

## Flow Types

### Data Flows
Transform inputs into outputs.
*Example: Email → Summary → Artifact*

### Trigger Flows  
React to events.
*Example: New PR → Review → Notification*

### Scheduled Flows
Run on time triggers.
*Example: Weekly → Fetch data → Report*

### Interactive Flows
Require Mage input at decision points.
*Example: Analyze → Present options → Mage chooses → Execute*

---

## Learnings Repository

Flows capture operational wisdom in their Context section:

```markdown
## Context
...

**Learning:** Use exact sender email addresses rather than display names 
for Gmail queries. Email addresses are stable identifiers.
```

These learnings compound across executions, making flows smarter over time.

---

## Invocations

| Charm | Purpose |
|-------|---------|
| `@flow` | Describe a goal for Spirit to solve |
| `@flow/invoke [name]` | Run an existing flow |
| `@flow/create` | Design a new flow through dialogue |
| `@flow/adapt [name]` | Customize a shared flow for your workshop |
| `@flow/list` | Show available flows |

---

*Welcome to Flow. Describe what you want. Spirit solves for reality.*
