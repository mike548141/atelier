- [ ] ⏳ **Rule-4 cold pass queued: `tools/archivecut.py` and atelier's cut
      of its pre-split board archive into
      `docs/roadmap/990-done-before-the-split/`.** Written by a worker of
      session 19378351 (Opus 5.5, 2026-11-20 UTC), which queues this and does
      not take it or brief it. **Needs a brief.**
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Intent record:* `010/220`.
      *Delta, scoped to paths:* `tools/archivecut.py`,
      `tools/test_archivecut.py`, `tools/sizescan.py` (`is_archive_path`
      and its call sites), `tools/test_sizescan.py`, `tools/pathscan.py`
      (`RECORDS_GLOBS`), `tools/coldsweep.py` (`BARRED`), `.spellscanignore`,
      `.wrapscanignore`, `docs/build/templates/docs/ROADMAP.md`,
      `docs/build/REPO-STANDARD.md`, `docs/PERSONAL-DATA.md`, the
      `tools/README.md` sections that name the archive, and the cut itself
      (the removal of `docs/ROADMAP-DONE.md`, the new section, the link
      re-points): the commit that adds this item and its parent, which
      adds the tool; widened 2026-11-20 by the commit closing `010/260`
      (`docs/method/RECORD.md`, four places reworded to the store form).
      *Suggested finding prefix:* `XC` (no collision in `docs/reviews` or the
      board at queuing).
      *What to test hardest:* can a cut pass its proof and still lose or
      alter a byte (`--verify` from disk against the deleted file's last
      committed copy); does any link re-point change a word rather than a
      path, or leave a link pointing somewhere other than where it did; is
      the fallback reached on every input the proof cannot carry; is the
      session-archive route sound on shapes the synthetic fixtures do not
      cover; and does the harvest-integrity gate now read the whole section
      on both planes.
