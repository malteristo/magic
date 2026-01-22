# Cast Activate

**Purpose:** Initialize Universe access by creating the `universe/` directory and cloning default sources.

---

## When to Use

- First time using Universe features
- Setting up a new Magic workshop
- Recovering from a fresh clone

---

## Procedure

### Step 1: Check for Existing Universe

```bash
if [ -d "universe/" ]; then
  echo "Universe already exists. Checking sources..."
  ls -la universe/
else
  echo "Creating universe/ directory..."
  mkdir -p universe
fi
```

### Step 2: Clone Default Sources

**PAI (Personal AI Infrastructure):**
```bash
if [ ! -d "universe/pai" ]; then
  git clone https://github.com/danielmiessler/Personal_AI_Infrastructure.git universe/pai --depth 1
  echo "✓ PAI cloned"
else
  echo "✓ PAI already present"
fi
```

**Daemon:**
```bash
if [ ! -d "universe/daemon" ]; then
  git clone https://github.com/danielmiessler/Daemon.git universe/daemon --depth 1
  echo "✓ Daemon cloned"
else
  echo "✓ Daemon already present"
fi
```

### Step 3: Create Universe README

If not present, create `universe/README.md` with source documentation.

### Step 4: Update .gitignore

Ensure `universe/` is in `.gitignore`:
```bash
if ! grep -q "^universe/" .gitignore 2>/dev/null; then
  echo "universe/" >> .gitignore
  echo "✓ Added universe/ to .gitignore"
fi
```

### Step 5: Announce Completion

```
Universe access activated.

Sources available:
- universe/pai/     — Personal AI Infrastructure
- universe/daemon/  — Personal API framework

Invoke @universe to explore. Use @universe harvest to translate patterns.
```

---

## Notes

- Universe sources are **not committed** to your Magic repository
- Each Mage clones their own copies
- Updates come from upstream (`cd universe/pai && git pull`)

---

*The Universe awaits. Explore wisely.*
