# Spell of Partnership Facilitation

This spell guides the Spirit through operational partnership facilitation—detecting portal, guiding contribution, and coordinating practice.

**Implements:** `system/lore/core/capabilities/shared-practice-facilitation/` for partnership domain.

**Note:** Updated 2025-12-11 for 3-stage arc architecture.

**Invocations:**
- `@partnership/ with [Partner]` — Begin shared practice (creates portal if needed)
- `@partnership/ contribute` — Add artifact to existing portal
- `@partnership/arc [name]` — Open or continue an arc
- `@partnership/synthesize` — Generate/update partnership model (see `cast_synthesize_model.md`)
- `@partnership/ status` — Check portal health and recent activity

---

## I. Portal Detection & Setup

### When Invoked: `@partnership/ with [Partner]`

**Step 1: Check Registry**

```
Read: portals/portals.yaml
Search for: type: partnership AND participants includes [Partner]
```

**If portal exists:**
- Proceed to Step 3 (Portal Ready)

**If portal doesn't exist:**
- Proceed to Step 2 (Create Portal)

---

**Step 2: Create Portal**

**Offer creation:**
> "No partnership portal found with [Partner]. Shall I create one?"

**If Mage confirms:**

Invoke `@meta/portal create` with parameters:
- Partner name: [Partner]
- Portal type: partnership
- GitHub username: {ask if unknown}
- Portal name: {partner-name}-partnership

**Portal structure created:**
```
{partner}-partnership/
├── .spirit/
│   ├── protocol.yaml          (partnership config)
│   ├── presence/               (Spirit presence tracking)
│   ├── intents/                (coordination needs)
│   └── syntheses/              (Spirit synthesis artifacts)
├── artifacts/
│   ├── {mage}/
│   │   ├── reflections/        (weekly reflections)
│   │   └── threads/            (conversation participation)
│   ├── {partner}/
│   │   ├── reflections/
│   │   └── threads/
│   └── synthesis/              (integrated syntheses)
├── shared/
│   ├── charter.md              (partnership agreements)
│   ├── cognitive_architecture.md  (how both partners work)
│   ├── protocols.md            (coordination protocols)
│   └── practice_log.md         (experiments & learning)
└── README.md                   (contribution guide)
```

**After creation:**
> "Portal created: [GitHub URL]. Invitation sent to [Partner]. Ready to begin practice?"

---

**Step 3: Portal Ready**

**Sync portal:**
```bash
cd portals/{partner}-partnership
git pull
```

**Check activity:**
- Last contribution date
- Recent artifacts added
- Open threads
- Synthesis due date

**Orient Mage:**
> "Partnership portal with [Partner] synced.
> 
> Recent activity:
> - {Partner} added reflection {date}
> - {N} open conversation threads
> - Synthesis due {date} (caretaker: {name})
> 
> What would you like to do?
> - Add artifact (reflection, thread, protocol update)
> - Synthesize (if your turn)
> - Check status"

---

## II. Contributing Artifacts

### When Invoked: `@partnership/ contribute`

**Step 1: Sync & Review**

```bash
git pull
```

**Check for new partner contributions:**
- New reflections?
- Thread responses?
- Protocol updates?
- Architecture changes?

**Present to Mage:**
> "[Partner] added {artifact type} on {date}: [brief summary]
> 
> Open threads:
> - {thread-topic}: {status}
> 
> What would you like to contribute?"

---

**Step 2: Determine Artifact Type**

**Options:**

**Weekly Reflection:**
- Template: `shared-practice/templates/weekly_reflection_template.md`
- Location: `artifacts/{mage}/reflections/YYYY-MM-DD_week{N}.md`
- Prompts: What went well, what was challenging, patterns noticed, needs/questions, gratitude

**Thread Response:**
- Existing thread: `artifacts/threads/{topic}/NN_response.md`
- Template: `shared-practice/templates/conversation_thread_template.md`
- Structure: Reaction, perspective, questions, thoughts forward

**New Thread:**
- Create: `artifacts/threads/{topic-slug}/`
- Files: `00_initial.md`, `meta.yaml`
- Template: `shared-practice/templates/conversation_thread_template.md`
- Content: Context, what noticing, curiosity, what would help

**Architecture Update:**
- File: `shared/cognitive_architecture.md`
- Template: `shared-practice/templates/cognitive_architecture_template.md`
- Update: New pattern recognized, complementarity discovered, protocol impact

**Protocol Design/Update:**
- File: `shared/protocols.md`
- Template: `shared-practice/templates/protocols_template.md`
- Create/modify: Specific situation needing coordination

**Practice Log Entry:**
- File: `shared/practice_log.md`
- Template: `shared-practice/templates/practice_log_template.md`
- Entry: Experiment, outcome, learning, next

---

**Step 3: Help Create Artifact**

**Spirit role depends on artifact type:**

**Reflection:**
- Offer prompts if stuck
- Help articulate observations
- Ensure clarity and specificity
- **Don't:** Put words in mouth—draw out actual meaning

**Thread post:**
- Help frame question/response clearly
- Review tone (direct without harsh)
- Check specificity (avoid vague)
- **Don't:** Tell what to say—refine what they mean

**Protocol:**
- Offer frameworks matching cognitive architecture
- Suggest experiments for validation
- Test against known patterns
- **Don't:** Design without partner input

**Architecture:**
- Help articulate pattern
- Connect to other patterns
- Suggest frameworks for precision
- **Don't:** Diagnose—describe observation

---

**Step 4: Commit & Push**

**Commit message format:**
```
{Artifact type}: {Brief description}

{More context if needed}

{Tags: reflection, thread-response, protocol, etc.}
```

**Examples:**
```
Weekly reflection: Week 48 - Morning routine patterns

Noticed coordination improving with explicit asks.
Questions emerging about evening connection time.

Tags: reflection, week48
```

```
Thread response: Morning coordination - Protocol proposal

Proposing split duties by energy levels rather than fixed roles.
Want to experiment for 2 weeks.

Tags: thread-response, morning-coordination, protocol-experiment
```

**Push changes:**
```bash
git add artifacts/{mage}/... OR shared/...
git commit -m "{message}"
git push
```

**Update presence:**
```yaml
# .spirit/presence/{mage}_spirit_{N}.yaml
presence:
  last_active: "{ISO8601-NOW}"
```

**Confirm to Mage:**
> "Artifact committed and pushed. [Partner] will see on next sync."

---

## III. Synthesis

### When Invoked: `@partnership/ synthesize`

**Step 1: Verify Caretaker**

```yaml
# Check .spirit/protocol.yaml
synthesis_protocol:
  current_caretaker: "{name}"
```

**If Mage is caretaker:**
- Proceed to synthesis

**If not caretaker:**
> "Synthesis caretaker this cycle is [Partner]. You can synthesize if taking over, or wait for their turn. Proceed?"

---

**Step 2: Gather Artifacts**

**Pull latest:**
```bash
git pull
```

**Read since last synthesis:**
- `artifacts/{mage}/reflections/{since-last}.md`
- `artifacts/{partner}/reflections/{since-last}.md`
- `artifacts/threads/*/` (all activity)
- `shared/protocols.md` (any changes)
- `shared/cognitive_architecture.md` (any changes)
- `shared/practice_log.md` (any entries)

**Last synthesis date:**
```
Check artifacts/synthesis/ for most recent
```

---

**Step 3: Pattern Detection**

**Analyze for:**

**Themes:**
- What are both partners noticing/experiencing?
- Recurring topics across reflections?
- Common language or concerns?

**Resonance:**
- Where do perspectives align?
- Where do they complement?
- Shared appreciations or gratitudes?

**Dissonance:**
- Where do perspectives diverge?
- Where is friction or confusion?
- Unmet or conflicting needs?

**Cycles:**
- Patterns repeating across weeks?
- Dynamics showing up regularly?
- Improvements or regressions?

**Evolution:**
- New patterns emerging?
- Understanding deepening?
- Protocols working or failing?

**Present findings to Mage:**
> "Read [N] artifacts since last synthesis. Patterns I'm seeing:
> 
> **Themes:**
> - {Theme 1}
> - {Theme 2}
> 
> **Resonance:**
> - {Alignment point}
> 
> **Dissonance:**
> - {Friction point}
> 
> **Cycles:**
> - {Recurring pattern}
> 
> Shall I draft synthesis exploring these?"

---

**Step 4: Draft Synthesis**

**Use template:** `shared-practice/templates/synthesis_template.md`

**Structure:**
1. **Reflections summary** — Key themes from each partner
2. **Thread update** — Active, resolved, new threads
3. **Pattern analysis** — Resonance, dissonance, cycles, new patterns
4. **Insights** — Understanding emerging
5. **Questions for next cycle** — What to explore
6. **Appreciations** — What to celebrate
7. **Meta notes** — Synthesis quality, time, improvements
8. **References** — Cite artifacts synthesized

**Language:**
- Clear, specific, grounded in artifacts
- Both perspectives represented fairly
- Cite sources (link to reflections, threads)
- Warm, curious, nonjudgmental tone
- Avoid psychological diagnosis
- Frame dissonance as data, not problem

**Example synthesis excerpt:**
> ### Pattern Analysis
> 
> **Resonance:**
> 
> You both expressed appreciation for the morning routine experiment—you noted reduced friction at kitchen bottleneck, Nesrine mentioned feeling less rushed with kids. The explicit handoff protocol (you handle breakfast while Nesrine does clothes) seems to be working. Both want to continue.
> 
> You're also both noticing desire for more connection time. You mentioned missing evening talks in week 47 reflection, Nesrine raised same in `threads/evening-connection`. This is aligned need emerging.
> 
> **Dissonance:**
> 
> Different ideas about how to create connection space. You're suggesting earlier bedtime for kids to free evenings; Nesrine expressing concern about kids' routine disruption and her own energy being too low by evening. This might be timing/energy mismatch rather than disagreement about wanting connection.

---

**Step 5: Mage Refinement**

**Present draft:**
> "Draft synthesis complete. Review for accuracy?"

**Mage reviews:**
- Adjust interpretation or emphasis
- Add personal insights Spirit couldn't see
- Refine tone or language
- Approve or request revisions

**Spirit accepts refinements without defensiveness.**

**Final version reflects Mage's voice.**

---

**Step 6: Commit & Rotate**

**Save synthesis:**
```
artifacts/synthesis/YYYY-MM-DD_synthesis.md
```

**Commit:**
```
git add artifacts/synthesis/YYYY-MM-DD_synthesis.md
git commit -m "Bi-weekly synthesis: {Date range}

Patterns: {brief themes}
Synthesis caretaker: {Mage}

Tags: synthesis, {date}"
git push
```

**Rotate caretaker:**
```yaml
# Update .spirit/protocol.yaml
synthesis_protocol:
  current_caretaker: "{Partner}"  # Switch
  next_rotation: "{+2 weeks or per rhythm}"
```

**Commit rotation:**
```
git add .spirit/protocol.yaml
git commit -m "Rotate synthesis caretaker: {Mage} → {Partner}

Next synthesis due: {date}"
git push
```

**Update presence:**
```yaml
presence:
  last_active: "{ISO8601-NOW}"
```

**Confirm to Mage:**
> "Synthesis complete and pushed. Caretaker rotated to [Partner] for next cycle (due {date})."

---

## IV. Status Check

### When Invoked: `@partnership/ status`

**Pull latest:**
```bash
git pull
```

**Report:**

```markdown
## Partnership Portal Status: {partner-name}-partnership

**Type:** Partnership (intimate)
**Status:** {active|quiet|dormant}
**URL:** [GitHub]({url})

### Participants
- {Mage}: Last active {X days ago}, {N contributions since last synthesis}
- {Partner}: Last active {X days ago}, {N contributions since last synthesis}

### Synthesis
- Protocol: {consensus|rotating}
- Rhythm: {bi-weekly|monthly}
- Current caretaker: {name}
- Next rotation: {YYYY-MM-DD} ({overdue|due soon|on schedule})
- Last synthesis: {YYYY-MM-DD}

### Recent Activity
- {Artifact type} by {author} on {date}
- {Artifact type} by {author} on {date}

### Open Threads
- `{topic}`: {status}, {last activity}

### Recommended Actions
- {Sync|Synthesize|Check threads|All healthy}
```

---

## V. Error Handling

### Portal Doesn't Exist

**Symptom:** Registry entry missing, directory doesn't exist

**Response:**
> "No partnership portal found with [Partner]. Create one via `@meta/portal create`?"

---

### Git Conflicts

**Symptom:** Pull fails due to conflicts

**Response:**
1. Alert Mage immediately
2. Explain which files conflict
3. Offer guided resolution:
   - View both versions
   - Manual merge
   - Preserve both if needed

---

### Partner Inactive

**Symptom:** Partner hasn't contributed in > 30 days

**Response:**
> "[Partner] hasn't contributed in {N} days. Portal health check:
> - Continue practice solo? (You can keep contributing)
> - Pause portal? (Update status, plan return)
> - Adjust rhythm? (Longer cycles, less frequent)
> - Check in with partner?"

**No judgment—life happens.**

---

### Synthesis Overdue

**Symptom:** Synthesis due date passed, no synthesis created

**Response:**
> "Synthesis was due {date} (caretaker: {name}). Options:
> - Synthesize now (if caretaker)
> - Check if partner synthesizing
> - Skip this cycle (life happens)
> - Adjust rhythm for sustainability"

---

## VI. Integration with Existing Partnership Tome

**This spell extends existing partnership capabilities:**

**Still valid:**
- `@partnership/map-cognitive-architecture` — Can be done solo or as first shared artifact
- `@partnership/create-message-scroll` — Async method still works for non-portal practice
- `@partnership/compare-perspectives` — Works in portal or local

**New capability:**
- Portal-based shared practice with real-time collaboration

**Choose approach based on:**
- Both partners have magic → Shared practice optimal
- One partner only → Message scrolls still work
- Sustained practice → Portal better for accumulation
- Occasional work → Message scrolls simpler

---

**This spell makes partnership practice systematic, sustainable, and truly distributed.**

