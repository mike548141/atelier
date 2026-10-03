- [~] (claimed 2026-10-03-0203, wt: qr-ccarchive-manifest) 🔎 **`ccarchive`'s manifest lags its own mirror in 14 files, so the
  shrink guard compares against a stale, smaller figure** (found 2026-10-03
  by the read-only investigation that answered `150`; cause NOT diagnosed)

  **Measured.** `ccarchive --verify --json` reports **14 mismatches**: 8
  transcript `.jsonl` and 6 memory `.md` files. In every one the mirror is
  **longer** than the manifest records, and the recorded bytes are a
  **prefix** of the mirror. So the mirror was written and the manifest entry
  was not updated to match. In 11 of the 14 the mirror already equals the
  current source. In the other 3 the source has grown since. The lag ranges
  from 11 B to about 4.9 MB. The same run: 8,643 manifested, 3,549 verified,
  0 missing, 274 unmanifested, and 5,080 evicted, which are not local and so
  not checked. The signature verified.

  **Why it matters.** The shrink guard compares a source against the
  manifest's `rawBytes`. Where the manifest lags, that comparand is too low,
  so a real truncation down to anywhere above the stale figure would **pass
  silently**. The guard errs permissive, which is the direction that loses
  data. This is the comparand drift `150` suspected. It did not explain the
  two refusals, but it is real elsewhere.

  **Not diagnosed. Two hypotheses, neither tested:**
  - A lost update between overlapping runs (a scheduled run and a hand run),
    where one run's stale in-memory manifest overwrites a newer one. This
    fits a `manifest.json.corrupt` dated 2026-09-16 beside the live manifest,
    and 6,306 entries sharing one `archivedAt` from the 2026-09-29 rebuild.
  - A manifest sync conflict on the storage layer.

  **The first step owed** is to check whether `ccarchive` takes any lock
  around read-modify-write of the manifest, and whether a scheduled and a
  hand run have overlapped. That is read-only. A fix waits on knowing which
  cause it is.

  🔎 **The mechanism, read in the code (2026-10-03, before claiming).**
  `archive()` writes each mirror **inside** its loop, but saves the manifest
  **once, after** the loop (`saveManifest` at the end of the run). So a run
  that dies part-way, whether killed, put to sleep or stopped by a throw on
  a later file, leaves every mirror it already wrote **ahead of** the
  manifest. The next run then **cannot heal it**. The mirror carries the
  source's mtime, so `shouldArchive` skips the file. The old entry still
  exists, so the backfill skips it too. The manifest stays stale for good.
  That matches the measurement exactly: in 11 of 14 the mirror equals the
  current source. There is also no lock, so the overlapping-runs hypothesis
  stays open as well. Whether any run actually died is **not established**.
  The code shows the mechanism, not that it fired.
