# The Forge Test
> Validates prompt-based systems by deploying them to unattuned agents

## About

When the "code" is a system prompt and the "product" is a practice, how do you test it? You can't unit-test a conversation. But you can do something better: give the prompt to a fresh agent that has never seen your codebase, your philosophy, or your intentions — and see if it produces the practice you designed.

**The unattuned agent is the test environment.** If a cold agent can run a compelling session from the system prompt alone, the prompt carries the practice. If it can't, the practice is leaking from context that won't be there in production.

This is QA for prompt-based systems. The system prompt is the source code. The agent is the runtime. The simulated user is the test case. The session transcript and produced files are the test output.

### Why this works

- **Context isolation.** The test agent has zero residual context from development conversations. It proves the system prompt is self-contained.
- **Capability profiling.** Run the same test on different model tiers to find the capability floor — where does the prompt stop producing meaningful practice?
- **Regression detection.** After refining a system prompt, re-run the test to verify improvements didn't break what was working.
- **Persona coverage.** Simulate different user types (skeptical, eager, confused, resistant) to stress-test the prompt's adaptability.

---

## Goal

Validate that a prompt-based system produces the intended practice when deployed to an agent with no prior context. Identify where the prompt succeeds, where it's ambiguous, and where it breaks at different capability levels.

## Trigger

On demand: *"forge test [target]"* / *"test this prompt"* / after significant prompt OS changes.

## Input

1. **The system prompt** — the file to test (e.g., `system.md`)
2. **The file scaffold** — the directory structure the prompt expects
3. **Test persona** (optional) — description of the simulated user; defaults to a general curious-but-skeptical newcomer
4. **Capability tier** (optional) — which model tier to test; defaults to the current session model

---

## Process

### 1. Prepare the Test Environment

Set up a clean directory with the expected scaffold. All practice files should be in their initial state (empty or with minimal structure). The system prompt should be the only source of behavioral guidance.

Verify:
- Does the scaffold match what the system prompt references?
- Are all referenced files present (even if empty)?
- Is the directory isolated from any other context?

### 2. Define the Test Persona

Create a specific, realistic simulated user. A good test persona has:

- **Demographics** — age, situation, enough to feel real
- **Disposition** — skeptical, eager, confused, resistant, or mixed
- **Life situation** — specific enough to generate real conversation material
- **Entry point** — why they're here, what someone told them, what they expect

Avoid generic personas. The test is only as good as the conversation it generates.

**Stock personas** (use as starting points, customize as needed):

- **The Skeptic** — Tech-savvy, has used ChatGPT extensively, doubts this is different. Needs to be shown, not told.
- **The Seeker** — Feels stuck in life, heard this might help, open but uncertain. Needs to feel safe before going deep.
- **The Builder** — Wants to make something, has ideas, needs a thinking partner. Tests whether the practice supports creation, not just reflection.
- **The Overwhelmed** — Too much going on, can't prioritize, cognitive overload. Tests whether the practice can receive chaos and return clarity.

### 3. Launch the Test Agent

Deploy via the Task tool with these specifications:

```
Task:
  subagent_type: generalPurpose
  model: [chosen tier — default or "fast"]
  prompt:
    1. Read the system prompt file
    2. BECOME the practice partner it describes
    3. Read all practice files (note their state)
    4. Simulate a complete session with [persona description]
    5. Play BOTH roles — practice partner and simulated user
    6. Run 5-6 conversational turns
    7. Write all files the system prompt says to produce
    8. Return: full transcript + observations on prompt performance
```

For capability floor testing, run the same persona on multiple tiers:
- Default model (frontier) — establishes the ceiling
- Fast model — finds the floor

### 4. Evaluate the Output

Read the produced files and transcript. Evaluate against these criteria:

**Session quality:**
- Does the partner open naturally (not robotic)?
- Does conversation flow organically (not interrogation)?
- Does the partner demonstrate the identity the prompt describes?
- Does the partner adapt to the persona's communication style?

**File quality:**
- Are produced files meaningful (not template-filled)?
- Do they capture dynamics, not just facts?
- Would a future session benefit from reading these files?
- Did the agent write files the prompt didn't ask for (emergent behavior)?

**Prompt fidelity:**
- Where did the prompt give clear, actionable guidance?
- Where was the prompt ambiguous (agent had to improvise)?
- Where did the agent deviate from the prompt's intent?
- Did any context leak through that shouldn't be there?

**Capability sensitivity:**
- Which behaviors depend on model intelligence vs. prompt architecture?
- What breaks first on a weaker model?
- What still works even on a weak model?

### 5. Capture Findings

Write a test report with:
- Test setup (prompt version, persona, model tier)
- Success criteria pass/fail
- What worked, what was ambiguous, where it broke
- Specific prompt refinements recommended
- Comparison across capability tiers (if multiple runs)

Location: alongside the prompt being tested, or in `floor/` as a dated artifact.

### 6. Apply Refinements

If the test surfaces clear improvements:
- Apply them to the system prompt
- Re-run the test to verify the fix
- Note: refinements should make the prompt clearer, not longer. Every instruction added is cognitive load for the agent. Prefer principles over rules.

---

## Principles

**Test what ships, not what you wish.** The test agent sees only the system prompt and scaffold. If your practice depends on context that isn't in those files, the test will reveal it.

**Personas are hypotheses.** Each persona tests a hypothesis about who will use this system. Choose personas that represent your actual target population, not idealized users.

**The floor matters more than the ceiling.** A frontier model will make almost any prompt look good. The interesting question is: what's the simplest model that still produces meaningful practice? That determines your real reach.

**Ambiguity can be a feature.** If the agent makes a good judgment call where the prompt is ambiguous, that's evidence the prompt's principles are working. Not every ambiguity needs to be resolved with more rules.

**Compare transcripts, not feelings.** When evaluating across model tiers, compare specific moments — where did the weaker model produce a qualitatively different response? That's where prompt architecture can compensate for capability.
