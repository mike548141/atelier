- [ ] 🔥 **DOCTRINE CONTRADICTION — a private child cannot obey both
      `PROPAGATION.md` § *The route* rule 2 and § *Report without harming the
      parent* rule 1: a branch name in a public repository is public, so the
      prescribed branch form publishes the one thing rule 2 forbids** — filed
      from a private child repo 2026-09-06 via § *Pointing up*, by direct write
      into the parent's tree (the first filing shape), PR opened before
      stopping. The child is not named anywhere below; that omission is the
      point of the item.
  - [ ] **The two rules, quoted byte-for-byte from `docs/method/PROPAGATION.md`
        at the branch point.** § *The route*, rule 2 (line 503): *"**Carry the
        class, never the child's specifics.** atelier is public. A finding filed
        from a private child names the *shape* of what broke and the guarantee
        that failed — never the repo, its hosts, its clients or its secrets."*
        And § *Report without harming the parent*, the first of its four rules
        (line 560): *"**Name the branch for the report, not for the parent's
        work.** `report-<reporting-repo>-<subject>` reads as a hand-up in a
        branch list."*
  - [ ] 🔑 **Why they cannot both hold.** `<reporting-repo>` *is* the repo.
        Rule 2 forbids naming the repo. A git ref is not item content and no
        rule scopes rule 2 to item bodies, but a ref is published the moment the
        branch is pushed — and § *Report without harming the parent* rule 3
        requires the push, because a finding with no PR *"is a message left in a
        drawer"*. So the sequence doctrine mandates — name the branch after the
        reporting repo, push it, open the PR — is the sequence that discloses
        the private child's identity to anyone who can read the parent. There is
        no ordering between the two rules, no precedence note, and no exception
        carved out for either.
  - [ ] ✅ **Verified here, at this branch point, not asserted.**
    - [ ] **The parent is public.** `gh repo view mike548141/atelier --json
          visibility` returns `{"visibility":"PUBLIC"}`. The whole contradiction
          rests on this, so it was checked rather than assumed.
    - [ ] **The exposure is live, not hypothetical.** `git ls-remote --heads`
          against the parent's HTTPS URL, run with **no credentials** — token
          environment variables unset, `GIT_TERMINAL_PROMPT=0`, global and
          system git config suppressed — returns four refs. **Two of them carry
          a private child repository's name as a leading path token in the
          branch name**, exactly the `report-<reporting-repo>-<subject>` form
          rule 1 prescribes. Both are on `origin`, i.e. already pushed and
          already readable by any anonymous client on the internet. A third
          local branch of the same form exists in the working clone but is
          unpushed and therefore not part of the disclosure. The names are not
          reproduced here.
    - [ ] **The PR list carries it too.** Of the three open pull requests at
          this branch point, two have titles or head refs that name the same
          private child. A PR title and head ref are public API surface on a
          public repository, so the disclosure is not confined to the ref
          advertisement.
    - [ ] ⚖️ **And the doctrine file itself does it.** § *Report without harming
          the parent* § *The instance* opens by naming a child repository in
          prose while narrating what that child's session got wrong. Whether
          that particular repo is private was **not** checked here and is not
          claimed; the point is only that the narrative form invites the same
          disclosure that rule 2 forbids, in the very section that adds rule 1.
          Section `320`'s own items also name filing children in their first
          lines.
  - [ ] 📎 **What is NOT verified, stated so the item is not read as more than
        it is.** Whether the two exposed names were a deliberate accepted
        exposure or an unnoticed side effect of following rule 1 — no record
        was found either way, and the absence of a record is itself part of the
        finding. Whether any harm has followed. Whether every child named across
        section `320` is private. And nothing inside any child's tree was
        inspected for this item (`CONCURRENCY.md` § *Stay in your lane*).
  - [ ] 📄 **Told once informally already.** The body of the open PR that filed
        `320/160`–`180` flags this same collision in passing. That is a message,
        not a tracked item — this item exists so the house has something it can
        rule on and close.
  - [ ] 🎯 **atelier's to rule — the choice is the house's, not the reporting
        child's. Three shapes, each with what it costs.**
    - [ ] **(a) Exempt a private child from rule 1's naming form**, giving it a
          neutral shape — `report-<subject>-<HHMM>` with no repo token — while
          public children keep the current form. *For:* it is the only option
          that removes the disclosure rather than deciding to live with it, and
          it is a two-sentence edit. *Against:* it weakens what rule 1 was for.
          A neutral branch name still reads as a hand-up — the `report-` prefix
          carries that on its own — but the parent can no longer tell **which**
          child is reporting from the branch list alone, so a session triaging
          several hand-ups has to open each PR. It also makes branch shape
          depend on a property (the child's visibility) that the parent cannot
          see from its own tree.
    - [ ] **(b) Make rule 2 explicitly govern branch names, PR titles and commit
          subjects as well as item bodies, and say rule 1 yields to it.** *For:*
          it fixes the class rather than one instance — the same collision
          exists for PR titles and commit first lines, and (a) leaves both
          open. It also gives every future rule about naming a stated
          precedence to inherit. *Against:* it is the largest edit, and it makes
          rule 1's own worked example wrong as written, so § *The instance*
          needs revising alongside it or the section contradicts itself in a
          second place.
    - [ ] **(c) Accept the exposure deliberately, scoping rule 2 to item
          CONTENT** and stating that refs and PR metadata are out of its reach.
          *For:* this is a real position, not a cop-out — a repo *name* is
          weaker reconnaissance than its hosts, clients or secrets, all of which
          rule 2 would still protect; it keeps rule 1's triage value intact; and
          it costs nothing to implement because it describes what is already
          happening. *Against:* it is a widening of what the estate discloses,
          and the estate's own standing convention cuts the other way — the
          child doctrine block already refuses to name the private estate-root
          repo *"by name"* on the ground that a public repo naming it is
          reconnaissance. Choosing (c) means saying out loud that a child repo's
          name is not in that category.
    - [ ] 🔑 **The reporting session's recommendation, offered as reasoning and
          not as a ruling: (b), with (a) as its concrete consequence.** (a) alone
          leaves PR titles and commit subjects leaking the same name through the
          same mechanism, so it fixes one of three surfaces and reads as fixed.
          (c) is defensible but should not be arrived at by default — and it is
          the option that is hardest to reverse, because the names already
          pushed cannot be unpublished by a later rule. (b) is the only shape
          that states a precedence, which is what was actually missing: the two
          rules are each reasonable and the defect is that nothing says which
          wins. Whichever is chosen, the decision belongs on the record, because
          the present state is an unrecorded accident either way.
  - [ ] 🚩 **A ruling for (a) or (b) has a second half the fix must not skip.**
        Renaming a branch does not retract a name already advertised — the refs
        above are public and their history is public. Deleting them removes the
        live advertisement only; anything that mirrored or cached the repo keeps
        it. So the remediation question *"do we retire the exposed refs, and does
        that buy anything"* is the principal's, and it is separate from the
        doctrine edit.
  - [ ] 📄 **This item's own compliance, recorded because it is the test of
        whether the fix is even possible.** The body above obeys rule 2 — the
        reporting child is described only as *"a private child repo"*, and no
        host, client, filename or secret of its appears. That was achievable
        with no loss of meaning: nothing in the finding depends on which child
        filed it. **The branch was deliberately named against rule 1**, in the
        neutral `report-<subject>-<HHMM>` shape option (a) sketches, with no repo
        token, and the commit subject and PR body are written the same way. That
        deviation is disclosed rather than quiet, it is the only way to file this
        finding without committing the defect while reporting it, and it is
        offered as the worked demonstration that (a)'s shape is usable. The
        branch name is new and has never existed in this repo before
        (§ *Report without harming the parent*: *"never re-use or re-create a
        branch name"*).
