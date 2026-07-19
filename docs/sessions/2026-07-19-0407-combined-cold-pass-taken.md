# 2026-07-19 · 0407 UTC · the combined cold pass taken — three doctrine deltas, one verdict (Fable)

## Trigger

Mike opened a fresh session: "Do any reviews, use a worktree". One `⏳` item
sat in *Doctrine — review-owed*: the three-delta combined pass (the 07-18
design-review section, the 07-19 commitment re-key + fork→pointer conversion,
and the sizescan doctrine deltas). This session is a valid rule-4 taker — the
author sessions (Opus, 2026-07-18/19, one of them the prior delta's applier)
neither started nor instructed it.

## What happened

1. **Claimed before working** (CONCURRENCY § Claiming work): the `⏳` line
   stamped `(claimed 2026-07-19-0358, wt: fable-cold-pass)` direct to `main`
   (`d43ca75`), pushed; then worktree `fable-cold-pass`.
2. **Taker's brief written** (rule 4): refs-only subject naming the three
   deltas by commit (`30c9cd9`, `4c17f59`, `4fb09a7` + `b33f072`
   acknowledgement), review-at-HEAD instruction, the queued PRINCIPLES.md
   header question passed through for ruling, and the authors' evaluative
   accounts (intent records, session logs, prior verdicts) all below the
   divider. The authors seeded no questions — the deferral discipline was
   applied to their records instead.
3. **One cold reviewer spawned** (fresh-context Fable agent). Sequence held
   and is auditable in the commit trail: attack surface committed (`75b36a8`,
   twelve assumptions chosen cold) → findings committed (`ec58474`) → only
   then the deferred material opened and the reconcile appended (`9436d60`).
   Every recorded proof re-run: suite 267 green, drift tests 12/12, sizescan
   selftest, both live gate classes + fail-safe + declared-budget edge, four
   scans clean at HEAD — and the two wiring claims, which **failed**.

## Verdict — PASS-WITH-FINDINGS, 3 MAJOR · 3 MEDIUM · 3 LOW, nothing applied

`reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md`. The
doctrine content of all three deltas survived attack — the commitment re-key
parses artefact-free, the design-review section holds, the gate split is
live-proven sound. What failed is the **verification record**: F1 the stamped
`<atelier-path>` pointer is never filled in a create-repo child and the
prove-the-stamp grep is scoped past it (the recorded "verified, not assumed"
claim does not reproduce — and the queued fleet re-stamp would distribute the
defect); F2 the "old link broken in every stamped child" claim is false (the
template set ships the target, so it resolved by construction — the conversion
replaced a resolving link with a non-resolving placeholder while the record
asserts the reverse); F3 the "four statements → one" consolidation misses
`skills/review-brief/SKILL.md`, still in the old artefact grammar on the
plugin surface, unmarked as a copy. F4 records misattribute the ros incident
to the stamped template (the 07-18 intent record had it right); F5 "a red
never demands rewording, only a move" is contradicted by the sanctioned
standing-red roadmap case; F6 "enforcement is structural" overclaims while no
template carries the `review:` field. F7 no drift test pins the converted
template; F8 rules the queued PRINCIPLES.md question (genuine defect — re-key
lines 1+3); F9 the silent-absorb provenance, acknowledged adequately, LOW.

Reconcile: F1/F2 both originate in the 0111 retrospective addendum — this
pass was the first cold check of those claims. Taker's counsel appended below
the verdict (non-author): take F1–F8, accept F9; keep the fleet re-stamp
gated behind F1.

## Owed

🎯 **Mike's rulings on F1–F9** (per-finding counsel in the verdict file).
3 MAJOR ⇒ the cycle stays open; on the rulings a non-author applies and the
applied batch queues its own `⏳` pass. The review-line-artefact ROADMAP item
picks up F6's two halves.
