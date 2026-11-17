- [ ] ⏳ **Rule-4 cold pass queued: tools around the authority surface —
      `flipcheck`, a read-only report of the pre-flip platform settings with a
      pointer to it from `AUTONOMY.md`'s gate (`260/130`), and `quotescan`'s
      warn-only line when a commit edits the agent's grant (`115/110`).** The authoring
      session (queue run 78ca9153, Opus 5.5, principal-opened, 2026-11-16 UTC,
      which dispatched the worker that wrote it) queues this and does not take
      it.
      *Tier:* Fable, the principal-named review tier, checked at selection; the
      pass waits for his explicit permission for Fable work.
      *Pass type:* cold pass per `method/REVIEW.md` rule 4: `AUTONOMY.md` is
      the always-confirm floor's own document, and any edit to it earns one.
      *Delta, scoped to paths:* `tools/flipcheck.py`, `tools/test_flipcheck.py`,
      `tools/README.md`, `docs/method/AUTONOMY.md` (one sentence in the
      pre-flip gate): the commit that closes `260/130`, on `main`; and
      `tools/quotescan.py`, `tools/test_quotescan.py`, `tools/commitmsg.py`,
      `tools/floor.py` (quotescan's declarations), `tools/README.md`,
      `CHANGELOG.md`: the later commit that lands `115/110`'s authority
      advisory.
      *What to test hardest:* that every call is a GET (no `--method`, no
      field flags) and a refused read can never print as "set"; the
      private-repo "not available" paths are proved only by stubbed 403/404,
      the live read was of this public repo alone (2026-11-16T11:42Z). For
      the advisory: that an authority finding can never block, whatever the
      prompt plane's blocking date; the surfaces it cannot see (an unstamped
      floor copy, a child's autonomy block outside the stamp, other settings
      keys, an untracked `settings.local.json`); measured over atelier's
      history, 26 of 2,465 commits would have drawn the line.
      *Approval:* the principal, 2026-11-17 UTC, through the device at the
      authoring run's close, his pick verbatim: *"API credit if parity"*
      (option text: *"Run them on the API credit lane where a pass can match
      laptop quality; any that can't wait for the drain."*). So: on the API
      credit only, where the pass reaches laptop parity; a pass that cannot
      waits for his next weekly drain. The authoring run (78ca9153) neither
      briefs nor starts it.
