#!/bin/sh
# Installs the two session hooks on THIS machine (rows 134 + 141): the wall-clock
# injection (clock-hook.sh, SPEC INV-24's mechanical hand) and the chat-laws
# reminder (chat-law-hook.sh, SPEC INV-28/INV-35's voice). Copies both under
# ~/.claude/hooks and wires UserPromptSubmit entries in ~/.claude/settings.json.
# Run BY THE HUMAN — the agent's own hand is blocked from self-config by the
# harness classifier, deliberately. Idempotent: re-running changes nothing.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$HOME/.claude/hooks"
cp "$DIR/clock-hook.sh" "$DIR/chat-law-hook.sh" "$HOME/.claude/hooks/"
chmod +x "$HOME/.claude/hooks/clock-hook.sh" "$HOME/.claude/hooks/chat-law-hook.sh"
python3 - << 'PYEOF'
import json, os
p = os.path.expanduser("~/.claude/settings.json")
s = json.load(open(p)) if os.path.exists(p) else {}
ups = s.setdefault("hooks", {}).setdefault("UserPromptSubmit", [])
have = [hk.get("command", "") for e in ups for hk in e.get("hooks", [])]
for name in ("clock-hook.sh", "chat-law-hook.sh"):
    if not any(name in c for c in have):
        ups.append({"hooks": [{"type": "command",
                               "command": "sh ~/.claude/hooks/%s" % name}]})
json.dump(s, open(p, "w"), indent=2, ensure_ascii=False)
print("UserPromptSubmit hooks now wired:")
for e in ups:
    for hk in e.get("hooks", []):
        print("  " + hk.get("command", "?"))
PYEOF
echo "Installed. Every window's next prompt carries the wall clock + the chat laws."
