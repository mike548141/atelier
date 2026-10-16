- [~] (claimed 2026-10-16-1633 UTC by queue run abe96d8d, verification at HEAD only, a read-only worker) 🔎 **Hand-up from a private child: at the hook plane the content
      scanners (`spellscan`, `wrapscan`, and by registry `datescan`,
      `reviewscan`, `sizescan`) read the WORKING TREE, not the staged index,
      so one writer's unstaged draft blocks everyone else's commit, and the
      commit's own staged content can pass unread** `[S][tools]`. Handed up
      2026-10-12 under `PROPAGATION.md` § *Pointing up*; the reporting child
      first held it as owed upstream. The child saw the block live in a
      checkout shared by several writers. Atelier decides whether and how to
      remedy it.

      ## The finding

      The hook plane asks "what is this commit about to make true?", which is
      the staged index. `board`, `secretscan`, `leakscan`, `conflictscan`,
      `publishscan` and `harvestscan` already pass `--staged` there, and the
      `board` rationale in the registry says why (`010/020`). Five scanners
      do not, and the first two are blocking checks:

      | scanner | hook argv (registry) | `--staged` in the tool? |
      |---|---|---|
      | `spellscan` | `--root {root} {scope}` | no |
      | `wrapscan` | `--root {root} {scope}` | no |
      | `datescan` | `--root {root} {scope}` | no |
      | `reviewscan` | `--root {root} {scope}` | no |
      | `sizescan` | `--check --root {root} {scope}` | no |

      Two failures follow from reading the disk instead of the index:

      1. **A false block.** In a checkout with several writers, an unstaged
         file that is none of this commit's business (a half-written draft
         with a US spelling) reds the hook for every other writer until its
         author fixes it or someone works around the hook.
      2. **A false pass.** The check reads the file as it sits on disk. If the
         staged blob has the defect and the disk copy was fixed after
         `git add`, the hook is green and the defective blob is committed.

      ## Measured, 2026-10-12, at `origin/main` `fd63df8`

      Synthetic repro, a throwaway repo with a `docs/` directory and
      `core.hooksPath` pointing at `tools/pre-commit.sample` with
      `hooks.atelierTools` set to this checkout's `tools/`:

      - **False block.** `docs/a.md` and `docs/b.md` committed clean.
        `docs/a.md` edited and staged (clean content). `docs/draft.md` created,
        not staged, containing one line with "organize". `floor.py --plane hook`
        reports `❌ spellscan enforced` on `docs/draft.md:1 [us-spelling]` and
        `BLOCKED by: spellscan`; `git commit` exits 1 and no commit lands.
        The staged change was clean.
      - **False pass.** `docs/c.md` containing "organize" staged, then the
        disk copy changed to "organise" without re-staging. `git commit`
        succeeds, and `git show HEAD:docs/c.md` shows "organize". The
        committed content is exactly what the scanner exists to refuse.
      - **`wrapscan` on its own.** An unstaged 2,000-column line in
        `docs/long.md` is reported (`wrapscan: 1 finding(s)`) while the staged
        set is a single clean file, so it has the same working-tree reach.
      - **Not run:** `datescan`, `reviewscan` and `sizescan` were not
        exercised against an unstaged file. They are listed from the registry
        argv and from `grep -c staged tools/<name>.py` returning 0 for each.
        Treat their rows as read from the code, not measured.

      ## What is probably deliberate

      `linkscan`, `pathscan` and `indexscan` are whole-tree on both planes
      with a stated reason in the registry (a rename breaks a link outside
      the diff that caused it). That reasoning does not carry over to the five
      above, whose findings are properties of the text a commit adds, as it
      does for `secretscan` and `conflictscan`. Whether any of the five has a
      whole-tree reason the registry does not state is atelier's to judge.

      ## Suggested direction (atelier decides)

      Read the staged plane at the hook for the content scanners, the way
      `board` does: a `--staged` flag that selects the index (files via
      `git show :path`, reusing the `harvestscan` plumbing `010/020` used),
      added to the hook template only, with the CI template unchanged because
      a CI checkout already is the committed tree. Two points to settle when
      it is built: how the scope argument (`docs`) narrows a staged path
      list, and what the floor prints for a staged-only finding in a file
      whose disk copy differs. A fixture pair mirroring the two measurements
      above would pin both directions.
