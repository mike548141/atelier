# Cold pass — the reply gate unwired, and the three premise corrections

**Pass type:** doctrine cold pass (REVIEW.md rule 4 — the correction to
`COMMUNICATION.md` was written by the session that diagnosed the failure and
executed the unwiring; the two "rules earned" it states are new doctrine by
function, in the author's own wording).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).
**Status:** BRIEF WRITTEN, REVIEW NOT RUN. The next cold session that passes
rule 4's criterion and the tier bar takes it — see *Spawn provenance*.

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-15 (wt: `plain-reply-unwired-0816`; Opus tier per the commit
  trailer; see *What the work is*).
- **Who wrote this brief:** a cold session Mike opened on 2026-08-15 at about
  1120 UTC with the standing instruction, verbatim: *"As a cold session please
  do any review work, any work that is fable dependent, and write briefs for
  any reviews that need them. If you write the brief then do not run the
  review, that will require another cold review session."* That session
  authored no part of this delta and was neither started nor instructed by the
  authoring session. It wrote this brief from the delta (`git show cd6232b`
  for the four doctrine/tool surfaces below) and the queue pointer only; it
  did **not** open the session record or the board item the pointer names as
  intent records. **One disclosure:** its own session onramp read the tail of
  `docs/SESSIONS.md`, whose last index entry summarises this delta — that
  entry was read before this brief was written and is the reason the intent
  record itself was left unopened. The same session is orchestrating four
  *other* cold passes (the 2026-08-15-103x briefs, written by a different cold
  session) and **stopped** on this one — it did not run this review.
- **Who takes the review:** the next cold session that meets rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier, checked at selection. The taker repeats its own provenance in
  the verdict: how it was spawned, and its non-involvement with the authoring
  session and with the brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling file
  `2026-08-15-1126-reply-gate-unwired-cold.deferred.md` (rule 1's split): the
  intent-record references, the prior-verdict references, and the
  brief-writer's seeded questions. Recommended: the taker runs the review
  under an orchestrator that holds the sibling's bytes and hands them to the
  reviewer only after its findings are durably written. A taker reviewing by
  hand opens the sibling as a deliberate second act after its findings are
  written, and says so in the verdict. Fold in and delete when the verdict
  lands.
- **Adjacent pass, not this one.** The 2026-08-15-1033 brief
  (`communication-floor-cold`) reviews the *earlier* deltas on the same
  surfaces — the enforcement clause as first written (2026-08-09) and the
  repo-plane rescope (2026-08-10). Its verdict, once landed, is a prior
  verdict for this pass and is barred until reconcile like any other. This
  pass reviews what came *after*: the unwiring and the corrections.

## What the work is

Landed 2026-08-15 on `main` as `cd6232b`, merged as `433dc1f`. Reviewed at
HEAD:

1. [`docs/method/COMMUNICATION.md`](../method/COMMUNICATION.md) § *Some of it
   is enforceable* — the enforcement clause now says the reply plane is
   unwired, states how it failed, and states a rule (*a machine-decidable rule
   can still have no machine-deliverable remedy*); the plane-scoping paragraph
   beneath it was retensed and given a survival clause for any future
   collector.
2. [`tools/README.md`](../../tools/README.md) § *`plainscan.py`* — the
   two-planes description and the install stanza's preamble, rewritten to
   describe the reply plane in the past tense with a stop notice and to keep
   the install form "for the record and not to be reinstated without a
   ruling".
3. [`tools/hooks/plain-reply.py`](../../tools/hooks/plain-reply.py) —
   docstring only: an *UNWIRED — DO NOT REINSTALL WITHOUT A RULING* banner and
   a *THE PREMISE THIS FILE WAS BUILT ON, AND WHY IT WAS FALSE* section; the
   *WHAT THIS IS* paragraph re-tensed. **No behaviour changed** — the code is
   as it was, wired to nothing.
4. `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/README.md`
   § *COMMUNICATION.md enforced* — the section preamble retensed and pointed
   at the new ruling item.
5. **The unwiring itself is machine-local** — a hook stanza removed from
   `~/.claude/settings.json` on the principal's machine. It is not in the
   tree. Its *shape* is documented in the tools catalogue and reviewable; the
   live state is verifiable only by reading that file on this machine, and the
   verdict should say whether it was.

The commit message states measurements — a 12-hour transcript window,
24 sessions active, 16 hit, 29 turns blocked, 6 twice, ~123,500 characters
reprinted, a give-up path that fired on 4 of 6 turns — and a mechanism claim:
that a `Stop` hook fires after Claude Code has already streamed the reply, so
a block appends rather than replaces. Both are the author's claims and are
in scope as such.

## Scope

Widest the work admits: the mechanism claim and whether it is established
rather than asserted (the commit says the *previous* premise was asserted in
three places and checked in none — the same test applies to its replacement);
the measurement's method as recorded, since the corpus is private and cannot
be re-run from the repo; whether the corrections say what the mechanism does
and nothing more; the two rules stated as earned and whether the evidence
earns them; what the doctrine now leaves standing (the repo plane, the
"scoped to its reader" ruling, the fail-open trade) and whether each survives
the failure on its own grounds or only by assertion; and what a future session
reading these three surfaces cold will believe and do. **Non-goals — one, and
it does not fence the risk:** the reviewer does not decide any finding.
Doctrine here is self-authored; findings are the principal's to rule on (rule
3), and the destroy-or-repurpose ruling is his and is *not* under review — the
account he will rule on is. Counsel may be recorded, labelled as such.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Is "a `Stop` hook cannot un-print" true of Claude Code as shipped
   today, in every surface the hook ran on (terminal CLI, IDE extension,
   web/desktop app) — and did anyone check more than one? What does the
   claim rest on: documentation, a transcript, an experiment? Does the
   correction over-reach — is *any* rewrite-before-read control impossible,
   or only this one at this hook point? Was unwiring the only remedy the
   evidence supported, or the one the author reached first?
2. **Correctness & quality** — read all four surfaces at HEAD side by side
   with the diff: do they now agree with each other and with the hook's
   actual behaviour? Does anything in `COMMUNICATION.md`, `tools/README.md`,
   the hook, `tools/floor.py`, `tools/plainscan.py` or the tests still assume
   a live reply plane? Run the suites and the floor on both planes at HEAD;
   drive the hook by hand once to confirm the docstring's account of what it
   returns matches what it returns.
3. **Completeness / harvest** — every surface that named the reply plane as
   live: doctrine, catalogue, tests, CHANGELOG (does one exist for the
   wiring, the unwiring, either?), skills, templates, child-facing floor
   blocks, session-onramp text. What did the correction sweep miss? The
   commit says two rules were earned — do they belong where they were put,
   are they stated once, and does anything already in the doctrine say the
   same thing under another name?
4. **Security & privacy** — mandatory. The delta quotes measurements over
   the principal's private transcript corpus and names counts of sessions;
   atelier is PUBLIC — check that nothing in the four surfaces or the record
   surfaces joins a private repo's name to its posture or carries transcript
   content. The unwiring removed a hook that read every reply in every repo
   and kept a state file — say what, if anything, that state file still holds
   on this machine and whether the docstring tells a reader. If the lens has
   no surface beyond that, discharge it in one explicit line with grounds.
   The house security scanner reads pending diffs; this is a landed-delta
   review, so state the reach case that applied.

## Re-run obligation

Re-run, do not read: the mechanism claim itself — establish by experiment or
by cited documentation whether a `Stop` hook block replaces or appends, and
on which surface(s) you tested; the suites and the floor on both planes at
HEAD (house invocations live in [`.githooks/pre-commit`](../../.githooks/pre-commit)
and `.github/workflows/ci.yml` — lift them, do not guess); the hook driven
live with a clean and a rule-breaking payload; the live-install state
(`~/.claude/settings.json` — report presence or absence of the stanza, quote
nothing else); and the tree-wide search for surfaces still asserting a live
reply plane. The transcript measurement cannot be re-run from the repo — say
so, and review the *method* as recorded rather than treating the numbers as
verified.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/` (including the 2026-08-15-1033
communication-floor verdict once it lands), the intent record for this delta,
and the board item `020-…/310-…` (the ruling item, which carries the author's
full account). The sibling `.deferred.md` holds those references and the
brief-writer's seeded questions; open it after your findings are committed.
Reconcile after, never anchor before. A taker whose own session onramp has
already read the `SESSIONS.md` tail discloses that in the verdict.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `RG`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section; fold the sibling in below it and delete the sibling;
finalise. Update the queue pointer
(`docs/roadmap/160-doctrine-review-owed/180-rule-4-review-queued-tier-fable-pass-type-doc.md`)
and rebuild the index in the same commit.
