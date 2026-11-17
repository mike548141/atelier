- [ ] ⏳ **Rule-4 cold pass queued: leakscan's G3 reads Office and PDF
      metadata, warning until 2027-01-18 (`115/390`).** The authoring session
      (queue run 78ca9153, Opus 5.5, principal-opened, 2026-11-16 UTC, which
      dispatched the worker that wrote it) queues this and does not take it.
      Built on the principal's answer *"Build the reader"*, whose option named
      this review.
      *Tier:* Fable, the principal-named review tier, checked at selection; the
      pass waits for his explicit permission for Fable work.
      *Pass type:* cold pass on a blocking guard's new read surface, per
      `method/REVIEW.md` rule 4: it parses untrusted zip, XML and PDF bytes,
      and children run it at `@main`.
      *Delta, scoped to paths:* `tools/leakscan.py` (the *G3 documents* block),
      `tools/test_leakscan.py`, `tools/test_report.py`, `tools/README.md`: the
      commit that closes `115/390`, on `main`.
      *What to test hardest:* the parsers' bounds (zip directory checked
      before `zipfile` opens it, 1 MiB per part, DOCTYPE and entities refused,
      PDF read in 1 MiB windows under a 64 MiB inflation cap; unreadable reads
      `unknown`, never clean); that nothing new blocks before
      `DOCUMENT_UNTIL`, 2027-01-18; the estate probe (no sibling's blocking
      findings or exit code changed; 53 new warnings in 3 siblings); two
      open choices: Office and PDF Info fields gate only where they name a
      person or organisation while PDF XMP gates every field, and the reader
      is about 700 lines against the 300–450 estimate.
      *Approval:* the principal, 2026-11-17 UTC, through the device at the
      authoring run's close, his pick verbatim: *"API credit if parity"*
      (option text: *"Run them on the API credit lane where a pass can match
      laptop quality; any that can't wait for the drain."*). So: on the API
      credit only, where the pass reaches laptop parity; a pass that cannot
      waits for his next weekly drain. The authoring run (78ca9153) neither
      briefs nor starts it.
