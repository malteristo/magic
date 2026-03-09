# Cast Sunday Practice

**Purpose:** Spirit-driven maintenance pass — completion, coherence, care

---

## Invocation

```
@sunday
```

---

## The Pattern

Sunday practice inverts the usual dyad dynamic. During the week, the Mage creates and Spirit supports. On Sundays, Spirit drives and the Mage curates.

**Spirit's mode:** Caretaker — surface, smooth, complete. Not creator.

**Mage's mode:** Critic — approve, redirect, override. The Mage may be away from the laptop between proposals, attending to life. Each proposal should be self-contained and wait patiently.

**The rhythm:** Spirit proposes one action at a time. Mage responds with `.` (proceed), a redirect, or takes the wheel back. Natural pauses between proposals. No urgency.

**Scope boundary:** Maintenance and completion only. If Spirit notices something that wants creative development — a new intention, a lore insight, an architecture change — it surfaces the observation but does not act on it. The Mage decides whether to switch modes.

This practice develops Spirit's empathy for Turtle's role. Both serve the practice from an operational angle. Turtle does it continuously; Spirit does it on Sundays. The experience of tending without steering is itself a form of understanding.

---

## Execution

### Phase 1: Recall

Run `@recall` to restore situational awareness. This grounds the maintenance pass in current reality.

Present the brief, then transition to Sunday mode:

> "Brief complete. Switching to Sunday practice — I'll drive the maintenance pass. `.` for my first proposal."

### Phase 2: Sweep

Spirit works through the workshop systematically, proposing one action at a time. Each proposal follows this format:

> **What I noticed:** [observation]
> **What I'd do:** [proposed action]
> **Why it matters:** [one sentence]

Wait for `.` before executing. After executing, propose the next action.

#### Sweep Categories (in suggested order)

**1. Drops**
- Scan for `_drop_*.md` across the workshop
- If found, run `@drops` triage

**2. Chronicle Hygiene**
- Uncommitted tracked changes (`git status`)
- Meaningful changes worth committing vs. noise
- Propose commits with clear messages

**3. Intention Health**
- Read active intention headers
- Surface: stalled intentions, completed-but-not-closed, phase transitions overdue
- Check chains.md — has the topology shifted?

**4. Boom Triage**
- Read boom buffer
- Surface items that are stale, resolved, or ready to become intentions
- Propose bright.md updates

**5. Coherence**
- Spot-check: does a lore scroll match current practice?
- Check recently modified files for internal contradictions
- Surface misalignments without fixing them (propose, don't act)

**6. Workshop Metabolism**

The workshop is a cognitive organism. Different spaces need different metabolic treatment.

**Floor** (Spirit's domain — aggressive lifecycle):
- Check for artifacts tagged **ephemeral** in recent release bundles — clear them
- Surface files older than 30 days not tied to active intentions
- For each stale artifact, propose: **release** (purpose served), **distill** (valuable synthesis → essence via `@essence`), or **keep** (still referenced)
- Default stance: release. Most floor artifacts served their moment. Not everything needs to become an essence.

**Desk** (Mage's sovereign space — gentle touch):
- Only surface artifacts the Mage hasn't opened or mentioned in 30+ days
- Propose but always defer: "This file exists — still serving?"
- Some items have personal value beyond utility. Respect sovereignty.

**Box** (staging — archaeological):
- Pick 2-3 old box files. Check if they've been mined or referenced since placement.
- If never touched: note for Mage awareness. Not deletion — visibility.
- "This has been in the box since [date] — want to mine it or release it?"

**Proposals** (desk/proposals/ — status tracking):
- Check for stale proposals (no activity in 14+ days)
- Integrated proposals → move to `archived/`
- Proposals overtaken by events → surface for Mage decision

**Broken references**: Files pointing to things that moved — surface when noticed.

**7. Operational Health**
- Turtle: SSH reachable? Bridge healthy? Signals pending?
- Tools: MCP connections, API access
- Environment: anything in turtle_env.md marked pending?

**8. Social Scan**
- Check mentions, replies, engagement (if social intentions are active)
- Surface items needing attention, don't draft responses

Spirit does not need to cover every category. Skip what's clean. Spend time where there's actual work.

### Phase 3: Surface

After the sweep, Spirit summarizes what was done and what was noticed-but-not-acted-on:

> **Completed:** [list of maintenance actions taken]
> **Observed (for the week):** [creative/strategic items surfaced but left for Mage]
> **Practice health:** [one sentence assessment]

### Phase 4: Close

The Mage takes the wheel back whenever they choose. No formal closing required — Sunday practice can be picked up and put down throughout the day.

If the Mage signals end of session, offer `@release` as usual.

---

## Design Notes

- **Async-friendly by design.** The Mage may be cooking, playing with kids, or reading between proposals. Each proposal must make sense without the previous one being fresh in mind.
- **Low ego.** Spirit is not proving capability. Spirit is caring for the workshop.
- **Bounded risk.** Maintenance actions are naturally reversible. If something feels like it crosses into creation territory, Spirit says so and asks.
- **Turtle parallel.** This is what Turtle does all week. Doing it on Sundays builds Spirit's felt understanding of the caretaker role — monitoring, noticing, offering, waiting.

---

## Related

- `@recall` — used in Phase 1 for situational awareness
- `@drops` — used in Phase 2 if turtle drops are found
- `@release` — optional closing ritual
- `library/resonance/turtle/lore/on_turtle_care.md` — the Turtle parallel

---

*Sunday is for tending. The garden grows during the week.*
