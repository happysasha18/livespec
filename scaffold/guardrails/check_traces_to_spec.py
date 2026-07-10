#!/usr/bin/env python3
"""check_traces_to_spec.py — every surface traces to a spec clause (SPEC INV-97).

Every registry row's third column must cite at least one anchor, and every cited
anchor must exist in `spec_path` — an anchor X-nn exists when the spec contains
`[X-nn]` or `| X-nn |`. A behaviour with no spec backing cannot ship: the clause
does not have to be detailed; it must exist. Silence is not enough.

Usage: python3 check_traces_to_spec.py   (config: $GUARDRAILS_CONFIG or
./guardrails.config.json; run from the host repo root)

Python 3.9 stdlib only.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_lib  # noqa: E402

CHECK = "traces"


def main():
    config, root = gate_lib.load_config(CHECK)
    registry_rel = gate_lib.require_key(CHECK, config, "registry_path")
    registry_path = gate_lib.require_path(CHECK, root, registry_rel, "registry")
    spec_rel = gate_lib.require_key(CHECK, config, "spec_path")
    spec_path = gate_lib.require_path(CHECK, root, spec_rel, "spec")

    rows = gate_lib.parse_registry(gate_lib.read_file(registry_path))
    spec = gate_lib.read_file(spec_path)

    cited = 0
    for name, _needle, anchors in rows:
        if not anchors:
            gate_lib.fail(CHECK, "unanchored-surface",
                          "surface %r in %s cites no spec anchor in its third column"
                          % (name, registry_rel),
                          "add at least one spec anchor to the %r registry row — a "
                          "one-line spec clause is enough, silence is not" % name)
        for anchor in anchors:
            if "[%s]" % anchor not in spec and "| %s |" % anchor not in spec:
                gate_lib.fail(CHECK, "dead-anchor",
                              "surface %r cites anchor %s which appears nowhere in %s "
                              "(neither [%s] nor | %s |)"
                              % (name, anchor, spec_rel, anchor, anchor),
                              "write the %s clause into %s (or fix the registry row's "
                              "citation)" % (anchor, spec_rel))
            cited += 1

    gate_lib.ok(CHECK, "%d surface(s) trace to %d live anchor citation(s) in %s"
                       % (len(rows), cited, spec_rel))


if __name__ == "__main__":
    main()
