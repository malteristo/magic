#!/bin/bash
# configure_workshop_git.sh — Two Chronicles git defaults for the magic workshop.
#
# - main tracks turtle/main (private canonical) so IDE Sync/Push is safe
# - pre-push guard blocks desk/floor/box on public github remote
#
# Usage:
#   ./scripts/configure_workshop_git.sh              # this workshop
#   ./scripts/configure_workshop_git.sh <repo-path>  # a satellite repo you also keep
#
# The satellite form exists because guards installed only where they were written
# protect only the repository that wrote them. A practitioner's other public-bound
# repos — a product repo, a site, a fork — get nothing, and report clean while
# checking nothing. Point this at each of them.

set -euo pipefail

GUARD_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-}"

if [ -n "$TARGET" ]; then
  if [ ! -d "$TARGET" ]; then echo "No such directory: $TARGET" >&2; exit 1; fi
  ROOT="$(git -C "$TARGET" rev-parse --show-toplevel 2>/dev/null || true)"
  if [ -z "$ROOT" ]; then echo "Not a git repository: $TARGET" >&2; exit 1; fi
else
  ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
  if [ -z "$ROOT" ]; then echo "Not inside a git repository." >&2; exit 1; fi
fi
cd "$ROOT"
echo "Configuring: $ROOT"

# --- Satellite repo: machine-local guards, shared name list ------------------
# A satellite gets hooks in .git/hooks rather than tracked .githooks. That is a
# deliberate asymmetry, stated rather than hidden: tracked hooks in the magic
# workshop are how the framework reaches practitioners who clone it, but a
# product repo's downstream users have no practice and no name list, so a
# tracked guard there would fail open for everyone but its author. These hooks
# are yours, on this machine, and do NOT survive a clone.
if [ "$ROOT" != "$GUARD_ROOT" ]; then
  NAMES="$GUARD_ROOT/desk/config/private_names.txt"
  if [ ! -f "$NAMES" ]; then
    NAMES="$GUARD_ROOT/system/config/private_names.txt"
  fi
  if [ -f "$NAMES" ]; then
    git config magic.privateNames "$NAMES"
    echo "magic.privateNames -> $NAMES (shared with the workshop)"
  else
    echo "  warning: $NAMES does not exist yet — name checking stays off here." >&2
  fi

  EXC="$GUARD_ROOT/desk/config/sanitize_exceptions.txt"
  if [ ! -f "$EXC" ]; then
    EXC="$GUARD_ROOT/system/config/sanitize_exceptions.txt"
  fi
  if [ -f "$EXC" ]; then
    git config magic.sanitizeExceptions "$EXC"
    echo "magic.sanitizeExceptions -> $EXC"
  fi

  mkdir -p "$ROOT/.git/hooks"
  cat > "$ROOT/.git/hooks/pre-commit" <<EOF
#!/bin/bash
# Installed by magic's scripts/configure_workshop_git.sh — machine-local, not tracked.
exec "$GUARD_ROOT/scripts/sanitize.sh" "\$@"
EOF
  chmod +x "$ROOT/.git/hooks/pre-commit"
  echo "pre-commit installed (.git/hooks — machine-local, does not survive a clone)"
  echo ""
  echo "Verify what is already published:  $GUARD_ROOT/scripts/audit_public_history.sh <remote>"
  exit 0
fi

# --- Guards first, unconditionally ------------------------------------------
# These used to sit below the 'turtle' remote check, which exits early. That
# skipped hook installation for exactly the configuration that needs it most:
# a practitioner whose only remote is a public one.

git config core.hooksPath .githooks
echo "core.hooksPath = .githooks (tracked hooks — survive a clone)"

if [ -d "$ROOT/.git/hooks" ] && ls "$ROOT"/.git/hooks/pre-* >/dev/null 2>&1; then
  echo "  note: legacy hooks in .git/hooks are now inert; .githooks/ is authoritative"
fi

NAMES="$ROOT/desk/config/private_names.txt"
TEMPLATE="$ROOT/system/config/private_names.txt.template"
if [ ! -f "$NAMES" ] && [ -f "$TEMPLATE" ]; then
  mkdir -p "$ROOT/desk/config"
  cp "$TEMPLATE" "$NAMES"
  echo "Created desk/config/private_names.txt — add the names of"
  echo "  real people in your practice, or the pre-commit name check stays empty."
fi

if ! git remote get-url turtle >/dev/null 2>&1; then
  echo "No 'turtle' remote — Two Chronicles private sync not configured. Guards are installed; skipping upstream."
  git status -sb
  exit 0
fi

git fetch turtle main 2>/dev/null || git fetch turtle

current_remote="$(git config --get branch.main.remote || true)"
if [ "$current_remote" != "turtle" ]; then
  echo "Setting main upstream: turtle/main (was: ${current_remote:-unset})"
  git branch --set-upstream-to=turtle/main main
else
  echo "main already tracks turtle/main"
fi

git status -sb
echo "Workshop git configured: Sync/Push targets turtle (private). Public publish: ./scripts/publish_public_magic.sh"
