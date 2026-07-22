# Review brief — orchestrated-queue-run doctrine + skill (rule-4 cold pass)

- **Date/time:** 2026-07-22 1149 UTC
- **Reviewer:** fresh-context subagent (two-hop spawn — see provenance),
  worktree `queue-run-cold-pass`
- **Subject:** delta `343def8` (`docs/method/CONCURRENCY.md` § Orchestrated
  queue runs; `docs/method/ECONOMICS.md` § the orchestrated-run tier split)
  + `8111e9f` (`skills/queue-run/SKILL.md`, new; `skills/session-onramp/SKILL.md`
  wiring; `README.md` wiring).
- **Intent record:** `docs/sessions/2026-07-22-1018-orchestrated-queue-run.md`
  — **deferred material**, not opened by the reviewer before its findings are
  committed (REVIEW.md rules 1–2). No prior review of this delta exists.

## Spawn provenance (REVIEW.md rule 4)

Mike opened this session and pointed it at the queue ("Please do any review
work") — the worked example rule 4 names. The delta's author (the 2026-07-22
1018 orchestrated-run session) neither started nor instructed this session;
this taker authored none of the delta. The queue pointer carried refs only.

**Exposure, named:** the taker's session-start onramp read the tail of
`docs/SESSIONS.md`, which includes the author session's closing index entry —
an evaluative account of the run that produced this delta. So the review runs
**two-hop** (the 2026-07-21 2208 precedent): the taker wrote this brief
refs-only above the divider and spawns a **fresh-context subagent** as the
reviewer, whose prompt carries refs only. The reviewer names its own attack
surface first; this deferred section, the intent record, and all session
records stay closed to it until its findings are durably committed.

## Status of the work

Self-authored doctrine (doctrine by function — REVIEW.md rule 3): the pattern
was ratified by Mike in direction, but the wording is the author agent's own.
**Findings are Mike's to decide**; nothing is applied by this review, and each
finding carries plain-language what/why/likely-impact (00-APEX,
informed-principal).

## Scope

Widest the work admits: the pattern's design and assumptions, the wording as
doctrine future orchestrator and worker sessions will obey, consistency with
sibling doctrine (CONCURRENCY's own claiming/worktree rules, REVIEW rule 4,
ECONOMICS, PROPAGATION's stamped-copy discipline for the skill), the skill as
a plugin-bundled point-of-use surface, the README/session-onramp wiring, and
the mechanical floor re-run at HEAD. No non-goals are declared; nothing is
fenced off.

## Lenses

All four REVIEW.md lenses. Lens 4 reach: this is a landed-delta review of
markdown doctrine — `/security-review`'s exclusions bar the file class, so a
run would be definitionally empty; discharged on those grounds, weighed as
nothing. The manual lens-4 pass still runs at both altitudes — orchestration
doctrine has real design-altitude surface (what worker prompts are built
from, what authority workers inherit).

## Re-run every live-proven claim in scope

The floor at HEAD: full tool suite (`python3 -m unittest discover -s tools`),
instrument tests (`node --test instruments/*.test.js`), the scanner set as the
pre-commit hook invokes them, `sizescan --check`. Any claim the delta text
itself makes about mechanics (parity, wiring, bundling) is re-driven, not
read.

---

## DEFERRED — reviewer: do not open before your findings are committed

Taker's seeds (a floor, never a fence — REVIEW.md rule 1 shape; the taker is
a non-author but has read the author's closing account, so these sit below
the divider):

1. **Rule-4 transitivity.** The doctrine reportedly treats chained fresh
   sessions as natural rule-4 takers, and the authoring run itself took a
   rule-4 `⏳` mid-run. Does "a session the author neither started nor
   instructed" survive an orchestrator spawning the worker? Where is the
   line, and does the text draw it or blur it?
2. **Queue-item text as prompt input.** Worker prompts are built from queue
   items. ROADMAP text is agent-written under review discipline, but the
   pattern generalises to adopters — does the doctrine say anything about
   what a worker inherits/trusts from the item text (injection shape)?
3. **Skill parity.** Is `skills/queue-run` marked as a stamped
   copy/point-of-use compression, and can it drift from the CONCURRENCY
   parent unnoticed (the SL1/F3 drift class)? Is any parity floor mechanical?
4. **Per-item durability vs claiming rules.** Does the per-item close/chained
   session shape contradict or restate CONCURRENCY's claim `[~]` mechanics?
5. **The ECONOMICS tier split** — grounded in measured practice or asserted?

Intent record (deferred): `docs/sessions/2026-07-22-1018-orchestrated-queue-run.md`.
