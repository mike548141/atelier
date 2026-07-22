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

**1230 · ccrepo actual-spend reconciliation — built and merged.** Opus
worker in `wt ccrepo-actual-spend`, orchestrator-verified: 139/139 tests
green re-run, the CLI smokes, and the worker's flagged **pre-existing
USD×rate² defect** in the Actual footnote inspected line-by-line and
confirmed real (fee stored display-converted, then `money()` converted
again — invisible at `--fx usd`, overstated under the NZD default; the
Actual *column* was always right). Landed `1711711`, merge `12613e0`;
the `~/.local/bin/ccrepo` symlink means the feature is live on this
machine immediately. Design held to the boundary: spend source stays in
`~/.claude`, repo carries synthetic fixtures only; missing months degrade
to a stated partial, never a fabricated figure. Review stance:
self-verifying class (instrument code under its test floor, no doctrine
surface) — grounds stated, not skipped. 🎯 residue on the ROADMAP: the
machine-local config doesn't exist yet; mode choice (plan vs usage) is
Mike's fact, not the mechanism's.

**1247 · Person-context portability design pass — delivered.** Fable
worker (capable tier — structural design, the rework rule), records-only
deliverable placed as
[`2026-07-22-1233-person-context-portability-design.md`](2026-07-22-1233-person-context-portability-design.md),
orchestrator-verified against the public-repo boundary: written wholly in
tier/device/mechanism classes, no personal facts beyond the item's own
wording. The design runs the new REVIEW.md threat-pass discipline on
itself (8 threats), derives C1–C8 from named doctrine sections, and lands
argued per-tier-per-leg recommendations with the phone leg treated as a
different system, not "a sync problem" — exactly the item's framing.
🎯 D1–D5 to Mike on the ROADMAP; build steps and doctrine edits
deliberately undecided behind them. Review stance: records-only capture,
WARRANTED at build/doctrine time (gap-map precedent).

## Stop condition and the 🎯 report

**Stopped 1250 UTC on "everything left is blocked"** — the queue is drained
to the principal. Every item the run could not progress, and why:

- 🎯 **VP1–VP8** (v2-plugin cold pass, this run) — rulings + the merge/go-live
  call. The reviewer counsels both MAJORs precede merge.
- 🎯 **QR1–QR9, SA1–SA8** (prior cold passes) — standing rulings.
- 🎯 **Invariant candidates S1–S5 / V1–V7**; the anti-slop build items queue
  behind them.
- 🎯 **ccarchive metadata classes + signing defaults**; 🎯 **ccrepo spend
  config** (new this run — the machine-local file doesn't exist yet).
- 🎯 **D1–D5** (portability design, this run); "resume any project from any
  device" parks behind them.
- 🎯 **Checkbox grammar five-state question**; **session archive decide**;
  **floor-template duplicate trigger** (estate's call per repo).
- ⏳ **security-canon A/B/C/E cold pass** — queued this run; **rule-4-barred
  to this run** (its worker built the delta). A fresh principal-started
  session passes the criterion and can take it first thing.
- **Warn→block signing flip** — Mike's call + Mike's rotations; **SBOM/
  artifact signing** — deferred behind a first release; **scaffold.py** —
  trigger (a recurring stamp defect) not met; **peer adoption + the
  AUTONOMY/STORAGE practice-instance restructure** — gated on a real
  adopter; **Mike's two raw notes** (honesty/truth/transparency; the Teams
  chat) — do-not-interpret, his to expand.
- **Fleet children floor.yml/pin adoption** — 12/12 behind per
  `tools/pins.py`, but a pin bump is the tool's own "deliberate per-repo
  act" run from inside each child; out of this run's lane by design.
  Follow-on: per-child sessions (each also inherits the new SHA-pinned
  floor.yml and SECURITY.md template at its bump).

## Honesty ledger

- The 1018 run's stray-worktree call was *revised, not overturned*: with a
  day's distance the evidence (complete commit, recorded handoff, queued ⏳
  inside the delta) reads as parked-pending-review; the merge disposition
  remains Mike's exactly as that run left it.
- The ccrepo worker found and fixed a pre-existing rate² defect outside its
  brief; the orchestrator verified it line-by-line before accepting — flagged
  here because accepting unasked fixes is a judgement, not a default.
- The security worker diverged from the gap map in six named ways (see the
  1240 close); all six were accepted on review as better-grounded than the
  proposals they replaced.
- Orchestrator model: Fable (role check passed at open); workers: Opus ×2
  (build), Fable ×2 (cold review; design pass — the rework rule). All worker
  worktrees put away; `atelier-v2-plugin-deinstance` deliberately remains —
  it is the pending-merge branch, Mike's disposition.
