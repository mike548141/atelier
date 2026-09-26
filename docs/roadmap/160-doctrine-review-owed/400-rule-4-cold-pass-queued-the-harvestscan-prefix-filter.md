- ⏳ **Rule-4 cold pass queued — `harvestscan`'s prefix-filter rewrite
      (`020/400`).** Self-authored by the run (its dispatched worker's output
      is the run's authorship); queued at landing, and the run neither takes
      nor spawns it. *Tier:* Fable, the principal-named review tier — checked
      at selection; a session that cannot honour the bar stops rather than
      takes. *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta — scoped to paths:* `tools/harvestscan.py`
      (`_build_survivor_index`, `_candidate_bucket`, and `vanished`'s inlined
      containment), `tools/test_harvestscan.py` (the `BoundedTime` class),
      `tools/README.md` § *harvestscan*. Landed on `main`, 2026-09-20.
      **The lenses that matter most here, and the first is the whole review:**
      whether the exactness claim actually holds. The rewrite rests on a
      pigeonhole argument — that a survivor reaching `SURVIVAL_SIMILARITY`
      containment must intersect the fingerprint's rarest `n − k + 1` words —
      and on `similarity()` being `|A ∩ B| / |A|` over sets, which the fast
      path recomputes inline rather than calling. Both were checked here and
      both should be checked again independently, because an off-by-one in
      `k = ceil(0.6n)` or a divergence between the inlined formula and
      `similarity()`'s would silently drop true positives in a **warn-only**
      guard, where nothing downstream would ever notice. Then: whether
      duplicating the containment formula rather than calling `similarity()`
      is a drift hazard of exactly the `115/080` shape, given the two must now
      stay equal by hand; whether the `BoundedTime` ceilings are grounded in
      the work's class rather than fitted to the machine that measured them
      (`ground-numeric-limits`); and whether the 749-commit replay's
      byte-identical result is as strong as it reads, given only 9 commits
      were in scope under the gate.
      *Intent record:*
      [`../../sessions/2026-09-20-1053-queue-run-the-loose-ends.md`](../../sessions/2026-09-20-1053-queue-run-the-loose-ends.md).
      `[~]` **CLAIMED 2026-09-25 0705 UTC for the review run** (wt:
      review-batch-0925; brief
      `docs/reviews/2026-09-25-0715-harvestscan-prefix-filter-cold.md`) by a
      Mike-opened `claude-fable-5-1` session ("Please deliver all fable
      dependent work, and work that would be best delivered using fable") that
      authored none of the delta. Shape, disclosed per rule 4:
      reviewer-plus-orchestrator, both seats Fable — this session writes the
      refs-only brief and holds the `.deferred.md` sibling outside the worktree;
      a fresh Fable subagent it spawns forms every finding and severity. The
      sibling, the intent record and prior verdicts stay unopened by the
      reviewer until its phase-1 findings are committed. Provenance and exposure
      go in the verdict.
      - [ ] 🛑 **The pass RAN 2026-09-26 and the cycle stays OPEN — a MAJOR
            stands.** The rule-4 Fable cold pass (taker: a fresh
            `claude-fable-5-1` subagent under a `claude-fable-5-1` orchestrator
            — the shape disclosed in the claim above; the sibling, the intent
            record and prior verdicts opened only after the phase-1 findings
            were committed) returned PASS-WITH-FINDINGS — 1 MAJOR · 0 MODERATE ·
            5 minor · 3 note →
            [`2026-09-25-0715-harvestscan-prefix-filter-cold.md`](../../reviews/2026-09-25-0715-harvestscan-prefix-filter-cold.md)
            (sibling folded in and deleted). HP1 (MAJOR): the survivor index is
            rebuilt inside vanished(), which scan() calls once per watched file
            — 331 rebuilds at HEAD — so on the split board the bounded pass is
            16× slower than the quadratic one it replaced at function level and
            3× slower at the live hook plane, while the exactness claim itself
            holds on every probe (708 boundary cases, 4,000 bucket checks,
            byte-identical replay); no test or replay commit can see it, and
            built once the same scan takes under 3 s; HP8/HP9 formed at
            reconcile. Findings are the principal's to decide (rule 3); nothing
            was applied.
