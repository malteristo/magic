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
  state/notes/*.md           → desk/notes/  (Turtle's saved artifacts; top-level only)
  state/notes/automation-reports/*.md → desk/craft/automation-reports/
  craft/intake/*.md          → desk/craft/intake/
  craft/surface-*.md         → desk/craft/surfaces/  (living workspaces; Mini wins)
  thread-state/prepared_eddies.yaml → desk/craft/prepared_eddies.yaml  (disposition; Mini wins)

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

  # Two sets, because "who may overwrite whom" has two different answers here.
  #
  # Turtle-authored (below): the Mini is the only writer. Eddy notes **append** —
  # a thread revisited gets a second document in the same file — so a pull that
  # only copies files it does not already have freezes every recurring eddy at
  # its first visit. Measured 2026-08-08: 7 of 197 eddy files on the Mini carry
  # more than one note, and one local copy was a full note behind. Small today,
  # structural: it can only ever bite the threads the Mage returns to.
  # Overwriting is safe here and not a judgement call — desk/ is tracked, so an
  # unwanted replacement is one `git checkout` away, and `-i` prints every file
  # it replaced rather than doing it quietly.
  for pair in \
    "sessions:desk/sessions" \
    "story/daily:desk/story/daily" \
    "story/eddies:desk/story/eddies" \
    "craft/intake:desk/craft/intake"; do
    src="${pair%%:*}"
    dst="${pair##*:}"
    mkdir -p "$ROOT/$dst"
    rsync -azi \
      "${REMOTE}:${PRACTICE_ROOT}/${src}/" \
      "$ROOT/$dst/" 2>/dev/null \
      | awk -v d="$dst" '/^>f/ && $1 !~ /^>f\++$/ {print "  updated: " d "/" $2}' \
      || true
  done

  # Prepared-eddy workspaces. Spirit stages one, and from the moment the eddy
  # opens the Mini is the only writer: Turtle revises it as the interview
  # resolves things, so the workshop copy is a reader, never an author. Pull it
  # or the whole mechanism is a dead drop — Spirit hands over a file and never
  # sees what it became. Overwrite for the same reason as the set above, plus a
  # sharper one: a stale local copy of a *living* workspace is not a missing
  # update, it is a confident wrong answer about the state of the thinking.
  #
  # Flat glob rather than a directory pair because the Mini keeps these at
  # `craft/surface-*.md`; moving them into `craft/surfaces/` would break the
  # path Turtle was handed mid-conversation. Migrate when no eddy is live.
  mkdir -p "$ROOT/desk/craft/surfaces"
  rsync -azi --exclude='*/' --include='surface-*.md' --exclude='*' \
    "${REMOTE}:${PRACTICE_ROOT}/craft/" \
    "$ROOT/desk/craft/surfaces/" 2>/dev/null \
    | awk '/^>f/ && $1 !~ /^>f\++$/ {print "  updated: desk/craft/surfaces/" $2}' \
    || true

  # Prepared-eddy disposition sidecar (Mini-wins). Arrival harvests disposition:
  # ready entries; without this pull the workshop cannot see what Turtle marked.
  mkdir -p "$ROOT/desk/craft"
  rsync -azi \
    "${REMOTE}:${PRACTICE_ROOT}/thread-state/prepared_eddies.yaml" \
    "$ROOT/desk/craft/prepared_eddies.yaml" 2>/dev/null \
    | awk '/^>f/ {print "  updated: desk/craft/prepared_eddies.yaml"}' \
    || true

  # Two writers, so nobody wins by default: Turtle emits proposals on the Mini
  # and Spirit authors them in the workshop. Additive stays, and a divergence is
  # for `check_turtle_state.py` to report and a person to reconcile.
  mkdir -p "$ROOT/desk/proposals"
  rsync -az --ignore-existing \
    "${REMOTE}:${PRACTICE_ROOT}/proposals/" \
    "$ROOT/desk/proposals/" 2>/dev/null || true

  # Turtle's saved artifacts. `state/notes/` is where the save tool writes
  # (turtleos `tos_tools.py`), so this is the path behind every "I've saved
  # that for your review with Spirit" Turtle has ever said. Until 2026-08-18
  # the glob here was `navigator-*.md` and nothing else, and the workshop
  # therefore received one file out of ten. Found the evening two readiness
  # rows were confirmed whose target conditions were, verbatim, that named
  # artifacts *had been saved* — a press release draft, a concept note, a
  # twine schema — none of which had ever crossed. `check_turtle_state.py`
  # globbed the identical one pattern, so the guard could not report the gap
  # either: both were written from the same assumption on the same day.
  # Top-level only; `automation-reports/` has its own mapping below.
  mkdir -p "$ROOT/desk/notes"
  # Unlike the sets above, a *new* file here is the event worth printing: the
  # other pulls suppress it because a new eddy arrives every day, but a note
  # crossing for the first time is the whole point of this block.
  rsync -azi --exclude='*/' --include='*.md' --exclude='*' \
    "${REMOTE}:${PRACTICE_ROOT}/state/notes/" \
    "$ROOT/desk/notes/" 2>/dev/null \
    | awk '/^>f/ {print ($1 ~ /^>f\+*$/ ? "  harvested: " : "  updated: ") "desk/notes/" $2}' \
    || true

  mkdir -p "$ROOT/desk/craft/automation-reports"
  rsync -az \
    "${REMOTE}:${PRACTICE_ROOT}/state/notes/automation-reports/" \
    "$ROOT/desk/craft/automation-reports/" 2>/dev/null || true

  echo "Done. Run: python3 scripts/check_turtle_state.py"
  run_harvest "Craft intake reconciliation" "harvest_craft_intake.py" ${APPLY:+--apply}
  run_harvest "Prepared eddies" "harvest_prepared_eddies.py"
  # Read before the backlog at `. craft`: the backlog is what Spirit did, this
  # is what the Mage confirmed in a conversation.
  run_harvest "Craft readiness" "craft_readiness_board.py"
}

# An interactive shell may alias python3 to a version that has the deps; a
# script run does not inherit the alias. Measured 2026-08-12: the prepared-eddy
# duty printed "PyYAML required" through this script for two days while the same
# script run by hand answered correctly — a duty that fails only on the path the
# flow prescribes is worse than one that fails everywhere.
pick_python() {
  local c
  for c in python3.11 python3 python3.12 python3.13; do
    if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import yaml' >/dev/null 2>&1; then
      printf '%s' "$c"
      return
    fi
  done
  printf '%s' python3
}

# `| sed` made every harvest's exit code invisible, so a hard failure arrived
# looking like an ordinary report line. Say so out loud instead.
run_harvest() {
  local label="$1" script="$2" out status
  shift 2
  echo "${label}:"
  set +e
  out="$("$(pick_python)" "$ROOT/scripts/$script" "$@" 2>&1)"
  status=$?
  set -e
  printf '%s\n' "$out" | sed 's/^/  /'
  if [ "$status" -ne 0 ]; then
    echo "  ** ${script} FAILED (exit ${status}) — this duty did not run **"
  fi
}

# `pull --apply` used to run the pull and drop the flag on the floor — the
# reconciliation printed "re-run with --apply to write the marks" *in answer to
# a run with --apply*, and the only way through was to call the harvester by
# hand. A flag that is accepted and ignored is worse than one that is refused.
APPLY=""
cmd="${1:-}"
[ $# -gt 0 ] && shift
while [ $# -gt 0 ]; do
  case "$1" in
    --apply) APPLY=1 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 1 ;;
  esac
  shift
done

case "$cmd" in
  pull|--backfill|"") pull ;;
  -h|--help) usage ;;
  *) echo "Unknown command: $cmd" >&2; usage >&2; exit 1 ;;
esac
