- [ ] 🔎 **Archive-mode pool construction dominates every `--from-archive` run,
      and `--search` only made it visible** (found 2026-08-09; **pre-existing**).
      `--list --from-archive --all` costs **16.4 s before any searching**, and
      11.5 s of a 13.9 s archive search happens before a single hit is scored.
      Two causes, both in `sessionRecord`: `isDataless()` spawns one `stat(1)`
      subprocess **per mirror** (560 of them), and `cwdFromLog()` **fully gunzips
      every mirror** for a 64 KB cwd sniff — which the sweep then repeats. The
      fixes are a single batched `stat` and either caching or streaming the sniff.
      Queued rather than folded into the search build: it is a different file's
      hot path, and the honest reason `--search` is slow on the archive plane is
      not the search.
