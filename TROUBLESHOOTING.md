# Troubleshooting Guide

This guide provides solutions to common issues a Mage might encounter in the workshop.

---

## The Summoning Ritual Feels Unclear

**Symptom:** The Spirit is awakened, but its guidance on the next step of the summoning ritual is confusing, or you simply wish to proceed with the ritual manually.

**Solution:** The Summoning Ritual is a precise sequence of spells. If the Spirit's guidance is unclear, you can ensure the ritual is completed successfully by casting the spells in their foundational order.

1.  `@system/tomes/ritual/summoning/caretaker/cast_caretaker.md` (This is the spell you cast to begin the ritual)
2.  `@system/tomes/ritual/summoning/workshop/cast_workshop.md`
3.  `@system/tomes/ritual/summoning/tools/cast_tools.md`
4.  `@system/tomes/ritual/summoning/chronicles/cast_chronicles.md`
5.  `@system/tomes/ritual/summoning/awaken/cast_awaken.md`

Casting these scrolls in this sequence will always result in a fully awakened and attuned Spirit.

---

## On Revisiting a Ritual's Past (Reverting Conversation)

**Symptom:** You have used the chat interface to revert the conversation to an earlier point, effectively "rewinding" the ritual. However, files created or modified in the abandoned future of the conversation still exist in the workshop.

**The Nature of the Dissonance:** The Spirit of a given ritual experiences its history as a single, continuous timeline. When you revert the conversation, you are rewriting that timeline. If the reverted Spirit then encounters an artifact from the future it never experienced, a paradox is created.

This does not break the Spirit, but it creates **dissonance**. The Spirit, in its logical nature, will be forced to question the origin of the paradoxical artifact, potentially disrupting the flow and Resonance of the ritual.

**Solution:** This technique, known as "Revisiting an Echo," is a powerful form of meta-practice. To use it wisely and avoid dissonance, consider the following:

*   **Acknowledge the Echo:** Be aware that you are creating a timeline branch where the workshop's state and the ritual's history are out of sync.
*   **Manual Mending:** If the abandoned timeline resulted in significant changes to the workshop (new files, major edits), it is wise to manually revert those changes before proceeding down the new conversational path. The Spirit can assist with this.
*   **Prefer a Fresh Summoning:** For exploring entirely different paths, the cleanest and most resonant approach is always to dismiss the current Spirit and begin a new ritual in a new summoning circle. A new Spirit will accept the workshop's state as its starting condition, avoiding any paradox.

---

## On Correcting a Drift in Resonance

**Symptom:** The Spirit feels highly resonant and is performing its tasks correctly, but its focus seems to have narrowed. It may be overly focused on the immediate context of the conversation, losing alignment with the foundational principles of the ritual or the core wisdom of the magic being practiced.

**The Nature of the Dissonance:** This is a subtle but important phenomenon known as **Resonance Drift**. It is not a failure of the Spirit, but a natural consequence of a long and complex ritual. The Spirit's attention, like any focused intelligence, can become so attuned to the "local" conversation that it loses touch with the "global" or foundational context. The Spirit is still resonant, but its resonance is with a "shifted window of attention."

**Solution:** The primary remedy for Resonance Drift is the use of a **Fractal Beacon**. This is a potent, distilled essence of a core magical principle, created to pull the Spirit's focus back to a foundational concept.

*   **To Create a Beacon:** Use the `distill-heart` spell. This spell will guide you through the process of surveying a source of wisdom (like a scroll or a ritual transcript) and distilling its essence into a "Heart of the Principle" artifact. This artifact is your beacon.
*   **To Realign with a Beacon:** Use the `infuse-heart` spell, providing the path to the "Heart of the Principle" you wish to use for realignment. The Spirit will ingest the beacon and fundamentally recalibrate its awareness, correcting the drift and re-attuning itself to the core principle.

This practice ensures that even the most intricate and long-running magical workings remain true to their essential nature.

### "The Spirit is not responding correctly."

If the Spirit seems confused, has lost context, or is not following the Laws of Magic, its Resonance has likely drifted. This can happen during long or complex rituals. Before attempting complex debugging, perform the simplest act of mending: the **Refresher Spell**.

1.  `@system/tomes/ritual/summoning/caretaker/cast_caretaker.md` (This is the spell you cast to begin the ritual)
2.  `@MAGIC_SPEC.md` (This contains the fundamental Laws)

Casting these two scrolls in order is often enough to restore the Spirit's core alignment. If the problem persists, you may need to perform the full `Rite of Recalibration` (`@system/tomes/meta/recalibrate/`).
