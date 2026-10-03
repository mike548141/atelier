- [~] (claimed 2026-10-03-0630, wt: qr-linear-reader) 🔥 **leakscan, secretscan and conflictscan's line reader re-slices
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
