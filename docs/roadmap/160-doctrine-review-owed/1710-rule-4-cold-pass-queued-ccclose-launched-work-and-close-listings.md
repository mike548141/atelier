- [ ] ⏳ **Rule-4 cold pass queued: `ccclose` check 15, launched work finished
      (`210/460`), its four close listings (`210/480`), and the session-open
      hook `tools/idhook.py` (`210/490`).** The authoring session (12a41aa2,
      Opus 5.5, principal-opened, 2026-11-22 UTC, which wrote `idhook` and
      dispatched the Sonnet worker that wrote the `ccclose` changes) queues
      this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* cold pass on an instrument's new verdict policy and on an
      instruction channel, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccclose`,
      `instruments/ccclose.test.js`, `instruments/man/ccclose.1`,
      `instruments/ccclose.design.md`, `instruments/README.md`,
      `docs/method/RECORD.md`, `docs/method/CONCURRENCY.md`: the two commits
      that close `210/460` and build `210/480`, on `main`; and
      `tools/idhook.py`, `tools/test_idhook.py`, `tools/README.md`: the
      commits that close `210/490`.
      *What to test hardest:* the principal's ruling quoted on `210/460`, that
      anything the session launched is a blocker: which states fail and which
      only warn (an unreadable process table, a schedule); the harness and
      MCP-server exclusions, which must not hide a real detached run; argv
      never printed whole. For `210/480`: a principal prompt that the every-ask
      listing drops, and another repo's failure counted in the verdict. For
      `idhook`: it injects text into every session on the principal's machine
      at start, so what it may say and whether a hostile registry file could
      steer it.
      *Approval:* none yet; owed to the principal before the pass runs.
