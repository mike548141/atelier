# 2026-08-18 · 0740 UTC · Cold run — both 1321 briefs taken and run (Fable, wt: cold-run-0818-0740)

**Mike's standing prompt, verbatim:** *"Please do any reviews and fable
dependent work"* — a fresh session on the Fable tier (`claude-fable-5`,
checked at claim), which is what made the two open briefs takeable: it
authored neither delta, was started and instructed by neither authoring
session nor the brief-writer, and ran both passes by hand — reviewer only,
no orchestrator, each deferred sibling opened only after that pass's
findings were durably committed. Claim-commit `c5022cc` on `main` first,
worktree before the first review edit.

## The BW pass — the BS1 wording ruling applied (cycle stays OPEN)

**PASS-WITH-FINDINGS — 1 MAJOR / 3 MODERATE / 2 minor / 3 note** →
`docs/reviews/2026-08-17-1321-bs1-wording-cold.md`. The mechanism claims
reproduced live (scratch repo, both planes, four probe cases — including
the false-fail direction no surface mentions), and the suites reproduced
the landing commit's evidence exactly (1,344 Python, 235 node, selftest,
floor green both planes). **BW1 (MAJOR): the condition clause "at the hook
only when worktree and index agree" misnames the condition on all five
spellings — the probes show agreement is precisely the state in which the
hook misses; the true condition is staged-plane-matches-worktree.**
Reconcile reframed BW1 as counsel against a *ruled* wording (it descends
verbatim from BS1 counsel (c) through the ruling — the FR2 shape, severity
unchanged), so the resolution is Mike's re-briefing. Also: CONCURRENCY
qualifies "a forgotten rebuild", which the hook demonstrably catches (BW2);
the board preamble still asserts the guarantee unqualified (BW3); the new
stop rule loses to CF3's unedited branch test thirty lines below it (BW4).

## The PT pass — the posture section and the fourth guard requirement (cycle stays OPEN)

**PASS-WITH-FINDINGS — 1 MAJOR / 2 MODERATE / 3 minor / 3 note, plus PT4a
(MODERATE) and PT1a (note) at reconcile** →
`docs/reviews/2026-08-17-1321-posture-cold.md`. The section is a real
principle — the reluctance diagnostic and the precondition flag are its
strongest content — and every mechanical claim reproduced. **PT1 (MAJOR):
the fourth requirement's declaration has no home by `GUARDS.md`'s own
same-page, same-day test — no surface, format or check is named, so no
guard can comply and every landed guard is in permanent defect; no board
item funds the homing.** At reconcile: **ruling 1's stamped-copies half —
the case-owning docs pointing up at §10 — is unapplied and unqueued
(PT4a)**, and the requirement overlaps open item `115/120`'s wider
declaration scheme over the same registry entry, with the ruling record
citing `115/130` (vacuity — wrong item) for the asymmetry (PT1a). Also:
the sentence above the new section still says *three* requirements (PT2);
`ACCESS.md` is assigned a device-joining case it does not carry (PT4).

## The 130/010 probe — reading converted to measurement

The stale-pointer detector item asked for confirmation before pricing a
fix; a scratch-board probe ran both directions: the live lead-claim shape
scans clean, the reordered evidence-first shape fires the documented cycle
finding — and two sharpenings landed with it: a split-board state line is
the item's first line by definition, so the order heuristic can never fire
on the lead-claim convention every taken pointer now uses; and pointerscan
is warn-only on both planes regardless. Shape choice stays Mike's.

## State handed forward

Both review cycles stay OPEN on their MAJORs; **BW1–BW9 and PT1–PT9 +
PT4a/PT1a join Mike's ruling round** — BW1 is a re-briefing of a ruled
wording, PT1's homing decision wants to answer 115/120 in the same breath.
Everything else on the board awaits rulings or is another session's lane
(CMF1's DESTROY ruling, the FR/AP rounds, BG1/BG2's working session).
Taker disclosures for both passes are in the verdicts' provenance,
including the onramp `SESSIONS.md` tail read (a ~2KB preview showing a
2026-07-27 entry; the recent entries were never displayed) and, for PT,
the cross-pass exposure from BW's reconcile.
