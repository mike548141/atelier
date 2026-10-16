- [ ] 🔎 **Hand-up: the repo-local check seam (`local` in
      `.atelier-floor.json`) is absent from the README and the method docs, and
      a child recorded a hand-up for a capability that already existed**
      `[S][doctrine]` — filed 2026-10-11 from a private child repo via
      `PROPAGATION.md` § *Pointing up*. Class only: no repo, product or host
      appears below. Also the first adopter report for `020/130` D4.

  - [ ] 🔑 **What happened.** A child built a small checker that proves a
        service's static config is loadable, because a duplicate-key mistake
        had sat on a running host unnoticed. Its board item recorded that
        wiring the checker into the commit hook "is atelier's and per-clone,
        so this is a hand-up rather than a local edit", and the item stayed
        open for about a month on that reasoning. The seam that does exactly
        this had existed since 2026-07-26: a `local` block in
        `.atelier-floor.json` names a repo-relative script, a one-line
        reason, planes and arguments, and the floor runs it. On the day the
        child read the floor's source rather than its summary, wiring took
        one declaration and was proven by staging a deliberate duplicate key
        and watching the hook block.

  - [ ] 🔑 **Why it was missed (the findability defect).** At this HEAD the
        seam is described in the docstring of `tools/floor.py` and in
        `docs/build/REPO-STANDARD.md` (the `.atelier-floor.json` bullet). It
        is not in `docs/method/` (where `GUARDS.md` § *Related* only points at
        the file as where a repo declares what it decides) and not in
        `tools/README.md`. A child session reads its onramp block, which says
        the hook set is the parent's, and that is true and reads as "a child
        cannot add one". That is the failure `PROPAGATION.md` § *Check the
        parent's file first* warns about, in the other direction: the summary
        was right as far as it went, and the file owning the subject (a
        build-standard doc, not a method doc) was not on any path the child
        would take to it. *(Whether REPO-STANDARD.md is read by children at
        all after scaffolding is unmeasured here.)*

  - [ ] 💡 **Offered, not decided.** A short `tools/README.md` section (or a
        line in the hook sample's header, which every child reads) naming the
        seam with the one-declaration example; and the hand-up route in
        `PROPAGATION.md` § *Pointing up* asking the reporter to grep `floor.py`
        for an existing seam before filing "the hook set is the parent's".

  - [ ] 📊 **For `020/130` D4.** The child's declaration is hook-plane only,
        not CI, because the CI runner's dependencies for the checker are
        unproven there. That is a small data point on the seam: a local check
        that needs a third-party library has no stated way to declare a
        dependency for the CI plane. Child's own account; the declaration was
        run once in the hook plane and blocked a staged duplicate key.
