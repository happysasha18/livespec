# feedback-intake

**Catches anything a person hands back to a project and files it where it belongs, so nothing is ever lost. A [Claude Code](https://claude.com/claude-code) skill, part of the [live-spec pack](https://github.com/happysasha18/live-spec).**

A person looks at what shipped and reacts. They leave a remark, answer an open question, drop a screenshot with a red circle on it, or hand over a log file. **Feedback** is anything a person hands back to the project, at any size, at any moment, through any channel. This skill takes each handed-in item and routes it to one home, in the same session it arrives. The person hears back where it went.

It is the receiving half of a pair. The [communicator](https://github.com/happysasha18/live-spec/tree/main/skills/communicator) skill carries work out to the person. This skill carries what comes back.

This skill ships inside the live-spec pack. Install the pack to get it. Used on its own, this README reads as plain advice about handling feedback.

---

## The rule it keeps

Every item that a person hands in lands in a home the same session it arrives, and the person is told where it went. Nothing waits in the agent's head and nothing is dropped.

---

## The three channels an item can arrive through

- **Spoken or typed.** A remark in the conversation, or a note in a file the person points at.
- **A comment on something shown.** A person answers a decision page or a review page. Each saved answer is a feedback item, and the page's own rules already name its home.
- **A dropped file.** A screenshot, a log, or a document, handed over in the conversation or arriving from an outside session through the project's inbox folder. A file that arrives with no words gets one plain question about what it means. A guess is never written down.

---

## The routing table

Every item takes exactly one route, and every route has a home.

| What arrived | Route | Home |
|---|---|---|
| a request for new behaviour | it is a wish; walk it through wish intake | its queue row |
| a small comment on shown work | fix it the same session; a larger comment becomes a wish | the fixing commit and its journal line |
| an answer to an open question | it closes the question, recorded the same session | the decision archive and the answered row |
| a reaction to a shipped feature | field evidence; the note cites the feature it concerns | a dated line in FEEDBACK.md |
| a workshop snag, such as a flaky tool | the problem ledger | `.live-spec/PROBLEMS.md` |

A **wish** is a request for the product to do something new. **Field evidence** is a plain reaction to a feature that already shipped. The line between the two ledgers is the subject. The product's behaviour goes to FEEDBACK.md. The workshop's own snags go to PROBLEMS.md. Each fact has one home.

---

## The feedback ledger

Some routes had no home before this skill: field evidence, plain reactions, and a wordless file waiting for its question. They get FEEDBACK.md, an append-only file that sits beside the queue at the project root.

Each item is one dated line. The line records when it arrived, who handed it in and through which channel, what it concerns in the product, the item in plain words, and where it went. The file is born with a two-line header. A ledger holding only its header is healthy. It is never trimmed. Dates come from the clock at the moment of writing, never invented.

---

## What's inside

No code and nothing to build. The skill is a single `SKILL.md`, a set of instructions Claude follows. It works anywhere Claude Code runs.

---

## Install

Clone the pack and place its skill folders where Claude Code reads them.

```
git clone https://github.com/happysasha18/live-spec
cp -r live-spec/skills/* ~/.claude/skills/
```

The `feedback-intake` folder now sits at `~/.claude/skills/feedback-intake/`.

---

## Usage

The skill fires on its own the moment a session receives a handed-in item, and at every sweep of the inbox folder. You can also call it by name:

> *"sweep the inbox"* · *"log this feedback"* · *"where does this handed-in item belong?"*

---

## When to use it, and when not

Use it whenever feedback arrives in any form: a comment on shown work, an answered decision page, a file that appears in the inbox, or a user report that the person relays. Use it when you open or add to the feedback ledger, and when you need to decide where a handed-in item belongs.

Do not use it on the agent's own output or on a question the agent asked. Do not use it on something the person merely mentions without handing it in; when it is unclear whether a remark was handed in, one plain question settles it. It never opens a queue row on its own judgment. When an item asks for new behaviour, this skill recognizes it as a wish and walks it to wish intake, where that verdict is made. It also does no reading, scoring, or counting of the collected feedback. That analysis stays with the pack's measurement skills.

---

## One scenario

A person is shown a new export button and writes back: "love it, but the file lands in Downloads and I expected it next to the project." The skill catches the remark the same session. The first half is a plain reaction to a shipped feature, so it becomes a dated line of field evidence in FEEDBACK.md, citing the export feature. The second half asks for new behaviour, so the skill recognizes a wish and walks it to wish intake, which opens a queue row. The person hears one sentence back: the reaction is logged, and the location request is queued. Both halves have a home, and neither is lost.

---

## License

[MIT](LICENSE) © Alexander Abramovich.
