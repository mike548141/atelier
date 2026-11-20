# Session — applying TA1–TA9 (Track A application cold pass)

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 213+1 -->
- [2026-07-28 · 0214 UTC · TA1–TA9 applied; the estate-root branch reviewed and corrected; C1 ruled and built (Opus, wt: ta-findings-application, estate-root-naming)](2026-07-28-0214-ta-findings-application.md) — Mike's *"Bring me the TA1 ruling first, in plain language with impacts, and measure the blast radius against the live estate before costing it"*, with the standing warning that this programme's stated blast radius **has been wrong three times**. It was wrong twice more today, in both directions. **TA1 (MAJOR) → (a), TA2–TA9 → fix all eight, all nine applied, none deferred**: the scope guard tested path existence rather than membership, so `/etc`, `..` and an in-tree symlink pointing out all passed it and vacated a boundary check under a green tick; both halves of the membership rule now sit where `local.run`'s already did, and the rule was widened to `local.*.scope` because guarding one spelling of *where does this check look* while leaving its siblings open **is** the finding. Measured first: 14 configs, 2 declaring `scope`, 4 paths, **zero migrations** — the strong fix cost no more than the weak one, so the usual trade did not exist. TA2 rode free; TA3 gives silent scope drift a 🟡; TA4 was fixed **at the claim, not the mechanism**, and says so; TA5 stopped a commented-out floor step reading as `wired`; TA7 made the board work from a worktree, the mode this repo's doctrine prescribes. 720 → 733 tests, green with and without a machine term list. **The estate-root branch was reviewed cold and redone, not landed**: three defects — the mention count was an **~8× undercount** (8 claimed, **63 across 19 files**, 10 beside what the root holds), C5 had deferred the cheapest forcing function on an unmeasured cry-wolf premise that measurement **contradicts** (0 of 63 uses are the ordinary English word), and 🛑 **the widened rule was broken by the commit widening it** — the C5 item named the estate root in this public tree, inside the item proposing to enforce the rule. Its `⏳` pointer was also trimmed to refs after steering its own reviewer. Mike's forward-only ruling survives the correction and is strengthened by it. **Then Track C, C1 ruled and built (phase 1)**: `advisory` takes a `why` and a `review-by`, both hard-required, the date validated at parse; a passed date reds the board **and blocks nothing** (a commit failing on a date set months ago is how a forcing function becomes a `--no-verify` habit); the bare list still parses through a deliberate transition because children fetch `atelier@main` at run time and a hard error would break all ten children's CI the same afternoon. **A1 option (b)** ruled alongside it. Re-measured: **17 advisories across 10 children**, not the roadmap's 11 across 8. 747 tests green. 🚩 **Not done, and flagged rather than fudged**: the 17 declarations are unmigrated, because a `review-by` is a commitment about when a backlog clears — Mike's to set, not mine to invent across ten of his repos — and phase 2 is blocked behind that. Rule-4 `⏳` queued for both landings, neither spawned by this session.


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
