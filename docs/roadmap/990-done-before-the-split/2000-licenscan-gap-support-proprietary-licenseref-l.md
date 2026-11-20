- [x] **licenscan gap — support proprietary / `LicenseRef-*` licences.**
      (claimed 2026-08-05-1243, wt: queue-batch-0806)
      A proprietary repo going public is *precisely* when copyleft-contamination
      detection matters most, and today the tool is **silent exactly there**.

      **Reproduction (2026-07-25, run before disabling the gate on 3 repos).**
      A fixture with a proprietary `LICENSE` ("ALL RIGHTS RESERVED") plus a
      source file carrying an SPDX header declaring GPL-2.0 (written literally in
      the fixture, described here — a real tag in this file trips licenscan, as
      it did on the first draft of this entry):

      - `licenscan --expect LicenseRef-Proprietary .` reports **one** finding —
        `LICENSE:1 [unknown-license]` — and **never mentions the GPL file**. It
        stops at "repo licence unrecognised" and verifies nothing further.
      - Appending `licenscan:allow:` to the LICENSE line does **not** restore
        the file-header checks: the finding persists and the GPL file stays
        invisible. So there is no in-repo workaround; the fix must be in the tool.

      **Why this is a real hole, not a cosmetic one.** A vendored strong-copyleft
      file cannot be relicensed on the way out. In an Apache repo licenscan
      catches that; in a proprietary repo — the one most likely to be scrubbed
      and published deliberately — it catches nothing, while *appearing* to be a
      configured gate. A check that is off is a decision; a check that runs and
      covers nothing is the failure class this repo keeps closing.

      **Fix shape.** Accept an unrecognised or `LicenseRef-*` repo licence as a
      *declared* licence: skip the "which known SPDX licence is this" comparison
      (which genuinely cannot be answered), and still run the per-file header
      incompatibility checks, which do not depend on recognising the repo
      licence — only on knowing it is not the copyleft one found. **Test to
      write with it:** the fixture above must report the GPL file.

      **Unblocks the 3 repos currently `disabled` with a stated reason**, and
      those declarations should be retired in the same change rather than left
      standing (see the advisory/disabled ageing item).
