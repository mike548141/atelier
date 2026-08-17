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
