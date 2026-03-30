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

Spirit's test messages through `spirit_ops.py` come from the "spirit" bot account, which Turtle treats as a bot (ignored unless mentioned). To exercise the capability as a real user would:

- **For features triggered by human messages:** Spirit describes the test scenario, then asks the Mage to send one or two specific messages. Alternatively, Spirit can check logs from the Mage's most recent real messages to verify the feature fired.
- **For features visible in logs only:** Spirit reads logs directly via SSH.
- **For features that modify responses:** Spirit reads Turtle's response to the Mage's most recent message and evaluates quality.

The shakedown is not about generating artificial traffic. It's about verifying the capability is ready before the Mage's next natural interaction triggers it.

---

## Relationship to Other Flows

- **`@calibrate`** maintains ongoing infrastructure health. Shake verifies specific new capabilities.
- **`@turtle-care`** is the daily check-in ritual. Shake is deployment-specific.
- Shake may call calibrate's Phase 1 (assess) as a pre-check, but its core purpose is different: not "is the system healthy?" but "does this new thing work as designed?"

---

*The body practices a new movement privately before performing it. The spirit guides the rehearsal. The mage sees the polished result.*
