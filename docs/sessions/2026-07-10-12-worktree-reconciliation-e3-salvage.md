**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 34+1 -->
- [2026-07-10 · parallel-worktree reconciliation + E3 salvage + cleanup (Opus)](2026-07-10-12-worktree-reconciliation-e3-salvage.md) — traced a dangling parallel worktree line (independent method-review verdict draft on atelier-method-review@3bfcbbc, never landed; main had its own reworked verdict); nothing lost (both pushed to origin). Side-by-side of the two verdicts: 12/14 findings common+on-main, 3 main-only (all done), 3 worktree-only — salvaged E3 (two-register EVIDENCE §1) to main (48fa5ff), P2/PR2 consciously dropped. Cleanup way-back-verified: archive tag + kept remote branch, removed worktree, deleted local branches.

**2026-07-10 (Opus) — parallel-worktree reconciliation + E3 salvage + cleanup.**
Mike asked whether a worktree he'd opened for parallel atelier work had
completed/saved/closed cleanly, or been lost. Forensics: the worktree
(`~/worktrees/atelier-method-review-method-review`, branch `method-review`) was
**clean and fully merged** into main; a *separate* branch `atelier-method-review`
(tip `3bfcbbc`, a "merge main, both sides kept") carried an **independent draft of
the method-layer review verdict** (`8407b37`, 17:23) — while main had committed
its own reworked verdict of the same review ten minutes later (`6fd64ba`, 17:33).
Both drafts were pushed to origin, so **nothing was ever at risk of loss**; the
loose end was that the parallel line was never `land`ed — it dangled with a
second, divergent verdict.

**Substantive side-by-side of the two verdicts** (brief identical; only the
below-divider verdict written twice). 12 of 14 findings common, all on main;
3 main-only (L1 device-figure swap, V2 ADRs, H2 CHANGELOG — all *done* on main);
3 worktree-only: **E3** (two-register provenance rule in EVIDENCE §1 — genuinely
absent from main, which had judged "§1 holds"; a real improvement), **P2**
(deploy-on-push confirm in the block template — main consciously folded it into
"private→public" and AUTONOMY carries the full rule; judgment difference, not
loss), **PR2** (ros-trim guardrail — moot, the trim already shipped `73fd50b`).

**Action:** salvaged **E3** into canonical EVIDENCE §1 (`48fa5ff`, + CHANGELOG),
the one delta worth keeping. Then cleanup, way-back verified first (all three
pre-flight checks green: method-review merged, worktree clean, local
atelier-method-review == origin): pushed an annotated archive tag
`archive/2026-07-10-method-review-parallel-verdict` at `3bfcbbc`, removed the
worktree, deleted both local branches. The alternate verdict stays preserved on
origin **twice** — the `atelier-method-review` branch (kept as archive) + the
tag. Local tree back to one worktree, one branch.

**Doctrine note worth harvesting later:** this is the failure mode CONCURRENCY's
`land`-the-line discipline exists to prevent — a parallel line whose output was
re-created on main instead of merged back, leaving two divergent artifacts. The
worktree tool makes forking easy; the reconciliation still has to be *done*. Not
a defect in the tooling, a reminder to land or explicitly retire every line.
**Model note:** Opus, plan-included — forensics + a 4-line doc salvage; no flag.
