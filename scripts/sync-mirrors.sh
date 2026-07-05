#!/usr/bin/env bash
# sync-mirrors.sh
#
# What this does, in plain English:
#
# The live-spec pack (this repo) is the single source of truth for every skill
# under skills/<name>/. Some of those skills ALSO exist as their own separate
# public GitHub repos (e.g. happysasha18/product-prover), kept around so people
# who only want one skill don't have to clone the whole pack. Those standalone
# repos are READ-ONLY MIRRORS — nobody should edit them directly, and this
# script is the one thing that updates them.
#
# For every skill folder in skills/:
#   1. Look for a GitHub repo named happysasha18/<skill-name>.
#      - If it doesn't exist, we do NOT create one (that's a deliberate,
#        separate decision the project owner makes) — we just print that we
#        skipped it and move on.
#   2. If it exists, clone it into a scratch directory, replace its contents
#      with the current skills/<skill-name>/ folder from the pack (keeping the
#      mirror's own .git history), make sure its README.md opens with a banner
#      explaining it's a read-only mirror, and if anything actually changed,
#      commit and push that to the mirror repo.
#   3. If nothing changed, we say "up to date" and don't make an empty commit.
#
# This script only ever pushes to the STANDALONE MIRROR repos, never to the
# pack repo itself — the pack's own push is a separate, human-gated step.
#
# Usage:
#   ./scripts/sync-mirrors.sh
#
# Requires: git, rsync, and the GitHub CLI (`gh`), already authenticated.

set -euo pipefail

# Resolve the pack root (this script lives in <pack>/scripts/).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACK_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_DIR="$PACK_ROOT/skills"
GITHUB_OWNER="happysasha18"

PACK_VERSION="$(cat "$PACK_ROOT/VERSION" 2>/dev/null || echo "unknown")"
PACK_SHA="$(git -C "$PACK_ROOT" rev-parse --short HEAD)"

# The banner leads with WHAT THIS IS (a stranger from a directory reads that first),
# then the read-only notice (promoter inbox wish, 2026-07-05).
banner_for() {
  local skill_name="$1"
  echo "**${skill_name}** — one skill from the [live-spec pack](https://github.com/${GITHUB_OWNER}/live-spec), installable on its own. Read-only mirror: do not open PRs here; changes land in the pack and are synced by scripts/sync-mirrors.sh."
}

# One status line per skill, collected here and printed again at the end as a summary.
declare -a SUMMARY_LINES=()

# Pull a short description out of a SKILL.md's YAML frontmatter "description:" field.
# Used only as a fallback when a mirror has no README.md of its own.
extract_skill_description() {
  local skill_md="$1"
  awk '
    /^---[[:space:]]*$/ { fence++; next }
    fence == 1 && /^description:[[:space:]]*/ {
      sub(/^description:[[:space:]]*/, "");
      gsub(/^"|"$/, "");
      print;
      exit
    }
  ' "$skill_md"
}

for skill_path in "$SKILLS_DIR"/*/; do
  [ -d "$skill_path" ] || continue
  skill_name="$(basename "$skill_path")"
  repo="${GITHUB_OWNER}/${skill_name}"

  echo "== ${skill_name} =="

  # Does a standalone mirror repo exist for this skill? We never create one here.
  if ! gh repo view "$repo" >/dev/null 2>&1; then
    echo "${skill_name}: skipped (no mirror repo yet)"
    SUMMARY_LINES+=("${skill_name}: skipped (no mirror repo yet)")
    continue
  fi

  work_dir="$(mktemp -d)"
  trap 'rm -rf "$work_dir"' EXIT

  echo "cloning ${repo} into scratch dir..."
  gh repo clone "$repo" "$work_dir/mirror" -- -q

  mirror_dir="$work_dir/mirror"

  # Replace the mirror's content with the pack's copy of this skill, but keep
  # the mirror's own .git history (that's how it stays a real, pushable repo).
  rsync -a --delete --exclude='.git' "$skill_path" "$mirror_dir/"

  # Make sure README.md starts with the what-this-is + read-only banner.
  BANNER="$(banner_for "$skill_name")"
  readme="$mirror_dir/README.md"
  if [ -f "$readme" ] && head -1 "$readme" | grep -q "Read-only mirror"; then
    # a banner (old or new wording) is there — rewrite line 1 to the current wording
    tmp_readme="$(mktemp)"
    { echo "$BANNER"; tail -n +2 "$readme"; } > "$tmp_readme"
    mv "$tmp_readme" "$readme"
  elif [ -f "$readme" ]; then
    # Skill has its own README — keep it, just prepend the banner above it.
    tmp_readme="$(mktemp)"
    {
      echo "$BANNER"
      echo
      cat "$readme"
    } > "$tmp_readme"
    mv "$tmp_readme" "$readme"
  else
    # No README shipped with the skill — write banner + a short description
    # pulled from the SKILL.md frontmatter.
    desc="$(extract_skill_description "$mirror_dir/SKILL.md" 2>/dev/null || true)"
    {
      echo "$BANNER"
      echo
      if [ -n "$desc" ]; then
        echo "# ${skill_name}"
        echo
        echo "$desc"
      else
        echo "# ${skill_name}"
      fi
    } > "$readme"
  fi

  # Anything to commit?
  ( cd "$mirror_dir" && git add -A )
  if ( cd "$mirror_dir" && git diff --cached --quiet ); then
    echo "${skill_name}: up to date"
    SUMMARY_LINES+=("${skill_name}: up to date")
  else
    commit_msg="sync from live-spec pack ${PACK_VERSION} (${PACK_SHA})"
    ( cd "$mirror_dir" && git commit -q -m "$commit_msg" )
    ( cd "$mirror_dir" && git push -q )
    echo "${skill_name}: updated"
    SUMMARY_LINES+=("${skill_name}: updated")
  fi

  rm -rf "$work_dir"
  trap - EXIT
done

echo
echo "== summary =="
for line in "${SUMMARY_LINES[@]}"; do
  echo "$line"
done
