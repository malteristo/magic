#!/bin/bash
# listener_audit.sh — What is this machine serving, and did we mean to?
#
# The practice's threat model covers what leaves via `git push`. This covers
# what leaves via a socket. Every non-loopback TCP listener is compared against
# the declared allowlist; anything undeclared is reported.
#
# Takes a target, because a checker that only examines the machine it runs on
# protects that machine and reports clean everywhere else.
#
# Usage:
#   ./scripts/listener_audit.sh                      # scope 'local', this machine
#   ./scripts/listener_audit.sh mini <ssh-target>    # scope 'mini', over SSH (read-only)
#   ./scripts/listener_audit.sh --self-test          # positive control
#
# Allowlist: system/config/declared_listeners.txt
# Addresses belong in system/config/connections.md, never here.

set -uo pipefail

RED=$'\033[0;31m'; YEL=$'\033[0;33m'; GRN=$'\033[0;32m'; DIM=$'\033[2m'; OFF=$'\033[0m'

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Same resolution chain as the name list and the exceptions list — one shape
# for every list this practice keeps out of the public tree. The template is
# deliberately NOT in the chain: it declares only macOS built-ins, so falling
# back to it would quietly turn a missing allowlist into a working audit that
# flags every real service, and the noise would be read as the check being
# broken rather than unconfigured.
ALLOWLIST=""
for candidate in \
  "${MAGIC_LISTENER_ALLOWLIST:-}" \
  "$(git config --get magic.declaredListeners 2>/dev/null || true)" \
  "$ROOT/system/config/declared_listeners.txt" \
  "$ROOT/.declared_listeners.txt"
do
  if [ -n "$candidate" ] && [ -f "$candidate" ]; then ALLOWLIST="$candidate"; break; fi
done
: "${ALLOWLIST:=$ROOT/system/config/declared_listeners.txt}"   # for the error message

# Apple services whose ports are ephemeral and change every boot — matched by
# process name because there is no stable number to declare.
SYSTEM_PROCS="rapportd|sharingd|remoted"

usage() { sed -n '2,20p' "$0"; exit "${1:-0}"; }

SELF_TEST=false
case "${1:-}" in
  -h|--help) usage 0 ;;
  --self-test) SELF_TEST=true ;;
esac

SCOPE="${1:-local}"
SSH_TARGET="${2:-}"
[ "$SELF_TEST" = true ] && { SCOPE="local"; SSH_TARGET=""; }

# --- the allowlist must be present and non-empty, and say so ---------------
if [ ! -f "$ALLOWLIST" ]; then
  echo "${RED}No allowlist found — this audit has nothing to compare against.${OFF}" >&2
  echo "${RED}Refusing to report. This is a failure, not a clean run.${OFF}" >&2
  echo "${YEL}  cp ${ALLOWLIST#"$ROOT"/}.template ${ALLOWLIST#"$ROOT"/}${OFF}" >&2
  exit 2
fi

declared=$(grep -vE '^\s*(#|$)' "$ALLOWLIST" | awk '{print $1}' | grep -E '^[a-z]+:[0-9]+$' | sort -u)
declared_count=$(printf '%s\n' "$declared" | grep -c . || true)
if [ "$declared_count" -eq 0 ]; then
  echo "${RED}Allowlist $ALLOWLIST parsed to 0 entries — malformed. Refusing to report.${OFF}" >&2
  exit 2
fi

# --- collect listeners -----------------------------------------------------
LSOF_CMD='lsof -nP -iTCP -sTCP:LISTEN 2>/dev/null'

if [ -n "$SSH_TARGET" ]; then
  raw=$(ssh -o ConnectTimeout=8 -o BatchMode=yes "$SSH_TARGET" "$LSOF_CMD")
  rc=$?
  if [ $rc -ne 0 ] && [ -z "$raw" ]; then
    echo "${RED}Could not reach $SCOPE over SSH (exit $rc) — scope NOT audited.${OFF}" >&2
    echo "${RED}Unreachable is not clean.${OFF}" >&2
    exit 2
  fi
else
  raw=$(eval "$LSOF_CMD")
fi

# lsof prints a header even with no rows; a truly empty result means the
# instrument failed, not that nothing is listening.
if [ -z "$raw" ]; then
  echo "${RED}lsof returned nothing at all on '$SCOPE' — instrument failure, not a clean result.${OFF}" >&2
  exit 2
fi

# Rows: keep listeners NOT bound solely to loopback. Emit "proc port".
observed=$(printf '%s\n' "$raw" | awk '
  NR == 1 { next }
  $9 ~ /^127\.0\.0\.1:/ { next }
  $9 ~ /^\[::1\]:/      { next }
  {
    n = split($9, a, ":")
    port = a[n]
    if (port ~ /^[0-9]+$/) print $1, port
  }' | sort -u)

total_rows=$(printf '%s\n' "$raw" | grep -c LISTEN || true)
observed_count=$(printf '%s\n' "$observed" | grep -c . || true)

# --- compare ---------------------------------------------------------------
undeclared=""
while read -r proc port; do
  [ -z "${port:-}" ] && continue
  if printf '%s\n' "$proc" | grep -qE "^($SYSTEM_PROCS)"; then continue; fi
  if printf '%s\n' "$declared" | grep -qx "$SCOPE:$port"; then continue; fi
  undeclared+="    $proc  port $port"$'\n'
done <<< "$observed"

# --- report — always state what was examined -------------------------------
echo "Listener audit — scope '${SCOPE}'${SSH_TARGET:+ (remote)}"
echo "${DIM}  examined ${total_rows} listening socket(s), ${observed_count} non-loopback binding(s), against ${declared_count} declared entr(ies)${OFF}"

if [ -n "$undeclared" ]; then
  echo "${RED}[UNDECLARED] listening on a non-loopback address and named in no allowlist:${OFF}"
  printf '%s' "$undeclared"
  echo "${YEL}  Each is reachable by anything that can route to this machine.${OFF}"
  echo "${YEL}  Close it, bind it to 127.0.0.1, or declare it in ${ALLOWLIST#"$ROOT"/} with a reason.${OFF}"
  status=1
else
  echo "${GRN}  All non-loopback listeners are declared.${OFF}"
  status=0
fi

# --- positive control ------------------------------------------------------
# A guard that has never been seen to fire is not known to work. This class of
# defect reports success, so a clean result is not evidence until the
# instrument has proved it can still see.
if [ "$SELF_TEST" = true ]; then
  echo
  # A port already in use would let the control pass (or fail) on someone
  # else's socket. Refuse rather than test the wrong thing.
  if lsof -nP -iTCP:8421 -sTCP:LISTEN >/dev/null 2>&1; then
    echo "${YEL}  INCONCLUSIVE — port 8421 is already in use; the control needs it free.${OFF}"
    exit 2
  fi

  echo "Positive control — planting an undeclared listener on port 8421…"
  python3 -c "
import socket, time
s = socket.socket(); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8421)); s.listen(1)
time.sleep(20)
" >/dev/null 2>&1 &
  plant=$!

  # Wait for the plant to actually bind. Without this the control tests a port
  # nothing is on and reports the guard blind when the guard is fine — a false
  # FAIL costs exactly as much trust as a false PASS.
  #
  # Poll for THIS process's socket (-a -p "$plant"), not for "something on
  # 8421". A dying listener from a previous run satisfies the looser check,
  # and the control then probes before the real plant is up. That is this
  # script's own subject matter turned on itself: the check named the port
  # instead of the thing, and passed while measuring the wrong object.
  bound=false
  for _ in $(seq 1 40); do
    if lsof -nP -iTCP:8421 -sTCP:LISTEN -a -p "$plant" >/dev/null 2>&1; then bound=true; break; fi
    kill -0 "$plant" 2>/dev/null || break   # plant died — stop waiting
    sleep 0.25
  done

  if [ "$bound" != true ]; then
    echo "${YEL}  INCONCLUSIVE — the planted listener never came up.${OFF}"
    echo "${YEL}  The guard was not exercised; this is not a pass and not a failure.${OFF}"
    kill "$plant" 2>/dev/null; wait "$plant" 2>/dev/null
    exit 2
  fi

  # Capture rather than discard: a nested run that dies early prints nothing to
  # stdout, which is indistinguishable from a guard that looked and saw nothing.
  probe=$(MAGIC_LISTENER_ALLOWLIST="$ALLOWLIST" "$0" local 2>&1)
  if printf '%s' "$probe" | grep -q "port 8421"; then
    echo "${GRN}  PASS — the audit saw the planted listener.${OFF}"
    ctl=0
  else
    echo "${RED}  FAIL — the audit did NOT see a listener on 0.0.0.0:8421.${OFF}"
    echo "${RED}  Every clean run from this instrument is now unevidenced.${OFF}"
    echo "${DIM}  What the nested audit actually printed:${OFF}"
    printf '%s\n' "$probe" | sed 's/^/    | /'
    ctl=1
  fi
  kill "$plant" 2>/dev/null; wait "$plant" 2>/dev/null
  exit $ctl
fi

exit $status
