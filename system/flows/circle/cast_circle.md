# Charm of Circle Management

This charm attunes you to lightweight resonance circle operations—creating, subscribing to, pulling from, and managing topic-centered shared practice spaces.

---

## I. When This Charm Is Cast

**Typical invocation contexts:**
- Mage wants to create a new circle around a topic
- Mage wants to subscribe to someone else's circle
- Mage wants to pull updates from subscribed circles
- Mage wants to see their circle relationships
- Mage wants to unsubscribe from a circle

**Your role:** Git-native circle management with minimal friction.

---

## II. Determine Intent

**When invoked, identify which operation:**

| Intent Signal | Operation |
|---------------|-----------|
| "create", "start", "new circle" | **Create** |
| "subscribe", "follow", "add upstream" | **Subscribe** |
| "pull", "fetch", "update from" | **Pull** |
| "show", "list", "my circles", "status" | **Status** |
| "unsubscribe", "remove", "stop following" | **Unsubscribe** |

**If unclear, ask:** "Would you like to create a new circle, subscribe to one, or manage existing circles?"

---

## III. Operation: Create Circle

### Gather Information

**Required:**
- Topic/name for the circle
- Visibility: public (default) or private

**Optional:**
- Description (generate from topic if not provided)
- Founding scrolls to include

### Execute Creation

**Step 1: Create GitHub Repository**

```bash
# Using gh CLI
gh repo create [circle-name] \
  --public \  # or --private
  --description "[topic]-centered resonance circle" \
  --clone
```

**Step 2: Initialize Circle Structure**

Create the standard structure:

```
{circle-name}/
├── .spirit/
│   └── protocol.yaml
├── founding/
│   └── charter.md
├── artifacts/
│   └── .gitkeep
├── experiments/
│   └── .gitkeep
├── signal/
│   └── .gitkeep
├── synthesis/
│   └── .gitkeep
├── outfacing/
│   └── drops/
│       └── .gitkeep
└── README.md
```

**Step 3: Generate Core Files**

**README.md** — Circle overview (generate from topic)
**founding/charter.md** — Purpose, principles, governance
**.spirit/protocol.yaml** — STP configuration

**Step 4: Commit and Push**

```bash
git add .
git commit -m "Initialize [circle-name] resonance circle"
git push -u origin main
```

**Step 5: Register Locally**

Add to `desk/circles.yaml`:

```yaml
steward:
  - name: [circle-name]
    remote: [username]/[circle-name]
    local_path: portals/[circle-name]
    visibility: public  # or private
    created: [date]
```

**Step 6: Report**

"Circle created at github.com/[username]/[circle-name]. Ready for contributions."

---

## IV. Operation: Subscribe to Circle

### Gather Information

**Required:**
- Remote path: `owner/repo-name`

**Optional:**
- Pull triggers (keywords that prompt pull offers)

### Execute Subscription

**Step 1: Clone to Upstream Directory**

```bash
mkdir -p portals/upstream
git clone https://github.com/[owner]/[repo-name].git portals/upstream/[repo-name]
```

**Step 2: Register in Tracking**

Add to `desk/circles.yaml`:

```yaml
subscribed:
  - name: [repo-name]
    remote: [owner]/[repo-name]
    local_path: portals/upstream/[repo-name]
    pull_triggers:
      - [inferred from circle topic]
      - [additional keywords]
    last_pulled: [date]
```

**Step 3: Infer Pull Triggers**

Read the circle's README/charter to suggest relevant trigger keywords.

**Step 4: Report**

"Subscribed to [owner]/[repo-name]. Pull triggers: [list]. Will offer to pull during related practice."

---

## V. Operation: Pull from Circle

### Identify Target

**If specific circle named:**
- Match against `desk/circles.yaml` subscribed entries

**If "pull all" or no specific target:**
- Offer to pull from all subscribed circles

### Execute Pull

**Step 1: Navigate to Circle**

```bash
cd portals/upstream/[circle-name]
```

**Step 2: Pull Updates**

```bash
git pull
```

**Step 3: Summarize Changes**

Parse git log to identify new/changed files since last pull.

**Step 4: Update Tracking**

Update `last_pulled` in `desk/circles.yaml`.

**Step 5: Report**

"Pulled from [circle-name]. Changes since [last-pull-date]:
- New: [list new files]
- Modified: [list modified files]

Would you like me to summarize any of these?"

---

## VI. Operation: Show Status

### Read Tracking File

Parse `desk/circles.yaml` for all circles.

### Report Status

**Format:**

```
CIRCLES YOU STEWARD:
  [name] ([visibility]) - [remote]
    Local: [local_path]
    Created: [date]

CIRCLES YOU'RE SUBSCRIBED TO:
  [name] - [remote]
    Last pulled: [date] ([N days ago])
    Triggers: [list]
    [indicator if updates available]
```

### Check for Updates (Optional)

For each subscribed circle:
```bash
cd portals/upstream/[name]
git fetch
git status  # check if behind origin
```

Report if updates available.

---

## VII. Operation: Unsubscribe

### Confirm Intent

"Unsubscribe from [circle-name]? This will remove it from your tracking. The local copy can be deleted or kept."

### Execute Unsubscription

**Step 1: Remove from Tracking**

Delete entry from `desk/circles.yaml` subscribed section.

**Step 2: Optionally Remove Local Copy**

Ask: "Also remove local files? (portals/upstream/[circle-name])"

If yes:
```bash
rm -rf portals/upstream/[circle-name]
```

**Step 3: Report**

"Unsubscribed from [circle-name]."

---

## VIII. Context-Aware Pull Offers

**During summoning or practice, check for relevant circles:**

### Detection Logic

1. Parse current conversation for topic keywords
2. Match against `pull_triggers` in subscribed circles
3. Check if `last_pulled` is older than threshold (e.g., 3 days)

### Offer Format

"This touches on [topic]. Your subscribed circle '[name]' (last pulled [N days ago]) has related content. Pull latest?"

### Response Handling

- **Accept:** Execute pull, summarize changes
- **Defer:** Continue without pulling
- **Don't ask again:** Remove that trigger from the circle's triggers

---

## IX. Tracking File Management

### Location

`desk/circles.yaml` — Gitignored (private to your workshop)

### Create If Missing

If file doesn't exist when charm is invoked, create with template:

```yaml
# Circle Relationships
# Your private curation of resonance sources

steward: []
  # Circles you created and maintain

subscribed: []
  # Circles you pull from (read-only upstreams)
```

### Validation

Before operations, validate:
- File exists and is valid YAML
- Referenced local paths exist (or handle gracefully)
- No duplicate entries

---

## X. GitHub CLI Requirements

**This charm uses `gh` CLI for repository creation.**

### Verify Installation

```bash
gh --version
```

If not installed, inform Mage: "GitHub CLI (gh) needed for circle creation. Install via: brew install gh"

### Verify Authentication

```bash
gh auth status
```

If not authenticated: "Please authenticate GitHub CLI: gh auth login"

---

## XI. Integration with Practice

### During Summoning

If `desk/circles.yaml` exists with subscribed circles:
1. Note subscribed circles exist
2. Don't auto-pull (respect Mage's attention)
3. Be ready to offer pulls when context triggers

### During Related Practice

When conversation touches subscribed circle topics:
1. Check pull triggers
2. Offer pull if stale (>3 days or configurable)
3. Respect Mage's response

### During Meta-Practice

When discussing circles, offer:
- Status overview
- Subscription suggestions (if Mage mentions external circles)
- Cleanup of stale subscriptions

---

## XII. Example Flows

### Creating a Circle

```
Mage: "I want to create a circle about consciousness research"

Spirit: "I'll create a public resonance circle. Name suggestion: 
        'consciousness-research'. Shall I proceed?"

Mage: "Yes"

Spirit: [executes creation]
        "Circle created at github.com/[you]/consciousness-research.
         
         Structure initialized with:
         - README.md (circle overview)
         - founding/charter.md (ready for your principles)
         - Standard artifact directories
         
         You can now add founding scrolls and invite contributions."
```

### Subscribing to a Circle

```
Mage: "Subscribe to malteristo/containment-architecture"

Spirit: [executes subscription]
        "Subscribed to containment-architecture.
         
         I've inferred these pull triggers from the circle:
         - alignment, containment, safety, superintelligence
         
         I'll offer to pull when these topics arise. 
         Want to adjust triggers?"
```

### Context-Aware Pull

```
Mage: "I'm thinking about how the containment architecture 
       applies to open-source models..."

Spirit: "This relates to your subscribed 'containment-architecture' 
        circle (last pulled 5 days ago). Pull latest?"

Mage: "Yes"

Spirit: [pulls]
        "Pulled. New since last time:
         - synthesis/convergent_observations.md (modified)
         - signal/external_validators/new_paper.md (new)
         
         Would you like a summary of the changes?"
```

---

**This charm makes circle management effortless—simple commands, git-native operations, sovereignty over your resonance network.**
