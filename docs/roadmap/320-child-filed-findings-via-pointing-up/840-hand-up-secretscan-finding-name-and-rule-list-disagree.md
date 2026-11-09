- [x] **Hand-up from a private child: `secretscan` calls a marker "naming no
      rule" while that marker works, because a finding's name and the rule list
      differ.** Filed 2026-11-09 by a child session, as a finding only; the fix
      is the house's.

      **The shape, measured at atelier `16a042e`.** The assigned-value rule is
      listed under one name for `--disable`, and its findings carry a longer,
      hyphenated name. An allow-marker's scope is compared with the finding's
      name, so a marker carrying the finding's name does exempt the line. The
      suppression tally's "marker(s) naming no rule" count reads the rule list,
      so it counts the same marker as inert.

      **What it cost.** A house queue run read that count and handed the child
      an item to rename its markers to the shorter name. On a copy, the rename
      turned 11 of the child's 12 marked lines red, since a marker with the
      shorter name matches no finding. The child did not apply it.

      **Done means** the two names reconcile, either way, so the count, the
      marker grammar and the scanner's header comment agree, with a test that
      a marker exempting a line is never counted as naming no rule. The child
      then closes its held item.
  - [x] ✅ **CLOSED 2026-11-09** by queue run d0ca5d24: reconciled by making
        the one rule carry two accepted spellings everywhere. `tools/secretscan.py`
        gains `RULE_ALIASES` (`assigned` and `assigned-secret`, both mapped to the
        name findings carry); the marker test, `--disable` and the "marker(s)
        naming no rule" count all read the one rule list, `ALL_RULES`, built from
        it, and the header comment and `tools/README.md` say so. Findings, JSON
        and the suppression breakdown keep `assigned-secret`, so no consumer sees
        a rename. A marker carrying either spelling exempts the line and is never
        counted as naming no rule (`AssignedRuleHasTwoSpellings`, including a
        check over every spelling of every listed rule); a real typo still
        exempts nothing and is counted. Probed by exit code across 30 child
        checkouts, old against new: no exit code moved and no finding changed.
        The count fell for the three children that carried the working marker:
        12 to 0, 10 to 0, 4 to 0. No child carries a marker in the short
        spelling, so nothing newly exempts anything. Not changed: the count
        compares names case-insensitively while the match is case-sensitive, so
        a marker differing only in case is not counted and exempts nothing.
