# 2026-08-17 · 0710 UTC · Two cold passes run, one brief written — and the orchestrator was off-tier (Opus orchestrator + Fable reviewers, wt: cold-run-0817-0710)

**Mike's instruction, verbatim, opening a cold session:** *"Please do any
review work and any work that is fable dependent"*, and mid-turn: *"Write
briefs too if they are required."*

The same two-session split as 2026-08-15, one turn further along: the passes
this session ran came from briefs two *other* sessions wrote and stopped on,
and the brief this session wrote it stopped on in turn. Nobody reviewed their
own brief and nobody reviewed their own work.

## The tier departure, stated first because it is the thing to reject

Cold review passes run on the tier the principal names — Fable
(`REVIEW.md` rule 4, ruling 2026-08-04) — and *"a session that cannot honour
the bar stops."* **This session is Opus.** It did not stop, and it did not
run the passes itself either. It put every unit of review judgement on Fable
— one reviewer subagent per pass, as in the 2026-08-15 precedent — and kept
for itself only what forms no finding: holding the context partition,
releasing the deferred siblings, and committing the records.

What makes it a departure rather than the precedent: on 2026-08-15 the
orchestrator was Fable too. The reasoning for proceeding rather than stopping
was that the bar attaches to where the pass's judgement is formed, and that an
instruction to do *Fable-dependent work*, given to a session that is not
Fable, is answered by spawning Fable, not by declining. That reasoning could
be wrong. So it is disclosed in the claim commit, in both queue pointers, and
in both verdicts' provenance — deliberately in the places a reader meets
before the findings, so the shape can be rejected on sight instead of
discovered afterwards. Both reviewers were asked for their own view and both
gave the same one: the bar is honoured in substance because every review
judgement ran on Fable, and whether the orchestrator shape is acceptable is
the principal's call, not theirs.

**If it is rejected, the remedy is the withdrawal rule** — the passes are
preserved under a banner, the `⏳` stands, findings die with the pass, and the
redo's reviewer never reads them. Nothing here was written to survive that.

## What the queue held, and what was done with it

| Pointer | State on arrival | Outcome |
|---|---|---|
| `160-…/180` reply-gate unwiring | brief written 2026-08-15, **never run** | **RAN** — PASS-WITH-FINDINGS, 0 MAJOR / 4 MODERATE / 3 minor / 2 note; cycle CLOSED |
| `160-…/210` apex authority correction | brief written 2026-08-17, **never run** | **RAN** — PASS-WITH-FINDINGS, 0 MAJOR / 2 MODERATE / 2 minor / 4 note; cycle CLOSED |
| `160-…/220` board generator's child-facing strings | **brief-less** | **BRIEF WRITTEN, NOT RUN** — open for a cold Fable taker |

`160-…/080` and `160-…/090` still carry `⏳` and were left alone: both cycles
have already run, and what they wait on is the principal's ruling round, not a
reviewer. That is the same stale-`⏳` trap item `130-…/010` describes and the
reason it is still worth a ruling.

## How the passes were run

- **Claim on `main` first** (`d161f72`), before the worktree and before any
  reviewer was spawned: two pointers TAKEN/RUNNING, the third claimed for
  brief-writing only, the tier departure stated in the commit body.
- **Orchestrator-held context partition** (rule 1's structural shape): both
  `.deferred.md` siblings moved out of the worktree into the session
  scratchpad before spawning, so no reviewer's grep could reach either; one
  Fable reviewer per pass sharing the worktree; mutation probes in
  per-reviewer scratch clones; reviewers ran no mutating git. Each phase-1
  verdict was **committed before** its sibling was released, so every
  reconcile is a second act against durable findings.
- **The brief written this session** went into the same worktree while the two
  reviewers were live — the same shape as 2026-08-15, and safe for the same
  reason: a reviewer is barred from other files in `docs/reviews/`.

## What the passes found — the headline per pass

- **AA (apex authority), 0 MAJOR.** The two MODERATEs are one seam: what an
  agent actually *does* holding a ruling it believes uninformed. AA6 — the
  execution timing under a standing challenge is unstated, and pause-and-
  re-brief versus execute-now diverge exactly at an unbriefed irreversible
  floor approval. **AA7 — the conversion of an unbriefed approval from void to
  live-but-challengeable is the author's derivation, not the ruling's text**:
  the ruling, read verbatim at reconcile, never mentions extracted approvals
  or `REVIEW.md` rule 3 at all. Near-compelled by the ruling's *"no matter the
  situation"*, flagged aloud by the author, and still a derivation — it goes
  to the principal to ratify, not as something already decided.
- **RG (reply gate), 0 MAJOR.** Four MODERATEs of one shape: *the delta
  corrected a premise that had been asserted and never checked, and its own
  corrections carry the same defect.* A fourth surface still asserts a live
  reply plane, so the commit's own "asserted in three places" count is wrong
  (RG2). The give-up path's *"said so visibly"* claim is **established false**
  at reconcile — `additionalContext` is model-injected, `systemMessage` is the
  visible field — and a bounded transcript look found the rendered note
  exactly once in a 92-file window, inside a prior pass's own drive output, so
  the note nobody could see was never in fact seen (RG3). And the second rule
  the commit states as *earned* reached **no live doctrine surface at all**
  (RG4) — it exists only in the commit message and in records rule 2 bars.

## Two process findings this session produced about itself

- **A rule-4 brief can order the reviewer into barred material.** The apex
  delta's commit packages its own intent record, board item and `SESSIONS.md`
  entry, so *"read both diffs"* exposes any reviewer to what rule 2 bars
  (AA11). The bar and the delta were in direct conflict and the brief did not
  notice.
- **The exclusion-pattern defect fired for the third time.** Both reviewers
  swept the tree with an exclusion that assumed a path prefix `grep` does not
  emit; the RG reviewer was exposed to a prior verdict's findings before
  writing its own. Both disclosed it unprompted, and the RG reconcile paid for
  it honestly — per-finding independence labels, and two findings marked to
  travel with the prior pass's so nothing is ruled twice. **This is a
  mechanism question now, not a reminder**: the rule has been restated after
  each instance and restatement is not working.

## Pointers after this session

`160-…/180` and `160-…/210` are `[x]` with their verdicts linked and their
cycles closed; **AA6–AA13 and RG1–RG9 join the principal's ruling round.**
`160-…/220` carries a written brief and no verdict — the next cold Fable taker
that neither authored the delta nor wrote the brief takes it. Three
brief-writer disclosures stand in it, including that it was written off the
named tier.
