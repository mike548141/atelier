# Deferred sibling — guards read git-quoted paths (160/760)

**Held under REVIEW.md rule 1's split. Open only after your phase-1 findings in
`docs/reviews/2026-10-16-1551-git-quoted-paths-cold.md` are committed.** A floor,
never a fence: these questions were seeded by a brief-writer who read the landing
diffs and commit bodies, so they carry that reading's framing. Reconcile against
them; do not let them narrow what you found.

## Intent record (not opened by the brief-writer)

- `docs/sessions/2026-10-05-1120-queue-run-closes-and-builds.md`

## Prior verdicts on the same surfaces (named, not opened)

- `docs/reviews/2026-09-25-0715-staged-plane-check-cold.md`
- `docs/reviews/2026-09-25-0715-bw-rulings-applied-cold.md`
- `docs/reviews/2026-10-03-0357-publishscan-round-2-cold.md`
- `docs/reviews/2026-10-04-2215-git-enumerated-walk-cold.md`

## The queue pointer's own lens hints

None. The pointer is refs-only, plus the orchestrator's brief-writing claim line.

## Seeded questions (the brief-writer's, from the diffs)

1. `diff_header_path`'s docstring says only git's two default-prefix spellings
   count, "so an added line that merely reads `++ …` is not taken for a header".
   An added line whose content is `++ b/x` prints as `+++ b/x` and matches the
   unquoted spelling exactly. Was that case ever tested at `4dfaf8d`, and is it
   what board item `115/280` and commit `39a74b9` later addressed?
2. The guards pin `core.quotePath=false` but not `diff.noprefix` or
   `diff.mnemonicPrefix`. Under either, no header starts `+++ b/`; does the guard
   then scan nothing and exit 0, at landing and at HEAD?
3. `unquote_c` decodes with `replace`, so a non-UTF-8 name becomes U+FFFD and no
   longer names a real file. Does the guard then fail to open it (exit 2), skip it
   silently, or report under a name nobody can find?
4. publishscan decodes its `-z` tokens through its own `_decode` (UTF-8 with
   `replace`, then control characters stripped); `report.nul_paths` uses
   `os.fsdecode`. Two readers of one format, landed three hours apart by the same
   run — is that one fact in two homes, and do they give the same name for the
   same bytes? Can stripping a control character make a name match, or stop
   matching, a never-publish pattern?
5. The commit says a trailing TAB marks "a name whose contents contain a space".
   Is that git's documented rule, or an observation from one git version (EVIDENCE
   § 15: a test written from the same belief as the code)?
6. Did the fix reach `filewalk.py` and the other tools that read `ls-files`
   without `-z`, or only the ones the triggering case named?
