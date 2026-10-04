- [ ] **A run aborts on one evicted iCloud mirror instead of skipping it**
      (handed up by a private child, 2026-10-05, over the channel; Mike:
      *"yes hand them over"*)

      `~/Library/Logs/ccarchive.log` shows repeated failures of the shape
      `Error: Unknown system error -11: Unknown system error -11, open
      '<path under the iCloud Drive mirror store>'`, each time on a file
      already in the archive on iCloud Drive.

      **Unverified diagnosis, to re-measure before fixing:** errno 11 on
      macOS is `EDEADLK`, which is what opening an evicted (dataless) iCloud
      placeholder returns when macOS cannot download it on demand. If so,
      iCloud has moved archived copies off the Mac to save local space, and
      the run dies the moment it opens one.

      **The fix, once confirmed:** one such file must not abort the whole
      run. Report it as skipped or unchecked and carry on, and choose a safe
      way to handle an evicted file (request the download and wait, treat it
      as unverifiable this run, or both with a flag).

      *Distinct from `210/170`* ("the manifest lags the mirror"): per a
      shed-side read-only finding, `170`'s manifest-lag defect treats an
      evicted file only as unchecked — it does not cover a run that aborts on
      one. This is its own item.

      *Stakes, as handed up:* low. Claude Code keeps transcripts for 395
      days, and the Mac is Time-Machine-backed to the NAS — ccarchive's local
      archive is a third copy of material that already has two others.
