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
  - [ ] 📊 **Eight instances, formed independently in two children and pooled
        over the cross-session channel.** Described by mechanism; no tree,
        host or product identity is carried.
        | The negative that was read | The silent second explanation |
        |---|---|
        | An artefact absent from the live filesystem tree | it was present in a backup nobody had opened |
        | A record stating a copy had been made | the bytes were not on disk; the record evidenced the attempt, never the result |
        | A directory listing returning empty | the filesystem had no mount point set — never mounted, not deleted |
        | A snapshot read through a container returning zero entries, exit 0 | the snapshot is an automount that had not yet materialised on first access |
        | A port mapping declared and not serving | silently dropped by the network driver in use |
        | Two configuration keys set and not taking effect | ignored by the image, no warning emitted |
        | A tool's records asserting a full passing test run | the self-test had been crashing for eight days |
        | A guard reporting clean over a set | the set it swept had been silently narrowed |
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
