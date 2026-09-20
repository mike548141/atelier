- [~] (claimed 2026-09-20-1053, wt: at-harvestscan-linear) 🔥 **`harvestscan`'s vanished-item check is quadratic in the number of
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
