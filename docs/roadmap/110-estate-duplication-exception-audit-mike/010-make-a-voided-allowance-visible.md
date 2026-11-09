- [x] **Make a voided allowance visible.** The fix above closes the known
      cause; it does not close the class. A marker that parses as nothing is
      indistinguishable from no marker, so the next parser gap will also be
      silent. Cheapest honest answer: when a line carries the marker *string*
      but no allowance is recognised, say so — a one-line "marker present but
      unparseable" note beside the finding, which is where the reader already
      is. Recurrence, not severity, earns the check (`PROPAGATION.md` rung 2);
      this is instance one, so it is queued rather than built.
      - **2026-11-09, built** (queue run d0ca5d24). `tools/allowmarker.py`: every
        reader (`scope_of`, `scopes_of`, `present`) now prints one stderr note,
        `allow-marker present but unparseable, so it allows nothing`, per
        distinct marker head per run, when a line carries the marker word
        outside a code span and no allowance is recognised. It is one change for
        the class, 15 reader call sites across the scanners, and no scanner file
        changed. The malformed-scope grace (`MALFORMED_GRACE_UNTIL`, `160/480`
        AM2 and LK1) is untouched: during the grace a broken scoped marker still
        allows and warns as malformed; the new note fires for it only after the
        date, when it allows nothing. A note only: no result or exit status
        moves. Tests: `tools/test_allowmarker.py` (`TestUnparseableNote`).
      - **Probe, old scanner against new, whole tree, one repo at a time, under
        `nice`.** leakscan and secretscan in each of 30 estate repos: exit code
        and stdout length identical in every one (the note is on stderr). After a
        tightening (the marker word must end at a colon, a space or the line's
        end, so a code string `"<name>scan:allow"` is not noted) the note fires
        in 2 repos: twice per scanner in this repo's own tooling source and once
        in one child's secretscan run, every one a mention of the marker, none a
        genuinely voided marker. So the estate holds no voided marker of this
        shape today, and the check costs a few stderr lines of mention noise.
      - **Stated limit.** The note is on stderr, not on the finding line, and it
        fires on any line a reader is asked about, finding or not, because the
        readers are not told whether the line has a finding. Printing it beside
        the finding would mean changing each scanner's render path (15 sites),
        which was not done. A prose mention of a marker outside a code span is
        noted too; that is the same residual `160/480` AM3 names.
