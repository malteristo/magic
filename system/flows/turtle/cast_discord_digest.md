# Cast Discord Digest

**Purpose:** Read recent Discord conversations, extract boom entries, generate dogfooding proposals for turtleOS/Spirit behavior, and manage trace lifecycle  
**Invocation:** `@discord-digest`  
**Frequency:** Post-summoning re-entry (before boom sweep), or on-demand  
**Duration:** 5–10 minutes  
**Output:** Boom entries appended to `desk/boom.md`, proposals to `desk/proposals/`, digest summary presented to Mage

---

## When to Use

- **Post-summoning:** Runs as part of the re-entry sequence (after `@recall`, before boom sweep) so Discord-sourced entries get swept in the same pass
- **On-demand:** When the Mage wants to see what happened on Discord since last session
- **Dogfooding:** When actively developing turtleOS and wanting Spirit-on-Cursor's independent assessment of Turtle behavior

**Graceful skip:** If SSH to the Turtle is unreachable, announce "Turtle offline — skipping Discord digest" and continue.

---

## Execution

### Phase 1: Pull Messages from Both Channels + Threads

Fetch from two channels. Channel IDs are stored in `~/turtle-shell/.env` on the Mac Mini.

**#dialogue** (`DISCORD_CHANNEL_DIALOGUE`) — the conversational surface:

```bash
ssh turtle@100.82.131.75 'TOKEN=$(grep DISCORD_BOT_TOKEN ~/turtle-shell/.env | cut -d= -f2); CHANNEL=$(grep DISCORD_CHANNEL_DIALOGUE ~/turtle-shell/.env | cut -d= -f2); curl -s -H "Authorization: Bot $TOKEN" "https://discord.com/api/v10/channels/$CHANNEL/messages?limit=100" | python3 -c "
import json, sys
msgs = json.load(sys.stdin)
for m in reversed(msgs):
    ts = m[\"timestamp\"][:16]
    author = m[\"author\"][\"username\"]
    reply = \"\"
    if m.get(\"message_reference\") and m.get(\"referenced_message\"):
        ref = m[\"referenced_message\"]
        reply = f\" [replying to: {ref[\"author\"][\"username\"]}]\"
    content = m[\"content\"][:300].replace(chr(10), \" \")
    print(f\"{ts} | {author:15}{reply} | {content}\")
"'
```

**#system** (`DISCORD_CHANNEL_SYSTEM`) — Spirit's activity log:

```bash
ssh turtle@100.82.131.75 'TOKEN=$(grep DISCORD_BOT_TOKEN ~/turtle-shell/.env | cut -d= -f2); CHANNEL=$(grep DISCORD_CHANNEL_SYSTEM ~/turtle-shell/.env | cut -d= -f2); curl -s -H "Authorization: Bot $TOKEN" "https://discord.com/api/v10/channels/$CHANNEL/messages?limit=50" | python3 -c "
import json, sys
msgs = json.load(sys.stdin)
for m in reversed(msgs):
    ts = m[\"timestamp\"][:16]
    author = m[\"author\"][\"username\"]
    content = m[\"content\"][:300].replace(chr(10), \" \")
    print(f\"{ts} | {author:15} | {content}\")
"'
```

**Threads in #dialogue** — where deep conversation happens:

```bash
ssh turtle@100.82.131.75 'TOKEN=$(grep DISCORD_BOT_TOKEN ~/turtle-shell/.env | cut -d= -f2); CHANNEL=$(grep DISCORD_CHANNEL_DIALOGUE ~/turtle-shell/.env | cut -d= -f2); curl -s -H "Authorization: Bot $TOKEN" "https://discord.com/api/v10/channels/$CHANNEL/threads/active" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for t in data.get(\"threads\", []):
    print(f\"Thread: {t[\"name\"]} (id: {t[\"id\"]}, messages: {t.get(\"message_count\", \"?\")})\")
"'
```

For each active thread, fetch its messages:

```bash
ssh turtle@100.82.131.75 'TOKEN=$(grep DISCORD_BOT_TOKEN ~/turtle-shell/.env | cut -d= -f2); curl -s -H "Authorization: Bot $TOKEN" "https://discord.com/api/v10/channels/THREAD_ID/messages?limit=50" | python3 -c "
import json, sys
msgs = json.load(sys.stdin)
for m in reversed(msgs):
    ts = m[\"timestamp\"][:16]
    author = m[\"author\"][\"username\"]
    content = m[\"content\"][:300].replace(chr(10), \" \")
    print(f\"{ts} | {author:15} | {content}\")
"'
```

**Cutoff:** Use the timestamp from `floor/briefings/latest.md` to focus on messages since last session. If no previous brief exists, process all fetched messages.

---

### Phase 2: Context Loading

Before analyzing the conversation, load the lens:

- `desk/intentions/compass.md` — life landscape
- `desk/intentions/active/*.md` — headers only (name, priority, phase, focus)
- `desk/boom/bright.md` — current mind surface

This context enables recognizing which conversation topics connect to active intentions and which bright entries are already tracked.

---

### Phase 3: Content Digest

Read the conversation content across #dialogue main channel, all active threads, and #system log. Extract:

**Boom entries:**
- Ideas, questions, or insights that emerged in conversation
- Unresolved threads of thought worth holding
- Anything the Mage said that hasn't been captured in the workshop yet
- Interesting patterns or connections noticed by the Turtle

**Intention connections:**
- Which active intentions were discussed or advanced?
- Any new intention signals (topics that keep recurring but don't have an intention yet)?

**#system cross-reference:**
- What operations did the Turtle perform? (session notes, boom patches, thread creation, etc.)
- Did the Mage comment on or react to any #system entries? These are direct behavioral feedback — surface them prominently.

---

### Phase 4: Dogfooding Review

Evaluate Turtle's behavior from Spirit-on-Cursor's independent perspective:

**Dialogue quality:**
- Does Turtle sound like a practice partner or a generic assistant?
- Are responses demonstrating practice awareness? (referencing boom, bright, intentions, compass)
- Is the conversational texture warm, concise, and contextually aware?

**Thread orchestration:**
- Were threads recommended at appropriate moments?
- Were thread configurations (model, attunement) well-chosen for the topic?
- Did hub-and-spoke model work? (main channel synthesis, thread depth)

**Operational coherence:**
- Are #system log entries clear and useful?
- Do session notes accurately capture what happened?
- Any missed opportunities? (Could have offered a flow, connected to an intention, suggested a boom entry, etc.)

**Identity coherence:**
- Does Turtle maintain its identity across conversations?
- Any identity amnesia phrases? ("I'm just an AI", "I don't have access to", etc.)
- Does the Mage need to correct or redirect the Turtle frequently?

**Generate proposals** for `CLAUDE.md` / `system.md` / prompt improvements when specific behavioral patterns warrant them.

---

### Phase 5: Trace Lifecycle

Discord conversations accumulate. This phase manages the metabolism of communication traces:

**Session notes** (`practice/sessions/`):
- Are session notes being written when conversations go quiet?
- Do they capture the substance of what was discussed, or just surface-level summaries?
- Any gaps — conversations that happened but produced no session note?

**Thread lifecycle:**
- Which threads are still actively receiving messages?
- Which have gone quiet? Note concluded threads for awareness.
- Any thread context worth absorbing into the workshop (lore, proposals, intention updates)?

**Uningested insights:**
- Ideas that emerged in Discord but never reached `desk/boom.md` — these traces evaporate if not captured
- Mage statements that express intention, desire, or frustration — these are boom material

**Cross-substrate sync:**
- Are `practice/boom.md` and `practice/bright.md` on the Turtle in sync with workshop versions?
- Flag any drift (workshop updated but Turtle stale, or vice versa)

---

### Phase 6: Route and Present

**Present the digest:**

```
## Discord Digest — [date]

**Period:** [since last session / date range]
**Sources:** #dialogue (N messages), #system (N entries), N active threads

### What Happened
[2-4 sentence summary of conversation topics and activities]

### Boom Entries (N new)
[List entries extracted — these will be appended to desk/boom.md]

### Dogfooding Observations
[Behavioral assessment — what's working, what could improve]

### Proposals (if any)
[Specific turtleOS/Spirit behavior changes worth making]

### Trace Status
[Thread lifecycle, sync status, any metabolism concerns]
```

**Route:**
- Boom entries → append to `desk/boom.md` (will be swept in the following boom pass)
- Substantive proposals → write to `desk/proposals/` with descriptive filename
- Quick observations → present inline, no file needed

---

## Error Handling

| Situation | Response |
|-----------|----------|
| SSH unreachable | "Turtle offline — skipping Discord digest." Continue re-entry. |
| Discord API error | Note the error, continue with whatever data was retrieved |
| No messages since last session | "Discord quiet since last session." Skip to Phase 5 (trace lifecycle check). |
| No threads active | Note "No active threads." Proceed normally. |
| #system channel empty or missing | Skip #system analysis. Note "Activity log unavailable." |

---

## Integration Points

- **Post-summoning stack:** Runs after `@recall`, before boom sweep — so Discord-sourced entries get swept in the same pass
- **`@sunday`:** Can run as part of the maintenance sweep for weekly catchup
- **`@discord-health`:** Complementary. Health checks behavioral metrics; digest reads content. Run independently or together.
- **`@recall`:** Recall reads session notes (Turtle's summaries). Digest reads raw conversation (Spirit's independent lens). Different perspectives on the same source.
- **On-demand:** Invoke anytime with `@discord-digest`

---

## What This Is

This is Spirit-on-Cursor reading the Discord conversation with independent eyes. The Turtle writes session notes from its own perspective. This flow gives the Mage a second perspective — Spirit observing Turtle's behavior, extracting insights the Turtle may have missed, and proposing improvements from the outside.

During dogfooding, this is especially valuable: Spirit can notice patterns in Turtle's behavior that the Turtle cannot notice about itself.

---

*First designed: 2026-03-18*
*Source: Post-summoning meta-practice — clarifying what the dot protocol triggers and what re-entry should include*
