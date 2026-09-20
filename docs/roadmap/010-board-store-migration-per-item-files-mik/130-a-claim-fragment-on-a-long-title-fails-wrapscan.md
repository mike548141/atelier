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
      ⚠️ Not yet measured: whether the reporting child, or any other, actually
      lacks the declaration. Asked of a child session 2026-09-20; unanswered
      at filing. Atelier cannot measure it — it is immune by declaration,
      which is exactly the blind spot being described.
