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
      that close `210/460` and build `210/480`, and the later one that closes
      `210/510`, and the one that closes `210/540` and `210/550` (check 15
      accepts later evidence that a detached launch ended), on `main`; and
      `tools/idhook.py`, `tools/test_idhook.py`, `tools/README.md`: the
      commits that close `210/490`.
      Widened 2026-11-27 by folding `160/1560` here (board `460/040`, one open pass per
      subject; his pick *"Drop 8, merge 6 (Recommended)"*): `instruments/ccclose`,
      `instruments/ccclose.test.js`, `instruments/man/ccclose.1`,
      `instruments/ccclose.design.md`, `instruments/README.md`: the commit that lands the
      `ccclose` half of `020/470` (`74a0ceaf`); and `tools/floorhook.py`,
      `tools/test_floorhook.py`, `tools/README.md`: the later commit that closes `020/470`.
      Intent record for that part:
      [`../020-policy-as-code-programme-five-tracks-mik/470-a-hook-that-fails-noisy-when-a-child-floor-copy-is-stale.md`](../020-policy-as-code-programme-five-tracks-mik/470-a-hook-that-fails-noisy-when-a-child-floor-copy-is-stale.md).
      The folded item's own notes stay in `160/1560`.
      *What to test hardest:* the principal's ruling quoted on `210/460`, that
      anything the session launched is a blocker: which states fail and which
      only warn (an unreadable process table, a schedule); the harness and
      MCP-server exclusions, which must not hide a real detached run; argv
      never printed whole. For `210/480`: a principal prompt that the every-ask
      listing drops, and another repo's failure counted in the verdict. For
      `idhook`: it injects text into every session on the principal's machine
      at start, so what it may say and whether a hostile registry file could
      steer it.
      For `210/540`/`550`: whether any of the three after-the-fact forms can
      clear a launch that is still running (a pid reused, a pattern that
      misses the live process, a stale result file from an earlier run).
      *Approval:* none yet; owed to the principal before the pass runs.
