# Cold pass — the cancelled-run clause under RECORD.md's floor-at-head all-clear

**Pass type:** doctrine cold pass (REVIEW.md rule 4 — self-authored doctrine).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-09 (see *What the work is*).
- **Who spawned this review:** the principal (Mike), in a session he opened on
  2026-08-09 and pointed at the review queue — rule 4's worked example. His
  words: *"Please do any review work that waiting."*
- **Author's non-involvement:** the taker session authored no part of this
  delta, was neither started nor instructed by the authoring session, and wrote
  this brief as the non-author taker. Rule 4's single criterion is met, and the
  tier was checked at selection.
- **Orchestration shape:** the review runs under an orchestrator holding a
  context partition — the intent-record references are withheld from this brief
  and handed to the reviewer only after its own findings are durably written
  (REVIEW.md rule 1, the one arrangement honestly called structural).

## What the work is

Doctrine landed 2026-08-09, reviewed at HEAD:

1. [`docs/method/RECORD.md`](../method/RECORD.md) — § *The session log*, the
   sub-bullet under *When the close pushes, the evidence is the floor at head*
   covering cancelled CI runs.
2. The `CHANGELOG.md` entry that landed with it.

## Scope

Widest the work admits: the clause's intent, its wording as it will bind every
future session close, and its fit with the surrounding all-clear rule and with
the CI configuration it describes. **Non-goals — one, and it does not fence
the risk:** the reviewer does not decide any finding. Self-authored doctrine;
findings are the principal's to rule on (rule 3). Counsel may be recorded,
labelled as such.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Is the clause aimed at the real failure mode? Does it describe the
   CI's actual cancellation behaviour correctly?
2. **Correctness & quality** — verify the clause against the workflow files in
   `.github/workflows/` at HEAD: does the concurrency configuration it
   describes exist as described, and does the prescribed remedy work?
3. **Completeness / harvest** — what other run conclusions (failure, skipped,
   timed-out, queued-forever) does the all-clear rule meet in practice, and
   does the clause's shape cover or exclude them coherently?
4. **Security & privacy** — mandatory. If genuinely surface-free, discharge in
   one explicit line with grounds. The house security scanner reads pending
   diffs; this is a landed-delta review, so state the reach case that applied.

## Re-run obligation

Any claim in the delta text stamped as measured, live-proven, or grounded is
re-run, not read, where the repo admits it — the grounding incident's
mechanics can be verified against the workflow configuration and the GitHub
Actions run history (`gh run list`, full SHA).

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the intent-record refs are orchestrator-held under the rule-1 context partition, handed over only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/sessions/`, every prior verdict in
`docs/reviews/`, and the intent-record item for this delta (its reference is
held by the orchestrator and will be provided on receipt of your committed
findings). Reconcile after, never anchor before.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `CR`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then report; the deferred
references arrive; append a reconcile section and finalise.
