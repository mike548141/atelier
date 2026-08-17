- [ ] 🚩 **The floor clause has to reach 11 children, and each child adopts it
      in its own session** `[M][docs]` — blocked on `010` landing the canonical
      text, then open to every child. Mike ruled **method plus floor**, not
      method alone, on 2026-08-17.
      **Why it is not one sweep from here.** Work lands in the repo it changes
      (Mike's ruling, 2026-08-09) — a floor edit made sideways from an atelier
      session is the breach that ruling names, and the auditing-session shape is
      exactly what tempts it. So this item is a *queued* instruction: each child
      bumps its pin, re-inlines the canonical floor region, and re-stamps, in a
      session working that repo.
      **What the mechanism does and does not do today, measured rather than
      assumed.** `tools/stampscan.py` compares a child's stamped copy against
      the canonical region — but it is deliberately **not** in `floor.py`'s
      registry, not in the reusable floor workflow, and not in the pre-commit
      hook, because its ST3 precondition is open: the stamp's `source=` resolves
      to a path that exists only in atelier, so a scaffolded child running it
      would exit 2. ⇒ **Editing the canonical region reds no child's commits.**
      A child stays green on its old copy until a session there reads the pin
      drift and re-stamps. That is the propagation path, and it is a *read*
      obligation with no machine behind it yet.
      **The one lockstep that IS mechanical, inside this repo.**
      `docs/build/templates/CLAUDE.md` carries a stamped copy of the floor
      region and `tools/test_templates.py` asserts it matches the canonical text
      exactly. Canonical edit and template re-stamp land in one commit or
      atelier's own floor goes red.
      **The first child's position, reported on the channel 2026-08-17 by a
      session live in it.** `faves` bumped its pin to `19eb0e2` that day, having
      measured `git diff <old-pin>..origin/main -- docs/method/` **empty at that
      moment** — so this section's floor commit is *exactly* the next drift its
      check will report, and the re-inline plus re-stamp is **owed at that next
      bump, not done**. Recorded because it is the one case where the read
      obligation has a known trigger rather than an open-ended one; the other
      children's pins are wherever they are.
      **Sequencing worth stating.** Only one child in the fleet currently runs
      five sessions wide, which is where the clause pays. The other ten inherit
      it against a hazard they have not met yet — cheap to carry, and the
      timing trap named at `030/140` applies here too: a concurrency rule looks
      theoretical on the day it is adopted and bites on the first morning of
      real parallel load.
