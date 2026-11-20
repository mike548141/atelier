- [x] **Rewire `create-repo` to inherit from atelier** — DONE 2026-07-10 (Opus):
      the core Q1 fix. The skill now inherits from atelier (points up to
      REPO-STANDARD/REPO-BOUNDARY/PROPAGATION, seeds from `build/templates/`)
      instead of re-encoding the standard, and **stamps the doctrine block + SHA
      pin** into every new repo's CLAUDE.md — the skill had *no CLAUDE.md template
      at all*, so PROPAGATION was bypassed at birth. Templates moved skill→
      `build/templates/` (18 files, one source), the missing CLAUDE.md template
      added, three instance-residue scrubs + one live ros-is-canonical drift fix;
      leakscan clean. Skill stays machine-local (delivery vehicle), hard-depends
      on atelier, fails honestly if absent. Stamp core dry-run-proven in scratch
      (renames + all four placeholders + drift-check runs "current"); real-repo
      run (`gh` create + hook install) + Fable sweep owed. Review-owed.
  - [x] **Real-scaffold exercise — DONE 2026-07-10 (Opus):** scaffolded a real
        local git repo from the templates (seed → 3 renames → stamp → hook →
        commit) and drove the hook end-to-end. Surfaced + fixed a live
        **scan-hook fail-open defect** the scratch dry-run couldn't:
        `tools/pre-commit.sample` pointed at `$repo_root/tools/` and skipped
        silently when the scanners were absent — a child has none (they live in
        atelier), so its hook committed a real `AKIA…` secret. Fixed to resolve
        atelier's tools (`ATELIER_TOOLS` → `git config hooks.atelierTools` →
        in-repo fallback) and **fail closed**; step 6 bakes the path + a
        prove-it-once check. Re-proven: fail-closed / blocks-secret / passes-clean
        / atelier-unaffected, then pinned by `tools/test_precommit.py` (5 tests,
        known-failure proven against the pre-fix sample; suite 137→142 OK).
        **Still owed:** the single `gh repo
        create --push` step (not run — outward, unneeded for a throwaway); the
        Fable sweep (now briefed — gate below); and **CI scan wiring** — CI
        templates run no scanner, so the hook is a scaffolded repo's only scan
        gate (needs the scanner-distribution call: vendor / fetch atelier /
        publish — folds into the deferred supply-chain item).
