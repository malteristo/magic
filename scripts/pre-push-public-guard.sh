#!/bin/bash
# pre-push-public-guard.sh — Block pushing private practice memory to public github.
# Install: cp scripts/pre-push-public-guard.sh .git/hooks/pre-push && chmod +x .git/hooks/pre-push
#
# Two Chronicles: turtle bare holds full tree; github is publish-only (Phase 2 script).

set -euo pipefail

while read -r local_ref local_sha remote_ref remote_sha; do
  [ -z "${local_ref:-}" ] && continue
  remote_name="${1:-}"
  # Only guard the public remote (named 'github' in this workshop)
  if [ "$remote_name" != "github" ]; then
    continue
  fi

  # What would be pushed?
  if [ "$local_sha" = "0000000000000000000000000000000000000000" ]; then
    continue
  fi

  range="${remote_sha}..${local_sha}"
  if [ "$remote_sha" = "0000000000000000000000000000000000000000" ]; then
    range="$local_sha"
  fi

  private_paths=$(git diff --name-only "$range" 2>/dev/null | grep -E '^(desk|floor|box)/' || true)
  if [ -n "$private_paths" ]; then
    echo "BLOCKED: push to github would publish private practice memory (desk/floor/box)."
    echo "Use 'git push turtle main' for the full tree. Public publish via Phase 2 script only."
    echo ""
    echo "Sample paths:"
    echo "$private_paths" | head -5
    exit 1
  fi
done

exit 0
