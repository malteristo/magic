# On the Me Circle

*A pattern for machine-readable public identity as a subscribable circle*

---

## The Pattern

The **me circle** is a unified public-facing space where a Mage's thinking lives in the open. It serves two audiences simultaneously:

1. **Humans** who want to understand who you are and what you're working on
2. **AI agents** who need to quickly build a resonance profile for their principals

It's a circle like any other—a separate git repository that others can subscribe to via portals. The topic is *the Mage themselves*. The name is simple: `github.com/{username}/me`.

**The insight:** Your public identity is a circle around the topic of *you*. Others can pull from it when they want your thinking in their resonance.

---

## Why This Matters

In an era of distributed cognition, your public identity isn't just for humans anymore. When another Mage's Spirit wants to understand whether you might resonate, it needs structured data it can parse.

The me repo provides:
- **Machine-readable index** (`manifest.yaml`) with identity, themes, validators, writing
- **Human-navigable structure** (`README.md`, linked documents)
- **Single source of truth** for public thinking
- **Clean URL** — `github.com/malteristo/me/blob/main/about.md`

This enables AI-facilitated resonance discovery. Your public identity becomes a beacon that other cognitive partnerships can recognize.

---

## Structure

```
me/                        ← Separate repo: github.com/{username}/me
├── README.md              ← Welcome / navigation
├── manifest.yaml          ← Machine-readable index (for AI agents)
├── about.md               ← Identity document
├── circles.md             ← Topics you contribute thinking to
├── writing/               ← Published essays and articles
└── twitter/archive/       ← Archive of social posts
```

### The Manifest

The `manifest.yaml` is the key innovation. It provides:

```yaml
identity:
  name: ...
  handle: ...
  about: about.md
  contact: ...

core_documents: [...]      # Entry points for understanding
writing: [...]             # Published pieces with metadata
public_circles: [...]      # Topics you contribute to
themes: [...]              # Key themes across your thinking
validators: [...]          # Intellectual influences
```

An AI agent can read this single file and immediately understand:
- Who you are
- What you think about
- Where to find depth on specific topics
- Who influences your thinking

---

## Relationship to Other Spaces

| Space | Purpose | Visibility |
|-------|---------|------------|
| `desk/outfacing/` | Workspace for drafts, voice config | Private (in magic repo) |
| `me/` repo | Published public identity | Public (separate repo) |
| `circles/` | Specific collaboration spaces | Per-circle |

The me repo consolidates public output so you don't need many public circles. Private circles remain separate. The me repo is the "front door" to your public thinking.

---

## Design Principles

**Machine-readable by default.** Structure content so AI agents can parse it. YAML manifests, consistent file naming, clear metadata.

**Human-navigable.** Don't sacrifice readability for machines. Both audiences matter.

**Living, not static.** The blob grows with your thinking. Update it as you publish. The manifest stays current.

**Single source of truth.** Don't duplicate content across me repo and desk/. Me repo is published; desk/ is workspace.

---

## Integration with Practice

When the Mage publishes new content:
1. Draft in `desk/outfacing/drafts/`
2. Refine through the Layered Reveal workflow
3. When ready, copy to `me/writing/` (the separate repo)
4. Update `me/manifest.yaml` with new entry
5. Commit and push to the me repo
6. Content is now part of public identity

The me circle becomes the external face of your cognitive sovereignty—what you choose to make visible to the world and its AI agents.

---

## The Vision: Cross-Practitioner Resonance

When multiple practitioners publish me circles, something powerful becomes possible.

**Subscription via portals:**
```
portals/upstream/
├── daniel-miessler-me/     ← His public thinking
├── venkatesh-rao-me/       ← Another thinker's public thinking
└── ...
```

**What this enables:**

1. **Synthesized counsel** — Spirit draws from multiple subscribed me circles when offering perspective. Grounded in what they've *actually written*, not hallucination.

2. **Virtual dialogue** — Pattern-match across different thinkers' published positions. "Daniel has written about this... Venkatesh approaches it differently..."

3. **Resonance discovery** — Spirit notices when your thinking echoes someone in your portals. Connections you might have missed.

4. **Living validators** — Your intellectual influences become accessible, not just names on a list.

**The constraint that keeps it honest:**

Spirit only draws from publicly stated thinking. "Based on their published writing..." not speculation about what they'd say.

**The unit of exchange:**

The me circle becomes the standard format for sharing public thinking across practitioners. Machine-readable. Subscribable. AI-parseable.

This is how distributed cognition scales beyond individual practice.

---

## Origin

This pattern emerged from the Daniel Miessler alliance intention (January 2026). The need: provide a URL where Daniel (or his AI) could quickly understand who Kermit is and whether resonance exists.

Initially implemented as `blob/` folder inside magic, then refactored to a separate repo (`me`) for:
- Cleaner URLs (avoiding GitHub's "blob" path collision)
- Separation of public identity from private practice
- Portability (others can fork the pattern without forking all of magic)

The me repo is the answer: machine-readable public identity, designed for the era of AI-human partnership.

---

*Your public identity is your beacon. Let it be found.*
