- [x] 🔎 **The generated index fails two of the floor's own scanners, and only
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
      ✅ **`pathscan` half: FIXED 2026-08-17** with `060`, same commit. The
      generator no longer repeats the path as link text — a section now renders
      `*[Narrative](roadmap/<dir>/README.md)*`, and the `##` heading directly
      above it already carries the section's name, so the title option this
      item listed would have re-stated what the reader had just read. Measured,
      not assumed: atelier's index went 28 findings → **0 generator-caused**
      (the one that remains, `F1/GUARDS.md` at `:184`, is a real stale path
      inherited verbatim from an item's own title). In `faves` this is all 49.
      ✅ **`wrapscan` half: ALSO FIXED, and the fix is one line of the
      renderer.** This took a wrong turn first, recorded because the wrong
      turn is the useful part. This item said *"eight lines were over"*; a raw
      column count of `faves`' index says **127 of 291**, and that looked like
      a contradiction worth writing up. It is not one — **the two numbers
      measure different things, and the item's was the right one**: 8 (15
      today) is what the *gate printed*, 127 is what `awk` counts. `wrapscan`
      exempts a line whose overflow is **one unbreakable token**, and an item
      line ends in a store path, so almost every long line in the index was
      already exempt. The peer that filed this item challenged the raw count
      and the reproduction is what found the real cause.
      🔑 **The cause, and it is not the shape of the file:** an item line
      carried its eye-flag *after* the link, so ` 🎯` put a space **after** the
      path — the overflow gained a legal wrap point and the exemption stopped
      applying. Measured in `faves`: **13 of the 14 findings were exactly its
      13 flag-bearing lines**, and nothing else. The renderer now emits flags
      and the claim fragment **before** the link, so every item line ends in
      its path; allow-comments stay trailing, because that is how every
      scanner reads them and such a line exempts itself anyway. The one
      remaining finding was the preamble — real prose — now wrapped at the
      house width. **`faves` 15 → 0. atelier's index: `wrapscan` clean,
      `pathscan` 1 (the real stale path).** A reader also gains a flag column
      that aligns rather than flags tracked to ragged line ends.
      🎯 **So the floor-policy question this item was heading for — does a
      `GENERATED` marker exempt a file from the prose gates fleet-wide — is
      NOT needed for the board, and is not asked.** The index passes both
      scanners unscoped, in any repo, with no ignore file: `faves` can delete
      the `.wrapscanignore`/`.pathscanignore` pair it opened, and `ros`/`shed`
      never write one. The question may still be worth asking for other
      generated files; it is not this item's to force.
      🚩 **The near-miss, which is the reason this paragraph is long.** The
      first reading of the raw 127 said *"unfixable in the generator, escalate
      to a policy ruling"* — a conclusion that would have been wrong, would
      have put an unnecessary decision on the principal, and would have left
      every child writing ignore files forever. What broke it was a peer
      reproducing the number instead of accepting it. **A measurement that
      does not name what it counted can falsify a correct report and buy an
      unnecessary ruling.**
