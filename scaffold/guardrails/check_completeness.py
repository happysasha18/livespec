#!/usr/bin/env python3
"""check_completeness.py — no partial or stripped artifact ships (SPEC INV-97).

The surface registry (`registry_path`) is compared against the RENDERED content both
ways: every registered surface must be present and non-empty, and — when
`surface_discovery_pattern` is set — every surface the rendered content exhibits must
be registered (the self-closing direction: you cannot drift past this by forgetting
to update a list).

Usage: python3 check_completeness.py   (config: $GUARDRAILS_CONFIG or
./guardrails.config.json; run from the host repo root)

Python 3.9 stdlib only.
"""

import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_lib  # noqa: E402

CHECK = "completeness"
TAG = re.compile(r"<[^>]*>")


def rendered_content(config, root):
    """The content under test: `render_command`'s stdout when the host declares one,
    else every file named in `rendered_artifacts` read off disk."""
    command = config.get("render_command")
    if command:
        proc = subprocess.run(command, shell=True, cwd=root,
                              capture_output=True, text=True)
        if proc.returncode != 0:
            gate_lib.fail(CHECK, "dead-path",
                          "render_command %r exited %d: %s"
                          % (command, proc.returncode, proc.stderr.strip()[:300]),
                          "make render_command runnable from the repo root, or set it "
                          "to null and list rendered_artifacts instead")
        return proc.stdout
    artifacts = gate_lib.require_key(CHECK, config, "rendered_artifacts")
    chunks = []
    for rel in artifacts:
        full = gate_lib.require_path(CHECK, root, rel, "rendered artifact")
        chunks.append(gate_lib.read_file(full))
    return "\n".join(chunks)


def matching_lines(needle, content):
    """Lines the needle hits — as a plain substring first, else as a regex."""
    lines = [ln for ln in content.splitlines() if needle in ln]
    if lines:
        return lines, False
    try:
        pattern = re.compile(needle)
    except re.error:
        return [], False
    return [ln for ln in content.splitlines() if pattern.search(ln)], True


def line_is_empty(line, needle, is_regex):
    """Empty match content: the needle's line carries no other non-tag text."""
    text = TAG.sub("", line)
    if is_regex:
        text = re.sub(needle, "", text)
    else:
        text = text.replace(needle, "")
    return not text.strip()


def main():
    config, root = gate_lib.load_config(CHECK)
    registry_rel = gate_lib.require_key(CHECK, config, "registry_path")
    registry_path = gate_lib.require_path(CHECK, root, registry_rel, "registry")
    rows = gate_lib.parse_registry(gate_lib.read_file(registry_path))
    content = rendered_content(config, root)

    for name, needle, _anchors in rows:
        lines, is_regex = matching_lines(needle, content)
        if not lines:
            gate_lib.fail(CHECK, "registered-but-absent",
                          "surface %r is registered in %s but its needle %r matches "
                          "nothing in the rendered content" % (name, registry_rel, needle),
                          "render the %r surface (or retire its registry row if it is "
                          "gone on purpose)" % name)
        if all(line_is_empty(ln, needle, is_regex) for ln in lines):
            gate_lib.fail(CHECK, "registered-but-empty",
                          "surface %r matches in the rendered content but every "
                          "matching line is empty of non-tag text" % name,
                          "give the %r surface real content — an empty element must "
                          "not pass as present" % name)

    discovery = config.get("surface_discovery_pattern")
    if discovery:
        registered = {name for name, _n, _a in rows}
        found = re.findall(discovery, content)
        unregistered = sorted({fid for fid in found if fid not in registered})
        if unregistered:
            gate_lib.fail(CHECK, "rendered-but-unregistered",
                          "rendered content exhibits surface id(s) %s absent from the "
                          "registry %s" % (", ".join(unregistered), registry_rel),
                          "add a registry row for each rendered surface — the DOM is "
                          "the source of truth, the registry must keep up")

    gate_lib.ok(CHECK, "%d registered surface(s) present and non-empty; rendered "
                       "content exhibits nothing unregistered" % len(rows))


if __name__ == "__main__":
    main()
