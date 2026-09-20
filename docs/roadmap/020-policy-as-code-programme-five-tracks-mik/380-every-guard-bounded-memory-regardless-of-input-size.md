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
      - [ ] `leakscan` (suspect — scanned the same large repo)
      - [ ] `conflictscan` (new 2026-09-18; the worker reported a multi-minute
            scan of the large repo, so it walks the same way)
      - [ ] `linkscan`
      - [ ] `reviewscan`
      - [ ] `publishscan`
      - [ ] `sizescan`
      - [ ] `board`
      - [ ] `datescan`
      - [ ] `wrapscan`
      - [ ] `spellscan`
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
