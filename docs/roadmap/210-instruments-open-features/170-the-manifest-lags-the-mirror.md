- [ ] 🔎 **`ccarchive`'s manifest lags its own mirror in 14 files, so the
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

  ✅ **FIXED 2026-10-03 for the diagnosed cause (queue run, merge
  `0264387`). Locking is still open, so the item stays `[ ]`.**
  - **Progress is durable.** The manifest is checkpointed every 50 archived
    mirrors, and the run also persists it if the loop throws, then rethrows
    the original error. Each checkpoint **re-signs**, so the signature always
    attests the saved bytes, which the man page already promised. An entry
    is still set only after its mirror is written and stamped, so the
    manifest never claims a mirror that is not there. A hard kill can now
    leave at most 50 mirrors ahead.
  - **Stale entries heal.** On the skip path, an entry whose `rawBytes`
    disagrees with the source's size is refreshed from the source. This is
    sound because a mirror is only ever stamped with the mtime of the source
    version it was written from. It is size-triggered only, never runs on
    `--dry-run`, and does not catch a same-size rewrite, which `--verify`
    still does. The 14 lagging entries measured here heal on the next
    ordinary run where the mirror equals the source. The 3 whose source has
    grown take the normal re-archive.
  - 104 tests pass, 5 of them new: a run dying after K mirrors, a stale
    entry healed then verified, dry-run healing nothing, and the size-only
    trigger. A test-only seam, `CCARCHIVE_TEST_FAIL_AFTER`, follows the
    existing `CCARCHIVE_SIMULATE_DATALESS` pattern. The real archive was
    never written to.
  **Still open:** no lock against overlapping runs, so the lost-update
  hypothesis stands untested. Whether a run actually died in the field is
  also unknown. Rule-4 code pass queued at `160/460`.
