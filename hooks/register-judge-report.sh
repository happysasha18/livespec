#!/bin/sh
# The judge's reading half (ROADMAP row 416). Runs on UserPromptSubmit, beside the clock and the chat
# laws. It reads the verdict the Stop arm left in the background and puts it in front of the model at
# the moment a reply is about to be written, which is the moment the correction can be sent.
#
# It costs nothing to wait for: the judging already happened while the human was reading and typing.
#
# A verdict is consumed once and deleted. An unread verdict from an older turn is stale by the time a
# newer one lands, and the collect arm overwrites rather than queues, so what this reads is always the
# judgment of the last thing the human was actually shown.
#
# Repo home: hooks/register-judge-report.sh; installed copy: ~/.claude/hooks/.
PAYLOAD=$(cat)
VERDICT_DIR="${HOME}/.claude/hooks/.judge"
SESSION=$(printf '%s' "$PAYLOAD" | python3 -c 'import json,sys;print((json.load(sys.stdin) or {}).get("session_id","unknown"))' 2>/dev/null || echo unknown)
VERDICT="${VERDICT_DIR}/${SESSION}.json"

[ -f "$VERDICT" ] || exit 0

python3 - "$VERDICT" <<'PY'
import json, os, sys
path = sys.argv[1]
try:
    with open(path) as fh:
        verdict = json.load(fh)
except (OSError, ValueError):
    os.unlink(path) if os.path.exists(path) else None
    sys.exit(0)
os.unlink(path)
reason = verdict.get("reason", "").strip()
if reason:
    print(reason.replace("REGISTER JUDGE —", "REGISTER JUDGE (on your PREVIOUS reply, judged while you waited) —"))
PY
exit 0
