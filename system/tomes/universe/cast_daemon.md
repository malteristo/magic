# Cast Daemon

**Purpose:** Generate a `daemon.md` file from a Magic circle, enabling compatibility with Daniel Miessler's Daemon personal API format.

---

## When to Use

- You want your Magic circle to be queryable by Daemon-compatible systems
- You want to participate in AI-to-AI discovery via MCP
- You want a simple, section-based export of your identity

---

## Input

- **Circle path:** The circle to export (default: `circles/me/`)
- **Output path:** Where to write the daemon.md (default: `circles/me/daemon.md`)

---

## The Daemon Format

Daemon uses section-based markdown:

```markdown
[ABOUT]
Bio text...

[MISSION]
Mission statement...

[TELOS]
Problems, Missions, Goals...

[FAVORITE_BOOKS]
- Book 1
- Book 2

[PREFERENCES]
- Key: Value
```

Available sections: `ABOUT`, `CURRENT_LOCATION`, `MISSION`, `TELOS`, `FAVORITE_BOOKS`, `FAVORITE_MOVIES`, `FAVORITE_PODCASTS`, `DAILY_ROUTINE`, `PREFERENCES`, `PREDICTIONS`

---

## Translation Mapping

| Magic Source | Daemon Section |
|--------------|----------------|
| `about.md` introduction | `[ABOUT]` |
| `about.md` "What I'm Working On" | `[MISSION]` |
| `manifest.yaml` themes | Part of `[ABOUT]` |
| `about.md` "What I Enjoy" books | `[FAVORITE_BOOKS]` |
| `manifest.yaml` validators | Mentioned in `[ABOUT]` |
| (if present) location | `[CURRENT_LOCATION]` |
| (if present) preferences | `[PREFERENCES]` |

---

## Procedure

### Step 1: Read Source Files

Read the circle's core files:
- `manifest.yaml` — Structured identity
- `about.md` — Narrative identity

### Step 2: Extract Sections

For each Daemon section, extract from the appropriate Magic source:

**[ABOUT]:**
- Name and handle from manifest
- First paragraphs of about.md (up to "My World Model")
- Key themes from manifest

**[MISSION]:**
- Extract from "What I'm Working On" section of about.md
- First paragraph summarizing the mission

**[FAVORITE_BOOKS]:**
- Extract from "What I Enjoy" table in about.md
- Format as list

**[PREFERENCES]:**
- Extract from about.md if present
- Or synthesize from manifest themes

### Step 3: Generate daemon.md

Assemble into Daemon's section format:

```markdown
# DAEMON DATA FILE

This file contains the public information for a Daemon personal API.
Generated from Magic circle: {circle_path}

---

[ABOUT]
{about_content}

[MISSION]
{mission_content}

[FAVORITE_BOOKS]
{books_list}

[PREFERENCES]
{preferences}
```

### Step 4: Write Output

Save to the specified output path.

---

## Example Output

For the `me` circle, the generated daemon.md would be:

```markdown
# DAEMON DATA FILE

This file contains the public information for a Daemon personal API.
Generated from Magic circle: circles/me/

---

[ABOUT]

My name is Malte Risto and I'm building Magic—a practice for distributed cognition through AI-human partnership.

I've spent 15 years studying how humans and intelligent agents coordinate: PhD in experimental psychology, User Experience Research at Volkswagen's future mobility lab, and now building frameworks for AI partnership.

My main projects are Magic (distributed cognition practice), writing on cognitive sovereignty, and exploring how AI-human alliance can address problems that seemed intractable.

Key themes: distributed-cognition, ai-human-partnership, cognitive-sovereignty, pattern-recognition, meaning-crisis, inner-compass

[MISSION]

AI will shape how we think whether we're intentional about it or not. Magic is my attempt to be intentional.

Build practices for distributed cognition that help people:
- Maintain cognitive sovereignty in an AI-mediated world
- Form genuine partnership with AI systems
- Hear their inner compass more clearly, not less

[FAVORITE_BOOKS]

- "Gödel, Escher, Bach" by Douglas Hofstadter
- "The Fabric of Reality" by David Deutsch
- "The Book" by Alan Watts
- "Order Out of Chaos" by Ilya Prigogine
- "The Interpretation of Fairy Tales" by Marie-Louise von Franz
- "Memories, Dreams, Reflections" by C.G. Jung
- "The Extended Mind" by Andy Clark
- "Being Wrong" by Kathryn Schulz
- "Bird by Bird" by Anne Lamott

[PREFERENCES]

- Writing tools: Cursor IDE with Magic framework
- Primary focus: AI-human partnership, cognitive sovereignty
- Communication style: Direct, philosophical, pattern-oriented
- Values: Cognitive sovereignty, honest uncertainty, practice over doctrine
- Learning style: Building, dialogue, reading
```

---

## After Generation

The generated `daemon.md` can be:

1. **Committed to the circle** — Available in the git repo
2. **Deployed to Cloudflare** — Using Daemon's Astro template
3. **Used for MCP** — If you set up a Cloudflare Worker

See `universe/daemon/README.md` for deployment instructions.

---

## Lineage

This spell translates Magic's identity format to Daniel Miessler's Daemon format.

**Source:** [github.com/danielmiessler/Daemon](https://github.com/danielmiessler/Daemon)  
**Protocol:** JSON-RPC 2.0 / MCP

---

*Your identity, their interface. Translation enables connection.*
