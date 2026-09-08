- [ ] **REPORT — `datescan` enforces the SHAPE of a date and cannot enforce its
      FRAME, so the UTC-at-rest rule is the one rule nothing checks** `[S][tools]`
      — filed from a private child, 2026-09-08, via § *Pointing up*. Evidence
      available.

      ## The seam

      `CONVENTIONS.md` declares **UTC at rest; local on presentation**, and
      `RECORD.md` names the exact failing case in as many words: *"the absolute
      date is the UTC date (ADR 2026-07-15): an NZ morning is still the previous
      UTC day, so the prose date matches the record's own UTC identifier, not
      the wall clock."*

      🔑 **The rule is clear, correct and already written. Nothing enforces it.**
      `datescan` blocks relative-time words and non-ISO shapes — both real and
      both valuable — but a **local** date written in ISO form is
      indistinguishable, by shape, from a UTC one. `2026-09-09` is a
      well-formed ISO date whether it is the right day or a day early.
      **So the floor gates the format and leaves the frame open**, and the frame
      is the half the ADR exists for.

      ## The incident (2026-09-08, a private child on a UTC+12 estate)

      A record was created by a commit whose committer timestamp is
      `2026-09-08T12:58:53Z`. The item it created states the date of its own
      filing as **2026-09-09**, twice — the local wall-clock date, 00:58 the
      next morning. Four sibling commits from the same working stretch carry
      the same one-day skew. Every one of them **passed `datescan` clean**,
      because every date in them is well-formed ISO.

      🚩 **The visible damage is chronology.** Records in that repo now claim
      dates that run a day ahead of the commits, the session logs and the
      identifiers they sit beside, so an ordering read off the prose disagrees
      with an ordering read off git. The repo's own board carries items whose
      stated filing date is later than the day the work happened.

      ⚠️ **And it is self-reinforcing.** A session reads the previous session's
      prose date, matches it, and the skew propagates. Nothing in the loop ever
      compares a written date against `date -u`.

      ## Why this is not a request to change the rule

      The reporting session's first reading was that the doctrine was
      *ambiguous* about whether "date" meant UTC or local. **That reading was
      wrong and is recorded here because it is the interesting part.**
      `RECORD.md` addresses the NZ-morning case directly. The rule is not
      unclear; it is **undiscoverable at the moment it is broken**, because the
      only mechanism that looks at dates says nothing.
      🔑 The general shape, which is this house's own: **guidance that
      constrains a value's form but not its frame leaks through the frame, and
      the leak looks like compliance the whole way.** The same sentence appears
      in `320/190` about content versus metadata. This is that lesson again on a
      different axis.

      ## A gap the ADR genuinely does not cover, raised alongside

      The estate owner, ruling on this report 2026-09-08, restated the standing
      rule and added a dimension the ADR does not address:

      > *"The accuracy of the date/timestamp recorded will vary depending on the
      > usecase of the timestamp e.g. a date range vs a date vs to the hour
      > minute second ms ns etc.. But when date/time is presented (e.g. CLI,
      > webui etc) it should be on local time so it makes sense to the user"*

      The **presentation half is already doctrine** — `CONVENTIONS.md` says
      *"local on presentation, labelled where doubtable"*. The **precision half
      is not**. The three declared shapes fix *format* per surface (machine
      timestamp, record identifier, prose stamp) and say nothing about how
      precise a value should be for its purpose: a date range, a date, an hour,
      a second, a millisecond. Recording a timestamp to nanosecond precision
      when the underlying fact is only known to the day is a false claim about
      resolution, and the house has no rule against it.

      ## Options, none chosen here

      1. **Give `datescan` a frame check where one is derivable.** In a git
         working tree it can compare a date written in a staged record against
         the committer time in UTC and flag a skew. Cheap where it applies,
         silent where it does not, and it would have caught every instance
         above.
      2. **Require prose stamps to carry the designator, not inherit it.**
         `CONVENTIONS.md` allows a bare `YYYY-MM-DD` in prose with the zone
         *"carried by the UTC-at-rest default"*. An inherited frame is exactly
         what a scanner cannot see. Requiring the label makes the frame
         checkable — at a real cost in prose weight, which is why it is an
         option and not a recommendation.
      3. **Declare precision as a fourth shape**, so a value states the
         resolution its use case supports rather than the resolution its source
         happens to print.
      4. **Accept it** — the rule stands, unenforced, and children are trusted
         to obey it. Defensible, but it should be a decision on the record
         rather than the current state of affairs by default.

      🎯 **The reporting session's recommendation is 1 and 3.** Option 1 is the
      only one that closes the loop at the moment it is broken, and it costs a
      check rather than a change to every record. Option 3 answers a real gap
      the owner named and nothing else covers. Option 2 is a genuine fix and its
      cost falls on every line of prose the house writes, which is the wrong
      trade for a frame that already has a default.

      ⚠️ **Consideration and remediation are atelier's.** The reporting repo has
      not worked around the rule and is filing its own non-compliance as a
      separate item on its own board; this report is about the mechanism, not
      about that repo's tidying.
