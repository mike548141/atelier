# Cold pass — the board store migration (per-item files + generated index)

**Pass type:** combined doctrine + code cold pass (REVIEW.md rule 4 — the
delta carries self-authored doctrine *and* the mechanism that enforces it).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).
**Status:** BRIEF WRITTEN, REVIEW NOT RUN. The next cold session that passes
rule 4's criterion and the tier bar takes it — see *Spawn provenance*.

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-15 (wt: `board-per-item-0815`; see *What the work is*).
- **Who wrote this brief:** a cold session Mike opened on 2026-08-15 with
  the standing instruction, verbatim: *"As a cold session please do any review
  work, any work that is fable dependent, and write briefs for any reviews
  that need them. If you write the brief then do not run the review, that
  will require another cold review session."* That session authored no part
  of this delta, was neither started nor instructed by the authoring session,
  wrote this brief from the delta and the queue pointer only (it did not open
  the intent record), and **stopped** — it did not run the review.
- **Who takes the review:** the next cold session that meets rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier, checked at selection. The taker repeats its own provenance in
  the verdict: how it was spawned, and its non-involvement with both the
  authoring session and the brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling file
  `2026-08-15-1030-board-store-migration-cold.deferred.md` (rule 1's split):
  the intent-record reference, the prior-verdict references, and the
  brief-writer's seeded questions. Recommended: the taker runs the review
  under an orchestrator that holds the sibling's bytes and hands them to the
  reviewer only after its findings are durably written — the one shape
  honestly called structural. A taker reviewing by hand opens the sibling as
  a deliberate second act after its findings are written, and says so in the
  verdict. Either way the sibling is folded in below the verdict and deleted
  when the verdict lands.

## What the work is

Landed 2026-08-15 on `main` as the series `da6ba70` (claim) → `8ce1bb7`
(toolchain) → `a9abc26` (store migration) → `15d3de2` (doctrine, ADR,
changelog) → `10354e3` (records + this review's queue pointer) → `2f07ee8`
(merge). Reviewed at HEAD:

1. [`tools/board.py`](../../tools/board.py) and
   [`tools/test_board.py`](../../tools/test_board.py) — the generator for
   `docs/ROADMAP.md` and its `check`/`rebuild` modes.
2. [`tools/floor.py`](../../tools/floor.py) — the new `board` entry in the
   floor registry, wired enforced on both planes.
3. [`tools/harvestscan.py`](../../tools/harvestscan.py),
   [`tools/test_harvestscan.py`](../../tools/test_harvestscan.py) and
   [`tools/pointerscan.py`](../../tools/pointerscan.py) — the reach changes
   that let the two item-grammar scanners read a split store and skip the
   generated index. [`tools/README.md`](../../tools/README.md) catalogue rows.
4. The store itself: [`docs/roadmap/`](../roadmap/) — the preamble
   `README.md`, one `README.md` of narrative per section, one file per item;
   and [`docs/ROADMAP.md`](../ROADMAP.md), now a generated index. The
   pre-migration `docs/ROADMAP.md` is the parent of `a9abc26`.
   [`docs/ROADMAP-DONE.md`](../ROADMAP-DONE.md) gained a frozen-store note.
5. Doctrine moved with the mechanism: [`docs/method/RECORD.md`](../method/RECORD.md)
   § *The roadmap*, [`docs/method/CONCURRENCY.md`](../method/CONCURRENCY.md)
   § *Claiming work* (the split-board paragraphs), the repo
   [`CLAUDE.md`](../../CLAUDE.md) read-order line, and the decision record
   [`docs/decisions/2026-08-15-0610-board-store-per-item-files.md`](../decisions/2026-08-15-0610-board-store-per-item-files.md).
6. The `CHANGELOG.md` entry that landed with them.

## Scope

Widest the work admits (REVIEW.md § *What a review actually checks*): the
intent the split claims to serve, the decision as recorded, the store layout,
the generator and check, the two scanners' reach changes, the tests (a wrong
test verifies nothing), the fidelity of the migration itself, and the doctrine
as it will bind future sessions and child repos. **Non-goals — one, and it does
not fence the risk:** the reviewer does not decide any finding. Doctrine here
is self-authored; findings are the principal's to rule on (rule 3). Counsel may
be recorded, labelled as such.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Is one-file-per-item with a committed, checked, generated index the
   right shape for the three problems the ADR names? What does the store now
   assume about how sessions and scanners find work?
2. **Correctness & quality** — run the tools live: `check`, `rebuild`,
   the floor on both planes, harvestscan and pointerscan over the split store,
   the suites. Does the generator's grammar match every item state the
   scanners already speak? Is the index a faithful projection?
3. **Completeness / harvest** — what should the migration have carried and
   did not? Is every line of the pre-migration board accounted for in the
   store? What existing doctrine now says the monolithic thing while the
   mechanism says the split thing?
4. **Security & privacy** — mandatory. atelier is PUBLIC: 118 item files and
   27 narratives were re-homed in one commit — check whether the move surfaced
   or re-linked anything that joins a private repo's name to its posture, and
   what the new store causes future records to carry. If the lens genuinely
   has no surface beyond that, discharge it in one explicit line with grounds.
   The house security scanner reads pending diffs; this is a landed-delta
   review, so state the reach case that applied.

## Re-run obligation

Re-run, do not read: the full suites (house invocations live in
[`.githooks/pre-commit`](../../.githooks/pre-commit) — lift them, do not
guess); the test-count claims at the landing commits; the board check in both
its passing and its drifted state (edit an item file, run `check`, restore);
the migration fidelity claim (4,063 lines → 27 sections / 118 items, index at
253 lines) by comparing the pre-migration board against the store; harvestscan
and pointerscan on the split store; and the claim mechanics on a split board
described in CONCURRENCY (make a claim in a scratch clone and observe what
collides).

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
per-lens answers, findings with stable IDs (prefix `BS`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section; fold the sibling in below it and delete the sibling;
finalise. Update the queue pointer
(`docs/roadmap/010-board-store-migration-per-item-files-mik/050-rule-4-cold-pass-queued.md`)
and rebuild the index in the same commit.
