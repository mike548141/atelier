- [ ] 🔎 **The generated index fails two of the floor's own scanners, and only
      atelier's `scope` block hides it** — reported by `faves` 2026-08-17, the
      first child to adopt the board. Sibling of `060`: same root, different
      strings. `board.py` emits an index that **cannot pass `wrapscan` or
      `pathscan` in a repo without a `scope` block**, and atelier has one
      (`.atelier-floor.json` scopes both to `docs/method|build|decisions`), so
      neither has ever fired here.
      🔎 **Measured in `faves`, which runs both repo-wide:**
      **`wrapscan`** — `GENERATED_LINE` is **115 columns** against the estate's
      85-column house limit, and index lines carry a title plus a path, so eight
      lines were over. It **blocked the commit that landed the split**, and the
      block is unfixable in place: rewrapping by hand is undone by the next
      `rebuild`.
      **`pathscan`** — the index renders link *text* as a path-shaped string
      (`[040-theme-2-location-maps/README.md](roadmap/040-theme-2-…)`), so
      pathscan resolves the text half from `docs/` and finds nothing: **49
      findings, one per section, on every commit, none of them real.** Warn-only,
      so it does not block — which is worse. A check that always fires is a check
      nobody reads, and this board has already recorded that failure twice.
      🎯 **The fix is upstream in the generator, not downstream in each child.**
      `faves` opened two holes in its own boundary to land the split
      (`.wrapscanignore` and `.pathscanignore`, each entry reasoned in the file
      that opens it), and every child after it will open the same two. Options,
      cheapest first: wrap the banner and keep index lines inside the house
      width; render link text as the item's *title* rather than its filename
      (which also reads better); or, if the shape is deliberate, have `board.py`
      **declare the exemption itself** — the generator emitting the marker for
      the lines it generates, rather than 40 clones each hand-writing an ignore
      file to accommodate one tool's output.
      ⚠️ **What a fix must not do:** silence the scanners over the whole board.
      `faves` scoped both exemptions to the generated file alone —
      hand-written prose under `docs/roadmap/` is still scanned, which is where
      the signal actually is. `linkscan`, which checks the links themselves
      rather than their text, stays enforced and passes.
      🔑 **The class, stated with `060`'s:** *a generator writes text that is
      read by tools it was never written for.* `060` is the reader being human;
      this is the reader being another scanner in the same floor. Both are
      invisible in atelier and unavoidable in a child, so the first rollout pays
      for them — worth fixing before `ros` and `shed` (item `030`) rather than
      after, or the fleet accumulates one ignore-file pair per repo to
      accommodate a string this board could simply stop emitting.
