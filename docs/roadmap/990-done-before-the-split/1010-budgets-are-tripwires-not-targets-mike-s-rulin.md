- [x] **Budgets are tripwires, not targets — Mike's ruling 2026-07-19, APPLIED
      2026-07-19; SUPERSEDED 2026-07-20 by the cold-content rebalance.** As
      applied: `--check` gated only the lossless-remedy files (`ROADMAP.md`,
      `SESSIONS.md` — a red demands a *move*, never rewording); judgement docs
      (`README`/`ARCHITECTURE`/`CLAUDE`) reported but never failed the build; the
      one-sided signal (no thinness floor) stated as deliberate in the module doc.
      **Superseded** 2026-07-20 (Mike's 2026-07-20 rebalance): the gate no longer
      keys on file class *or* line count at all, but on relocatable **cold
      content** — a `[x]` item on the hot path. The tripwire-not-target insight
      survives (its "always has a lossless fix" logic is exactly why the
      cold-content gate is fair); only its line-count *mechanism* was replaced.
      See the review-owed rebalance entry in `ROADMAP.md`.
