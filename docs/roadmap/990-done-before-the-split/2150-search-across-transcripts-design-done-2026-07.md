- [x] **Search across transcripts — DESIGN DONE 2026-07-27, BUILD not started
      (Mike's ask, 2026-07-26).** *"Something that lets you search all the
      transcripts using regex or for a simple term. If you give cctranscript a
      command like `--repo` that limits the scope to search within."* The design
      pass is done — surface (`--search` + `--regex`/`--case`), match unit,
      excerpting, output shape, cost, eviction and DONE conditions are all settled
      there. **No decision is left open for Mike.** What remains is the build.
