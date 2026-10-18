- [x] **DONE 2026-10-18** (wt: atelier-qr-020-150)
      **E7 residue — G3 (binary media): FUNDED as its own item, soon
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
      🎯 **Mike answered both decisions, 2026-10-18** (through the decision
      device, choosing the queue run's recommended options). First, land
      G3 with a grace period: *"Grace period (Recommended)"*. The option
      read: unlisted files print a warning naming a cut-off date (~30
      days), then start blocking. Second, keep the reasoned acceptance of
      opaque metadata as built: *"Allow with reason (Recommended)"*. 🚩
      The grace is a dated, self-expiring warning inside leakscan's binary
      rules only. That stands against E6a's no-advisory-form decision, and
      Mike's answer is the authority for this one exception. Recorded so
      the next reader does not read it as E6a quietly loosened.
      Mike, 2026-10-18, narrowing the second answer: *"PS that reason for
      the image metadata must be specific to the sets of metadata it wants
      to keep. It should only keep the metadata it has a need for"*. So the
      single opaque-metadata scope is not enough as built. An entry names
      each metadata set it keeps (for example a colour profile) with its
      own need, and any set it does not name still blocks.
      ✅ **LANDED 2026-10-18 as PR #97, squash `b5a2c53`, on Mike's two
      answers.** Rebased onto `main` after 15 days, with the board-claim
      commit dropped. The staged plane now goes through
      `report.scope_staged`. **Grace:** `BINARY_GRACE_UNTIL = 2026-11-18`
      (UTC). Before it the four G3 rules warn, naming the date and the
      remedy; from it they block. No flag, env var or config key moves it.
      The span was the queue run's choice on "~30 days", not a ruling.
      **Metadata by set:** `exif`, `iptc`, `xmp`, `icc`, `png-text`,
      `jpeg-comment` and `unknown`. Each kept set needs its own line with
      its own reason, and a copied reason is refused. An unnamed set
      blocks, and a named set the file lacks is stale. A judgement call:
      text metadata now needs a line too, read as following "only keep the
      metadata it has a need for". **Floor hardening found on the way:**
      `flags` refuses abbreviations of forbidden mode flags (`--binary`,
      `--self` had expanded to modes that scan nothing), and `scope`
      refuses dash-led paths. This covers every scanner run through the
      floor. 2,031 Python and 489 node tests green, PR checks green. Cold
      pass queued at `160/980`; the removal of both graces is `010/190`.
