- [ ] ⏳ **Rule-4 cold pass queued: `ccopen`, the session-open twin of
      `ccclose` (`210/520`).** The authoring session (12a41aa2, Opus 5.5,
      principal-opened, 2026-11-22 UTC, which dispatched the Sonnet worker
      that wrote it) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* cold pass on a first-of-kind instrument, per
      `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccopen`,
      `instruments/ccopen.test.js`, `instruments/ccopen.design.md`,
      `instruments/man/ccopen.1`, `instruments/README.md`, and the exports
      added to `instruments/ccclose` and `instruments/cclive`: the two commits
      that build `210/520`, on `main`.
      *What to test hardest:* which residue is ❌ "recover first" and which
      only warns, since a false ❌ sends a session to recover work that is a
      live peer's; that the calling session is left out of the live read; the
      one write it makes (`git fetch`); what it prints as unknown.
      *Approval:* none yet; owed to the principal before the pass runs.
