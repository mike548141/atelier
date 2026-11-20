- [ ] ⏳ **Rule-4 cold pass queued: the session log's one-file index retired
      into `docs/sessions/`, the tool that does it, and atelier's own run.**
      Written by a worker of session 19378351 (Opus 5.5, 2026-11-20 UTC),
      which queues this and does not take it or brief it. **Needs a brief.**
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the principal has said reviews wait for his next weekly drain, so this
      pass waits for it and for his explicit permission for Fable work.
      *Pass type:* code and doctrine cold pass, per `method/REVIEW.md` rule 4.
      *Intent record:* `010/270`; the grace removal is `010/290`.
      *Delta, scoped to paths:* the tool, guards and doctrine commit
      `b68cf410` (`tools/archivecut.py` and
      `tools/test_archivecut.py`; `instruments/ccclose`, its test, design
      doc and man page; `tools/pathscan.py`, `tools/coldsweep.py`,
      `tools/sizescan.py`, `tools/wrapscan.py`; `docs/method/RECORD.md`
      § *The session log*, `docs/method/CONCURRENCY.md`,
      `docs/method/REVIEW.md`, `CLAUDE.md`, `docs/build/REPO-STANDARD.md`,
      the repo template, `skills/create-repo`, `skills/fleet-sweep`), and the
      run `e5f9f245` (the removal of `docs/SESSIONS.md`, 302 session files
      written, `docs/sessions/README.md`).
      *Suggested finding prefix:* `XS` (no collision in `docs/reviews` or the
      board at queuing).
      *What to test hardest:* can the retirement pass its proof and still
      lose or alter a byte (`--verify` from disk against the deleted file's
      last committed copy, and the "existing files unchanged" check); does any
      placed entry's link now point somewhere other than where it did; is an
      entry ever placed in a session file that is not its own (the "only one
      it links" rule); do the new files' names sort by start time, and is the
      day counter honest where no time was stated; does an archive cut by the
      earlier route still verify after the index goes; and can any child go
      red the day this lands (the `ccclose` grace, and the record lists in
      `pathscan`, `coldsweep` and `sizescan`).
