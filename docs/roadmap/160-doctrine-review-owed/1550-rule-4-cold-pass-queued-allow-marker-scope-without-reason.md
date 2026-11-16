- [ ] ⏳ **Rule-4 cold pass queued: an allow-marker scope with no reason
      exempts nothing (`115/230` item 1).** The authoring session (queue run
      78ca9153, Opus 5.5, principal-opened, 2026-11-16 UTC, which dispatched
      the worker that wrote it) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection; the
      pass waits for his explicit permission for Fable work.
      *Pass type:* cold pass on a shared guard module's behaviour change, per
      `method/REVIEW.md` rule 4: every scanner reads markers through it, and
      children run it at `@main`.
      *Delta, scoped to paths:* `tools/allowmarker.py`,
      `tools/test_allowmarker.py`, `tools/datescan.py` and `tools/pathscan.py`
      (docstrings), `tools/README.md`: the commit that lands `115/230` item 1,
      on `main`.
      *What to test hardest:* the new no-reason pattern's edges (a scope
      followed by `-->`, a full stop, a quote, a second marker on the line);
      the claim that no grace was needed rests on a census of tracked files in
      atelier and 29 siblings on 2026-11-16 (0 markers changed); the adjacent
      shapes left as they were (`m:allow:kind why` with no colon, 5 markers in
      one sibling; `covers()` widening on a reasoned marker with no named kind).
