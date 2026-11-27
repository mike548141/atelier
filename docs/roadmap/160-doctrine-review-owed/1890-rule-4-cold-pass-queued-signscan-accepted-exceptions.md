- [ ] ⏳ **Rule-4 cold pass queued: `signscan` accepts named commits by full id, and
      `SIGNING.md` says how a hosted session hands its work back (`115/520`).** The
      authoring session (9c5fa72c, `atelier-fa`, Opus 5.5, principal-opened by
      `/atelier:work run`, whose Opus worker wrote it) queues this and neither briefs nor
      takes it.
      *Tier:* Fable, the principal-named review tier, checked at selection; it runs only on
      his approval (the general Fable hold), at the next drain by default (`460/060`).
      *Pass type:* code, per `method/REVIEW.md` rule 4: an exception list a security guard
      reads.
      *Delta, scoped to paths:* `tools/signscan.py`, `tools/test_signscan.py`,
      `.signscanaccept`, `.github/workflows/ci.yml`, `docs/method/SIGNING.md`: every commit
      on `main` after `3d3ded90` up to and including the commit that lands this pointer.
      *Intent record:*
      [`../115-guardrail-architecture-mike-commissioned/520-hosted-session-commits-fail-signscan.md`](../115-guardrail-architecture-mike-commissioned/520-hosted-session-commits-fail-signscan.md).
