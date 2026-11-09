- [ ] ⏳ **Rule-4 cold pass queued: `quotescan`, a quote of the principal on commits touching his prompt, warn-first (`160/900` QK1, `320/810`), and `leakscan --messages` (`320/550`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/quotescan.py`, `tools/test_quotescan.py`, its registry entry in `tools/floor.py`, the `--messages` mode in `tools/leakscan.py` and its test — the commits that add them, on `main`.
      *Questions worth the pass's time:* whether any quotation marks at all satisfy it; whether `--messages` reports only its own findings and stays read-only.
      *Intent record:* `160/900`, `320/810`, `320/550`.
