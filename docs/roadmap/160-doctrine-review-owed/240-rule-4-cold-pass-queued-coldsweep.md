- ⏳ **Rule-4 cold pass queued — `coldsweep.py`, the cold-sweep exclusion
      guard.** First-of-kind build, queued at landing by its author, who may
      not take it. *Tier:* Fable, the principal-named review tier — checked at
      selection; a session that cannot honour the bar stops rather than takes.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta — scoped to paths, deliberately not to the commit:*
      `tools/coldsweep.py` · `tools/test_coldsweep.py` · `tools/README.md`
      § *`coldsweep.py`* · `docs/method/REVIEW.md` rule 2's sweep clause ·
      `CHANGELOG.md`.
      *Intent record:* board item
      `290-ruling-round-2026-08-17-the-cold-run-find/040-build-the-cold-sweep-guard.md`,
      carrying the principal's ruling — background the reviewer's own deferral
      discipline governs, never part of the delta.
      🚩 **The reviewer should weigh one thing the author cannot:** this guard
      makes the safe path easier but does not make the unsafe path fail, so a
      reviewer that reaches for `grep` out of habit is unprotected. Whether
      that is the right altitude for the ruling, or whether the guard should
      also detect a bare sweep, is a lens-1 question the build did not decide.
      Brief written 2026-08-17 by a non-author cold session on the Fable tier —
      REVIEW NOT RUN, open for a cold Fable taker:
      `docs/reviews/2026-08-17-1000-coldsweep-cold.md`
      (deferred sibling `docs/reviews/2026-08-17-1000-coldsweep-cold.deferred.md`,
      opened only after the reviewer's findings are durably written; finding
      prefix `SW`; wt: cold-run-0817-0955). Two brief-writer disclosures stand
      in it: the `SESSIONS.md` tail was read at onramp before the brief was
      commissioned, and the landing commit's message was read in full.
