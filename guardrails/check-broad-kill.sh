#!/usr/bin/env bash
# check-broad-kill.sh — SPEC INV-162 (ROADMAP 334, inverted 417): a cleanup ends only what THIS RUN
# provably owns, identified by a recorded PID, the process group the run itself holds, or a path under
# the run's own tree. A guard that recognised a cleanup by a process NAME could never tell this run's
# copy of a program from the person's copy — that is the defect that once closed the owner's REAL
# browser mid-session (a broad `pkill chrome` / `pkill chrome_crashpad_handler`), destroying work state
# outside git, the effect base rule 17 forbids. So this gate DENIES every ending that names a NAME, and
# accepts an ending that proves what it owns. The four browser words that used to BE the check are now
# only this comment's example — the check itself never asks which programs matter, it asks whether the
# command can prove what it is ending.
#
# Usage: check-broad-kill.sh [path]
#   no arg  — scan the repo's tracked executable surfaces (default, the push gate)
#   path    — scan one file or directory (used by the guardrail's own test)
#
# What it flags: a line whose comment-stripped code ENDS a process by NAME —
#   * `pkill` or `killall`, which target a process by name/pattern by construction; or
#   * `kill` fed by a name-to-pid resolver (`pgrep` / `pidof`), the same danger wearing kill's clothes
#     (`kill $(pgrep chrome)`, `pgrep chrome | xargs kill`).
# An ending that PROVES what it owns passes quiet: `kill $pid` / `kill 48213` / `os.killpg($pgid,...)`
# name a PID or a process group directly and are never name-based; and a kill scoped to an install /
# profile PATH under the run's own tree (`~/.cache/puppeteer/...`, a `--user-data-dir`) is exempt
# because the path is unique to this run. The path scope is read from the CODE after comments are
# stripped, so a path sitting only in a comment cannot launder a broad kill (the founding-incident
# bypass). This says nothing about which programs matter — Safari, Slack, node, and chrome all red the
# same when ended by name, because none of them proves ownership. Portable across GNU and BSD grep.
# Prose surfaces (spec, ROADMAP, inbox, this checker, its own tests, the probe corpus) legitimately
# NAME the patterns to forbid or exercise them and are excluded from the repo scan.
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

# the install-path / profile scope that makes an ending's target UNIQUE to this run (a legal form).
# Applied AFTER comments are stripped, so a path in the actual argument exempts the ending while a path
# sitting only in a comment cannot.
SCOPED='\.cache/puppeteer|user-data-dir'

scan_file() {
  # Read the comment-stripped code and print `file:line: code` for each line that ends a process by
  # NAME without an owned-path proof. `pkill`/`killall` are name-based by construction; `kill` becomes
  # name-based when a `pgrep`/`pidof` on the same line resolves its target. A `kill`/`killpg` fed a PID
  # or a process group directly is not name-based and never reaches the flag. The whole classification
  # runs in awk so the kill-plus-resolver case (two tokens on one line) is judged as one unit.
  awk -v F="$1" '
    BEGIN {
      # regexes held as strings so a "/" inside a character class does not close an awk /literal/.
      NAMEKILL = "(^|[^/a-zA-Z._])(pkill|killall)([^a-zA-Z]|$)"   # pkill/killall: name-based by design
      RESOLVER = "(^|[^a-zA-Z._])(pgrep|pidof)([^a-zA-Z]|$)"      # a name-to-pid lookup
      KILL     = "(^|[^a-zA-Z._])kill([^a-zA-Z]|$)"              # the kill verb as a word (not killpg)
      SCOPED   = "\\.cache/puppeteer|user-data-dir"              # an owned-path scope, unique to the run
    }
    {
      l = $0; sub(/#.*/, "", l)                      # strip a trailing comment, judge the code only
      name_kill = (l ~ NAMEKILL)
      kill_by_lookup = ((l ~ RESOLVER) && ((l ~ KILL) || name_kill))
      if (!(name_kill || kill_by_lookup)) next       # not a name-based ending — an owned PID/pgroup kill
      if (l ~ SCOPED) next                            # scoped to a path under the run own tree — owned
      printf "%s:%d: %s\n", F, NR, l
    }' "$1" 2>/dev/null || true
}

hits=""
target="${1:-}"

if [ -n "$target" ]; then
  if [ -d "$target" ]; then
    while IFS= read -r f; do hits="$hits$(scan_file "$f")"$'\n'; done \
      < <(find "$target" -type f \( -name '*.sh' -o -name '*.py' -o -name '*.js' \
            -o -name '*.ts' -o -name '*.mjs' -o -name '*.cjs' -o -name '*.txt' -o -name '*.md' \))
  else
    hits="$(scan_file "$target")"
  fi
else
  cd "$REPO_ROOT"
  while IFS= read -r f; do
    # tests and the checker itself legitimately NAME / exercise the patterns; prose (.md) is not code.
    case "$f" in
      tests/*) continue ;;
      guardrails/check-broad-kill.sh) continue ;;
      guardrails/check-cleanup-notice.sh) continue ;;  # names the kill verbs to detect an ending
      *.md) continue ;;
    esac
    hits="$hits$(scan_file "$f")"$'\n'
  done < <(git ls-files '*.sh' '*.py' '*.js' '*.ts' '*.mjs' '*.cjs' 'scripts/*' 2>/dev/null)
fi

hits="$(printf '%s' "$hits" | grep -vE '^[[:space:]]*$' || true)"

if [ -n "$hits" ]; then
  echo "FAIL (broad-kill): a cleanup ends a process by NAME, with no PID / process-group / owned-path"
  echo "proof of what it owns (SPEC INV-162):"
  printf '%s\n' "$hits" | sed 's/^/  /'
  echo "  Fix: end only what THIS run provably owns — a recorded PID (kill \$pid), the process group the"
  echo "  run holds (os.killpg(\$pgid, ...)), or an install path under the run's own tree"
  echo "  (~/.cache/puppeteer/..., a --user-data-dir). A name pattern (pkill/killall chrome, Chrome,"
  echo "  crashpad, puppeteer — or Safari, Slack, node) cannot tell this run's copy of a program from"
  echo "  the human's own, which is how a broad kill once closed the human's real browser (row 334,"
  echo "  base rule 17)."
  exit 1
fi

echo "OK (broad-kill): no cleanup ends a process by a bare name pattern (INV-162)."
exit 0
