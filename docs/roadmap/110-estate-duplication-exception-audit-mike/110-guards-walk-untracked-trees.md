- [~] (claimed 2026-10-03-0547, wt: qr-walk-tracked) 🔥 **The content guards walk the whole filesystem, untracked trees
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
