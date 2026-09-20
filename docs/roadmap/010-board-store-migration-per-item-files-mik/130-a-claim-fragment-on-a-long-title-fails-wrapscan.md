- [ ] 🔎 **A claim on a long-titled item fails the wrapscan floor — on the item's
      state line and again on its generated index line** — reported by a child
      over the peer channel 2026-08-17 (the fourth child to adopt the store),
      reproduced here against `tools/wrapscan.py` at HEAD the same day; sibling
      of `070` (same scanner, a different string). The claim fragment
      `(claimed YYYY-MM-DD-HHMM, wt: <name>)` is ~48 columns and doctrine puts
      it on the state line, which `board.py` reproduces on the index line.
      wrapscan's single-token exemption holds only while every space sits at or
      before column 85 and the tail is one unbreakable token — exactly what lets
      an unclaimed `[title](store/path.md)` line pass. Prepend the claim and the
      title's own spaces are pushed past 85, so the exemption stops applying to
      **both** surfaces. Measured in the child: four claims, seven blocking
      findings, commit refused. Reproduced here: the same 162-column unclaimed
      line scans clean; with the claim in front (212 columns) it is flagged.
      🚩 **The hatch works and that is the finding.** `board.py` propagates an
      item's `<!-- …:allow: … -->` marker onto the generated line, so a claim
      can be landed by hand-adding an exemption to the item and hand-removing
      it at release — on every claim, in every child. Claiming is the most
      routine act the store asks for; a guard that taxes it that way is the
      shape people reach for `--no-verify` around.
      🎯 Candidate shapes, the child's list carried as reported (measurement
      apart from diagnosis): (i) strip the claim from `index_title`'s fallback
      (`140`, which fixes the leak but not this); (ii) a shorter claim rendering
      on the index line — does not by itself recover 48 columns; (iii) wrapscan
      learning that a **generated** file's lines cannot be rewrapped by hand,
      which is the honest reading: gating a machine-written line on a human
      formatting rule leaves no legal fix but an exemption. Detail is in the
      child's own board item `120-…/030`; the fix belongs here (PROPAGATION —
      the owning repo).
      🔎 **The discriminator is a per-repo scope declaration, not the
      exemption logic — measured 2026-09-20, and it re-frames this item.**
      This item and its candidate shapes (i)–(iii) all reason about
      `wrapscan`'s single-token exemption. That is not what separates the
      child's experience from atelier's. Atelier declares in
      `.atelier-floor.json` that `wrapscan`'s scope is `docs/method`,
      `docs/build` and `docs/decisions` — Mike's WS1 ruling, 2026-07-23,
      option A, whose stated trade is *"Cover given up: long prose lines
      outside the doctrine surface go unflagged."* **`docs/roadmap/` and the
      generated index are outside the gate here by ruling.** So atelier cannot
      reproduce this defect at all, on either plane, however long a claim
      fragment gets — and the reproduction this item records as done "here
      against `tools/wrapscan.py` at HEAD" must have been an unscoped hand
      invocation, which is not what either plane runs.
      **Grounded the hard way:** a session claiming three items this day
      produced three 127–130-column item lines and three 207–235-column index
      lines, ran `wrapscan --root . docs` by hand, got **six findings and exit
      1**, and briefly believed the tree was red. CI was green on the same
      commit, correctly. The hand run was the thing that was wrong: passing a
      path argument overrides the declared scope, so it scanned a surface the
      floor never gates. *A scanner run outside its declared scope is not
      evidence about the floor* — and this item's own reproduction is an
      instance of that error, which is why it is recorded rather than tidied.
      🔑 **What this makes the real question.** Not "how should wrapscan treat
      a generated line", but **whether the scope narrowing that insulates
      atelier is part of what a child inherits.** It is currently a local
      declaration the parent holds and children do not, so the parent is
      immune to a class its children meet on the most routine act the board
      asks for. That is the same shape as `320/160`'s finding about the floor
      block — a parent-local accommodation that does not travel — and it is
      probably the cheaper half of this item to rule on.
      📈 **Measured in a child the same day, and the cause is confirmed.** A
      private child checked its own `.atelier-floor.json`: the `scope` block
      declares **one scanner, and `wrapscan` is not it**, so wrapscan runs
      unscoped over `docs/**`, `docs/roadmap/` included. The consequence,
      counted: **237 of 324 board item files carry a `wrapscan:allow`
      marker — 73%.** The child is not immune and never was; it pays a
      per-item marker where atelier pays one scope declaration. So the
      discriminator above is measured, not inferred, and this item's original
      reasoning about exemption logic is **downstream** of it — the exemption
      is what a child reaches for *because* it lacks the declaration.
      ⚠️ **The reporting child's own caveat, carried rather than shed:** it
      measured that 237 of 324 items carry a marker, **not that 237 markers
      are justified.** Counting them says how many there are, not whether
      they are right; anyone ruling on this should sample them.
      🔑 **And the substitute is worse than the accommodation it replaces.**
      Those markers are not free: a written reason each, hand-edited on every
      new item, and the child has a recorded instance of `secretscan` reading
      a long allow-reason as a secret. The parent's single declaration has no
      such failure mode. That is what makes this a doctrine question rather
      than an inconvenience — the child does not merely lack the parent's
      accommodation, its only available substitute carries a hazard the
      accommodation does not.
      🚩 **Second instance of the same asymmetry, same evening, different
      face.** A *different* private child filing a hand-up here had to file
      **class-only — no repo name, no paths** — because atelier is public and
      a private child naming itself in a public parent is the same disclosure
      as a public parent naming a private root, read from the other end. One
      child pays per-item markers where the parent pays a declaration;
      another pays anonymity where the parent can afford to name itself.
      **The class:** the parent holds accommodations its children cannot
      inherit, and neither child can see the asymmetry from where it stands.
      Neither can atelier, which is immune by declaration — the blind spot is
      structural on both sides.
      🎯 **The real question this leaves:** whether the scope narrowing that
      insulates the parent is part of what a child inherits. Same shape as
      `320/160` on the floor block; probably the cheaper half of this item to
      rule on.
