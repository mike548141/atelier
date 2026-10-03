- [x] 🔥 **leakscan, secretscan and conflictscan's line reader re-slices
      the remaining buffer for every line, so long runs of short lines cost
      quadratic time** `[S][tools]`. Found 2026-10-03 by the worker fixing
      `120`. linkscan carried the same reader: on 51 MB of ordinary short
      lines the old linkscan did not finish in 120 s, and the fixed one takes
      8 s. The three guards that still carry it are the ones `130` measured
      at about 0.5–1 MB/s, so this is the likely first cause there, ahead
      of the regex cost. **The fix this item builds:** port linkscan's linear
      reader into the three, with per-guard window and overlap kept as they
      are (`115/220` keeps the readers separate), output byte-identical on
      atelier's tree, and the large private repo re-timed.
      ---
      ✅ **FIXED 2026-10-03 (queue run).** linkscan's offset-walk reader has
      been ported into the three guards, with constants unchanged and the
      copies kept separate. Output is byte-identical on atelier's tree for
      all nine guard × mode runs. The full suite is 1,669 OK.
      **On the large private repo:** secretscan 139 s → **56 s**, leakscan
      231 s → **147 s**, conflictscan 77 s → **6 s**. leakscan's exit 1 there
      is the same before and after (findings, not a regression).
      **The prediction was half right.** conflictscan's cost was mostly this
      reader, about 10× faster now. leakscan and secretscan are still bound by
      regex time, so `130`'s levers stand.
