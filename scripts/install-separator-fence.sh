#!/bin/sh
# One-shot installer: a PreToolUse(Bash) hook that blocks a bare `===` separator in the
# agent's own shell commands (zsh eats it: "=== not found"; the standing separator is `---`).
# Backward compatible by design: quoted "===" is legal zsh and passes; heredoc bodies
# (file CONTENT written via `cat <<EOF`) are not shell words and are excluded from the scan.
# Ledger home: ~/live-spec/.live-spec/PROBLEMS.md (zsh-separator entry).
# Run once:  ! sh ~/live-spec/scripts/install-separator-fence.sh
set -e

mkdir -p "$HOME/.claude/hooks"
cat > "$HOME/.claude/hooks/block-triple-equals.sh" <<'EOF'
#!/bin/sh
# PreToolUse(Bash) guard: a bare === separator dies in zsh ("=== not found"); use --- instead.
# Scans only real shell words: text before any heredoc (<<) is checked; heredoc bodies are data.
cmd=$(jq -r '.tool_input.command // ""')
scan=$(printf '%s\n' "$cmd" | awk 'i=index($0,"<<"){print substr($0,1,i-1); exit} {print}')
# here-string, never a pipe: the pipefail/SIGPIPE false verdict on a large $scan (the muted-launch
# checker's 2026-07-17 CI red, same class)
if grep -qE '(^|[[:space:]])={3,}([[:space:]]|;|$)' <<< "$scan"; then
  printf '%s' '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"bare === separator in the command - zsh eats it (=== not found); draw separators with --- instead"}}'
fi
exit 0
EOF
chmod +x "$HOME/.claude/hooks/block-triple-equals.sh"

python3 - <<'PY'
import json, pathlib
p = pathlib.Path.home() / ".claude" / "settings.json"
s = json.loads(p.read_text())
pre = s.setdefault("hooks", {}).setdefault("PreToolUse", [])
cmd = "sh ~/.claude/hooks/block-triple-equals.sh"
if not any(h.get("command") == cmd
           for entry in pre for h in entry.get("hooks", [])):
    pre.append({"matcher": "Bash",
                "hooks": [{"type": "command", "command": cmd}]})
    p.write_text(json.dumps(s, indent=2, ensure_ascii=False) + "\n")
    print("hook installed into ~/.claude/settings.json")
else:
    print("hook already present - nothing changed")
PY

# self-tests: fire on a bare separator; stay silent on quoted and heredoc forms
fire=$(printf '%s' '{"tool_name":"Bash","tool_input":{"command":"echo === boom"}}' \
       | sh "$HOME/.claude/hooks/block-triple-equals.sh")
quiet1=$(printf '%s' '{"tool_name":"Bash","tool_input":{"command":"echo \"===\""}}' \
       | sh "$HOME/.claude/hooks/block-triple-equals.sh")
quiet2=$(printf '%s' '{"tool_name":"Bash","tool_input":{"command":"cat <<X\n===\nX"}}' \
       | sh "$HOME/.claude/hooks/block-triple-equals.sh")
case "$fire" in *deny*) : ;; *) echo "self-test FAILED: bare === not blocked"; exit 1;; esac
[ -z "$quiet1" ] || { echo "self-test FAILED: quoted === wrongly blocked"; exit 1; }
[ -z "$quiet2" ] || { echo "self-test FAILED: heredoc body wrongly blocked"; exit 1; }
echo "self-tests OK: bare === blocked; quoted and heredoc forms pass"
