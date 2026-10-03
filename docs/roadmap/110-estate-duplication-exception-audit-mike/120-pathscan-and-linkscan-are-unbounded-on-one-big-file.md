- [~] (claimed 2026-10-03-0547, wt: qr-bounded-path-link) 🔥 **pathscan and linkscan are unbounded on one large file**
      `[S][tools]`. Measured 2026-10-03 (`100` part 1, scale) on synthetic
      files. pathscan grew past 1 GB on a 500 MB file, because it reads
      whole files (`md.read_text` and then `scan_text`) and keeps every
      finding. linkscan grew past 500 MB, because it keeps every finding
      uncapped and resolves each link separately. **The fix this item
      builds:** both stream through the bounded line reader and the finding
      cap the other guards already use, and linkscan caches resolved
      targets. Output must stay identical on atelier's tree, and both must
      hold flat memory on the synthetic files.
