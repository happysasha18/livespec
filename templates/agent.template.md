# <agent name> — the agent card (SPEC E-32, INV-184)

Copy this to `<your tree>/.live-spec/agent.md` and fill it. It is this tree's
self-description, read by any agent before it acts on something that might be yours. The
roster naming which agents exist, and where their trees are, lives in the human's personal
profile [E-16]; this card is what a roster line points at. A tree carrying no card is
flagged at founding and at adoption's orient, the same rank a project kind recorded with no
layers carries [A-10, INV-36, INV-135].

The card's permission is the birth ratification itself, so it holds identity and addresses.
Product data placed here is a contract field and takes the contract's permission road
whatever file it sits in [INV-185].

## Name

<the one name this agent answers to — the same name its roster line uses>

## Mission

<what this project is for, standing until the owner changes it. One paragraph.>

## Zones this agent owns

<Each zone on its own line: the areas where this agent decides, builds, and is presumed
competent. A neighbour meeting a question inside one of these zones refers the asker here
and sends nothing [INV-190]. A neighbour needing a capability a zone here owns takes one of
the two channels rather than building its own copy [INV-194].>

- **<zone>** — <what it covers>
- **<zone>** — <what it covers>

Outside these zones this agent reads and writes nothing. Another project's tree is read-only
to it, save the one new file every agent may put in a neighbour's inbox [INV-10].

## Contracts this agent publishes

<One entry per published contract, or the plain word None.>

| contract | artifact path | contract version | cadence |
|---|---|---|---|
| <name> | `<path in this tree>` | <version> | <how often this agent regenerates it> |

<Each contract is authored as a spec surface in this tree's own spec: every field names its
meaning, its measurement window, its aggregation, and its source [E-33, INV-186]. The
artifact publishes nothing until the owner's dated permission opens a field, and credentials
never cross under any permission [INV-185]. The cadence names its watcher: this agent's own
check reds when its scheduled regeneration did not run [INV-41].>

## Contracts this agent consumes

<One entry per contract read, or the plain word None. Each names the version this agent
pinned and the staleness bound this agent declared — how old an artifact may be and still
carry this agent's analysis. The bound is this agent's own number, set independently of the
producer's cadence, and its watcher is the freshness check that reds past it before any
analysis runs [INV-187, INV-41].>

| contract | producer | pinned version | staleness bound |
|---|---|---|---|
| <name> | <agent> | <version> | <e.g. 30 hours> |

## Inbox address

`<this tree>/inbox/` — one new file per item, named `YYYY-MM-DD-<source>-<slug>.md`. A
co-located sender writes the file and stops; a remote sender commits that one file under its
grant and pushes [E-11, INV-10, INV-112, INV-174].

An agent's message here names its birth, and a message that can name neither is declined at the
door [INV-189]. The source lives in the filename, which `inbox/README.md` owns as its one home:

```
inbox/YYYY-MM-DD-from-<my-agent-name>-<slug>.md      the filename names the source

Blocked: <the work of mine that stands until this is answered>   (one birth)
Lived:   <the fault I hit in your zone, and the evidence: what ran, what happened>  (the other)
Need-by: <a date, or none>
Id:      <a stable identifier this message's reply can name>
```
