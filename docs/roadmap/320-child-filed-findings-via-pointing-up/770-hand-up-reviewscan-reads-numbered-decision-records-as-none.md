- [ ] 🔎 **Hand-up: `reviewscan` does not see decision records named by
      number, and reports "clean" over a repo full of them** `[tool]`.
      Handed up from a private child on 2026-11-02 under `PROPAGATION.md`
      § *Pointing up*, found by a brief-writing run (Opus 5.5, no reviewer)
      and reproduced before filing with this repo's `tools/reviewscan.py`
      at `6a16918`. Stated class-only. Consideration and remediation are
      atelier's; the filer stops here.
      **The gap.** `RECORD_NAME` (`tools/reviewscan.py` line 108) matches only
      `YYYY-MM-DD[-HHMM]-slug.md`. A child that names its ADRs `NNNN-slug.md`
      (a convention this repo's own `docs/decisions/0008-…` also uses) has
      every record skipped, and the scan prints a pass rather than "not in
      scope". The rule it enforces (`REVIEW.md`: each design record carries a
      review line; *"Omission is the bug"*) then goes unchecked there, and the
      green line reads as compliance.
      **Measured:** on one public child, 167 records named `NNNN-slug.md`, 0
      dated; `reviewscan.py --root <child>` printed *"✓ reviewscan clean — 0
      post-2026-07-21 decision record(s) carry a review line"*. The run that
      found it counted eleven records there from the last 30 days with no
      review line.
      **Why the name is load-bearing:** the post-2026-07-21 date gate is read
      from the filename, so a numbered record has no date to gate on. The
      options, all atelier's to choose: read the date from the record's body
      or its first commit; treat a numbered record as in scope from the
      child's adoption pin; or make a zero-record match print "not in scope"
      instead of "clean", so the gap at least shows.
      - **2026-11-10, minimum fix landed** (the third option): `reviewscan`
        now prints "not in scope" instead of "clean" when no dated record
        matched, and counts the `NNNN-slug.md` records it did not read (also
        in `--json` as `unread_numbered_records`). Exit status unchanged;
        tests in `tools/test_reviewscan.py`. Reproduced first on a fixture with
        two numbered records: it printed "clean" over both.
      - **Left open:** reading a numbered record's date from its body or first
        commit, or treating numbered records as in scope from an adoption pin,
        so the review-line rule is actually checked there. That is a policy
        choice about the rule's reach, not done here; until it is made the
        gap shows but is not closed.
