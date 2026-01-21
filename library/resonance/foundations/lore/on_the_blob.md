# On the Blob

*A pattern for machine-readable public identity*

---

## The Pattern

The **blob** is a unified public-facing space where a Mage's thinking lives in the open. It serves two audiences simultaneously:

1. **Humans** who want to understand who you are and what you're working on
2. **AI agents** who need to quickly build a resonance profile for their principals

The name "blob" is intentional—it's a living, growing mass of public thinking, not a rigid structure.

---

## Why This Matters

In an era of distributed cognition, your public identity isn't just for humans anymore. When another Mage's Spirit wants to understand whether you might resonate, it needs structured data it can parse.

The blob provides:
- **Machine-readable index** (`manifest.yaml`) with identity, themes, validators, writing
- **Human-navigable structure** (`README.md`, linked documents)
- **Single source of truth** for public thinking

This enables AI-facilitated resonance discovery. Your blob becomes a beacon that other cognitive partnerships can recognize.

---

## Structure

```
blob/
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
| `desk/outfacing/` | Workspace for drafts, voice config | Private |
| `blob/` | Published public identity | Public |
| `circles/` | Specific collaboration spaces | Per-circle |

The blob consolidates public output so you don't need many public circles. Private circles remain separate. The blob is the "front door" to your public thinking.

---

## Design Principles

**Machine-readable by default.** Structure content so AI agents can parse it. YAML manifests, consistent file naming, clear metadata.

**Human-navigable.** Don't sacrifice readability for machines. Both audiences matter.

**Living, not static.** The blob grows with your thinking. Update it as you publish. The manifest stays current.

**Single source of truth.** Don't duplicate content across blob and desk/. Blob is published; desk/ is workspace.

---

## Integration with Practice

When the Mage publishes new content:
1. Draft in `desk/outfacing/drafts/`
2. Refine through the Layered Reveal workflow
3. When ready, move to `blob/writing/`
4. Update `blob/manifest.yaml` with new entry
5. Content is now part of public identity

The blob becomes the external face of your cognitive sovereignty—what you choose to make visible to the world and its AI agents.

---

## Origin

This pattern emerged from the Daniel Miessler alliance intention (January 2026). The need: provide a URL where Daniel (or his AI) could quickly understand who Kermit is and whether resonance exists.

The blob is the answer: machine-readable public identity, designed for the era of AI-human partnership.

---

*The blob is your beacon. Let it be found.*
