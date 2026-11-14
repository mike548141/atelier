# Held back — a floor `disabled` entry takes an end date, and reviewscan's not-in-scope line

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer (`cclive` lists it as session `48ef9c3e`), which did not
author the delta. Nothing here is a finding: these are questions, and facts read off the machine.

## The pointer's own questions

1. Can the new shape lower a check silently?
2. Can a zero-record scan still read as a pass anywhere it is displayed?

## The brief-writer's questions

3. The zero-record line begins with the same ✓ glyph as the clean line, and the exit is 0 (fact
   5). Where the floor, CI or `floorfleet` shows reviewscan by exit status, does a not-in-scope run
   still render as a pass? Is the wording change visible anywhere but reviewscan's own output?
4. A repo with one dated record and many numbered ones prints "clean", and the human line does not
   mention the numbered records it skipped; only `--json` carries the count (fact 4). Is the gap
   `320/770` names closed for a repo that mixes the two schemes, or only for a repo with none
   dated?
5. `count_unread_numbered` looks only in `docs/decisions/` directories. A repo that keeps numbered
   records elsewhere gets "not in scope" with no count. Does the line then claim more than it
   knows?
6. `count_unread_numbered` walks `rglob("docs/decisions")` under each path. In a repo with nested
   worktrees or vendored trees under it, does it count other checkouts' records, follow symlinks,
   or cost a full tree walk on every run?
7. `review-by: ""` and `review-by: 0` load as undated, not refused (fact 3), while the docstring
   says a date that is present must be a real one. Is a falsy non-date "present"? Does the same
   hold for `advisory`, whose spelling this claims to share?
8. `floorfleet._disabled` drops a malformed date and shows the entry as 🟡 "no end date", while
   `floor.py` refuses the same config outright. Does the fleet board then describe a repo whose
   floor cannot load as merely undated?
9. Nothing caps how far ahead `review-by` may be set. Is a `disabled` entry dated decades ahead an
   expiring lowering under the principal's pick, *"Allow if declared + expiring"*? Does `advisory`
   have a cap this shape should have copied?
10. The local fleet holds three `disabled` entries, all undated, all the same check (fact 7). Is
    "warn-first so no repo goes red" grounded in a measured cost, and does anything carry the owed
    block to a date?
11. The pick in `020/170` line 121 is an answer, but `320/800` calls it "the rule" and the
    `GUARDS.md` heading reads "Ruled 2026-11-09" (fact 10). Does the delta's prose carry a pick as
    a ruling, against `COMMUNICATION.md`'s answer/ruling marks? (The heading may predate the
    delta; say which.)
12. `test_report.py`'s reviewscan pin was changed to feed one record, so the pin no longer covers
    the zero-record output. Does any test pin the not-in-scope line's exact text, as the clean line
    is pinned?

## Facts read off the machine (2026-11-14 UTC, worktree at `58f612b7`)

1. Re-run lines, all exit 0: `test_reviewscan` 70 tests OK; `test_floorfleet` 127 OK; `test_report`
   110 OK; `test_floor` 255 OK (about 209 s); `reviewscan --selftest`; `floorfleet --selftest`;
   `coldsweep --commit 06248fba`; `merge-base --is-ancestor 06248fba HEAD`. Python 3.14.6.
2. A `disabled` object with no `why`, a blank `why`, or `{}` is refused by `Config` load:
   "disabling 'spellscan' needs a stated reason". A blank string is refused the same way.
3. `{"why": "x", "review-by": ""}` and `{"why": "x", "review-by": 0}` both load, with no entry in
   `disabled_review_by`, so both read as undated.
4. reviewscan on a fixture with one dated record (with a review line) and two `NNNN-slug.md`
   records: exit 0, head line "✓ reviewscan clean — 1 post-2026-07-21 decision record(s) carry a
   review line; …", no mention of the two numbered records.
5. reviewscan on a fixture with only two numbered records: exit 0, "✓ reviewscan not in scope for
   decision records — 0 post-2026-07-21 dated record(s) matched (2 numbered NNNN-slug record(s) not
   read: they carry no date to gate on); nothing was checked for a review line. …"
6. reviewscan on a fixture with only one pre-boundary dated record: exit 0, the not-in-scope line
   with no count.
7. `floorfleet.py` (local, no `--remote`): exit 0; three `disabled` lines, all 🟡 "no end date",
   all `licenscan`; none dated, none expired. (Repo names withheld: this file is public.)
8. atelier's own `.atelier-floor.json` has no `disabled` key.
9. `reviewscan --root . .` on atelier: exit 0, "clean — 8 post-2026-07-21 decision record(s) …;
   234 review brief(s) …". atelier also holds `NNNN-slug.md` records (for example
   `docs/decisions/0008-enforcement-is-called-not-copied.md`), not counted on that line.
10. `020/170` lines 120–121 mark the principal's 2026-11-09 word with 💬 as an answer to options a
    queue run offered, "an answer, not a ruling", and quote the pick. `GUARDS.md` line 489:
    "### Ruled 2026-11-09: a repo may lower a check's response, declared and expiring".
11. `floor.py --json` serialises each result by `__dict__`, so `undated`, `review_by`, `expired`
    and `days_over` appear on every result, disabled or not.

The probe script is not in the tree; each fact above is reproducible from the brief's re-run lines
or a fixture of a few lines.
