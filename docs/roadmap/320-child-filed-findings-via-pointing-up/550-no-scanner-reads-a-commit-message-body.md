- [ ] 🔎 **Hand-up: no floor scanner reads a commit message, so a term that is
      caught in files lands unflagged in a message body** `[M][tools]` — filed
      2026-10-11 from a private child repo via `PROPAGATION.md` § *Pointing
      up*. Class only: no repo, term, person or hash appears below. Checked
      first: `tools/*.py` and `tools/README.md` at this HEAD, and the board,
      for any scan of commit messages. `datescan`, `pathscan` and `wrapscan`
      each state that commit messages are out of scope;
      `publishscan --history` reads paths added in history, not message
      text. No `--messages` mode exists. The related plural/possessive gap the same finding turned up is already fixed
      (`320/240`) and is not refiled.

  - [ ] 🔑 **The class.** The leak, secret and publish scanners all read
        trees: staged lines in the hook, the whole tree in CI. A commit
        message is not in the tree. A private repo that is later made public
        publishes every message verbatim, so the gate that is supposed to
        stop a name, address or credential reaching public view has never
        looked at a surface that publishes in full on the day of the flip.
        The finding is not that a message slipped past a check; it is that
        there is no check.

  - [ ] 📊 **Measured in the child.** A sweep of its history across all refs
        found one commit body naming a person that the term list is meant to
        catch. A later re-sweep found four. All of the later hits
        were added after the first sweep, with the tree scanners enforced and
        passing the whole time. Subjects were clean in both sweeps; the
        content was in bodies, which are where a why-dense message puts the
        narrative and so where an identifying detail is most likely to land.

  - [ ] 🎯 **Proposal.** A `--messages` mode over `git log` for the same rule
        sets (local terms, structural shapes, secret shapes), runnable:
        (a) at the pre-flip gate over all pushed refs, where it is the
        difference between knowing the size of the rewrite and finding out
        after; and (b) in the commit-msg hook plane for the message being
        written, so a new hit cannot be added while the older ones are
        waiting for a history rewrite. Branch names and pull-request titles
        and bodies are the same surface class and could share the mode.

  - [ ] ⚠️ **Cost note for the house to weigh.** A hit in an existing message
        cannot be fixed without a history rewrite, so the value of (b) is
        stopping the count growing, and the value of (a) is sizing the job
        before a flip. Evidence is the child's own sweep, not re-run here:
        **unevidenced at atelier's end**.
      🔎 **Verified at HEAD 2026-10-16** (1501 UTC queue run, a read-only
        Sonnet worker): CONFIRMED. datescan, wrapscan and pathscan docstrings
        exclude commit messages; publishscan --history reads paths only; no
        commit-msg hook ships. Repro: a commit body with an IPv6 address and a
        relative-time word exits 0; the same address in a staged file exits 1.
        320/240 exists. Sweep counts are child-side.
  - [x] ✅ **Part (a) BUILT 2026-11-10: `leakscan --messages [REVS]`**, read-only over
        `git log` (every ref by default), whole bodies, the same rule sets as a
        file, exit 0 whatever it finds and 2 if the log cannot be read. It is
        the pre-flip sizing tool the proposal asks for. A marker in a message
        exempts nothing, and authorship trailers are skipped (published identity,
        and 2,198 of the first run's 2,200 hits). Measured over atelier's 2,302
        messages: 4 hits in 3 messages (3 structural, 1 term), which answers
        "unevidenced at atelier's end" above. Listing them is one command; they
        are the principal's to weigh, since a hit in an existing message cannot
        be fixed without a history rewrite.
  - [ ] **Part (b) is NOT built, so this item stays open.** The commit-msg plane
        exists now (`320/810`), and the wiring is one registry line, but
        `leakscan` has no advisory form by design and blocks on a hit, so
        putting it on that plane is a blocking check over every message body
        from day one, with no warn-first period and no measure of the fleet
        behind it. `namescan` covers titles and branch names on that plane
        (`160/360` NP2); bodies are read only by the sweep above. Pull-request
        titles and bodies are not read by anything yet.
