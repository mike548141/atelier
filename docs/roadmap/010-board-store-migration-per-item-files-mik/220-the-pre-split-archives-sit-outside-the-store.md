- [x] **The pre-split archives sit outside the board's store.** Filed
      2026-11-20 by session 19378351. `ROADMAP-DONE.md` was frozen at the
      split (2026-08-15) and still sits in `docs/` in this repo and in about
      a dozen children; three children also keep a `SESSIONS-ARCHIVE.md` in
      the same frozen form. A 2026-11-14 pick left them whole. Mike's words,
      2026-11-20, which change that: *"I think we should find a way that the
      old ROADMAP-DONE.md is either split back out into files to match the
      current design for board work management. Or worst case if that is not
      going to work or ruin the historical record held in ROADMAP-DONE.md then
      we create a theme folder to store ROADMAP-DONE.md in so its not in the
      docs/ folder anymore"*.
      **Measured here, same day:** this repo's archive holds 218 `[x]`
      entries under 62 headings, plus 20 top-level bullets that are not
      entries; 269 tracked files mention it, 83 of them by a markdown link
      that `linkscan` would hold red if the file moved and the link did not.
      **The two routes:** (a) cut every entry into its own `[x]` item file in
      one archive section, its headings kept in that section's `README.md`,
      lossless by the multiset proof `010/030` records, links repointed; or
      (b) move the file whole into an archive section folder, links
      repointed. Route (b) is the fallback where (a) cannot prove itself
      lossless. Both repoint links inside records, which changes a path and
      never the words. Design to be settled with him before any build;
      atelier goes first as the worked example.
      **Route picked 2026-11-20** (Mike's pick from offered options, an
      answer): *"Split, fall back to move (Recommended)"*, covering both
      `ROADMAP-DONE.md` and `SESSIONS-ARCHIVE.md`: route (a) with the
      lossless proof, route (b) for any repo where the proof fails; atelier
      first as the worked example, then the health sweep carries it.
      **atelier's part done 2026-11-20** (a worker of session 19378351):
      `tools/archivecut.py` builds both routes for both archives, and ran
      route (a) here. `docs/ROADMAP-DONE.md` is now
      [`990-done-before-the-split/`](../990-done-before-the-split/README.md):
      218 `[x]` item files, the 62 `## ` headings and every non-entry line
      kept verbatim in its README; the proof passed (multiset of 4,604
      non-heading lines, byte-for-byte rebuild, 63 re-pointed links mapping
      back), and `archivecut --verify` repeats it from disk. 157 links in 27
      files across the tree were re-pointed, records included. The guards
      that named the file now know the section (`sizescan` integrity,
      `pathscan` records, `coldsweep`'s bar, the spelling and wrap ignores).
      A dry run on every child that keeps one of these archives, no writes:
      ten of twelve board archives would cut and two would move whole (no
      `[x]` entries to cut); all three session archives would cut.
      **Still owed, so this stays open:** each child's own cut, run in that
      child by the health sweep (`010/230`), then `--verify` there.
      **Closed 2026-11-20** (session 19378351): every child's own cut ran
      in that child through the health sweep. Eleven board archives cut to
      item files and one moved whole; the session archives cut with the
      session-log retirement (`010/270`). Each proved byte for byte and
      `--verify` passed in the child. Read from every child's
      `origin` head the same day: no `ROADMAP-DONE.md` or
      `SESSIONS-ARCHIVE.md` is left in any `docs/`. Rough edges the runs
      met are in `010/280`.
