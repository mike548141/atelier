- [x] **DONE 2026-10-18** (wt: atelier-qr-115-360)
      🔎 **A bare `.` (or `./…`) positional makes the three staged-plane
      guards scan nothing and report clean** `[S][tools]`. Found 2026-10-18 by
      the cloud session running the review queue, when the pushed floor went
      red on a finding its own by-hand staged scan had passed.
      **What happens.** `leakscan`, `secretscan` and `conflictscan` in
      `--staged` mode restrict the staged set to paths under the positional
      prefixes: each positional `p` becomes the prefix `p.rstrip("/") + "/"`
      and a staged path survives only if it starts with that prefix or equals
      `p`. git lists staged paths repo-relative (`docs/x.md`), so the
      positional `.` becomes `./` and matches nothing, `./docs` becomes
      `./docs/` and matches nothing, and the filtered set is empty — a scan
      covering nothing that prints exactly like a scan that found nothing
      wrong. Measured in a scratch clone with a staged conflict marker and a
      staged live-shaped key: `--staged --root . .` → all three guards clean;
      `--staged --root . docs`, `--staged --root . docs/sessions` and no
      positional → every finding reported. The real hook plane is **not**
      affected: `floor.py` expands `{scope}` to the declared paths or to no
      positional, and the same clone's hook plane blocked on both probes.
      **Why it matters.** This is the absolute-path hole's sibling.
      `report.refuse_absolute_staged` exists because "an absolute one matches
      nothing, the filter empties the set, and a boundary scan covering
      nothing looks exactly like one that found nothing wrong" (leakscan,
      2026-07-25); a relative spelling that also matches nothing fell outside
      that refusal. The natural hand invocation — the shape every tree-plane
      run accepts — is the one that scans nothing. The cost here was a run
      of 25 commits whose messages each said "leakscan structural-only green
      on the staged lines" on the strength of a `.`-scoped scan; the CI tree
      plane was the cover that actually held (green on every head until a
      record quoted an email-shaped identity, which CI caught and the hand
      scan had not).
      **Proposed fix, for the house to weigh:** normalise positionals in
      staged mode (`os.path.normpath`, so `.` means no restriction and `./x`
      means `x`) in the one shared place the three guards read them, and
      refuse a positional that leaves the staged set empty when it was
      non-empty before filtering — the same fail-closed shape as the
      absolute-path refusal, with a test per guard. `SX1` of the 2026-10-17
      staged-diff pass is the neighbouring class in the same reader.
      - review: not owed until the fix lands; it touches three guards'
        staged readers, which are doctrine by function, so it queues its own
        ⏳ at landing.
      ✅ **Fixed 2026-10-18, `692c04a`.** One shared reader,
      `report.scope_staged`, now serves all three guards. It normalises each
      positional (`.` restricts nothing; `./x` means `x`) and refuses, exit
      2, one that normalises out of the repo (`..`, `../x`), beside the
      existing absolute-path refusal. The item's proposed refusal, "a
      positional that empties a non-empty set", was deliberately NOT built:
      the hook plane passes declared scope as positionals, so a commit
      staging only out-of-scope files empties the set legitimately. Once
      spelling is normalised, leftover emptiness is scope. Probed in a
      scratch clone: `.`/`./docs` were exit 0 over a staged conflict marker
      and key before the fix, exit 1 after; hook plane scoped elsewhere
      stays clean, scoped to the findings still blocks. 16 new tests;
      1949 Python tests green. Cold pass queued at `160/950`.
      🔎 **The narrower truth, added 2026-11-09 beside the principal's
      2026-11-08 answer on `160/950` (the cold pass's QS11).** Three
      statements above hold only in part. *"The real hook plane is **not**
      affected"* was true of the bare `.`, which `floor.py` drops. It was not
      true of the class: the floor passes `./x` and `x/.` through its render,
      and a scope spelt by case (`Docs` for git's `docs`) or Unicode
      normalisation passed the floor's filesystem `exists()` check on a
      case-folding disk and then matched nothing in git's path list. *"Once
      spelling is normalised, leftover emptiness is scope"* was false on that
      platform: the reader compared text with git's paths, and a spelling the
      filesystem forgives and git does not (QS1, MAJOR) read clean over a
      staged live-shaped secret. And the refusal this record declined (a
      positional that names nothing) rested on a premise the floor
      contradicts: it blocks a declared scope that does not exist before any
      guard runs, so no hook-plane invocation hands the guards a missing
      directory (QS2). The principal's answer was to fix it and take the
      reviewer's advice on every finding. `tools/report.py`
      `resolve_staged_scope` now lets git resolve each positional and exits 2
      for one git does not know, and the same change covers `--root` naming a
      different repo from the cwd's (QS3), the prefix boundary and
      exact-file pins in each guard's tests (QS4, QU1), the stale comments
      (QS5), `tools/README.md` wiring (QS6), and `posixpath` (QS10). Item:
      `160/950`.
