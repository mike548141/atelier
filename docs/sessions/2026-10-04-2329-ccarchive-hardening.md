# 2026-10-04 · 2329 UTC — ccarchive hardening: the archive copy is the truth

**Tier:** Opus 5.5 orchestrating, stated at open per `ECONOMICS.md`
§ *The orchestrated-run tier split*. Workers: Sonnet 5.5 for parts A and C
and a read-only inventory, Opus 5.5 for part B (the trust model, the
security-critical design). One worktree, `atelier-ccarchive-1005`, because
every item lands in the same three files, so the parts ran serially.

**The brief.** The standard queue-run prompt, with this run's theme in Mike's
words: *"work related to ccarchive - I want to be able to rely on it to protect
my session transcript data as I expect it too"*.

## What the run found at open

- The last scheduled run (2026-10-03) had died on an iCloud-offloaded mirror,
  and 136 files were waiting to be archived. Mike had removed the launchd job
  on 2026-10-05 in a separate session.
- Two Fable cold passes on ccarchive (MC, 2026-10-03; HL, 2026-10-04) held
  5 MAJOR findings between them, unruled. The heart of them: an ordinary run
  could overwrite an intact archived copy with a shorter live file and report
  all-clear (HL1, HL2); a torn in-place write froze a damaged mirror (MC2,
  HL4); any run re-signed an index it never authenticated (HL3).

## Rulings, taken before the build

Mike: *"If there are rulings related to ccarchive lets do them now in case it
effects your work. After that I want you to build all of it"*. Every open
ccarchive decision was inventoried and walked in AskUserQuestion. Recorded
in full on [`210/210`](../roadmap/210-instruments-open-features/210-ccarchive-hardening-batch.md):
two rulings in his own words (index repair only on a proven part-way failure,
never adopting a planted file; a lock with stuck-lock detection and clearing),
his two-kind model of the data, verbatim, and four answers to options (stop on
an unverified signature; keep both versions of a living document on any
non-append change; encryption's crypto source C′ on `210/030`). One question
was sent back as *"a jumble of words and no clear ask. Do better"* and was
re-asked in plain words; the lock-free design offered first was declined in
favour of a lock.

## What was built (merge `8540a1d`)

- **Part A (`90683d3`).** Mirrors, manifest, signature and restored files
  are written by temp file, fsync, stamp and rename, so a kill never leaves a
  torn mirror and a symlink is replaced, not followed. `210/200` was
  diagnosed from the log: all 14 field crashes were the in-place
  `writeFileSync` over an offloaded mirror, so rename removes the cause. One
  unreadable source or undecompressable mirror is skipped and named, never
  fatal. Restore checks the hash before writing. Read-only modes move
  nothing. The schedule installer and all three schedule flags are gone
  (`210/190`). Exit 2 now means "could not finish", 1 "finished, needs a
  person".
- **Part B (`dcdf40b`).** The signature is checked before any write; anything
  but verified stops the run, cleared only by `--rekey`. A signed intent
  journal beside the key proves a part-way failure. Anything else the index
  does not vouch for is adopted only if identical to the live copy, otherwise
  moved to `_untrusted/`. A lock with `--lock-status` and `--clear-lock`.
  Unknown flags refused.
- **Part C (`cafa292`).** Two kinds of data: append-only records (transcripts,
  prompt history, tool results) where the only legal change is growth, checked
  by hashing the source's recorded-length prefix against the signed index
  without reading the mirror; and living documents (memory notes, subagent
  metadata), whose previous version is renamed to `_versions/` on any
  non-append change. A changed append-only record is never written over the
  mirror; it is kept aside in `_anomalies/` and the run exits 1. Session and
  per-kind counts (`210/160`). `--audit` checks the signature. Docs, tests,
  ENVIRONMENT section and CHANGELOG.

Tests: `ccarchive.test.js` 103 → 194; all instruments 377 pass; tools 1669
OK; `mandoc -T lint` clean.

**Measured, read-only, before part C** (on the real archive, against the
signed index): transcripts 3,634 unchanged and 7 grown by pure append, none
shrunk or rewritten; tool results and subagent metadata never changed; memory
notes 785 unchanged, 6 appended, 3 shrunk, 1 rewritten. That is the evidence
for the two-kind split and for treating prompt history as append-only.

**Dry run of the merged code against the real archive:** exit 0, a before
and after listing of the key directory and the archive root showed no writes,
99 files waiting, 4 memory versions to keep, no anomalies.

## Errors, recorded against this run

- 🛑 **A worker recreated the login job Mike had removed.** Part A's worker,
  checking its "removed flags are refused" test against the old script, ran
  `--install-schedule` on old code. The plist pointed at the PATH-installed
  instrument, which is a symlink to the main checkout, so `RunAtLoad` ran the
  real tool against the real archive once (it died on the offloaded-mirror bug
  this run fixes, having archived some new files as any hand run would).
  Mike saw Node reappear in Login Items. The plist was removed (not loaded by
  then; his own copy from that morning is still in the Bin). Lesson saved to
  machine-local memory, and parts B and C were dispatched with a hard rule:
  run only `node <worktree>/instruments/ccarchive`, never the bare name, never
  `launchctl`, `HOME` faked for any old-code check.
- ⚠️ **`210/160` was built without being claimed first.** It was folded into
  part C's dispatch as part of "build all of it" and only claimed at close. No
  parallel claim existed, so nothing collided, but the claim-before-work rule
  was broken.

## Left open

- The rule-4 code cold pass on this delta is queued, not taken: `⏳ 160/670`.
  The MC and HL cycles stay open until it runs.
- Known residue, from the workers, for that pass to weigh: a rewritten source
  carrying an older mtime is seen only by `--audit`; an anomaly that keeps
  growing keeps one aside copy per distinct state until `--force`; a lag from
  before the journal existed may be set aside once; `--rekey` mints the key
  before it re-signs; a narrow race remains when clearing a stuck lock.
- Encryption (`210/020`, `210/030`): crypto source answered, build not
  started, its build-time sub-decisions still open.
- `210/220` (version history like git, or diffs) is idea-only.
