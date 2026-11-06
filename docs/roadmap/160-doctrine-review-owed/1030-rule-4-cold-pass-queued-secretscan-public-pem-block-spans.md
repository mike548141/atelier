- [~] ⏳ **Rule-4 cold pass queued: `secretscan` exempts a public
      certificate's or public key's PEM body from the entropy rule
      (`320/790`).** `secretscan` is the publish-safety guard every child
      floats on at `floor.yml@main`, and this change opens a blind spot on
      purpose, so it must be shown never to cover a private key. The
      authoring session (a principal-opened Opus 5.5 queue run, session
      722ac2e2, 2026-11-06, which dispatched the Sonnet worker that wrote the
      code and twice sent it back: once to require a nested SEQUENCE so a
      private key's DER under a forged public header is not exempt, once to
      replace real throwaway private keys in the fixtures with synthetic DER)
      queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/secretscan.py`,
      `tools/test_secretscan.py`, `tools/README.md`, `CHANGELOG.md` (the two
      commits that close `320/790`, on `main`, 2026-11-06).
      *Questions worth the pass's time:* can any input other than a public
      certificate or public key reach the exemption (the label match, the
      consecutive-line and base64 rules, the 2048-line bound, the nested
      SEQUENCE check); does the `--staged` path read the index copy only when
      it should, and fail closed when git cannot give it; is whole-block
      voiding right, or too strict for a real-world certificate file.
      *Intent record:*
      [`../320-child-filed-findings-via-pointing-up/790-hand-up-secretscan-flags-every-body-line-of-a-public-certificate.md`](../320-child-filed-findings-via-pointing-up/790-hand-up-secretscan-flags-every-body-line-of-a-public-certificate.md).
      ✅ **Approved by the principal, 2026-11-06, through the device at the
      authoring run's close, verbatim:** *"If you can run it using the API
      credit and achieve parity of quality in the review as doing it locally
      then use the API. If you cant achieve parity then run it on fable
      locally now"*. The authoring session cannot start, instruct or brief
      it (rule 4), so on his pick a fresh session he opens takes it: an Opus
      brief first, then the pass on the API credit where it reaches parity,
      else Fable locally. Barred sessions: 722ac2e2 and anything it started.
      ⏳ **BRIEF WRITTEN 2026-11-06** by session `782f8a66` (Opus 5.5, off-tier,
      forms no finding; started by drain session `850e2a78`, which authored
      neither delta): `docs/reviews/2026-11-06-2027-secretscan-public-pem-spans-cold.md`,
      with its `.deferred.md` sibling (11 seeded questions, one results set, two
      held facts); review NOT run. Fable 5.1 on the laptop, checked at
      selection; `850e2a78` orchestrates, holds the sibling and forms no
      finding. Barred from reviewing: `722ac2e2` and its workers, `782f8a66`,
      `850e2a78`.
      `[~]` **CLAIMED 2026-11-06-2041** (wt: atelier-160-1030-2041; cold pass: a
      Fable 5.1 reviewer, tier checked at selection, run locally through
      Claude Code, not the API harness, which stays stopped until its own
      review's findings are ruled; orchestrator: drain session `850e2a78`,
      Opus 5.5, a rule-4 off-tier orchestrator that holds the context
      partition, forms no finding and writes no severity; it authored
      neither delta nor the brief, and was not started or instructed by
      `722ac2e2`). Runs under the principal's 2026-11-06 approval quoted
      above.
