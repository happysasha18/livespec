#!/bin/sh
# One-shot installer: a PreToolUse(Bash) hook that blocks a bare `===` separator in the
# agent's own shell commands (zsh eats it: "=== not found"; the standing separator is `---`).
# Ledger home: ~/live-spec/.live-spec/PROBLEMS.md (zsh-separator entry). Run once, by the human:
#   ! sh ~/live-spec/scripts/install-separator-fence.sh
set -e

mkdir -p "$HOME/.claude/hooks"
cat > "$HOME/.claude/hooks/block-triple-equals.sh" <<'EOF'
#!/bin/sh
# PreToolUse(Bash) guard: a bare === separator dies in zsh ("=== not found"); use --- instead.
cmd=$(jq -r '.tool_input.command // ""')
if printf '%s' "$cmd" | grep -qE '(^|[[:space:]])={3,}([[:space:]]|;|$)'; then
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

# self-test: the guard must fire on a synthetic payload
out=$(printf '%s' '{"tool_name":"Bash","tool_input":{"command":"echo === boom"}}' \
      | sh "$HOME/.claude/hooks/block-triple-equals.sh")
case "$out" in
  *deny*) echo "self-test OK: bare === is blocked" ;;
  *) echo "self-test FAILED: guard did not fire" ; exit 1 ;;
esac
