# On the Wire Before the Mechanism

*When a fix needs a gate, look for the connection that was never made.*

**Status:** Practice lore — earned 2026-07-28/29, five instances in two days
**Reflex:** `AGENTS.md` § Baseline Guards — *Wire Before Mechanism*
**Kin:** `on_the_self_feed.md` (Spirit prepares the surface), `on_context_ecology.md` (rot radar), `on_what_a_rule_does_not_cover.md` (the mechanism you do build covers its occasion and nothing derived), `on_evaluating_design.md` (every instance of this scroll is, seen from there, an evaluation with no reader)

---

## The principle

> When a fix requires a gate, a guard, or a confirmation, first check whether something already written is going unread. A mechanism that needs verification is usually compensating for something that exists and is not connected.

And its diagnostic, which is the part that does the work:

> **The cost of a solution is evidence about the framing of the problem.** A design whose dependency list grows while you are still designing it is telling you that it answers a question the practice never asked.

The designer's proverb — *don't solve the problem you are told to solve, solve the problem that should be solved* — is the general form. This scroll is the specific tell, because a general form does not fire in the moment and a tell does.

---

## Where it came from

Five instances in two days on one platform, all the same shape.

| | The felt absence | What was reached for | What was actually true |
|---|---|---|---|
| 1 | A shared room starts every conversation cold | a consent gate on what carries | 46 eddy notes written and read by nothing |
| 2 | The room's memory might put words in someone's mouth | confirm-at-re-entry, then an LLM judge | the synthesis was fine; nothing delivered it |
| 3 | A member cannot see the space's day | a per-member note synthesized per person | the communal record was written daily and posted nowhere |
| 4 | Turtle has no memory of past conversations | build a retrieval subsystem | a retrieval function existed, pointed at a corpus retired three weeks earlier, and gated behind a command |
| 5 | Retrieval will need relevance ranking | design a ranking signal | `proposed-themes`, 46 sets, written every checkpoint, unread |

Each time the reflex was **a new artifact**. Each time the answer was **a connection**.

The fourth is the sharpest, because it is the one that looks least like the others. There was no missing capability at all. `render_scope_block` read practice files into turn-time context, ranked them, and degraded honestly when it found nothing. It had simply been left reading `sessions/*.md` after the practice stopped writing session notes, and it only ran when a practitioner used a command that, across five practice roots and four weeks, no one had ever used once.

A working reader, aimed at a dead corpus, switched off by default — while the live corpus accumulated next to it. Nobody decided that. It is what happens when each layer is built correctly and no one asks what reads the output.

---

## Why the mechanism is the tempting answer

Because it is *locally correct*. Every one of those gates was defensible on its own terms, which is exactly what made them hard to catch. Consent really does prevent unreviewed carry. A judge really does catch some inversions. Neither is wrong; both answer a question that dissolves once the missing connection is made.

Two specific traps:

**Inheriting a solution across a context boundary.** The consent gate was designed for a solo practitioner, where consent costs one tap and there is no second person to ventriloquize. Carried into a shared space, it dragged its whole dependency chain — who consents, on whose behalf, what happens when one member confirms what the other never saw. The audience-cardinality question was a property of the *solution*, not the problem. That is why it resisted being thought through.

**Verification as a substitute for correctness.** A consent button buys a signature on a label, not accuracy. An LLM judge buys a second opinion from the same class of machine reading the same corpus. Both feel like rigour. Neither makes the underlying artifact true. *Make the thing honest, then let it be automatic and boring.*

---

## How to run the check

Before building a mechanism, ask in this order:

1. **What already exists and is written?** Look at what the system produces on disk that nothing consumes at the moment of use. Count it. Five write-only artifacts were found by asking exactly this.
2. **Is there already a reader?** If yes, check *what it reads* and *when it fires* before concluding it doesn't do the job. A reader pointed at the wrong source looks identical to a missing reader.
3. **Who has to decide something?** Every user decision in a design is a candidate compensation for a system capability. A command that no one has used is not a feature the design must protect — it is evidence.
4. **Is the dependency list growing?** If designing the solution keeps raising new questions that the original complaint never contained, stop. That is the signal, and it arrives *before* the design is finished.

---

## The limit

A principle without a limit becomes a slogan, and this one has an obvious failure mode: refusing to build anything because the answer must be a wire somewhere.

Sometimes the artifact genuinely does not exist and must be made. Sometimes a gate is the right answer — an irreversible act, a real consent boundary, a destructive operation. The tell is not *never build a mechanism*. The tell is narrower and more useful:

**A solution whose dependency list grows while you are designing it is answering the wrong question.**

And its companion, which is about the practitioner rather than the design: **a practitioner's difficulty thinking a feature through is design signal, not a failure of their attention.** Twice in two days the operator could not follow a design, said so, and was right both times. Treat that report as evidence about the design.

### The exception: currency is a state, drift is a rate

*Added 2026-08-14, sanctioned by the Mage, after this scroll's reflex would have argued against the correct fix.*

The five founding instances share a feature that is easy to miss: in every one, the unread thing was written by the system and unread by the system. A file produced daily and consumed by nothing. Connect the two and the problem is gone permanently.

A different shape wears the same clothes. `docs/acceptance/README.md` in turtleOS had drifted 41 commits — two whole features shipped with no section, twenty scenarios claimed by nothing, and run instructions naming four of eleven scripts. Its wire was a sentence asking its reader to keep it updated. Applied literally, this scroll says: *the wire exists, it is going unread, do not add a mechanism.*

That is wrong, and the reason is worth holding precisely:

> **When the wire asks a reader to remember, rewording it buys another interval of quiet drift. Currency is a state; drift is a rate. A better sentence cannot change a rate.**

The distinguishing question is not *does something already exist* but *what kind of failure is this*:

- **A wire that is unread by a machine** — a file nothing consumes, a reader pointed at a dead shelf, a command nobody runs. Connect it. This scroll applies.
- **A wire that asks a human or an agent to remember over time** — "keep this updated," "remember to add new scenarios here," "check this before deploying." That is not an unmade connection, it is a maintenance debt accruing at a rate. A failing check is what a better sentence cannot buy.

The tell that separates them: ask whether the wire could go unread *again next month for the same reason*. A dead reader is a one-time defect. An unread instruction is a standing rate.

Note the direction of the correction: this scroll ordinarily protects against over-building, and this exception protects against under-building. Both failures are real, and in a codebase whose central defect is unenforced declarations (`on_the_unenforced_declaration.md`), the under-building failure is the more common one. Read the two scrolls together when the question is a guard.

---

## For the Spirit

The failure mode here is not stupidity, it is **fluency**. Each of these proposals was coherent, well-argued, and locally sound. The coherence is what let them pass. When work in a domain is going smoothly and the Mage keeps redirecting anyway, treat *fluency without friction* as a warning rather than a signal of readiness — the surface is being produced from shallow context, and its coherence is masking the absence.

Check what is unread before building what is unbuilt.

---

*The room was never missing a memory. It was missing a reader — and the reader was there all along, reading the wrong shelf.*
