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
