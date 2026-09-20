- [ ] **REPORT — a child cannot stamp its inlined floor at all: `source=` may
      not leave `--root`, and every child must reword the canonical region
      anyway, so no correct child copy can be character-identical** `[M][tools]`
      — filed from a private child, 2026-09-06, via § *Pointing up*. Both
      obstacles re-verified here against `tools/stampscan.py` at `35912e3`
      before filing.

      ## What the child measured, and why this is not tool tuning

      The child's inlined floor **contradicted its canonical source for 60+
      commits while every check in its floor stayed green** (the child's
      measurement in its own repo, 2026-08-17, recorded as reported and not
      reproduced here). The drift was found by hand during a pin bump, not by a
      check: its apex bullet still named an ordering atelier had already
      removed, and three whole canonical bullets — concurrency, session rhythm,
      estate resources — were simply absent.

      `PROPAGATION.md` § *One statement, stamped copies* says the failure mode
      of a stamped copy is drift, and that `stampscan` was built to catch
      exactly this class. The class's real home is the children, and the
      scanner cannot reach them — so the one place the failure actually
      happened is the one place nothing watches.

      The child added no stamp markers rather than assert a compliance it has
      no way to check. That is the § *The duty* posture — the workaround
      reported, not silently kept — and it is why this is filed as a question
      for atelier rather than as work the child could have done.

      ## Obstacle 1 — source confinement (already half-owned here)

      A stamp names its canonical text as `source=<repo-relative-path>`, and
      `resolve_source()` resolves it against `--root` and rejects anything
      outside as a config error, exit 2, never downgraded. That confinement is
      deliberate — it is the 2026-07-26 cold pass finding on source resolution,
      which closed a crafted-`../`-traversal hole. The canonical region lives
      in `docs/method/PROPAGATION.md`, which is inside atelier and outside
      every child's root. **So there is no spelling of `source=` a child can
      write that resolves.**

      Already owned here, and named as such rather than re-filed: the
      scanner's own module docstring says a scaffolded child running it would
      exit 2, and
      [`020/110`](../020-policy-as-code-programme-five-tracks-mik/110-d2-residue-stampscan-registry-wiring-stays-bar.md)
      bars registry wiring until the child-side resolution story exists. This
      report restates obstacle 1 only because obstacle 2 sits behind it and
      survives every fix to it.

      ## Obstacle 2 — placeholder substitution, which no `source=` fix touches

      § *The standard child doctrine block* instructs every child to fill four
      placeholders in the copy it inlines: `<SHA>`, `<atelier-path>`,
      `<visibility fact>` and `<owner/repo>`. `stampscan`'s comparison is:
      equal is clean; an ordered subsequence of the canonical lines with a
      declared `narrow=` is clean; **anything not obtainable by pure deletion —
      an added, reordered or reworded line — is drift, red, regardless of
      `narrow=`.** Substitution rewords. There is no placeholder or template
      mechanism anywhere in the tool.

      **So a fully compliant child copy reds by construction**, and the
      declaration that excuses omission cannot excuse it.

      Measured on one private child's current, correct copy against the
      canonical region at `35912e3`:

      - the region is **86 lines**; **9 of them differ** in the child, rendered
        as 13 lines after re-wrapping;
      - **5 of those 9 carry the four mandatory placeholders** — the heading's
        pin, the two `Source & drift` lines, and the two visibility lines;
      - the other 4 are a private child's permitted naming of the estate root
        plus the re-wrap that naming forced;
      - **none of the 9 is obtainable by deleting lines.**

      🔑 **One placeholder perturbs more than one line.** A substituted value of
      a different length re-wraps the rest of its paragraph, so the deviation a
      child cannot avoid is wider than the number of placeholders suggests.

      🚩 **Pin-awareness does not answer this.** A pin-aware resolution decides
      *which* canonical text a child is compared against; obstacle 2 is about
      *how* a filled line can ever compare equal to the placeholder it filled.
      A child pinned exactly at atelier's tip still reds.

      ## The ask

      Decide how a child stamps its inlined floor across a repo boundary — or
      rule that it does not, and name what closes the drift class instead,
      because the measurement above is what happens when nothing does.

      Sketches only, raw material rather than a design, and deliberately not
      chosen here:

      - **A placeholder-aware comparison** — a canonical `<name>` token matches
        any single substituted run on the child's side, so a filled placeholder
        compares equal while a genuine reword still reds.
      - **Declare substitution the way narrowing is declared** — e.g.
        `fill=<placeholder-list>` on the child's begin marker, so a filled line
        is excused by name and an undeclared reword is not. This keeps the
        property that makes `narrow=` work: the declaration is the signal.
      - **A configured parent path** that `source=` may reach, the way the
        floor already reaches atelier's tools through a git config value —
        keeping the confinement rule against crafted traversal while giving the
        child one legitimate way out of its own root.

      Consideration and remediation are atelier's; the reporting child stops at
      this report.

  - [ ] 🔎 **Corroboration from a second private child, 2026-09-20 — and the
        standing-practice consequence this item does not yet draw.** Filed via
        § *Pointing up* at atelier's invitation, appended here rather than
        opened as its own item because it strengthens this finding rather than
        adding one.

        **The corroboration is weak and is labelled as such:** a second child
        independently hit obstacle 1 (the canonical `source=` may not resolve
        outside `--root`) and reached the same conclusion — no instrument can
        check its inlined floor. That is an echo, and an echo is not evidence.

        **The additive part is the consequence.** If a *compliant* child reds
        by construction — which this item establishes, and which no fix to
        obstacle 1 removes — then hand verification is **not a stopgap pending
        a better `stampscan`**. It is the only instrument that can ever pass a
        compliant child, and it will remain so under every sketch above except
        the placeholder-aware one. That reframes what children should be told:
        not *wait for the tool*, but *run the hand check on a cadence now*,
        whatever the ruling turns out to be. This item currently ends in a
        question for the principal; the practice question has an answer today
        and does not need to wait for it.

        **Grounded, not proposed in the abstract** — the filing child has run
        it twice, on 2026-08-17 and 2026-09-20:

        - **Method.** Extract the canonical region from the parent by its
          `floor:begin` / `floor:end` markers; extract the child's inlined
          block by its `stamp:begin` / `stamp:end` markers; fill the
          placeholders **by script rather than by typing**, so "verbatim" is a
          property of the construction and not a claim about care; compare
          byte-for-byte. Placeholder fills are the only permitted difference,
          and the check also asserts zero residual `<placeholder>` tokens and
          no line over the wrap limit, since a fill can silently push one over.
        - **Cadence.** Every pin bump — which is also when the parent's region
          can have moved, so the check costs nothing extra at the one moment it
          can find something.
        - **It found something.** On 2026-09-20 the check caught a real drift
          on a 288-commit delta: two whole floor bullets absent from the
          child's copy, and a stale recipe in a third that was **actively
          wrong** — it instructed reading staged **hunk headers**, which strip
          the very paths that check exists to surface. The child had been
          following it for four commits that session. No tool would have caught
          it, because no tool can run here.

        **The honest limit.** This says nothing about whether the hand check
        *scales* — it is one child, one operator, and a step that is skipped
        the moment it is inconvenient leaves no trace of having been skipped.
        That is an argument for the tool, not against the practice; the two
        are not alternatives, and the practice is what holds until the tool
        exists.
