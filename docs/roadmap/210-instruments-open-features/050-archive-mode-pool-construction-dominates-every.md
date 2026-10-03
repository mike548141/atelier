- [x] 🔎 **Archive-mode pool construction dominates every `--from-archive` run,
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
      ---
      ✅ **FIXED 2026-10-03 (queue run, merge `6cbf33f`). Both named causes
      are gone.** The dataless check is now **one batched `stat -f '%f\t%N'`
      per 400 paths** instead of one spawn per mirror. It reads the same
      `SF_DATALESS` bit, and an unreadable path counts as not dataless, as
      before. The cwd sniff now **inflates only a compressed prefix**, with
      `Z_SYNC_FLUSH`, doubling the prefix until 64 KB of text comes out. Once
      the prefix is the whole file it falls back to the strict gunzip, so a
      truncated mirror still fails as it did. Profiled first: the spawns cost
      about 15 ms each, roughly 14.7 s across 960 mirrors.
      **Measured:** `--list --from-archive --all` went from **14.3–17.7 s to
      6.9–7.8 s** over three back-to-back pairs on a loaded machine. The
      output was byte-identical in every pair, and the batched flags matched
      per-file `stat` on all 960 mirrors. 82 tests pass, four of them new.
      ⚠️ **A side effect, disclosed.** The worker's first profiling script
      read every mirror, which **pulled evicted iCloud mirrors back down**.
      The tool itself never does this. They re-evict over time, and nothing
      was lost, but it is the hazard this tool's own comments warn about,
      met by a probe.
      The remaining ~7 s is a different code path, filed as `180`.
