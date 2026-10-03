- [x] 🔥 **pathscan and linkscan are unbounded on one large file**
      `[S][tools]`. Measured 2026-10-03 (`100` part 1, scale) on synthetic
      files. pathscan grew past 1 GB on a 500 MB file, because it reads
      whole files (`md.read_text` and then `scan_text`) and keeps every
      finding. linkscan grew past 500 MB, because it keeps every finding
      uncapped and resolves each link separately. **The fix this item
      builds:** both stream through the bounded line reader and the finding
      cap the other guards already use, and linkscan caches resolved
      targets. Output must stay identical on atelier's tree, and both must
      hold flat memory on the synthetic files.
      ---
      ✅ **FIXED 2026-10-03 (merge `6b1dc9a`).** Both guards now read through
      the chunked line reader (a 256 KiB window with 4 KiB overlap, copied as
      `115/220` keeps the readers separate). They cap materialised findings
      at 50,000 with the true total reported, and carry fence state across
      chunk edges. pathscan judges a token cut by a window edge once, never
      as a fragment, and memoises resolution per file. linkscan memoises
      resolution per (directory, path), bounded, and keeps at most 2 paths
      per basename (enough for `_suggest`).
      **Measured on the synthetic stress files (hard kill at 300 s):**

      | File | Guard | Before | After |
      |---|---|---|---|
      | 500 MB, long lines | pathscan | killed, >1 GB and rising | 170 s, 46 MB |
      | 500 MB, long lines | linkscan | killed, rising | 92 s, 47 MB |
      | 200 MB, no newline | pathscan | killed, 680 MB | 54 s, 28 MB |
      | 200 MB, no newline | linkscan | killed, 138 MB | 21 s, 52 MB |

      Output is unchanged on atelier's tree, except a known-zero over-cap
      count now prints on every run, as the sibling guards do, so runs
      compare side by side. The full suite is 1,663 OK on the merged tree.
      **Named residuals** (in the README): on lines over 16 KiB, pathscan's
      blanking runs one pass per pattern, which differs from the exact loop
      only for adversarial nesting. A token over 4 KiB can be lost at a
      window cut. linkscan's basename index still scales with tree size.
      The same quadratic reader in three other guards is `140`.
