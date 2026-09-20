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
