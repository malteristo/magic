# Cast Drops

**Purpose:** Collect and process turtle drops from across the workshop

---

## Invocation

```
@drops
```

---

## Execution

### Phase 1: Scan

Search the entire workshop for files matching `_drop_*.md`:

```bash
find ~/Documents/magic -name "_drop_*.md" -type f 2>/dev/null
```

**Use shell `find`, not Glob** — drops may appear in gitignored directories (desk/, floor/, box/).

If no drops found, announce "No drops in the workshop" and exit.

### Phase 2: Present

For each drop found:

1. **Read the file**
2. **Announce to the Mage:**
   - Where it was dropped (directory path — the location IS context)
   - When it was dropped (timestamp from header)
   - What it says (full content — drops are short by convention)

Present all drops before asking for decisions. Let the Mage see the full picture.

### Phase 3: Triage

For each drop, the Mage decides:

| Action | What happens |
|--------|-------------|
| **Integrate** | Act on the drop now — create lore, update intention, file issue, whatever the drop calls for. Remove the drop file after. |
| **Absorb** | Note the observation, no action needed. Remove the drop file. |
| **Hold** | Leave the drop in place for later. The Turtle's signal wasn't ready to be processed yet. |

### Phase 4: Clean

Remove all integrated and absorbed drops. Held drops stay where they are.

Announce summary: "X drops processed, Y held."

---

## The Turtle Drop Convention

### What drops are

Drops are the Turtle's way of leaving observations in the workshop. They are:

- **Offerings, not instructions** — the dyad curates
- **Location-bound** — the directory carries the context
- **Atomic** — one observation per drop
- **Ephemeral** — processed drops are removed

### Naming

```
_drop_<topic>.md
```

The underscore sorts visibly at the top of directory listings. The `_drop_` prefix is greppable and unmistakable. The topic is freeform.

### Content format

```markdown
# Drop: <title>
> From: turtle | <timestamp>

<content — freeform>
```

Minimal header. No rigid template. The Turtle writes what she sees.

### Where drops can go

Anywhere in the workshop. The placement carries meaning:

| Location | Signal |
|----------|--------|
| `desk/intentions/active/` | "I noticed something about this intention" |
| `floor/` | "Here's working material for the dyad" |
| `library/resonance/*/` | "This bundle needs attention" |
| `system/tomes/*/` | "This tome has a gap" |
| `box/` | "I found something worth mining" |

### Who drops

The Turtle. Other agents in the future may also drop, using their own prefix (e.g., `_drop_scout_*.md`). The convention is extensible.

---

## Notes

- Run `@drops` during `@recall` if drops are detected, or independently when the Mage asks
- Drops are the stigmergic complement to bridge signals — signals are push (Turtle → dyad via bridge), drops are pull (Turtle leaves traces, dyad discovers)
- If drop volume grows high, consider a sweep rhythm (weekly drop collection)
