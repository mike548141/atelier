- [ ] **Give every guard a second dial — the standing consequence of Mike's
      2026-07-28 correction, carried across the whole fleet.** The
      scanner-precision track was opened on the premise that a false positive on
      a correct line trains someone to write an allow-marker, and that is how a
      scanner's output stops being read. Mike corrected the premise itself:
      *"it assumed one dial. Precision is only forced to trade against coverage
      while a scanner's sole response is block."* That correction has been
      applied to the credential scanner's tier and nowhere else systematically.
      **Why it is the cheapest real win available.** The case-file's worst
      outcome is not noise, it is silent coverage loss: with block as the only
      response, the only way to stop crying wolf is to shrink detection. The
      credential scanner did exactly that, and the record names the failure shape
      — *a coverage narrowing settled at tool altitude*, recorded in a code
      comment where it never reached the principal. Every guard still holding a
      single dial can reach the same outcome the same way, and nothing on the
      board would show it.
      **How it composes with the evidence-window rule above.** The window
      predicate explains why the false positives exist; the one-dial defect
      explains why they turn into damage rather than friction. Both are needed:
      widening a window without a second dial still forces the trade, and adding
      a tier to a guard that cannot see its licensing context still fires
      constantly, just more quietly.
      **Not started here.** Scoped as an audit first — which registry entries
      have a response tier separate from detection, and which conflate them —
      because the estate's own rule is that recurrence earns the check, and the
      recurrence count for this class has never been taken.

      🔎 **The audit, run 2026-10-16** (a read-only Sonnet pass over the
      code and the README. The orchestrator re-checked its four sharpest
      citations against the code before recording it). A guard has a
      *second dial* when a finding's response, block or report-only, is set
      separately from detecting it. The registry's `advisory=` field is a
      different dial: it switches the whole scanner, so it was counted
      apart.
      - **Tally.** Of the 16 registered guards, **2 have two dials**
        (secretscan, whose only advisory rule is `low-variety-entropy`, and
        sizescan). **13 have one.** `board` is N/A: it checks exact
        equality, so there is nothing to trade. Of the 3 unregistered
        guards, blockscan has two dials, and stampscan and signscan have
        one.
      - **The recurrence count this item asked for.** 9 of the 15 one-dial
        guards carry a code comment recording coverage that was narrowed,
        or declined, to stop false positives: leakscan, linkscan,
        reviewscan, publishscan, datescan, wrapscan, spellscan, harvestscan
        and pathscan. Two of them record a principal's ruling: harvestscan's
        scope cut and wrapscan's scope. The other seven were settled at
        tool altitude, which is the shape Mike's correction named.
      - **Ranked by what is lost silently today:**
        1. **leakscan.** It has no advisory tier (`leakscan.py:346`), yet
           rules were withdrawn or narrowed for noise: the `diagnosis` key,
           ipv6 and nz-address. A child may `--disable` a whole rule class,
           and the README suggests that for networking repos. Its
           `severity` field is computed but never used for the response.
        2. **datescan.** It blocks, and its docstring names a deliberate
           silent miss: a bare "today" with no date cue now passes
           (`datescan.py:117-121`). Every `>` line is exempt.
        3. **harvestscan.** It is warn-only, and was still cut to 6 of 429
           roadmap commits in scope, because the only lever left was scope.
        4. Lower: publishscan (path classes left out rather than demoted),
           spellscan and wrapscan (excluded surfaces), licenscan (cheapest:
           the severity data already exists), linkscan and pathscan (named
           residuals).
      - **Code and text disagree in three places.** These are filed
        separately as `115/290`, not fixed here.

      🎯 **What is left is Mike's call.** Which guards get a second dial,
      and in what order, is a posture choice on blocking guards. leakscan
      is the personal-data boundary, where `SECRETS.md` § *The boundary's
      posture* says to over-flag. The audit's recommendation is leakscan
      first, then datescan. licenscan's dial comes almost free with
      `115/290`.

      ✅ **Answered 2026-10-16, at the close of the queue run: leakscan
      first.** The device question set out the audit's ranking and what
      each choice changes. It offered leakscan first, datescan first, or
      not now, and Mike picked "leakscan first", the recommended option.
      That is his *answer*, recorded as such. **The build is owed:** a
      report-only tier in leakscan for its low-confidence rules. The
      audit's candidates are `ipv4`, `nz-address`, `nz-phone`,
      `coordinates`, `nz-ird`, and the withdrawn `diagnosis` key. Those
      rules would then report rather than be disabled, and a child's
      `--disable` of a whole class should be weighed against that. It
      uses `severity`, which leakscan already computes. It is first-of-kind
      on the personal-data boundary, so it gets a design note and the
      capable tier, and its blast radius is measured across the children
      before landing. datescan and harvestscan follow.
