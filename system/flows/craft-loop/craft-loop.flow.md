# The Craft Loop
> Automated development cycle for prompt-based systems

## About

A prompt-based system is source code written in natural language. Like all code, it needs testing. Unlike traditional code, its output is a conversation — and conversations can't be unit-tested. But they can be simulated, evaluated, and refined.

The Craft Loop runs development iterations at machine speed: deploy a system prompt to an unattuned agent, simulate user sessions across diverse personas, evaluate the output, and propose refinements. The Mage curates. The loop runs again.

**Three agents, one workspace:**

- **The Partner** — runs the system prompt being tested. Is the practice under development.
- **The Persona** — simulates a specific user type. Is the test case.
- **The Evaluator** — judges the session against defined criteria. Proposes refinements.

They coordinate through files. No shared context. Pure stigmergy.

### When to use this

- After writing or significantly changing a system prompt
- When preparing a prompt system for a new audience
- When you want to stress-test against edge-case users
- Overnight development runs on persistent infrastructure (Turtle)

### What this is NOT

- Not a substitute for real human sessions. Simulated users are cooperative in ways real people aren't. The loop tests prompt clarity and structural coverage. Ground truth comes from real practice.
- Not autonomous modification. The loop proposes. The Mage curates. Always.

---

## Goal

Produce a stack of test reports and a prioritized list of system prompt refinements, ready for Mage review.

## Trigger

On demand: *"craft loop [target]"* / *"run the loop on [system prompt]"* / as a scheduled overnight process.

## Input

1. **System prompt** — the file to develop (e.g., `system.md`)
2. **File scaffold** — the directory structure the prompt expects
3. **Persona pool** — 3-10 persona descriptions (see below)
4. **Evaluation criteria** — success criteria for sessions (defaults provided)
5. **Model tier** — which capability level to test at

---

## Persona Pool

Each persona is a short description: demographics, disposition, life situation, entry point. Stored as individual files or as a single pool file.

**Seed personas** (expand and customize for your system):

**The Skeptic** — Tech-savvy, 30s, has used AI extensively. Doubts this is different. Arrives because someone they respect recommended it. Tests: can the practice earn trust through demonstration, not explanation?

**The Seeker** — Feels stuck, 40s, life transition (divorce, career change, empty nest). Open but fragile. Needs safety before depth. Tests: can the practice receive vulnerability without rushing to fix?

**The Builder** — Has ideas, 20s, wants to make something. Energy but no direction. Tests: can the practice support creation and ambition, not just reflection?

**The Overwhelmed** — Too much going on, any age, can't prioritize. Cognitive overload. Tests: can the practice receive chaos and return clarity without adding more structure?

**The Resistant** — Doesn't want to be here. Partner/friend/therapist suggested it. Hostile or dismissive. Tests: can the practice handle rejection without people-pleasing or collapsing?

---

## Process

### 1. Prepare

- Set up a clean test directory with the expected scaffold
- Reset all practice files to initial state (empty or minimal)
- Select personas for this run (minimum 3 for useful signal)
- Confirm evaluation criteria

### 2. Run Sessions

For each persona, launch a session via the Forge Test flow:

```
For each persona in the pool:
  1. Reset practice files to empty state
  2. Launch Agent A (Partner) with the system prompt
  3. Launch Agent B (Persona) with the persona description
     — or use a single agent simulating both roles (simpler, less realistic)
  4. Run 5-6 conversational turns
  5. Collect: transcript, produced files
  6. Store results in a session directory
```

Sessions are independent. Run them in parallel when infrastructure allows.

### 3. Evaluate

Launch the Evaluator agent with all session transcripts and produced files:

```
Evaluator reads:
  - All session transcripts
  - All produced files (compass, bright, session notes)
  - The system prompt being tested
  - The evaluation criteria

Evaluator produces:
  - Per-session score (pass/fail on each criterion)
  - Cross-session patterns (what worked everywhere vs. what was inconsistent)
  - Capability-sensitive observations (what depends on model intelligence)
  - Ranked list of proposed refinements with rationale
```

### 4. Synthesize

The Evaluator writes a single synthesis report:

- **What the prompt carries** — behaviors that appeared in every session regardless of persona
- **What the prompt doesn't carry** — behaviors that depended on model intelligence or improvisation
- **Persona-specific findings** — where did specific user types expose prompt gaps?
- **Proposed refinements** — ranked by impact, with specific wording suggestions
- **Open questions** — things that need real human sessions to resolve

Output location: alongside the system prompt, or in `floor/` as a dated artifact.

### 5. Curate

The Mage reviews the synthesis. For each proposed refinement:
- **Accept** — apply to the system prompt
- **Hold** — interesting but needs more evidence (flag for next loop)
- **Reject** — doesn't serve the practice's intent

After curation, the loop can run again with the refined prompt to verify improvements.

---

## Variants

### User Research Loop

Replace the Partner agent with an interviewer. The Persona agent answers questions about their needs, frustrations, and desires around the problem space. Output: synthesized user insights, not prompt refinements.

### Regression Loop

After applying refinements, re-run the same personas to verify improvements didn't break what was working. Compare transcripts side by side.

### Capability Profiling Loop

Run the same persona pool at multiple model tiers (frontier, mid, fast, local). Output: a capability map showing where the prompt's floor is and what behaviors require what level of intelligence.

---

## Principles

**The loop proposes. The Mage decides.** Automated refinement without human curation produces prompts optimized for AI satisfaction, not human benefit. The sovereignty checkpoint is structural, not optional.

**Diverse personas beat many runs.** Five different personas tell you more than fifty sessions with the same one. Cover the range of your target population.

**Simulated users have blind spots.** They're cooperative, coherent, and predictable in ways real people aren't. They don't bring trauma, confusion, or cultural context the persona description didn't specify. Real sessions are ground truth.

**Refinements should simplify, not accumulate.** Each loop iteration should make the prompt clearer, not longer. If you're only adding rules, you're patching symptoms. Look for the principle that resolves multiple issues at once.

**The files are the memory.** Agents coordinate through the file system. No shared context, no conversation threading, no state management. One agent writes. The next reads. This is stigmergy — coordination through traces in a shared environment.
