- [ ] 🛑 **A possessive or plural form evades a `local-term`, and `leakscan`
      then reports the file CLEAN** — filed from a private child repo
      2026-08-26 via § *Pointing up*, written directly into this tree. Class
      only: no repo, no host, no term, no filename.

  - [ ] **The shape.** `load_local_terms` compiles each literal line as a
        case-insensitive **whole-word** match, and `derived_form_regex` (the
        opt-in `forms:` prefix, G6) widens a term across separators and case —
        `jane-q-public`, `jane_q_public`, `janeQPublic`, `janeqpublic`. Neither
        path admits an **inflection**. A listed `Xxxx` therefore does not match
        `Xxxxs`, and English puts a name in exactly that form whenever it says
        the thing belongs to someone.

  - [ ] 🔎 **Reproduced before filing, and the method is the reportable half.**
        The child did **not** read its own term list and reason about it. It
        wrote a throwaway file of test strings — a listed term bare, the same
        term with a trailing `s`, two terms believed listed, and one ordinary
        English word chosen because it *contains* a listed term as a substring —
        and ran the live scanner over it. Results: the bare term flagged; the
        possessive **did not**; the substring case correctly did not flag, so
        word-boundary anchoring is working as designed and this is an
        inflection gap and not a boundary bug.
        🔑 **Testing the scanner rather than reading its config is what made the
        finding trustworthy**, and it is what would have caught it years
        earlier. Reading the list tells you which terms are in it; only running
        it tells you which strings it catches.

  - [ ] 🛑 **Why this is worse than a missing term.** A missing term is a gap
        someone can see by reading the list. This one is invisible from the
        list: the term **is** present, correctly spelled, and the operator has
        every reason to believe the name is covered. The live instance was a
        tracked config value holding the possessive form of a name whose class
        the list is explicitly maintained to catch, in a repo with a
        going-public gate in front of it — and the scanner returned a clean
        green over it. **A guard that fails open while displaying a pass is the
        one failure mode a guard must not have** (`GUARDS.md`).
        ⚠️ **And the gap survives a correct list.** The child's first instinct
        was "add the missing term"; that would not have helped, because the
        value in the file was never the bare form.

  - [ ] 🤔 **The child's proposal, offered as a proposal and not a patch.**
        Fold optional inflection into the term compilation — a trailing
        `(?:s|'s|s')?` inside the existing word-boundary anchors — so
        `Xxxx` covers `Xxxxs` and `Xxxx's`.
        ⚖️ **The trade the child cannot judge from where it sits**, stated so
        the decision is not taken by silence: this widens **every** literal term
        at once, including short or common-word terms where the plural is an
        ordinary word with no relation to the name. The doc's own reasoning for
        keeping `forms:` opt-in — *"only the operator holding the real list can
        judge that"* — applies here with equal force, so *always-on* may be the
        wrong shape and a second opt-in prefix, or making inflection part of
        `forms:`, may be the right one. That is atelier's call.
        💡 A cheaper interim that needs no code: the `regex:` prefix already
        exists, so an operator can spell the inflection by hand today. Worth
        saying in the docs even if the matcher changes, because it is the only
        answer available to a list that is already live.

  - [ ] 🔑 **The class this belongs to, which is bigger than one prefix.**
        Two independent instances in one child session, hours apart, of the same
        failure: **a search whose pattern cannot match, reporting zero, read as
        a clean result.** The other was a log search for a bracketed severity
        token in a format that never emits it. Neither tool was wrong; both
        answered exactly what was asked. 🎯 **Worth considering whether the
        estate's scanners should be able to say "this pattern matched nothing
        anywhere, are you sure it can?"** — a corpus-level self-check rather
        than a per-file verdict. Filed as an observation, not a proposal; the
        child has no view on whether it is affordable.
