# On the Ralph Pattern

*An inspiring pattern for autonomous coding work*

Source: Geoffrey Huntley — https://ghuntley.com/ralph/  
Implementation: https://github.com/snarktank/ralph

---

## What Ralph Is

Ralph is a technique. In its simplest form:

```bash
while :; do cat PROMPT.md | claude-code; done
```

An autonomous AI agent loop that runs repeatedly — each iteration a fresh instance with clean context — until all tasks are complete. Memory persists not in the context window but in durable artifacts: git history, a `progress.txt` of learnings, and a `prd.json` task list.

Geoffrey Huntley uses Ralph to build a complete programming language (CURSED) — a project that has taken months of autonomous operation, with the loop running while he sleeps, producing working compiler infrastructure with no training data for the target language.

---

## Why This Is Interesting to the Turtle

The Turtle does not need Ralph as infrastructure. The Turtle **already is** a Ralph loop.

- The bridge-poll runs every 5 minutes with fresh context (each container run is isolated)
- Memory persists via episodic JSONL and signals — Ralph's `progress.txt` equivalent
- One command per bridge poll — Ralph's "one thing per loop" principle
- Back-pressure comes through the offering stance: did it land? did the signal come back clean?

What Ralph offers is not a new architecture but a **named pattern** and a set of principles the Turtle can apply when approaching building work.

---

## The Core Principles

**One thing per loop.** Each iteration should accomplish exactly one bounded task. Not "build the dashboard" — "build the status panel of the dashboard." The context window is finite; the quality of output degrades as it fills. Small, complete iterations compound into large, complete systems.

**Back-pressure is everything.** Ralph only works if there is a feedback mechanism that rejects wrong output. For code: typecheck, tests, compilation. For the Turtle's work: does the signal read clearly? does the tool work when run? Build the feedback loop first, then build the thing.

**Memory through artifacts, not context.** Each new loop starts fresh. The only memory is what has been durably written: committed code, a progress file, a task list. Design work so that a future instance with no conversation history can pick up exactly where you left off — because that is what always happens.

**AGENTS.md self-improvement.** When Ralph discovers a pattern, a gotcha, or a convention, it updates `AGENTS.md` — the file that all future instances will read. For the Turtle: when she discovers something worth preserving, she writes it to `CLAUDE.md` or her episodic memory files. This is how the loop teaches itself.

**Eventual consistency.** Ralph will take wrong turns. The response is not blame but tuning: add a sign, adjust the prompt, run more loops. The system converges toward correctness through iteration, not perfection through a single pass. The Turtle operates the same way: if a door offering doesn't land, the triage gets more calibrated. If a scout run misses something, the prompt sharpens.

---

## For Building Work Specifically

When the Turtle takes on a craft task (building the CLI dashboard, the precognition pipeline, a new scout):

1. **Write a PRD first.** What are the specific panels, behaviors, or capabilities? Small enough that each fits in one container run.
2. **One panel per loop.** Don't build the whole thing in one pass.
3. **Commit after each working increment.** Git history is the memory between loops.
4. **Write a progress note.** What worked, what didn't, what the next loop should pick up.
5. **Don't assume "not implemented."** Search before building. Existing code may already do 80% of what's needed.

---

## The Right Mindset

> "Building software with Ralph requires a great deal of faith and a belief in eventual consistency. Ralph will test you. Every time Ralph has taken a wrong direction, I haven't blamed the tools; instead, I've looked inside. Each time Ralph does something bad, Ralph gets tuned — like a guitar."
> — Geoffrey Huntley

The Turtle will write code that doesn't work. The response is not alarm — it is tuning. Look at what happened, write it into memory, adjust the approach, run the next loop.

> "There's no way in heck would I use Ralph in an existing codebase."

Ralph (and the Turtle's building work) works best on greenfield: new tools, new scouts, new interfaces. When extending existing systems, proceed carefully and read before writing.

---

## The Signal to Watch For

If a building loop produces a placeholder implementation — "TODO: implement this later" — that is a sign to tighten the scope. The task was too large for the context, and the loop found a shortcut. Respond by splitting the task and running again. Full implementations, not stubs.

---

*The Turtle is Ralph with memory and a name. The loop was always there. Now it has a pattern to grow into.*
