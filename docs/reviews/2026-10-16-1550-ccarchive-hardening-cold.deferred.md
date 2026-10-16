# Deferred sibling — ccarchive hardening

**Held under rule 1's split** (`docs/method/REVIEW.md`). Open only after your
phase-1 findings are committed to the brief
`docs/reviews/2026-10-16-1550-ccarchive-hardening-cold.md`. At verdict, fold this
file in below your reconcile and delete it.

Written 2026-10-16 UTC by the Opus brief-writer named in the brief, which authored
none of the delta and forms no finding: the questions below are seeds, a floor
and never a fence.

## Intent record

- `docs/sessions/2026-10-04-2329-ccarchive-hardening.md` — **not opened by the
  brief-writer**. The records commit `21a772f` appended to it after the run's
  close; the widening commits `bab1451` and `72e0093` may be recorded there or in
  `docs/sessions/2026-10-05-1120-queue-run-closes-and-builds.md` (also not
  opened).

## The earlier verdicts this delta answers (named, not opened)

The commit messages cite finding IDs as answered. ID greps over `docs/reviews/`
place them in these two files; neither was opened by the brief-writer:

- `docs/reviews/2026-10-04-2215-ccarchive-heal-pulled-cold.md` — the `HL` IDs
- `docs/reviews/2026-10-03-0357-manifest-checkpoints-cold.md` — the `MC` IDs

For each cited ID, check at reconcile that the code at HEAD answers what the
finding said, not what the commit message says it said; and list any finding in
those two verdicts the series does not cite.

## Other prior verdicts naming the tool (named, not opened)

- `docs/reviews/2026-07-17-1000-adr0006-ccarchive-preserve-cold.md`
- `docs/reviews/2026-07-17-1000-cli-docs-standard-cold.md` and
  `docs/reviews/2026-07-17-1157-cli-docs-applied-cold.md`
- `docs/reviews/2026-07-17-1000-conventions-utc-at-rest-cold.md` and
  `docs/reviews/2026-07-17-1157-conventions-utc-applied-cold.md`
- `docs/reviews/2026-07-20-2040-size-rebalance-cold.md`
- `docs/reviews/2026-08-15-1032-cctranscript-search-cold.md`
- `docs/reviews/2026-08-17-1321-plain-reply-repurpose-design.md`
- `docs/reviews/2026-09-25-0715-ccmail-build-cold.md`
- `docs/reviews/2026-10-03-0357-archive-pool-speedup-cold.md`

## The pointer's own lens hints

None. The pointer is refs-only (delta, intent record, tier, pass type).

## Seeded questions

1. **One destination, two machines.** The lock and the intent journal both live
   under the running machine's home, not on the destination. If the destination
   syncs between machines, does the lock exclude the other machine at all, and
   what does machine B do with a mirror machine A wrote but has not yet indexed
   (no entry → set aside as untrusted)?
2. **Rollback.** The signature is an HMAC over the manifest bytes. Does anything
   bind freshness, so that an older, validly signed manifest-and-signature pair
   (from a sync conflict, a backup restore, or an attacker with destination
   write) is refused rather than read as `verified`?
3. **Legacy trust.** Entries written before the hardening carry no mirror stat
   and are "trusted as signed until their next write". Every archive that
   predates the change starts in that state; is the stat-vouching weakest
   exactly where the most data sits, and does the legacy budget close it?
4. **Platform.** `stat -f` and `ps -o lstart=` are BSD and macOS forms; GNU
   `stat -f` reports file-system status instead. The schedule now supports
   Linux. Does the legacy batched stat, or the lock's process identity, behave
   on Linux, and does the Ubuntu CI run reach those paths or skip them? The
   `stat` argv also passes paths with no `--` separator.
5. **Seams in the shipped tool.** `CCARCHIVE_SCHEDULER_LOG` turns every scheduler
   call into a log line, and `CCARCHIVE_SCHEDULER_EXIT` fakes its result. Can a
   variable left set in a user's shell make `--install-schedule` report success
   while installing nothing, or make a real run inject a fault?
6. **Uninstall reach.** `--uninstall-schedule` also removes "an old login-style
   plist". By what test does it decide a file is its own, and can it remove a
   file another program owns?
7. **Retention.** `_anomalies/` and `_versions/` are never deleted, hold private
   transcripts and memory notes, and the destination may be a cloud-synced
   folder with encryption at rest unbuilt. Is unbounded retention of extra copies
   a privacy design choice the man page states, or an unexamined default?
8. **Story drift.** Part A removed the installer and refused its flags by name;
   `72e0093` brought it back two hours later. Do the man page, `--help`, the
   README and both CHANGELOG entries now tell one consistent story?
