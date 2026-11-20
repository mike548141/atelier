- [ ] ⏳ **Rule-4 cold pass queued: `leakscan`'s ipv4 rule skips a
      user-agent version (`115/460`), and the two adoption graces removed
      from `board` and `leakscan` (`010/190`).** A narrowed detection rule is
      a silent-failure surface: a real address the new shape skips reports
      nothing. Built by a worker of queue run 08cd3b95 (Opus 5.5,
      principal-opened, 2026-11-20 UTC), which queues this and does not take
      it or brief it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/leakscan.py`, `tools/test_leakscan.py`,
      `tools/board.py`, `tools/test_board.py`, `tools/test_floor.py`,
      `tools/test_report.py`, `tools/README.md`, `docs/method/SECRETS.md`,
      `CHANGELOG.md`, and the one-line comment edits in `tools/allowmarker.py`,
      `tools/attribscan.py`, `tools/blockscan.py`, `tools/pdlistscan.py`,
      `tools/pins.py`: the commits that close `010/190` and `115/460`, on
      `main`.
      *What to test hardest:* the ipv4 skip's boundaries (a capitalised
      word, a slash and a real address in prose is accepted as a version, and
      pinned by a test; is that the right cost?); that the grace removal left
      post-date behaviour exactly as it was the day after the date; and that
      no reader of the removed `--json` key `binary_grace` is left.
      *Intent records:*
      [`../010-board-store-migration-per-item-files-mik/190-remove-the-two-adoption-graces-after-their-date.md`](../010-board-store-migration-per-item-files-mik/190-remove-the-two-adoption-graces-after-their-date.md),
      [`../115-guardrail-architecture-mike-commissioned/460-ipv4-rule-reads-a-browser-version-as-an-address.md`](../115-guardrail-architecture-mike-commissioned/460-ipv4-rule-reads-a-browser-version-as-an-address.md).
      No brief yet: a brief-writer this run did not start writes it. **Drain
      priority: not set by the principal; this run suggests low.**
