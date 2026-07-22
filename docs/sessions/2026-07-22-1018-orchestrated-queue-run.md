# 2026-07-22 · 1018 UTC · Orchestrated queue run — wave 1 (Fable orchestrator, Opus/Fable workers)

**Shape:** Mike opened this session and pointed it at the shared queue ("progress
any work you can without me"), Fable orchestrating from the primary checkout,
workers in worktrees — the queue-run pattern the ROADMAP ratified 2026-07-22,
run live while its doctrine build is still queued (that build is a wave-2 item
for this run). Per-item close throughout: each item merges, pushes, and records
before the next report, so a session-limit cut loses at most the in-flight item.

**Rule-4 standing:** this session authored none of the queued `⏳` delta
(`caa85fe`) and was spawned by the principal with a generic queue instruction —
the worked example REVIEW.md rule 4 names as an eligible taker. The review
worker's brief and verdict carry the provenance statement.

## Wave 1 — claimed 1018 (commit `9e7e031`)

| Item | Worker | Worktree | State |
| --- | --- | --- | --- |
| ECONOMICS.md rename + ref sweep (decided, execution-only) | Opus | atelier-econ-rename | in flight |
| SECRETS/ACCESS `⏳` cold review (rule 4) | Fable | atelier-secrets-review | in flight |
| Security canon gap map (records-only) | Opus | atelier-sec-gap-map | in flight |
| ccarchive `--restore` full + delta | Opus | atelier-ccarchive-restore | in flight |

Wave 2 (queued, unclaimed until started): queue-run doctrine + skill (ratified —
waits for the rename so it lands citing `ECONOMICS.md`), then candidates by
economics: anti-slop registry mining, ccarchive dataless-awareness / manifest
signing, ccrepo reconciliation drift, the two ccarchive/cctranscript open
questions.

## Observations at open

- 🚩 **Stray worktree `atelier-v2-plugin-deinstance`** (branch
  `v2-plugin-deinstance`, one commit ahead of main: "plugin: de-instance
  create-repo, add worktree + fleet-pins commands (v2)", based on `4da0340`,
  clean tree). No `[~]` claim on the v2 item, no session record mentions it —
  either a live parallel session that skipped the claim step, or an orphan
  from a cut. Left untouched per stay-in-your-lane; the v2 item is out of
  bounds for this run; disposition is Mike's (resume it, or salvage → tag →
  delete per CONCURRENCY put-away).

## Per-item closes

**1030 · Security canon gap map — landed.** Worker (Opus) delivered
`sessions/2026-07-22-1025-security-canon-gap-map.md` (`be737aa`, merged
`--no-ff`): every canon source consulted live, every "already held" claim
verified against the cited doc. A/B/E confirmed narrow, C confirmed-reframed
(zero-dep is the unnamed control; residual = mutable-tag CI actions), D
dismissed to the instance layer. Honesty catch worth naming: the ROADMAP's own
"already held" list overclaimed the anti-slop promotion rule (captured, not
doctrine) — corrected at close. Follow-up queued: doctrine edits for A/B/C/E,
first slice SHA-pinned actions + SECURITY.md. Floor scanners re-run green on
main post-merge (orchestrator's first run used a wrong flag and read exit 2 as
suspect — invocation corrected against the hook, then clean; named per the
check-exit-codes rule). Worktree put away.
