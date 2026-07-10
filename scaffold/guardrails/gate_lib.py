"""gate_lib — the tiny shared floor under the four host checks (SPEC INV-97).

Config loading + validation, waiver resolution, the typed failure line (SPEC INV-47),
and `**`-aware glob matching. NO check logic lives here: each check owns its own
reading of the tree; this module only makes their honesty uniform — a missing config
is red with an attach-me line, a dead path is red, a declared waiver is visible.

Python 3.9 stdlib only — this file gets copied into arbitrary host repos.
"""

import json
import os
import re
import sys

ATTACH_ME_FIX = ("copy guardrails.config.example.json to guardrails.config.json and "
                 "fill your paths — see scaffold/guardrails/README.md")


def fail(check, reason, message, fix):
    """Red, honestly: the human sentence, then the one machine line (SPEC INV-47),
    then exit 1. `fix` is the same sentence a person reads."""
    code = "%s.%s" % (check, reason)
    print("FAIL (%s): %s" % (check, message))
    print("  fix: %s" % fix)
    print("GUARDRAIL-FAIL " + json.dumps(
        {"severity": "error", "code": code, "message": message, "fix": fix},
        ensure_ascii=False))
    sys.exit(1)


def ok(check, summary):
    print("OK (%s): %s" % (check, summary))
    sys.exit(0)


def load_config(check):
    """Resolve the host config: $GUARDRAILS_CONFIG if set, else ./guardrails.config.json
    at the repo root. Missing or unparseable is RED with the attach-me line — never a
    silent pass. Returns (config dict, host root dir) and honours a declared waiver."""
    path = os.environ.get("GUARDRAILS_CONFIG") or os.path.join(
        os.getcwd(), "guardrails.config.json")
    if not os.path.isfile(path):
        fail(check, "no-config",
             "no guardrails config found at %s" % path, ATTACH_ME_FIX)
    try:
        with open(path, encoding="utf-8") as f:
            config = json.load(f)
    except ValueError as e:
        fail(check, "no-config",
             "guardrails config at %s is not valid JSON: %s" % (path, e), ATTACH_ME_FIX)
    if not isinstance(config, dict):
        fail(check, "no-config",
             "guardrails config at %s is not a JSON object" % path, ATTACH_ME_FIX)
    root = os.path.dirname(os.path.abspath(path))
    waive_if_declared(check, config)
    return config, root


def waive_if_declared(check, config):
    """A check named in `waivers` prints its reason and exits 0 — visible, never silent."""
    waivers = config.get("waivers") or {}
    if check in waivers:
        print("WAIVED (%s): %s" % (check, waivers[check]))
        sys.exit(0)


def require_key(check, config, key):
    if key not in config or config[key] in (None, ""):
        fail(check, "no-config",
             "guardrails config lacks the %r key this check needs" % key, ATTACH_ME_FIX)
    return config[key]


def require_path(check, root, rel, what):
    """Any declared path that does not exist on disk is RED — a config pointing at
    nothing must never look green."""
    full = os.path.join(root, rel)
    if not os.path.exists(full):
        fail(check, "dead-path",
             "config declares %s %r but %s does not exist" % (what, rel, full),
             "fix the %r entry in guardrails.config.json to a path that exists, "
             "or declare a waiver for %r in its \"waivers\" map" % (what, check))
    return full


def glob_base(pattern):
    """The literal leading directory of a glob — 'src' for 'src/**/*.py', '' when the
    pattern starts wild (nothing to existence-check)."""
    parts = []
    for part in pattern.split("/"):
        if any(ch in part for ch in "*?["):
            break
        parts.append(part)
    return "/".join(parts)


def glob_match(path, pattern):
    """`**`-aware match of a /-separated relative path against one glob pattern.
    `**` crosses directory boundaries; `*` and `?` never do (fnmatch alone would)."""
    out = []
    i = 0
    while i < len(pattern):
        ch = pattern[i]
        if ch == "*":
            if pattern[i:i + 3] == "**/":
                out.append("(?:.*/)?")
                i += 3
            elif pattern[i:i + 2] == "**":
                out.append(".*")
                i += 2
            else:
                out.append("[^/]*")
                i += 1
        elif ch == "?":
            out.append("[^/]")
            i += 1
        else:
            out.append(re.escape(ch))
            i += 1
    return re.match("^" + "".join(out) + "$", path.replace(os.sep, "/")) is not None


def read_file(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def parse_registry(text):
    """Registry rows: `| <surface-name> | <needle-or-regex> | <spec-anchors comma-sep> |`.
    Header and separator rows ignored; returns [(name, needle, [anchors...]), ...]."""
    rows = []
    seen_header = False
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c != ""):
            continue  # separator row
        if not seen_header:
            seen_header = True  # the first non-separator table row is the header
            continue
        if len(cells) < 3:
            continue
        name, needle = cells[0], cells[1]
        anchors = [a.strip() for a in cells[2].split(",") if a.strip()]
        rows.append((name, needle, anchors))
    return rows
