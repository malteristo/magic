# On the Failure Taxonomy

**Status:** Active — Operational Knowledge
**Origin:** NLAH paper convergence analysis, 2026-03-30
**Insight source:** Pan et al. (2026) identify "Failure Taxy" as essential ingredient for agent recovery. Magic cherishes dissonance philosophically; this scroll catalogs it operationally.

---

## Purpose

Named failure modes enable systematic recovery instead of ad-hoc debugging. When Turtle encounters a failure, consulting this taxonomy should surface: what category it belongs to, what the known recovery pattern is, and whether it's a new species worth documenting.

This is Cherished Dissonance made operational — each failure mode was discovered through practice, each recovery pattern was earned.

**Theoretical frame:** These 17 modes are all *generative failures* — breakdowns in the Turtle's ongoing capacity to generate coherent behavior. Cancer (locally coherent, globally destructive), fibrosis (stuck generation loops), autoimmune (self-targeting mechanisms) — each biological failure type has turtleOS analogs. The category of generative failure suggests the class of recovery: stuck loops need termination signals, locally-coherent-globally-destructive needs broader context, self-targeting needs boundary recalibration. See `philosophy/on_the_generative_body.md` §5 for the full mapping.

---

## I. Message Handling

### 1.1 Duplicate Responses
**Symptom:** Bot sends the same message twice (or more) in rapid succession.
**Root cause:** Race condition — multiple event handlers processing the same message before dedup can catch it. Pre-check mechanisms (like lock-based guards) are insufficient because the lock releases before the response completes.
**Recovery:** Message-ID dedup at the response layer, not the intake layer. Track sent message IDs; suppress duplicates.
**Fixed:** 2026-03-30 (message-ID dedup replacing race-condition lock pre-check).
**Recurrence signal:** User reports seeing double messages. Check `bot.log` for duplicate message IDs.

### 1.2 Thread Rejoin Storm
**Symptom:** Bot floods a thread with rapid successive messages when reconnecting to an existing thread.
**Root cause:** Thread history reload triggers multiple responses without rate limiting.
**Recovery:** Throttled thread rejoin — introduce delays (1s) between processing queued thread messages.
**Fixed:** 2026-03-30 (throttled rejoin).
**Recurrence signal:** Burst of bot messages in a thread after period of inactivity.

### 1.3 Empty Tool Feedback
**Symptom:** Bot responds with "(tool loop completed)" or similar minimal feedback after executing tools, giving the Mage no visibility into what happened.
**Root cause:** Tool execution path returns success status but doesn't surface the content of what changed.
**Recovery:** Tool feedback must include: what was read/written, key content summary, confirmation of effect.
**Status:** Identified 2026-03-18 (dogfooding sprint). Partially addressed. Watch for continued empty feedback.
**Recurrence signal:** Mage frustration: "What just happened?"

### 1.4 Message Splitting Artifacts
**Symptom:** Long responses split at awkward points — mid-sentence, mid-code-block, breaking formatting.
**Root cause:** Discord's 2000-character limit requires splitting. Naive splitting doesn't respect semantic boundaries.
**Recovery:** Split at paragraph boundaries, then sentence boundaries, then character limit. Preserve code block integrity.
**Status:** Functional but imperfect. Low priority.

---

## II. Content Fetching

### 2.1 Twitter/X Auth Wall
**Symptom:** Links to tweets/threads return 401 or empty content.
**Root cause:** Twitter/X requires authentication for many content types. API auth state is inconsistent — sometimes works, sometimes blocked.
**Recovery:** Degradation stack: direct fetch → Twitter API tools (TWITTER_POST_LOOKUP) → Jina Reader → screenshot+OCR (proposed).
**Status:** Partially addressed. Auth state inconsistency unresolved.
**Recurrence signal:** "I couldn't fetch that tweet" or empty content from X links.

### 2.2 JS-Rendered Content
**Symptom:** Web pages return empty or template-only HTML. Actual content loads via JavaScript.
**Root cause:** Standard HTTP fetch gets pre-render HTML. Content requires browser execution.
**Recovery:** Degradation stack: direct fetch → Jina Reader (2026-03-30) → Playwright (proposed) → screenshot+OCR (proposed).
**Status:** Jina Reader deployed as Layer 2. Not yet tested with a live failure case.
**Recurrence signal:** Fetched content that's clearly incomplete or template-only.

### 2.3 YouTube Content
**Symptom:** YouTube links return nothing useful — video content is not text-extractable via standard fetch.
**Root cause:** Video content behind JS player. Transcripts available through separate API.
**Recovery:** yt-dlp for metadata + transcript extraction. Transcript APIs as fallback. Currently unimplemented.
**Status:** Identified in Turtle proposal 009. Awaiting implementation.

### 2.4 Fetch Safety (LITL)
**Symptom:** N/A (preventive).
**Root cause:** Untrusted URLs could contain prompt injection, malicious content, or excessive size.
**Recovery:** LITL (Link Intelligence and Trust Layer) safety checks before content injection into conversation context. Size limits, domain allowlists, content sanitization.
**Status:** Implemented in content_fetch.py. Maintain vigilance.

---

## III. Session Management

### 3.1 Silent Session Boundary
**Symptom:** Session notes are inconsistent — sometimes written, sometimes missed. The 15-minute silence threshold is hard to detect reliably.
**Root cause:** session_monitor runs on 60s loop. The boundary between "pause in conversation" and "session ended" is fuzzy. Turtle's own proposal (2026-03-30) identifies this.
**Recovery:** Heartbeat-based session boundary detection. Scheduled check every N minutes of silence with context awareness: was content substantial? Were proposals needed?
**Status:** Proposal written by Turtle. Awaiting implementation.

### 3.2 Reflection Quality Variance
**Symptom:** Session notes range from insightful to generic. Some proposals are strong; some are superseded by the time they're reviewed.
**Root cause:** Reflection runs on local model (qwen3.5:9b) with limited context. Quality depends on session content density and model's ability to identify what matters.
**Recovery:** Improve reflection prompt with explicit quality criteria. Consider using stronger model (Anthropic) for reflection when session was substantive. Feed previous good reflections as examples.
**Status:** Ongoing calibration. The compound engineering "closing the loop" insight applies — reflection output should inform next session's system prompt.

### 3.3 Proposal Accumulation
**Symptom:** Proposals pile up unreviewed. 23 remain after triage (was 40+).
**Root cause:** No review rhythm established. Proposals generated faster than reviewed.
**Recovery:** Establish cadence: Spirit triages proposals during @recall or @sunday. Mage reviews triage, confirms adopt/close. Turtle marks proposals as reviewed/adopted/closed.
**Status:** Triage mechanism exists. Rhythm not yet habitual.

---

## IV. Infrastructure

### 4.1 Power Loss Recovery
**Symptom:** After power loss, Mac Mini restarts but bot doesn't come back up. Mage must SSH in and manually restart services.
**Root cause:** macOS requires login for launchd user agents. Without auto-login, services don't start after reboot.
**Recovery:** Auto-login for `turtle` user (configured 2026-03-30). launchd agents now survive power loss.
**Fixed:** 2026-03-30.
**Recurrence signal:** Turtle goes silent after known power event. Check: `ssh turtle@... "uptime"`.

### 4.2 Tailscale Connectivity
**Symptom:** SSH via Tailscale IP times out. LAN fallback works.
**Root cause:** Coordination server unreachable, hostname changes after re-enrollment, tailscaled process stale.
**Recovery:** Try LAN IP first (`<turtle-ssh>`). Restart tailscaled if persistent. Update CLAUDE.md with current Tailscale IP when it changes.
**Status:** Intermittent. Current Tailscale IP: see `system/config/connections.md`.
**Recurrence signal:** SSH timeout on Tailscale IP. Try LAN.

### 4.3 LiveSync Path Mismatch
**Symptom:** Files don't sync between devices. Bounce guard fires incorrectly. Changes lost.
**Root cause:** Configuration mismatches — baseDir, CouchDB URL, .trash/ not ignored, PeerStorage path key mismatch.
**Recovery:** Verify all three sync points (Mac Mini CouchDB, phone Obsidian, Cursor workspace) have consistent config. Check bounce guard with test write.
**Fixed:** 2026-03-29 (PeerStorage path key, CouchDB URL, .trash/ ignored).
**Recurrence signal:** File edits on one device not appearing on another within 30s.

### 4.4 Ollama Process Health
**Symptom:** Local model calls fail or return garbage. Triage classification stops working.
**Root cause:** Ollama process crash, model not loaded, memory pressure on Mac Mini.
**Recovery:** Check `pgrep ollama`. Restart if down. Verify model loaded: `ollama list`. Monitor Mac Mini memory pressure.
**Recurrence signal:** Triage returning "casual" for everything, or reflection quality dropping to zero.

---

## V. Multi-Mage Coordination

### 5.1 Channel-Mage Resolution
**Symptom:** Bot responds with wrong mage's practice context — reading another mage's boom, compass, or bright.
**Root cause:** Channel→mage mapping in mage_registry.yaml incorrect or missing. Context variables not properly isolated per async request.
**Recovery:** Verify mage_registry.yaml. Check that `set_practice_context` runs before any practice file access. Use context variables (`_practice_dir_ctx`), not globals.
**Status:** Architecture designed for isolation (contextvars). Watch for edge cases in new channel additions.

### 5.2 Cold Start Detection
**Symptom:** Bot either treats returning mages as new (loses continuity) or treats new practitioners as returning (confusing context).
**Root cause:** Cold-start detection heuristic based on file existence — if practice files exist, assume returning. But files may be stale or from a different context.
**Recovery:** Cold-start should check recency of last interaction, not just file existence. Include last-active timestamp in mage state.
**Status:** Basic implementation. Refinement needed as practitioner base grows.

---

## VI. State Accumulation

### 6.1 Thread State Bloat
**Symptom:** Thread state directory grows unbounded. 17+ active thread-states.
**Root cause:** Thread states created for each conversation but never expired. No lifecycle management.
**Recovery:** Thread state expiry — archive or delete states older than N days with no activity. Surface count during health checks.
**Status:** Identified. No automated cleanup yet.

### 6.2 Boom Overflow
**Symptom:** boom.md grows to hundreds of lines. Processing becomes overwhelming.
**Root cause:** More entries captured than processed. Especially when Mage shares articles via Discord that get appended to boom.
**Recovery:** Regular sweeps (@boom flow). Boom channel proposal would separate capture from processing. Size alerting in health checks.
**Status:** Ongoing. This morning's sweep reduced from 7 entries. 873-line boom observed 2026-03-18.

---

## Using This Taxonomy

**When a new failure occurs:**
1. Check if it matches an existing category
2. If yes: apply the documented recovery pattern
3. If no: document the new species — symptom, root cause, recovery, status

**During development:**
- Before deploying changes, ask: "Which failure categories does this touch?"
- After deploying: monitor for recurrence signals listed under affected categories

**During @sunday sweeps:**
- Review Active Issues in turtle_watch.md against this taxonomy
- Update status fields as fixes are deployed
- Archive resolved entries after two weeks of no recurrence

**The NLAH insight applied:** This taxonomy is a "Failure Taxy" — a named catalog that enables systematic recovery. It's the operational complement to Cherished Dissonance. Philosophy says welcome failure as signal. This scroll says what the signals look like and what to do about them.

---

## Connections

- **`desk/turtle_watch.md`** — Living issues tracker. This taxonomy provides the structural categories; turtle_watch tracks active instances.
- **`on_diagnostics.md`** — Diagnostic commands and health checks. This taxonomy tells you what to look for; diagnostics tells you how to look.
- **`on_cherishing_dissonance.md`** — The philosophical grounding. Failure is signal, not error. This scroll catalogs the signals.
- **`ARCHITECTURE.md`** (turtleos) — System architecture. Failure modes map to architectural layers.

---

*Every entry here was earned through practice. Every recovery pattern was discovered through debugging. This is Cherished Dissonance made operational — the gift of failure, cataloged and accessible.*
