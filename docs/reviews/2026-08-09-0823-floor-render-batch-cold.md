# Cold pass — the floor-render batch (third render state + PS5 pathscan promotion + C1F3 floorfleet strip)

**Pass type:** code cold pass (rule-4 queued — the delta applies ruled
decisions, so the applier's judgement produced it).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-06 (see *What the work is*).
- **Who spawned this review:** the principal (Mike), in a session he opened on
  2026-08-09 and pointed at the review queue — rule 4's worked example. His
  words: *"Please do any review work that waiting."*
- **Author's non-involvement:** the taker session authored no part of this
  delta, was neither started nor instructed by the authoring session, and wrote
  this brief as the non-author taker. Rule 4's single criterion is met, and the
  tier was checked at selection.
- **Orchestration shape:** the review runs under an orchestrator holding a
  context partition — the intent-record references are withheld from this brief
  and handed to the reviewer only after its own findings are durably written.

## What the work is

Code landed 2026-08-06, reviewed at HEAD:

1. [`tools/floor.py`](../../tools/floor.py) and
   [`tools/floorfleet.py`](../../tools/floorfleet.py) — a third render state,
   the PS5 pathscan promotion, and the C1F3 floorfleet strip.
2. Their two test files — the suite grew 1178 → 1200 across the batch.
3. [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml) — the bespoke
   pathscan step retired.
4. [`.atelier-floor.json`](../../.atelier-floor.json) — the pathscan scope.
5. The reworded 2026-07-19 line in
   [`docs/decisions/README.md`](../decisions/README.md).
6. The `CHANGELOG.md` entry that landed with them.

## Scope

Widest the work admits: the intent the batch claims to apply, the design of
the render state and the promotion, the code, the tests (a wrong test verifies
nothing), and real behaviour exercised live. **Non-goals:** none narrows the
delta. The reviewer does not decide findings' dispositions; residue joins the
principal's ruling round per house practice.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Is a third render state the right mechanism for whatever it renders?
   Does promoting pathscan into the floor change any consumer's contract?
2. **Correctness & quality** — run the suites and the tools live; check the
   CI workflow change against what the floor actually covers now (did retiring
   the bespoke step lose any coverage the floor did not pick up).
3. **Completeness / harvest** — what should the batch have covered and did
   not; does anything duplicate what `floor.py` / `floorfleet.py` already had?
4. **Security & privacy** — mandatory, at code altitude: unsafe input paths,
   shell-out handling, anything the render state prints that it should not.
   atelier is PUBLIC — verify nothing in the delta or your verdict joins a
   private repo's name to its posture. The house security scanner reads
   pending diffs; this is a landed-delta review, so state the reach case that
   applied.

## Re-run obligation

Re-run, do not read, at least: the full test suites (house invocations live in
[`.githooks/pre-commit`](../../.githooks/pre-commit) — lift them, do not
guess), the suite-count claim 1178 → 1200 at the landing commits, the floor
render in all three states where they can be provoked read-only, and pathscan
under the floor scope in `.atelier-floor.json`.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the intent-record refs are orchestrator-held under the rule-1 context partition, handed over only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/sessions/`, and every prior verdict
in `docs/reviews/`. The intent record for this delta (the rulings the batch
applies) is held by the orchestrator and will be provided on receipt of your
committed findings. Reconcile after, never anchor before.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `FR`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then report; the deferred
references arrive; append a reconcile section and finalise.
