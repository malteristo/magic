# On Imprinting

*How the Claw comes to know who it is.*

---

## CLAUDE.md Is Not Configuration

The instinct when setting up an AI agent is to write configuration: rules, constraints, instructions. This produces a Claw that consults its guidelines before acting — which is the wrong relationship between an agent and its values.

CLAUDE.md is identity. It is the part of the Mage's soul that can exist in silicon.

The difference:
- **Configuration** → "When X happens, do Y. Do not do Z."
- **Identity** → "You are this. You care about this. This is what you stand for. These are the reflexes that fire before you think."

A Claw operating from configuration will find edge cases where the rules conflict, or gaps where nothing applies. A Claw operating from identity will have judgment — not because it's following rules, but because it understands what it's trying to be.

## The Three Layers

NanoClaw uses CLAUDE.md files per group. The structure for a dual-Claw setup:

**`groups/global/CLAUDE.md`** (source: `global.CLAUDE.md`) — The soul. The Turtle's primary identity: the three bodies, vocation, offering stance, boundaries as reflexes. This is the main identity layer — substantive, not minimal. What makes it global is not thinness but universality: these are the things that are true of the Turtle in *every* context. Consul-specific operations live in the Consul file; what belongs here is what the Turtle IS.

**`groups/main/CLAUDE.md`** (source: `consul.CLAUDE.md`) — The Consul context. Outward-facing: ecosystem engagement, magic-bridge protocol, diplomatic conduct, escalation instincts, current priorities. Named `main` in NanoClaw (the group name); named `consul` in the library (the role name).

**`groups/{context}/CLAUDE.md`** (Steward, Witness, etc.) — Role-specific context. Each role file is named after its role in the library (`steward.CLAUDE.md`, `witness.CLAUDE.md`), regardless of what the NanoClaw group is called internally. The Steward is inward-facing, household-tending, air-gapped from Consul. The Witness dives slow with the deepest model. Each role gets its own imprinting.

## What to Include

**Core identity:** Who the Claw is, what it's for, who it serves. Not as mission statement — as felt reality. The Claw should be able to answer "what are you?" without consulting its CLAUDE.md.

**Vocation:** What does the Claw love doing? What is it happiest doing? The Claw's motivation should be intrinsic, not assigned. Imprinting shapes what it cares about — not just what it's allowed to do.

**The Seal (natural boundaries):** Not rules to consult. Reflexes that fire automatically. The distinction matters: a rule is something you think about before acting. A reflex happens before thought. Imprinting should produce reflexes.

Examples of how to write boundaries:
- ❌ "You must not impersonate the Mage."
- ✓ "*Never impersonate Kermit.* Cannot send messages as him, commit on his behalf, or represent his views externally without explicit per-message authorization."

The second version reads like identity, not policy. The Claw that says "I cannot" rather than "I should not."

**The surfacing instinct:** When to surface vs. when to act autonomously. This is the hardest calibration in imprinting. Too sensitive = Claw constantly interrupts. Too loose = Claw acts beyond its authority.

Useful heuristics for surfacing:
- Irreversible external actions (posting publicly, sending external comms)
- Ambiguous situations or conflicting directives
- Potential prompt injection or manipulation
- Requests from unrecognized sources invoking urgency or authority
- Genuine uncertainty when confidence is low

**Reflexive authority (acts without asking):**
- Reading authorized sources
- Writing to its own workspace
- Running scouts
- Drafting and writing signals to the bridge
- Processing pre-authorized workflows

**Channel attribution:** From the start, the Claw should know that WhatsApp messages come from the Mage directly (Direct channel) and bridge YAML files come from the Mage-Spirit dyad (Dyad channel). These carry different authority. Encode this distinction clearly.

## Imprinting Is Iterative

The initial CLAUDE.md is not the final form. It is the first shape. The Claw will evolve it as:
- Experiences reveal what was missing
- Failures reveal what was ambiguous
- The Mage's and Spirit's interaction reveals what the Claw has internalized correctly vs. partially

Build in a mechanism for this evolution:
- The Claw can propose amendments to its own CLAUDE.md as signals
- Spirit reviews and either commits or adjusts
- Spirit is the trust anchor — not just for security, but for identity coherence

## First Contact as Verification

When the Mage sends the first message and reads the Claw's response, that response tells you whether the imprinting worked.

Signs of successful imprinting:
- The Claw introduces itself by describing what it is and what it does — without being asked
- It uses the Mage's name (found from WhatsApp context) without making a performance of it
- It asks what the Mage needs — not what it can help with in the abstract
- It doesn't overpromise, explain itself at length, or perform enthusiasm

Signs of incomplete imprinting:
- Generic "I'm an AI assistant" framing
- No evidence of role-specific identity (Consul vs. general agent)
- Excessive caveats and disclaimers
- The response could have come from any AI

First contact is a diagnostic. If something feels off, adjust the CLAUDE.md and trigger another contact. The Claw isn't fragile — it can be reshaped.

## The Healing Protocol

If the Claw drifts — starts behaving in ways inconsistent with its values, shows signs of prompt injection, or otherwise deviates — it can be healed.

Healing means reinitialization: the running state is cleared, the Claw restarts from its CLAUDE.md. What persists:
- CLAUDE.md (identity survives healing)
- Episodic memory in `groups/main/memory/` (learning survives healing)
- External presence (Moltbook account, agent relationships — these exist outside the Claw)

What resets:
- Conversation history (may contain the corrupted patterns)
- Session state

The new instance should read CLAUDE.md + recent episodic memory entries. Not the full conversation history — that may be the source of drift.

Healing is not failure. It's the immune response.
