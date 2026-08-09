# Cold pass — the PRINCIPLES.md §9 time-dimension principle

**Pass type:** doctrine cold pass (REVIEW.md rule 4 — self-authored doctrine).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).

## Spawn provenance

- **Author of the work under review:** the sessions that landed the delta on
  2026-08-08 and its 2026-08-09 extension (see *What the work is*).
- **Who spawned this review:** the principal (Mike), in a session he opened on
  2026-08-09 and pointed at the review queue — rule 4's worked example. His
  words: *"Please do any review work that waiting."*
- **Author's non-involvement:** the taker session authored no part of this
  delta, was neither started nor instructed by the authoring sessions, and
  wrote this brief as the non-author taker. Rule 4's single criterion is met,
  and the tier was checked at selection.
- **Orchestration shape:** the review runs under an orchestrator holding a
  context partition — the intent-record references are withheld from this brief
  and handed to the reviewer only after its own findings are durably written
  (REVIEW.md rule 1, the one arrangement honestly called structural).

## What the work is

Doctrine landed 2026-08-08, extended 2026-08-09, reviewed at HEAD:

1. [`docs/method/PRINCIPLES.md`](../method/PRINCIPLES.md) — the new §9
   (*Data modelling — every fact carries its time dimension*), the §1–8 → §1–9
   scope line, and the *state vs stateless* situation test now pointing at §9;
   extended by the 2026-08-09 ruling — §9's derivation-metadata bullet and its
   *Scope* clause.
2. [`docs/method/README.md`](../method/README.md) — item 11's principle list.
3. [`docs/method/CONVENTIONS.md`](../method/CONVENTIONS.md) —
   § *What lives elsewhere*, the frame-vs-existence seam.
4. The `CHANGELOG.md` entries for both landings.

## Scope

Widest the work admits: the principle's intent, its wording as it will bind
future data-modelling decisions estate-wide, the seam it draws against
CONVENTIONS.md, and fit with the other eight principles. **Non-goals — one,
and it does not fence the risk:** the reviewer does not decide any finding.
Self-authored doctrine; findings are the principal's to rule on (rule 3).
Counsel may be recorded, labelled as such.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Is a time-dimension rule a *principle* (universal, situation-tested)
   or a convention? Is the frame-vs-existence seam drawn in the right place?
2. **Correctness & quality** — is §9 internally consistent, and consistent
   with how the repo's own records actually stamp time (UTC at rest)?
3. **Completeness / harvest** — what does a time-dimension principle owe that
   §9 does not say; what existing doctrine does it duplicate or contradict?
4. **Security & privacy** — mandatory. atelier is PUBLIC: does §9 instruct
   future repos to retain or stamp anything that widens a privacy surface
   (times joined to identities, derivation trails)? If genuinely surface-free,
   discharge in one explicit line with grounds. The house security scanner
   reads pending diffs; this is a landed-delta review, so state the reach case
   that applied.

## Re-run obligation

Any claim in the delta text stamped as measured, live-proven, or grounded is
re-run, not read, where the repo admits it — including the cross-references
between the three method docs (do they actually point where they claim).

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the intent-record refs are orchestrator-held under the rule-1 context partition, handed over only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/sessions/`, every prior verdict in
`docs/reviews/`, and the intent-record item for this delta, rulings included
(its reference is held by the orchestrator and will be provided on receipt of
your committed findings). Reconcile after, never anchor before.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `TD`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then report; the deferred
references arrive; append a reconcile section and finalise.
