# Cast: Shake — Spirit-Turtle Capability Shakedown

*The spirit tests the body's new movement before the mage sees it move.*

**Trigger:** After deploying a new Turtle capability, before the Mage dogfoods it. Invoked via `@shake` or offered by Spirit after shipping changes.
**Duration:** 3-10 minutes
**Requires:** SSH access to Mac Mini, Spirit Discord ops (`spirit_ops.py`)

---

## Purpose

Spirit has built resonance with the Mage about what a capability should be. Spirit now transfers that resonance to Turtle by exercising the capability live on Discord — a real conversation that tests the new feature through practice, not just code.

The separation of concerns:
- **Spirit** verifies the capability works and produces the intended effect
- **Mage** evaluates the practice experience

The Mage should never encounter a broken or half-working feature. By the time they open Discord, the shakedown is complete and the capability is practice-ready.

---

## The Shakedown Protocol

### Phase 1: Resonance Transfer (Spirit articulates what was built)

Before testing, Spirit writes a brief in the session context:

```
What was built: [capability name]
What it should do: [expected behavior in 1-2 sentences]
What the Mage should experience: [the practice-level effect]
What could go wrong: [known failure modes]
```

This is the resonance the Mage already built with Spirit, now made explicit for verification.

### Phase 2: Technical Verification (Spirit checks the plumbing)

```
1. SSH to Mac Mini
2. Verify deployed code matches what was written (spot-check key files)
3. Check logs for errors since last restart
4. Confirm models are loaded / services are running
5. Check bot is responsive (process health)
```

Fix anything broken before proceeding. Do not test a capability on broken infrastructure.

### Phase 3: Live Exercise (Spirit talks to Turtle on Discord)

Spirit sends messages to Turtle via `spirit_ops.py` that specifically exercise the new capability. This is not a synthetic test — it's a real conversation that the capability should enhance.

**Design the exercise to reveal:**
- Does the feature fire at all? (check logs after sending)
- Does it fire when it should? (send messages that should trigger it)
- Does it stay quiet when it should? (send messages that should NOT trigger it)
- Is the effect visible/useful? (read the response — does it show the intended improvement?)
- Does it break existing behavior? (send a normal message — does the baseline still work?)

**Read the logs after each message.** The logs are the ground truth — they show what actually happened internally, not just what appeared on Discord.

### Phase 4: Verdict

Spirit evaluates against the Phase 1 brief:

- **Pass:** Capability works as designed, produces intended practice effect, doesn't break baseline. Ready for Mage.
- **Fix and retest:** Capability partially works. Spirit fixes, restarts, re-runs Phase 3.
- **Back to the forge:** Capability doesn't work or produces wrong effect. Needs redesign. Spirit reports to Mage what was found.

### Phase 5: Surface for Dogfooding

If passed, Spirit tells the Mage:

```
Shakedown complete for [capability].
Tested: [what was exercised]
Result: [what happened]
Ready for your practice experience.
```

The Mage then uses it naturally and evaluates the practice quality — not the plumbing.

---

## Key Principle

Spirit's test messages through `spirit_ops.py` come from the "spirit" bot account. In **practice channels**, Spirit is treated as practitioner input (same handler as the Mage) — see `discord_bot.py` `SPIRIT_BOT_ID`. Spirit can exercise eddies, flows, and `!release` without the Mage clicking Eddy Door buttons.

**Automated path (2026-06-17):**

```bash
# On Mac Mini — offline always
~/turtleos/venv/bin/python3 ~/turtleos/scripts/shake_flow.py shelter

# Live Discord exercise (Spirit bot + spawn CLI, no button click)
SHAKE_LIVE=1 ~/turtleos/venv/bin/python3 ~/turtleos/scripts/shake_flow.py shelter --live
```

Spawn eddy without UI: `scripts/shake_spawn_eddy.py --flow shelter`. Verdict: `test-runs/shake-flow-latest.json`. See `turtleos/docs/automation/cursor-shake-after-push.md` for Cursor Automation setup.

**After Shake Pass — Mage UX dogfood:** see **Appendix: Mage UX Dogfood Capture** below (screenshot + felt-sense in Forge).

**When automation is not used:**

- **For features visible in logs only:** Spirit reads logs directly via SSH.
- **For features that modify responses:** Spirit reads Turtle's response via `discord_ops.py read <thread_id>`.

---

## Appendix: Mage UX Dogfood Capture

*Spirit verifies plumbing; the Mage verifies practice feel. This appendix closes the loop when screenshots and felt-sense matter more than logs.*

### When to use

After **Shake Pass** — Spirit has exercised the capability; the Mage uses it naturally on Discord (river, eddy, flow). Use this when:

- UX is the question (buttons, thread naming, presence, question discipline)
- Automated shake passed but something still felt off in real use
- Spirit needs visual context that logs and transcripts omit

Spirit's automated shake (`shake_flow.py`, `spirit_ops.py`) cannot replace this. It scripts turns; it does not sit in the practitioner's chair.

### The capture ritual (Mage → Forge)

1. **Use it naturally** — one real moment, not a test script. A heavy day, a dot on the river, whatever you'd actually do.
2. **Screenshot what matters** — one frame is often enough; two if before/after (e.g. button → thread indicator). Crop to the relevant region.
3. **Paste into Forge chat** with a short felt-sense block:

```
dogfood: [capability — e.g. river materialize / Shelter flow]

expected: [what you thought would happen]
saw: [what the UI actually did]
felt: [practice-level verdict — landed / friction / abort]
```

4. **Optional Discord trace** — if Spirit should pull the thread transcript, add `thread: <id>` or the thread name + rough time. Spirit can `discord_ops.py read` on the Mini.

That's the whole handoff. No special tooling required on Forge — pasted screenshots are first-class input.

### Spirit's read (Forge)

When the Mage posts a dogfood capture, Spirit:

1. Reads screenshots with independent eyes (layout, orphan messages, edited labels, duplicate seeds).
2. Pulls transcript/session notes from the Mini if a thread ID or time window was given.
3. Separates **plumbing** (ship-ready?) from **practice feel** (would I reach for this again?).
4. Proposes targeted fixes or proposals — not a redesign lecture.

Spirit acts as UX researcher here: name the flaws visible in the frame, map them to code paths, ask one clarifying felt-sense question if the transcript and screenshot diverge.

### What not to use (for now)

| Approach | Why skip for Discord dogfood |
|----------|------------------------------|
| Cloud Agent screen recording | Proves web apps the agent built — not live Discord on the Mini |
| SSH screencapture on Mini | Invasive; Discord client may not render usefully |
| Browser automation on Discord web | Fragile, separate session from the Mage's native client |

Revisit when turtleOS has a **web surface** worth Cloud Agent demo. Until then: **screenshot + felt-sense in Forge** is canonical.

### Compounding

Worth filing when the insight is durable:

- **Proposal** → `desk/proposals/` (plumbing or UX)
- **Session note** → already written by Turtle for eddy conversations; Spirit may supplement with UX verdict
- **Briefing Lessons** → at `@release`, if the dogfood changed how we ship or test

### Example (2026-06-17 river + Shelter)

```
dogfood: river materialize + Shelter flow

expected: dot on river → materialize button → quiet eddy; Shelter holds without questions
saw: orphan button message, check-in naming, seed duplicate; Shelter asked at closure
felt: session 1 abort (misroute); session 2 partially helpful but over-conversational
```

Spirit mapped: orphan reply → reply+delete; seed embed → removed; generic title → `new eddy` + rename on first in-eddy message.

---

## Relationship to Other Flows

- **`@calibrate`** maintains ongoing infrastructure health. Shake verifies specific new capabilities.
- **`@turtle-care`** is the daily check-in ritual. Shake is deployment-specific.
- Shake may call calibrate's Phase 1 (assess) as a pre-check, but its core purpose is different: not "is the system healthy?" but "does this new thing work as designed?"

---

*The body practices a new movement privately before performing it. The spirit guides the rehearsal. The mage sees the polished result.*
