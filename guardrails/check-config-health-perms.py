#!/usr/bin/env python3
"""check-config-health-perms.py — a permission rule that points at nothing is a dead rule (SPEC INV-216).

The arm of config-health (gate m) that reads the settings the harness actually enforces. The worked
instance, found on the owner's report (2026-07-17 ~15:29) that the harness "sometimes" refuses a push
or a deploy: three deploy permissions named ~/tlvphoto, and the tree was renamed to ~/tlvphotos on
2026-07-10, so for a week every deploy fell through to a prompt while the rules sat there looking
correct — a stale allow rule fails exactly like a missing one, and no one could see it.

So this arm resolves every filesystem path named inside a permission rule and reds a rule whose path
is absent: a rename anywhere on the machine then reds at the next gate rather than degrading silently
into prompts. It reports the count of rules it resolved, so a rule shape it cannot parse is NAMED
rather than silently skipped (row 384's law — a check that looked at nothing is not a pass).

Personal-layer: the permissions live in ~/.claude/settings.json plus the host's project settings, so
the arm runs where those settings exist and stands down HONESTLY by name where it cannot read them —
an absent file is a legitimate stand-down, a present-but-unreadable file reds (never a false pass),
the same shape as the config-health hook checks. A single settings file to scan can be named through
CONFIG_HEALTH_PERMS_SETTINGS, which isolates a fixture from the real personal settings.
"""
import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# A permission rule wraps its command in Tool(...) — Bash(...), Edit(...), Read(...), Write(...).
_TOOL_WRAP = re.compile(r"^[A-Za-z]+\((.*)\)$", re.DOTALL)
# A trailing glob argument the harness uses for "any tail" — " *", " :*", ":*" — carries no path.
_TRAILING_GLOB_ARG = re.compile(r"(?:\s+\*|\s*:\*)\s*$")
# Shell operators that end one command segment and start the next.
_OPERATOR_SPLIT = re.compile(r"\s*(?:&&|\|\||\||;|>>|>|<)\s*")
# A path candidate begins at / or ~/ or $HOME/ , at a segment/quote boundary.
_PATH_START = re.compile(r"(?:^|(?<=[\s\"'`=(]))(?:~/|\$HOME/|/)")


def unwrap(rule):
    m = _TOOL_WRAP.match(rule.strip())
    inner = m.group(1) if m else rule.strip()
    return _TRAILING_GLOB_ARG.sub("", inner).strip()


def strip_trailing_glob(path):
    """Drop trailing path segments that are wildcards or empty (a glob tail carries no literal)."""
    parts = path.split("/")
    while parts and (parts[-1] == "" or "*" in parts[-1] or "?" in parts[-1]):
        parts.pop()
    return "/".join(parts)


def expand(path):
    if path.startswith("~"):
        path = os.path.expanduser(path)
    return os.path.expandvars(path)


def path_runs(cmd):
    """Yield each maximal path run in a command string: from a path start to the next start or the
    end of its quote/operator-bounded piece. Spaces stay INSIDE a run so a path with a space (the
    Google Chrome shape) is not split into a missing prefix."""
    runs = []
    for segment in _OPERATOR_SPLIT.split(cmd):
        # Split on quotes so a quoted path is one whole piece bounded by its quotes.
        for piece in re.split(r"[\"'`]", segment):
            starts = [m.start() for m in _PATH_START.finditer(piece)]
            for i, s in enumerate(starts):
                end = starts[i + 1] if i + 1 < len(starts) else len(piece)
                run = piece[s:end].strip()
                if run:
                    runs.append(run)
    return runs


def classify(run):
    """('exists'|'dead'|'unresolved', detail) for one path run."""
    literal = strip_trailing_glob(run)
    expanded = expand(literal)
    if "*" in expanded or "?" in expanded:
        return ("unresolved", "wildcard inside the path: %s" % run)
    if "$" in expanded:
        return ("unresolved", "unresolved variable in the path: %s" % run)
    if not expanded.startswith("/"):
        return ("unresolved", "not an absolute path after expansion: %s" % run)
    if os.path.exists(expanded):
        return ("exists", expanded)
    # The run may carry a trailing non-path argument after a space; the longest existing prefix at a
    # word boundary is the real path if one exists (the Chrome-with-a-space shape, already resolved
    # above unless the whole thing is absent).
    words = expanded.split(" ")
    for k in range(len(words) - 1, 0, -1):
        prefix = " ".join(words[:k])
        if prefix and os.path.exists(prefix):
            return ("exists", prefix)
    # Nothing resolves to an existing path: the first path word is the intended, dead target.
    return ("dead", words[0])


def rules_of(settings):
    perms = settings.get("permissions", {})
    rules = []
    for key in ("allow", "deny", "ask"):
        val = perms.get(key, [])
        if isinstance(val, list):
            rules.extend(r for r in val if isinstance(r, str))
    return rules


def scan_file(path):
    """Return (dead_messages, unresolved_messages, counts) for one settings file, or None to stand
    down. Raises ValueError on unreadable JSON (the caller reds that — never a false pass)."""
    with open(path) as f:
        settings = json.load(f)
    dead, unresolved = [], []
    rules = rules_of(settings)
    path_rules = resolved = 0
    for rule in rules:
        runs = path_runs(unwrap(rule))
        if runs:
            path_rules += 1
        for run in runs:
            verdict, detail = classify(run)
            if verdict == "exists":
                resolved += 1
            elif verdict == "dead":
                resolved += 1
                dead.append((rule, detail))
            else:
                unresolved.append((rule, detail))
    counts = {"rules": len(rules), "path_rules": path_rules, "resolved": resolved}
    return dead, unresolved, counts


def settings_targets():
    override = os.environ.get("CONFIG_HEALTH_PERMS_SETTINGS")
    if override:
        return [override]
    return [
        os.path.join(os.path.expanduser("~"), ".claude", "settings.json"),   # personal layer
        os.path.join(REPO_ROOT, ".claude", "settings.json"),                 # host project layer
    ]


def main():
    fail = 0
    scanned_any = False
    for target in settings_targets():
        if not os.path.isfile(target):
            print("config-health(perms): no settings at %s — the permission-path check stands down "
                  "by name (personal-layer file, absent here)." % target)
            continue
        try:
            dead, unresolved, counts = scan_file(target)
        except (ValueError, OSError) as e:
            print("{\"severity\":\"error\",\"code\":\"config-health\",\"message\":\"settings.json "
                  "at %s is unreadable (%s) — cannot verify its permission paths\",\"fix\":\"repair "
                  "the JSON so the permission-path check can read it\"}" % (target, e))
            fail = 1
            continue
        scanned_any = True
        for rule, detail in dead:
            print("{\"severity\":\"error\",\"code\":\"config-health\",\"message\":\"dead permission "
                  "rule in %s: %s points at a path that does not exist (%s)\",\"fix\":\"repoint the "
                  "rule at the current path or drop it\"}" % (target, rule, detail))
            fail = 1
        for rule, detail in unresolved:
            print("config-health(perms): unresolved path shape in %s — %s (named, not reded; the "
                  "check resolves absolute and ~/ paths only)." % (target, detail))
        print("config-health(perms): %s — %d rules, %d name a path, %d path(s) resolved, "
              "%d dead, %d unresolved."
              % (target, counts["rules"], counts["path_rules"], counts["resolved"],
                 len(dead), len(unresolved)))

    if fail == 0 and scanned_any:
        print("config-health(perms): OK (every permission rule's filesystem path exists).")
    return fail


if __name__ == "__main__":
    sys.exit(main())
