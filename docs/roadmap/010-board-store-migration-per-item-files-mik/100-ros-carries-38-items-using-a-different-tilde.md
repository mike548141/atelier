- [ ] 🎯 **A child has used `[~]` for *partially delivered* where the house
      means *held by a live session* — 38 items in `ros`, and the fleet
      rollout will keep finding it.** Handed up by the `ros` session that ran
      its split 2026-08-17, which carried all 38 across **verbatim** rather
      than let a script rewrite their state. That was the right call and is
      the reason this is a ruling and not a defect report: a state glyph is a
      claim about the world, and rewriting 38 of them by pattern would have
      asserted 38 things nobody checked.
      🔎 **Why it matters more than a vocabulary slip.** The house meaning is
      operational — `[~]` plus `(claimed <date>, wt: <branch>)` tells the next
      session *do not start this, someone is on it*
      (`method/CONCURRENCY.md` § Claiming work). `ros`' 38 carry no claim
      fragment, because there is no session to name. So a house-reading
      session meeting a `ros` board sees 38 items it must not take, none of
      which anyone holds; and a `ros`-reading session meeting a house board
      reads a live claim as "half done". **The failure is silent in both
      directions and neither reader can tell.**
      🎯 **Mike's to rule, and the options are not equal.** Normalise `ros` to
      the house grammar (someone must decide, per item, what those 38 states
      actually mean — 38 judgements, not a migration); or admit a fourth state
      to the house vocabulary, which the board README currently forbids in
      terms (*"never a fourth bracket"*, the tri-state ruling of 2026-07-22);
      or rule the child divergence legitimate and recorded, which
      `PROPAGATION.md` § *A child may add* permits **only** for adding, not for
      conflicting — a different meaning for the same glyph is a conflict, and
      conflicts need a ruled exemption recorded in the child.
      ⚠️ **The rollout should expect this rather than normalise it silently.**
      `ros` found it because it read its own 38 before migrating. A repo that
      migrates by script will carry the divergence into a per-item store
      without anyone noticing it was there. Any child brief for `shed` and
      after should ask the question before the cut, not after.
      *Source: the `ros` session's hand-up, 2026-08-17, measured in `ros` at
      its split (`98ec234`, regenerated `5cff027`).*
