# [Project Name] — Architecture

How the product is BUILT: the named nodes the spec's facts live in. Written from the proven SPEC.md,
proven itself (product-prover, architecture lens) before the test matrix is derived from it. One node =
one name = one responsibility — the one-surface-one-name rule, applied to structure.

**When this doc changes:** a large or surface-class wish updates it BEFORE the matrix is touched; a bug or
small wish only cites the existing node it lands in. Re-proven only when it changes.

**This doc is ITERATIVE. Never written milestones ahead.** It maps the product as it stands plus the
landing in flight. A node exists for what ships today, or for what the spec already promises under an
owned queue row (marked [target], pin empty until code lands). A future feature earns its node when its
landing arrives; a speculative node is unbacked structure — the prover flags it as a node without spec
backing.

---

## Nodes

Every spec fact is OWNED by exactly one node. In a live codebase every node pins to its owning
`file:line` (each pin from a command actually run — an unverified pin is merely a claim). In a
new project the pin column starts empty and fills as code lands.

| Node | Responsibility (one line) | Owns spec facts (anchors) | Pinned to (file:line) |
|---|---|---|---|
| [e.g. renderer] | [builds the HTML widget from analysis JSON] | INV-1, T-3, E-2 | `build_widget.py:120` |
| [e.g. player] | [multi-stem playback, seek, mute/solo] | INV-4..6 | `player.js:1` |

## Seams

The places two nodes meet — named, because that is where composition bugs live. Each seam states what
crosses it and which side owns the format.

| Seam | Between | What crosses | Format owner |
|---|---|---|---|
| [analysis → render] | [analyzer · renderer] | [analysis JSON] | [analyzer] |

## Prover record

| Date | Doc version proven | Record |
|---|---|---|
| [YYYY-MM-DD] | [v0.1] | `docs/prover/YYYY-MM-DD-architecture.md` |

---

*Coverage rule (walked at matrix derivation): every spec anchor appears in some node's "owns" column —
an orphan fact means a missing node or a missing assignment; a node owning nothing traces to no spec
backing and is itself a finding.*
