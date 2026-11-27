- [x] **Rule-4 cold pass queued: `floor.py` refuses the bare-list spelling
      of `advisory`, `scope` and `flags` (C1 phase 2, `020/070`), and prints
      its own coverage line (`115/130`).** The authoring session (queue run
      78ca9153, Opus 5.5, principal-opened, 2026-11-16 UTC, which dispatched
      the worker that wrote it) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection; the
      pass waits for his explicit permission for Fable work.
      *Pass type:* cold pass on a blocking guard's behaviour change, per
      `method/REVIEW.md` rule 4: children fetch the floor at `@main`, so the
      refusal reaches every child's next CI run.
      *Delta, scoped to paths:* `tools/floor.py`, `tools/test_floor.py`,
      `tools/README.md`: the commit that closes `020/070`, on `main`.
      *What to test hardest:* the zero-users premise (the worker and the
      orchestrator each counted 0 bare-list uses across 22 sibling configs on
      2026-11-16; a child cloned later or a config outside the sweep is the
      gap); the `--json` field set lost `legacy` with no consumer found; the
      coverage line counts checks run, not the scanners' own coverage lines;
      `floorfleet.py` still words a bare list as "migrate it".
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
      reds on misuse: `floor.py` now refuses the bare-list spelling, so a config still using
      it fails loud; the census found 0 users. This takes back his earlier pick on this pass,
      *"API credit if parity"* (2026-11-17 UTC, recorded above); the option text he chose on
      2026-11-27 says so.
      review: not warranted — a tightening that reds on misuse; the census found 0 users
