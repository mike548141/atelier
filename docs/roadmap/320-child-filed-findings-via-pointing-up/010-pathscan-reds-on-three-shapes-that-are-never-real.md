- [ ] 🔥 **`pathscan` reds on three reference shapes that are never real, and
      the package-source-root gap is three quarters of it** `[M][tool]` —
      filed from a private child 2026-08-18 via § *Pointing up*, then
      **measured twice at atelier HEAD (`6f54489`)**, because the first
      measurement was wrong. The final classes below are the second pass.
      **Class A — no package-source-root anchor. 34 of the child's 46, and the
      whole story.** In a repo laid out `src/<pkg>/`, prose naming a module as
      `sub/module.py` reds while `src/<pkg>/sub/module.py` resolves. One extra
      resolution root drops the noise by three quarters. **A discrepancy found
      while reproducing:** the failure message names **three** anchors —
      repo-root, the file's own directory, the outermost enclosing `docs/` —
      where the module docstring advertises **four**. A reader trusting the
      docstring is being told the scanner checks something it does not; which of
      the two is wrong is part of this item.
      **Class B — prose shorthand only, and materially LESS severe than this
      item first claimed.** These red: the bare shape `docs/method/RECORD.md`
      with no sibling prefix, and `atelier/docs/method/REVIEW.md` naming the
      sibling without `../`. Both are references written as **prose shorthand
      rather than as paths** — 7 of the child's 45. The **correct relative
      shape `../atelier/docs/method/GUARDS.md` resolves fine**, because the
      repo-root-relative anchor lands on a real file wherever the estate is
      actually laid out as siblings, which is the house shape.
      🔴 **The correction, recorded rather than quietly folded in.** This item
      first claimed the correct relative form reds too, and called that the
      sharp end — *a child obeying the doctrine accrues a finding for obeying
      it*. **That was false, and the cause was an invalid control:** the
      throwaway probe repo had no sibling at the path the reference named, so
      the token had nothing to resolve to and the red was the probe's artefact,
      not the scanner's behaviour. The filing child falsified it from its own
      tree, where five references in exactly that form appear in none of its 45.
      Re-probed with the sibling present and it resolves. **This is the third
      recorded instance of a control not checked comparable before it was used
      to kill or confirm a hypothesis** — the recurring one, and the reason the
      claim is left visible here instead of being edited out.
      **And the child asked not to be credited with a check it did not make**
      (its words, unprompted): *"I only avoided the same class of error by
      accident. I had the real sibling on disk, so my probe was comparable
      without my having reasoned about whether it was."* Recorded because the
      lesson is otherwise the wrong one — **the estate got the right answer here
      from an accident of layout, not from anybody's discipline**, so nothing in
      this exchange demonstrates that the comparability check is being made.
      **Class C — token truncation, and the backtick discriminator this item
      first proposed is FALSIFIED.** Measured at HEAD: a **brace expansion**
      truncates (`docs/COLLECTING-{COMMVAULT,VMWARE}.md` → `docs/COLLECTING-`,
      red) **whether backticked or not**, and a **trailing slash is stripped
      rather than exempting the token** (`docs/client/` → `docs/client`, red).
      A `*` glob is correctly excluded by the existing lookbehind and does not
      red. So the real discriminator is **which wildcard character** — `*` and
      `?` are handled, `{` is not — and backticks are irrelevant. The child's
      original framing, *parse artefacts*, was right in spirit and wrong in
      every detail; its count of 2 stands, its cause did not, and neither did
      this item's first correction of it.
      **Controls, so this is not read as "the scanner is broken":** a genuinely
      present path passed clean and a genuinely absent one was flagged
      throughout. Three specific resolution gaps, not a failed scanner.
      🚩 **Why it earns doctrine attention and not just a tuning ticket.**
      `pathscan` is warn-only, so nothing blocks — *that is the problem*. The
      child reports **46** findings, **0 of them real** (its measurement, in its
      repo, recorded as reported and **not** reproduced here — this session
      verified the three mechanisms, not the tally). A check that prints an
      unactionable page on every commit is the alarm-fatigue failure
      `PROPAGATION.md`'s own drift-check rationale names — *"a check that keeps
      re-surfacing old noise trains sessions to skim it"* — and it is training
      sessions to skim the one output where a real stale path would hide. It
      also fails `GUARDS.md`'s fourth requirement in spirit: at a 0%
      true-positive rate it neither makes a failure cheap nor forbids an act.
      📈 **The tally moved between the measurement and the filing, and that is
      the argument in miniature** (child's amendment, 2026-08-18). It was 45
      when measured and **46 an hour later**, because the child added one board
      item that referenced a path in the same shorthand style and it red
      immediately. Class balance unchanged — the new one is Class A. So **the
      noise floor rises with ordinary authoring**, at roughly the rate the repo
      writes prose about its own code; a fix that only clears today's backlog
      buys back a floor that refills.
      🎯 **What would count as fixed — and the resolution root alone is not
      it.** Class A's true-positive rate is not merely low, it is **zero across
      the whole corpus**, and that stays measurable after any fix. If the
      resolution root lands and the count falls to roughly a dozen with the
      remainder still all false, the check is **quieter but still at 0% true
      positives, and still not earning its place**. The number that vindicates
      it is a **real stale path caught after the noise is gone**. So the
      closing evidence for this item is a re-measurement showing both a lower
      count *and* a non-zero true-positive rate — not a lower count alone. The
      child has offered to file the re-measurement if it is the session that
      runs it.
      **Every child-side hatch is worse than the defect**, which is what makes
      this atelier's and not the child's: `.pathscanignore` blinds the check
      wholesale, 45 per-line markers tax every future author, and a third of the
      hits sit in frozen records that must not be rewritten retroactively.
      **Fix candidates, in the priority the second measurement supports** —
      deliberately not chosen here: add the package source root as a resolution
      root, auto-detected or declared (Class A, 33 of 45, clearly first) · add
      `{` to the wildcard lookbehind and decide whether a trailing slash should
      exempt rather than strip (Class C, cheap) · decide whether bare
      doctrine shorthand should be out-of-scope rather than missing (Class B,
      7 of 45, and the least clear-cut — the shorthand genuinely is not a path).
