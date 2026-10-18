- [ ] ⏳ **Rule-4 cold pass queued: the staged-positional reader the three
      staged-diff guards share (`115/360`).** Guard code, doctrine by
      function: a clean `--staged` scan is read as "nothing barred was
      staged". So the authoring session (a Mike-opened Opus 5.5 queue run,
      session 8e498ef1, 2026-10-18, wt atelier-qr-115-360, which dispatched
      the Sonnet worker that wrote the code) queues this and does not take
      it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/report.py` (`scope_staged`),
      `tools/leakscan.py`, `tools/secretscan.py`, `tools/conflictscan.py`
      and their four `tools/test_*.py` files, commit `692c04a` on `main`,
      2026-10-18. One question the author could not settle alone: whether
      any child's declared scope relied on the old exact-spelling match.
      *Intent record:*
      [`../115-guardrail-architecture-mike-commissioned/360-a-bare-dot-scope-makes-the-staged-plane-scan-nothing.md`](../115-guardrail-architecture-mike-commissioned/360-a-bare-dot-scope-makes-the-staged-plane-scan-nothing.md).
      No brief written.
