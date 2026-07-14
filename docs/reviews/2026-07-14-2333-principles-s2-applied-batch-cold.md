# Review brief — PRINCIPLES §2 applied batch, cold pass

*2026-07-14 2333 · commissioned by a session that is neither the doctrine's
author nor the applier of the batch under review. Un-briefed by design: the
commissioning session has not read `docs/method/PRINCIPLES.md` §2 at HEAD nor
the prior verdict, so no seeded questions exist and none are deferred below a
divider.*

## What the work is

On 2026-07-14 a prior session applied a batch of five decided review findings
to `docs/method/PRINCIPLES.md` §2 (the four bullets). The first cold pass on
that section returned a MAJOR, so under `REVIEW.md` (*Applying decisions to
doctrine — and when the cycle stops*) the applied batch earns its own
un-briefed cold pass by a different session. That session authored both the
verdict and the edits, so this pass is also the applier-independence backstop.

## The ask

Review `docs/method/PRINCIPLES.md` §2 as it stands at HEAD (`c6d66c8`;
last touched by `f4356f8`... check the file's own log), deep not fast, under
all three lenses of `REVIEW.md`:

1. **Approach & assumptions** — name the section's load-bearing assumptions
   yourself, as your first act, and attack them.
2. **Correctness & quality** — does the text do what it claims; internal
   consistency; consistency with sibling `method/` docs; any overclaim.
3. **Completeness / harvest** — what §2 should cover and doesn't; what
   elsewhere in the repo it duplicates or contradicts.

Re-run every live-proven claim in scope (`REVIEW.md` §Re-run): if §2 or its
surroundings assert something checkable (a tool exists, a gate runs, a date or
event happened per the repo record), check it.

## Sequence — binding

This is an application review, so rule 2 cannot be fully honoured; the
residual exposure is named here, not denied. The sequence is:

1. Review the doctrine at HEAD. Write your findings (stable IDs, severity
   MAJOR/MEDIUM/LOW) into this file below the divider, and **commit** them.
2. Only after that commit, open the prior verdict
   (`docs/reviews/2026-07-14-2154-principles-s2-four-bullets-cold.md`) and
   reconcile: verify each `[fixed]` claim against the text at HEAD as
   fix-verification, note agreements/divergences, and append the
   reconciliation + final verdict (PASS / PASS-WITH-FINDINGS / FAIL) below
   your committed findings. Commit again.

Findings on doctrine are the principal's to decide (`REVIEW.md` rule 3):
record, do not apply. Per the close rule, if this pass returns no MAJOR the
cycle closes.

---

## Cold pass — findings (reviewer: independent session, 2026-07-15)

*Written and committed before opening the prior verdict or any diff/message of
the applied batch, per the brief's binding sequence. One exposure declared:
locating the file's last-touch commit via `git log --oneline` showed the batch
commit's subject line only — no body, no diff, no prior verdict.*

### Load-bearing assumptions named and attacked (lens 1)

1. Each new bullet generalises from decided practice, not invented to fill a
   heading — **held** (bf7ef4d / ae43f12 record Mike bringing all four,
   dated 2026-07-14).
2. The mobile-first ban's DRY rationale discriminates the banned case from the
   permitted one — **attacked, fails** (F2).
3. The grounding claims re-run true at the primary source — **attacked, one
   fails** (F1), the rest verified below.
4. The scope tests (twin's reads-vs-operates; API-first's more-than-one-surface)
   are decidable — held; no concrete case found where they mis-decide.
5. The fleet honours the twin rule rather than silently violating its own
   doctrine — **held**: `tiki` carries `--json` with documented schemas
   (ros `tiki/src/tiki/cli.py:62`); atelier's `ccrepo` and `cctranscript` both
   carry `--json`.

### Live-proven claims re-run (REVIEW.md §Re-run)

- ✅ "decided 2026-07-14" (API first; mobile-first) — ae43f12, attributed Mike.
- ✅ "direction set 2026-07-12" (CA seam) — ros `docs/SPECS.md:1232`.
- ✅ "the seam's first slice shipped 2026-07-14" — ros `8d297e8` (`ca.py`,
  pluggable `CaBackend`); "its own review owed" — tracked as an open ros
  ROADMAP item with brief `docs/reviews/2026-07-14-common-ca-engine.md`.
- ✅ EVIDENCE.md §9 is the one-fact-one-home rule; PROPAGATION.md carries the
  one-source rule; §6 "Observable by design" reads as §2 cites it.
- ❌ "its one non-REST path is a single SFTP upload on the rescue route" —
  fails re-run at the primary source. F1.

### Findings

**F1 · MAJOR · The API-first bullet's grounding parenthetical is false at the
primary source — and was false when written.** §2 states tiki drives RouterOS
via REST "for all steady-state convergence (its one non-REST path is a single
SFTP upload on the rescue route)". At ros HEAD, `apply_plan` takes a pre-apply
`/export` snapshot **over SSH before every mutation** and refuses to apply if
it fails (ros `tiki/src/tiki/apply.py:186-194`, `snapshot.py:59`) — a second,
load-bearing non-REST path inside the steady-state convergence verb itself. It
landed 2026-07-13 (ros `0df23f7`), the day *before* the claim was written, so
this is the §6 cautionary class exactly: a recorded proof false at its own
recording commit. Charitable readings don't save it: `tiki pki` deliberately
writes device certs over SSH (pki.py header: "Why SSH and not REST"), and the
ros record itself names **two** authenticated management planes — REST and SSH
— that "every steady-state verb enforces" (ros `docs/ACCESS-MAP.md:52`). The
principle stands; its stated evidence doesn't. Note the miss also flattens a
*better* case: pki's SSH-not-REST is a documented, reasoned departure where the
API has a gap — a model instance of §2's own "stated deliberate exception"
discipline, stronger grounding than the false "single exception" tally.

**F2 · MEDIUM · The mobile-first bullet's DRY rationale doesn't discriminate
between the banned case and the permitted one.** The ban's stated ground —
"two surfaces asserting the same product truth, diverging from the day they
fork" — applies equally to a native app; the permission's stated ground —
"riding the API-first contract" — applies equally to a separate mobile web
edition. The real discriminator is unstated: within the web medium one
responsive artifact already serves every form factor, so a forked web edition
is pure duplication with zero capability delta, while a native client is a
different medium bringing capabilities the web surface cannot (offline, push,
sensors). As written, an agent applying the *reasoning* rather than the fiat
could ban a native client or wave through an API-backed m-dot edition. State
the capability-delta test; the labels then follow instead of being asserted.

**F3 · LOW · "the same seam the vendor's own UI rides" is an unverified
vendor-internals claim stated as fact.** Nothing in the ros record asserts
WebFig rides the REST API, and at a strict reading it likely doesn't (WebFig
shares the www service, not the documented `/rest` seam) — EVIDENCE.md §2
would tier this ai-inference presented at primary confidence. Soften to what
is known ("the same HTTP management plane") or ground it.

**F4 · LOW · Legibility: the mobile-first bullet is one ~80-word sentence with
a doubly nested parenthetical** (the native-app carve-out inside the DRY
aside). The doc holds KISS as doctrine; give the carve-out its own sentence.

**Count: 1 MAJOR · 1 MEDIUM · 2 LOW.**

## Reconciliation with the prior verdict (opened after findings commit `0b0510d`)

### [fixed]-claim verification at HEAD (fix-verification, REVIEW.md step 5)

- **Prior F1 [fixed] — ⚠️ applied as ruled, but the fix does not survive
  re-run.** "Exclusively" is gone and the counselled wording is present at
  HEAD. But the replacement clause — "its one non-REST path is a single SFTP
  upload on the rescue route" — is itself false at the primary source (this
  pass's F1): ros `0df23f7` (2026-07-13, *before both passes*) put an SSH
  `/export` snapshot in front of every mutating apply. The prior pass's
  counsel leaned on tiki's own `rescue.py:21` comment ("the one non-REST
  step"), which was already stale in ros when quoted — the false source
  propagated through the counsel into the fix.
- **Prior F2 [fixed] — ✅ verified.** The restated case is at HEAD and all
  three facts re-ran true independently: direction set 2026-07-12 (ros
  `SPECS.md:1232`), first slice shipped 2026-07-14 (ros `8d297e8`), review
  owed (open ros ROADMAP item + carved brief).
- **Prior F3 [fixed] — ✅ verified.** The *Scope* sentence is at HEAD and
  matches the counsel (more-than-one-surface / is-a-service; single-surface
  CLI satisfied by the twin).
- **Prior F4 [fixed] — ✅ verified.** "Commodity" replaces "minor"; the
  adopt-outright exit (KISS, precedence 5–6) and the §5 hold for
  security-critical commodities are both at HEAD.
- **Prior F5 [fixed, bundle] — ✅ verified, with residuals.** Read-vs-operate
  test, §6 cross-link, and the native-app clause are all at HEAD; tiki naming
  kept as ruled. Residuals found by this pass on the added clause: its DRY
  rationale doesn't discriminate (F2 here) and the sentence's nesting hurts
  legibility (F4 here).

### Agreement / divergence

The prior pass and this one agree on the doctrine's shape and on four of five
fixes. The one divergence is structural, not a quarrel: the prior F1 fix
traded a large overclaim for a smaller one, because the "one non-REST step"
tally came from a ros comment that ros's own 2026-07-13 snapshot change had
already invalidated. This pass's F3 (vendor-UI seam) and F4 (legibility) are
new; F2 here is a residual edge on the prior F5's native-app clause.

### Final verdict — PASS-WITH-FINDINGS · 1 MAJOR · 1 MEDIUM · 2 LOW

The applied batch is real, honest work: all five rulings were applied as
decided, four verify clean at the primary sources, and the section is
materially stronger than at the first pass. The MAJOR is confined to one
grounding clause whose falsity originates in the child repo's own stale
comment.

**Cycle status — the escape valve applies.** This pass carries a MAJOR, so
the close rule does not close the cycle — and the MAJOR count is *not
falling* (pass 1: one MAJOR; this pass: one MAJOR). Per REVIEW.md, that is
the signal to stop cranking and ask the principal for direction rather than
spawn another full ceremony. Reviewer's counsel, labelled as counsel: F1 is a
one-clause ruling (e.g. "its non-REST paths are a pre-apply snapshot and the
rescue upload over pinned SSH — stated exceptions, not drift"), and fixing
ros's stale `rescue.py:21` comment in the same sweep removes the false
source; a principal ruling on F1–F4 directly, with fix-verification only,
would close honestly without a fourth pass. The decision is Mike's.
