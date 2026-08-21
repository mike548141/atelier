- [ ] 🎯 **PROPOSAL — a transcript has three principal-authored channels, and a
      read that names one is a confident negative** `[S][docs]` — filed from
      `cbom` 2026-08-19/21 via § *Pointing up* (its board `120/080`), on Mike's
      direction to that session: *"Suggest it to atelier repo for doctrine +
      guards"*, and then *"pass that question to atelier for it to look into"*.
      **The three channels.** Opening prompts (`type:"user"`,
      `message.role:"user"`) · **mid-turn messages** typed while a session works
      (`type:"attachment"` · `attachment.type:"queued_command"` · text in
      `.prompt`) · structured rulings (an `AskUserQuestion` selection, arriving
      as a `tool_result`). A read filtering on `type == "user"` drops the second
      and third **silently**.
      **Reproduced at the parent, estate-wide, 2026-08-21.** 4,433 opening
      prompts against **2,237 mid-turn** — **33.5%** of the principal's messages
      across the live store, by repo: `kainga` 56.8% · `faves` 54.4% · `cbom`
      53.0% · `shed` 24.9% · `ros` 24.2% · `atelier` 23.5%. The child measured
      44% on its own 26-transcript slice; the class holds well past its repo.
      **The consequence is scope loss, not sampling noise.** The filer's worked
      example: of the nineteen most consequential instructions its repo holds,
      **all nineteen arrived mid-turn and none as an opening prompt** — four of
      the five deliverables that repo exists to produce were commissioned in
      messages a `type == "user"` read cannot see. An audit built that way does
      not return a noisy answer; it returns *"he never asked for that"* about
      work he commissioned.
      **Two candidate rules, as filed.** (1) **A mid-turn instruction is a
      first-class instruction** — it arrives as steering rather than as a brief,
      so a session acts on it and never homes it; if it is standing or a ruling,
      home it before the turn ends. That is `GUARDS.md`'s *a rule with no home*
      duty applied to an **arrival mode** rather than a rule type. (2) **An audit
      of what the principal has asked for states which channels it read** —
      otherwise its negatives are artefacts of its filter.
      **Where the class already bit atelier:** `210/100` — `cctranscript` reads
      only channel one at both selection points and prints `searched
      prompts+replies` anyway. That is this finding's strongest evidence and it
      was found in the house's own instrument, not the child's.
      **Related:** `320/080` (the `quotescan` proposal, which depends on this
      one) and `020/…`'s check of the 2026-08-09 measurement, which the same
      filing prompted and which came back clean.
