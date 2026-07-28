# Session — applying TA1–TA9 (Track A application cold pass)

- **Date**: 2026-07-28 02:14 UTC
- **Worktree**: `ta-findings-application`
- **Subject**: apply the nine findings of the Track A application cold pass
  ([verdict](../reviews/2026-07-28-0123-track-a-application-cold.md)),
  ruled by Mike 2026-07-28.
- **Rulings taken**: TA1 → **(a)** (validate at parse, mirroring `local.run`);
  TA2–TA9 → **fix all eight**. Both rulings were put to Mike with the blast
  radius measured first, per the standing instruction that this programme's
  stated blast radius has been wrong three times.

## Blast radius, measured before costing

The measurement that decided TA1's cost, taken against the live estate rather
than inferred from the fix shape:

| Measure | Count |
|---|---|
| Floor configs in the estate | 14 (parent + 13 children) |
| Repos declaring `scope` at all | 2 |
| Declarations on a scanner that can be vacated | 1 |
| Declared paths failing the stricter rule | **0** |

Every live declaration is relative, in-tree and unsymlinked, so the strong fix
carried **zero config migrations**. That removed the usual cheap-vs-thorough
trade entirely — the fourth time this programme's real numbers have come in
under the shape's implied cost. Re-verified after landing: 14 configs load
clean under the new rule, `floorfleet --check` exits 0.

## What was applied

| Finding | Applied as | Proof |
|---|---|---|
| **TA1** (MAJOR) | Both halves of the membership rule: lexical (absolute, `..`) at `Config.validate` for fleet `scope` *and* `local.*.scope`; resolved (`commonpath`) at the run guard for the symlink member | ✅ live — all three members block, both planes, rc=1, zero tracebacks; an in-tree scope still runs |
| **TA2** (minor) | Rides free — rejected at parse, so an absolute scope never reaches `scan_paths` to crash it | ✅ live — 0 tracebacks across 6 probe/plane combinations |
| **TA3** (minor) | Partial scope drift on a softenable check renders 🟡 with "N of M scope paths missing", carried into `--json` by EP3's route | ✅ live — renders, does not block (rc=0), reaches JSON |
| **TA4** (minor) | Fixed at the claim: the note states the *invocation*, not a cover level it cannot observe | ✅ live — scanner says "structural + local", floor says the plane omits `--require-terms`; both true |
| **TA5** (minor) | Quote-aware comment stripping before `PARENT_RUN_RE` matches; workflow files newline-joined | ✅ 4 cases — commented-out ✗, live ✓, trailing comment ✗, quoted `#` ✓ |
| **TA6** (note) | Fixture moved from module scope to `setUpModule`/`tearDownModule` | ✅ bare import now creates no temp dir |
| **TA7** (note) | Discovery searches beside the **main checkout**, via the `--git-common-dir` resolution `_repo_name` already used | ✅ live — board run *from this worktree* lists parent + 13 children |
| **TA8** (note) | EP2's MAJOR grade restored in the intent record, with a stamped correction note | ✅ record |
| **TA9** (note) | AWA2 given a multi-commit grammar: the landing commit is the one that **completes** the series | ✅ doctrine; followed by this very series |

## Named, not hidden

**TA4 is fixed at the claim, not by plumbing.** The floor still cannot read
what cover a scanner actually got — that needs capturing child output, and
streaming scanner prose live is worth more than closing a gap that errs toward
claiming *less* cover than a run had. The 🟡 stays because on a real runner,
which holds no term list, the reduction is real. Stated here because "fixed"
would otherwise round up.

**TA1 was widened inside the ruled class, deliberately.** The ruling named
fleet `scope`; `local.*.scope` feeds the same `subtrees`/`_render` path and
carried the identical hazard. One spelling of "where does this check look"
being guarded while its siblings were not *is* the finding, so applying the
rule to only one spelling would have re-created it. Named in the code and here.

## Verification

- **733 Python tests + 207 node tests, run twice** — machine term list present,
  and absent (`HOME` redirected, `ATELIER_LEAKSCAN_TERMS` cleared). Green both
  ways, both suites. 727 → 733 over the series (+13 from 720 at pass time).
- Live probes for TA1/TA2/TA3/TA4/TA5/TA7 as tabled above, each run against the
  probe that established the defect rather than against the tests' word.
- Estate re-measured after landing: 14/14 configs load, fleet `--check` rc=0.

## Owed

Rule 4: a MAJOR stood in the reviewed pass, so the cycle is open and **this
application earns a further cold pass**. A `⏳` is queued in the landing commit
of this series — the commit carrying this record — per the grammar TA9 just
added. **Not spawned by this session**: the applier does not spawn its own
review, and REVIEW.md's own text was edited here (TA9), which is self-authored
doctrine and independently earns the pointer.

Open from this session: nothing. TA1–TA9 are all applied; no finding was
deferred.
