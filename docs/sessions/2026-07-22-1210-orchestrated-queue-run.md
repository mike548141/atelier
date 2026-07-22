# 2026-07-22 · 1210 UTC · Orchestrated queue run — Fable orchestrator, Opus workers

The queue-run pattern (`CONCURRENCY.md` § Orchestrated queue runs, `skills/
queue-run`) run on the principal's per-run directive: **maximise plan use**,
any unclaimed work of the run's own selection, Fable orchestrates/reviews,
Opus executes (flex allowed), per-item close for cap-safety, stop on the four
named conditions. Records close **per item** — this file is appended and
pushed per close, never batched to the end.

## Observations at open

- Tree clean, 0/0 vs origin/main; no `[~]` claims live on main; no stashes.
- The 1018 run's 🚩 stray worktree `atelier-v2-plugin-deinstance` re-read on
  the evidence: its one commit (`1516ae1`, 2026-07-21) is a **complete,
  recorded** v2-plugin build — session record + accepted ADR + ROADMAP delta
  queueing its own rule-4 `⏳` all inside the commit; commit message states
  "review queued; go-live/merge stays Mike's". That is a parked
  handoff-per-rule-4, not a mid-flight death. Disposition of the *merge*
  remains Mike's; the queued **review** is a `⏳` any criterion-passing
  session may take.
- **Rule-4 provenance for that take, stated before taking**: this session was
  started by the principal pointing it at the queue (the rule's own worked
  example); the delta's authoring session (2026-07-21, Opus worker) neither
  started nor instructed this session. QR1's chain-spawn caution noted: the
  criterion checked here is started-or-instructed, not mere authorship.
- Stale local branch `review-trigger-commitment` noted; put-away checked at
  close.

## Selection

Loose ends & unblockers first (`CONCURRENCY.md` default order):

1. **v2-plugin de-instance `⏳` review** — unblocks Mike's go-live call on the
   chosen widening.
2. **Security canon doctrine edits A/B/C/E** (both slices) — live public-repo
   exposure; proposals already mapped.
3. **ccrepo actual-spend vs API estimate** — feature most of the way scoped.

## Per-item closes

(appended per item)
