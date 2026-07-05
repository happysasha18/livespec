#!/usr/bin/env bash
# guardrails/install.sh — installs the pre-commit and pre-push hooks from this folder
# into the current repo's .git/hooks/. Idempotent: re-running just overwrites with
# whatever is currently in guardrails/, no duplication and no error if already installed.
#
# This does NOT arm the concurrent-edit fence — that stays opt-in
# (see guardrails/fence-refresh.sh and guardrails/README.md).

set -euo pipefail

GUARDRAILS_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(git -C "$GUARDRAILS_DIR" rev-parse --show-toplevel)"
HOOKS_DIR="$REPO_ROOT/.git/hooks"

if [ ! -d "$HOOKS_DIR" ]; then
  echo "No .git/hooks directory found at $HOOKS_DIR — is $REPO_ROOT a git repo?"
  exit 1
fi

for hook in pre-commit pre-push; do
  cp "$GUARDRAILS_DIR/$hook" "$HOOKS_DIR/$hook"
  chmod +x "$HOOKS_DIR/$hook"
  echo "Installed $hook -> $HOOKS_DIR/$hook"
done

echo "Done. The fence (pre-commit) stays OFF until a session runs guardrails/fence-refresh.sh."
