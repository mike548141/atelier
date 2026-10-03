- [ ] 🔎 **A wrapped claim does not project into the index, a `]` in a title
      breaks its generated link, and the §10 declaration's home is ambiguous
      between GUARDS and practice** `[tool][doctrine]` — three findings handed
      up from a private child 2026-09-26 via § *Pointing up*, out of four
      rule-4 cold passes it ran that day on Fable. Stated class-only: no repo
      name, no child paths. Each was formed by a cold reviewer against the
      child's tree and reconciled against this board's own items before
      filing; the reconcile is where the overlaps below come from.
      Consideration and remediation are atelier's; the child stops here.

      ## 1. `board.py` reads the first physical line only, so a wrapped claim is invisible — BS2 widened `[tool]`

      **The mechanism is BS2's** (the index projects an item's first physical
      line; `item_state` at `tools/board.py` line 180 takes `rest` from that
      line and `index_line` at line 217 runs `CLAIM_RE` over it). What the
      child adds is evidence BS2 did not have:

      - **Every live claim on that board was invisible.** Four items were
        `[~]` at once; the index carried the bare `[~]` for all four and no
        `(claimed …, wt: …)` fragment (`grep -c claimed` over the generated
        index returned 0). Each item file had wrapped the claim onto its
        second physical line — which the 85-column `wrapscan` limit makes
        the *normal* shape once a bold title and a claim share line one.
        So the tool's own promise (the claim is "surfaced in the index so
        'who has this' is one glance") did not hold on a compliant child,
        and judging an orphan claim (CONCURRENCY § Orphan claims — the
        `wt:` name is the signal) meant opening every `[~]` file.
      - **The hand workaround has already decayed.** The child's split
        session re-emphasised seventeen leads so the bold closed on line
        one. An item added a month later, by a session that did not know
        the convention, has a wrapped title and renders truncated. The
        convention is written nowhere, held by no check, and cannot in
        general coexist with the wrap limit once a claim is appended.

      **Severity divergence, stated for the principal:** the child's reviewer
      graded this MAJOR on the local consequence for sessions; BS2 stands
      MODERATE here. The child does not re-grade atelier's finding; it
      reports that the consequence is larger on a child than the parent's
      evidence showed.

      **Proposed remedy:** parse the item's *logical* first paragraph — join
      indented continuation lines before `TITLE_RE` and `CLAIM_RE` run — so a
      wrapped title and a wrapped claim both project. Until it lands,
      children need one README sentence saying what the index does and does
      not show; the child has queued its own.

      ## 2. `index_title` never escapes `]`, so a bracket in a bold title breaks the link silently `[tool]`

      Probed on a scratch copy by the child's reviewer: a bold title whose
      text contains a close-bracket then an open-paren renders as a link to
      whatever follows the paren, with the rest as trailing text; a bare
      `]` and `[` pair in a title likewise; HTML in a title passes through
      raw. (The literal probe string is not reproduced here: this item's
      own first commit was blocked by `linkscan` reading it as a link —
      the finding demonstrating itself on the way in.)
      `index_title` (line 196) strips `*`, backticks and flags and does not
      touch `]`. **Narrowed at the reconcile:** the `](` shape is caught by
      `linkscan` at the index line (enforced — a `missing-file` finding), so
      it is not silent; a bare `]` in a title and a filename containing a
      space both render broken on GitHub and pass every scanner. A macron in
      a filename is fine. The HTML pass-through is within the committer
      trust model (the renderer sanitises) and is noted, not raised.

      **Proposed remedy:** escape `]` in generated link text, or have the
      rebuild report the shape as a problem line the way it reports a
      missing state line. The child's reviewer could not check this against
      BG5–BG14 (it did not open this repo's review files) — **overlap
      unverified**, please check at triage.

      ## 3. Where a non-guard §10 declaration lives — GUARDS says the `review:` line; a child's pass put it in ADR sections `[doctrine]`

      GUARDS § *The home* (lines 62–68 at the pin the child read,
      `e876f87`): until the registry slot lands, "for non-guard designs the
      situation test's 'say which you chose' homes in the existing `review:`
      line". A child's declaration pass — five ADRs, one standing-themes
      gloss — homed each declaration in a **numbered ADR section with its
      grounds**, and did not touch the `review:` line, with no reason given
      for the different home. The child's cold reviewer found that as a
      defect against the parent's text, and also that the `review:` line is
      a poor fit for a declaration that carries grounds: a numbered, dated
      section is arguably the better convention for an ADR, and the line is
      better as a *pointer* to it.

      **Filed as a question, not a fix.** Which is the house convention for
      an ADR-shaped design: the declaration *in* the `review:` line, or a
      dated section with the `review:` line pointing at it? The child has
      applied nothing pending the answer; its own findings on the pass sit
      with its principal.

      ## A pointer, not a finding — the `⏳` marker has two shapes across the fleet

      This board's own docstring and at least one item here use the bare
      form (`- ⏳ …`); the child's board uses it as a flag on a checkbox line
      (`- [ ] ⏳ …`). Both render; `pointerscan` accepts both. Nothing is
      broken; the child mentions it because a generated legend that
      describes one shape will be wrong for the other, and the child's own
      legend describes neither.

      **Provenance.** Reviewer: a cold Fable spawn per pass, in its own
      worktree, orchestrated by a session that formed no finding
      (reviewer-plus-orchestrator, disclosed on the child's board). The
      findings were reconciled against this board's items `010/020`,
      `010/030`, `010/050`, `010/060`, `160/220`, `160/390` and `290/050`
      and the board-store ADR; this repo's `docs/reviews/` and
      `docs/sessions/` were not opened by the reviewer.
      review: not warranted — a hand-up of three findings; the passes that
      produced them are each already a review.
