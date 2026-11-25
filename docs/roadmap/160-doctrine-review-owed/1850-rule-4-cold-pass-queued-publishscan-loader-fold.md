- [ ] ⏳ **Rule-4 cold pass queued: `publishscan`'s ignore loader folded into `allowmarker` (`210/590`).** The authoring session (f8dd3843,
      `atelier-31`, Opus 5.5, principal-opened by `/atelier:work run`, whose Sonnet worker wrote it)
      queues this and neither briefs nor takes it.
      *Tier:* Fable, the principal-named review tier, checked at selection; it runs only on
      his approval (the general Fable hold).
      *Pass type:* code, per `method/REVIEW.md` rule 4: does every scanner read its ignore file exactly as
      before, and does `publishscan` keep every refusal byte for byte (PA3, C1F3/PA4, PL7).
      The item asked that it join the next scanner cold pass, so a drain may batch it with one.
      *Delta, scoped to paths:* `tools/allowmarker.py`, `tools/publishscan.py`, `tools/test_allowmarker.py`: every commit on `main` after `a033f023` up to and
      including the commit that lands this pointer.
      *Intent record:*
      [`../210-instruments-open-features/590-publishscan-keeps-its-own-ignore-loader.md`](../210-instruments-open-features/590-publishscan-keeps-its-own-ignore-loader.md).
