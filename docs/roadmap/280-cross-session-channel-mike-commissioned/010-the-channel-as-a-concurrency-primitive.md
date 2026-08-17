- [~] 🎯 **The channel as a concurrency primitive — a new section in
      `CONCURRENCY.md`, and a floor clause beside it** `[M][docs]` (claimed
      2026-08-17-0734, wt: channel-doctrine-0817) — Mike commissioned
      2026-08-17 after reading four days of five-session parallel work in the
      public child `faves`.
      **The gap, stated as a property rather than an omission.** Every
      coordination mechanism this house has works by forcing a collision onto
      one shared line so git catches it. That covers the tree, the queue and
      the record namespace. It cannot cover a class where **both parties are
      individually correct and neither has written yet** — and that class is
      where the measured cost sat.
      🔑 **The formulation the whole section turns on, from the child:** *a file
      map is a claim about your own writes; a collision is a fact about
      somebody else's.* No amount of care about your own half surfaces it. Only
      the overlap of two broadcasts does — and in the grounding case it was a
      **third** session noticing two answers to one broadcast that found the
      double-held file.
      **Three laws, each grounded in a failure rather than reasoned:**
      1. **Message is awareness; artefact is authority.** A message reserves
         nothing — only a pushed artefact does. Every version reservation in
         the grounding window was stale by merge time, and a session spent a
         day broadcasting exactly that rule before colliding on an identifier
         anyway.
      2. **The closing check runs after the push, not before.** Reading a
         shared allocator before you write reads a value that expires in
         minutes. Generalises past identifiers to every shared counter.
      3. **A repair is itself a claim, and its tie-break must be
         deterministic.** Courtesy is not coordination: two sessions each
         politely yielding off a collided identifier both chose the next free
         number and collided again five minutes later. The tie-break has to be
         a function of shared public evidence both parties compute
         identically — *fewest inbound references*, cheapest repair over
         precedence — and the repair is announced, never taken silently.
         Corollary: a burned identifier stays burned, and an allocator counts
         records rather than contiguity.
      **The cost clause, and it is not optional.** The channel's own primary
      source records four rounds of which **two existed only to correct claims
      made in the earlier two**. A primitive that makes peer contact cheap also
      makes it cheap to be confidently wrong at a peer before anyone opens a
      file. Its pair is the strongest primitive in the same transcript: both
      load-bearing corrections came from a party **re-running** a claim rather
      than reasoning about it. The smooth handoffs were not the value.
      **A publication clause, which was not foreseen.** The channel crosses
      repo boundaries, so it crosses publication boundaries. One exchange in
      the transcript is deliberately abridged: it joined a repo name to a
      guard-coverage inventory, the reconnaissance shape `PROPAGATION.md` bars
      from a public tree. What two sessions may safely say to each other is not
      what a public record may hold — abridge on the way *into* the record, and
      say that you did.
      **Scope, and what is deliberately left alone.** The section is new text
      plus corollary edits at the seams (claiming gains the file-set
      broadcast; integration hygiene gains absorption and the post-push
      check; interruption gains the close broadcast). It does **not** touch
      the CF3 yield branch — `030/140` is an open finding against that exact
      passage and the fix is Mike's to choose, so rewriting it here would
      leave the board carrying a finding against text that no longer exists.
