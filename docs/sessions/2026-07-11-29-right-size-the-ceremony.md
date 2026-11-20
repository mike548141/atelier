# 2026-07-11 · right-size the ceremony — calibrate review/session gates to risk (Opus)

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 51+1 -->
- [2026-07-11 · right-size the ceremony — calibrate review/session gates to risk (Opus)](2026-07-11-29-right-size-the-ceremony.md) — Mike's observation accepted: "one thing per session" was being over-applied and productivity degraded across the day; the driver was *not* economy (a fresh session is the pricier choice for related work) but an over-generalised rule + a pull to hand back at a safe green boundary. Found the record's actual words are narrower than my use: **"one task per session"** targets an *unrelated pivot* dragging stale tokens, not one-item-then-stop; **"don't-stack" was nowhere in the doctrine** — an un-codified session habit enforced as a rule, over-broadly. Captured proportionately (living the advice): MODEL-ECONOMICS gains **"Match the ceremony to the risk"** (gates/sweeps/session-breaks are *spend*, apply ∝ cost-of-being-wrong; what earns full ceremony vs. what's self-verifying; don't-stack codified with its narrow scope — an *unreviewed dependency*, not mere sequence) + a sharpened hygiene item 1; REVIEW gains a **"whether a change earns a review at all"** bearing pointing up. **Recursive check: this change is doctrine text, so by its own new rule it is review-owed — flagged, not self-certified, not merged by me.** Done in an isolated worktree (`gate-calibration`, off `bafeaa3`) to avoid clobbering a concurrent live session; handed back as a branch + PR for Mike to merge. Template MODEL-ECONOMICS copy deliberately untouched (separate templates pass).


Mike's observation, accepted: I had been treating "one thing per session" as a
near-law and advising a fresh session after each single item — and productivity
was visibly degrading across the day. Examined honestly, the driver was **not**
economy (for related work a fresh session is the *more* expensive choice — a cold
re-onramp and a cache miss); it was two things: over-generalising a narrow rule,
and a pull to hand back at a safe green boundary (risk-aversion dressed as
discipline). This session captures the correction as doctrine.

## What the record actually said vs. how I applied it

- **"One task per session"** (MODEL-ECONOMICS hygiene item 1) is about *pivoting
  to an unrelated task* dragging stale tokens — not a ban on related sequential
  work. I had inflated it into one-checkbox-then-stop.
- **"don't-stack"** turned out to be **nowhere in the doctrine** — it lived only
  in the session records as a practice I named and re-applied. So an un-codified
  habit was being enforced as if it were a rule, and over-broadly: it properly
  covers *building a gate on unreviewed tooling/doctrine* (an unreviewed
  dependency), not sequential independent work.

## The change (proportionate on purpose — living the advice while writing it)

One principle + one bearing + one sharpening, not a sprawl across every doc:

- **MODEL-ECONOMICS.md** — new section **"Match the ceremony to the risk"**: review
  gates, fresh-context sweeps, session breaks, and the don't-stack pause are all
  *spend*; apply them in proportion to the cost of being wrong, not uniformly
  (uniform ceremony is exactly how a maturing repo's overhead-to-output ratio
  climbs — the mechanism behind Mike's productivity read). Lists what earns the
  full ceremony (first-of-kind/structural tooling, silent-failure surfaces,
  doctrine text, irreversible/public actions) vs. what is self-verifying (tests +
  dogfooding over already-reviewed machinery). Codifies don't-stack with its
  correct narrow scope. Plus a **sharpening of hygiene item 1** so "one task" can't
  be re-misread: a task is a coherent *line* of work; break for a genuine reason,
  not because one item went green.
- **REVIEW.md** — new bearing **"Whether a change earns a review at all — calibrate
  to risk"**: the lifecycle is the full ceremony, not every change earns it;
  points up to the MODEL-ECONOMICS section. Fills a real gap — REVIEW already
  calibrated *which reviewer* and *inline-vs-batched*, but read as though every
  change goes through brief→verdict.

## Recursive consistency — this change is review-owed by its own rule

The new doctrine says *doctrine text earns an independent fresh-context review*
(a wrong rule propagates everywhere it's inherited). This change is doctrine text,
so it does not get to self-certify. **Flagged review-owed; not merged by me.** A
light fresh-session read suffices (small, self-contained) — but independent, per
the rule it just wrote.

## Concurrency — done without touching the live session

Another session was running concurrently in the shared iCloud checkout (it built
session 27's child-CI floor and pushed it to main). Editing files on `main` in the
same working directory risks live file-clobbering, not just git races — so this
line was forked into its own worktree (`tools/worktree.py start gate-calibration`
→ `~/worktrees/atelier-gate-calibration`, off `bafeaa3`), dogfooding CONCURRENCY.
Handed back as a **branch + PR**, not a merge: merging to a shared main while
another session lands there is the coordinated step, left to Mike. ROADMAP/SESSIONS
tail lines may need a trivial keep-both if the other session appended its own.

## Left open

- The **review** of this doctrine change (owed by its own rule, above).
- **Template copy** `build/templates/docs/MODEL-ECONOMICS.md` carries a condensed
  "one task per session" line; deliberately *not* touched here (it pulls in the
  create-repo/propagation surface — a separate, review-owed change). Noted for a
  templates pass.
