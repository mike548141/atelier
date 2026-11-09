# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-g3-who-when-gate-order-cold.md` (`REVIEW.md` rule 1).
Written 2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta.
Open this only after act 1 is committed. Everything here is a floor, never a fence, and none of it
is a finding.

## The queue pointer's questions (author-written, verbatim)

> whether the who/when parse can be satisfied by a line that records nothing true; whether
gate-before-ignore reaches every binary a child tracks; whether an old line can still pass silently.

## The brief-writer's own questions

1. `by=principal-ruled` is free text any agent can type. Is the field's truth checked by anything,
and does the doctrine say what it does not check?
2. Provenance is removed before the reason is judged. Can a line carry provenance and an empty or
generic reason?
3. A reason sentence that happens to contain `by=`: `re.search(r"\bby=", text)` makes it "incomplete
who/when", a config error on a line that loaded yesterday. Check against the "never blocks" claim.
4. The date boundary: is `today` local or UTC? New Zealand is 13 hours ahead of CI, so does the hook
go red a day before CI, or after?
5. Which binaries does "tracked binary" reach: by extension or by content? Files under skip-named
directories, Git LFS pointers, files over a size limit, a binary reached only through a scoped
`--staged`?
6. A `Raw profile type xmp` chunk is hex inside a compressed chunk: is decompression bounded, and
what does a hostile one cost before the UNREADABLE verdict?
7. `_staged_manifest` when the manifest is unmerged, deleted in the index, or differs from the
working copy.
8. `floor.py`'s forbidden flags and abbreviations: the prefix test's direction, and a flag in
`key=value` form.
9. The tests' Python floor (3.11) is named by this delta, while the immediately preceding one says
the suite no longer needs it. Which is true?

## What the brief-writer ran, and what it got

- `wm_tests`: python3 3.14: test_leakscan and test_floor inside the 1019-test run (OK, exit 0);
  test_allowmarker separately, 55 OK, exit 0. Under /usr/bin/python3 3.9 test_floor fails at import
  (`str | None`).
- `p1080`: --binary-entries: exit 0, prints the entry with by=agent, the session id and on=. No
  manifest: exit 0, binary-unlisted warning until 2026-11-18. Reason-only line: exit 0 with
  binary-no-provenance warning naming line 1. Full provenance: exit 0, no warning. by=nobody: exit
  2, config problem. Glob only: exit 0, binary-unlisted warning, so the gate ran before the glob.
- `floor`: at c132cc1c: hook exit 0, ci exit 0. pathscan reports 3 findings, warn-only:
  docs/method/EVIDENCE.md:427, docs/method/session-open/session-open-prompt.md:13 and
  docs/method/session-open/template-history.md:10 (paths that do not exist from the repo root).
