# 2026-07-20 · 13:02 UTC · Session-onramp operating-rhythm doctrine

**Trigger.** Mike asked for a review of atelier + children + past sessions to
improve how he works with Claude, and offered ~7 candidate standing instructions
he keeps re-typing into child-repo sessions (think step-by-step · worktrees +
watch other sessions · claim work / claimed beats "even if I told you" · focus on
given work · prompt when economics favour a new session · safe-stop under
overload · confirm-tidied-and-ready-to-close at the verdict). Worked in worktree
`atelier-session-onramp-review`.

## Concurrency coordination (dogfooded)

A sibling session was live in `atelier-concurrency-assume-parallel`, editing the
*exact* docs this work touches (CONCURRENCY, the child block, ROADMAP). Mike said
pause and pick up when it lands. Parked findings to scratchpad, armed a
background watch for its landing, went quiet. It landed as `295d94a` (the
"assume you are not alone" flip) and put its worktree away; a second sibling then
landed `62fe96a` (DOCUMENTATION.md first draft). Rebased onto both; re-validated
every finding against the final tree before authoring. No collision.

## The reframe (the actual finding)

Mike's candidates are **not** mostly new rules — 6 of 7 are already grounded
doctrine in `method/*`. The gap is **reach**: the only surface a child session
always loads is the *standard child doctrine block* (`PROPAGATION.md`), which
inlines the **safety floor only**. Claim / economics / close never reach a
session, so Mike re-types them. A propagation gap, not a content gap — and the
block already carries an operational beat (the concurrency line), so surfacing a
working beat extends a precedent rather than inventing one.

## Authored this session (home docs — applied, on main)

- **(A) `CONCURRENCY.md` § Claiming work** — a live `[~]` claim **outranks a
  standing instruction** to take that item (the "don't work it even if I told you
  to below" case). Same yield as a rejected push, reached one step sooner off a
  marker the instruction predates; a *current* re-assignment still overrides.
- **(B) `MODEL-ECONOMICS.md` § Session hygiene item 7** — **surface the session
  boundary** (say so when economics favour a fresh session, don't cross silently)
  and **stop safely under overload** (safe stopping point → record → hand off; a
  clean handoff of half beats a muddy completion of all).
- **(C) `RECORD.md` § close** — sharpens the existing declare-the-close signal:
  the all-clear **carries its evidence** (shows what was captured/put away), not a
  bare "done" — the apex claim-carries-its-evidence rule at the session boundary
  (Mike's session-close communication point, this session).

**Dropped:** "think step-by-step" — ungrounded, cargo-cult, and modern models
reason by default; it would be the one line violating the repo's ground-everything
rule. **Folded:** "focus on given work" → "stay in your lane" in the cue.

## Applied — the child-block cue (standalone)

Mike ruled (2026-07-20): *yes*, the always-read block may carry an operating
beat, not only the floor. He then decoupled it from the concurrency-flip
catch-up (the coupling was confusing and not a real dependency). So a **Session
rhythm** bullet (claim → lane → economics/boundary → evidence-based close, each
pointing up) now lives in `PROPAGATION.md`'s canonical block **and**
`build/templates/CLAUDE.md`. Children adopt at their next pin bump. *Still owed
on the block but NOT this work's:* the concurrency-flip (`295d94a`) catch-up —
the block's Concurrency bullet still carries the pre-flip wording; that's the
concurrency cycle's job.

## Follow-on — the size-signal rebalance (Mike commissioned; fresh session)

Landing the operating-rhythm work tripped `main`'s floor: `sizescan --check` reds
on ROADMAP > 300 lines. Mike rejected the easy de-fang ("make it advisory") and
named the real bug — a flat line-count is a crude proxy made a **hard CI
failure**, punishing fulsomeness on a number grounded in nothing. Agreed reframe:
**cost is size × read-frequency**; meter only the hot path, gate only on
relocatable cold content, never on live fulsomeness. Captured as an open ROADMAP
item (File-size hygiene) with the full design direction, for a fresh focused
session. **`main`'s floor is deliberately left RED** until it lands — the red is
the false signal being fixed, not a real defect; not hacked to hide it.

## Review

Doctrine → REVIEW.md rule 4. Author does not self-review; ROADMAP item is ⏳,
queued for an independent (non-author) session, which writes the brief and, when
it also carries the block cue, reconciles with the concurrency-flip propagation.

## Identifier note

Id is `date -u` per CONVENTIONS (UTC at rest). 13:02 UTC 2026-07-20 = 01:02 NZ
2026-07-21. May *read* as preceding same-day sibling entries whose stamps were
written local-mislabelled-as-UTC; those are theirs, unchanged (append-only).
