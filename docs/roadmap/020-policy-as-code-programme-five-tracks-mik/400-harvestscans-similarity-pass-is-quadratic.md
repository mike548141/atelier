- [x] 🔥 **`harvestscan`'s vanished-item check is quadratic in the number of
      items, and it is already past useful at estate scale** — split out of
      `020/380` 2026-09-20, where a worker measured it while converting five
      guards and correctly refused to patch around it.
      **Measured, on a synthetic git repo:** `vanished()` compares every
      candidate item against every survivor through `similarity()`, which is
      O(items × survivors) — in *item count*, not bytes. **500 items: ~21
      seconds. 5,000 items: did not finish inside a 120-second ceiling.**
      Ten times the data, more than six times the time budget, and no answer.
      **Why it matters now rather than later.** This repo's own board is past
      470 index lines and the fleet's boards grow with it; harvestscan is
      warn-wired on the record plane, so the failure mode is not a red
      build — it is a guard that quietly takes longer than anyone waits for
      and stops being run at all. `020/380`'s requirement already covers it:
      *running time at most linear in the bytes read*. This is the second
      time that clause has caught a defect no memory measurement would show
      (`spellscan`'s backtracking regex was the first, `linkscan`'s two
      quadratic passes the second and third).
      **Owed:** an indexed or bucketed similarity pass — block on a cheap key
      (leading number, title prefix, normalised first words) and compare only
      within a bucket, so the common case is linear and the worst case is
      bounded by bucket size. Then the same `BoundedMemory`-shaped regression
      test the other guards carry, but on **time** as well as memory, since
      time is what fails here.
      **Explicitly not:** raising the ceiling, sampling the comparisons, or
      capping the item count — each of those makes the number go away and
      leaves the guard wrong at the size the estate is actually reaching.
      ---
      ✅ **FIXED 2026-09-20, and exactly rather than approximately.** The
      quadratic join is replaced by a **prefix filter over an inverted word
      index** — the standard technique for a set-overlap join, not a heuristic
      dodge. Containment against an `n`-word fingerprint needs at least
      `k = ceil(0.6n)` shared words, so any true match must intersect the
      fingerprint's **rarest `n − k + 1`** words: leave all of those unshared
      and at most `k − 1` remain available, which is short of `k`
      (pigeonhole). Ranking by rarity keeps the touched postings small when a
      fingerprint mixes rare words with common ones — the common words' long
      posting lists are never walked. Worst case is bounded by **bucket** size,
      not corpus size, which is what this item asked for.
      **Why it cannot change a verdict**, checked rather than asserted:
      `similarity()` is `|A ∩ B| / |A|` over *sets*, and the fast path computes
      that same quantity, so it can only skip survivors `similarity()` could
      not have accepted. Corroborated independently of the argument —
      `--replay --only-bulk-deletes` over **749 real commits** gives
      byte-identical output before and after (9 in scope, 4 fired, 16 items,
      same SHAs), and the 35 pre-existing tests pass untouched.
      | items | before | after | verdicts |
      |---|---|---|---|
      | 500 | 2.4 s | 0.10 s | 455 = 455 |
      | 5,000 | 217.6 s | 6.5 s | 3,018 = 3,018 |
      **The regression test was proved to fail against the old code**, not
      merely to pass against the new: `BoundedTime` in `test_harvestscan.py`,
      same shape as the guard layer's `BoundedMemory` classes but on wall time,
      measured 79.5 s against its 15 s ceiling on the pre-fix implementation.
      A test that passes both before and after is not a regression test.
      🔎 **The item's own suggested bucket keys were tried and rejected with a
      reason** — leading number, title prefix, normalised first words all
      change under a retitle, which must still match and which an existing
      test pins. That is worth keeping: the item's illustration would have
      reintroduced the title-matching failure mode this tool exists to avoid.
      **None of the three forbidden shortcuts was taken:** no sampling, no
      raised ceiling, no item-count cap.
      Rule-4 `⏳` at `160/400`; this run may not take it.
