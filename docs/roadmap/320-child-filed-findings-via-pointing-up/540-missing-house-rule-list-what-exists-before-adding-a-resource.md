- [ ] 🔎 **MISSING HOUSE RULE — list what already exists before adding a
      resource to an estate, and read the neighbouring file before inventing a
      pattern** `[S][doctrine]` — hand-up from a private child repo, filed
      2026-10-11 via `PROPAGATION.md` § *Pointing up*. Class only: no repo,
      host, product or person appears below. Checked first: a search of
      `docs/method/` for list-before-create, inventory-first and check-what-
      exists wording found no rule that says this.

  - [ ] 🔑 **The class.** A container-orchestration tool reported that a
        network the stack declared as external could not be found. The
        shortest edit that clears that message is to declare a new network,
        so a session wrote two. The estate already had the networks the stack
        needed, and a sibling file in the same directory, for the same stack,
        was already attached to them. The answer was one file over and nobody
        looked; nobody ran the one-line command that lists existing networks.
        **An error message says what the tool wants, never what the estate
        already has.**

  - [ ] 🔑 **It was not cosmetic.** A network created with no explicit
        addressing was auto-allocated an address family the deploy engine
        could not parse. That exact class had been fixed earlier in the
        estate, with a written warning that any network created afterwards
        would bring it back. The shortcut re-broke a solved problem and
        blocked every deploy of the stack until it was traced.

  - [ ] 🎯 **Proposed rule (for the house to word and place).** Before
        adding a resource of any kind (network, volume, secret, dataset,
        directory, queue, DNS record), list the ones that exist; the command
        is one line and takes seconds. Before inventing a pattern, read the
        file beside the one being edited, because a stack with five working
        members already answers most questions about the sixth. This is the
        existing "verify before acting" posture applied at the moment an
        error tempts the fastest edit: the failure was not ignorance of the
        rule but reaching for the edit that silenced the message.

  - [ ] 💡 **Possible mechanical half, offered not decided.** A declarative-config
        lint cannot know the estate, so this is probably doctrine only. But
        a child that keeps one canonical file declaring its shared resources
        can have a check that flags any *new* resource declaration outside
        it. That is the child's to build; the house's part is the rule.
        Evidence is the child's own account, not re-measured here:
        **unevidenced at atelier's end**.
