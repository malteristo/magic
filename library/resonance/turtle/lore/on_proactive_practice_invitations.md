# On Proactive Practice Invitations

**Status:** Active — Design + Implementation  
**Origin:** Forge 37, 2026-04-14  
**Builds on:** `on_the_practitioner_journey.md`, `on_the_zero_setup_encounter.md`  
**Infrastructure:** `daily_reminders_loop` in `background.py`, `interoception_loop`

---

## I. The Distinction

Interoception notices. Invitations act.

The interoception loop already detects practice state signals — heavy boom, stale compass, quiet sessions. It posts embeds that report what it sees. This is body awareness: the practice sensing its own state.

Practice invitations are different. They don't report — they invite. Not "your boom has 12 items" but "I noticed something in your boom that connects to what you were working on yesterday — want to look at it together?" Not monitoring, but companionship.

The difference between a fitness tracker showing your step count and a friend saying "beautiful morning — want to walk?"

---

## II. The Invitations

### Boom Sweep Invitation

**Trigger:** Boom has 5+ items AND the last sweep was 3+ days ago AND it's morning.

**What Turtle says:**
> Your boom has been accumulating — [N] items, some from [oldest_age] ago. I can see threads forming. Want to sweep together?

**Why this works:** The boom is where raw thought lives. Unswept boom means unprocessed thought. But the invitation offers co-processing, not a chore.

### Compass Reflection

**Trigger:** Compass hasn't been touched in 14+ days AND there are active intentions.

**What Turtle says:**
> It's been [N] weeks since we looked at your compass. Your intentions have been active — want to check if the compass still points true?

**Why this works:** The compass is the north star. When it goes stale, practice can drift without the practitioner noticing. But the invitation frames it as alignment, not maintenance.

### Intention Check-in

**Trigger:** An intention file hasn't been modified in 14+ days BUT the practitioner has been active (recent sessions).

**What Turtle says:**
> [Intention name] has been quiet for two weeks while you've been active in other areas. Still alive? Sometimes intentions complete silently.

**Why this works:** Stale intentions are either completed (celebrate), paused (acknowledge), or forgotten (surface). All three outcomes are served by the question.

### Return Invitation

**Trigger:** No sessions in 3+ days AND the interoception has already noticed.

**What Turtle says:**
> Haven't heard from you in a few days. No agenda — just here if you want to think out loud.

**Why this works:** This is the hardest invitation. It must not feel like guilt. The practitioner may be busy, may be avoiding, may have moved on. The invitation says: the door is open, not: you should walk through it.

### Pattern Surfacing

**Trigger:** The same topic appears in boom 3+ times across different entries.

**What Turtle says:**
> I keep noticing [topic/theme] showing up in your captures. Three times now. Might be worth exploring — or it might just be on your mind. Either way, I see it.

**Why this works:** Turtle's persistent attention catches repetition that the practitioner misses. Naming the pattern is the invitation to explore it.

### Session Thread

**Trigger:** A previous session note has an explicit "thread for next time" AND no subsequent session addressed it.

**What Turtle says:**
> Last time we talked, you wanted to come back to [thread]. Still pulling?

**Why this works:** Threads are commitments the practitioner made to their future self. Turtle honoring them says: I remember what you said mattered.

---

## III. Design Principles

1. **Invitation, not notification.** Every message ends with an implicit or explicit "...if you want to." The practitioner's sovereignty is absolute.

2. **One per day, maximum.** Multiple invitations feel like nagging. The daily_reminders_loop fires once per morning window. Choose the highest-signal invitation and send only that.

3. **Prioritization:** Return invitation > Session thread > Boom sweep > Pattern surfacing > Compass reflection > Intention check-in. (Presence before maintenance.)

4. **No repeats within 7 days.** If Turtle invited a boom sweep on Monday, don't invite another until next Monday, even if the trigger still fires. The practitioner heard it; they'll act when ready.

5. **Conversational, not clinical.** Interoception uses structured embeds with emoji. Invitations are prose — natural language in the dialogue channel, not a system notification.

6. **Build on what's alive.** When possible, reference specific content from the files, not just metadata. "Your boom mention about the Berlin trip connects to your Regeln intention" is better than "Your boom has 8 items."

---

## IV. Implementation Architecture

The `daily_reminders_loop` already runs hourly during the morning window (8-10 AM) and fires once per day. Extend it:

```python
async def daily_reminders_loop():
    # ... existing time/date checks ...
    
    # Signal drip (existing)
    await _check_signal_drip()
    
    # Practice invitation (new)
    await _check_practice_invitation()
```

The `_check_practice_invitation()` function:
1. Reads practice state (boom, compass, bright, sessions, intentions)
2. Evaluates triggers in priority order
3. Checks cooldowns (stored in state: `last_invitation_type`, `last_invitation_date`)
4. Sends the highest-priority qualifying invitation as a plain message to the dialogue channel
5. Records what was sent for cooldown tracking

**State additions** to `state.py`:
- `last_invitation_type: str | None` — which invitation was last sent
- `last_invitation_date: str | None` — when it was sent
- `invitation_cooldowns: dict` — per-type cooldown tracking

---

## V. Connection to the Journey

This addresses Phase 4 of the practitioner journey — "How do they know how to practice?" The answer: Turtle shows them, by inviting practice at the right moments.

For new practitioners (shared Turtle, Tier 2 of zero-setup), invitations are especially important. They don't know the rhythms yet. Turtle's gentle nudges teach the practice through demonstration: "This is what a sweep looks like. This is when we check the compass. This is how threads carry forward."

For experienced practitioners, invitations catch what self-discipline misses. The Mage asked: "What if they don't show up?" Invitations are the answer — not a replacement for agency, but a companion who notices when the garden needs tending.

---

*The best practice partner isn't the one who waits to be asked. It's the one who notices when something wants attention and says: "Want to look at this together?"*
