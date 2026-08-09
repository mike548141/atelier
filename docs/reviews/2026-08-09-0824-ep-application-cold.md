# Cold pass — the EP application (enforcement-is-called-not-copied, applied)

**Pass type:** code cold pass (rule-4 queued — an application of ruled
decisions; the applier's judgement produced the delta).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-06, and the session that landed the 2026-08-09 follow-up on the same
  surfaces (see *What the work is*).
- **Who spawned this review:** the principal (Mike), in a session he opened on
  2026-08-09 and pointed at the review queue — rule 4's worked example. His
  words: *"Please do any review work that waiting."*
- **Author's non-involvement:** the taker session authored no part of this
  delta, was neither started nor instructed by the authoring sessions, and
  wrote this brief as the non-author taker. Rule 4's single criterion is met,
  and the tier was checked at selection.
- **Orchestration shape:** the review runs under an orchestrator holding a
  context partition — the intent-record references are withheld from this brief
  and handed to the reviewer only after its own findings are durably written.

## What the work is

Code and templates landed 2026-08-06 plus a 2026-08-09 follow-up on the same
surfaces, reviewed at HEAD:

1. [`tools/floor.py`](../../tools/floor.py) and
   [`tools/floorfleet.py`](../../tools/floorfleet.py).
2. [`tools/pre-commit.sample`](../../tools/pre-commit.sample) and
   [`.githooks/pre-commit`](../../.githooks/pre-commit).
3. [`.github/workflows/floor.yml`](../../.github/workflows/floor.yml) and
   [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml).
4. [`docs/build/templates/workflows/floor.yml`](../build/templates/workflows/floor.yml)
   and
   [`docs/build/templates/CONTRIBUTING.md`](../build/templates/CONTRIBUTING.md).
5. [`docs/decisions/0008-enforcement-is-called-not-copied.md`](../decisions/0008-enforcement-is-called-not-copied.md)
   — Decision 6 and the Consequences control clause.
6. The four test files — the suite grew 1164 → 1178 across the application.
7. The `CHANGELOG.md` entry (2026-08-06), and the 2026-08-09 follow-up:
   `tools/floor.py` validate + `tools/test_floor.py`, the legacy-spelling
   exemption removed for never-softened scanners (delta widened per the
   landing-commit rule).

## Scope

Widest the work admits: whether the application matches the decision it
applies (ADR 0008 is in the delta and is readable now — the *verdict* that
ruled on it is not, until phase 2), the design of the called-not-copied
wiring, the code, the hooks, the workflows, the templates other repos will
copy, the tests, and live behaviour. **Non-goals:** none narrows the delta.
The reviewer does not decide findings' dispositions; residue joins the
principal's ruling round per house practice.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Does the wiring actually make enforcement *called*, not copied — or
   does any surface still carry a copy that can drift?
2. **Correctness & quality** — run the suites; exercise the hook and the
   floor validate path live; check both workflow files do what the ADR's
   control clause says.
3. **Completeness / harvest** — which surfaces that call or copy enforcement
   were missed; do the two templates and the live workflows agree with each
   other?
4. **Security & privacy** — mandatory, at code altitude: the hook and
   workflows execute on every commit and push — check what they run, what
   they trust, and what a malicious or malformed tree could make them do.
   atelier is PUBLIC — the templates ship to adopters; check what they carry.
   The house security scanner reads pending diffs; this is a landed-delta
   review, so state the reach case that applied.

## Re-run obligation

Re-run, do not read, at least: the full suites (house invocations in
[`.githooks/pre-commit`](../../.githooks/pre-commit)), the suite-count claim
1164 → 1178 at the landing commits, `tools/floor.py` validate on the current
tree, and the pre-commit hook's behaviour on a scratch staged change (in the
scratchpad or read-only — never leave the repo dirty).

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the intent-record refs are orchestrator-held under the rule-1 context partition, handed over only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/sessions/`, and every prior verdict
in `docs/reviews/` — this cycle has prior verdicts, so the bar binds hard. The
intent record (the prior pass and the ruling the application applies) is held
by the orchestrator and will be provided on receipt of your committed
findings. Reconcile after, never anchor before.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `AP` — `EA` and `EP` are taken by prior
passes in this store) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then report; the deferred
references arrive; append a reconcile section and finalise.
