- [ ] **E7 residue — G3 (binary media): FUNDED as its own item, soon
      (Mike ruled 2026-08-09; shape unchanged from 2026-08-04).** A
      deliberate landing, not a rider: the build session designs the
      blast-radius half deliberately — marker ergonomics for legitimate
      images and the adoption/re-baseline story — because every binary in
      every adopting tree starts blocking the moment the registry carries
      it. Original residue note kept below.
      Mike ruled G3 BLOCKING (2026-08-04): an unscannable or
      metadata-bearing binary blocks, a legitimate image carries a
      one-time reasoned marker, keeping E6a's no-advisory-form decision
      intact. The 2026-08-06 build deliberately did not take it — the
      ruling's funded list named G1/G2/G4/G6/G7, and G3 changes behaviour
      for every binary in every adopting tree, a blast radius that
      deserves its own landing. Whether it rides the next leakscan touch
      or gets its own item is Mike's call, put at this session's close.
      (The build did add path-name scanning, so a binary's NAME is now
      read even while its body is not.)
      ---
      ⚖️ **BUILT 2026-10-03 and HELD FOR MIKE as draft PR #97 (branch
      `qr-leakscan-g3`). It is not merged.** The shape is the ruling's. A
      tracked binary blocks until `.leakscanbinaries` holds an entry for its
      exact bytes: a SHA-256 prefix, the path and a reason, so a changed file
      blocks again. That hash binding is what makes "one-time" true.
      PNG/JPEG/WebP text metadata is scanned. Opaque metadata (Exif, IPTC)
      blocks unless the entry names that scope. E6a stands. The full suite
      passes (1,646), and atelier has 0 tracked binaries.
      🛑 **Why it is held: children float at `floor.yml@main`, so merging
      reds CI in 7 children at their next run, with 152 binaries to list**
      (2 of 4 public children, 57 files; 5 private, 95). There is no
      deferment path, because E6a forbids an advisory form and floor.py
      refuses a dated block. Turning seven repos' CI red is the principal's
      act, not a queue run's.
      🎯 **Two decisions, in the PR:** land as built, or first rule on an
      adoption-time deferment for a gate with no advisory form; and whether
      the opaque-metadata scope hatch should exist at all.
      🔎 **Found by the build, fixed in the held branch:** the staged plane
      never saw a binary at all, not even a leak in its *name*, and it also
      missed empty new files and pure renames. That falsifies G2's hot-path
      coverage claim. `floor.py`'s flag blocklist would also have missed the
      new listing mode, the "a blocklist underblocks" class again. The
      doctrine gap it exposed is filed as `410`.
