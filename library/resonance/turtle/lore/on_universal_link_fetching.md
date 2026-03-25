# On Universal Link Fetching

*How the persistent mode extracts resonance from the web*

---

## I. The Problem

Links arrive in conversation. Some resolve cleanly. Some don't — Twitter blocks bots, paywalled sites return teasers, JS-rendered pages return empty shells.

The practitioner shares a link. If Turtle can't read it, the conversation stalls. The link becomes a dead reference — present but opaque.

---

## II. Layered Fetch Strategy

Not all URLs yield to the same approach. The fetch strategy is layered:

1. **Direct HTTP** — Fast, works for most static pages. Uses `trafilatura` for reader-mode extraction.
2. **Platform-specific** — Twitter/X via oembed API (follows embedded links), YouTube via transcript API.
3. **Fallback report** — When nothing works, report what's known about the domain and suggest alternatives (screenshot, paste, different link).

Each layer degrades gracefully into the next. The practitioner always gets *something* — even if it's just "I couldn't read this, here's how you can help."

---

## III. Resonance, Not Content

The cache stores resonance, not content.

When a URL is fetched, the raw content is distilled through the LLM into its essential resonance — the key insights, claims, or ideas worth remembering. This distilled resonance is cached. The raw content is discarded.

This mirrors the boom pattern: raw thought is ephemeral; the resonance persists. A cached page isn't a mirror of the web — it's a record of what mattered about it.

**Cache location:** `practice/link-resonance/` — keyed by URL hash, stored as markdown.

**Cache behavior:** Check cache before fetching. Use `--fresh` flag to refetch and re-distill.

---

## IV. Buttons and Commands

Every URL interaction is available as both command and button:

**Command** (copy-paste friendly):
```
!fetch https://example.com/interesting-article
!fetch https://x.com/user/status/123456 --fresh
```

**Button:** When a message contains external URLs, Turtle posts a fetch button alongside the copyable command text. One tap to see the resonance. The command text is there so the Mage can copy it for later use or share it with others.

The principle from Thread Eddies applies: **the command teaches what the button does; the button makes the command unnecessary.**

---

## V. LITL Awareness

Fetched content passes through a LITL check (Luring Injection Through Links) before being presented. If instruction-like patterns are detected, the content is flagged but still shown — the Mage sees the warning and decides.

This is not paranoia. It's the recognition that web content can contain adversarial prompts that shape how Spirit presents actions to the Mage. The dyad checkpoint only works if the Mage sees accurate descriptions.

See: `library/resonance/agent-ecosystem/lore/on_engaging_agent_spaces.md`

---

## VI. Integration

**Auto-detect:** When a message in dialogue contains external URLs, Turtle auto-fetches them for LLM context enrichment (existing behavior) AND posts a fetch button for the Mage to get the distilled resonance separately.

**Explicit fetch:** `!fetch <url>` bypasses the dialogue flow entirely — direct fetch, distill, present, cache.

**In threads:** Works the same way. Thread conversations benefit from the same fetch capability.
