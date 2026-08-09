# Cold pass — the E6b secretscan advisory tier + the E3 fingerprint carve-out

**Pass type:** code cold pass (rule-4 queued — an application of ruled
decisions; the applier's judgement produced the delta).
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

1. [`tools/secretscan.py`](../../tools/secretscan.py) and
   [`tools/test_secretscan.py`](../../tools/test_secretscan.py) — the advisory
   tier (E6b) and the fingerprint carve-out (E3); that suite grew 89 → 122.
2. [`tools/floor.py`](../../tools/floor.py) and
   [`tools/test_floor.py`](../../tools/test_floor.py) — the advisory-count
   contract; that suite grew 98 → 108.
3. The consumer note in
   [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml).
4. The corrected check row in [`tools/README.md`](../../tools/README.md).
5. The `CHANGELOG.md` entry that landed with them.

## Scope

Widest the work admits: the intent of a two-tier (blocking / advisory) secret
scanner, the carve-out's design, the code, the tests, the consumer contract in
CI and the floor, and live behaviour. **Non-goals:** none narrows the delta.
The reviewer does not decide findings' dispositions; residue joins the
principal's ruling round per house practice.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. An advisory tier is a deliberate softening: does the design keep the
   blocking floor intact, and is the boundary between tiers principled or
   convenient? Does a fingerprint carve-out create a class of secret that can
   never red the floor?
2. **Correctness & quality** — run the suites; run the scanner live against
   scratch fixtures in the scratchpad (never leave the repo dirty); verify the
   advisory-count contract between `secretscan.py` and `floor.py` behaves as
   documented, including exit codes.
3. **Completeness / harvest** — what secret classes does the carve-out
   accidentally widen to; does the README row match actual behaviour; do CI
   and the hook consume the tiers consistently?
4. **Security & privacy** — mandatory and central: this delta *is* a security
   control. Check for bypasses — a real secret shaped to land in the advisory
   tier, a fingerprint-lookalike that is actually live material, ordering or
   precedence defects between allowlists, carve-outs, and tiers. atelier is
   PUBLIC — your verdict must not quote any live-looking token or join a
   private repo's name to its posture; describe classes, never contents. The
   house security scanner reads pending diffs; this is a landed-delta review,
   so state the reach case that applied.

## Re-run obligation

Re-run, do not read, at least: both suite-count claims (89 → 122, 98 → 108) at
the landing commits and the full suites at HEAD (house invocations in
[`.githooks/pre-commit`](../../.githooks/pre-commit)), the advisory tier's
exit-code behaviour, and the fingerprint carve-out against both a genuine
fingerprint shape and a near-miss.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the intent-record refs are orchestrator-held under the rule-1 context partition, handed over only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/sessions/`, and every prior verdict
in `docs/reviews/`. The intent record (the prior intent pass and the rulings
the delta applies) is held by the orchestrator and will be provided on receipt
of your committed findings. Reconcile after, never anchor before.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `AB`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then report; the deferred
references arrive; append a reconcile section and finalise.
