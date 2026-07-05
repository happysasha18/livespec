# Wish from the promoter window (2026-07-05): prep live-spec repo for plugin-directory submission

From: promoter session (~/promoter). One file per the inbox rule; apply at your discretion.

Goal: Alexander wants the skills promoted. Two channels chosen (research in
`~/promoter/research/landscape-2026-07-05.md`): the Anthropic community plugin directory
(form at clau.de/plugin-directory-submission) and the hesreallyhim/awesome-claude-code list
(issue-form only, no PRs). Both need small repo changes that only this window may make.

## Asks (all in github.com/happysasha18/live-spec unless noted)

1. **Add `.claude-plugin/plugin.json`** at repo root — observed pattern from an accepted
   community plugin (quickdesign). Draft, adjust freely:
   ```json
   {
     "name": "live-spec",
     "version": "0.1.0",
     "description": "Living-spec methodology pack: five skills (spec-author, product-prover, build-pipeline, communicator, live-spec-base) that take a feature through spec -> prove -> architecture -> tests -> code with formal-verification thinking.",
     "icon": ".claude-plugin/icon.png",
     "author": { "name": "Alexander Abramovich", "url": "https://github.com/happysasha18" },
     "homepage": "https://github.com/happysasha18/live-spec",
     "repository": "https://github.com/happysasha18/live-spec",
     "license": "MIT",
     "keywords": ["spec", "specification", "product-spec", "formal-verification", "methodology", "pipeline", "prover"]
   }
   ```
2. **Add `.claude-plugin/marketplace.json`** (self-referencing, same observed pattern):
   ```json
   { "name": "live-spec", "owner": { "name": "Community" },
     "plugins": [ { "name": "live-spec", "source": "./", "strict": false } ] }
   ```
3. **Icon file** — any simple square PNG/SVG at `.claude-plugin/icon.png` (promoter can
   produce one on request).
4. **Fix dead link**: `product-prover` mirror README links to
   `https://github.com/happysasha18/spec-author` — that repo does not exist (404). Point it
   at `live-spec/tree/main/skills/spec-author` or drop the sentence. (Change lives in the
   mirror-sync source, so it's this window's.)
5. **Mirror README first line**: product-prover mirror opens with "read-only mirror / do not
   open PRs here" — a stranger clicking from a directory sees that first. Consider one
   plain "what this is" line above it.
6. The existing `skills/<name>/SKILL.md` layout already matches what the directory pipeline
   expects — no restructuring needed.

After these land + push, Alexander (human, per both directories' rules) submits:
- plugin directory form: clau.de/plugin-directory-submission
- awesome-claude-code: their "submit a new resource" issue form; one-line factual entry,
  draft: "live-spec — five-skill methodology pack that takes a feature through
  spec → prove → architecture → tests → code, with a formal-verification-style spec
  reviewer (product-prover)."

Promoter window tracks this in `~/promoter/NEXT_STEPS.md` (first story). Ping there when done.
