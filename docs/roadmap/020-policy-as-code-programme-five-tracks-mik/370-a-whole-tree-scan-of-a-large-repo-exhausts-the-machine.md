- [x] 🔥 **DEFECT — `secretscan`'s memory grows with what it scans: ~9 GB over
      one large repo, enough to thrash the principal's machine** — found
      2026-09-18 by the queue run that caused it, reported by a peer session in
      another repo; reframed as a defect on Mike's ruling, 2026-09-19.
      **Mike, verbatim:** *"that means there is a defect in secretscan, it
      should not matter how much it scans it should no have this affect. Put
      work on the board to fix that, and the same for all the other guards"*.
      The other guards are `020/380`.

      **What happened.** An estate probe (old vs new scanner, every sibling
      repo) ran `secretscan` over each repo's working tree. One sibling holds
      several GB, mostly untracked data plus a very large tracked CSV. A single
      `secretscan` process over it reached ~9 GB resident after ~56 minutes; a
      second, unrelated session's run over the same repo sat at the same size.
      With the probe's `leakscan` beside them they pushed a 16 GB machine ~21 GB
      into swap at load 54. A peer session traced the processes; they were
      killed.

      **The requirement (the ruling, stated as a testable property):** a
      guard's peak memory is bounded by a constant that does not grow with the
      size of the tree or of any one file, and its running time grows no
      faster than linearly with the bytes it reads. How big the input is must
      never be a reason a machine suffers. Excluding the large repo, or
      scanning only tracked content, works around the defect and does not fix
      it.

      **Where the memory plausibly goes — read from the code at `63e27b3`, NOT
      yet measured; the fix starts by measuring:**
      - `iter_files()` builds the whole tree's file list up front
        (`base.rglob("*")` into a list) instead of streaming it.
      - `scan_paths()` holds each file whole three times at once:
        `read_bytes()`, then the decoded `str`, then `scan_text`'s
        `splitlines()` list. For a multi-GB CSV that is several times the
        file's size.
      - Every finding is kept in one list until the end. The large repo
        produced ~43,000 advisory findings, each carrying its path and
        excerpt.
      - A whole-tree walk reads untracked and gitignored content (build
        output, data dumps) that CI never sees, which is `020/160`'s question
        from another direction.

      **Owed:**
      1. Measure peak memory (`tracemalloc` / `resource.getrusage`) against a
         synthetic large tree — one huge single-line file, one huge many-line
         file, many small files, and a tree that produces many findings. Name
         which of the causes above are real.
      2. Fix to the requirement: stream files line by line (bounded line
         length, with overlong lines reported rather than dropped silently),
         stream the walk, and emit or aggregate findings instead of holding
         every one. Where a limit is unavoidable, the output says what was
         skipped and why — **never silently**.
      3. A regression test that fails when peak memory on the synthetic large
         input exceeds a bound grounded in the design (per line or per file),
         not in whatever today's measurement happens to be.
      4. The same test shape becomes the template every guard in `020/380`
         reuses.

      **Interim, and only interim:** an estate-wide probe scans tracked content
      (`git archive HEAD`), one process at a time. That practice retires when
      this item and `020/380` land.

      ✅ **DONE 2026-09-20.** All three suspected causes measured real and
      each isolated on its own: the up-front file list (~1 KiB held per file,
      +54 MB at 60,000 files over a 10,000-file baseline), the three-copies-
      per-file read (a clean 32 MB/400k-line file peaked the OLD code at
      134 MB, ~7.5× the file), and the findings list (~700 B each; 400,000
      findings cost ~283 MB on their own, more than assumed at filing).
      **Peak RSS, before → after:** 114 → 42 MB (32 MB single line) · 432 →
      52 MB (32 MB of short lines) · 83 → 23 MB (60,000 files) · 304 →
      61 MB (dense findings, cap engaged and reported).
      **The fix:** `os.walk` with in-place `dirnames` pruning streams the
      tree (and stops descending into skipped dirs rather than discarding
      them after); a fixed 1 MiB read feeds a 4 MiB line window with a
      64 KiB overlap, so a token straddling a window cut is whole in one of
      the two, and an overlong line is *windowed* rather than truncated;
      findings past a fixed 50,000 cap are **counted, never dropped**, with
      the overflow stated in the output and the exit code and advisory total
      read off the counters rather than `len(findings)`.
      **The test:** `test_secretscan.py::BoundedMemory` runs the real CLI
      over 1 MiB vs 8 MiB of clean input and asserts growth under
      `4 × (window + overlap)` ≈ 17 MB — derived from the one buffer the
      reader ever holds, not fitted to a measurement, and checked to
      discriminate (pre-fix code measures 2.3× over it, fixed code 10–17×
      under).
      **Output equivalence verified, not asserted:** old and new scanners run
      over this repo's `docs/` and `tools/` trees produce identical JSON
      counts.
      **The interim practice retires when `020/380` lands, not here** — the
      `git archive HEAD`, one-process-at-a-time estate probe stays until every
      other guard is measured.
      *review: queued as a code cold pass, `160/350`.*
