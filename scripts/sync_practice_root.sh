#!/usr/bin/env bash
# Pull turtleOS practice outputs from Mini into Magic desk (one direction).
# Forge → Mini: no practice file push (Magic stays on Forge; turtleOS is sovereign).
#
# One deliberate exception, added 2026-08-06: scripts/export_craft_digest.py
# pushes a projection of desk/craft/backlog.md to craft/development.md, so
# craft-turtle can think about what to build next from the real state. The
# principle is unchanged — the *practice* stays on Forge. The development
# record of a piece of software is not the practice. That script is a
# selection, never a directory copy; read its docstring before widening it.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CONNECTIONS="$ROOT/system/config/connections.md"

if [ -z "${REMOTE:-}" ] && [ -f "$CONNECTIONS" ]; then
  REMOTE=$(grep -Eo 'turtle@[^`]+' "$CONNECTIONS" | head -1 || true)
fi
REMOTE="${REMOTE:-turtle@turtles-mac-mini}"
PRACTICE_ROOT="${TURTLE_PRACTICE_ROOT:-/Users/turtle/workshops/kermit}"

usage() {
  cat <<'EOF'
Usage: sync_practice_root.sh pull [--backfill]

  pull         Copy Mini practice outputs into local desk/ (never overwrites existing files)
  --backfill   Alias for pull (same behavior)

Maps:
  sessions/*.md              → desk/sessions/
  story/daily/*.md           → desk/story/daily/
  story/eddies/*.md          → desk/story/eddies/
  proposals/*.md             → desk/proposals/
  state/notes/navigator-*.md → desk/notes/
  state/notes/automation-reports/*.md → desk/craft/automation-reports/
  craft/intake/*.md          → desk/craft/intake/
  craft/moves/*.md           → desk/craft/moves/

Does not sync boom, bright, intentions, or briefings.
craft/backlog.md is deliberately NOT synced: the local copy is the worked one
(tick marks, notes). Reconcile it with scripts/harvest_craft_intake.py, which
reports remote intake ids that never reached the workshop.
Native topology: Mini ops reports land under practice root (not ~/workshop); Forge harvests via this pull.
EOF
}

pull() {
  local tmp
  tmp="$(mktemp -d)"
  trap 'rm -rf "${tmp:-}"' EXIT

  echo "Pulling from ${REMOTE}:${PRACTICE_ROOT}"

  for pair in \
    "sessions:desk/sessions" \
    "story/daily:desk/story/daily" \
    "story/eddies:desk/story/eddies" \
    "proposals:desk/proposals" \
    "craft/intake:desk/craft/intake" \
    "craft/moves:desk/craft/moves"; do
    src="${pair%%:*}"
    dst="${pair##*:}"
    mkdir -p "$ROOT/$dst"
    rsync -az --ignore-existing \
      "${REMOTE}:${PRACTICE_ROOT}/${src}/" \
      "$ROOT/$dst/" 2>/dev/null || true
  done

  mkdir -p "$ROOT/desk/notes"
  rsync -az --include='navigator-*.md' --include='*/' --exclude='*' \
    "${REMOTE}:${PRACTICE_ROOT}/state/notes/" \
    "$ROOT/desk/notes/" 2>/dev/null || true

  mkdir -p "$ROOT/desk/craft/automation-reports"
  rsync -az \
    "${REMOTE}:${PRACTICE_ROOT}/state/notes/automation-reports/" \
    "$ROOT/desk/craft/automation-reports/" 2>/dev/null || true

  echo "Done. Run: python3 scripts/check_turtle_state.py"
  echo "Craft intake reconciliation:"
  python3 "$ROOT/scripts/harvest_craft_intake.py" 2>&1 | sed 's/^/  /' || true
  echo "Craft moves:"
  python3 "$ROOT/scripts/harvest_craft_moves.py" 2>&1 | sed 's/^/  /' || true
}

case "${1:-}" in
  pull|--backfill|"") pull ;;
  -h|--help) usage ;;
  *) echo "Unknown command: $1" >&2; usage >&2; exit 1 ;;
esac
