#!/usr/bin/env python3
"""assemble.py — build the one requirements-format PRODUCT_SPEC.md from the nine converted units.

Reads the nine section.md files (read-only), strips each unit's head (title, preamble, per-unit
glossary), renumbers requirements into one continuous sequence, pools the glossaries into one block,
applies the declared body sharpens from ASSEMBLY-NOTES, and writes assembly/PRODUCT_SPEC.md. Then it
builds the generated code-to-location table with the shared parser and appends it as the Reference
section. Stdlib only.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROTO = os.path.dirname(HERE)                                  # prototype/2026-07-22-spec-format
CONV = os.path.join(PROTO, "conversion")
REPO = os.path.dirname(os.path.dirname(PROTO))                 # repo root
GUARDRAILS = os.path.join(REPO, "guardrails")
sys.path.insert(0, GUARDRAILS)
import specformat as sf  # noqa: E402

# Source order mirrors docs/attic/2026-07-22-pre-format/PRODUCT_SPEC.md. The pilot unit
# (Starting and adopting a project) lives beside the conversion directory, at its source position
# between when-something-breaks and agents-together. The composing-across-axes unit (converted from
# the Reference section's essay) closes the normative body, after bounds — its cross-references all
# point backward, and the source's own order places it last.
UNITS = [
    "what-live-spec-is",
    "build-loop-a-intake",
    "build-loop-b-doors-spec-lanes",
    "build-loop-c-prototype-tests-rhythm-publish",
    "what-the-human-sends-back",
    "when-something-breaks",
    "pilot",
    "agents-together",
    "rules-and-who-applies",
    "bounds",
    "composing-across-axes",
    "format-laws",
]

UNIT_DIRS = {"pilot": os.path.join(PROTO, "pilot")}


def unit_path(unit):
    return UNIT_DIRS.get(unit, os.path.join(CONV, unit))

REQ_RE = re.compile(r"^## Requirement\s+(\d+)\s*:\s*(.*)$")
TERM_RE = re.compile(r"^\s*-\s+\*\*(.+?)\*\*\s+—\s+(.*\S)\s*$")

TITLE = "# live-spec — Product Spec (v4.0.0, 2026-07-22)"

PREAMBLE = """\
This document is the living statement of what live-spec is right now. The body is a flat list of requirements, each stating one rule of the method. A requirement carries a Context block, a one-sentence User Story, and acceptance criteria grouped into named cases; a requirement whose heading carries a `[feature: F-...]` tag is a person-facing scenario — what the reader does and what the reader sees. Edit history lives in `JOURNAL.md`; this spec states what is true today.

live-spec takes any request a person submits, of any size and at any moment, breaks it into story-sized pieces — one user story to a piece — and runs each piece through the same pipeline, one stage at a time, each stage checked by its own gate before the next, until the piece reaches a delivery and ships tested. A machine enforces the process at every step, every claim earns a test, and nothing ships until that test passes.

Bracket codes like `[E-1]` and `[INV-27]` trail a criterion and point to the rule's home in the project spec; a reader can ignore them, a maintainer follows them. The letter before the number names the kind: `E-` an entity, a numbered part of the product; `INV-` an invariant, a numbered rule that must always hold; `T-` a transition, a numbered change of state; `M-` a rhythm rule, a numbered recurring routine; `A-` an adoption step; `B-` a bootstrap step; `ACT-` an actor; `C-` a composition-axis rule; `D-` a recorded decision; `S-` a header rule; and `F-` a feature, which a scenario heading carries as a `[feature: F-...]` tag. A range such as `[T-1..T-7]` cites its whole run of codes. A `[target]` marker on a line of its own marks a feature or leg that is promised but not yet built, and a `[default]` marker names a value the agent set that the human may retune. A `[GAP: ...]` line under a criterion records a place the source states a behaviour and leaves its judge, its measure, or its scope unstated; it is the honest output for a real hole, never a filled-in guess.

The keywords *when*, *while*, *if*, *then*, and *shall* are set in lowercase italics and carry their standard requirements meaning: *shall* states a duty, *when* and *while* open a situation, and *if* and *then* open a condition and its result.

The foundational nouns of the method — request, pipeline, spec, architecture, invariant, guardrail, suite, session, journal, queue, movement, delivery, delivery report, footprint, profile, and resume file — carry the meanings the base method glossary gives them. The glossary below defines, in one place, every domain noun the twelve assembled sections introduce; a term appears once, under one name, and the criteria use it with that meaning.
"""

# --- Collision resolutions: term.lower() -> (canonical term, chosen/merged definition). --------------
OVERRIDES = {
    "user story": ("user story",
        "the unit a request is split into: one distinct thing a person does and sees, told as a short sentence naming who wants what and for which benefit; a wish carries one, and a wish carrying more is split at intake into a row apiece."),
    "base skill": ("base skill",
        "the pack skill that holds the shared rulebook and the default settings, stated once, so every working skill points at one home rather than restating them."),
    "working skill": ("working skill",
        "a pack skill that elaborates one domain of the pipeline and opens by naming the base skill and the base version it was written against; the pack's working skills are spec-author, product-prover, design-reviewer, build-pipeline, test-author, communicator, publish, text-audit (the audit-and-fix loop for human-facing texts, which runs mechanical lints and then fresh zero-context cold reads and fixes each finding at its source until two reads come back clean in a row), feedback-intake, and feedback-collector."),
    "target tag": ("target tag",
        "the marker `[target]` a spec line carries on a line of its own to mark a feature or leg that is promised but not yet built."),
    "checkpoint": ("checkpoint",
        "a saved point of work that can be resumed from, written under `.live-spec/`. A planned-work checkpoint is one grouped unit of planned work in the resume state, carrying a status the landing that ships its items flips to closed; a worker's checkpoint is the file a worker keeps under `.live-spec/checkpoints/`, holding its resume point and touched on a fixed interval as a heartbeat."),
    "spec-delta": ("spec-delta",
        "the set of spec sentences one wish or feature adds or changes, drafted and proven against the whole spec before any test or code is written."),
    "door": ("door",
        "the intake classification that places a queued wish at one entry point of the pipeline, one of feature, bug, refactor, docs-only, or skip, decided before any code is written and kept separate from the wish's size. A request that never becomes a queued wish — an ask merely to see or try a thing — takes a separate entry lane, the labelled-sketch door, held outside this five-way set."),
    "work-kind": ("work-kind",
        "the intake axis naming what a wish produces, one of product, infra, skill, or prose, which scales how much machinery each pipeline step spends."),
    "decision archive": ("decision archive",
        "the directory `docs/decisions/` where a decision page is filed once its answer comes back."),
    "regression fence": ("regression fence",
        "one sentence in a spec-delta naming a neighbouring promise that must stay true through a change, citing the existing clause it guards."),
    "non-goal": ("non-goal",
        "one sentence in a spec-delta naming what the change deliberately leaves out, so a deliberate absence reads as a decision."),
    "success measure": ("success measure",
        "one written way, with a number where one exists, to notice a feature worked for its person, written in the feature's spec-delta."),
    "status report": ("status report",
        "the running account a session keeps of the work in hand, what the queue holds next, and the messages its agent channel has sent."),
    "lens": ("lens",
        "a named check the prover or the design review walks a document with, each testing one concern (the architecture lens, the cognitive-load lens)."),
    "catch-up walk": ("catch-up walk",
        "the ordered set of steps a session walks to run catch-up on an adopted host."),
    "seat": ("seat",
        "the one acting orchestrator session that owns judgment, orchestrates the pipeline, briefs workers, judges lane independence, reads and writes and reports during a turn, and reports to the person; the source also names this actor the senior, the senior agent, and the orchestrator, and this document keeps the one name seat throughout."),
    "problem ledger": ("problem ledger",
        "the per-host file `.live-spec/PROBLEMS.md` that records the workshop's own recurring operational noise as a signature with its dated occurrences and a status, born on its first entry."),
    "concurrent-edit fence": ("concurrent-edit fence",
        "the check, run before every shared write or commit, that compares the repository's `HEAD` and tree state against what the session last read at its start, blocking a commit when either has moved, and clearing again once the session re-reads and accounts for the change."),
    "grant": ("grant",
        "one recorded permission a session or remote seat holds for one repository: a push grant to deposit and push into it, a read grant to clone and pull a private producer's repository."),
    "stranger": ("stranger",
        "a contributor with no push rights and no per-repository grant for a repository; a stranger's message enters through an Issue or Discussion opened on the repository's public tracker, which the monitor bridges into the inbox."),
}

# The when-something-breaks "delta" entry folds into "spec-delta" (ASSEMBLY-NOTES item 2), and the
# what-live-spec-is plural "checkpoints" entry folds into the singular "checkpoint" entry.
REMOVE = {"delta", "checkpoints"}

# New entries the worklist demands (ASSEMBLY-NOTES items 3, 9, 11, 12, 13, 15, 16, 17, 18). Each term
# appears in a body, so none is a dead glossary entry. Definitions are sourced from the units' bodies.
ADDITIONS = [
    ("milestone",
     "a rhythm point where the whole spec and architecture are re-proven, the design review runs, and the full gate list completes; periodic routines such as the skill-eval re-run and the problem-ledger compaction fold in at it."),
    ("gate",
     "a check that must pass before work proceeds; a red gate stops the work at that step."),
    ("expected-red note",
     "a recorded note that a check is held red for an understood, stated reason, which keeps a known owned problem parked without blocking unrelated work."),
    ("proactivity mode",
     "the per-person setting for how far the agent acts on its own before asking, held in the personal profile and moved only on the human's word."),
    ("revisit trigger",
     "the recorded condition on a deferred queue row that, once it fires against the current moment, returns the row to the runnable head."),
    ("Done-when",
     "the written acceptance a queue row or one of its legs carries, naming the observable state that closes it."),
    ("queue-take",
     "the moment a session reads the queue's runnable head to plan the next work, building its dependency graph before opening any lane."),
    ("deferral test",
     "the intake check on whether a wish's work may be deferred, run before any row is parked."),
    ("suite-honesty class",
     "the class of invariants that keep a green suite meaningful — each naming the net that enforces it — so a passing suite proves the behaviour it claims."),
    ("open leg",
     "a leg of a multi-part queue row whose own Done-when acceptance has not yet been met."),
    ("verify walk",
     "the pipeline's final step, run in the form the medium has, where the delivery is exercised end to end through the visitor's own outside eyes before the row closes."),
    ("echo-name",
     "the short name the capture echo posts back on an item's source, so the person can find the row the item became."),
    # item 9's home pointer, in scope now that the starting-and-adopting (pilot) unit is assembled:
    ("orient",
     "adoption's opening phase, in which the system reads every existing document before touching anything and answers the founding questions about what it found; its digest and inventory land in `.live-spec/adopt/`."),
]


def split_head_body(text):
    lines = text.split("\n")
    first_req = None
    for i, ln in enumerate(lines):
        if REQ_RE.match(ln.strip()):
            first_req = i
            break
    head = "\n".join(lines[:first_req])
    body = "\n".join(lines[first_req:])
    return head, body


def collect_glossary(head):
    out = []
    for ln in head.split("\n"):
        m = TERM_RE.match(ln)
        if m:
            out.append((m.group(1).strip(), m.group(2).strip()))
    return out


def renumber(body, offset):
    def repl(m):
        return "## Requirement %d: %s" % (int(m.group(1)) + offset, m.group(2))
    out = []
    for ln in body.split("\n"):
        m = REQ_RE.match(ln)
        out.append(REQ_RE.sub(repl, ln) if m else ln)
    return "\n".join(out)


# --- Declared body sharpens (ASSEMBLY-NOTES). Each is (unit, old, new); applied once, must match. -----
SHARPENS = {
    "build-loop-c-prototype-tests-rhythm-publish": [
        # item 1: R47.1 mis-anchor E-12 -> E-20 (publish skill owns the per-kind checklist).
        ("riding the delivery report like any other step. [E-12, INV-22]",
         "riding the delivery report like any other step. [E-20, INV-22]"),
    ],
    "when-something-breaks": [
        # item 2: "delta" is renamed to the one name "spec-delta".
        ("re-fence and re-prove its delta against the now-committed truth",
         "re-fence and re-prove its spec-delta against the now-committed truth"),
        ("since the bug's fix may have moved the law the delta was built against",
         "since the bug's fix may have moved the law the spec-delta was built against"),
        ("The system *shall* integrate no delta proven only against the pre-bug truth",
         "The system *shall* integrate no spec-delta proven only against the pre-bug truth"),
        # item 9: enumerate the four moves where the closed set is named (Context edit, no criterion).
        ("the method drives four moves rather than one, so a point fix",
         "the method drives four moves rather than one — name the class and hunt its siblings, check the architecture, check the spec, and escalate a boundary call to the human — so a point fix"),
    ],
}


def apply_sharpens(unit, body):
    for old, new in SHARPENS.get(unit, []):
        n = body.count(old)
        if n != 1:
            raise SystemExit("sharpen match error in %s: %d matches for %r" % (unit, n, old[:50]))
        body = body.replace(old, new)
    return body


def main():
    gloss = {}          # term.lower() -> (term, definition), first occurrence wins
    bodies = []
    offset = 0
    counts = []
    for unit in UNITS:
        with open(os.path.join(unit_path(unit), "section.md"), encoding="utf-8") as f:
            text = f.read()
        head, body = split_head_body(text)
        for term, definition in collect_glossary(head):
            key = term.lower()
            if key not in gloss:
                gloss[key] = (term, definition)
        body = apply_sharpens(unit, body)
        n = len(REQ_RE.findall("\n".join(l for l in body.split("\n") if REQ_RE.match(l.strip()))))
        n = sum(1 for l in body.split("\n") if REQ_RE.match(l.strip()))
        body = renumber(body, offset)
        counts.append((unit, offset + 1, offset + n))
        offset += n
        bodies.append(body.strip())

    # Apply glossary overrides, removals, and additions.
    for key, (term, definition) in OVERRIDES.items():
        gloss[key] = (term, definition)
    for key in REMOVE:
        gloss.pop(key, None)
    for term, definition in ADDITIONS:
        gloss[term.lower()] = (term, definition)

    entries = sorted(gloss.values(), key=lambda td: td[0].lower().lstrip("`"))
    gloss_lines = ["## Glossary", ""]
    for term, definition in entries:
        gloss_lines.append("- **%s** — %s" % (term, definition))
    glossary = "\n".join(gloss_lines)

    doc_no_index = "\n\n".join([TITLE, PREAMBLE.rstrip(), glossary, "\n\n".join(bodies)]) + "\n"

    # Build the generated code-to-location table from the assembled body criteria.
    parsed = sf.parse(doc_no_index)
    table = sf.build_index_table(parsed)
    with open(os.path.join(HERE, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write(table)

    reference = ("## Reference\n\nThe code-to-location table below is generated output, built from the "
                 "body criteria by `scripts/build-index.py`; no one edits it by hand. Feature codes "
                 "(`F-...`) live on their scenario headings and carry no table row.\n\n" + table)
    doc = doc_no_index + "\n" + reference

    with open(os.path.join(HERE, "PRODUCT_SPEC.md"), "w", encoding="utf-8") as f:
        f.write(doc)

    total_reqs = offset
    print("requirements: %d" % total_reqs)
    for unit, a, b in counts:
        print("  %-46s R%d..R%d" % (unit, a, b))
    print("glossary entries: %d" % len(entries))
    print("bytes: %d" % len(doc.encode("utf-8")))


if __name__ == "__main__":
    main()
