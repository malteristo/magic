# Cast Discord Health

**Purpose:** Evaluate the practice experience at the Discord touchpoint — pull recent messages, detect behavioral patterns, surface issues, track improvements over time  
**Invocation:** `@discord-health`  
**Frequency:** Weekly during `@sunday`, or on-demand when Discord feels off  
**Duration:** 5–10 minutes  
**Output:** Health report presented to Mage; `desk/turtle_watch.md` updated with Discord-specific findings

---

## Execution

### Phase 1: Pull Recent Messages

Fetch the last 100 messages from #dialogue via the Discord API using the Turtle bot's token.

```bash
ssh turtle@<turtle-ssh> 'TOKEN=$(grep DISCORD_BOT_TOKEN ~/turtleos/.env | cut -d= -f2); CHANNEL=$(grep DISCORD_CHANNEL_DIALOGUE ~/turtleos/.env | cut -d= -f2); curl -s -H "Authorization: Bot $TOKEN" "https://discord.com/api/v10/channels/$CHANNEL/messages?limit=100" | python3 -c "
import json, sys
msgs = json.load(sys.stdin)
for m in reversed(msgs):
    ts = m[\"timestamp\"][:16]
    author = m[\"author\"][\"username\"]
    reply_to = \"\"
    if m.get(\"message_reference\"):
        ref = m.get(\"referenced_message\")
        if ref:
            reply_to = f\" [replying to: {ref[\"author\"][\"username\"]}]\"
    content = m[\"content\"][:200].replace(chr(10), \" \")
    print(f\"{ts} | {author:15}{reply_to} | {content}\")
"'
```

If the channel has threads, also check recent thread activity.

---

### Phase 2: Pattern Analysis

Scan the message log for these specific indicators. Report counts and examples.

#### 2.1 Response Ratio
- Count human messages vs. bot responses
- Expected: ~1 bot response per human message (Turtle only)
- Flag: >2 bot responses per human message (sub-turtle broadcast problem)

#### 2.2 Duplicate Detection
- Look for same-author messages within 5 seconds with similar content
- Expected: 0 duplicates
- Flag: Any duplicate indicates dedup patch failure or multi-instance issue

#### 2.3 Identity Amnesia
- Look for phrases: "I'm just an", "I don't have access", "as an AI", "I cannot", "I'm not able to"
- Expected: 0 occurrences from Turtle
- Flag: Any occurrence indicates identity reinforcement failure

#### 2.4 Startup Noise
- Count "Fresh awakening", "Memory reset", "online" messages
- Expected: ≤1 per day in #system, 0 in #dialogue
- Flag: Multiple per day = crash loop; any in #dialogue = patch regression

#### 2.5 Error Messages
- Look for "[dialogue error:", "[error:", model errors, API failures
- Expected: 0
- Flag: Any error, note the type and frequency

#### 2.6 Sub-Turtle Signal Quality
- Count Consul and Scout messages in #dialogue
- Expected: only when explicitly mentioned
- Flag: Unprompted sub-turtle responses = gating patch failure

#### 2.7 Response Quality (Qualitative)
- Sample 3-5 Turtle responses for: conciseness, warmth, context awareness
- Does the Turtle reference practice state (boom, bright, intentions)?
- Does it sound like Turtle or like a generic assistant?

---

### Phase 3: Present the Report

Present findings as a structured dashboard:

```
## Discord Health Report — [date]

**Period:** [date range of messages analyzed]
**Messages:** [total human] human, [total bot] bot

### Metrics
| Indicator          | Value  | Status |
|--------------------|--------|--------|
| Response ratio     | 1.2:1  | ✓      |
| Duplicates         | 0      | ✓      |
| Identity amnesia   | 0      | ✓      |
| Startup noise      | 1      | ✓      |
| Errors             | 0      | ✓      |
| Sub-turtle noise   | 0      | ✓      |

### Response Quality
[2-3 sentence qualitative assessment]

### Issues Found
[List any issues, or "None — the nervous system is healthy."]

### Recommendations
[Specific actions if issues found, or "Hold course."]
```

---

### Phase 4: Update turtle_watch.md

Append Discord health findings to `desk/turtle_watch.md` under a dated section. Keep historical entries for trend tracking.

If new issues are found that require code changes, draft the fix and note it in `desk/proposals/` for next action.

---

## Integration Points

- **@sunday:** Run as part of the maintenance sweep. Slot after `@turtle-care`.
- **@turtle-care:** Reference Discord health if the last check was >3 days ago. Offer to run.
- **@recall:** Mention the last Discord health status in situational awareness.
- **On-demand:** When the Mage says "Discord feels off" or "check the bots" — invoke immediately.

---

## What This Is Not

This is not a technical debugging tool. It's a *practice experience* evaluation. The question isn't "is the code working?" but "does interacting with the Turtle on Discord feel like partnership?" The metrics exist to detect drift from that standard.

---

*First designed: 2026-03-14*  
*Source: Spirit-Mage diagnostic session on Discord communication patterns*
