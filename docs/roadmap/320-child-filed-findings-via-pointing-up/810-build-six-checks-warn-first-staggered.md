- [ ] 🔎 **Build the six checks he chose, warnings first, then blocking, each
      turned on at a staggered date.** His words, 2026-11-09: *"all six, warnings
      at first and then move to blocking action. With a staggered turn on of each
      so they dont all hit at once"*. The six, each with its home item: commits
      name their files (`320/060`); "ruled" with no quote of him (`320/100`);
      private names in branch names and commit titles (`160/360` NP2); the closed
      personal-data list (`160/630`), which needs a per-repo visibility key (now
      built by `260/050`) and warn-first since several private children carry many
      personal-data markers; edits inside mapped sub-sections (`320/340`); a quote
      of him on commits touching his prompt (`160/900` QK1's second counsel).
      **Shape:** a dated constant per check, in the style of G3's grace, and the
      turn-on dates spaced out so at most one goes blocking at a time. Probe every
      child before each flip. Each build is self-authored guard code, so each
      queues its own cold pass at its landing.
  - [x] ✅ **Slice 1 LANDED 2026-11-09: edits inside mapped sub-sections
        (`320/340`)**, in `tools/blockscan.py`. An edit in an unmapped subsection
        of a mapped section is a `subsection` finding, the same remedies as a
        violation. It warns and exits 0 until **2027-01-11**
        (`SUBSECTION_WARN_UNTIL`), then exits 1. Not fleet-registered, for the
        reason that scanner's docstring gives: it reads atelier's own doctrine
        docs. Probe by exit code: 21 of 21 child checkouts exit 2 before and
        after (no map, never wired there), atelier exits 0; replayed over 124
        doctrine commits, 14 would have warned, all real subsection edits. Tests:
        18 new in `tools/test_blockscan.py`, 53 total.
  - [x] ✅ **Slice 2 LANDED 2026-11-09: "ruled" with no quote (`320/100`)**, a
        new scanner, `tools/attribscan.py`, registered in `tools/floor.py` with an
        advisory form. It reads only lines a commit adds, on both planes, and the
        whole-tree form reports and never blocks, because an old record cannot be
        fixed without rewriting it. Warns and exits 0 until **2027-02-08**
        (`ATTRIBUTION_WARN_UNTIL`), then exits 1 unless `--warn`. Probe by exit
        code on the CI plane's own line, with the date patched: 22 of 22 (21
        children and atelier) exit 0 today and on the flip date. Whole-tree
        share, measured, not gated: 1,372 of 5,144 Markdown files carry the
        form (27%); the highest single child is 1 of 2 files and the next 4 of
        10, so no child's records are mostly this. Tests: 32, in
        `tools/test_attribscan.py`.
  - [x] ✅ **Slice 3 LANDED 2026-11-09: the closed personal-data list
        (`160/630`)**, a new scanner, `tools/pdlistscan.py`, registered in
        `tools/floor.py`. Only a repo that declares `"visibility": "public"` is
        in scope, so a private child's markers never reach it. Reports a missing
        list, a personal-data marker in a file no entry names, and a listed
        string in a file its entry does not name. Warns until **2027-03-08**
        (`PERSONAL_DATA_WARN_UNTIL`), then exits 1 unless `--warn`. Probe by
        exit code with the date patched: 22 of 22 exit 0 today and on the flip
        date; atelier is the only repo in scope, with 0 findings. Tests: 21, in
        `tools/test_pdlistscan.py`.
  - [x] ✅ **Slice 4 LANDED 2026-11-10: commits name their files (`320/060`)**,
        a new scanner, `tools/sweepscan.py`, registered hook-only, warn-only,
        **with no blocking date**: see the finding on `320/060`, where the
        measured rate (88% of commits in atelier, 97% in one child, by session
        transcript) is why. Probe by exit code: 21 of 21 exit 0. Tests: 11, in
        `tools/test_sweepscan.py`.
  - [x] ✅ **The commit-message plane LANDED 2026-11-10**: `floor.py --plane msg`,
        `.githooks/commit-msg` beside `pre-commit`, a `msg` template on `Scanner`
        absent by default. A clone that predates the hook is told by one line on
        its own next commit; nothing reaches into it (a hook needs installing per
        clone, and `floorfleet` does not yet check for this one).
  - [x] ✅ **Slice 5 LANDED 2026-11-10: private names in branch names and commit
        titles (`160/360` NP2)**, a new scanner, `tools/namescan.py`, on the
        commit-message plane, in scope only for a repo declared public, reading
        leakscan's own term sources (no new list). Warns until **2027-05-03**
        (`NAME_WARN_UNTIL`), then exits 1 unless `--warn`; on CI it reports only.
        Measured over atelier: 0 of 2,285 titles and 0 of 41 refs. Probe by exit
        code with the date patched: 21 of 21 exit 0 today and on the flip date
        (atelier in scope, the other 20 out). Tests: 14, in
        `tools/test_namescan.py`, plus `tools/test_commitmsg.py` (11).
  - [x] ✅ **Slice 6 LANDED 2026-11-10: a quote of him on commits touching his
        prompt (`160/900`, QK1's second counsel)**, a new scanner,
        `tools/quotescan.py`, on the commit-message plane. Warns until
        **2027-05-31** (`QUOTE_WARN_UNTIL`), then exits 1 unless `--warn`; on CI it
        reports only. Measured over atelier: 19 commits touch the prompt, 8 carry
        a quote (42%). Probe by exit code with the date patched: 21 of 21 exit 0
        today and on the flip date; only atelier holds the path, so it is the
        only repo where this can fire. Tests: 14, in `tools/test_quotescan.py`.
  - [ ] **The dates are the run's choice, not his**: 2027-01-11, 2027-02-08,
        2027-03-08, one check at a time and four weeks apart, none before
        2027-01-11 because earlier flips already fall on 2026-11-18, 2026-12-09
        and 2026-12-18. Each flip needs a fresh fleet probe before its date.
  - [ ] **Three cold passes owed**, one per landing (each is self-authored
        guard code): the orchestrator queues them when it lands the work.
  - [ ] **What remains: the flips and their probes.** Five dated turns, each
        needing a fresh fleet probe by exit code before its date:
        `SUBSECTION_WARN_UNTIL` 2027-01-11, `ATTRIBUTION_WARN_UNTIL` 2027-02-08,
        `PERSONAL_DATA_WARN_UNTIL` 2027-03-08, `NAME_WARN_UNTIL` 2027-05-03,
        `QUOTE_WARN_UNTIL` 2027-05-31. `sweepscan` has no date and no flip: it
        waits on his call (`320/060`). The 2027-04-05 slot the run planned for
        it stays unused, so the later two did not move up. Existing clones need
        `tools/commit-msg.sample` installed for the last two to run; the hook
        plane tells each one on its next commit, and until then their CI report
        is the only cover. `floorfleet` does not yet check for this hook.
  - [ ] **Dates 2027-05-03 and 2027-05-31 are the run's choice, not his**, four
        weeks apart and after the three already set, in the order built. The
        measurement fits both: `namescan` found nothing in atelier's titles, and
        `quotescan` fires only on commits touching one file.
