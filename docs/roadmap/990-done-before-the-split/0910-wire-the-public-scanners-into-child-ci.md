- [x] **Wire the public scanners into child CI** — DONE 2026-07-10 (Opus): the
      other half of the CI build, unblocked by the public flip (ADR 0005).
      `docs/build/templates/workflows/floor.yml` — a language-agnostic scanner
      floor any doctrine-inheriting child drops in beside its `ci.yml`. It checks
      `mike548141/atelier` out **as a sibling** and runs its public
      secretscan/leakscan/linkscan against the child's own tree (`repo/`) — no
      secret, no vendored copy, no drift. Design calls stated in the header, not
      buried: **floats `atelier@main`** (a scanner *floor* wants newest; also
      avoids a second stamped-SHA drift surface — the CLAUDE.md pin stays the sole
      doctrine-version truth; `ref:` commented for anyone wanting reproducible CI);
      **leakscan structural-only** (term list is machine-local — same honest scope
      as atelier's own `ci.yml`); **licenscan commented** (it hard-fails with no
      LICENSE, so it's a *publish* gate, wrong to default-on for a private child).
      Scan scoped to `repo/` because a whole-workspace scan would false-positive
      on atelier's own fake-secret fixtures (proven, load-bearing). Driven both
      ways before claimed: clean child passes 0/0/0, damaged child (real `AKIA…`
      key + broken link) blocks. Wired into create-repo (seed step 3, step 6 CI
      text), REPO-STANDARD file set, and pinned by 5 `test_templates.py` tests
      (one-source, repo-scoped, structural-only, licenscan-commented, least-priv;
      suite 190→195). The step-6 "not wired yet" text is retired.
  - [x] **Exercised on a real child (numen) — DONE 2026-07-11 (Opus).** Session
        27's owed real-child run: numen adopted `floor.yml`, closing its own
        stated no-CI-gate (unblocked by ADR 0005). Driving it caught two real link
        breaks in numen before push and exposed a **four-session linkscan false
        negative** — `SKIP_DIR_NAMES` held `build`, masking atelier's own
        `docs/build/` layer (14 files); fixed at `d0870a4` (drop `build`/`dist`;
        suite 195→196), which also caught the inherited template placeholder (now
        code-spanned). Proven on real GitHub Actions both ways: happy path green
        (`29092514962`), fail-closed red via a throwaway broken-link PR
        (`29092599385`, since cleaned up). Detail:
        `sessions/2026-07-11-28-child-ci-floor-exercised.md`.
  - [x] **Review the child-CI floor + the linkscan masking fix** — RAN
        2026-07-11 (Fable, cold session): **PASS-WITH-FINDINGS**, verdict below
        the divider in `docs/reviews/2026-07-11-child-ci-floor.md`. The brief's
        sharpest question answered decisively: the masking fix closed the
        *instance*, not the class — secretscan + leakscan still hardcode-skipped
        `build`/`dist` (a planted key in `docs/build/` scanned green, proven
        live), still phantom-succeeded on a nonexistent path (the linkscan L1
        class), and the child's ignore-file hatch was dead under exactly the
        floor.yml invocation (CWD-relative vs root-relative globs). Six findings
        N1–N6, all [fixed] + re-driven same session (suite 196→205): both
        scanners mirror the linkscan fixes; floor.yml gains every-push triggers
        (a never-PR'd branch was scanned by nothing), a selftests step, and
        in-file FP-hatch docs. Floating `atelier@main` attacked and **held**
        (N1–N3 reaching every child with zero bumps is the argument); the
        real-infra secret drive judged NOT owed (closed by composition).
        **Gate cleared — floor.yml may roll to further children.**
        - [x] Follow-ups — BOTH DONE 2026-07-11 (Opus), each proven on real
              infra. **atelier's own `ci.yml`** widened to every-push +
              `workflow_dispatch` (`2a4b2fd`); the gap-closure proven by pushing
              a throwaway `n4-trigger-proof` branch (never PR'd) and watching CI
              fire green on it — a run that would not have existed before — then
              torn down local+remote. **numen re-copied `floor.yml`** byte-for-
              byte from the post-review template (numen `f81f66f`), picking up the
              workflow-file fixes that don't float (N4 every-push, N5 selftests
              step, N6 hatch docs); numen's floor ran green with the new selftests
              step live in the job log. numen's tree re-scanned clean in the exact
              floor.yml shape first. numen's frozen pre-scaffold hook (no linkscan)
              stands as already flagged — its floor is the only linkscan gate.
