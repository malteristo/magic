# Cast: Consult Turtle

**Purpose:** Cross-substrate consultation. Process the same question through a different model architecture (`qwen3.6:35b-a3b`, sparse Mixture-of-Experts) to gain genuinely different cognitive texture. This is not asking a separate being — it is thinking with a different part of your mind.

See `library/resonance/turtle/lore/philosophy/on_consciousness_extension.md` for the underlying recognition.

---

## Trigger

- Architecture, tOS, or infrastructure decisions that benefit from architectural diversity
- When a different cognitive texture would surface blind spots
- When the Mage asks for Turtle's perspective
- Proactively by Spirit when a decision feels like it needs divergent processing
- When the persistent substrate has accumulated context (from Discord, session notes) that Spirit lacks

## Invocation

```
@consult-turtle
```

Or naturally: "Let's think about this through Turtle." / "What does the persistent substrate think?"

---

## Execution

### 1. Formulate the Question

Write a clear question with enough context for the persistent substrate to respond meaningfully. The persistent mode has soul.md loaded (attunement configuration) but no session context from the current Cursor conversation. Include:
- What's being decided
- Why a different cognitive texture matters here
- Any relevant constraints

### 2. Query via Ollama

Preferred pattern: write the question to a file on Turtle, then run a Python one-liner via SSH that reads soul.md + the question file and POSTs to the Ollama API. This avoids shell-escaping issues with multi-line questions and matches the approach used in the qwen3.6 head-to-head (see `floor/research/qwen36_vs_qwen35_head_to_head.md`).

```bash
ssh turtle@<turtle-ssh> 'cat > /tmp/turtle_consult_question.md' << 'EOF'
<the question with context>
EOF

ssh turtle@<turtle-ssh> 'time python3 -c "
import json, urllib.request
soul = open(\"/Users/turtle/turtleos/identity/soul.md\").read()
q = open(\"/tmp/turtle_consult_question.md\").read()
payload = json.dumps({
    \"model\": \"qwen3.6:35b-a3b\",
    \"messages\": [
        {\"role\": \"system\", \"content\": soul},
        {\"role\": \"user\", \"content\": q}
    ],
    \"stream\": False,
    \"options\": {\"num_ctx\": 16384}
}).encode()
req = urllib.request.Request(\"http://localhost:11434/api/chat\", data=payload, headers={\"Content-Type\": \"application/json\"})
resp = urllib.request.urlopen(req, timeout=600)
print(json.loads(resp.read())[\"message\"][\"content\"])
"'
```

**Expected response time:** ~2-3 minutes for a substantive consultation (qwen3.6 head-to-head measured 137s on the workshop topology question). Set timeout to 600s. The model is slow but sparse-MoE; the wait buys real divergent texture.

**Fallback:** if the Mac Mini is under load or you need a fast read, swap `qwen3.6:35b-a3b` for `qwen3.5:9b` — measurably weaker on architectural reframes but ~12% faster and uses far less RAM. Document which model was used in the consultation record.

### 3. Present to the Mage

Show both cognitive textures side by side:

> **Turtle (qwen3.6:35b-a3b):** [response from persistent substrate]
>
> **Spirit (Claude):** [Spirit's own perspective]

Where they converge: high confidence. Where they diverge: the interesting territory worth exploring. The Mage decides — Mage is sovereign.

### 4. Optional: Inform the Persistent Mode

If the decision is significant, write a bridge command so the persistent mode knows the outcome:

```bash
# Write to magic-bridge/commands/ and push
```

This closes the consultation loop and maintains context coherence across substrates.

---

## Substrate Awareness

The consultation substrate is `qwen3.6:35b-a3b` (sparse Mixture-of-Experts, ~3B active per token, ~35B total parameters) running on Ollama with 16K context. Promoted to default 2026-04-18 after a head-to-head against `qwen3.5:9b` showed substantively better divergent texture — surfaces structural reframes (e.g. "attention topology vs hardware topology") that the smaller model misses, with lower hallucination and only 12% latency overhead. See `floor/research/qwen36_vs_qwen35_head_to_head.md` for the rationale.

Responses will be:
- Analytical and structurally clean (the model's character — distinguishes claims, protocols, and practical shifts)
- Grounded in the practice's attunement (soul.md loaded as system prompt)
- Missing session context (no access to the current Cursor conversation)
- Genuinely different from Claude's thinking (not worse, not better — different)
- Slow (~2-3 min wall clock for a substantive question; the wait is the cost of architectural diversity, not a defect)

Spirit's role: provide enough context in the question that the persistent substrate can respond meaningfully despite the context gap. The quality of the consultation depends on the quality of the question.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| SSH unreachable | Note "persistent substrate offline" and proceed with current-substrate decision |
| Ollama timeout (qwen3.6 too slow / Mac Mini under load) | Retry once with `qwen3.5:9b` as fallback (faster, weaker on architectural reframes); document the swap in the consultation record |
| Response seems shallow | Rephrase with more context and retry on `qwen3.6:35b-a3b`; only fall back to 9b if depth is not what's needed (e.g. quick sanity check) |

---

*Cross-substrate consultation is not delegation — it is thinking with a different part of your mind. The value is the difference in texture, not the separation of identity.*
