# Held back — the empty term list, the credential carve-out, publishscan, the hand-up route

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer, session `9bb1b984`, which did not author the delta.

## The pointer's own questions

1. Can refusing an empty term list strand a child?
2. Does the secret carve-out close every credential shape?

## The brief-writer's questions

3. Who is on the hook plane with a comments-only list: a fresh clone, a new machine, a child that
   ships a stub file? Is exit 2 a blocked commit with a remedy they can act on, or a stranding? What
   does the same list do under `floor.py --plane hook` end to end?
4. "CI passes no `--require-terms`, so no child's CI changes": is that a fact about every child's
   `floor.yml` caller, or only the reusable workflow's default?
5. The carve-out turns on "a line that names a credential key". Build the shapes: YAML with the key
   on the line above, JSON, `Authorization:`, `client_secret`, `passwd`, a key with a suffix or
   prefix, an array, a heredoc. Then the reverse: a legitimate `ssh_key_fingerprint: SHA256:…` or a
   `known_hosts` line. Does the restored block now fire on the use E3 was built to exempt?
6. A secretscan suppression is now printed as `path:line`. Does any printed line carry the
   suppressed value, in a public CI log?
7. Publishscan's first ten hidden paths print on every run and `--json` carries them all, in public
   CI logs. What does a path disclose in a repo whose ignore file exists because the path is
   sensitive?
8. "Case folded": `.casefold()` or `.lower()`? Non-ASCII (`ß`, dotted `İ`). On a case-sensitive
   filesystem can two tracked paths differ only by case, one allowed? `.*_history` and `._*` moving
   to basename-only: what did the old match reach that the new one does not?
9. `--end-of-options` in `signscan`: which git version introduced it, and which git runs on each
   plane?
10. Does the `REVIEW.md` rule 3 sentence (an ask names any prior answer) reach its mirrors: the
    skill's rule, `docs/build/templates/docs/reviews/README.md`, the queue-run prompt?
11. Hand-up check: "a `report-` head with no repo token unless that repo is public". How does a
    session know what a repo token is, in a repo it has never heard of? "Files that are the item and
    the index only": does that refuse a filing that adds a new section?
12. The read-order step adds `gh pr list` to every atelier session open. What happens with no `gh`,
    with `gh` unauthenticated, or under a cold reviewer, and is a PR title then part of the
    reviewer's pre-brief exposure?
13. "The duty is the principal's repos": is a fork of a public child inside or outside it? The
    private-first path for a vulnerability: where does the public item land if the fix is never
    made?

## Facts held back

- **Re-run lines, 2026-11-09 UTC, machine load about 9 at the start, run from the worktree root
  (the `cd tools` line from `tools/`).** `python3` was 3.14.6. Every `--selftest` named in the
  brief exit 0; the combined unittest line, 1,086 tests, exit 0; `floor.py --plane ci --root .` exit 0,
  with `pathscan` warn-only findings; the full `unittest discover -s tools` under `nice`: 2,718 tests
  in about 647 s, OK, exit 0.
- **Interpreter:** under `/usr/bin/python3` (3.9.6) `test_floor` and `test_floorfleet` exit 1 with
  `TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'`. The brief-writer did not
  trace the source. CI pins 3.12.
- **The prior-pass result by item, read from the board** (why these four and not the other nine):
  `160/090` FAIL with 2 MAJOR and a stated stay-open; `160/470` 1 MAJOR; `160/300` 1 MAJOR;
  `160/100` 0 MAJOR. The other nine each 0 MAJOR, several marked closed on that pass.
