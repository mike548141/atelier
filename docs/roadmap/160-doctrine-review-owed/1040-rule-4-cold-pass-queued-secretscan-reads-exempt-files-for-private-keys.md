- [ ] ⏳ **Rule-4 cold pass queued: `secretscan` still reads a file its
      `.secretscanignore` exempts, for real private-key material, as an
      advisory (`115/380`).** It changes what the publish-safety guard reads
      inside its own exemptions, in every child at `floor.yml@main`. The
      authoring session (a principal-opened Opus 5.5 queue run, session
      722ac2e2, 2026-11-06, which found the gap at its landing of `320/790`
      and dispatched the Sonnet worker that wrote the code) queues this and
      does not take it. The principal's approval of `160/1030` does not
      cover it: it waits for his word, and a session he approves may take
      both together (same file, same run's work).
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/secretscan.py`,
      `tools/test_secretscan.py`, `tools/README.md`, `CHANGELOG.md`,
      `.secretscanignore` (the commit that closes `115/380`, on `main`,
      2026-11-06).
      *Questions worth the pass's time:* the fragment-joining state machine
      in `exempt_key_hits` (what real shapes it misses, and whether any input
      makes it slow); whether the private-key outline test can match a
      non-key; the staged path reading added lines only.
      *Intent record:*
      [`../115-guardrail-architecture-mike-commissioned/380-the-scanners-exempt-test-files-hold-a-promise-nothing-checks.md`](../115-guardrail-architecture-mike-commissioned/380-the-scanners-exempt-test-files-hold-a-promise-nothing-checks.md).
