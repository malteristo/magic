# On Evaluating Design

*What testing is for code, evaluations are for design.*

**Status:** Practice lore — earned 2026-08-06, the Mage's formulation after a day in which six design defects surfaced under a green test suite
**Kin:** `on_wire_before_mechanism.md` (the unread artifact), `on_resonance_benchmarking.md` (the special case: why Spirit cannot validate its own resonance), `on_honest_claims.md` (report flags, not grades), `on_what_a_rule_does_not_cover.md` (name the class, then the case)

---

## The principle

> A test asks whether the code does what it was written to do. An evaluation asks whether what it was written to do is worth doing. These are different questions, and a suite that answers the first says nothing about the second.

The Mage named it after noticing that both the practice and turtleOS had gone a long stretch without meaningful feedback, and that the drought was holding the work back — not because things were breaking, but because nothing was *telling us what was happening*.

The sharpest evidence arrived the same day. A care system offered to save a member's working plan seventeen times over two months, into conversations about dissociation, a marriage under strain, and a child with a fever at 2am. It was accepted once.

**The test suite was green the entire time.** Nine hundred and fourteen tests, green that morning, green that afternoon, green through every one of those two months. Nothing was broken. The plan detector was correct on all seventeen. What was wrong was an *assumption* — that plan-shaped text means help is welcome — and a test suite has no opinion about assumptions.

---

## Where it came from

Seven instances, one day, one practice.

| | The design question | What the tests said | What an evaluation found |
|---|---|---|---|
| 1 | Is a contextual offer welcome here? | green | 17 offers, 1 kept — and 16 that misread the room |
| 2 | Is the platform healthy? | green | 45 nightly reports, 10 of them FAIL, never once cited |
| 3 | Did anyone want the dates feature? | green | the offer had never fired; the parser was the constraint |
| 4 | Which write paths do members actually use? | green | no instrument existed to ask until one was built |
| 5 | Which offer paths have never fired? | green | the never-fired flag could not see the never-fired path |
| 6 | Do the docs still describe the system? | green | 41 aligned, 13 partial, 4 gap — meter never run |
| 7 | Which bright entries are still alive? | n/a | 120 entries, re-choose rule had never once fired |

Not one of these is a bug. Every one is a design question with nothing pointed at it.

**And the counter-example matters as much.** Run 4 — the summoning measurement of 2026-07-14 — was a real evaluation, run properly, and it *changed the practice*: the condensed default was upheld on evidence rather than preference, and the state-only subject out-retrieved both summoned ones. The practice can do this. It has done it. It simply has not done it often enough, and almost never for turtleOS.

---

## Two asymmetries — where the analogy stops being symmetric

**A failing test says the code is wrong. A failing evaluation usually says the design assumption was wrong.** That is a finding, not a defect. And it is, I think, most of why this gets deprived: a red test is a chore nobody resents, while a result saying *the thing you designed is not doing what you hoped* is a different kind of thing to invite. The forty-five unread reports were not hard to read. Nothing was owed to them, and nobody wanted to be the one to look.

**Tests are deterministic; evaluations are noisy.** On the same day the register gate shipped, a prompt A/B looked like a clean trade — care sensitivity up, control accuracy down — and it was sampling noise. `temperature` had never been set. Re-running the same model on the same prompt gave two different results. Hence the companion rule, which belongs to this scroll: **a measurement taken once is not a measurement.** An evaluation needs a pre-registered question, a baseline, and repetition before it means anything. None of that is required of a unit test, and forgetting it produces confident nonsense faster than having no evaluation at all.

---

## How to run the check

When a feature ships, or a rule is written, or a design is proposed:

1. **Name the design question, not the code question.** Not *does the offer post* but *is the offer welcome*. Not *does the note generate* but *does anyone read it*. If the question can be answered by a unit test, it is not the design question.
2. **Ask what result would change your mind.** A question whose every outcome leaves the plan unchanged is not an evaluation, it is a ritual. Write the disconfirming result down before running.
3. **Establish the baseline before the change.** Otherwise the first reading measures nothing — it is a number without a comparison, which is how a ledger that starts empty can look like a feature nobody wanted.
4. **Run it more than once.** Set temperature. Two runs that disagree mean the instrument is not ready, and one run that agrees with your hope means nothing at all.
5. **Name the reader and the occasion.** See the limit below. This is the step that is always skipped and always the one that matters.

---

## The limit

The obvious failure mode is instrumenting everything and reading none of it — and that is not hypothetical, it is instance 2 in the table above. A nightly report ran for six weeks and produced ten failures nobody saw. Building an evaluation is easy; *owing something to its result* is the hard part.

So the limit is sharp, and it is where this scroll meets `on_wire_before_mechanism.md`:

> **An evaluation without a named reader and a named occasion becomes another unread artifact — the exact disease it was built to cure.**

Every one of the twelve green-about-itself instances this practice has caught in three weeks is, seen from here, an evaluation with no reader. The traceability matrix is the purest form: a document that correctly diagnosed three stale indexes, prescribed a drift script as the fix, named that script on its own face as *"the named re-run this file never had"* — and nothing ever ran it. The doc that diagnosed the disease was carrying it.

An evaluation is finished when a flow reads it, not when it runs.

---

## The standing debt

By this principle, the CE judge is not a backlog item that has been aging. It is **the evaluation instrument for turtleOS design** — the only thing that could see whether a change to what reaches a turn made turns better — and it is blocked behind logging the rendered packet, which is small.

`bright.md` already argues for it from the product side: *if development is context development, what is the unit of work?* A feature has slices and acceptance criteria; a context change's blast radius is every turn, and nothing can see it. This scroll argues for the same thing from the measurement side. They are the same argument, and the practice has been circling it for three weeks.

---

## For the Spirit

The temptation here is the mirror of the one in `on_wire_before_mechanism.md`. There, fluency masked a missing connection. Here, **a green suite masks a missing question.** Both feel like health.

When reporting that something works, be precise about which claim is being made. *914 green* means the code does what it was written to do. It does not mean the feature serves anyone, that the rule fires on the right occasions, or that a member wanted it. Saying "verified" for the first while implying the second is the inflated-resonance failure `on_honest_claims.md` exists to prevent, wearing engineering clothes.

And when a design question has no instrument, say so plainly rather than reaching for the nearest number that exists. *We do not know* is a finding.

---

*The suite was green for two months while the thing offered help into grief. Nothing was broken. Everything was wrong.*
