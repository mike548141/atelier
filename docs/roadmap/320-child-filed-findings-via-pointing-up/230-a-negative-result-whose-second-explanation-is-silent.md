- [ ] 🔎 **MISSING HOUSE RULE — the method has no name for *a negative result
      whose second explanation is silent*, though it already reasons that way
      case by case** — filed from a private child 2026-09-08 via
      `PROPAGATION.md` § *Pointing up*, by direct write into the parent's tree,
      PR opened before stopping. Class only: no repo, host, client or child
      filename appears below.
  - [ ] 🔑 **The class.** A probe returns nothing — an empty listing, a missing
        directory, a zero count, a setting that had no effect — and the reading
        taken is *"the thing is not there"*. But the negative has a **second
        explanation that is silent by construction**: the observer could not
        see it, or the mechanism quietly declined to act. The expected
        explanation and the silent one produce **byte-identical output**, so
        nothing in the result discriminates between them. The defining
        property, and the reason it survives review: **the failure always
        presents as a successful check.**
  - [ ] 📊 **Nine instances. The first eight** were formed independently in two
        children and pooled over the cross-session channel; **each child then
        read its own four back against source and confirmed them**, rather than
        letting the other's paraphrase stand. Described by mechanism; no tree,
        host or product identity is carried.
        | The negative that was read | The silent second explanation |
        |---|---|
        | An artefact absent from the live filesystem tree | it was present in a backup nobody had opened |
        | A record stating a copy had been made | the bytes were not on disk; the record evidenced the attempt, never the result |
        | A directory listing returning empty | the filesystem had no mount point set — never mounted, not deleted |
        | A snapshot read through a container returning zero entries, exit 0 | the snapshot is an automount that had not yet materialised on first access |
        | A port mapping declared and not serving | silently dropped by the network driver in use |
        | A setting applied to a service and never taking effect, for months | that image maps the setting from a *different variable name* than its sibling image does; nothing warned |
        | A configuration key rejected as malformed | the rejection **is** logged — into a container log nobody reads — and the default silently stands |
        | A tool's records asserting a full passing test run | the self-test had been crashing for eight days; a test that dies counts nothing and reports nothing |
  - [ ] 🔥 **A NINTH INSTANCE, ADDED 2026-09-08 AFTER THE ITEM WAS FIRST
        WRITTEN, AND IT IS THE METHOD'S OWN DRIFT CHECK.** This one is worth
        more than the other eight together, because the sentence that produces
        the false reading is written into **every child's onramp**, so a session
        that obeys it *correctly* gets the wrong answer. Two children hit it
        the same day, **in opposite directions**, which is what makes it a
        measurement rather than an anecdote.
    - [ ] **The prescribed check compares the pin against `HEAD` of a *shared*
          parent checkout** — and `HEAD` is whatever branch that checkout
          happens to be sitting on, which on a busy day is some other session's
          unmerged report branch, not the parent's `main`.
    - [ ] 🔥 **THE PRESCRIPTION IS THIS REPOSITORY'S OWN, NOT A CHILD'S
          MISREADING — located after the item was first written, and it changes
          where the defect lives.** `docs/method/PROPAGATION.md` specifies
          `<PIN>..HEAD` in **two** places: **line 46** (§ *The drift check rides
          the session-start read*, *"it now ends the doctrine block with one
          command"*) and **line 179**, which is inside the **floor-stamp block
          text every child inlines verbatim**. So this is not a child rendering
          the rule badly — every child is faithfully copying a command from
          here, and the two failure directions above are what faithful copying
          produces. It also means a child cannot fix it locally without
          **conflicting** with an explicit parental prescription, which § *the
          layer-override rule* bars absent a recorded owner exemption. The
          defect and the fix are therefore both **atelier's**, and a child that
          silently corrects its own copy has created an undeclared conflict.
    - [ ] **Direction 1 — false NEGATIVE (reported by a sibling child).** Its
          pin names a commit that is not on `main` at all: a single unmerged
          commit on a report branch, one *ahead* of `origin/main`. So the pin
          names a **proposal, not accepted doctrine**; the range against the
          checkout's branch is empty because the pin is on that same branch; and
          the range against `origin/main` is empty **permanently**, because the
          pin is ahead of it rather than behind. The check answers *"no drift"*
          in both directions for two independent reasons, neither of them drift.
    - [ ] **Direction 2 — false POSITIVE (measured first-hand by the reporting
          child, 2026-09-08).** Its pin *is* `origin/main`. The prescribed
          `pin..HEAD` returned one commit and the session recorded *"the house
          moved"*; the correct `pin..origin/main` is **empty**. It took reading
          the commit and confirming no doctrine file was touched to undo the
          false reading, and an earlier record had already been written against
          it and needed correcting.
    - [ ] ⚠️ **A third failure mode neither child hit today, named because it is
          latent in the same line:** the check reads **remote-tracking refs
          without fetching**. Even the corrected `pin..origin/main` is only as
          fresh as whoever last fetched in that shared checkout, so it can
          report *"no drift"* from a stale ref with no indication of staleness.
    - [ ] 📌 **The distinction the class may want to carry, raised by the
          sibling from its own third instance:** *no signal at all* versus
          *a signal emitted where no one observes* — a rejected setting that
          **is** logged, into a container log nobody reads, still leaves the
          reader with a silent negative. Whether those are one class or two is
          the house's call, like the split noted below.
    - [ ] 🎯 **The doctrine CONTENT is not in question here — the pin in each
          case is at or near `main` and nothing was missed.** **The protocol is
          the defect, not the position**, and fixing it is atelier's: the pin
          and drift-check design is the parent's. Filed here only as evidence
          for the class; the protocol half is raised **separately** rather than
          fixed in passing, per § *Pointing up*.
  - [ ] ✅ **Checked against this repository's own files before being called
        missing** — the step `PROPAGATION.md` § *Pointing up* requires, and the
        step a child is recorded as having skipped in 2026-08 when it asserted
        a principle the method already held.
    - [ ] `GLOSSARY.md` carries no entry for the concept, and a search across
          all 22 `docs/method/` files returns no statement of it.
    - [ ] **`EVIDENCE.md` §14 is the nearest neighbour and is NOT the same
          rule.** It governs *an instrument the agent built* reporting on
          itself — phantom success, "unknown is a valid output", silent success
          as a defect equal to silent failure. This class is about **reading a
          negative out of a system the agent did not build**, where no
          self-report is involved at all.
    - [ ] **§3 and §13 are also adjacent, not this.** Both tier and escalate
          the strength of a **positive** claim. Neither says what a *negative*
          result is worth, and the ladder in §13 has no rung for "the empty
          answer may be an artefact of the probe".
    - [ ] ⚖️ **The strongest evidence the rule is missing rather than merely
          unindexed: `SIGNING.md` line 219 is an instance of this exact class,
          stated as a one-off.** It records that a green floor is not evidence
          that a child signs, only that a particular thing was observed. The
          house already reasons this way where it has been bitten, and has no
          general statement to reason from where it has not.
  - [ ] ⚠️ **An honest limit on the generalisation, recorded rather than
        smoothed away.** One child's four instances are cleanly *a negative
        reading with a second explanation*. At least two of the other's four
        are *a positive action silently no-opped*, which may be a neighbouring
        class rather than the same one. **Whether this is one rule or two
        adjacent ones is the house's to decide** — the filing children stop at
        the report and do not write the parent's doctrine.
  - [ ] 📎 **Not claimed, so the item is not read as more than it is.** No
        position is taken on which `method/` file should hold this, on the
        wording, or on whether it warrants its own numbered principle versus a
        clause inside `EVIDENCE.md`. No parent file was edited. Nothing in
        either child's tree is cited, quoted or linked.
  - [ ] 🚩 **This item's branch deviates from `PROPAGATION.md` § *Report
        without harming the parent* rule 1, deliberately and visibly.** That
        rule prescribes `report-<reporting-repo>-<subject>`; this branch
        carries the subject and a timestamp with **no repository token**,
        because the reporting child is private and rule 2 of § *The route*
        forbids naming it in a public tree. That collision is already filed by
        a different private child as item `190` of this section, with evidence
        that names of this form are already exposed on the public remote — **not
        linked, because that item is still on an unmerged branch and a link to
        it would be broken at `main`**, which is itself a small instance of the
        class this item reports. The deviation is declared here rather than
        taken silently,
        which is § *Pointing up*'s own instruction: narrow locally **and**
        report up, never work around in silence. If the house rules the
        prescribed form must be used, this branch can be renamed and re-pushed.
