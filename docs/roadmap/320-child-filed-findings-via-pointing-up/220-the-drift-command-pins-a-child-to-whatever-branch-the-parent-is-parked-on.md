- [ ] 🔎 **The canonical floor block's drift command reads `..HEAD`, so a
      child pins itself to whatever branch the parent's checkout happens to be
      parked on — and § *Pointing up* has made "parked on a filing branch" a
      NORMAL state for this repo.** Filed from a private child 2026-09-08 via
      § *Pointing up*, by direct write into the parent's tree (the first
      filing shape), PR opened before stopping. The child is not named; per
      § *The route* rule 2 that omission is deliberate. **The branch name here
      carries no repo token either** — see the note at the end, which is the
      only reason this item touches `320/190` at all.
  - [ ] **The text, quoted from `docs/method/PROPAGATION.md`'s canonical
        floor block** (the `<!-- floor:begin -->` region every child inlines):
        *"canonical doctrine is `<atelier-path>/docs/method/`. At session
        start run `git -C "<atelier-path>" log --oneline <SHA>..HEAD`; any
        output means the house doctrine moved — read it, then bump the pin
        above deliberately."*
  - [ ] 🔑 **Why `..HEAD` is the wrong ref, and why it got worse recently.**
        `HEAD` in a sibling checkout is not the parent's mainline — it is
        whatever branch that working tree was last left on. A child session
        running the command verbatim gets a diff against that branch, reads
        the delta, and **bumps its pin to a commit that may exist only on an
        unmerged branch**. Nothing in the block says `origin/main`, and
        nothing in the child's own onramp would catch it: the SHA resolves,
        the diff is real, and the drift check goes quiet next session because
        the ref is genuinely an ancestor of that branch's tip.
        **The exposure is new.** Before § *Pointing up*, a parent checkout sat
        on `main` most of the time and `..HEAD` was right by accident. The
        route this doctrine created makes filing branches routine — the
        section this item sits in is the evidence — so the accident no longer
        holds, and the idiom now misfires in exactly the repo state the
        doctrine encourages.
  - [ ] ✅ **Verified by walking into it, not by reading the text.** A child's
        pin bump today was written from `HEAD` and named a commit **one ahead
        of `origin/main`**, on an unmerged filing branch. Measured
        afterwards: `git branch -r --contains <sha>` returned only that
        branch, and `git merge-base --is-ancestor origin/main <sha>` confirmed
        it was ahead. The child corrected its pin to the mainline SHA and
        changed its own copy of the command to `..origin/main`.
        ⚖️ **The damage was nil, and that is itself the finding's sharpest
        edge:** `docs/method/` and `tools/` were **byte-identical** between
        the two commits, so every doctrine claim the child had just inlined
        stood unchanged. The failure was silent and would have stayed silent.
        A child that had inlined a bullet which existed only on an unmerged
        branch would have had no way to notice.
  - [ ] 📎 **Not verified, stated so this is not read as more than it is.**
        Whether any child is currently pinned to an unmerged tip — only the
        one instance above was checked, and it was corrected. Whether other
        children copy the block verbatim or have already localised it.
        Whether `HEAD` was deliberate (a parent that wants children reading
        unmerged work) rather than an oversight — nothing found either way,
        and the absence of a note is part of the finding.
  - [ ] 💡 **Proposed fix, offered as reasoning and not as a ruling.** Change
        the canonical block to `git -C "<atelier-path>" log --oneline
        <SHA>..origin/main`, and say inline why — a child pins to the
        parent's *published* mainline, never to a working tree's current
        branch. It is a one-token change to the region, and `stampscan` would
        carry it to any child that has stamped its copy. Two alternatives
        rejected here and named so the choice is visible: telling children to
        `git -C <path> checkout main` first (touches a working tree the child
        does not own — worse than the bug), and leaving `..HEAD` with a
        warning (the failure is silent, so a warning that must be remembered
        at exactly the wrong moment is not a guard).
  - [ ] 🔗 **A corroboration for `320/190`, recorded here rather than by
        editing that item** (§ *Report without harming the parent*: touch only
        your own item). `190` states as explicitly unverified whether the
        child named in the two already-pushed refs is in fact private. It is:
        `gh repo view <that child> --json visibility` returns `PRIVATE`,
        checked directly today. The name is not reproduced here. So `190`'s
        core claim is now corroborated rather than assumed, and its severity
        is real: a private repository's name is readable, unauthenticated, on
        a public remote.
        ✅ **And a data point for `190`'s own open question:** this repo's
        three most recent hand-up branches already use a **neutral** `report/`
        prefix with no repo token, while the two exposing refs use the
        `report-<repo>-` form rule 1 prescribes. Practice has already drifted
        toward `190`'s option (a). The filing child adopted the neutral form
        for THIS branch too — a deviation from rule 1, declared here rather
        than taken silently, and it is the reason this item can quote `190`
        at all without repeating the disclosure.
      *review: not warranted for the finding — it is a measurement of a
      documented command against an observed repo state. The fix to the
      canonical region is a doctrine edit and earns whatever review this
      repo's own process gives that.*
