# 2026-07-19 · 0544 UTC · the applied-batch cold pass taken — 1 MAJOR, rulings owed (Fable)

## Trigger

Mike opened a fresh session: "Do any review work". One `⏳` item sat in
*Doctrine — review-owed*: the applied batch of the combined cold pass (the
F1–F9 rulings applied at `9d95644`). This session is a valid rule-4 taker —
the applier (the 0407 taking session) neither started nor instructed it, and
this session authored none of the three original deltas, the 0407 verdict, or
the applied batch.

## What happened

1. **Claimed before working**: the `⏳` line stamped
   `(claimed 2026-07-19-0544, rule-4 taker, on main)` (`599b631`), pushed.
   On `main` directly — tree clean, no parallel session.
2. **Taker's brief written** (rule 4 + the application-review sequencing
   clause): refs-only subject naming the one delta commit (`9d95644`) plus the
   machine-local create-repo stamp fix; the 0407 verdict file's hunks, the
   applier's session log and the SESSIONS index entry all deferred below the
   divider — the application review's rule-2 residual (the delta carries the
   rulings' decision stamps) named, not denied. Committed `fcf9787`.
3. **One cold reviewer spawned** (fresh-context Fable agent). Sequence held,
   auditable in the commit trail: attack surface committed (`04ae013`, seven
   assumptions chosen cold) → findings committed (`b556392`) → only then the
   deferred material opened and the reconcile appended (`52550ef`). Every
   recorded proof re-run: suite 274 green, sizescan selftest, four scans clean
   at HEAD, all eight F7 bite-mutations red in scratch, F1's red leg and
   partial-tree green leg reproduced — and F1's green leg on a **full step-3
   scaffold**, which **failed**.

## Verdict — PASS-WITH-FINDINGS, 1 MAJOR · 0 MEDIUM · 1 LOW + 1 note, nothing applied

`reviews/2026-07-19-0544-combined-applied-batch-cold.md`. The application
itself verified clean: all nine rulings applied exactly as ruled, no
drift/softening/overshoot, the F2/F4 correction addenda independently
fact-checked (including that `ros` never carried `docs/reviews/README.md`),
originals standing (all record hunks pure additions). What failed is F1's
**proof**, not its fix: **G1 (MAJOR)** — the widened whole-tree
prove-the-stamp grep is unsatisfiable on the skill's own standard scaffold,
because `templates/workflows/floor.yml` ships a deliberate stay-unfilled
`<SHA>` pin slot that step 3 copies into every house-doctrine child; the
recorded "live-proven both ways" green only ever held on a partial tree
without floor.yml (REVIEW.md's stale-proof class verbatim), and the queued
fleet re-stamp would distribute a check that is red on every healthy child.
**G2 (LOW)** — no set-wide placeholder-inventory test pins the invariant G1
breaks; one test would have caught it on the suite run. **G3** — withdrawn as
a defect at reconcile per its own committed caveat (F6's ruling never scoped
the 0820 record); stands as a discretionary one-line note. Taker's counsel
appended (non-author): take G1 three-part (reword the pin-slot vocabulary,
correct the false proof stamp by addendum, hold the fleet re-stamp), G2 with
it, G3 as the one-liner. ROADMAP updated: the item now carries the 🎯 rulings
ask; the fleet re-stamp flipped from "unblocked" to **HELD** on G1.

## Owed

🎯 **Mike's rulings on G1–G3** (per-finding counsel in the verdict file).
1 MAJOR ⇒ the cycle stays open; on the rulings a non-author applies and that
application queues its own `⏳` pass. The fixes are small — a comment reword,
one addendum set, one test, one line — so the next pass has every prospect of
being the no-MAJOR terminal one.
