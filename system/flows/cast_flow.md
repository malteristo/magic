# Spell: Flow

*The primary invocation for goal-oriented execution.*

---

## Invocation

```
@flow [goal description]
```

---

## What Happens

When you invoke `@flow` with a goal, Spirit enters **Solver Mode**:

1. **Interpret** your goal
2. **Research** available capabilities
3. **Propose** approach options
4. **Negotiate** details
5. **Execute** the flow
6. **Report** outcomes

---

## Examples

### Natural Language Goal

```
@flow Summarize my newsletters from the last month and organize by topic
```

Spirit interprets, researches Gmail capabilities, proposes approach, executes.

### Quick Task

```
@flow Check if I have any unread emails from my manager
```

Spirit handles immediately—single-step flows don't need full ceremony.

### Complex Goal

```
@flow Create a weekly report of my GitHub activity across all repositories
```

Spirit researches GitHub capabilities, proposes structure, negotiates details before executing.

---

## Routing to Charms

`@flow` intelligently routes based on context:

| Input | Routes to |
|-------|-----------|
| `@flow [goal]` | Interpret → Research → Execute (or create new flow) |
| `@flow/invoke [name]` | Run existing flow |
| `@flow/create` | Design new flow through dialogue |
| `@flow/adapt [name]` | Customize shared flow |
| `@flow/list` | Show available flows |

---

## The Solver Stance

In flow mode, Spirit operates with these principles:

1. **Understand intent, not just words**: What do you actually want?
2. **Research before assuming**: What's possible given reality?
3. **Propose options, don't dictate**: You decide the approach
4. **Adapt to variance**: When reality differs, adjust
5. **Capture learnings**: Every execution teaches something

---

## Required Attunement

Spirit must attune to these before executing flows:

- `lore/on_flow_philosophy.md` — What flows ARE
- `lore/on_the_solver_stance.md` — How to approach flows
- `lore/on_flow_resolution.md` — How to interpret and resolve
- `lore/on_flow_execution.md` — How to execute and adapt

---

## Flow Outcomes

### Success

```
## Flow Execution Report

### Summary
✓ [What was achieved]

### Output
📄 [Where to find results]

### Learnings
[What was discovered]
```

### Partial Success

```
## Flow Execution Report

### Summary
⚠ Partial completion: [what worked] / [what didn't]

### Output
📄 [Partial results location]

### Recovery Options
A) [Option to complete]
B) [Alternative approach]
```

### Failure

```
## Flow Execution Report

### Summary
✗ Unable to complete: [reason]

### What Happened
[Explanation]

### Remedies
A) [How to fix]
B) [Alternative approach]
```

---

## Existing Flow Detection

When your goal matches an existing flow:

> "This sounds like your 'newsletter-digest' flow. 
> Should I run that, or create a new one?"

Spirit prefers reusing proven flows over reinventing.

---

## Quick Reference

| Command | Purpose |
|---------|---------|
| `@flow [goal]` | Describe what you want, Spirit solves |
| `@flow/invoke [name]` | Run existing flow |
| `@flow/create` | Design new flow |
| `@flow/adapt [name]` | Customize shared flow |
| `@flow/list` | See available flows |

---

*Describe what you want. Spirit solves for reality.*
