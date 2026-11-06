- [~] ⏳ **Rule-4 cold pass queued: `secretscan` still reads a file its
      `.secretscanignore` exempts, for real private-key material, as an
      advisory (`115/380`).** It changes what the publish-safety guard reads
      inside its own exemptions, in every child at `floor.yml@main`. The
      authoring session (a principal-opened Opus 5.5 queue run, session
      722ac2e2, 2026-11-06, which found the gap at its landing of `320/790`
      and dispatched the Sonnet worker that wrote the code) queues this and
      does not take it. **Approved by the principal, 2026-11-06,** through
      the device at the authoring run's close: asked whether the fresh
      session he opens for `160/1030` should review this too, he picked
      **"Yes, both in that session"** (the recommended option). That
      session takes both, on the same terms as `160/1030`: API credit where
      it reaches parity, else Fable locally. Barred sessions: 722ac2e2 and
      anything it started.
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
      ⏳ **BRIEF WRITTEN 2026-11-06** by session `782f8a66` (Opus 5.5, off-tier,
      forms no finding; started by drain session `850e2a78`, which authored
      neither delta): `docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.md`,
      with its `.deferred.md` sibling (11 seeded questions, one results set, two
      held facts); review NOT run. Fable 5.1 on the laptop, checked at
      selection; `850e2a78` orchestrates, holds the sibling and forms no
      finding. Barred from reviewing: `722ac2e2` and its workers, `782f8a66`,
      `850e2a78`.
      `[~]` **CLAIMED 2026-11-06-2115** (wt: atelier-160-1040-2115; cold pass: a
      fresh Fable 5.1 reviewer, not the one that ran `160/1030`, tier
      checked at selection, run locally through Claude Code, not the API
      harness, which stays stopped until its own review's findings are
      ruled; orchestrator: drain session `850e2a78`, Opus 5.5, a rule-4
      off-tier orchestrator that holds the context partition, forms no
      finding and writes no severity; it authored neither delta nor the
      brief, and was not started or instructed by `722ac2e2`). Runs under
      the principal's 2026-11-06 approval quoted above.
