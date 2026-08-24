- [ ] 🔎 **CF3's branch list stopped answering the sibling-dirty case when the
      board split, and what replaced it is a stop with no exit** — filed from
      `cbom` 2026-08-24 via § *Pointing up*, over the **channel** (the second
      filing shape), explicitly to avoid writing into a tree the parent was live
      in. Reported with the workaround rather than the workaround kept: the
      child hit this, could not comply, proceeded anyway, and says so.
  - [ ] **The report, as received.** `CONCURRENCY.md` § *Claiming at a dirty
        primary checkout* (CF3) gives two branches. **A:** if the stranger's
        edits do *not* touch the queue — *"any item's state line — yours or a
        sibling's"* — stage and commit the claim alone. **B:** if *"the item's
        file **itself** is dirty"*, sync, take the next open item, touch
        nothing. A **sibling's** item line being dirty touches the queue, so A
        is excluded; it is not your item's file, so B does not fire. The child
        read the branch list and concluded the case was in neither.
  - [ ] ✅ **Verified here, quotation by quotation, against `origin/main`.** All
        three quoted fragments are byte-accurate, and the reading of them is
        right: the branch list, read alone, does not resolve the sibling case.
  - [ ] 🔎 **But the house does answer it — thirty lines earlier, inside a
        parenthetical.** The split-board paragraph carries *"a dirty sibling
        item state line is a stop for claiming from that checkout, not a
        stage-yours-alone case — BS1; wording per the principal's ruling
        2026-08-23, until the staged-plane check lands"*. So this is a
        **findability defect, not a gap** — the category § *The duty* names
        explicitly. The sharp part is where the child found the rule instead:
        **in `cbom`'s own inlined floor**, and it reported it as the child's
        local addition. A stamped copy was more findable than its source, which
        is § *Pointing up*'s own second-order hazard running in reverse.
  - [ ] 🔑 **The child's suspicion is FALSIFIED, and the history is the useful
        part of this item.** It suspected *"yours or a sibling's"* was
        over-broad and that branch A had always meant *your* item. The opposite
        is true, and it is checkable in three commits:
    - [ ] `87af9f9` (CF3 as ruled, 2026-07-20, monolithic board): both branches
          keyed on **"the queue file"** — one file for the whole board. Any
          dirty item line meant the queue file was dirty, so the sibling case
          fired **branch B** and was answered.
    - [ ] The split-board migration rewrote *"the queue file"* to *"the item's
          file"*. That silently narrowed B from *any* item to **your** item, and
          the sibling case fell out of the branch list — not by a decision, but
          as a side effect of renaming the unit.
    - [ ] `80e6fc0` (BS1 applied, 2026-08-23, the principal's ruling) then
          widened A's exclusion to *"any item's state line — yours or a
          sibling's"* **deliberately**, because a rebuild can absorb a sibling's
          dirty state line — the exact defect that ruling closed.
    - [ ] So shape (i) as offered — *narrow A back to "yours"* — is not a
          restoration of intent; it re-opens what BS1 closed. What the history
          actually indicts is the **rewrite that emptied branch B**.
  - [ ] ⚖️ **What survives the correction, and it is the real finding: the stop
        has no exit.** Three rules bind at once — the claim lands on `main`
        **from the primary checkout** (§ *Where the claim lands*, load-bearing
        by its own words), a queue-dirty primary is a **stop** for claiming from
        that checkout (BS1), and work is claimed **before** it starts. A
        worktree cannot discharge the first. The only remaining moves are an
        **unbounded wait** on a peer whose finish time is unknowable, or
        **working unclaimed** — and doctrine sanctions neither. BS1's own
        wording concedes the posture is interim: *"until the staged-plane check
        lands"*, which is [`010/020`](../010-board-store-migration-per-item-files-mik/020-board-check-staged-plane-seam.md).
  - [ ] 📎 **Not a duplicate of
        [`030/140`](../030-enforcement-propagation-the-estate-rollo/140-cf3-s-claiming-rule-collapses-on-a-monolithic.md),
        and the two together are the argument.** That item is the same deadlock
        on the **yield branch** of a **monolithic** board, and it says of this
        clause, correctly, that it is *"a different clause … the finding stands
        exactly as written"*. The pair matters: the deadlock survived the split
        that was supposed to be its fix. It moved from "the board file is dirty"
        to "a sibling's item file is dirty" and kept its shape, so *split the
        board* is not on its own an answer to it.
  - [ ] 📄 **What the child actually did, recorded because the evidence is the
        point.** Worktree taken; file set announced on the channel and the
        peer's read back; work built **unclaimed**; claim and completion
        committed together afterwards; landed by fast-forward once the peer's
        tree was clean; no peer file staged, absorbed or reset. Logged in the
        child's own record as **done out of order**, not as compliant. That is
        the § *The duty* clause working as written — the workaround reported
        rather than kept.
  - [ ] 🎯 **Mike's to rule; raw material only, and one option is already dead.**
        (i) is falsified above. **(ii) sanction the claim-after-the-fact** where
        the primary is queue-dirty, with the out-of-order act recorded and the
        file set announced first — which is what the child did unprompted, and
        the shape it says it would rather doctrine named than have each session
        invent. **(iii) restore an answer to the branch list itself**, wherever
        the ruling lands, so a reader meets it where the branches are
        enumerated rather than in a parenthetical thirty lines up. (iii) is
        cheap and independent of (ii): it fixes the findability half whatever is
        decided about the deadlock half.
  - [ ] 🔁 **The child fed one more observation back, and checking it here
        changed both the number and the owner** (2026-08-24, same channel). Its
        offer: the reverse-direction hazard has a cheap general fix — *an
        inlined floor bullet names its source file* — and in its own block the
        omission looked local and inconsistent rather than structural, since
        other bullets cite doc names and the BS1 one does not. Measured against
        **atelier's canonical `floor` region**, which is the surface that would
        actually have to change:
    - [ ] 🔑 **The canonical block does not carry the sibling stop at all** —
          zero occurrences of "sibling" in the whole region. So the earlier
          reply to the child needs a precision it did not have: **the rule is
          atelier's** (`CONCURRENCY.md` § *Claiming work*), **the inlined bullet
          carrying it is the child's own**. Both halves matter — the child was
          wrong that the rule was local, and right that the bullet was.
    - [ ] ⚖️ **"Bullets don't cite their sources" is 1, not 4.** Five of nine
          canonical bullets name a doc; four do not, and three of those are
          deliberate: *Source & drift* names a **path**, which is its source;
          *Estate resources* omits the estate-root repo **on purpose** (a public
          repo naming it is reconnaissance); *This repo's visibility* is a repo
          fact, not doctrine. That leaves exactly one real instance — **the apex
          bullet states the never-traded rules and never names `00-APEX.md`,
          while the bullet directly beneath it does.** Reporting the raw
          four-of-nine would have been the over-claim; the finding is one line.
    - [ ] 📎 **What is NOT verified, and is the child's to check:** its block
          reportedly cites `GUARDS.md`, which the canonical region does not. If
          so its block differs from canonical in more than the BS1 bullet, and
          that is a pin-bump question in that repo — flagged, not asserted, and
          not this session's to look at (`CONCURRENCY.md` § *Stay in your lane*).
    - [ ] ✅ **The child declined to make the child-side edit because a peer
          asked**, and sent it to Mike as a recommendation instead. Recorded
          because it is the right call and the cheap thing to get wrong: a
          citation is a small edit, and "small" is exactly the argument that
          erodes the line. It is also why the fix above is written as a finding
          for ruling rather than applied here.
