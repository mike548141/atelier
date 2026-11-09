# Estate-internal context in public records

**Status**: accepted • **Date**: 2026-08-05 (drafted) • **Decided**: 2026-11-08

**Review**: queued — a rule-4 cold pass is owed on the doctrine edit this
acceptance drove (`docs/method/RECORD.md` § *The record is public*); the ⏳
pointer is written when that edit lands, by the landing session.

> **Decided, with its provenance stated plainly.** On 2026-11-08 Mike chose
> *"Type-only for private state"* from the options a session offered him in a
> ruling round. That is an **answer to options a session offered, not a ruling
> in his own words**, and this record does not dress it as one. The option read:
> a private repo's internal state is described by its type only in a public
> record ("a private child was failing a check"); naming a repo in any other
> context stays allowed. It is the posture this draft called **C** (and framed
> as a "variant"). The Decision below is a session's precise statement of that
> pick; where Mike's own words differ, his words win. The places where this
> statement makes a judgement the pick did not spell out are marked
> **(drafter's reading)**.

## Context

`rpi` flipped public on 2026-07-29. Its post-flip cold pass raised **F5**
(minor, deferred to the principal as doctrine-by-function) in two parts:

- **(a) records residue** — a session log naming sibling repos together with
  their scan states;
- **(b) published workflow** — a model-economics document publishing internal
  operating detail as a matter of course.

The atelier roadmap harvested part (a) and under-stated part (b). Both are
restated here from the source finding, because they behave differently and a
single ruling has to cover each.

atelier already holds the **narrow** rule (`method/RECORD.md` § *The record is
public — keep private repos generic*): the regulated class is the **join** — a
private repo's name coupled to its *sensitive* posture (which secrets it holds,
where, exposure history, publication intent, confidential content). That rule
is explicit that naming a private sibling is *not* itself the harm, that
adoption lists and worked examples name children legitimately, and that the
test is whether the name is load-bearing for the lesson.

F5 asks the wider question the narrow rule does not reach: is estate-internal
context in a public record **accepted transparency**, or a records-convention
defect? The ruling binds every repo heading public, not just the one that
raised it.

### What the record actually contains — measured 2026-08-05

Counted over this repo's tracked prose (`docs/`, `README.md`, `CHANGELOG.md`)
at commit `1f026c1`. Sibling repos are counted by name-class here rather than
listed, per the narrow rule this ADR is about.

| Measure | Count |
|---|---|
| Sibling-repo name mentions, all siblings | ~1,030 across ~140 file-instances |
| Mentions naming a **currently-private** sibling | ~270 |
| Private-sibling mentions in **records** | ~96% |
| Private-sibling mentions in **doctrine** | ~4% |
| Candidate name × posture joins, tightened probe | 15 lines |

Three findings follow from the measurement, and each one moves the decision.

**1. The exposure is a records phenomenon, not a doctrine one.** Ninety-six
percent of private-sibling mentions sit in session logs, the session index,
review briefs, the roadmap and its archive. Doctrine — the method and build
layers, the README, the ADRs — accounts for roughly one mention in twenty-five,
and those are the worked examples `RECORD.md` already sanctions as
load-bearing. Any writing friction a convention change creates therefore lands
almost entirely on the highest-volume, lowest-deliberation surface in the repo:
records written at session close.

**2. The narrow rule is broadly holding; what accumulates is the adjacent
band.** A tightened probe for a private sibling's name on a line with
posture vocabulary returns 15 lines, 12 of them index entries in one file. On
inspection these are name × *operational state* — a floor exercised somewhere,
a pin bumped, a scanner run — not name × *sensitive* posture. That is the
greyer band F5 names, and it is consistent with the reviewer grading F5 minor
rather than major.

**3. Retrofit is not available, so any tightening binds forward only.**
`RECORD.md` establishes it in its own words: on a public repo a scrub of HEAD
is not remediation, because scrubbed prose stays reachable in pushed history
forever. The ~270 existing mentions cannot be recalled at any price. This
removes a whole branch of the cost comparison — neither posture implies a
clean-up programme, and any option that seemed to is mis-specified.

### Part (b) is not symmetric with part (a)

For a child repo, publishing internal workflow is incidental — a document
happened to be in a tree that went public. For atelier it is the **stated
purpose**: this repo exists to publish an operating model (ADR 0005; the
README describes the layers as shareable doctrine). A rule that treats
published workflow as leakage would be a rule against atelier existing.

So part (b) needs its own boundary, and the honest one is not *whether*
workflow is published but *whose* workflow. Published **method** — how work is
done, generalised — is the product. Published **operations** — what a
particular named private repo is currently doing, and in what state — is the
residue. That line is not the same as the name-join line, and the ruling
should say whether it is adopted.

## The postures

### Posture A — open-estate transparency

Estate-internal context is publishable by default. The name × sensitive
posture join stays the only bar, exactly as written today. F5 is answered as
*accepted transparency*: the record's resumability depends on concrete names,
the operating model is the product, and the residual is reconnaissance value
of a low order against an estate whose defences are already published by
design.

**Cost.** The reconnaissance surface the 2026-07-29 publication-surface
analysis opened stays open at its current width: a reader can assemble, from
public records, which sibling repos exist and roughly what operational state
each was in on a given date. `publishscan` does not reach it — it judges paths,
not prose — and no scanner can (the narrow rule already declares its own
enforcement as write-time discipline plus review sweeps, nothing stronger). It
also leaves the greyer band permanently un-adjudicated, which is how the
narrow rule came to be breached three times: not because it was unclear, but
because the generic form is harder to write while holding a concrete finding
list in mind.

**What it makes true.** Zero writing friction. Zero migration. The measured
~270 mentions need no disposition. The candidate name × posture scanner in the
anti-slop registry keeps its current narrow specification.

### Posture B — class-level estate-internal detail

Estate-internal context about a *private* sibling goes class-level in public
records: "a child repo", "an infra repo", "one repo in the fleet". Names remain
available where load-bearing for a lesson, which is the existing test, but the
default inverts — generic unless the name earns its place.

**Cost.** Writing friction on every session close, on the surface that carries
96% of the mentions and is written under the most time pressure. That is a
real and recurring tax, and the three prior breaches of the *narrower* rule are
direct evidence the tax gets paid late or not at all. Resumability degrades: a
cold resumer reading "an infra repo" has to reconstruct which one, and the
operating model's whole premise is cold resumability (`RECORD.md`). Enforcement
is unavailable for the same reason as the narrow rule — no scanner can hold
it — so it binds on discipline alone, and a rule that binds on discipline
alone and taxes the writer is the shape most likely to be quietly dropped.

**What it makes true.** The adjacent band closes. Forward-only, so the existing
~270 mentions stand and the record permanently contains two conventions —
which is itself a legibility cost for anyone reading the archive cold.

### Variant C — bind by surface, not by repo (surfaced by the measurement)

Neither posture as framed accounts for the 96/4 split, so the drafter records a
third shape rather than leave the finding buried: doctrine names siblings
freely (worked examples are load-bearing, and the volume is negligible);
**records** go class-level for private siblings' *operational state*
specifically, leaving ordinary naming — adoption, pin bumps, who did what —
untouched.

**Cost.** Narrower than B by a wide margin: it taxes only the sentence that
couples a private name to what its guards were doing, which the probe puts at
roughly 15 lines across the entire history. It asks the writer to hold one
distinction rather than a general reticence, and it gives the candidate
name × posture scanner a specification it could plausibly implement — the
registry item currently blocked on exactly that.

**What it makes true.** Part (a) closes at its measured width; part (b) is
answered by the method-versus-operations line above rather than by silence.
The cost is a more complex rule, and this repo's own doctrine warns that when a
rule keeps being broken the framing is the first suspect — a two-clause rule is
more framing to get wrong.

## Decision

**Posture C: in a public record, a private repo's internal state is described
by its type only.** It binds forward only.

**What must be type-only.** A sentence that says what *condition* a particular
private repo was in at a time. That covers what its checks, guards or scans
showed (passing, failing, which one); its findings and open items; how current
its pin or install was; what it was configured with or holding; its health;
and the work in flight inside it. The repo is described by a *type* that more
than one repo could answer to ("a private child", "an infra repo", "one repo in
the fleet"), never by its name, and never by a description specific enough to
identify it alone **(drafter's reading: a type that only one repo fits is a
name)**.

**What stays allowed, unchanged.** Naming a private repo in any other context:
that it adopts atelier, adoption lists and fleet rosters, who did what and
which session ran in it, a PR or item that concerns it, and an *act* done to or
by it (a pin bumped, a floor installed, a fix landed) as distinct from its
resulting *condition* **(drafter's reading: act versus condition is the line
the pick implies for pin bumps; "bumped the pin in `widget-api`" is an act,
"`widget-api` is three pins behind" is a condition)**. Public repos are
unaffected: their state is public already. Worked examples in doctrine keep
their names where the name is load-bearing for the lesson.

| Allowed (names, acts, roles) | Type-only (private state) |
|---|---|
| "`widget-api` (private) adopted the floor today." | "A private child was failing the secret scan." |
| "Bumped the pin in `widget-api`." | "A private child's pin was three bumps behind." |
| "Session ran in `widget-api` to land item X." | "An infra repo had two open scan findings." |

> **Correction, 2026-11-09.** The sentence above, "Worked examples in doctrine
> keep their names where the name is load-bearing for the lesson", is
> superseded. Mike's pick from options offered on `320/330` (*"Approve all
> 20"*, 2026-11-09, an answer and not a ruling in his words) was that public
> doctrine names no private child in a worked example: it says "a private
> child" (`RECORD.md` § *The record is public*; `PROPAGATION.md` § *The route*
> rule 2). Citations of where a rule was extracted from, adoption lists and
> fleet rosters are "who did what", and stay allowed as stated above. Also
> 2026-11-09 (`020/050`, same kind of pick, *"Treat like any private repo"*):
> the estate-root repo has no stricter rule than this one. The ADR is not
> rewritten; read it with this note.

The narrower rule stands as the stricter floor beneath this one, unchanged: a
private repo's name coupled to its *sensitive* posture (secrets held and where,
exposure history, publication intent, confidential content) stays barred. This
rule adds the milder name x operational-state band the join rule never reached.

**Part (b), published workflow.** Answered by the same line: published
*method* (how work is done, generalised) is this repo's purpose and stays;
published *operations* (what a named private repo is currently doing and in
what state) goes type-only. This is the method-versus-operations line the
Context draws.

**Forward only.** No scrub, no migration, no retrospective disposition of the
~270 existing mentions: pushed history is permanent, and a scrub of HEAD
remediates nothing (`RECORD.md`).

**Enforcement, stated honestly.** The rule binds at write-time discipline plus
review sweeps, as the narrow rule does. A scanner for the whole rule is not
available, because telling a state sentence from an act sentence is judgement.
A narrow advisory aid is plausible (see Consequences).

## Rejected

- **Posture A, open-estate transparency (the name x sensitive-posture join as
  the only bar):** it leaves the reconnaissance surface open at its present
  width. A reader can assemble from public records which sibling repos exist
  and roughly what state each was in on a given date, and `publishscan` judges
  paths, not prose, so nothing stops it widening. It also leaves the greyer
  band permanently un-adjudicated, which is how the narrow rule came to be
  breached three times. Its one real merit, zero writing friction, is bought
  entirely by leaving the band open.
- **Posture B, class-level wording for all estate-internal context about a
  private sibling (generic unless the name earns its place):** it taxes every
  session close, on the surface carrying ~96% of the mentions and written under
  the most time pressure, and the three breaches of the narrower rule are the
  evidence that a tax like that gets paid late or not at all. It also degrades
  cold resumability, the operating model's premise, by turning ordinary
  who-did-what naming into "an infra repo" for no protective gain, since the
  harm sits in the state sentence and not in the name. C taxes only the state
  sentence, measured at ~15 lines across the whole history.

## Consequences

- `docs/method/RECORD.md` § *The record is public* gains the rule, stated once
  and pointing here. The change is self-authored doctrine, so it queues a
  rule-4 cold pass at landing (the **Review** line above).
- A session writing a record asks one question of any sentence about a private
  repo: is this its *condition* (type only) or an *act / role* (name allowed)?
- **Registry scanner item (the name x posture item in the 200 section of the
  board).** Re-specify against this line. A mechanical aid can flag a line that
  puts a private repo's name beside state vocabulary (failing, passing, behind,
  finding, stale and the like) as an advisory prompt to a human, never a gate:
  the act-versus-condition judgement stays with the writer and the reviewer.
- Forward-only. The archive permanently holds two conventions; that legibility
  cost is accepted, since the alternative (a scrub) is unavailable.
- **Estate reach**: the ruling binds every repo heading public, and reaches
  children through the next doctrine pin, not through this ADR.
