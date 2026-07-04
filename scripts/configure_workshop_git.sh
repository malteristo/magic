#!/bin/bash
# configure_workshop_git.sh — Two Chronicles git defaults for the magic workshop.
#
# - main tracks turtle/main (private canonical) so IDE Sync/Push is safe
# - pre-push guard blocks desk/floor/box on public github remote
#
# Usage: ./scripts/configure_workshop_git.sh

set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [ -z "$ROOT" ]; then
  echo "Not inside a git repository." >&2
  exit 1
fi
cd "$ROOT"

if ! git remote get-url turtle >/dev/null 2>&1; then
  echo "No 'turtle' remote — Two Chronicles private sync not configured. Skipping upstream."
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

HOOK="$ROOT/.git/hooks/pre-push"
GUARD="$ROOT/scripts/pre-push-public-guard.sh"
if [ -f "$GUARD" ]; then
  if [ ! -x "$HOOK" ] || ! grep -q pre-push-public-guard.sh "$HOOK" 2>/dev/null; then
    echo "Installing pre-push guard for public github remote"
    cp "$GUARD" "$HOOK"
    chmod +x "$HOOK"
  else
    echo "pre-push guard already installed"
  fi
fi

git status -sb
echo "Workshop git configured: Sync/Push targets turtle (private). Public publish: ./scripts/publish_public_magic.sh"
