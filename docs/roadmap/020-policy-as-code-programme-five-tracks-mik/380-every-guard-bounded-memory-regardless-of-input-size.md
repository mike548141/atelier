- [~] (claimed 2026-09-20-0620, wt: three workers; registered floor guards first) 🔥 **Every guard runs in bounded memory, whatever it is pointed at** —
      Mike's ruling, 2026-09-19, extending `020/370` from `secretscan` to the
      whole guard layer: *"it should not matter how much it scans it should no
      have this affect. Put work on the board to fix that, and the same for all
      the other guards"*.

      **The requirement** is `020/370`'s, applied to each guard: peak memory is
      bounded by a constant that does not grow with the size of the tree or of
      any one file; running time is at most linear in the bytes read; anything
      skipped to honour a limit is reported, never silent. `020/370` builds the
      measurement harness and the regression-test template first, and each
      guard below reuses it rather than inventing its own.

      **Evidence so far:** one guard measured bad (`secretscan`, ~9 GB). A
      second is suspect: the same run's `leakscan` probe over the same repo was
      also heavy, though never measured on its own. The rest are **unmeasured,
      not known good**. Several share `secretscan`'s shapes — whole-file reads,
      tree walks with name-only directory skips (`020/160`), findings held
      until the end — so assume the class until each one is measured.

      **Per guard — measure, fix to the requirement, pin with the regression
      test (the registered floor guards first, since they run on every commit
      and CI in every repo):**
      - [x] `leakscan` — fixed — 3 causes, +44 MB → +1.3 MB on a 23 MB many-line file (suspect — scanned the same large repo)
      - [x] `conflictscan` — fixed — +28 MB → +1.1 MB, and its exit-2-on-OSError contract kept (new 2026-09-18; the worker reported a multi-minute
            scan of the large repo, so it walks the same way)
      - [ ] `linkscan`
      - [ ] `reviewscan`
      - [ ] `publishscan`
      - [x] `sizescan` — fixed — 110 MB → 0.7 MB (many lines), 48 MB → ~0 (one line)
      - [ ] `board`
      - [x] `datescan` — fixed — 268 MB → under an 8.5 MB design bound on the one-line case
      - [x] `wrapscan` — fixed — same shape; truncation at the 8 KiB line cap is counted, and the residual on a truncated line's column count is documented inline
      - [x] `spellscan` — fixed — and the batch's real find: its path/URL regex backtracked catastrophically, 107 s on one 1 MB line, now under 1 ms on 200,000 chars
      - [ ] `harvestscan`
      - [ ] `pointerscan`
      - [ ] `pathscan`
      - [ ] `licenscan`
      - [ ] `stampscan` and `signscan` (guards outside the floor registry)
      - [ ] `floorfleet`, `signfleet`, `pins` — fleet tools, not guards, but
            they walk every sibling repo, so they fall in the same class

      **Close condition:** every box above is either fixed and pinned by the
      shared regression test, or measured, shown bounded by the test, and
      ticked with that evidence. "Looks fine by reading" does not tick a box.
      Split any guard into its own item if its fix proves bigger than one
      sitting.

      **Progress, 2026-09-20.** Six ticked above, each measured before and
      after, each regression test confirmed to FAIL against the pre-fix file,
      and each scanner's output verified identical over this repo's `docs/`
      and `tools/` trees. All six carried `secretscan`'s exact defect shape,
      so all six take its fix rather than inventing their own — the
      convergence the item asked for.
      🔎 **The class is wider than memory, and that was found by accident.**
      `spellscan` could be stalled, not just bloated: a whole-line regex of
      the shape that backtracks catastrophically took **107 seconds on one
      1 MB line** and timed out a 120-second harness. A guard an input can
      stall is the same defect as one an input can exhaust — the requirement
      already says *linear in the bytes read*, and nobody was reading it that
      way until a memory probe hit a timeout. Every later batch is asked to
      look for that shape while it is in each file.
      **In flight:** `linkscan`/`reviewscan`/`publishscan`, then
      `board`/`harvestscan`/`pointerscan`/`pathscan`/`licenscan`, then
      `stampscan`/`signscan`/`blockscan` with the three fleet tools.
      **`blockscan` (new 2026-09-20) belongs on this list** and is covered by
      the last batch, though it has no box above yet.
