#!/usr/bin/env python3
"""check_tests_present.py — tests travel with every change (SPEC INV-97).

If the diff against the base ref touches any file matching `user_facing_globs` and
touches nothing under `tests_dir`, this is RED. It does not judge whether the test is
good — that is the matrix's and the prover's job — only whether one exists at all.

Usage: python3 check_tests_present.py [--base REF]
Base resolution: --base arg, else origin/main when it resolves, else the config's
"base_ref". Config: $GUARDRAILS_CONFIG or ./guardrails.config.json.

Python 3.9 stdlib only.
"""

import argparse
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_lib  # noqa: E402

CHECK = "tests-present"


def git(root, *args):
    return subprocess.run(["git"] + list(args), cwd=root,
                          capture_output=True, text=True)


_VERSION = re.compile(r"\d+\.\d+\.\d+")


def _stamp_only(root, base, path):
    """True when the file's base and HEAD contents are identical after every version
    string (N.N.N) is normalized — the version stamp's mechanical output."""
    old = git(root, "show", "%s:%s" % (base, path))
    if old.returncode != 0:
        return False
    try:
        with open(os.path.join(root, path), encoding="utf-8") as f:
            new = f.read()
    except OSError:
        return False
    return _VERSION.sub("V", old.stdout) == _VERSION.sub("V", new)


def resolve_base(root, arg_base, config):
    if arg_base:
        return arg_base
    if git(root, "rev-parse", "--verify", "--quiet", "origin/main").returncode == 0:
        return "origin/main"
    if config.get("base_ref"):
        return config["base_ref"]
    gate_lib.fail(CHECK, "dead-path",
                  "no base ref to diff against: no --base given, origin/main does not "
                  "resolve, and the config declares no \"base_ref\"",
                  "pass --base <ref>, or add \"base_ref\" to guardrails.config.json")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="git ref to diff against")
    args = parser.parse_args()

    config, root = gate_lib.load_config(CHECK)
    tests_dir = gate_lib.require_key(CHECK, config, "tests_dir").rstrip("/")
    gate_lib.require_path(CHECK, root, tests_dir, "tests_dir")
    globs = gate_lib.require_key(CHECK, config, "user_facing_globs")
    for pattern in globs:
        base_dir = gate_lib.glob_base(pattern)
        if base_dir:
            gate_lib.require_path(CHECK, root, base_dir,
                                  "user_facing_globs base for %r" % pattern)

    base = resolve_base(root, args.base, config)
    diff = git(root, "diff", "--name-only", "%s...HEAD" % base)
    if diff.returncode != 0:
        gate_lib.fail(CHECK, "dead-path",
                      "git diff against base %r failed: %s"
                      % (base, diff.stderr.strip()[:300]),
                      "pass --base with a ref that exists in this repository")
    changed = [ln.strip() for ln in diff.stdout.splitlines() if ln.strip()]

    offenders = [f for f in changed
                 if any(gate_lib.glob_match(f, g) for g in globs)]
    test_touched = [f for f in changed
                    if f == tests_dir or f.startswith(tests_dir + "/")]

    if offenders and not test_touched:
        # A file whose whole diff is version-string substitution is the stamp script's
        # mechanical output; the stamped-copy guard test already holds those copies, so
        # such a file stands outside this check's subject. A file added, deleted, or
        # unreadable stays an offender.
        real = [f for f in offenders if not _stamp_only(root, base, f)]
        if not real:
            gate_lib.ok(CHECK, "%d user-facing change(s) are version-stamp-only "
                               "(identical after normalizing version strings), held by "
                               "the stamped-copy guard test (base %s)"
                               % (len(offenders), base))
        gate_lib.fail(CHECK, "missing-test",
                      "user-facing file(s) changed with no change under %s/: %s"
                      % (tests_dir, ", ".join(real)),
                      "add or update a test under %s/ for this change (or record the "
                      "exemption where your matrix expects it)" % tests_dir)

    if offenders:
        gate_lib.ok(CHECK, "%d user-facing change(s) travel with %d test change(s) "
                           "(base %s)" % (len(offenders), len(test_touched), base))
    gate_lib.ok(CHECK, "no user-facing files changed against %s" % base)


if __name__ == "__main__":
    main()
