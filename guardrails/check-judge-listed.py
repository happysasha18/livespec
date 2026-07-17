#!/usr/bin/env python3
"""check-judge-listed.py — the chat judges stay wired in settings.json (SPEC INV-211, gate v).

config-health (gate m) proves an installed hook FILE matches its source, and its docstring hands
this residual to the row 420 audit by name: it does not prove settings.json still LISTS the judge
entries. A judge whose file is present and correct still never runs when its settings.json entry
is gone — the run comes from the entry, not the file. That is the no-verdict failure this movement
hit: an LLM gate that silently did nothing while every other gate stayed green.

This check reads the wired-hook declaration (guardrails/judge-hooks.json), asserts every hook
under hooks/ is classified there (wired to a settings.json event surface, or named a library file
another hook invokes), and asserts each wired hook is referenced in its surface's hook array in the
installed ~/.claude/settings.json. A wired hook missing from its array reds, naming the hook, the
surface, and the fix. settings.json is personal-layer, so where it cannot be read (a CI checkout, a
host without it) the gate stands down by name and never falsely passes — exactly as config-health
skips a CI checkout.
"""
import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_json(path):
    with open(path) as f:
        return json.load(f)


def main():
    decl_path = os.environ.get(
        "JUDGE_HOOKS_JSON", os.path.join(REPO_ROOT, "guardrails", "judge-hooks.json"))
    settings_path = os.environ.get(
        "JUDGE_SETTINGS_JSON", os.path.join(os.path.expanduser("~"), ".claude", "settings.json"))
    hooks_dir = os.environ.get("JUDGE_HOOKS_DIR", os.path.join(REPO_ROOT, "hooks"))

    decl = load_json(decl_path)
    wired = decl.get("wired", {})           # stem -> settings.json surface
    library = set(decl.get("library", []))  # stems invoked by another hook, not listed directly

    fail = 0

    # Self-widening honesty: every source hook is classified, so a hook added later cannot go
    # unclassified and silently escape the wiring check (the shape config-health already uses).
    if os.path.isdir(hooks_dir):
        for name in sorted(os.listdir(hooks_dir)):
            p = os.path.join(hooks_dir, name)
            if not os.path.isfile(p):
                continue
            stem = os.path.splitext(name)[0]
            if stem not in wired and stem not in library:
                print("judge-listed: hooks/%s is not classified in judge-hooks.json — add it to "
                      "\"wired\" with its settings.json surface, or to \"library\"." % name)
                fail = 1

    # settings.json is personal-layer: stand down by name where it cannot be read. The
    # honesty finding above (a repo-level fact) still stands; only the wiring check stands down.
    if not os.path.isfile(settings_path):
        print("judge-listed: no settings.json at %s — the wiring check stands down by name "
              "(personal-layer file, absent on a CI checkout or a host without it)." % settings_path)
        return fail
    try:
        settings = load_json(settings_path)
    except (ValueError, OSError) as e:
        print("judge-listed: settings.json at %s is unreadable (%s) — the wiring check stands "
              "down by name." % (settings_path, e))
        return fail

    hooks = settings.get("hooks", {})

    def commands_for(surface):
        out = []
        for group in hooks.get(surface, []):
            for h in group.get("hooks", []):
                cmd = h.get("command", "")
                if cmd:
                    out.append(cmd)
        return out

    for stem, surface in sorted(wired.items()):
        cmds = commands_for(surface)
        if not any(stem in c for c in cmds):
            print("judge-listed: hook '%s' is declared wired to the %s surface but no %s entry in "
                  "%s references it — the judge is dark though its file is present. Fix: add its "
                  "command to the %s hook array (run scripts/install-session-hooks.sh)."
                  % (stem, surface, surface, settings_path, surface))
            fail = 1

    if fail == 0:
        print("judge-listed: OK (every wired judge is referenced in its settings.json surface).")
    return fail


if __name__ == "__main__":
    sys.exit(main())
