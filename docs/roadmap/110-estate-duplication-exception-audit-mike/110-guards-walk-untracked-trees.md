- [x] 🔥 **The content guards walk the whole filesystem, untracked trees
      included, and that is what makes them run for hours** `[M][tools]`.
      Measured 2026-10-03 (`100` part 1, scale). `tools/filewalk.py`'s
      `walk_files` is an `os.walk` that prunes ten fixed directory names and
      never asks git what is tracked or ignored. One private repo has 132 MB
      tracked and 15.8 GB walked, so secretscan, leakscan and conflictscan
      all ran past a 300 s cap. It feeds nine guards. **The fix this item
      builds:** in a git tree, enumerate files by streaming `git ls-files -z
      --cached --others --exclude-standard`. That is the tracked set plus
      untracked files that are not ignored, everything that *could* be
      committed. Keep the `os.walk` fallback outside git. A gitignored file
      can never be committed, so dropping it loses no protection. Every
      guard's output must stay identical on atelier's tree, and the large
      repo must finish inside the cap.
      ---
      ✅ **FIXED 2026-10-03 (merge `bd9bd49`).** Inside a git work tree,
      `walk_files` now streams `git ls-files -z --cached --others
      --exclude-standard`, with git's environment scrubbed so a hook's
      `GIT_DIR` cannot redirect it. Per-guard skips and the linked-worktree
      prune still apply. Deleted-but-cached paths drop out. Symlinks behave
      as before. A nested clone or submodule is still walked as before
      (FW9 unchanged). Outside git, or with git missing, it falls back to
      `os.walk`. A missing git says so on stderr, and a git failure partway
      through raises instead of returning a shortened list.
      **Evidence:**
      - All eleven filewalk guards are byte-identical on atelier's tree.
      - On a synthetic repo, 2,007 files went to 6, the 2,000 dropped being
        the gitignored junk.
      - The full suite gave 1,637 OK, and `test_filewalk` is new, with 15
        tests.
      - **On the large private repo** (128 MB tracked in 1,834 files,
        15.7 GB untracked), the three guards that hit the 300 s cap now
        finish: secretscan in **139 s / 43 MB**, leakscan in **231 s /
        60 MB**, conflictscan in **77 s / 43 MB**.
      The remaining cost is per byte, about 0.5–1 MB/s on regex scanning,
      filed as `130`.
