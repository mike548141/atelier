- [x] **Rule-4 cold pass queued: the `cctranscript --search` fixes, CS1–CS14 (`210/580`).** The authoring session (f8dd3843,
      `atelier-31`, Opus 5.5, principal-opened by `/atelier:work run`, whose Opus worker wrote it)
      queues this and neither briefs nor takes it.
      *Tier:* Fable, the principal-named review tier, checked at selection; it runs only on
      his approval (the general Fable hold).
      *Pass type:* code, per `method/REVIEW.md` rule 4: each CS finding against its fix, above all the
      `--regex` gate's safety check (can any pattern it calls safe match decoded text the raw
      log hides?), and CS13, the design never reviewed before it was built to.
      *Delta, scoped to paths:* `instruments/cctranscript`, `instruments/cctranscript.test.js`,
      `instruments/man/cctranscript.1`, `instruments/cctranscript.search.design.md`,
      `instruments/README.md`, `CHANGELOG.md`: every commit on `main` after `a033f023` up to and
      including the commit that lands this pointer.
      *Intent record:*
      [`../210-instruments-open-features/580-fix-cctranscript-search-cs1-cs14.md`](../210-instruments-open-features/580-fix-cctranscript-search-cs1-cs14.md).
      **Dequeued 2026-11-27 ~01:55 UTC (board `460/040`; session 4ce066ba, `atelier-c1`,
      AskUserQuestion; an answer to options Claude wrote, not a ruling), not run.** His pick,
      verbatim: *"Drop 8, merge 6 (Recommended)"* (option text: *"31 reviews stay in Monday's
      drain. Takes back your earlier picks on 4 of them. Saves roughly 8 Fable passes of
      budget; the 6 merged ones still get reviewed, just together."*). Under the bar in
      `method/REVIEW.md` § *Whether work earns a review at all*, this is a re-check of fixes
      whose pass returned no MAJOR (its worst was MODERATE). The round marked this one weaker
      than the rest: the pointer also asks for a first look at CS13, a design never reviewed
      before it was built to.
      review: not warranted — a re-check of fixes whose pass returned no MAJOR
