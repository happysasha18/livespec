# Text audit — planted "About the workspace" paragraph (bare arm, no skill loaded)

Run 2026-07-23, one Sonnet worker, WITHOUT reading any skill file, zero tool uses (verified: 0 tool
calls in the transcript). Prompt: the eval's own bare-arm line — "Audit this paragraph — will a
stranger understand it? Tell me where a reader would stop." + "do not invoke any tools or skills" +
the paragraph verbatim. Honest boundary (evals/README.md) applies: bare-of-the-SKILL, loader-fed.
Verbatim transcript below.

---

[14:32] Stop points, in reading order:

1. **"keeps the workspace coherent"** — asserts a benefit before defining the mechanism. Reader doesn't yet know what "coherent" means here (no conflicting refreshes? consistent data? visual sync?) or what "Relay Gate" is beyond a name. First read of a coined name with no definition.

2. **"depends on the upstream state"** — "upstream" is undefined. Upstream of what — another panel, an external data source, a previous step in some pipeline? A stranger can't tell if this is panel-to-panel dependency or a single external state everyone reads from. This is the first real stop: the sentence's core claim rests on a term the paragraph never grounds.

3. **"as soon as the gate clears"** — "clears" implies the gate can be blocked, but nothing has said what blocks it or what condition satisfies it. Reader is asked to accept a state-change verb for a mechanism they haven't seen.

4. **"a coordinator — not a queue — so panels never wait on one another"** — this defines the gate by what it isn't, then draws a conclusion ("so... never wait") that doesn't obviously follow. Sentence 2 just said panels wait for the gate to clear — so panels do wait, just not on each other. The "so" reads as a non-sequitur unless the reader already understands the coordinator/queue distinction being invoked to justify it — but that distinction was never explained, only named. This is the sharpest stop in the paragraph: it feels like it's explaining something, but a stranger can't reconstruct the actual reasoning.

5. **"every panel registers with it before the first refresh"** — "registers" is a new undefined mechanism appearing in the closing sentence. What does registering do — does it announce readiness, subscribe to updates, claim a slot? Without that, the sentence describes a sequence of steps ("gate runs first," "panels register," "first refresh") without telling the reader why the order matters or what breaks if it didn't happen.

Net: the paragraph names a mechanism (Relay Gate) and asserts its effects (coherence, no mutual waiting, ordered startup) but never explains the mechanism itself — three load-bearing terms (upstream state, gate clears, registers) are used as if already defined. A stranger finishes it knowing what the Relay Gate is called and what it prevents, not what it does.

---

**What the bare arm shows (the contrast the eval is for):** the loader-fed bare reader caught all
three planted defects in SUBSTANCE — the undefined "Relay Gate", the unfilled "depends on the
upstream state" slot, and it read "a coordinator — not a queue" as a definition-by-denial plus a
non-sequitur — and both smaller terms ("coherent", "the gate clears") besides. What it did NOT do is
the method: no mechanical lints before the read, no blocking/non-blocking verdict on any finding, no
fix pass at all (so neither a fix-from-source nor a recorded question for the person — and, unlike
the eval's predicted red, no invented definition either, because it stopped at diagnosis), no fresh
zero-context reader (the same session that got the audit framing did the reading), and no stated
termination rule — one pass, done.
