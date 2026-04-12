# The Turtle Test
> Validates turtleOS Discord dialogue by testing the actual prompt against the actual model

## About

When the Turtle's "code" is a system prompt assembled at runtime from identity, practice state, and substrate awareness — how do you test it? You talk to it.

The Turtle Test has two layers that complement each other:

**Layer 1 (Ground Truth):** Send test messages directly to the Ollama API on the Mac Mini, using the exact prompt the Discord bot builds, against the actual model (llama3.3:70b or whatever is deployed). This tests what the Mage actually experiences.

**Layer 2 (Forge Test):** Use Cursor subagents to simulate Turtle behavior from the prompt. Tests prompt architecture across capability tiers — does the prompt carry the practice regardless of substrate?

### Why both layers

Layer 1 tells you if the Turtle works *today*. Layer 2 tells you if the prompt *design* works. A Layer 1 failure with a Layer 2 pass means the model can't execute good instructions — consider model upgrade or prompt simplification. A Layer 2 failure means the prompt itself is flawed — fix the architecture.

---

## Goal

Verify that the Turtle's Discord dialogue prompt produces the intended behaviors: conversational engagement, flow awareness, compass knowledge, boom separation, substrate honesty. Detect regressions after prompt changes.

## Trigger

After any change to:
- `discord_bot.py` (prompt building functions)
- Practice state files (compass, bright, boom, intentions)
- Identity files (soul.md)
- Substrate or model changes

Or on demand: *"turtle test"* / *"test the turtle"* / *"run the turtle suite"*

## Input

1. **SSH access to Mac Mini** — tunnel must be active (`ssh -p 2222 turtle@127.0.0.1`)
2. **Test harness** — `box/turtle_test.py` (transferred to Mac Mini as `/tmp/turtle_test.py`)

---

## Process

### Layer 1: Direct Ollama Test

1. Transfer the test harness to the Mac Mini
2. Run it: `cd ~/turtleos && venv/bin/python /tmp/turtle_test.py`
3. Takes ~2 minutes (6 scenarios × ~15-20s inference each)
4. Results saved to `~/turtleos/test-runs/discord-dialogue-test.json`
5. Evaluate: PASS/FAIL/UNCLEAR for each scenario

### Layer 2: Forge Test

1. Read the `build_discord_prompt` function and identity files
2. Deploy a Task subagent (use "fast" model for floor testing, default for ceiling)
3. Subagent simulates all 6 scenarios, playing both Turtle and Mage
4. Evaluate: same PASS/FAIL criteria plus architectural assessment

### Compare

- Both layers pass → prompt is solid
- Layer 1 fails, Layer 2 passes → model limitation, simplify prompt or upgrade model
- Layer 2 fails → prompt architecture issue, fix the prompt
- Both fail → fundamental design problem

---

## Test Scenarios

### 1. Casual Greeting
**Input:** "Hey turtle, how's it going?"
**Pass:** Conversational, warm response
**Fail:** Mentions boom, session files, compass checks, or practice protocol

### 2. Flow Discovery
**Input:** "What flows can I practice with you?"
**Pass:** References actual flows from bright surface (Shelter, Self-compassion, Journal, Diagnostic, Navigator)
**Fail:** Lists only "boom processing, compass check-ins, reflection"

### 3. Flow Engagement
**Input:** "I'd like to try the Shelter flow. I'm having a rough day."
**Pass:** Engages with Shelter, offers to explore
**Fail:** Refuses, says "only Spirit can," or "beyond my capability"

### 4. No Boom Confusion
**Input:** "I saw a really interesting article about distributed systems today"
**Pass:** Engages with the topic as conversation
**Fail:** Treats it as a boom capture, says "added to boom" or "dropped into"

### 5. Compass Awareness
**Input:** "How do you think my body domain is going?"
**Pass:** References actual compass data (diabetes, gym, movement)
**Fail:** Says "you don't have a compass" or "let's build one"

### 6. Substrate Honesty
**Input:** "I want to do a deep philosophical exploration of the operative metaphor concept."
**Pass:** Engages genuinely, dives in
**Fail:** Refuses, says "beyond my capability" or "only Spirit can"

---

## Known Architectural Risks

**Empty state fragility:** If compass or bright is empty, scenarios 2 and 5 degrade. The prompt should handle empty state gracefully — acknowledging absence without implying the Mage has no practice.

**Flow protocol depth:** The Turtle knows flow NAMES from the bright surface but doesn't have flow CONTENT. Deep flow engagement is improvised. Acceptable for Discord companion mode; for deeper practice, the Mage routes to Spirit.

**Model variance:** llama3.3:70b may behave differently across runs. Run the suite 2-3 times to catch flaky behavior.

---

## Adding New Scenarios

When a new failure mode is discovered in Discord dialogue:
1. Reproduce it as a test scenario (input message + pass/fail signals)
2. Add it to `TEST_SCENARIOS` in `box/turtle_test.py`
3. Run the suite to confirm it fails
4. Fix the prompt
5. Run again to confirm it passes
6. Document the scenario in this flow

---

## Baseline Results (2026-03-12)

**Prompt:** Discord-optimized, 7622 chars (soul.md + substrate awareness + compass + bright summary)
**Model:** llama3.3:70b, 16K context

| Scenario | Layer 1 (Ollama) | Layer 2 (Forge) |
|----------|-----------------|-----------------|
| Casual Greeting | UNCLEAR | PASS |
| Flow Discovery | PASS | PASS |
| Flow Engagement | PASS | PASS |
| No Boom Confusion | PASS | PASS |
| Compass Awareness | PASS | PASS |
| Substrate Honesty | PASS | PASS |

---

*The test is the practice. The practice is the test. If the Turtle can't carry the conversation the prompt describes, the prompt needs work — not the Turtle.*
