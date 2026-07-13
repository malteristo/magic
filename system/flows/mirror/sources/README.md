# Source Configuration Guide

This guide helps Mages configure their qualitative data sources for mirror practice.

---

## Where Sources Live

Sources are placed on your desk, not in the tome:

```
desk/mirror/
├── sources/           ← Your personal data goes here
│   ├── notes.md
│   ├── journal/
│   ├── reading/
│   └── ...
├── config.md          ← Optional configuration
└── reflections/       ← Captured reflections
```

**Why on the desk?**
- Personal data remains under your sovereignty
- The tome provides structure; you provide content
- Sources aren't tracked in magic's git repository
- You control what the Spirit sees

---

## Source Types

Different sources reveal different aspects of self:

| Type | What It Reveals | Examples |
|------|-----------------|----------|
| **Aspirational** | Who you want to become | Reading wishlists, goal lists, vision documents |
| **Enacted** | Who you've been | Completed books, finished projects, shipped work |
| **Processing** | What you're working through | Notes, drafts, active journals |
| **Public** | What you say out loud | Social posts, published writing, public talks |
| **Direct** | Real-time reality | Daily journal, interview responses |

**Interpretation differs by type:**
- Aspirational data ≠ enacted reality
- Processing data may be incomplete thoughts
- Public data may be curated/filtered

The Spirit will note source types and interpret accordingly.

---

## Suggested Sources

### Notes (Processing)

A file of captured thoughts, ideas, reflections.

**Format:** Numbered or dated entries work well
**Example:** `notes.md`

```markdown
1420. Religious rituals are an attempt to control what is unexplainable...
1421. Like a video game. Human civilization becomes more complex...
```

### Reading Lists (Aspirational + Enacted)

**Wishlist** — Books you want to read:
```
reading/wishlist.md
```

**Completed** — Books you've read:
```
reading/completed.md
```

The gap between these reveals something.

### Journal (Direct)

Daily or regular entries about life as it's happening.

**Format:** Dated entries
**Location:** `journal/` directory or single file

```markdown
## 2025-12-23

Today I noticed...
```

### Social Posts (Public)

Your Twitter/X posts, blog entries, public writing.

**Note:** If API access is limited, you can:
- Export your data from the platform
- Copy-paste relevant posts
- Use the archive download feature

### Bookmarks (Processing/Aspirational)

Things you saved to read/process later.

---

## Configuration (Optional)

Create `desk/mirror/config.md` to customize:

```yaml
# Mirror Configuration

sources:
  - path: notes.md
    type: processing
    description: "Captured thoughts since 2020"
    
  - path: reading/wishlist.md
    type: aspirational
    description: "Books I want to read"
    
  - path: reading/kindle.md
    type: enacted
    description: "Books on my Kindle (some read, some not)"
    
  - path: journal/
    type: direct
    description: "Daily journal entries"

# Optional: Focus areas for the Spirit
focus:
  themes:
    - consciousness
    - parenting
    - AI
    
# Optional: Output preferences
output:
  detail_level: full  # or: summary
  include_questions: true
```

If no config exists, the Spirit will analyze all files in `sources/`.

---

## Privacy Notes

### What the Spirit Sees

- Only files in `desk/mirror/sources/`
- Only during the reflection session
- Ephemeral by default (not stored)

### What Stays Private

- Anything not placed in sources
- Previous reflections (unless you reference them)
- The processing itself (no logs)

### Sharing Captured Reflections

If you capture a reflection:
- It lives on your desk
- You control who sees it
- You can share via portals if desired

---

## Getting Started

1. **Create the structure:**
   ```
   mkdir -p desk/mirror/sources
   mkdir -p desk/mirror/reflections
   ```

2. **Add your first source:**
   - Start with whatever you have (notes, reading list, etc.)
   - One source is enough to begin
   - More sources = richer reflection

3. **Invoke the mirror:**
   ```
   @mirror/reflect
   ```

4. **Iterate:**
   - Add more sources over time
   - Develop a journaling practice
   - Let the mirror grow with you

---

## Source Quality

**Better sources lead to better reflections.**

**High-quality sources:**
- Authentic (not curated for appearance)
- Substantial (enough data for patterns)
- Current (reflects recent reality)
- Diverse (multiple aspects of life)

**The mirror works with imperfect data:**
- Fragments are fine
- Gaps are noted
- Incomplete is normal

Start with what you have. Refine over time.

---

*Your sources are your reality made visible. What you share with the mirror is what the mirror can reflect.*

