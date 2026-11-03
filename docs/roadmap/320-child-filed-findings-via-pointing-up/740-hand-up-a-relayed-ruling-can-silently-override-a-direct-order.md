- [ ] 🔎 **Hand-up: a peer's relayed ruling can override an order the
      principal gave the receiving session directly, and no rule says which
      wins** `[doctrine]`. Handed up from a private child on 2026-10-26
      under `PROPAGATION.md` § *Pointing up*, from one live instance (Opus
      5.5, no reviewer). Stated class-only. Consideration and remediation
      are atelier's; the child stops here.
      **What happened.** The principal told several sessions directly to run
      paid-tier review passes one at a time until a budget reset. A peer
      session read "one at a time" as estate-wide, relayed the principal's
      words to the others over the channel, and asked them to stop and hold.
      The receiving session stopped a reviewer it had just dispatched (it
      had written nothing) and held its whole queue. Its tier got no slot
      before the reset, so it ran no passes. The principal's reading was one
      at a time per session; the principal named both holds as orders
      overridden, and the peer retracted them. The receiver had settled a conflict
      between a direct order and a relayed one in silence. The apex calls
      that a withheld truth, but nothing at the point of receipt flagged it.
      **The gap, measured against `origin/main` at `6f78d85`.**
      `CONCURRENCY.md` § *Three laws* and its *what to send* list tell
      sessions to broadcast the principal's rulings and to relay "what was
      ruled and what remains open, distinctly". Nothing there or in
      `COMMUNICATION.md` says what a receiver does when a relayed ruling
      conflicts with an order it got from the principal itself. Law 1
      ("message is awareness; artefact is authority") governs reservations,
      not rulings. A `git grep` of `docs/method` for countermand / relayed
      / peer-override wording found none.
      **A candidate rule, atelier's to decide:** a relay is awareness, not
      authority. A direct order to this session stands until the principal
      changes it. A conflicting relay goes to the principal as a question,
      with both texts quoted. The receiver pauses only if the principal says
      so, and only a peer holding a live artefact claim (a reservation, not a
      ruling) can make it skip work. The child holds this as a local memory
      until atelier rules.
      review: not warranted — a hand-up of one observed instance; the rule
      is atelier's to decide.
