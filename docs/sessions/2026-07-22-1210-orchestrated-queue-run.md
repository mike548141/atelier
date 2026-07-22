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

**1221 · v2-plugin de-instance ⏳ review — delivered.** Two-hop rule-4 pass
(taker's exposure named in the brief; fresh-context Fable subagent as
reviewer, refs-only prompt): **PASS-WITH-FINDINGS 2M/3M/1L/2n**, verdict
appended verbatim to
[`reviews/2026-07-22-1215-v2-plugin-deinstance-cold.md`](../reviews/2026-07-22-1215-v2-plugin-deinstance-cold.md).
Design upheld (instance-facts externalisation the right cut, no leftover
identity in the bundle — grep-verified); both MAJORs are gaps on the
bundled-adopter path itself (VP1 no canonical bundled-mode propagation
block; VP2 signing posture un-externalised). Mechanical floor re-run at
branch HEAD: all exits 0. 🎯 VP1–VP8 to Mike on the ROADMAP; the reviewer
counsels both MAJORs precede merge; merge and rulings stay Mike's. This
run applied nothing (rule 3) and, having instructed the reviewer's spawn,
may not take any further review of fixes it might later apply — noted for
the chain.

**1240 · Security canon gaps A/B/C/E — built and merged.** Opus worker in
`wt sec-canon-edits`, orchestrator-verified before commit: all five
tag→SHA resolutions re-run independently against the live API (matched),
zero bare `@vN` `uses:` lines left anywhere, floor + YAML parse green at
the worktree (sizescan's ROADMAP size-advisory pre-existing, exit 0).
Landed as `85157c3`, merge `73da10d`. Worker judgement calls, recorded as
the divergence ledger: (1) pinning extended beyond the two named files to
*all* child workflow templates incl. commented example lines — gap C's own
logic; (2) gap E's seam chosen as REVIEW.md over RECORD.md (the finding
lifecycle lives there); (3) child SECURITY.md template + REPO-STANDARD
registration added, framed publish-time like LICENSE; (4) gap-C bearing
placed in PRINCIPLES §8 not §2; (5) SECURITY.md response window stated
best-effort, no fabricated number (ground-numeric-limits); (6) why-SHA
comments at each pin per the say-why convention. Gap D untouched (map
dismissed it). Self-authored doctrine ⇒ **rule-4 `⏳` queued on the
ROADMAP; this run built it and may not spawn its review.**
