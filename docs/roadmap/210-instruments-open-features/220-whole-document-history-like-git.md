- [ ] 💡 **IDEA ONLY — do not build until Mike says to start: keep whole
      documents (memory notes and the like) as a version history, more like
      git** (Mike, 2026-10-05, mid-run)

      His words: *"I wonder if the memory notes (and similar use cases) should
      be more like a git history. Something to consider"*, then *"Or a diff
      maybe"* — so the shape is open between full versions and stored diffs.

      Context at filing: ccarchive mirrors each file as one compressed copy,
      which suits append-only transcripts. Memory notes are whole documents
      that get rewritten, so a single mirror either refuses the rewrite or
      loses the older wording. The `210/210` hardening build answers the
      shrink case with a dated copy of the old version; this item asks whether
      every whole-document class should instead keep a full, browsable
      history of every version. Not scoped, not designed.
