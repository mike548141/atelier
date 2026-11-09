# Guards — how a finding is governed

A guard is a check that can refuse work: a scanner, a floor gate, a hook. This
doc governs what happens *after* a guard fires — how a finding is assessed, what
response it earns, and on what terms that response may be lowered.

It does not say how to detect things. It says who may decide a finding does not
apply, at what granularity, on what evidence, and how anyone reading the repo
later can see that the decision was made.

**Status:** rebuilt 2026-08-05 from Track F / F1, on the frame Mike named
2026-08-02 and the FG1–FG6 rulings of 2026-08-03. Self-authored doctrine — its
rule-4 review is queued, not discharged.

## The intent this serves

Mike, 2026-08-05, on granting a named exception, narrowing a scanner, or
reducing scope:

> **(a)** as specific or narrow an allowance as possible, so it only applies to
> what we want it to and other things don't get excluded by mistake ·
> **(b)** it must be clearly seen, recorded and understood — things fail noisy;
> ideally it fails noisy as it is scanned, and *then* the exceptions are applied
> to remove the expected and explicitly accepted noise · **(c)** it must have a
> clear reason recorded, so we can tell who allowed it, why, and when.

Three requirements — **narrow, noisy, reasoned** — joined by a fourth below:
**declared**. All four are requirements on every guard in the estate, not
preferences. The rest of this doc is the model that makes the first three
enforceable rather than aspirational; the fourth's check is funded and not yet
built (its homing, below).

### The fourth requirement — declared (Mike's ruling, 2026-08-17)

A fourth joined them, from the posture at `PRINCIPLES.md` §10: **engineer for the
failure being cheap, not for the failure being impossible, and measure the
posture by what you are free to do.** Ruled as a *test guard work has to pass*
rather than a stance held beside it, with the consequence stated to him first —
that some already-landed guards would fail it.

Every guard declares which of two things it does:

| | What it does | What it costs |
|---|---|---|
| **Makes the failure cheap** | The bad event still happens and is survivable — recoverable, rotatable, restorable, reversible | Building the recovery |
| **Forbids the act** | The bad event is prevented by removing the ability to perform it | Freedom of action, permanently |

**Both are legitimate answers. The defect is not declaring which** — and that is
the requirement, because an undeclared choice cannot be reviewed, re-costed, or
argued with. Prevention is correct wherever the recovery genuinely is not
buildable; what is never correct is reaching for it *by default* and calling the
result strength.

🔑 **This is the standard the `why` field was missing.** Every registry entry
already carries a reason that is printed and compared to nothing — the finding
filed against this estate's own guard architecture. A reason with no standard
behind it is a sentence; the same reason answering *cheap-failure or forbid-the-
act* is a claim someone can test. The estate demanded a reason for **weakening** a
guard and no reason for **building** one; this closes that asymmetry from the
build side.

🏠 **The home (the principal's ruling, 2026-08-23).** The declaration lives in
the **floor registry, beside the `why` field** — one standard, folded with the
wider declaration scheme of board item `115/120` and funded there as one item:
the slot, its format (cheap-failure or forbids-the-act), and the check that
reads it land together. Until that lands, the requirement binds new guard work
as a review question, not a machine check — and for non-guard designs the
situation test's "say which you chose" homes in the existing `review:` line.

⚖️ **Two limits, so the requirement is not read as a licence.** A test arriving
after the work is grounds to **declare**, never grounds to unwire a working gate
on the author's own judgement — a guard that fails this test is a *finding for the
principal*, not a revert. And declaring "forbids the act" is not a failure grade:
much of this estate's floor is prevention, deliberately, and the honest reading of
this requirement is that it makes that visible rather than that it condemns it.
The pass over the open board is queued rather than done, precisely so nothing is
re-litigated in the sitting that wrote the rule.

### Choosing between them — the side of the boundary the writer is on

The fourth requirement says to declare *which*; this is how to pick, at the
moment of building one. **The side of the boundary the writer is on decides
it.**

- At a **construction site inside your own code**, where you control the
  writer: **forbid.** There is no recovery to build, because a wrong label is
  already in the reader's hands before anyone could notice.
- At a **read site**, where the writer is a future build or another producer
  you do not control: **make the failure cheap.** Carry the unrecognised thing
  through, unlabelled.

This is why one subsystem can give *opposite* answers to the same validation
question without contradicting itself: a classifier that raises on an unknown
kind where it builds its own labels, and its grouping counterpart that files an
unknown kind as `unclassified` where it reads another producer's. Without the
rule that reads as an inconsistency, and a future session would be right to try
to "fix" one of them.

Grounded in two parallel child sessions that reached it independently on
2026-08-17, filed through `PROPAGATION.md` § *Pointing up* as `320/020`. Mike
adopted it on 2026-11-09 as a short companion to the fourth requirement (his
pick from options offered; an answer, not a ruling in his words). ⚠️ **Not yet
audited:** whether atelier's own guards obey it, and which would fail it, is
unmeasured. Like the fourth requirement it binds new guard work as a review
question, and a guard found to fail it is a finding for the principal, not a
revert.

### Declare the threat model — who is it protecting whom from

A guard also declares **who it protects, and from whom.** Almost every guard
answers one question: *a reader, from a bad artefact* (a stale index, a
duplicate key, an incomplete prior artefact, a leak). Few know that another
**writer** exists, and nobody notices, because a single session never meets the
other case. Six instances in one evening across three parallel sessions, which
the filer called a rate rather than a level, so a design finding rather than a
discipline one:

- a peer's staged path lands under your commit message (`CONCURRENCY.md`
  § *The trigger* owns this one);
- a check that reads the **worktree** fails your unrelated commit on a peer's
  uncommitted edit (reproduced here by reading `tools/floor.py`'s registry:
  most hook-plane checks render absolute worktree paths);
- a guard reading only the staged column of `git status --porcelain` misses
  the unstaged twin, so `reset --hard` silently reverts a change nobody
  staged (reproduced in a scratch repo: a symlink a tool repoints stages
  nothing, and `git diff --cached --name-only` is empty);
- a blocking chain in which no single link was wrong (the strongest argument
  for worktree-by-default).

Declare the writer the guard assumes, so that a guard reading one plane says so
and a reviewer can ask what a second writer does to it.

🛑 **The pathspec caveat is not detachable.** `git commit -- <paths>` commits
only the named paths and leaves every other index entry staged and untouched,
a real third option beside *commit the sweep* and *take a worktree*. Its
safety came entirely from **knowing whose the other paths were**. The test is
not "the paths are foreign", it is "the paths are identified": a session
working alone cannot meet it, and without the precondition the technique lets a
session commit *around* a hazard it has not understood.

Filed as `320/050` from a private child on 2026-08-19; Mike approved it on
2026-11-09 (his pick from options offered, not a ruling in his words). Like
the fourth requirement it is a review question today; where its declaration
lives (the registry slot of `115/120`, or beside it) is **not decided here**.
Whether the shared-checkout hazards already recorded in `CONCURRENCY.md`
(absorbing a peer's work with a wide add; destroying a peer's hunks with a wide
revert) are the same finding at guard-design level is likewise open.

## What a finding is assessed on — three axes

A finding carries three independent assessments. They were collapsed into one
field for most of this estate's life, which is how a field named `severity` came
to hold confidence.

| Axis | Question | Who can answer |
|---|---|---|
| **Identification confidence** | Is this really the thing I think it is? | The guard, by construction |
| **Probability of harm** | Given it *is* that thing, how likely is harm? | The repo, sometimes mechanically |
| **Impact of harm** | If harm lands, how bad? | The repo, almost always |

**Undeclared axes default to worst-case.** A model that demands three
assessments per finding will be ignored, and an ignored model governs nothing.
Declaring nothing costs nothing and changes nothing; the axes exist so that
someone *with grounds* can say more, not so that everyone must.

Probability of harm is measurable for credentials — rotated, expired, scoped to
nothing — and close to unmeasurable for personal data: there is no validity
check for an address at rest. That asymmetry is real and is not a defect in the
model; it means the credential half of the boundary can earn declarations the
personal-data half mostly cannot.

### Assessment is not response

Three axes describe the finding. The **response** — block, report, or stay
silent — is computed from them and is a separate thing. Keeping them separate is
what lets a response change without anyone editing what the guard believes, and
it is how prior art does it too.

### Prior art — verified at pickup, not inherited

Per the FG4 ruling, checked against the sources on 2026-08-05 rather than
carried over from the review that proposed them:

| Ours | Semgrep | CodeQL | CVSS v4.0 |
|---|---|---|---|
| Identification confidence | `confidence` (low/medium/high) | `@precision` (low → very-high) | — |
| Probability of harm | `likelihood` | — | Threat group (Exploit Maturity) |
| Impact of harm | `impact` | `@security-severity` (0.0–10.0) | Base impact metrics |
| Response | `severity`, from likelihood × impact | `@problem.severity` (error/warning/recommendation) | — |
| Repo-declared adjustment | — | — | Environmental group |

Three things fall out of the check, and two of them the review did not have:

1. **Semgrep carries the full three-way split as distinct fields**, and computes
   severity from likelihood × impact. The review claimed only that confidence
   and severity were distinct there. The frame is more exactly prior art than
   the pass that endorsed it knew.
2. **CodeQL separates assessment from response explicitly** — `@precision` and
   `@security-severity` describe the finding, `@problem.severity` says what to
   do about it. That is the separation above, already shipped by someone else.
3. **CVSS's Threat group is defined as the metrics that "change over time"**,
   and its Environmental group is the deployer adjusting severity for their own
   asset importance and compensating controls. Repo-declared impact is the
   environmental score in another vocabulary — and the fact that time-varying
   metrics are quarantined into their own group is independent grounding for the
   expiry rule below, which this estate had reached on its own reasoning.

We use our own words in the estate's voice, but they are translations, not
inventions. An adopter who knows any of these three already knows this model.

## Granularity — the axis that was doing silent work

The estate governs findings at three levels. Naming them is what makes rule (a)
checkable, because "as narrow as possible" is meaningless without a scale.

| Level | Mechanism | Reaches |
|---|---|---|
| **Line** | `<guard>:allow: <reason>` marker | One line, in the file it concerns |
| **Check** | floor `advisory` / `disabled`, ignore-file glob | A check, or a path, across the repo |
| **Repo** | not wired, adopt mode, bypassed hook | Every finding the guard would make |

**Rule (a) in operational form: use the narrowest level that covers the case,
and the narrowest scope within that level.** A line marker that exempts a whole
file, a path glob that exempts a tree to quiet one file, a disabled check that
exempts a repo to quiet one path — each is a defect to fix, not a style
preference, because everything else inside the widened scope goes unguarded
silently and nobody chose that.

Within a level, scope narrows further by *rule*: a line marker written for a
false-positive email must not also exempt a credential on the same line. A guard
with more than one rule therefore supports rule-scoped allowance, and an
unscoped allowance is the deliberate whole-line case, not the default.

**A marker's grammar fails closed** (Mike, 2026-11-09: *"Strict, with a warning
period"*). A scoped marker whose scope is broken — no reason after it, a space
or a stray character inside the scope, a trailing comma — used to be read as the
*unscoped* form with the scope word for a reason, so it quietly exempted every
rule on the line: wider than its author named, on every guard, both boundary
guards included. It is now a *mention* and exempts nothing. To let a repo find
and fix its own, the shared reader (`tools/allowmarker.py`) honours such a
marker as before until `MALFORMED_GRACE_UNTIL` (2026-12-09) and warns about it
on every run; from that date it exempts nothing. A marker inside an inline code
span is likewise a mention, the safe way to document the syntax. The grammar,
and which scope words each guard takes, are in `tools/README.md` under *Allow
markers and ignore files*.

## Acceptance and deferment are different things

One spelling covered both for most of this estate's life, which is how
advisories with no end date became a decay problem.

- **Acceptance** — this finding does not apply, indefinitely. Carries a
  **reason**. No expiry, because nothing about it will change.
- **Deferment** — this finding applies and is not fixed *yet*. Carries a reason
  **and an expiry**. The expiry is the whole point: a deferment that cannot
  lapse is an acceptance that never admitted what it was.

Either one also records **when it was granted**: the date, always, acceptance
and deferment alike; an expiry only where the claim can rot. (Mike's 2026-08-09
restatement as the board records it, not verbatim: the cold pass on the C5
item, C5R9, found the text above did not yet say so. The three repo-wide
opt-outs in the estate already practise it through dated ADRs.)

The two already exist at different granularities by accident rather than design:
a line marker is pure acceptance, a floor advisory is pure deferment. Now they
are distinguished on purpose, at every level. A repo-level adopt mode is a
deferment. An ignore-file glob for a scanner's own test fixtures is an
acceptance.

**One kind of finding takes no acceptance at all** (160/790 HX3). `sizescan`'s
cold-content gate, a completed `[x]` item on the hot-path roadmap, is ruled
*"Never allow it"*, so no marker and no ignore-file glob exempts it: a glob over
a roadmap exempts nothing, and the run names it inert. The remedy for a tracked
fixture roadmap that carries `[x]` lines is to fence them (a `[x]` inside a
fenced code block is a quoted example, not an item) or to name the file
something other than a roadmap. A roadmap under a store-named directory
(`sessions/`, `reviews/`, `decisions/`, `archive/`, `_archive/`, `intake/`) is
not read for cold content, and the check's suppressed line counts those files.

### Who may move a deferment's date: mandate or default

A deferment's expiry is sometimes set by the principal for the whole fleet,
as a `review-by` the children are held to. Such a date is one of two kinds,
and the kind decides what a child may do with it. Mike's rule (2026-08-09):

> If I specifically said all child repos must do X by date Y then they must
> do it by that date, but the child repos may set an earlier date or argue
> for an exemption to something that should not apply to them. If I set a
> date as a default then the child repo could set an alternative date for
> before, the same, or after.

- **Mandate.** The date binds the whole class. A child may **tighten** it to
  an earlier date, or **argue for an exemption**. It may never set a later
  date. (The house's reading of the quote: the argument travels up the route
  `PROPAGATION.md` § *Pointing up* gives, and an exemption the principal
  grants is recorded in the child, by § *The layer-override rule*.)
- **Default.** The date seeds the value. A child may set an **earlier, the
  same, or a later** date of its own. (The house's reading: a later date
  needs no ruling, and still carries the reason every deferment carries,
  § *Provenance, not direction*.)

**The kind is a label the checkers read, and it lives beside the date.** A
dated advisory in `.atelier-floor.json` takes an optional
`"kind": "mandate"` or `"kind": "default"` next to its `review-by`
(Mike's answer, 2026-11-09, to the options a session offered on the cold
pass on this subsection: *"Add a readable label"*). `tools/floor.py` validates
it and shows it on the floor line and in `--json`; `tools/floorfleet.py` shows
it on the board. Two things follow from the label being there:

- **An unlabelled date reads as a mandate**, the stricter reading, until the
  principal says otherwise (§ *The layer-override rule*: on a live
  collision the stricter reading wins). The board says "date kind not
  recorded" aloud. A date ruled before the label existed has no kind on
  record; when its kind matters, ask, and record the answer as the label,
  with the date it was ruled.
- **A mandate's date moving later is reported at the commit that does it.**
  On the hook plane `floor.py` compares the staged `review-by` with HEAD's
  and prints a line when it moved later on a date that was a mandate or
  unlabelled. HEAD's label decides, so relabelling in the same edit does not
  escape it. It reports and never blocks. What it cannot see is the *house's*
  date, because no tool holds one: a fleet-wide declaration of the house's
  dates, which the board could compare each child against, is not built.

**A ruling that sets a date for the fleet names its kind**, so no later pass
has to work out after the fact which one was meant. *Scope:* this is for dates
the principal sets for the whole fleet. A date a child sets for itself, with
no fleet date behind it, is a deferment under § *Provenance, not direction*
(declared, reasoned, principal-visible) and carries a label only if the child
chooses one. A pending-upstream line (`PROPAGATION.md` § *Pointing up*) expires
on an event, the next pin bump, so it has no date to label. A fleet horizon a
session set without the principal has no kind until one is asked for.

*Grounding:* the C1b `review-by` horizon of 2026-09-01. Two repos that
migrated themselves had set later dates, and nothing said whether the house
date was a ceiling. Mike ruled it a **default** (2026-08-09), so the later
dates stand. An unnamed date is the gap this closes. The sentence about a
date ruled before this rule was written is the run's addition (2026-10-03),
not Mike's.

## Provenance, not direction

The E6d(i) ruling (2026-07-29) was **escalate only**: impact may raise a finding's
response, never lower it. FG2 counselled replacing that with a provenance
constraint, and Mike ruled it adopted as a **working hypothesis to test at
design, not inherit**. This is the test and its result, and **Mike confirmed it
on 2026-11-09** (below).

**The test.** Does the estate already contain a lawful downward lane? If it does
not, escalate-only is a live constraint and should stand. If it does, then
escalate-only is already false in practice and is protecting nothing that a
better-stated rule would not protect.

**The result: it does, in three places, and always has.** An allow-marker with a
reason lowers a blocking finding to nothing. An ignore-file glob does it for a
path. A floor `advisory` with `why` + `review-by` does it for a whole check.
Every one of them is a downward move, and every one is legitimate. Escalate-only
never described this estate; it described the *tool's* authority, in words that
also forbade things the estate does daily and correctly.

**So the invariant is not direction. It is provenance:**

> A guard may never lower its own response on its own judgement. A **declared,
> reasoned, principal-visible** act may — and where the claim is one that can
> rot, it carries an **expiry**.

Four conditions, and all four bind:

1. **Declared** — written down in the repo, not decided in someone's head or in
   a session that ended.
2. **Reasoned** — the reason travels with the declaration, in the place a
   reviewer reads it. This is rule (c).
3. **Principal-visible** — a person can see the whole set of live allowances
   without going looking. This is rule (b), and it is the one the estate has
   least of.
4. **Expiring, where the claim rots** — "this credential is rotated" is a claim
   about the world that decays; "this line is a test fixture" is not. Deferment
   expires; acceptance does not. CVSS quarantines its time-varying metrics for
   the same reason.

What E6d(i) was protecting survives intact: a "this one doesn't matter" lane
decided by the tool stays forbidden, and that was always the real risk — the
estate has been wrong that way before. What changes is that the taxonomy now
describes what the estate actually does, instead of forbidding it in theory
while doing it in practice.

### Ruled 2026-11-09: a repo may lower a check's response, declared and expiring

Asked whether the provenance model should replace E6d(i), Mike answered
*"Allow if declared + expiring"*. In operational terms:

> A repo may lower a check's response **only with a written reason and an end
> date, visible in the fleet view**. The tool never lowers a response on its own
> judgement, and a lowering with no end date is not a lowering this model
> allows.

This **replaces E6d(i)'s wording** ("impact may only raise a response, never
lower it") with that rule; E6d(ii) repo-declared and E6d(iii) computed-severity
are untouched. It is stricter than condition 4 at the *check* and *repo* levels
of [Granularity](#granularity--the-axis-that-was-doing-silent-work): there the
end date is always required, not only "where the claim rots", because a check
that is quieter than its default is a deferment whatever it is called. A *line*
marker and an ignore-file *glob* stay acceptances: a reason, no end date, since
what they say about one line or one path does not decay.

Where each lowering stands against the rule today, so the gap is a list and not
a feeling:

| Lowering | Reason | End date | In the fleet view |
|---|---|---|---|
| floor `advisory` (a check reports, does not block) | required (`why`) | required (`review-by`), goes red when it passes | yes: dated, and red when expired |
| floor `disabled` (a check is off) | required | **none yet** | listed with its reason, no date |
| floor `scope` / `flags` (a check looks at less, or is tuned) | required (`why`) | none: ruled a permanent fact about the repo (2026-07-28) | not as a lowering |
| line marker, ignore-file glob (acceptance) | required | none, by design | counted in the scan's suppressed line |

**One check is barred from the `advisory` row** (160/790 HX1, the principal,
2026-11-09: *"Bar it; nova converts"*). `sizescan` enforces the board's design:
the main board is a short list of work and its state, and the detail of each
item sits in a file of its own, never in a flat running log. His ruling on that
was *"Never allow it"*, and a report-only form is a way to allow it with the
gate still printing, so it is the one lowering the general rule above does not
give this check. From 2026-12-09 an `advisory.sizescan` declaration, however
reasoned and dated, is a config error and the floor blocks; before that date the
declaration still works and the check's line on the floor board names the date.
A specific "never" beats the general "declared and expiring". `disabled` is not
what he ruled on and stays open with its reason.

The `disabled` row is the one place the ruling and the machinery disagree, and
`scope` / `flags` need a decision on whether narrowing counts as lowering a
*response* or is a separate axis. Neither is built or decided here; both are
open follow-ups to the board item that carried the ruling (`020/170`).

## Fail noisy, then subtract

Rule (b), stated as machinery, because it is the requirement the estate has
built least of.

**The finding is produced before the allowance is applied, and the subtraction
is reported.** A guard that suppresses silently produces the same output for
"nothing matched" and "forty things matched and all were exempted" — and those
are opposite states of the world. The second is where an allowance quietly grew
past what anyone approved.

Every guard therefore:

- emits its clean result with a **count of what was suppressed and by which
  mechanism** — line markers, path globs, disabled rules — never a bare tick;
- names any **scope reduction taken at invocation** (a disabled rule, a narrowed
  path set) in its own output, because a reduction nobody can see is a reduction
  nobody reviewed;
- keeps the suppressed set **retrievable**, so the question "what is this repo
  currently not looking at" has an answer that does not require reading every
  file.

A repo's live allowances are a standing, reviewable inventory. That inventory is
also, unavoidably, a map of where the guards are not looking — so on a public
repo it is itself part of the publication surface, which is the boundary
`publishscan` exists to hold.

## Who, why, when

Rule (c) asks for all three. The reason is written; **who and when come from
version control**, which records them more reliably than a hand-maintained field
and cannot drift from the truth. A guard that demanded an author field would be
asking someone to retype what `git blame` already knows, and it would go stale.

*Narrowed 2026-11-09 for one manifest (`160/980`).* Mike's 2026-10-03 words
(ADR `2026-10-03-0641`) ask that every exception record who created it (a
session id, and whether he ruled or an agent chose) and when, and measured that
git cannot name either. For `.leakscanbinaries` he answered on 2026-11-08 that
each line records who allowed it and when, so its lines carry `by=`, `session=`
and `on=` beside the reason. Everything else here is as written until the
exception register (`110/100`) replaces it.

The requirement is therefore: **a reason, in the declaration, on the line or in
the file a reviewer reads** — and never in a location the exemption itself makes
unreadable. An exemption whose reason lives inside the file that the exemption
stops anyone from scanning is an exemption nobody will ever review.

## Visibility, and what this model owns

**In scope** (FG1 asked for an explicit answer either way): a repo's visibility
is an input to the **response** — the same environmental adjustment CVSS names,
where the deployer's context changes what a finding earns. A public repo is a
different risk position from a private one holding identical content, and the
model owns that rule.

**Not in scope:** the *mechanism* — declaring visibility, cross-checking it
against the platform, and treating a stale declaration as a finding. That is
**P3**'s build. The rule lives here; the plumbing lives there; neither builds a
second original of the other.

## Side-stepping — the family that governs nothing

A guard can be defeated without any allowance being declared at all: **not wired
in**, **overruled**, or **ignored**. None of these is an assessment, so none of
them is governed by the axes above — which is exactly why they are the dangerous
class. A guard that was never installed produces no findings to accept.

The rule: **side-stepping must be observable.** A bypass is a recorded event or
it is not a bypass, it is a hole. Making the escape hatch painful is not the
answer — that invites worse workarounds — but making it *silent* is how a floor
becomes decoration. `C4` is the open build.

### Which commits the hook plane reaches

The hook plane is git's `pre-commit` hook, and git calls that hook for an
ordinary `git commit` only. Measured on git 2.50.1 (roadmap `115/340`):

| How the commit is made | Client-side hook that runs | Can it refuse? |
|---|---|---|
| `git commit` | `pre-commit` | yes |
| `git merge` that stops on a conflict, finished by `git commit` | `pre-commit` | yes |
| `git merge --no-ff` (a clean automatic merge) | `pre-merge-commit` (atelier ships it beside `pre-commit`; it hands over to the same checks) | yes |
| `git cherry-pick`, `git revert`, `git rebase` (including `rebase --continue` after a hand-resolved conflict) | none | **no** |

A rebase or cherry-pick writes commits whose bytes no client-side plane read,
and a hand-resolved rebase conflict lands genuinely new content that way.
`post-rewrite` can warn after a rebase but cannot refuse. **Those commits are
checked by CI only**, so a check that exists only at the hook (a local,
credentialed tripwire CI cannot run) does not cover them at all. `--no-verify`
skips `pre-commit` and `pre-merge-commit` alike; it is a bypass, and the
side-stepping rule above applies to it.

## A rule with no home is not a rule

A guard's family above is *rules that exist and can be defeated*. This is the
tier beneath it: **a rule that was never written to a surface anyone reads does
not govern anything, however firmly it was stated** (the principal's ruling,
2026-08-17).

The shape is specific and it looks like diligence, which is why it survives. A
session hits a real failure, reasons well about it, and states the rule it
earned — in a commit message, in a session record, in a board item. All three
are records. **Rule 2 bars a cold reviewer from reading records**, and no
onramp loads them, so the rule reaches exactly the readers who already knew it
and none of the sessions it was written to govern. It is not lost, and it is
not live either. Two of the three recorded instances were found by a reviewer
looking for something else.

The test, applied when a session says *this is a rule we've now earned*: **name
the surface a future session reads it on.** Doctrine, a tool's docstring, a
template, a skill, a check — a place that is loaded or enforced, not a place
that is archived. If the honest answer is "the commit message", the rule is not
yet a rule and the work is not yet done; queue the homing or drop the claim.

**And the surface may not be in this repo.** Where the rule a session earned is
the *house's* rather than this repo's, "queue the homing" means filing it in the
parent, and the route — how to tell the two apart, where the finding goes, and
what the child may hold while it waits — is `PROPAGATION.md` § *Pointing up*.
Writing it into the local onramp instead satisfies this test's letter and
defeats it: the rule is now on a loaded surface, and it is loaded for exactly
the sessions it does not govern. That route opens with the check this test does
not make — *read the parent's actual file, never your own inlined summary of it*
— because a rule the parent already owns cannot be homed anywhere, and a session
reasoning from the summary cannot tell the difference (grounded 2026-08-18; the
instance is in that section).

This is why `RECORD.md`'s § *An approval is not the whole ruling* sits in
doctrine and not only in the incident that earned it: the incident is the
evidence, the doctrine surface is the rule. Same relationship for every entry
in this file.

**The principal's own words are subject to the same test.** An instruction he
typed mid-turn, or chose in the question box, is as binding as one in the
opening prompt, and as homeless if nothing writes it down (`RECORD.md` § *What
the principal said arrives three ways*).

## When a guard is wrong

A false positive is not an allowance case. It is a defect in the guard, and the
fix belongs to the guard.

This is a **specialisation of `PROPAGATION.md`'s resolved-upward rule**, not a
second original of it: children point up, the parent never points down for
truth. What the specialisation adds is the operational route — where to file,
what evidence to carry, who triages — which is what was missing when false
positives kept being discovered ad hoc and fixed locally.

**Every allowance written for a guard defect is debt, and should be recorded as
such.** A repo that accumulates markers against a systematically wrong rule has
been trained to stop reading that guard's output — which costs more than the
false positives ever did.

## Adoption — the case a steady-state model would miss

A repo whose existing content already fails a guard **cannot commit the change
that installs the guard.** First contact is not steady-state operation, and a
model built only for steady state meets it as an afterthought — twice, so far,
resolved by undocumented one-time bypass.

Adoption is a **deferment at repo granularity**: the guard installs
advisory-first, with a reason and an expiry, and tightens on re-baseline. That
is a governed act with an end date, where a bypass is an ungoverned one with
neither. `C3` is the open build.

## What this model does not decide

Stubbed honestly rather than filled in:

- **The response function itself** — what confidence × probability × impact
  computes to, in what units. E6d(iii) owns it; this doc says only that it is
  computed and that assessment and response are separate.
- **How probability of harm gets declared** for credentials mechanically
  (validity checking, as GitHub secret scanning does it). Named as reachable,
  not built.
- **The false-positive route's operational detail** — the filing form and triage
  owner. The rule is settled here; the route is not built.

## Related

- `PRINCIPLES.md` §10 — the posture the fourth requirement comes from, and the
  *prevention-or-cheap-failure* situation test that applies it to a design
- `PROPAGATION.md` — resolved-upward, and enforcement by call not copy
- `build/REPO-STANDARD.md` — a child may narrow, never contradict; the
  `.atelier-floor.json` seam where a repo declares what it decides
- `SECRETS.md` — the boundary scanners' over-flag posture, which this model
  governs the exemptions to
- `REVIEW.md` — the rule-4 independence this doc's own review is queued under
