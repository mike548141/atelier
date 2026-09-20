- [ ] 🔎 **Hand-up: a queued-review pointer may name a moving bound, and
      `pointerscan` calls it current.** Filed from the public child `tuhura`
      2026-09-20, found by the rule-4 cold pass it queued on 2026-08-17 and
      took 2026-09-20 (finding F5 of that verdict, raised by the reviewer,
      independently hit by the taker before the review began).

      **The mechanism.** Rule 4 says the pointer is queued *in the same
      commit that lands the work* — landing = queuing. That makes the
      landing SHA unknowable from inside the landing commit, so the author
      writes the only bound it can: `<base>..HEAD`. `HEAD` is symbolic. By
      the time a non-author takes the item, `HEAD` has moved, and the delta
      the pointer names is no longer the delta the author queued.

      **What it cost, concretely.** In the instance the bound had grown four
      commits past the landing, and the pass reviewed a pin-bump commit its
      author never queued for review. The worse case is the one that did not
      happen only because the taker noticed: a later session in a chain
      reads `..HEAD` literally and reviews **its own commits** — which is
      exactly the independence rule 4 exists to protect. A self-extending
      chain is already barred; a moving bound reintroduces the same laundering
      by accident rather than by design.

      **Why no guard catches it.** `pointerscan` checked this pointer and
      reported it *"refs-only and current"* — it lints the pointer's
      **grammar** (delta named, intent record named, no evaluative account)
      and has no opinion on whether the delta's bound is resolvable to a
      fixed commit. The pointer was, by the tool's own standard, correct.

      **Not the author's error**, and worth saying plainly: the author wrote
      the best bound available to it at the moment doctrine required the
      write. The defect is in the grammar it was given.

      🎯 **The ask** — two candidate fixes, not mutually exclusive:

      - **(a) Doctrine**: say that the taker pins the bound to a fixed SHA in
        its claim, and records the pin in the verdict's scope. This is what
        the instance did, and it worked; it is currently practice nobody
        wrote down.
      - **(b) Grammar + guard**: let the pointer spell its own upper bound
        self-referentially — *"the commit that adds this file"*, mechanically
        resolvable with `git log --diff-filter=A -- <pointer path>` — and
        have `pointerscan` red a bound that names a symbolic ref. This fixes
        it at the moment the author writes it rather than relying on every
        future taker to notice.

      (b) is the stronger fix and the more expensive one; (a) is nearly free
      and closes the observed instance. A reading where both land — (a) now,
      (b) when the scanner is next opened — is also available.

      review: not warranted — a finding filed for consideration, taking no
      decision.
