# live-spec — SPEC prose style (the register a spec is written in)

Decided 2026-07-08 with Alexander, grounded in RFC 2119/8174, the RFC 7322 style guide, Diátaxis
(reference documentation), and exemplars — the Go language specification, RFC 9110 (HTTP), ECMA-262,
POSIX — plus a register brief from Fable.

**A spec is REFERENCE documentation**: austere, systematic, terse, factual, present tense, described
without opinion. Not a tutorial, not an explainer, not a story. It is consulted, not read cover to cover.

## TARGET REGISTER — Flavor A (declarative / Go-spec)

Force is carried by plain declarative statement, NOT by RFC keywords. State each rule as a fact of a
conforming system ("A decision card opens with an Effect Statement."). Use "does not" / "never" for
prohibitions. No MUST/SHALL machinery, no §-numbering, no NOTE-boilerplate required. Terse, dry,
definitional — like the Go language specification. Readable. (A stricter full-RFC-2119 flavor was
considered and set aside as too heavy for this genre; if a future host needs it, it is the same rules
plus the capitalized keyword system.)

## The rules

- **R2 — One requirement per sentence.** Never bundle two rules with "and"; each must be individually citable and testable.
- **R3 — Every requirement binds a NAMED actor**: "The classifier …", "A decision card …", "The ask …". BANNED: second person ("you"); vague "it"/"the system" when a finer actor exists.
- **R4 — Declarative PRESENT tense.** Facts as facts, rules as rules. BANNED: future narration ("the card will show"), invitation ("let's"), reassurance ("don't worry", "you can ignore").
- **R5 — Defined terms, used VERBATIM, forever.** No elegant variation; a different word asserts a different thing. Repetition is correct.
- **R6 — NORMATIVE and INFORMATIVE are separated.** Rationale, motivation, examples live in a marked companion, never folded into a requirement sentence.
- **R7 — The normative body has no metaphor, no warmth, no narration, no persona.** BANNED there: "simply/just/of course", sign-posting ("as we saw above"), apologies, jokes. Cross-reference by section, not by story.
- **R7b — Warmth is quarantined, not deleted.** Human touches (a user quote, motivating voice) are legal ONLY as a separate, clearly-marked informative element beside the rule (`NOTE (informative):` or a `> quote`), never inside a normative sentence. The dry statement comes first; the note is an optional companion.
- **R7c — A quote earns its place or it is cut.** Keep a quote only when it adds something the formal rule does not capture, or is needed to understand the rule; drop decorative/redundant quotes. Any quote that stays is translated into idiomatic English, never verbatim source-language. The whole informative/voice lane is gated by the project's KIND and the aspect: a book, or a project with a distinctive interface, can warrant it; a backend service almost never does. Default is no quote.
- **R8 — Testability is the acceptance test of a sentence.** Untestable qualifiers ("if it helps", "where sensible", "generally") are deleted, given a stated criterion, or moved to a note.
- **R9 — Canonical conditional**: "If X, the Y does Z", with an explicit "otherwise" — never leave a case unaccounted.
- **R10 — Exact quantities and references.** BANNED: "a few", "small", "recently".
- **R11 — Pronoun hygiene**: "it"/"this"/"they" only with an unambiguous same-sentence antecedent; else repeat the noun.
- **R12 — Typographic shout is not force.** Remove ALL-CAPS/bold on ordinary verbs ("CHANGES"). Force comes from the declarative statement itself.

**HARD (unchanged from the current doc):** every bracketed anchor token stays VERBATIM in place; never
drop a rule; keep `##`/`###` headings and bold law-titles; provenance stays out of the body (in JOURNAL).

## Exemplar — one real section in the target register

Source register was the warm "colleague" voice; this is the same section, same anchors, in Flavor A:

---

## Asking what the product does (the feature map on demand)

The ask answers a "show all features" request with one answer containing the whole product map, current as of the request. The departures board reports in-flight work status at every report [INV-27]. Intake places each arriving wish on the map [INV-37]. The ask answers the third of the three standing questions — what the product does today — with the whole map, on demand.

The ask reads its answer live from the living documents:

- the spec's scenario sections name the features;
- the header's current-vs-target paragraph separates shipped features from promised features, at the granularity the [target] tag binds to. A scenario containing both shipped law and named promised parts is marked "shipped, with promised parts (named)," each status stated at that same granularity [S-0];
- the queue's open rows supply the remainder: each in-flight feature's station, and each wish whose `map:` verdict is NEW while its scenario is still unwritten. The queue shows a feature on the map before the spec documents it [INV-27, INV-37].

The spec's scenarios and the architecture's nodes constitute the map. No third document exists to maintain. No separate copy exists to drift out of date — no feature-list file, no cached copy [E-14]. The ask reads the living documents directly.

Each line follows the line law [INV-28]:

- a short descriptive name, in the product's own words;
- the value the feature gives its user;
- the feature's status — shipped, target, or in-flight — followed by its station.

The ask delivers the map in chat by default. The ask delivers a rendered page instead on request, per the show rule [default]. Routine reports retain the departures board's in-flight scope. The ask returns the whole map only on request.

If a host has no spec and no scenario sections, the ask states that condition; otherwise the ask proceeds as described above. The ask directs the requester to bootstrap or adoption when that condition holds. The ask reports only what currently exists [INV-38].
