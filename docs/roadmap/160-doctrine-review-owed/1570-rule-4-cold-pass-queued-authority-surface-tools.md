- [ ] ⏳ **Rule-4 cold pass queued: tools around the authority surface —
      `flipcheck`, a read-only report of the pre-flip platform settings with a
      pointer to it from `AUTONOMY.md`'s gate (`260/130`).** The authoring
      session (queue run 78ca9153, Opus 5.5, principal-opened, 2026-11-16 UTC,
      which dispatched the worker that wrote it) queues this and does not take
      it.
      *Tier:* Fable, the principal-named review tier, checked at selection; the
      pass waits for his explicit permission for Fable work.
      *Pass type:* cold pass per `method/REVIEW.md` rule 4: `AUTONOMY.md` is
      the always-confirm floor's own document, and any edit to it earns one.
      *Delta, scoped to paths:* `tools/flipcheck.py`, `tools/test_flipcheck.py`,
      `tools/README.md`, `docs/method/AUTONOMY.md` (one sentence in the
      pre-flip gate): the commit that closes `260/130`, on `main`.
      *What to test hardest:* that every call is a GET (no `--method`, no
      field flags) and a refused read can never print as "set"; the
      private-repo "not available" paths are proved only by stubbed 403/404,
      the live read was of this public repo alone (2026-11-16T11:42Z).
