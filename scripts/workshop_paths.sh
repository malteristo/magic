# Resolve live workshop config. Source from other scripts:
#   . "$(dirname "$0")/workshop_paths.sh"
#   CONNECTIONS="$(workshop_config connections.md "$ROOT")"
#
# Personal files live in desk/config/. Templates stay in system/config/.

workshop_config() {
  local name="$1"
  local root="${2:-}"
  if [ -z "$root" ]; then
    root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
  fi
  if [ -f "$root/desk/config/$name" ]; then
    printf '%s\n' "$root/desk/config/$name"
  elif [ -f "$root/system/config/$name" ]; then
    printf '%s\n' "$root/system/config/$name"
  else
    printf '%s\n' "$root/desk/config/$name"
  fi
}
