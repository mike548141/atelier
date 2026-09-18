- [x] **Sweep monolith-era board wording across the doctrine surface.** The
      load-bearing docs moved with the mechanism (RECORD, CONCURRENCY,
      CLAUDE, the board README); a residue of incidental references to
      editing `ROADMAP.md` directly or harvesting to `ROADMAP-DONE.md` may
      survive elsewhere (REVIEW.md's generic "ROADMAP ⏳" wording was checked
      and still reads true). One grep-led pass, fixing only what now
      mis-describes the mechanism — history and archive mentions stay
      verbatim.

      ✅ **Swept 2026-09-18, nothing to fix.** `git grep -i` for
      `ROADMAP-DONE` and `harvest` across `docs/method`, `docs/build`,
      `tools/README.md` and instrument docs: every hit is either history, the
      scanners' own subject, or monolith-board wording that is still
      **current for the children** — the split board is atelier's alone until
      `010/030`'s fleet rollout, so `REPO-STANDARD.md`'s spill rule and the
      template's ROADMAP header describe what a child actually runs.
      `RECORD.md` already states both modes. The one line worth a second look
      when `010/030` lands: `CONCURRENCY.md` § *Orchestrated queue runs*'s
      "the roadmap harvest" in the close litany, which becomes a no-op on a
      split board rather than a wrong instruction.
