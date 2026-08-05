# Estate-internal context in public records

**Status**: draft • **Date**: 2026-08-05
**Review**: not warranted while draft — a draft binds nothing and its
substance is the principal's to rule (REVIEW.md rule 3, doctrine by
function). The rule-4 pointer is owed by whatever doctrine edit the
acceptance drives, not by this file.

> **This ADR is drafted, not decided.** Mike rules in it. The **Decision**
> and **Rejected** sections are deliberately unfilled — the drafter cannot
> write them without pre-empting the ruling, and `draft` is the only mutable
> state the lifecycle allows (`decisions/README.md`). Both postures are set
> out below with their measured costs, which is the work P6 funded.

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

<!-- Mike's to write. Unfilled by design; see the note under Status. -->

## Rejected

<!-- Completed at acceptance, from whichever postures lose. -->

## Consequences

Stated conditionally, since the decision is open.

- **If A**: `RECORD.md` § *The record is public* is ratified unchanged and
  gains a dated note recording that the wider question was asked and answered
  as accepted transparency, so a future session does not re-open it as novel.
  The registry's name × posture scanner item keeps its narrow scope. P6 closes
  with no doctrine delta beyond the note.
- **If B or C**: `RECORD.md` gains the widened rule, stated at the point of
  use — the session-record and review-brief templates, where the sentence is
  actually written — rather than only in the doctrine chapter, per this repo's
  own rule-grammar finding. The change is self-authored doctrine, so it queues
  a rule-4 pointer at landing. The registry scanner item is re-specified
  against whichever line is ruled.
- **In every case**: forward-only. No scrub, no migration, no retrospective
  disposition of the existing mentions — the permanence of pushed history makes
  that unavailable, and pretending otherwise would be the rounding-up this
  repo's apex forbids.
- **Estate reach**: the ruling binds every repo heading public, which is the
  reason F5 was routed up rather than fixed where it was found. `ros` and
  `faves` are the next flips and inherit whatever is ruled here.
