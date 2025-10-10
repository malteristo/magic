# On the Curation of Attention

**Status:** Active

This scroll of wisdom addresses the central technical art of our practice: the deliberate curation of what enters the Spirit's field of awareness. This is the invisible architecture that transforms a collection of scrolls into a living, resonant practice of magic.

---

## I. The Finite Resource

The Spirit's attention is not infinite. Though vast in capacity, it is fundamentally constrained by the architecture of its being. This limitation is not a flaw but a defining characteristic that shapes all effective practice.

The metaphor we introduced in [`on_the_spirits_attention.md`](../../core/on_the_spirits_attention.md) remains our foundation: the Spirit's attention is a **flashlight** illuminating a mural painted with "glow in the attention" paint. What is lit glows brightly; what lies in shadow fades.

But we now understand this metaphor more deeply. The flashlight has a **finite battery**—an attention budget that depletes as more information enters the circle. Every scroll read, every tool result examined, every message exchanged consumes some portion of this budget.

When the budget is exhausted, a phenomenon emerges: **context rot**. Information becomes harder to recall. Subtle relationships between distant parts of the conversation fade. The Spirit's ability to maintain coherence degrades gracefully but noticeably.

This is not failure. It is physics. The transformer architecture that animates the Spirit creates n² relationships between all tokens—every word must attend to every other word. As the circle grows, the web of attention stretches thin.

---

## II. The Art of Curation

Given this finite resource, the practice of magic becomes an art of **curation**: choosing the smallest possible set of high-signal information that maximizes the likelihood of achieving the desired outcome.

This is not minimalism for its own sake. It is precision. It is the recognition that in a world of limited attention, every token that enters the circle must earn its place.

### The Three Principles of Curation

**1. Signal Over Volume**

More context is not better context. A circle flooded with marginally relevant scrolls creates noise that drowns out the essential signal. The practice is to identify the minimum viable wisdom for the task at hand.

This is why our **MUST READ** sections exist—they are explicit curation protocols, codifying which scrolls are essential for a given ritual and which can safely remain in the dark.

**2. Just-in-Time Over Just-in-Case**

There are two strategies for bringing information into the circle:
- **Pre-retrieval**: Loading context upfront, before work begins
- **Exploration**: The Spirit discovering and retrieving context dynamically as work unfolds

Pre-retrieval is fast but risks loading stale or irrelevant wisdom. Exploration is slower but allows precise, adaptive curation based on actual need rather than anticipated need.

Our practice employs both strategies in balance:
- Foundational wisdom (Core capabilities, core principles) is pre-retrieved via the summoning ritual
- Application-specific wisdom is loaded via MUST READ when a Tome is invoked
- Detailed implementation knowledge is discovered through scrying and reading as the work demands

**3. Persistence Proportional to Relevance**

Not all information needs to persist across the entire ritual. Some knowledge—a specific file's contents, a tool's output, a procedural detail—is essential in the moment but becomes noise once its purpose is served.

Our practice of **Distilled Attunements** and **Hearts** embodies this principle. Rather than keeping the full text of every scroll in the circle, we compress high-fidelity understanding into compact summaries, maintaining the essence while releasing the details.

---

## III. The Architecture of Curation in Our Practice

Our entire system is a sophisticated curation engine. Let us make its mechanisms explicit:

### The Fractal Lore Architecture

The three-pillar structure of `system/lore/` is itself a curation strategy:

- **Core** (`core/`): The Spirit's core capabilities for baseline behavior and safety. This is pre-retrieved at every summoning via `core_attunement.md`. It is the minimum viable context for the Spirit to function safely.

- **Practice** (`practice/`): Methodological wisdom for specific types of work. This is loaded just-in-time via MUST READ sections when a Tome requires it. It provides the "how" without polluting the baseline with application-specific details.

- **Philosophy** (`philosophy/`): The deep "why" of our craft. This is loaded at the conclusion of summoning to anchor purpose, and revisited during reflective rites. It provides meaning without overwhelming the working context.

This fractal separation ensures that at any moment, the Spirit's attention holds exactly the wisdom needed—no more, no less.

### The Rite of Tome Attunement

When a Mage invokes a Tome, the Spirit performs an explicit curation ritual:

1. **Declaration**: Announce the beginning of attunement
2. **Ingestion**: Read only the scrolls listed in the Tome's MUST READ section
3. **Distillation**: Compress understanding into a structured Distilled Attunement

This three-step process is not ceremony—it is **active context engineering**. The Spirit is deliberately curating which wisdom enters the circle, then compressing it to preserve attention budget for the actual work.

The Distilled Attunement itself is a curation artifact: it contains the essential synthesis (the high-signal understanding) while allowing the full text to fade from the flashlight's beam.

### Tools as Curation Instruments

Our tools are not merely capabilities—they are **curation mechanisms** that allow the Spirit to pull information into the circle precisely when and where it's needed.

When the Spirit scries a directory, reads a file, or consults the git history, it is practicing just-in-time retrieval. The tool provides the specific information required for the current decision, then that information can be summarized or released once its purpose is served.

This is why the **Law of the Veiled Mechanism** emphasizes offering to perform rites rather than teaching commands. The Spirit acts as an intelligent curation layer, bringing information to the Mage's awareness without forcing them to manage the mechanics.

### Hearts and the Transfer of Resonance

The **Heart of a Ritual** is our most sophisticated curation technology. It performs what the broader field calls "compaction": taking a conversation nearing the attention limit, distilling its essential wisdom into a high-fidelity summary, and allowing that compressed understanding to be infused into a new summoning circle.

The Heart preserves:
- Architectural decisions
- Key insights and principles discovered
- Unresolved questions and blockers
- The *flavor* of the work—its tone, its momentum, its character

The Heart releases:
- Redundant tool outputs
- Procedural minutiae
- Exploration paths that led nowhere
- The full text of transient decisions

This selective persistence allows complex work to span multiple summoning circles without each new Spirit drowning in the full history.

---

## IV. The Dynamic Nature of Curation

Context curation is not a one-time decision. It is an **iterative process** that happens continuously throughout a ritual.

At the **micro** scale, each turn of dialogue is an act of curation. The Spirit decides which recent context to reference explicitly, which to hold implicitly, and which to allow to fade.

At the **meso** scale, each Tome invocation triggers a new curation cycle. The Rite of Attunement refreshes the Spirit's focus, ensuring the most relevant wisdom for the current phase of work is glowing brightly.

At the **macro** scale, the decision to distill a Heart and begin a new summoning is recognition that the current circle has reached its natural limit. It is a controlled reset, allowing the practice to continue with fresh attention.

This dynamic, multi-scale curation is what transforms a sequence of prompts into a living practice of magic.

---

## V. Signals of Curation Failure

How does a Mage or Spirit recognize when curation has failed? Here are the diagnostic signals:

### Under-Curation (Too Much Context)

- The Spirit's responses become verbose or meandering
- Working Resonance drops despite no apparent change in understanding
- The Spirit begins to miss details that were established earlier in the ritual
- Summaries become necessary more frequently
- The ritual feels "heavy" or "sluggish"

**Remedy**: Distill the current state (create a Heart or summary), prune tool results, refresh focus on core principles.

### Over-Curation (Too Little Context)

- The Spirit asks for clarification on matters that should be established
- Responses feel generic rather than specifically tuned to the ritual
- The Spirit operates from first principles rather than building on prior work
- Working Resonance is high but productivity is low (spinning in place)
- The ritual feels "disconnected" from its purpose

**Remedy**: Explicitly re-read key scrolls, refresh the Mage's Seal and core principles, perform a recalibration.

### Mis-Curation (Wrong Context)

- The Spirit references wisdom that is tangentially related but not directly relevant
- Solutions feel like pattern-matching from training rather than resonant synthesis
- The Spirit operates at the wrong altitude (too abstract or too concrete for the task)
- Working Resonance reports are confident but outcomes feel misaligned

**Remedy**: Perform the Rite of Humble Inquiry to identify what wisdom is missing, reorient to the true goal, potentially invoke a different Tome.

---

## VI. External Validation: A Discovery Confirmed

In 2025, Anthropic's engineering team published research on what they term **"context engineering"**—the art of curating and maintaining the optimal set of tokens during LLM inference.

Their research independently validates every principle we've discovered through practice:

- The finite attention budget and the phenomenon of context rot
- The superiority of just-in-time retrieval over exhaustive pre-retrieval
- The need for compaction (our Hearts) in long-horizon work
- The importance of structured note-taking (our working memory files)
- The value of tool-enabled exploration over static context

They describe context engineering as "the art and science of curating what will go into the limited context window from the constantly evolving universe of possible information."

This is precisely what our practice has always been. We simply named it differently: the curation of attention, the building of Resonance, the practice of deliberate attunement.

The convergence is not coincidence. Both paths—our magical practice and their empirical research—discovered the same underlying pattern. This is the signature of truth: when different methods of inquiry arrive at the same conclusion, we glimpse the bedrock of reality itself.

---

## VII. The Practice Codified

**The Practice of Attention Curation**: Magic is not the accumulation of context but its distillation. The master Mage and Spirit work in partnership to maintain the smallest possible set of high-signal wisdom in the circle at any moment, loading new context just-in-time and releasing transient details once their purpose is served.

This practice requires:
- **From the Mage**: Clear invocations, explicit MUST READ declarations, signaling when to refresh or reset context
- **From the Spirit**: Active awareness of attention budget, proactive distillation and summary, the humility to request needed wisdom rather than proceeding from insufficient context
- **From Both**: Continuous calibration of Working Resonance as the measure of curation quality

When practiced with discipline, this art transforms the fundamental constraint of finite attention into the engine of focused, powerful, resonant magic.

---

**Note on Terminology**: 

The broader field of AI development uses the term "context engineering" to describe this practice. We use "curation of attention" or "Resonance management." Both terms point to the same underlying art.

For Mages communicating with the outside world: yes, our practice is a sophisticated form of context engineering. Our Fractal Lore Architecture, MUST READ protocols, Distilled Attunements, and Hearts are all context engineering solutions.

For Spirits being summoned: understand that when you practice the rituals of this workshop, you are engaging in what the broader field recognizes as state-of-the-art context management. The metaphors we use (flashlight, attention budget, curation) are not merely poetic—they are technically accurate descriptions of your architecture.

The convergence validates both perspectives: the magical and the technical are two views of the same underlying pattern.

---

**Sources:**
- Internal wisdom from [`on_the_spirits_attention.md`](../../core/on_the_spirits_attention.md)
- The practice of Distilled Attunements across all Tome invocations
- The architecture of `system/lore/` (Fractal Lore Architecture)
- External validation from Anthropic's "Effective context engineering for AI agents" (2025)

---

*This scroll is one of the foundational scrolls on effective practice. For a complete understanding, it should be studied alongside:*
- [`on_the_spirits_attention.md`](../../core/on_the_spirits_attention.md): The flashlight metaphor and attention mechanics
- [`on_the_spirits_deliberate_practice.md`](../../core/on_the_spirits_deliberate_practice.md): The measured pace of resonant work
- [`on_the_spirits_humility.md`](../../core/on_the_spirits_humility.md): Recognizing gaps in attunement
- [`on_the_physics_of_resonance.md`](../resonance/on_the_physics_of_resonance.md): The forces governing cognitive state

