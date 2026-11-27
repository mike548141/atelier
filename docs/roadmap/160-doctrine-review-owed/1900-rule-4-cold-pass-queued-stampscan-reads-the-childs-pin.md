- [ ] ⏳ **Rule-4 cold pass queued: `stampscan` reads a child's stamp at the child's pin,
      and runs warn-only on the floor's CI plane (`020/110`).** The authoring session
      (9c5fa72c, `atelier-fa`, Opus 5.5, principal-opened by `/atelier:work run`, whose
      Opus worker wrote it) queues this and neither briefs nor takes it. `160/1240` covers
      some of the same paths but is already briefed, so this is its own pass.
      *Tier:* Fable, the principal-named review tier, checked at selection; it runs only on
      his approval (the general Fable hold), at the next drain by default (`460/060`).
      *Pass type:* code and doctrine, per `method/REVIEW.md` rule 4: a guard every child's
      floor runs.
      *Delta, scoped to paths:* `tools/stampscan.py`, `tools/test_stampscan.py`,
      `tools/floor.py`, `tools/test_floor.py`, `.github/workflows/ci.yml`,
      `skills/repo/create.md`, `docs/method/PROPAGATION.md`, `tools/README.md`,
      `CHANGELOG.md`: every commit on `main` after `868faf8a` up to and including the
      commit that lands this pointer.
      *Intent record:*
      [`../020-policy-as-code-programme-five-tracks-mik/110-d2-residue-stampscan-registry-wiring-stays-bar.md`](../020-policy-as-code-programme-five-tracks-mik/110-d2-residue-stampscan-registry-wiring-stays-bar.md).
