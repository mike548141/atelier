- [x] **Rule-4 cold pass queued: an allow-marker scope with no reason
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
      *Approval:* the principal, 2026-11-17 UTC, through the device at the
      authoring run's close, his pick verbatim: *"API credit if parity"*
      (option text: *"Run them on the API credit lane where a pass can match
      laptop quality; any that can't wait for the drain."*). So: on the API
      credit only, where the pass reaches laptop parity; a pass that cannot
      waits for his next weekly drain. The authoring run (78ca9153) neither
      briefs nor starts it.
      **Dequeued 2026-11-27 ~01:55 UTC (board `460/040`; session 4ce066ba, `atelier-c1`,
      AskUserQuestion; an answer to options Claude wrote, not a ruling), not run.** His pick,
      verbatim: *"Drop 8, merge 6 (Recommended)"* (option text: *"31 reviews stay in Monday's
      drain. Takes back your earlier picks on 4 of them. Saves roughly 8 Fable passes of
      budget; the 6 merged ones still get reviewed, just together."*). Under the bar in
      `method/REVIEW.md` § *Whether work earns a review at all*, this is a tightening that
      reds on misuse: a scope with no reason now exempts nothing, so the scanner reports the
      line it used to pass; the census changed 0 markers. This takes back his earlier pick on
      this pass, *"API credit if parity"* (2026-11-17 UTC, recorded above); the option text he
      chose on 2026-11-27 says so.
      review: not warranted — a tightening that reds on misuse; the census changed 0 markers
