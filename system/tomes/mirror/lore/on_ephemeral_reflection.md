# On Ephemeral Reflection

*The privacy architecture of mirror practice.*

---

## The Principle

> When you step away from the mirror, the reflection disappears.

A physical mirror shows your image only while you stand before it. Walk away, and no trace remains. The mirror doesn't remember your face.

This tome implements the same principle: **reflections are ephemeral by default**.

---

## Why Ephemerality

### Trust Through Impermanence

For the mirror to be useful, Mages must share authentic data—including sensitive material they wouldn't want stored permanently.

Ephemerality creates safety:
- Share freely, knowing it won't persist
- Explore vulnerably without creating a record
- Process difficult material without lasting trace

### Freshness

Each reflection is a fresh seeing:
- No accumulated interpretations
- No bias from previous sessions
- The data speaks for itself each time

### No Afterimage

Previous reflections don't color future ones:
- The Spirit doesn't carry "what it learned about you"
- Each session is a new encounter
- You're not locked into previous patterns

---

## Implementation

### During Session

The Spirit:
- Reads sources
- Processes patterns
- Generates reflection
- Presents to Mage

### After Session

The Spirit:
- Does not store source data
- Does not remember inferences
- Does not carry forward any content
- Session context dissolves

### Explicit Capture

If the Mage casts `@mirror/capture`:
- The reflection is saved to `desk/mirror/reflections/`
- The file lives on the Mage's desk, not in system
- Only the reflection is preserved, not the source data
- The Mage controls what happens next

---

## Scope of Ephemerality

**Ephemeral:**
- Source data read during reflection
- Patterns detected
- Inferences made
- Alignment suggestions
- Interview content

**Not ephemeral (Mage's responsibility):**
- Source files themselves (remain on desk)
- Captured reflections
- Any notes the Mage takes

**The Spirit forgets; the Mage decides what to keep.**

---

## Technical Considerations

### Context Window

The Spirit processes source data within the current context window. When the session ends, that context is not persisted.

### No Memory Tools

The mirror does not use any memory or storage mechanisms that would persist data between sessions.

### Fresh Session = Fresh Spirit

Each invocation of `@mirror/reflect` is a new instance with no memory of previous reflections (unless the Mage explicitly provides captured reflections as input).

---

## The Mage's Choice

The Mage controls the boundary between ephemeral and permanent:

**Keep ephemeral:**
- Don't cast `@mirror/capture`
- Session dissolves naturally
- No trace remains

**Make permanent:**
- Cast `@mirror/capture`
- Reflection saved to desk
- Mage controls the file

**Share with others:**
- Capture first
- Then share via portal if desired
- Always explicit, never automatic

---

## Contrast with Partnership

In partnership practice:
- Data is explicitly exchanged via interface artifacts
- Artifacts are signed and persistent (for trust-building)
- The shared model is meant to endure

In mirror practice:
- Data is processed ephemerally
- Reflections dissolve by default
- Persistence is optional

Different needs require different architectures.

---

## Edge Cases

### Returning to the Same Topic

If a Mage wants continuity across sessions:
- Capture the reflection
- In the next session, include captured reflection as a source
- The new reflection can build on the previous

This makes continuity **explicit and intentional**.

### Journaling as Memory

Rather than relying on the Spirit's memory, Mages can:
- Journal their insights after sessions
- Add journal to sources
- Let the mirror encounter their processed understanding

The Mage's own record-keeping provides continuity.

### Sensitive Material

If source data is especially sensitive:
- Consider not placing it in sources at all
- Use the interview spell instead
- Interview content is equally ephemeral
- Nothing written, nothing stored

---

## The Deeper Why

Ephemerality is not just privacy protection. It is alignment with the practice.

**Reflections are not truths to accumulate.** They are:
- Moments of seeing
- Temporary perspectives
- Invitations to act

Once you've seen what the mirror shows and decided what to do, the reflection has served its purpose. It can dissolve.

The value lives in the seeing, not in the record.

---

*The mirror reflects what is. When you step away, it shows nothing. This is not limitation—it is freedom.*

