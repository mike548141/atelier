# 2026-08-09 · 0815–0905 UTC · The seven-pass review-queue batch

**Session:** Fable, spawned by Mike and pointed at the review queue — *"Please
do any review work that waiting."* Rule 4's worked example, tier checked at
selection. Worktree `review-batch-0809-0815`; orchestrator committed, reviewers
ran no git.

## What ran

All seven queued rule-4 `⏳` pointers, claimed 0815 UTC in one commit
(`5f2e4c7`) and run as seven parallel cold Fable reviewers. Each got a
taker-written refs-only brief; the intent-record references were withheld under
the orchestrator-held context partition and handed over only after that
reviewer's findings were durably written — the one arrangement REVIEW.md calls
structural, exercised here for the first time across a whole batch.

## The board

| Pass | Verdict | Cycle |
|---|---|---|
| Child-membership + work-locality | 0 MAJOR / 3 MOD / 5 min / 5 note (CM1–CM13) | CLOSED |
| PRINCIPLES §9 time dimension | 0 MAJOR / 1 MOD / 1 min / 1 note (TD1–TD3) | CLOSED |
| RECORD.md cancelled-run clause | 0 MAJOR / 2 MOD / 1 min / 3 note (CR1–CR6) | CLOSED |
| Floor-render batch | 0 MAJOR / 3 MOD / 1 min / 2 note + FR2a (FR1–FR6) | CLOSED |
| E6b advisory + E3 carve-out | 0 MAJOR / 1 MOD / 2 min / 3 note (AB1–AB6) | CLOSED |
| E7 leakscan build | 0 MAJOR / 1 MOD / 2 min / 3 note (LK1–LK6 + G2 reach) | CLOSED |
| EP application | **1 MAJOR** / 1 MOD / 2 min / 4 note (AP1–AP8) | **OPEN** |

Across the batch: 1 MAJOR, 12 MODERATE. Six cycles terminal under the no-MAJOR
close rule; the EP cycle stays open on AP1 — ADR 0008's control clause names
branch protection + signed commits + registry review as what makes the floating
`@main` enforcement call safe, and its first live check failed (no branch
protection, no rulesets, signing warn-first). Reconcile classified AP1 a
descendant of EP7, with EP1–EP3's substance verified closed at HEAD. Every
verdict's re-run table reproduced in full — suite counts at landing commits,
HEAD suites green (1210 Python / 207 node), live probes on both scanner planes,
the hook driven end-to-end in a scratch repo. All residue joins the scheduled
ruling round; the EP cycle's next application queues its own pointer at its
landing. Nothing was applied, nothing ruled — all dispositions are Mike's.

## Incidents worth carrying

- **The shared tree bit again, gently.** The 0813 queue-batch session was live
  in the primary checkout when this one started; its claim commit was disjoint
  by its own message, but this session's first roadmap edits landed in the
  shared tree and were wiped by the parallel session's file operations within
  minutes. Nothing was lost (the edits were re-applied from context in the
  worktree) — but the lesson is sharper than CONCURRENCY's current trigger: a
  *claim* is write-heavy work, so take the worktree before the first edit,
  not after the first collision. One push later rejected non-fast-forward
  against the same session's comms-floor landing; rebase was clean.
- **reviewscan read the briefs' "Deferred reading" heading as a deferred
  section.** The guard keys on heading vocabulary, and these sections *bar*
  reading rather than carry deferred content — the refs live with the
  orchestrator. Resolved with scoped `reviewscan:allow:deferral` markers
  stating exactly that; the sibling-file rule had nothing to move.
- **The tree-plane datescan caught a reviewer's illustrative "next month"**
  in a finding about time semantics — scoped marker with reason, per the
  worked precedent.

## State at close

Head `3a1de1c` pushed; hook-plane floor green on every landing commit (the
one advisory: ROADMAP size, standing). Worktree removed after merge
verification. The ruling round now holds all seven verdicts' residue on top
of the findings already scheduled — the queue Mike was told about at the
0708 sitting has grown by design, not by drift.
