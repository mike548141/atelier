- [ ] 🔎 **Design exercise: refine how we manage work using the board, from the
      lived experience of past sessions.** Commissioned by Mike, 2026-11-09; his
      words are on `310/060`. Scope: the states an item can be in, including a
      two-tier model (a class such as "no more work to be done on this item and
      any children", with sub-classes such as done, not required, superseded,
      duplicate; and a mixed or in-progress state for a parent whose children
      differ). He has mocked up additional statuses in prior sessions, here or
      in other repos: find those first. Output is a design for him to decide,
      grounded in what sessions actually hit.
  - [ ] 📝 **DRAFTED 2026-11-09** by queue run 722ac2e2 (an Opus worker, read by the orchestrator before landing): the ADR proposes boxes `[ ]`, `[/]` partly delivered, `[~]` claims only, `⏳` reviews only, `[x]` delivered, and `[-]` closed and not delivered with a required reason word; named children and a checked roll-up for parents; waiting as a field, never a state. Three questions are his. Fable re-review queued as `160/1230`.
