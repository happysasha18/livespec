#!/usr/bin/env bash
# fence-refresh.sh — (re-)arms the concurrent-edit fence (SPEC INV-11) at the current
# HEAD. Run this to opt in to the fence, or after reviewing what another writer
# changed so the fence tracks the repo again.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
sha="$(git -C "$REPO_ROOT" rev-parse HEAD)"
echo "$sha" > "$REPO_ROOT/.live-spec-fence"
echo "Fence armed: recorded HEAD $sha into $REPO_ROOT/.live-spec-fence"
