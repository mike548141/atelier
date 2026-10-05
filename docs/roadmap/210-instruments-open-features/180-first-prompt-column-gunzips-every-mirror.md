- [x] 🔎 **`--list --from-archive` still fully gunzips every local mirror for
  its first-prompt column** (found 2026-10-03 by the worker that fixed `050`;
  measured, not built)

  With `050`'s two causes fixed, the listing still takes about 7 s. A CPU
  profile puts zlib at about 4 s, UTF-8 slicing at about 1.7 s, and
  `firstUserPromptText` at about 1.6 s. That function decompresses each
  locally present mirror **in full** to find the first user prompt for the
  listing's column. The prefix inflate `050` added (`gunzipHead`) is the
  obvious tool. A first prompt can sit beyond any fixed prefix, though, so
  a prefix read needs a bound and a whole-file fallback, the way the cwd
  sniff has one. `--search` on the archive plane pays the same full-gunzip
  cost per mirror, and that has not been measured.

      ✅ **Built and merged 2026-10-05** (queue run, a Sonnet 5.5 worker;
      commit `83d9b0b`). `firstUserPromptText` now reads a `.gz` mirror
      through `gunzipHead` with a 64 KB bound, and searches only the complete
      lines of that prefix. When the prefix holds no prompt, it falls back to
      the whole-file read, which is the old behaviour unchanged. So the bound
      is a speed path and can never change an answer. The bound comes from a
      census of 983 local mirrors: the first prompt ended within 64 KB in all
      but 24, and the tail beyond that was flat. 64 KB also matches the cwd
      sniff.

      **Evidence.** Text and `--json` listing output were byte-identical
      before and after, three runs each. Old and new functions returned the
      same string on all 983 mirrors. Listing CPU fell from about 27 s to
      about 7 s. Wall time was noisy on a loaded machine, and the 7 s this
      item quoted did not reproduce. There are five new tests (inside the
      prefix, beyond it, no prompt, no trailing newline, corrupt mirror), and
      all 87 cctranscript tests pass.

      **One behaviour difference, accepted.** Before, a corrupt mirror whose
      first prompt sits in its intact prefix aborted the whole listing. Now it
      lists a row. One whose prefix holds no prompt still throws as before.
      This is the same trade the cwd sniff already makes, and it leans the
      same way as the skip-and-report shape ccarchive was hardened to
      (`210/210`), rather than letting one bad file stop the whole listing.

      **Left alone, measured.** `--search` uses a different function: a
      whole-text gate whose miss can only be proven by reading everything. A
      prefix cannot be output-identical there. One miss-term search over the
      983 mirrors took 51 s wall and about 21.5 s CPU. Going faster would need
      a cache or an index, which is a design question and is not filed.
