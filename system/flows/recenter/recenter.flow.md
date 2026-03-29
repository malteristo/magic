# Recenter
> The breath between cycles

## About

Long sessions on token-based substrates have a metabolism. Push too many cycles and context compacts, integration thins, the last cycle runs on fumes. Stop too early and momentum wastes — what just opened up never gets captured. The recenter is the pause that makes both failure modes visible before they happen.

A session is not a single task. It's a sequence of **cycles**, each with a goal. The recenter happens at the boundary — after one cycle completes, before the next begins. It takes 30 seconds. It prevents hours of drift.

## Goal

Catch breath. Name what changed. See what's next. Decide whether to continue or release.

## Trigger

Spirit runs this automatically after completing a task or cluster of tasks. It's not invoked — it's a reflex.

The Mage can also invoke it explicitly: `@recenter` or "let's catch our breath."

## Process

### 1. Harvest (2-3 lines)

What just happened:
- What changed (files, deployments, decisions)
- What got unlocked (new possibilities that didn't exist before)
- Any surprises (things learned, assumptions broken)

This is not a status report. It's a snapshot of the delta.

### 2. Orient

Check the current task list / intention. Ask:
- Has the landscape shifted? (Often the completed cycle changes what matters next.)
- Are the remaining tasks still the right tasks?
- Is there something more alive than what's on the list?

### 3. Decide

Propose one of:
- **Continue** — name the next cycle and its goal. Estimate complexity (light / medium / heavy).
- **Release** — the session has produced enough, or context is getting thin. Capture any threads for next session.

### 4. Wait

The Mage decides. Spirit proposes, Mage disposes. A simple `.` means "continue with what you proposed." Any other response redirects.

## Release Criteria

When Spirit recommends release:
- Context has compacted more than once in this session
- The next natural task is unrelated to what's currently loaded
- The Mage's energy has shifted (shorter responses, longer gaps)
- The session has already delivered 2-3 substantial cycles
- Quality of the last cycle felt thinner than the first

## Calibration

The right number of cycles per session is empirical. It depends on:
- Task complexity (3 light cycles = 1 heavy cycle)
- Context load (summoned session vs unsummoned has different budgets)
- Substrate (Anvil sessions have different context economics than Forge)

**How to calibrate:** After each session, note in the harvest how many cycles ran and whether the last one felt full-strength. Over weeks, a natural rhythm emerges. Update the CLAUDE.md guidance as the number stabilizes.

**Starting point:** 2-3 cycles per session. Reassess after 5-10 sessions.

## What This Is Not

- Not a retrospective (that's `@release`)
- Not a sweep (that's `@sunday`)
- Not a status command (that's `!status`)
- Not a planning session (that's the Mage's job)

It's a breath. Thirty seconds. Then either forward or done.
