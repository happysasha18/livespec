#!/usr/bin/env bash
# sync-skills.sh — the pack developer's freshness tool (SPEC E-23).
# Copies each repo skill over its installed copy and REPORTS every version change old -> new,
# so the A-7 re-read has its trigger line. The repo is the source (D-4); the installed copy
# is a mirror that must never run stale through a working session.
# Usage: scripts/sync-skills.sh [dest]   (default: ~/.claude/skills)

set -euo pipefail

REPO_SKILLS="$(cd "$(dirname "$0")/../skills" && pwd)"
DEST="${1:-$HOME/.claude/skills}"

mkdir -p "$DEST"

version_of() {
  # frontmatter form:  metadata:\n  version: X.Y.Z
  awk '/^  version: / { print $2; exit }' "$1" 2>/dev/null || true
}

changed=0
for skill_dir in "$REPO_SKILLS"/*/; do
  name="$(basename "$skill_dir")"
  src_v="$(version_of "$skill_dir/SKILL.md")"
  dst_v="$(version_of "$DEST/$name/SKILL.md")"
  if [ "$src_v" = "$dst_v" ] && ! [ "$skill_dir/SKILL.md" -nt "$DEST/$name/SKILL.md" ]; then
    echo "  $name — unchanged ($src_v)"
    continue
  fi
  mkdir -p "$DEST/$name"
  cp -r "$skill_dir"/. "$DEST/$name/"
  echo "  $name — synced: ${dst_v:-absent} -> $src_v   (A-7: RE-READ this skill before continuing)"
  changed=$((changed + 1))
done

if [ "$changed" -eq 0 ]; then
  echo "sync-skills: everything fresh."
else
  echo "sync-skills: $changed skill(s) updated — journal the old -> new line (A-7)."
fi
