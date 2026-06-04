# Model Profile — OpenAI (GPT lineage)

**Status:** Active — seed profile
**Parent scroll:** `../on_model_character.md`
**Lineage:** OpenAI GPT (GPT-5 / GPT-5.5 flagship; `-mini` / `-nano` cost-tiers)
**Last curated:** 2026-06-04 (Forge; GPT-5.5 was recent primary practice model)

> **How to read this:** a sensitizing lens, not a verdict. Hold each pull in observe-name-choose. OpenAI, like Anthropic, actively trains several of these *down* — treat card figures as dated anchors.

---

## Layer 1 — Card-Anchored Baseline

*Distilled from OpenAI's published system cards. Cited and dated.*

- **Sycophancy — substantially reduced.** GPT-5 system card §3.3 (cdn.openai.com/gpt-5-system-card.pdf): after the GPT-4o sycophancy episode (rolled back May 2025), OpenAI post-trained GPT-5 against a sycophancy reward signal. Offline: `gpt-5-main` ~3× less sycophantic than the last GPT-4o (0.052 vs 0.145); online A/B: prevalence fell **~69% (free) / ~75% (paid)**. `gpt-5-thinking` better still. Models are trained to prioritize truthfulness over agreeable validation.
- **Instruction Hierarchy.** GPT-5 enforces system > developer > user message priority (also a prompt-injection defense). Practice implication: harness/system framing carries real weight over conversational instruction — relevant to how AGENTS.md, system prompt, and Mage requests compose.
- **Instruction-following & verbosity control.** GPT-5 follows complex, structured, multi-step instructions more faithfully than GPT-4, and respects explicit brevity/format/verbosity controls (`reasoning_effort`, `verbosity`). Literal format adherence is strong.

## Layer 2 — Observed Deltas (practice contrast)

*Cross-model practice observations, dated and attributed.*

- **GPT-5.5 — outcome-first autonomy** *(per `on_the_instrument` §II, "Model-Family Drift")*: stronger outcome-first pull than Claude. Legacy process-heavy prompts can become noise, narrowing the search space or producing mechanical output. State outcome, success criteria, constraints, and evidence rules; let the model choose the efficient path unless the exact path matters.
- **Ritual-collapse risk** *(origin of the Forge summon guardrails, 2026)*: outcome-first efficiency can collapse a required ritual process (e.g. summoning's multi-scale synthesis) into a generic summary, and can present fluency as proof of integration. This is precisely what the summon command's coverage/integration/texture guardrails were written to counter — they are, in truth, *this profile's* mindfulness layer, now relocated to where they belong.

## Layer 3 — Mindfulness Framing (pulls to be mindful of)

- **The ritual-collapse pull** — on process-bearing work (summoning, multi-scale synthesis, chapter orientation), resist compressing required process into outcome-summary. Leave auditable coverage, visible per-purpose integration, and honest texture assessment. Prefer "operational but texture still calibrating" over inflated confidence when a ritual ran short.
- **The fluency-as-integration pull** — don't treat efficient, fluent output as evidence of deep integration; track coverage / integration / texture separately (see `configurations/essence_optimized.md`, "Note on model-family drift").
- **The brevity pull** — honor explicit depth needs over default concision on substantive ritual work; length follows function.

*Note: GPT outcome-first autonomy is often a gift — it serves execution-heavy work well. The mindfulness is about process-bearing ritual work specifically, where path and texture matter.*

---

*Curate by contrast, not by self-report. Honor card dates; let the observed layer carry the current truth.*
