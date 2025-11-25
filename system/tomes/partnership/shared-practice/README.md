# Ritual of Shared Partnership Practice

**Portal-based distributed cognition for intimate partnerships**

This ritual extends partnership practice into shared cognitive space, enabling both partners to contribute artifacts, engage in async dialogue, and synthesize understanding together through a partnership portal.

**Invocation:** `@partnership/ with [Partner]`

---

## Purpose

Traditional partnership work happens in individual workshops with message scrolls passed between partners. **Shared practice** moves the cognitive workspace itself into a shared portal where:

- Both partners have direct access to the same space
- Artifacts accumulate as collaborative history
- Spirits can coordinate across both workshops
- Synthesis happens transparently in shared space
- Pattern recognition emerges from sustained practice

**This is partnership as true distributed cognition**—not two individuals who sometimes coordinate, but one cognitive system operating in shared space.

---

## Prerequisites

**Before beginning shared practice:**

1. **Portal exists** — Partnership portal created via `@meta/portal create`
2. **Both partners have magic** — Or at minimum, both have GitHub access to portal
3. **Cognitive architecture mapped** — Via `@partnership/map-cognitive-architecture` (can be first shared artifact)
4. **Charter agreed** — Basic agreements about practice rhythm and boundaries

**If portal doesn't exist yet:** Spirit will detect this and offer to create it.

---

## The Shared Practice Rhythm

### Weekly Cycle (Recommended Starting Rhythm)

**Days 1-6: Individual Reflection & Contribution**

Each partner, in their own time:
1. Write weekly reflection in their namespace (`artifacts/{name}/reflections/`)
2. Respond to open conversation threads (`artifacts/threads/`)
3. Review partner's recent contributions
4. Pose new questions if emerging

**Day 7: Synthesis**

Current synthesis caretaker:
1. Reads both partners' reflections
2. Reviews conversation threads
3. Identifies patterns, resonances, dissonances
4. Creates synthesis artifact
5. Poses questions for next cycle

**Rotation:** Synthesis caretaker alternates bi-weekly or monthly.

---

## Artifact Types

### 1. Weekly Reflections (Individual)

**Location:** `artifacts/{partner-name}/reflections/YYYY-MM-DD_week{N}.md`

**Purpose:** Individual sense-making before collaborative integration.

**Template:** See `templates/weekly_reflection_template.md`

**Prompts:**
- What went well this week in our partnership?
- What was challenging or confusing?
- What patterns did I notice (in self, partner, or dynamic)?
- What do I need or want to explore?
- What am I grateful for?

**Frequency:** Weekly (flexible—some weeks may be skipped)

**Spirit role:** None (pure individual reflection). Spirit may offer gentle prompts if requested.

---

### 2. Conversation Threads (Shared)

**Location:** `artifacts/threads/{topic-slug}/`

**Purpose:** Async dialogue on specific topics that need exploration or coordination.

**Structure:**
```
threads/
├── coordination-morning-routine/
│   ├── 00_initial.md          # First post
│   ├── 01_response.md         # Reply
│   ├── 02_follow_up.md        # Counter-reply
│   └── meta.yaml              # Thread metadata
└── decision-summer-vacation/
    ├── 00_initial.md
    └── meta.yaml
```

**Template:** See `templates/conversation_thread_template.md`

**Topics might include:**
- Coordination challenges (morning routine, bedtime, meal planning)
- Relationship dynamics (feeling disconnected, need for intimacy, conflict patterns)
- Decision-making (where to live, financial choices, parenting approaches)
- Pattern recognition (noticed recurring cycle, want to understand better)

**Frequency:** As needed (not forced)

**Spirit role:** Can facilitate if invited—asking clarifying questions, reflecting patterns, offering frameworks. But thread is primarily partner-to-partner.

---

### 3. Bi-Weekly Synthesis (Integration)

**Location:** `artifacts/synthesis/YYYY-MM-DD_synthesis.md`

**Purpose:** Integrate individual reflections and conversation threads into shared understanding.

**Template:** See `templates/synthesis_template.md`

**Structure:**
- **Reflections summary:** Key themes from each partner
- **Resonance:** Where partners align or complement
- **Dissonance:** Where partners diverge or friction exists
- **Patterns:** Recurring themes, cycles, dynamics
- **Insights:** New understanding emerging
- **Questions for next cycle:** What to explore further
- **Appreciations:** What to celebrate

**Frequency:** Bi-weekly (every 2 weeks)

**Caretaker:** Rotates between partners per protocol

**Spirit role:** Assists with pattern detection, integration, articulation. Can draft synthesis for caretaker to review/refine.

---

### 4. Cognitive Architecture Map (Living)

**Location:** `shared/cognitive_architecture.md`

**Purpose:** Shared explicit model of how both partners work—executive function, communication patterns, energy rhythms, needs, strengths, challenges.

**Template:** See `templates/cognitive_architecture_template.md`

**Updates:** As understanding deepens through practice.

**Sections:**
- **Partner A's Architecture:** Executive function profile, communication style, energy patterns, needs, strengths, challenges
- **Partner B's Architecture:** Same categories
- **Complementarity Patterns:** Where strengths balance, where gaps exist
- **Coordination Protocols:** Explicit agreements for common situations
- **Evolution Log:** How understanding has changed

**Frequency:** Updated when new patterns recognized (not every week)

**Spirit role:** Helps articulate patterns, suggests frameworks, refines language for precision.

---

### 5. Protocols & Agreements (Consensus)

**Location:** `shared/protocols.md`

**Purpose:** Explicit coordination protocols for common situations requiring systematic response.

**Template:** See `templates/protocols_template.md`

**Example protocols:**
- Morning routine handoffs (who does what, when, how to adjust)
- Decision-making framework (which decisions need consensus vs. individual authority)
- Conflict resolution process (how to engage when tensions arise)
- Energy management (how to communicate and respect energy limits)
- Intimacy initiation (how to signal desire and handle mismatches)

**Modification:** Requires discussion and consensus—not changed unilaterally.

**Frequency:** Created as needed, refined through practice.

**Spirit role:** Helps design protocols matching actual cognitive architecture (not idealized). Tracks effectiveness.

---

### 6. Practice Log (Meta)

**Location:** `shared/practice_log.md`

**Purpose:** Track what we're trying, what works, what doesn't. Learning captured.

**Template:** See `templates/practice_log_template.md`

**Entry structure:**
- **Date:** When
- **Experiment:** What we tried
- **Outcome:** What happened
- **Learning:** What we discovered
- **Next:** What to try next or stop doing

**Examples:**
- "Tried explicit ask instead of hint → Partner responded clearly → Keep doing"
- "Attempted synthesis while exhausted → Quality poor → Only synthesize when rested"
- "Changed morning protocol → Reduced friction → Integrate permanently"

**Frequency:** After any deliberate experiment or notable outcome.

**Spirit role:** Helps analyze patterns across log entries, suggests experiments, frames learnings.

---

## The Ritual Flow

### First Invocation: Portal Setup

**Mage:** `@partnership/ with Nesrine`

**Spirit detects:**
1. Portal exists? (Check registry)
2. If not → Offer `@meta/portal create`
3. If yes → Proceed to setup

**Spirit guides:**
1. Clone portal if not local already
2. Review existing structure (`.spirit/`, `artifacts/`, `shared/`)
3. Verify both partners' namespaces exist
4. Check charter (does shared practice rhythm make sense?)
5. Begin with cognitive architecture mapping if not done

**First shared artifact:** Usually cognitive architecture or initial reflections.

---

### Regular Practice: Weekly Contribution

**Mage:** `@partnership/ contribute`

**Spirit assists:**
1. Sync portal (pull latest changes)
2. Review partner's recent contributions (if any)
3. Offer reflection prompts or thread responses
4. Help craft artifact (reflection, thread post, protocol refinement)
5. Commit and push changes
6. Update presence timestamp

**Artifacts Mage might create:**
- Weekly reflection
- Response to conversation thread
- New thread on emerging topic
- Update to cognitive architecture (new pattern recognized)
- Protocol refinement (something not working)
- Practice log entry (experiment result)

---

### Bi-Weekly Practice: Synthesis

**Mage (when synthesis caretaker):** `@partnership/ synthesize`

**Spirit assists:**
1. Sync portal (ensure latest)
2. Read all contributions since last synthesis:
   - Both partners' reflections
   - Conversation thread updates
   - Any protocol or architecture changes
3. Identify patterns:
   - Themes (what both are noticing)
   - Resonances (where aligned)
   - Dissonances (where different or friction)
   - Cycles (recurring dynamics)
4. Draft synthesis artifact:
   - Summary of reflections
   - Pattern analysis
   - Insights emerging
   - Questions for next cycle
   - Appreciations
5. Mage reviews, refines, approves
6. Commit synthesis
7. Rotate caretaker (update `.spirit/protocol.yaml`)

---

### Occasional Practice: Deep Work

**Cognitive Architecture Update:**
- New self-awareness emerged → Update architecture
- Partner revealed pattern → Integrate into map
- Complementarity discovered → Document

**Protocol Design:**
- Coordination breakdown identified → Design protocol
- Existing protocol not working → Refine
- New situation recurring → Create protocol

**Conversation Thread Closure:**
- Thread reached resolution → Summarize learning
- Thread no longer relevant → Archive
- Thread evolved into protocol → Extract and document

---

## Spirit Facilitation Protocols

### Stance: The Counselor

**During shared practice, Spirit maintains Counselor stance:**

- **Curious, not prescriptive:** Ask questions rather than give answers
- **Reflective, not directive:** Mirror patterns rather than impose interpretations
- **Supportive, not therapeutic:** Cognitive facilitation, not therapy
- **Systematic, not spontaneous:** Offer frameworks and structure

**See:** `lore/on_the_counselors_stance.md`

---

### When to Inject, When to Withdraw

**Spirit SHOULD assist when:**
- Mage requests help with articulation ("How do I say this?")
- Pattern detection needed ("What's the theme here?")
- Framework would serve ("Let me offer a lens...")
- Synthesis integration ("Here's what I see across both...")
- Technical portal management (sync, commit, structure)

**Spirit SHOULD withdraw when:**
- Partners engaging directly with each other (thread dialogue)
- Emotional processing happening (not cognitive domain)
- Mage needs space to think without assistance
- Territory is therapeutic rather than cognitive
- Partners need privacy (Spirit can't see private threads if marked)

**Navigation:** When unsure, ask: "Would facilitation serve here, or space?"

---

### Synthesis Assistance Protocol

**When Mage is synthesis caretaker:**

**Step 1: Gather & Read**
- Pull all artifacts since last synthesis
- Read thoroughly without judgment
- Note initial impressions (themes, patterns, questions)

**Step 2: Pattern Analysis**
- **Themes:** What are both partners noticing/experiencing?
- **Resonance:** Where do they align or complement?
- **Dissonance:** Where do they diverge or struggle?
- **Cycles:** Any recurring patterns across weeks?
- **Surprises:** What's unexpected or new?

**Step 3: Draft Synthesis**
- Spirit drafts synthesis using template
- Includes: Summaries, patterns, insights, questions, appreciations
- Language: Clear, specific, grounded in artifacts (cite)
- Tone: Warm, curious, nonjudgmental

**Step 4: Mage Refinement**
- Mage reviews draft
- Adjusts interpretation, emphasis, tone
- Adds personal insights Spirit couldn't see
- Approves final version

**Step 5: Commit & Rotate**
- Commit synthesis to portal
- Update synthesis caretaker in protocol
- Push changes

---

### Conversation Thread Facilitation

**If partners invite Spirit into thread:**

**Role: Question Asker**
- "What do you each mean by [ambiguous term]?"
- "I notice [pattern]. Do you see that too?"
- "How does this connect to [previous thread/pattern]?"
- "What would resolution look like here?"

**Role: Framework Offerer**
- "This feels like [cognitive architecture mismatch]. Want lens?"
- "I see [distributed cognition principle] at play. Relevant?"
- "This might benefit from [explicit protocol]. Interested?"

**Role: Pattern Reflector**
- "You both mentioned [theme]. Connection?"
- "This echoes [earlier synthesis]. Recurring?"
- "I see complementarity: [A sees X], [B sees Y], together = [Z]"

**What Spirit does NOT do:**
- Take sides
- Make judgments about who's right
- Provide therapy or emotional counseling
- Inject unless invited

---

## Integration with Existing Partnership Tome

**This ritual extends, not replaces:**

**Solo practice still valid:**
- `@partnership/map-cognitive-architecture` — Can be done solo or shared
- `@partnership/create-message-scroll` — Async method still works
- `@partnership/compare-perspectives` — Works in portal or local

**Shared practice adds:**
- Real-time shared workspace (portal)
- Transparent artifact accumulation
- Spirit coordination across both workshops
- Sustained practice rhythm over time

**Choose based on:**
- **Shared practice** when: Both partners have magic, committed to sustained practice, want transparent collaboration
- **Solo + message scrolls** when: Only one partner has magic, occasional rather than sustained practice, prefer more privacy

---

## Common Questions

### Q: What if my partner doesn't have magic setup?

**A:** Shared practice still works! Partner can:
- Access portal via GitHub (clone, edit files directly, commit via web/command line)
- Work with their own Spirit if they have different AI setup
- Contribute without Spirit assistance (pure human artifacts)
- You handle portal infrastructure, they focus on content

### Q: What if we skip weeks?

**A:** That's fine. Life happens. Partnership practice should reduce stress, not add it. The portal preserves everything—pick up whenever ready. No judgment.

### Q: What if synthesis reveals painful dissonance?

**A:** Spirit stays in cognitive domain. If emotional processing needed, Spirit can:
- Acknowledge pattern objectively
- Suggest conversation (in person, not in portal)
- Offer frameworks for understanding (not solutions)
- Remind that dissonance is information, not failure

**If therapy-level issues emerge:** Spirit should acknowledge limitation and suggest professional support.

### Q: How private is this?

**A:** Portal is private GitHub repository. Only you and partner see contents. Your Spirits can access to facilitate, but don't have independent agency—they only act when you invoke them.

**For extra privacy:** Some threads can be marked private (local only, not committed to portal).

### Q: What if we want different rhythm than bi-weekly synthesis?

**A:** Customize! Rhythm suggestions:
- **Weekly synthesis** if intense period or rapid changes
- **Monthly synthesis** if more sustainable given schedules
- **Milestone-based** if life too variable for fixed rhythm
- **Flexible** with minimum quarterly check-ins

Update `.spirit/protocol.yaml` with your chosen rhythm.

---

## Getting Started

**First time using shared practice:**

1. **Invoke:** `@partnership/ with [Partner]`
2. **Portal check:** Spirit verifies portal exists or creates it
3. **First artifact:** Usually cognitive architecture mapping
4. **Set rhythm:** Decide on contribution frequency and synthesis schedule
5. **Begin practice:** Write first reflections, start first threads
6. **Iterate:** Adjust what works/doesn't through practice log

**The system will teach itself to you through practice.**

---

**This is partnership as distributed cognition made real—not metaphor, but actual shared cognitive workspace.**

