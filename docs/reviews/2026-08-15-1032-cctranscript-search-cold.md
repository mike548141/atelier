# Cold pass — the `cctranscript --search` build

**Pass type:** code cold pass (rule-4 queued — the build applies a reviewed
design, and the builder's judgement produced both the code and the places it
departed from the design).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).
**Status:** BRIEF WRITTEN, REVIEW NOT RUN. The next cold session that passes
rule 4's criterion and the tier bar takes it — see *Spawn provenance*.

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-09 (see *What the work is*).
- **Who wrote this brief:** a cold session Mike opened on 2026-08-15 with
  the standing instruction, verbatim: *"As a cold session please do any review
  work, any work that is fable dependent, and write briefs for any reviews
  that need them. If you write the brief then do not run the review, that
  will require another cold review session."* That session authored no part
  of this delta, was neither started nor instructed by the authoring session,
  wrote this brief from the delta and the queue pointer only, and **stopped**
  — it did not run the review.
- **Who takes the review:** the next cold session that meets rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier, checked at selection. The taker repeats its own provenance in
  the verdict: how it was spawned, and its non-involvement with both the
  authoring session and the brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling file
  `2026-08-15-1032-cctranscript-search-cold.deferred.md` (rule 1's split): the
  intent-record references, the prior-verdict references, and the
  brief-writer's seeded questions. Recommended: the taker runs the review
  under an orchestrator that holds the sibling's bytes and hands them to the
  reviewer only after its findings are durably written. A taker reviewing by
  hand opens the sibling as a deliberate second act after its findings are
  written, and says so in the verdict. Fold in and delete when the verdict
  lands.

## What the work is

Landed 2026-08-09 on `main` as `0eb03ed`. Reviewed at HEAD:

1. [`instruments/cctranscript`](../../instruments/cctranscript) — the
   `--search <term>` / `--regex` mode and its flags (`--since`/`--until`,
   `--top`, `--materialise`, `--from-archive`, and any others the file
   declares).
2. [`instruments/cctranscript.test.js`](../../instruments/cctranscript.test.js)
   — the suite grew 38 → 62 tests in the landing commit.
3. [`instruments/man/cctranscript.1`](../../instruments/man/cctranscript.1) —
   the manual page's `--search` sections.
4. [`instruments/README.md`](../../instruments/README.md) — the catalogue row,
   the `--materialise` / flag-vocabulary note, and the shared-flags table rows.
5. [`instruments/cctranscript.search.design.md`](../../instruments/cctranscript.search.design.md)
   — the design of record, with a status banner listing where the build
   departed from it. **This document is in-delta and reviewable as such** —
   it is the builder's account of its own departures, not settled ground.
6. The `CHANGELOG.md` entry that landed with them.

The tool reads Claude Code session transcripts on the local machine (live
logs, or the archive mirror). It is an instrument, not doctrine, but it is
shipped in a PUBLIC repo and reads a private corpus.

## Scope

Widest the work admits: the design the build claims to apply and every
departure it declares, the code, the tests, the manual page and README as the
contract users read, and real behaviour exercised live against a transcript
store. **Non-goals:** none narrows the delta. The reviewer does not decide
findings' dispositions; residue joins the principal's ruling round per house
practice.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Read the design of record cold and decide, before reading the
   banner, what a faithful build would look like — then compare. Is each
   declared departure a departure the design should have made, and are there
   undeclared ones?
2. **Correctness & quality** — run the suite; run the tool live against a
   store (a scratch store you construct is acceptable, and safer for
   disclosure — see lens 4); probe the term gate (escaping, non-ASCII, regex
   mode), the date bounds, `--top`'s truncation accounting, and what happens
   on an evicted or unreadable file. Do the tests pin the properties the
   design's DONE conditions name, or weaker proxies of them?
3. **Completeness / harvest** — the design's DONE conditions versus what the
   banner concedes; the flag vocabulary versus the sibling instruments (does
   `--search` reuse their conventions or coin new ones); the manual page and
   README versus the actual flags at HEAD.
4. **Security & privacy** — mandatory, at code altitude, and this instrument
   has a real surface: it searches a private transcript corpus and prints
   excerpts. What does an excerpt carry, where does it go, and could its
   output be pasted into a public record by a session following the house's
   own evidence rules? Regex input handling (catastrophic patterns, injection
   into anything shell-adjacent). Path handling under `--from-archive`.
   atelier is PUBLIC — verify nothing in the delta, and nothing you put in
   your verdict, carries transcript content or private-repo detail. The
   house security scanner reads pending diffs; this is a landed-delta
   review, so state the reach case that applied.

## Re-run obligation

Re-run, do not read: the instrument suite (house invocation lives in
[`.githooks/pre-commit`](../../.githooks/pre-commit) — lift it, do not guess);
the 38 → 62 test-count claim at the landing commit; the manual page through
the house renderer and linter (they differ — the repo's records name both);
and every timing or ratio claim the design banner or the CHANGELOG entry
makes, where a store to measure against exists — and where it does not, state
that plainly rather than reading the numbers as verified.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/`, and the intent record for this delta.
The sibling `.deferred.md` holds those references and the brief-writer's seeded
questions; open it after your findings are committed. Reconcile after, never
anchor before. A taker whose own session onramp has already read the
`SESSIONS.md` tail discloses that in the verdict.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `CS`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section; fold the sibling in below it and delete the sibling;
finalise. Update the queue pointer
(`docs/roadmap/160-doctrine-review-owed/010-rule-4-review-queued-tier-fable-pass-type-code.md`)
and rebuild the index in the same commit.
