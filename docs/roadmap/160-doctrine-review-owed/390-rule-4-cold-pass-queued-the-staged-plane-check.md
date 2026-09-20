- ⏳ **Rule-4 cold pass queued — the staged-plane board check and its doctrine
      sweep (`010/020`, BS1's fund).** Self-authored by the run: its dispatched
      worker built the code, the orchestrator wired the registry and swept the
      doctrine surfaces, so the whole delta is the run's authorship and it
      neither takes nor spawns the pass. *Tier:* Fable, the principal-named
      review tier — checked at selection; a session that cannot honour the bar
      stops rather than takes. *Pass type:* code **and** doctrine cold pass,
      per `method/REVIEW.md` rule 4. *Delta — scoped to paths:* `tools/board.py`
      (the `--staged` / `--from-index` planes and the two `_*_sections`
      readers), `tools/test_board.py` (the `StagedPlane` class),
      `tools/README.md` § *board*, `tools/floor.py` (the `board` Scanner's hook
      argv), `docs/method/CONCURRENCY.md` §§ *On a split board* and *Claiming
      at a dirty primary checkout*, `docs/roadmap/README.md` preamble, and the
      board-store ADR's 2026-09-20 amendment. Landed on `main`, 2026-09-20.
      **The lenses that matter most here:** whether reading the index on both
      sides is genuinely the hook's right question in every case, or whether
      some third state (a merge in progress, a partial `add -p`) makes it the
      wrong one; whether `board.py` importing `harvestscan` at module scope is
      the right way to share the plane vocabulary given `115/080`'s open
      question about a shared harness, and what it does to a child resolving
      tools through `$ATELIER_TOOLS`; whether the registry wiring is as safe as
      its comment claims, given that a previous registry wiring was refused as
      unsafe on 2026-09-19 for a reason that reads similarly; and whether the
      swept doctrine surfaces now agree with each other and with the code, the
      original BS1 defect having been four surfaces asserting a guarantee the
      tool did not provide.
      *Intent record:*
      [`../../sessions/2026-09-20-1053-queue-run-the-loose-ends.md`](../../sessions/2026-09-20-1053-queue-run-the-loose-ends.md).
