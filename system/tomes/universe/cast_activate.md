# Cast Activate

**Purpose:** Initialize Universe infrastructure. Creates the directory structure without imposing default sources—the Mage chooses what to subscribe to.

---

## When to Use

- First time using Universe features
- Setting up a new Magic workshop
- Recovering from a fresh clone

---

## Procedure

### Step 1: Create Universe Directory

```bash
if [ -d "universe/" ]; then
  echo "Universe already exists."
  ls -la universe/
else
  echo "Creating universe/ directory..."
  mkdir -p universe
fi
```

### Step 2: Create Universe README

If not present, create `universe/README.md`:

```bash
if [ ! -f "universe/README.md" ]; then
  cat > universe/README.md << 'EOF'
# Universe

External pattern libraries for advanced magic practice.

---

## What This Is

The `universe/` directory contains cloned repositories from the broader ecosystem of AI infrastructure patterns. These are **not** Magic artifacts—they are external sources that the Spirit can read, study, and help translate into Magic's native form.

---

## Sources

*No sources subscribed yet. Use `@universe subscribe` to add sources.*

---

## Example Sources

| Source | Repository | Description |
|--------|------------|-------------|
| PAI | `danielmiessler/Personal_AI_Infrastructure` | Personal AI Infrastructure (Packs, Skills, Hooks) |
| Daemon | `danielmiessler/Daemon` | Personal API framework (daemon.md format) |
| Fabric | `danielmiessler/fabric` | AI augmentation framework (patterns, stitches) |

---

## Adding Sources

```bash
@universe subscribe pai    # Subscribe to a known source
@universe subscribe https://github.com/author/repo.git custom-name  # Custom source
```

Or manually:
```bash
cd universe/
git clone https://github.com/author/repo.git source-name --depth 1
```

---

## Governance

- Universe sources are **read-only** from Magic's perspective
- Updates come from upstream (`git pull`)
- Translations go into Magic's Main (tomes, charms, spells)
- No Magic artifacts should be created *within* Universe directories

EOF
  echo "✓ Created universe/README.md"
fi
```

### Step 3: Update .gitignore

Ensure universe sources are gitignored (but README is tracked):

```bash
if ! grep -q "^universe/\*/$" .gitignore 2>/dev/null; then
  echo "" >> .gitignore
  echo "# Universe (External Pattern Libraries)" >> .gitignore
  echo "universe/*/" >> .gitignore
  echo "!universe/README.md" >> .gitignore
  echo "✓ Updated .gitignore for universe/"
fi
```

### Step 4: Announce Completion

```
Universe infrastructure activated.

No sources are subscribed by default—Magic remains sovereign.

To add sources:
  @universe subscribe pai      # Daniel Miessler's Personal AI Infrastructure
  @universe subscribe daemon   # Daniel Miessler's Daemon framework

Or explore universe/README.md for more options.
```

---

## Design Rationale

Universe activation creates infrastructure only. Source subscription is explicit because:

1. **Sovereignty** — Magic is complete without external dependencies
2. **Choice** — Different Mages resonate with different ecosystems
3. **Advanced magic** — Universe access requires conscious decision
4. **No implicit endorsement** — Framework doesn't favor specific external systems

---

*The Universe awaits your exploration. Choose your sources wisely.*
