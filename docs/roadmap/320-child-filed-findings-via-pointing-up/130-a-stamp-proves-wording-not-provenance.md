- [ ] 🔎 **A stamp proves the wording; it does not tell a reader which half of a
      block is inherited — and position, which would, is doctrine only as an
      aside** — filed from `cbom` 2026-08-24 via § *Pointing up*, over the
      channel, as the residue of `320/120`. Its words: *"stampscan diffs
      wording; it does not tell a READER which half of a block is inherited."*
  - [ ] **Where it comes from.** In `320/120` a child session found a house rule
        (BS1) in its **own inlined floor block**, reasonably read it as a local
        addition, and reported it upward as such. The reply corrected it; the
        child then asked the better question — *what would have prevented the
        misreading?* — and answered that a stamp would not have.
  - [ ] ✅ **Verified here, against the tools and the doc rather than the
        report.**
    - [ ] `tools/stampscan.py` checks the text **between** a `stamp:begin` /
          `stamp:end` pair against its canonical region. It is a *wording*
          check. It says nothing about a block carrying **no markers at all**
          (the case that produced this), and nothing about what sits around the
          region — so it cannot answer "is this bullet the house's or mine?"
          for any reader, which is not a defect in the tool but a limit of what
          stamping is for.
    - [ ] **The house does have a position rule, and it is an aside.**
          § *The standard child doctrine block* ends: *"Everything below the
          block is repo-specific onramp."* One sentence, at the tail of a long
          paragraph about block length, phrased as scope for the onramp rather
          than as the invariant that makes **position** answer provenance.
    - [ ] **And nothing joins it to the rule that produces the collision.**
          § *Who is a child* makes **Add** free and *"actively wanted"* — a
          child adding a guardrail its parent lacks is the mechanism working —
          and never says where the addition goes. A child that adds a bullet
          *inside* its floor block is exercising a permitted verb in the one
          place that destroys the reader's ability to tell inherited from local.
  - [ ] 🔑 **So the claim stands, and sharper than filed: stamping buys
        wording-equality, not provenance-legibility.** The two are different
        properties and only the first has a mechanism. Position would give the
        second for free — canonical region verbatim, local additions strictly
        below it — because then a reader answers the question by *looking*,
        with no tool, no pin resolution and no parent checkout.
  - [ ] 🎯 **Mike's to rule; the shapes, cheapest first.** (a) Promote the
        position sentence from an aside to a stated invariant, and point
        § *Who is a child*'s **Add** verb at it — prose only, reaches every
        child at its next pin bump. (b) Additionally make the boundary
        machine-visible, since an unmarked block is exactly the case stampscan
        cannot see. (c) Do nothing and rely on the pointer — the honest null
        option, and its cost is this item's own instance: a session read a
        stamped copy as the source and manufactured a finding, which is
        § *Pointing up*'s second-order hazard doing it a second time.
  - [ ] 📎 **Taken on the child's report and NOT verified here** (its tree is
        its own — `CONCURRENCY.md` § *Stay in your lane*): that its block cites
        `GUARDS.md` twice where the canonical region cites it none, that the
        divergence set is three and was **already ruled** in that repo on
        2026-08-18, and that it has now recorded the measurement against its own
        item. Its disclosure that it put a settled ruling back in front of the
        principal is its record's to carry, not this board's — noted here only
        because it is why the observation arrived as new.
  - [ ] 🔥 **And it is worse than "cannot see": on an unstamped block the tool
        reports SUCCESS.** Flagged by the child 2026-08-24 from its own tree,
        then **reproduced here** rather than taken on its account — fixture
        built from atelier's own `docs/build/templates/CLAUDE.md` with the two
        marker lines stripped, nothing else changed:

        ```
        $ stampscan.py --root <fixture> CLAUDE.md
        ✓ stampscan clean — no stamped blocks found.
        EXIT=0
        ```

        Eleven bullets of safety floor, never compared to canonical, and a
        green tick. **The string is honest and the exit code is not** — which
        is [`020/040`](../020-policy-as-code-programme-five-tracks-mik/040-a-scanner-s-verdict-has-two-states-and-needs-t.md)
        (a verdict with two states needing three) and
        [`115/130`](../115-guardrail-architecture-mike-commissioned/130-a-guard-reports-whether-its-rule-fired-at-all.md)
        (a guard reporting whether its rule fired) meeting in one tool, so the
        class is filed and this is a new **instance** rather than a new class.
    - [ ] 🔑 **The house has already solved this exact shape once**, which makes
          the remedy a copy rather than a design: `leakscan --require-terms`
          exists precisely so a degraded run cannot pass silently, and its own
          help text carries the reasoning — *"to automation, a degraded exit-0
          pass is indistinguishable"* (review B5). `stampscan` has **no
          equivalent switch**: its flags are `--warn`, `--json`, `--selftest`,
          `--root`. So the null option (c) above is not "nothing changes" — it
          is "the guard keeps returning green over an unchecked floor, and the
          repo it happens in has no way to tell".
    - [ ] ⚖️ **The blast radius today is smaller than it looks, and that is
          exactly why the sequencing matters.** `stampscan` is deliberately
          **not** in `floor.py`'s registry, not in the reusable `floor.yml`, and
          not in the pre-commit hook — verified by `floor --list`; it runs as a
          hand step in atelier's own `ci.yml` only, barred from wider wiring
          while ST3 is open
          ([`020/110`](../020-policy-as-code-programme-five-tracks-mik/110-d2-residue-stampscan-registry-wiring-stays-bar.md)).
          So today this is a **hand-run** hazard, and the child met it by hand.
          🚩 **It becomes a fleet hazard at the moment that bar lifts**: wiring
          the scanner to children without a cover switch ships green-over-
          nothing to every child whose block is unstamped, on the plane nobody
          reads because it is green. **So the cover gap is a precondition on
          `020/110`, not a parallel nicety** — that ordering is the finding
          this round adds, and it is cheap to honour only while the wiring is
          still barred.
    - [ ] 📄 **Provenance and division of labour.** The child flagged rather
          than filed, on the grounds that `320/130` was open and consideration
          is atelier's — the duty's own split, honoured without being asked. It
          also corrected its own item's wording of this finding, having first
          written the weaker *"a stamp diffs wording"*. Everything inside its
          tree stays its record's, unverified here; what is written above was
          re-derived in atelier against atelier's artefacts.
