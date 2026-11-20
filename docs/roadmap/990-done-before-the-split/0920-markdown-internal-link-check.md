- [x] **Markdown internal-link check** — BUILT 2026-07-10 (Opus), **REVIEWED
      2026-07-10 (Fable, cold session): PASS-WITH-FINDINGS, gate cleared** —
      verdict below the divider in `docs/reviews/2026-07-10-linkscan.md`.
      `tools/linkscan.py`, the mechanical check that atelier's "thin anchor, fat
      pointer" graph actually resolves. The review proved damage to **all five**
      of the brief's load-bearing assumptions and fixed it same session (suite
      171→187): L1 a typo'd path arg scanned nothing and exited 0 (the §14
      silent-success class — now exit 2); L2 case-mismatched links green on APFS
      but 404 on GitHub (now walked against on-disk casing, NFC/NFD-safe); L3
      links escaping the repo root (new `outside-root` kind — GitHub serves
      nothing above root); L4+L5 anchor matching now exact like GitHub's, after
      fixing the slugger's underscore-stripping divergence; L6 parenthesised
      filenames parse; L7 fence tracking length/info-string-aware (nested ````
      examples stay code); L9 setext headings now mint anchors. L8 root-relative
      `/…` semantics verified against GitHub docs; L10 indented-code FP stated
      as residual by design.
  - [x] **Wire linkscan into `ci.yml` + `pre-commit.sample`** — DONE 2026-07-10
        (Opus), the session after the verdict (don't-stack honoured). CI: a
        `--selftest` line + a whole-tree `linkscan --root . .` step, mirroring
        the triad. Hook: linkscan added as a **whole-tree integrity** check —
        *not* `--staged` like the two boundary scanners, because a link breaks
        when a *different* file is renamed/deleted (the stale file is usually
        not the one in your diff). `run_scan` generalised to drop the hardcoded
        `--staged` so each scanner declares its own mode; header documents the
        distinct contract; block-message + README updated. Contract pinned by
        three new `test_precommit.py` tests incl. the whole-tree crux (a rename
        breaking an *unstaged* link blocks — a staged-only scan would miss it);
        suite 187→190. Installed atelier hook refreshed so this very commit
        dogfoods it. **Residual, stated:** a scaffolded child inherits the
        stricter whole-tree contract (its whole doc tree must stay link-clean to
        commit, vs the diff-scoped boundary scanners) — cheap for a clean tree,
        `linkscan:allow`/`.linkscanignore`/`--no-verify` are the hatches.
