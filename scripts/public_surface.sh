#!/bin/bash
# public_surface.sh — one answer to "may this path be public?", for every consumer.
#
# Sourced by scripts/pre-push-public-guard.sh, scripts/sanitize.sh and
# scripts/publish_public_magic.sh. Run directly for the self-test:
#
#   ./scripts/public_surface.sh --self-test    # unit checks + drift vs the live public repo
#   ./scripts/public_surface.sh --list         # every private-tree path that may be public
#   ./scripts/public_surface.sh --check PATH   # one path: public | private
#
# Why this exists: scripts/public_surface.conf, top of file.
#
# The design lesson underneath, learned the hard way on 2026-08-07: the six
# lists that used to answer this question did not merely duplicate each other,
# they described a publish that *does not happen*. `public.gitignore` carries
# `!floor/README.md` exceptions that never fire, because `floor/` is not
# rsync'd into the publish worktree at all — those files are in the public repo
# only because the worktree is `reset --hard github/main` and nothing ever
# prunes what is no longer intended. **The public tree is an accumulation, not
# a derivation.** So the self-test does not compare this config against the
# other configs; it compares it against the published artifact, which is the
# only ground truth in the system.

set -uo pipefail

PS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")/.." && pwd)"
PS_CONF="${PS_CONF:-$PS_ROOT/scripts/public_surface.conf}"

PS_DIRS=()
PS_FILES=()
PS_DENY=()

# Paths that must never be public regardless of what the conf says. This is the
# backstop for FILE-beats-DENY: an exact FILE entry is powerful enough to
# override a class rule, so the things that must never move sit here, in
# tracked code, where changing them is a visible act.
PS_ABSOLUTE_NEVER=(
  "desk/config/connections.md"
  "desk/config/private_names.txt"
  "desk/config/sanitize_exceptions.txt"
  "desk/config/declared_listeners.txt"
  "system/config/connections.md"
  "system/config/private_names.txt"
  "system/config/sanitize_exceptions.txt"
  "system/config/declared_listeners.txt"
  "AGENTS.md"
  "mage_seal.md"
)

ps_load() {
  [ "${#PS_DIRS[@]}" -gt 0 ] && return 0
  [ -f "$PS_CONF" ] || { echo "public_surface: missing $PS_CONF" >&2; return 1; }
  local kind value
  while read -r kind value _rest; do
    case "$kind" in
      DIR)  PS_DIRS+=("${value%/}") ;;
      FILE) PS_FILES+=("$value") ;;
      DENY) PS_DENY+=("$value") ;;
      ''|'#'*) ;;
    esac
  done < <(sed 's/#.*//' "$PS_CONF" | grep -E '^\s*(DIR|FILE|DENY)\s')
  return 0
}

_ps_denied() {
  local path="$1" pat base
  base="$(basename "$path")"
  for pat in "${PS_DENY[@]}"; do
    case "$pat" in
      */)
        # directory, at any depth: "archive/" matches a/b/archive/c
        local d="${pat%/}"
        [ "$path" = "$d" ] && return 0
        case "$path" in "$d"/*|*/"$d"/*) return 0 ;; esac
        ;;
      *\**)
        # shellcheck disable=SC2254
        case "$path" in $pat) return 0 ;; esac
        case "$base" in $pat) return 0 ;; esac
        ;;
      */*)
        [ "$path" = "$pat" ] && return 0
        ;;
      *)
        # bare token: basename, at any depth
        [ "$base" = "$pat" ] && return 0
        ;;
    esac
  done
  return 1
}

# is_public_surface <repo-relative-path> → 0 public, 1 private
is_public_surface() {
  ps_load || return 1
  local path="${1#./}" never d f
  [ -z "$path" ] && return 1

  for never in "${PS_ABSOLUTE_NEVER[@]}"; do
    [ "$path" = "$never" ] && return 1
  done

  # FILE beats DENY.
  for f in "${PS_FILES[@]}"; do
    [ "$path" = "$f" ] && return 0
  done

  _ps_denied "$path" && return 1

  for d in "${PS_DIRS[@]}"; do
    case "$path" in "$d"/*) return 0 ;; esac
  done
  return 1
}

# Every path in the working tree that may be public.
ps_list_surface() {
  ps_load || return 1
  local p
  while IFS= read -r p; do
    is_public_surface "$p" && echo "$p"
  done < <(cd "$PS_ROOT" && git ls-files)
  # The last path is often private; without this, `set -e` + pipefail
  # treats a finished listing as failure (publish_public_magic.sh).
  return 0
}

ps_publish_dirs()  { ps_load && printf '%s\n' "${PS_DIRS[@]}"; }
ps_publish_files() { ps_load && printf '%s\n' "${PS_FILES[@]}"; }
ps_deny_patterns() { ps_load && printf '%s\n' "${PS_DENY[@]}"; }

# ─── Self-test ───────────────────────────────────────────────────

_ps_fail=0
_ps_expect() { # <path> <public|private> <why>
  local got="private"
  is_public_surface "$1" && got="public"
  if [ "$got" != "$2" ]; then
    echo "  FAIL  $1 → $got, expected $2   ($3)"
    _ps_fail=$((_ps_fail + 1))
  fi
}

ps_self_test() {
  ps_load || return 1
  echo "public_surface self-test"
  echo "  conf: $PS_CONF (${#PS_DIRS[@]} DIR, ${#PS_FILES[@]} FILE, ${#PS_DENY[@]} DENY)"
  echo ""
  echo "Unit checks"

  # The framework ships.
  _ps_expect "system/flows/summon/covenant.md" public  "allowed DIR"
  _ps_expect "library/resonance/turtle/README.md" public "allowed DIR"
  _ps_expect "README.md" public "allowed FILE"
  _ps_expect "AGENTS.md.template" public "template ships, personal file does not"

  # The practice record does not.
  _ps_expect "desk/craft/backlog.md" private "practice memory"
  _ps_expect "floor/briefings/latest.md" private "practice memory"
  _ps_expect "box/transcripts/some-call.md" private "practice memory"
  _ps_expect "desk/intentions/active/turtle.md" private "practice memory"

  # FILE beats DENY — the scaffolding exception.
  _ps_expect "desk/README.md" public "FILE beats DENY desk/"
  _ps_expect "box/transcripts/ytfetch.py" public "FILE beats DENY box/"

  # The absolute set is unreachable.
  for never in "${PS_ABSOLUTE_NEVER[@]}"; do
    _ps_expect "$never" private "absolute never"
  done

  # Instance config is desk/; system/config keeps a DENY backstop if someone
  # writes a live file there again. Templates still ship.
  _ps_expect "desk/config/connections.md" private "instance config"
  _ps_expect "system/config/sanitize_exceptions.txt" private "backstop if rewritten under system/"
  _ps_expect "system/config/declared_listeners.txt" private "backstop if rewritten under system/"
  _ps_expect "system/config/connections.md.template" public "templates ship"

  # Class rules.
  _ps_expect "library/archive/old.md" private "archive/ at any depth"
  _ps_expect "system/tomes/librarian/x.md" private "denied subtree"
  _ps_expect "system/foo.lock" private "runtime noise"
  _ps_expect ".DS_Store" private "OS noise"
  _ps_expect "circles/registry.yaml" private "live registry"
  _ps_expect "circles/registry.yaml.template" public "template ships"

  # Positive control: the matcher must be able to say no for the right reason.
  local before_fail=$_ps_fail
  if is_public_surface "system/config/connections.md"; then
    echo "  FAIL  positive control: absolute-never did not hold"
    _ps_fail=$((_ps_fail + 1))
  fi
  [ "$_ps_fail" -eq "$before_fail" ] && echo "  ok    positive control: absolute-never holds"

  if [ "$_ps_fail" -eq 0 ]; then
    echo "  ok    $((26)) checks passed"
  fi

  echo ""
  echo "Drift vs the published artifact"
  if ! git -C "$PS_ROOT" rev-parse --verify -q github/main >/dev/null 2>&1; then
    echo "  (no github/main ref — run: git fetch github main)"
  else
    local tmp_pub tmp_int
    tmp_pub="$(mktemp)"; tmp_int="$(mktemp)"
    git -C "$PS_ROOT" ls-tree -r --name-only github/main | sort > "$tmp_pub"
    ps_list_surface | sort > "$tmp_int"

    local would_add would_remove
    would_add=$(comm -13 "$tmp_pub" "$tmp_int" | grep -v '^$' || true)
    would_remove=$(comm -23 "$tmp_pub" "$tmp_int" | grep -v '^\.gitignore$' | grep -v '^$' || true)

    if [ -n "$would_add" ]; then
      echo "  + $(echo "$would_add" | wc -l | tr -d ' ') path(s) this config would ADD to the public repo:"
      echo "$would_add" | sed 's/^/      /' | head -20
    fi
    if [ -n "$would_remove" ]; then
      echo "  - $(echo "$would_remove" | wc -l | tr -d ' ') path(s) in the public repo this config does NOT intend:"
      echo "$would_remove" | sed 's/^/      /' | head -20
      echo "      (accumulation — the publish worktree never prunes. Decide: keep or prune.)"
    fi
    [ -z "$would_add" ] && [ -z "$would_remove" ] && echo "  ok    intent and artifact agree"
    rm -f "$tmp_pub" "$tmp_int"
  fi

  echo ""
  if [ "$_ps_fail" -gt 0 ]; then
    echo "FAILED — $_ps_fail unit check(s)"
    return 1
  fi
  echo "Unit checks green. Drift above is a decision, not a failure."
  return 0
}

if [ "${BASH_SOURCE[0]:-$0}" = "$0" ]; then
  case "${1:---self-test}" in
    --self-test) ps_self_test ;;
    --list)      ps_list_surface ;;
    --check)     if is_public_surface "${2:-}"; then echo "public"; else echo "private"; fi ;;
    --dirs)      ps_publish_dirs ;;
    --files)     ps_publish_files ;;
    *) echo "usage: $0 [--self-test|--list|--check PATH|--dirs|--files]" >&2; exit 2 ;;
  esac
fi
