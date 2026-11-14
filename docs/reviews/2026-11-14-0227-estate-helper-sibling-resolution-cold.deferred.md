# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-14-0227-estate-helper-sibling-resolution-cold.md` (`REVIEW.md`
rule 1). Written 2026-11-14 UTC by the brief-writer (`cclive` lists it as session `cdb0c296`),
which authored none of the delta. Open this only after act 1 is committed. Everything here is a
floor, never a fence, and none of it is a finding: the brief-writer read the code once and probed
none of these past what is recorded below.

## The brief-writer's own questions

1. **An oracle in the repo's own hands (SB-A2).** `main_checkout` and `_View` trust whatever
   `--git-common-dir` prints. A worktree's `.git` file and its `commondir` are local files; can a
   crafted layout name a "main checkout" anywhere on disk, so that `pathscan` reports a `..`
   reference as found because a file of that name exists at an arbitrary place? Is that reachable
   from content a contributor commits, or only from local layout?
2. **Two or more climbs from the main checkout.** The single-climb rule bounds only the
   group-folder landings. The main-checkout landing joins any `rel` onto the main checkout,
   however many `..` it has. Does `../../../x` from a worktree read somewhere the physical path
   from the main checkout would also read (same answer, fine), or somewhere above the operator's
   folder that the delta's "escape" question means?
3. **`linkscan` runs `landings` on every missing target**, not only on a target that leaves the
   repo. `landings` returns nothing for an in-repo target, but builds the per-root view (two git
   runs, `rev-parse` and `config --get` when the environment variable is unset) on first use. Does
   the cost claim ("a scan with no failing `..` token never runs git") hold for `linkscan`, or only
   for `pathscan`, whose call is guarded by `".." in token`?
4. **`outside-root` swallows `missing-file`.** A link that exists only in some *other* same-named
   repo in another group folder, or in an archive the setting points at, now reports
   `outside-root`. If that line carries an `outside-root` allow marker, the finding is suppressed
   entirely. Was it suppressed before the change, from a main checkout, for the same link?
5. **The cache key.** `_VIEWS` is keyed on the scan root and `ATELIER_ESTATE_ROOT` only; the git
   config carrier is read once into the view. Is there any in-process path (tests, a fleet tool
   scanning several children) where the config differs per repo but the key does not?
6. **Group folder by negation.** Every non-hidden, non-symlink, non-repo directory under the
   estate root becomes a place a sibling may land, including a downloads folder, a folder of
   linked worktrees, or a scratch folder holding stale clones of a repo. Is that SB-A1 in another
   form?
7. **Two definitions of a group folder.** `estate.repo_parents` and `pins.discover` each decide
   what a group folder is, with near-identical but separate code (one skips an unreadable folder
   silently, the other warns). One fact, two homes (V4)?
8. **A submodule's or bare repo's worktree.** The delta changes `floorfleet`'s and `pins`'
   `main_checkout` for those two cases from "the common dir's parent" to "the path given". Is that
   behaviour change named anywhere a reader of the fleet tools would see it?
9. **Machine-local files.** From the main checkout, `pathscan` resolved nine in-repo references
   (`.claude/worktrees`, `.claude/settings.json`) that the same scan from a worktree reported as
   missing: ignored local files present only in the main checkout. That is not this delta's `..`
   path, but it is the same class `320/180` reported (same scanner, same content, different
   verdict by checkout). In scope as harvest, or a separate item?

## What the brief-writer ran, and what it got

All on 2026-11-14 UTC, foreground, load average 3.9 to 5.1 on 12 cores, neither carrier of the
setting present, from the review worktree at `d3293d93` unless stated.

- `cd tools && python3 -m unittest test_estate`: 24 tests, OK, exit 0, about 6 s.
- `test_pins`: 37 tests, OK, exit 0, about 29 s. `test_pathscan`: 172 tests, OK, exit 0, about 13 s.
  `test_linkscan`: 89 tests, OK, exit 0, about 6 s. `test_signfleet`: 21 tests, OK, exit 0, about
  8 s.
- `python3 tools/pathscan.py --root . .`: exit 1, 88 findings. `linkscan`: exit 0, 1230 Markdown
  files, 1620 internal links, 4 suppressed by allow marker (all `missing-file`).
- The same `pathscan` from the main checkout, at `2a6d7a41`: 79 findings. The difference was nine
  in-repo references to ignored local files (question 9) plus line-number drift in one README;
  no `..` reference differed.
- `python3 tools/pins.py`: exit 1 (at least one child not current). Funnel line: 32 entries, 29
  git repos, 22 carry a pin; no grouped-layout line, as expected with the setting unset.
- `git merge-base --is-ancestor c1af4465 HEAD`: exit 0. `git log c1af4465..HEAD` on the two
  `estate` files: empty; on the callers: nine commits.
- The `coldsweep --commit` line in the brief, as written: exit 0. The sweep line with the
  four `--also-exclude` paths: exit 0.
