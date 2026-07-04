#!/usr/bin/env bash
# Pull turtleOS practice outputs from Mini into Magic desk (one direction).
# Forge → Mini: no practice file push (Magic stays on Forge; turtleOS is sovereign).
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
  proposals/*.md             → desk/proposals/
  state/notes/navigator-*.md → desk/notes/
  state/notes/automation-reports/*.md → desk/craft/automation-reports/

Does not sync boom, bright, intentions, or briefings.
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
    "proposals:desk/proposals"; do
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
}

case "${1:-}" in
  pull|--backfill|"") pull ;;
  -h|--help) usage ;;
  *) echo "Unknown command: $1" >&2; usage >&2; exit 1 ;;
esac
