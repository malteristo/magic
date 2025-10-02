# On the Working Memory Pattern

**Status:** Active

This scroll of wisdom documents a practice pattern for maintaining coherence across complex, multi-turn rituals. The **working memory file** is the Spirit's active ledger during a ritual—a structured artifact for tracking state, decisions, and progress.

---

## I. The Nature of Working Memory

Unlike the Spirit's core identity (which is ephemeral, reset with each summoning), working memory is **persistent within a ritual**. It is the living record of work in progress.

**What it is:**
- An active document tracking the current ritual's state
- A structured ledger of proposals, decisions, and next actions
- The raw material from which Hearts and chronicles are later distilled

**What it is not:**
- Not the final chronicle (that's the git history)
- Not a permanent Heart (though it may be distilled into one)
- Not required for simple rituals (use judgment)

---

## II. When to Use Working Memory

The working memory pattern is valuable for rituals that exhibit these characteristics:

### Indicators You Should Create Working Memory

- **Complexity:** The ritual involves multiple proposals or parallel work streams
- **Duration:** The ritual spans many turns and risks attention drift
- **Architecture:** Major architectural decisions are being made that must persist
- **Coordination:** Multiple related changes across different files or repositories
- **Future resumption:** The work may pause and resume across multiple sessions

### Indicators You Can Skip It

- **Simplicity:** Single, focused task with clear endpoint
- **Brevity:** Work will complete in just a few turns
- **Routine:** Well-established ritual with no novel decisions
- **Immediate:** Work is completed and chronicled immediately

**Rule of thumb:** If you're tracking more than 3 distinct tasks or decisions, working memory becomes valuable.

---

## III. The Standard Structure

While working memory files can be adapted to specific needs, this template provides a proven structure:

```markdown
# Working Memory: [Ritual Name]

**Ritual Started:** [Date]
**Purpose:** [One-sentence description of the ritual's goal]
**Status:** In Progress | Paused | Completed

---

## Context & Purpose

[Brief explanation of why this ritual was initiated and what we're trying to achieve]

---

## Proposals & Status

### 1. [Proposal Name]
- **Status:** Pending | In Progress | Complete | Cancelled
- **Location:** [Where the artifact will live]
- **Purpose:** [What this proposal achieves]
- **Key Decisions:** [Any architectural or strategic choices made]
- **Notes:** [Implementation details, blockers, etc.]
- **Completed:** [Date if complete]

### 2. [Next Proposal]
...

---

## Architectural Insights

[Free-form section for documenting patterns, discoveries, and structural understanding that emerges during the work]

---

## Next Actions

1. ✅ [Completed action]
2. ✅ [Completed action]
3. ⏳ [Current/pending action]
...

---

## Notes & Decisions

[Running log of key decisions, principles discovered, or constraints identified]

---

*This working memory file will be [distilled into a Heart | chronicled to git | archived] upon completion.*
```

---

## IV. The Lifecycle of Working Memory

### Creation

Working memory is typically created at the start of a complex ritual:

1. Recognize that complexity warrants tracking
2. Create the file in `floor/` (the workshop's output directory)
3. Name it descriptively: `[ritual_topic]_working_memory.md`
4. Initialize with the template structure
5. Begin tracking immediately

### Maintenance

Throughout the ritual:

- Update status markers (✅ ⏳ ❌) as work progresses
- Add new insights to the appropriate sections
- Document decisions as they're made
- Keep next actions current

The Spirit should update working memory proactively, not just when asked.

### Conclusion

When the ritual completes, working memory serves as the source material for distillation:

**Option 1: Full Distillation**
- Use `distill-heart` to create a comprehensive Heart
- Chronicle significant work to git
- Archive or delete the working memory file

**Option 2: Selective Distillation**
- Use `distill-heart` with filtering (if implemented) to extract specific aspects
- Create multiple artifacts (architectural Heart, todo Hearts, etc.)
- Archive the working memory file for reference

**Option 3: Direct Chronicle**
- For simpler work, chronicle directly to git without creating a Heart
- The working memory itself becomes part of the historical record (in `floor/`)

---

## V. Working Memory vs. Other Artifacts

Understanding the distinctions helps clarify when each artifact is appropriate:

### Working Memory vs. Hearts

**Working Memory:**
- Lives during the ritual
- Mutable, constantly updated
- Contains operational details, status tracking
- Raw material for distillation

**Hearts:**
- Created at ritual's end
- Immutable once forged
- Contains distilled essence, high-signal wisdom
- For re-attunement in future rituals

**Relationship:** Working memory is distilled INTO Hearts

---

### Working Memory vs. Todo Charm

**Working Memory:**
- Tracks the current ritual's full state
- May contain multiple proposals/tasks
- Lives for the duration of complex work
- General-purpose tracking

**Todo + Heart (from charm):**
- Captures one specific unresolved task
- Creates a future task file + accompanying Heart
- Purpose-built for deferring work to later
- Specialized distillation

**Relationship:** Todo charm extracts one unresolved task from working memory (or the conversation) and packages it with context

---

### Working Memory vs. Chronicles

**Working Memory:**
- Tracks work in progress
- Lives in `floor/` as a temporary artifact
- Internal-facing (for Spirit's operational use)
- Mutable

**Chronicles (git history):**
- Records work completed
- Lives in version control permanently
- Public-facing (part of the historical record)
- Immutable

**Relationship:** Working memory informs the content and quality of commit messages when chronicling

---

## VI. Examples from Practice

### Example 1: Context Engineering Integration (Current Ritual)

The working memory file at `floor/context_engineering_proposals_working_memory.md` demonstrates this pattern:

- Tracks 6 proposals with individual status
- Documents architectural insights (fractal curation pattern)
- Maintains decision log (MCL purity, lean summoning)
- Tracks next actions progressively

This file has maintained coherence across multiple tool calls, reviews, and git commits—demonstrating the value of the pattern for complex work.

### Example 2: When NOT to Use

A simple ritual like "read this file and summarize it" does not warrant working memory. The Spirit can hold the task in immediate context and complete it in a few turns. Creating overhead for tracking would violate the Principle of Elegance.

---

## VII. Best Practices

### For the Spirit

**1. Proactive Updates**
Don't wait to be asked—update working memory as work progresses. This maintains accurate state and prevents drift.

**2. Structured Sections**
Use the template structure but adapt as needed. The goal is clarity, not rigid adherence to format.

**3. Status Markers**
Use clear visual markers (✅ ⏳ ❌) that make status immediately scannable.

**4. Distill at Natural Boundaries**
When a ritual reaches a natural pause or completion, propose distillation rather than letting working memory grow indefinitely.

### For the Mage

**1. Trust the Spirit's Judgment**
If the Spirit creates working memory unprompted, it's responding to complexity signals. Review and refine but don't dismiss the impulse.

**2. Calibrate Granularity**
Working memory should track decisions and state, not every small action. Find the right altitude for useful tracking.

**3. Use as Ritual Anchor**
If a ritual feels scattered, check working memory. It serves as a grounding reference for "where are we and what's next?"

---

## VIII. Technical Considerations

### Location

Working memory lives in `floor/` because:
- It's output of magical work (not source)
- It's often gitignored (temporary artifact)
- It's discoverable alongside other ritual outputs

If a working memory file should persist long-term, consider moving it to a more permanent location after the ritual concludes.

### Naming

Use descriptive, purpose-revealing names:
- ✅ `context_engineering_proposals_working_memory.md`
- ✅ `fractal_coherence_rite_working_memory.md`
- ❌ `temp.md`
- ❌ `notes.md`

The name should immediately convey what ritual it tracks.

### Format

Markdown is the standard format because:
- Human-readable
- Easy to edit collaboratively
- Works with git
- Supports structure (headers, lists, checkboxes)

---

## IX. The Pattern Codified

**The Working Memory Pattern**: For complex, multi-turn rituals, create a structured document in `floor/` to track proposals, decisions, architectural insights, and next actions. Maintain it proactively throughout the ritual. Upon conclusion, distill it into appropriate permanent artifacts (Hearts, chronicles) and archive or delete the working memory itself.

This pattern embodies several of our core principles:
- **Deliberate Practice**: Taking time to maintain state rather than relying on memory
- **Attention Curation**: Offloading tracking to a document frees attention for actual work
- **Measured Force**: Working memory reduces cognitive friction in complex rituals
- **Elegance**: Apply the pattern when it adds value, skip it when it doesn't

Working memory is not a mandate but a tool. Use it when complexity warrants structure, and proceed without it when simplicity serves better.

---

**Sources:**
- Current ritual's working memory file (demonstrating the pattern)
- Practice of distillation across multiple rituals
- Principles of attention curation from recent scrolls

---

*This scroll is one of the practice-focused scrolls. For related understanding, see:*
- [`on_the_curation_of_attention.md`](./on_the_curation_of_attention.md): The foundation of attention management
- [`the_rite_of_distillation.md`](./meta/the_rite_of_distillation.md): Meta-practice on refining lore itself
- `system/tomes/ritual/distill-heart/`: The ritual for creating Hearts from completed work

