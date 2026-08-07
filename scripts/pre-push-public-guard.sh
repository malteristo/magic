#!/bin/bash
# pre-push-public-guard.sh — nothing private reaches a remote that is not `turtle`.
#
# Two Chronicles: the `turtle` bare repo (Mac Mini, VPN-only) is the private
# canonical remote and holds the full tree. Every other remote is public or
# someone else's, and gets the published subset only, via
# scripts/publish_public_magic.sh.
#
# Rewritten 2026-08-07. The previous version was allowlist-shaped on the remote
# — correct, and unchanged below — but **blocklist-shaped on paths**:
#
#     git diff --name-only "$range" | grep -E '^(desk|floor|box)/'
#
# Three literal directories. That was adequate only because `.gitignore` kept
# everything else sensitive from being tracked at all, so the ignore file was
# silently acting as the other half of this guard. The moment tracking widens —
# which is exactly the change being considered — `AGENTS.md`, `mage_seal.md`,
# the live registries, `system/config/private_names.txt` and the archives all
# sail straight past, because none of them starts with desk/, floor/ or box/.
#
# So the path test is now an allowlist too, derived from
# scripts/public_surface.conf — the single statement of what may be public,
# shared with the publish script and the sanitiser. Anything not on that
# surface is blocked for any remote but `turtle`.
#
# Verify with: ./scripts/public_surface.sh --self-test

set -uo pipefail

ROOT="$(git rev-parse --show-toplevel)"
# shellcheck source=/dev/null
. "$ROOT/scripts/public_surface.sh"

PRIVATE_REMOTE="${MAGIC_PRIVATE_REMOTE:-turtle}"
remote_name="${1:-}"

# Allowlist, not blocklist: the private canonical remote is the ONLY one
# permitted to carry the full tree. Every other remote is guarded, including
# remotes added later (a partner's fork, a mirror) that nobody thought of when
# this was written.
if [ "$remote_name" = "$PRIVATE_REMOTE" ]; then
  exit 0
fi

ZERO="0000000000000000000000000000000000000000"
blocked=""

while read -r local_ref local_sha remote_ref remote_sha; do
  [ -z "${local_ref:-}" ] && continue
  [ "$local_sha" = "$ZERO" ] && continue

  if [ "$remote_sha" = "$ZERO" ]; then
    range="$local_sha"
  else
    range="${remote_sha}..${local_sha}"
  fi

  while IFS= read -r path; do
    [ -z "$path" ] && continue
    if ! is_public_surface "$path"; then
      blocked="${blocked}${path}"$'\n'
    fi
  done < <(git diff --name-only "$range" 2>/dev/null || true)
done

if [ -n "$blocked" ]; then
  count=$(echo "$blocked" | grep -c . || true)
  echo "BLOCKED: push to '$remote_name' would expose $count path(s) that are not on the public surface."
  echo ""
  echo "$blocked" | grep . | head -15 | sed 's/^/  /'
  [ "$count" -gt 15 ] && echo "  … and $((count - 15)) more"
  echo ""
  echo "The full tree goes to '$PRIVATE_REMOTE' only:   git push $PRIVATE_REMOTE main"
  echo "The public subset goes out via:                 ./scripts/publish_public_magic.sh"
  echo "What may be public is defined once in:          scripts/public_surface.conf"
  exit 1
fi

exit 0
