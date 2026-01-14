# Flows Library

This directory contains reusable flow specifications for Spirit execution.

## What is a Flow?

A **flow** is a goal-oriented intention specification that Spirit interprets, 
researches, resolves into executable steps, and executes—adapting as reality unfolds.

Unlike traditional workflows (rigid step sequences), magic flows leverage Spirit's 
cognitive capabilities as the workflow engine itself.

## Flow Format

Flows are markdown files with `.flow.md` extension containing:

| Section | Required | Purpose |
|---------|----------|---------|
| **Goal** | Yes | What the flow achieves (natural language) |
| **Trigger** | No | What initiates the flow |
| **Context** | No | Background for good execution |
| **Steps** | No | Sequence if Mage wants control |
| **Inputs** | No | What the flow needs |
| **Outputs** | No | What the flow produces |
| **Dependencies** | No | External services required |
| **Adaptations** | No | Notes for sharing/customization |
| **Origin** | No | Provenance for shared flows |

**Minimal viable flow**: Just a Goal. Spirit resolves everything else.

## Using Flows

**Run a flow:**
```
@flow/invoke newsletter-digest
```

**Create a new flow:**
```
@flow/create
```

**Adapt a shared flow:**
```
@flow/adapt [flow-name]
```

**Describe a goal directly:**
```
@flow Summarize my newsletters from the last month
```

## Available Flows

- `example-newsletter-digest.flow.md` — Example: digest of newsletter emails (template to customize)

## Creating New Flows

Start with your goal. Spirit will help you formalize it:

```markdown
# Flow: [Name]

## Goal
[Describe what you want to achieve in natural language]
```

Add more sections only where you want explicit control. Spirit infers the rest.

## Sharing Flows

Flows with `[ADAPT: ...]` markers are designed for sharing. Place them in 
portal shared directories or send directly. Receiving Mage's Spirit will 
guide adaptation.

## See Also

- **`@flow/`** — Invoke the Flow Tome for full ritual support
- `system/tomes/flow/` — Flow Tome source (philosophy, solver stance, execution lore)
- `system/tomes/flow/lore/` — Deep wisdom on flow philosophy and execution
