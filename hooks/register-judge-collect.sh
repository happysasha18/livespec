#!/bin/sh
# The judge's asynchronous half (ROADMAP row 416; the owner's word 2026-07-17 ~16:39, choosing the
# asynchronous road over a 33-second wait per reply).
#
# The judge reads meaning, so it costs a model call, and the call costs ~33s — almost all of it the
# harness's own process start rather than the model's thinking (probed: the flag that skips the start
# breaks the login). Waiting for it at the end of every turn would tax the human 33 seconds per reply
# to fix a sentence he has already read, and a tax that size gets a guard torn out.
#
# So the cost is moved off the waiting path entirely. This script is the Stop arm: it hands the turn's
# last message to the judge in the BACKGROUND and returns at once, blocking nothing. The verdict lands
# in a file. The UserPromptSubmit arm (register-judge-report.sh) reads that file at the human's next
# message and puts the finding in front of the model, which sends the correction then.
#
# The trade this makes, stated plainly because the human asked and it is his to know: the offending
# message reaches him uncorrected, and the correction follows one turn later. A sent message cannot be
# recalled or edited — the harness offers no such act — so one turn is the floor for any judge that
# reads meaning.
#
# Repo home: hooks/register-judge-collect.sh; installed copy: ~/.claude/hooks/.
PAYLOAD=$(cat)
VERDICT_DIR="${HOME}/.claude/hooks/.judge"
mkdir -p "$VERDICT_DIR"

# One verdict slot per session: a second turn's judgment replaces an unread first, since the newer
# message is the one the human is reading and a queue of stale verdicts would report the wrong text.
SESSION=$(printf '%s' "$PAYLOAD" | python3 -c 'import json,sys;print((json.load(sys.stdin) or {}).get("session_id","unknown"))' 2>/dev/null || echo unknown)

printf '%s' "$PAYLOAD" | REGISTER_JUDGE_TIMEOUT=120 nohup python3 "${HOME}/.claude/hooks/register-judge.py" \
    > "${VERDICT_DIR}/${SESSION}.json.part" 2> "${VERDICT_DIR}/${SESSION}.err" < /dev/stdin &
# Rename on completion so the reader never reads a half-written verdict.
{
    wait $! 2>/dev/null
    if [ -s "${VERDICT_DIR}/${SESSION}.json.part" ]; then
        mv "${VERDICT_DIR}/${SESSION}.json.part" "${VERDICT_DIR}/${SESSION}.json"
    else
        rm -f "${VERDICT_DIR}/${SESSION}.json.part"
    fi
} > /dev/null 2>&1 &

exit 0
