- [ ] **Hand-up from a private child: `secretscan` calls a marker "naming no
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
