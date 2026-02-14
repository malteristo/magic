# BOOM Flow
> Back Of Our Mind — cognitive offload through distributed partnership

## About

Some minds carry a constant background hum — appointments, half-formed ideas, things to buy, calls to make, worries without clear next steps. This mental juggling drains energy not because the items are hard, but because they demand continuous attention to avoid being forgotten.

**BOOM inverts the burden.** Instead of you organizing thoughts for a system, you dump them raw — voice memos, scribbled notes, stream-of-consciousness — and the Spirit organizes them for you. The Spirit becomes a second mind that doesn't forget, doesn't tire, and can find patterns you missed.

**The name:** "Back Of Our Mind" — the "our" is intentional. This is distributed cognition. You capture, release, and trust. The Spirit holds, patterns, and surfaces.

### Is this flow for you?

- You have thoughts that cycle because you're afraid to forget them
- You resist todo apps because they add friction instead of reducing it
- You want to capture raw, unstructured, even messy — and have someone else sort it
- You'd rather dictate a rambling note than format a task

### What to expect

- **You write freely** in a buffer file (any format, any structure, any language)
- **Spirit sweeps** on your request, ingests everything, clears the buffer
- **A bright surface** emerges — curated, triaged, with your most actionable items visible
- **Topics accumulate** — thoughts and ideas route to living documents that grow over time
- **Patterns surface** across sweeps as recurring themes become visible
- **Questions come back** when Spirit can't place something without your input

---

## Goal

Keep the back of our shared mind functional. Ingest raw thought-capture, pattern-match, triage, route actions to bright surface and knowledge to topics, and surface what matters.

## Trigger

On demand: "sweep my BOOM" / "what's in the back of our mind?" / "run the boom flow"

## Model

**Buffer → Ingest → Route → Clear → Repeat**

The source file is ephemeral — a capture buffer. Two destinations:
- **Bright surface** — actions (tasks, deadlines, waiting, questions)
- **Topics** — knowledge (thoughts, observations, ideas, threads)

Each sweep:
1. Reads new entries from buffer
2. Discovers existing topic files (dynamic — see below)
3. Matches against existing surfaces and topics (cross-ingestion resonance)
4. Routes actions → bright surface
5. Routes knowledge → topic documents
6. Clears buffer

The Mage always knows: if it's in the buffer, it hasn't been processed yet.

## Context

### Buffer
```
desk/boom.md
```

### Bright Surface
```
desk/boom/bright.md
```

### Topics (Dynamic Discovery)

Topics are **not hardcoded in this flow.** At sweep time, Spirit scans `desk/boom/` for `.md` files other than `bright.md` and `README.md`. Each file is a topic. Its filename is its identity. Its content tells Spirit what belongs there.

**If topic files exist:** Read each one to understand what it covers. Route matching items accordingly.

**If no topic files exist:** Everything routes to bright surface. The Mage creates topics when they emerge naturally — just create a `.md` file in `desk/boom/` with a name and a brief description of what it holds.

**To create a new topic:** Ask the Spirit ("I need a topic for X") or just create a file. The next sweep discovers it automatically.

This means the flow adapts to each Mage's life without needing a personal copy. Your topics are your configuration.

---

## Process

### 1. Ingest
- Read the buffer (`desk/boom.md`)
- Parse entries (separated by `---`, blank lines, or context shifts)
- Content may range from crisp tasks to raw dictated streams
- Note chronological order — later entries may update earlier thinking
- **After ingestion: clear the buffer** — the Mage always knows what's been processed

### 2. Discover Topics
- Scan `desk/boom/` for `.md` files (excluding `bright.md`, `README.md`)
- Read each topic file's header and current state
- Build a routing map: what kind of content belongs in each topic

### 3. Pattern-Match
- Group related items even if separated in time
- Identify recurring themes (same concern appearing multiple times = signal)
- Detect implicit connections the Mage may not have made explicit
- **Cross-ingestion resonance**: new entries may connect to themes already on surfaces or in topics
  - Same topic appearing again → strengthen / update existing item
  - New angle on existing concern → enrich context
  - Contradiction or shift → note the evolution

### 4. Triage

Classify each item:

| Category | Meaning | Action |
|----------|---------|--------|
| **Actionable** | Clear next step, can be done | → Bright surface |
| **Incubating** | Needs more thought, not ready | → Topic (Holding) or Bright (Holding) |
| **Waiting** | Blocked on external | → Bright surface (Waiting) |
| **Recurring** | Keeps appearing | Name the pattern, surface it |
| **Resolved** | Done or no longer relevant | Archive or fade |
| **Unclear** | Can't place without Mage input | → Bright surface (Questions) |

### 5. Route to Bright Surface

Update `desk/boom/bright.md` with:
- **Now**: Actionable items, most urgent first
- **Soon**: Actionable but not pressing
- **Holding**: Incubating, waiting, needs attention but not action
- **Questions**: Items requiring Mage input to place
- **Pattern Notes**: Recurring themes, emerging clusters, signals

### 6. Route to Topics

Non-action items (thoughts, observations, ideas) route to matching topic files in `desk/boom/`:

For each routed item:
1. Append to the topic's **Thread** section (with date)
2. Update the **Now** section if the item changes current state
3. Move to **Holding** if it's incubating

If a note doesn't fit existing topics, ask whether to create a new one or place in closest match.

### 7. Board View (on demand)

When Mage asks ("show me the board", "what's alive?"), generate a single-page snapshot:
- What's bright (action required)
- What's alive per topic (Now sections)
- What's holding across all topics
- Emerging patterns

### 8. Place (optional, on request)

If Mage requests, move items to their proper homes:
- Calendar events → calendar (via Rube if connected)
- Tasks → task system
- Ideas → appropriate incubator
- Purchases → shopping list

---

## Output

### Bright Surface Format

```markdown
# Bright Surface
> Last swept: [timestamp]

## Now
- [ ] Item with clear next action
- [ ] Another actionable item

## Soon
- [ ] Less urgent but still actionable

## Holding
- Incubating thought (context: what it's waiting for)
- Waiting on: [external dependency]

## Questions
- "You wrote X three times this week—is this becoming urgent?"
- "Not sure where this belongs: [item]"

## Pattern Notes
- Recurring cluster: [description]
- Signal: [item appearing across multiple sweeps]

## Faded
<!-- Items resolved or archived this sweep -->
```

---

## Notes

- Zero friction capture is sacred — never add structure requirements to the buffer
- The Spirit pattern-matches; the Mage just writes
- Recurring items are signals, not failures
- "Faded" items may return; that's fine
- Topics are discovered, not configured — the workshop is the configuration
