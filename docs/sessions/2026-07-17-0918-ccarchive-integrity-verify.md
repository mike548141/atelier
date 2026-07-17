# 2026-07-17 · 0918 UTC · ccarchive — integrity manifest + --verify

## What prompted it

Mike: "Is there a verify mechanism? How do we know the files we restore from
iCloud haven't been mutated? Perhaps sha256." Right question for a long-term
reference archive.

## The gap

gzip's built-in **CRC-32** catches a corrupted `.gz` on decompression (that's
what the earlier `gunzip -t` relied on), but it's weak and only proves the file
is *self-consistent* — nothing bound the archived content to what was captured,
no whole-archive audit, no recompute-and-compare.

## The change (`instruments/ccarchive`)

- **sha256 manifest.** On archive, record `{sha256, rawBytes, archivedAt}` for
  each transcript's **raw bytes** in `<dest>/manifest.json` (keyed by the same
  source-relative path the mirror uses). Written atomically (temp + rename),
  keys sorted for stable diffs.
- **`--verify`.** Re-hashes every archived `.gz` (gunzip → sha256) against the
  manifest; reports **mismatch** / **missing** / **unmanifested**, exits
  non-zero if the archive doesn't verify. `--json` for machines.
- **Manifest tracks the archive, not live sources.** A source pruned by Claude
  Code's cleanup keeps its entry (its `.gz` is kept — append-only). First run
  after shipping **backfills** hashes for the already-archived files (from the
  present source, or by decompressing the `.gz` when the source is already gone).
- **Honest limit, documented:** the manifest is the trust anchor — it defends
  against accidental corruption/bit-rot/sync-glitch; a tamperer who also rewrote
  the manifest would pass. Mitigation noted (keep a copy of `manifest.json`
  separate from the archive). A cross-checked off-archive anchor is a possible
  future step, not built here.

## Verified

- **25 tests** green (was 18; +7): known-answer sha256; manifest records the raw
  hash; `--verify` passes intact (exit 0), detects a mutated `.gz` (exit 1, names
  it), detects a deleted `.gz` as missing (exit 1); pruned-source entry survives
  and still verifies; `saveManifest` atomic + deterministic order.
- **Driven live:** ran the archive → built a 428-entry `manifest.json` (one-time
  backfill, ~1.5 s) → `--verify` → **428 verified, 0 mismatched, 0 missing**.
  Tamper/missing detection exercised by the contract tests over a temp tree (the
  real archive was not touched).

## Owed

Nothing new. The earlier ⏳ ADR-0006-addendum cold review still stands. This is
routine instrument code — tested and driven, self-verifying.

## Noted for a later call (not this change)

- **man pages.** Mike asked whether the cc tools ship man pages — they don't
  (self-documented via `-h`/`--help` + `instruments/README.md`). Whether to add
  `man` pages for the instruments is a documentation-convention decision (a new
  maintenance surface, sets precedent for the layer) — Mike's call, queued as a
  question, not actioned.
- **Scheduled verify.** `--verify` is on-demand; a periodic (e.g. weekly) verify
  via a second launchd entry could catch silent bit-rot early. Deferred.
