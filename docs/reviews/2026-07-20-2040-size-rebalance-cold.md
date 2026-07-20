# Cold pass — size-signal rebalance: line-count budget → cold-content gate (delta `5e68923..910085f`)

- **Date/time**: 2026-07-20 2040 UTC
- **Spawn provenance (rule 4)**: taken from the ROADMAP `⏳` queue by a session
  Mike spawned with "do any review or fable dependent work" (Fable). This
  session authored none of: the rebalance delta (`5e68923`, `3ec8823`,
  `b5dc12d`, `7418b41`, `910085f`), the sizescan tool it reworks, the doctrine
  files it edits, or any record of the authoring session (Opus,
  wt: atelier-size-signal-rebalance). Claim landed on `main` (`c8a1222`)
  before this worktree was created; this brief is taker-written.
- **Named exposure**: before claiming, the taker read the full ROADMAP `⏳`
  entry — which is **not** refs-only: it carries the author's complete
  evaluative account (the ruling's rationale, the "shipped" list, "green **the
  right way**") and a *review:* paragraph seeding two attack sites ("reverses
  a dated ruling + reworks a gate with a **silent-failure mode**"; "SR2's
  re-grounding rides"). The taker also read the SESSIONS.md index line for the
  authoring session (another evaluative summary) and the five commit
  *subjects*. All of that is author framing — treated as claims to re-derive,
  not facts; the seeded sites sit below the divider until this pass's own
  findings are committed. The pointer's breach of rule 4's refs-only ceiling
  is itself in scope as a compliance observation.
- **Deferred material (opened only after findings are committed)**: the
  ROADMAP entry's *review:* paragraph (re-read for reconcile); the authoring
  session's record `docs/sessions/2026-07-20-2025-size-signal-rebalance-cold-content-gate.md`;
  the CHANGELOG entry; commit message *bodies* of the five delta commits; the
  records commit `910085f`'s diff except its two-line `sizescan.py` /
  `test_sizescan.py` touch (which is code, in scope immediately); the
  2026-07-19 ruling record the delta supersedes.

## What the work is (refs only)

Commits `5e68923` (tools/sizescan.py + test_sizescan.py rework;
.github/workflows/ci.yml; docs/build/templates/workflows/floor.yml),
`3ec8823` (docs/ROADMAP.md → docs/ROADMAP-DONE.md harvest), `b5dc12d`
(docs/method/RECORD.md module doc), `7418b41` (docs/method/PROPAGATION.md
child-block size spec, "SR2"), `910085f` (records + a two-line code touch).
In-scope at HEAD: those files, plus every other doc/template/skill that
states or relies on the size signal (REPO-STANDARD, PROPAGATION child block,
create-repo, tools/README).

## Lenses and the taker's attack surface

Lens 1 — approach & assumptions (named by the taker as its first act):

- **A1 — the cold-content definition must be decidable at scan time.** The
  gate now fires on "a completed `[x]` item on a checkbox-worklog file". Both
  halves are classifiers: what makes a file a *checkbox-worklog* file, and
  what counts as a *completed item*? Attack both edges: false positives
  (`[x]` inside code fences, templates, doctrine that *quotes* checkbox
  syntax, and above all **ROADMAP-DONE.md itself** — if the archive is
  classified as a worklog, the gate demands harvesting the harvest, an
  infinite regress) and false negatives (`- [X]` uppercase, `* [x]`,
  indented sub-items, a done-item written without checkbox syntax).
- **A2 — dropping length as a *gate* must not open an unbounded hole.** The
  claim is that prose-shaped cold content and thinness are "caught at
  review, not measured". Is that the standing one-sided honesty applied
  correctly, or does it retire the only mechanical bound on hot-path growth
  with nothing mechanical left? What, concretely, still fires on a hot doc
  that doubles in pure prose?
- **A3 — the new gate must fail loud, not silent.** A regex-shaped detector
  that misses is indistinguishable from a clean repo — gate green either
  way. Does the tool distinguish "scanned and found nothing" from "didn't
  recognise anything as scannable", and does the suite prove the miss modes?
- **A4 — SR2's "~50 lines" must be grounded in the class, not the current
  measurement.** The standing rule (grounded-budgets correction, 2026-07-18)
  bars setting a number from what the artefact currently measures. "Class-
  grounded on the block's seven-concern shape" is the author's claim: if the
  block as shipped is ~50 lines and the derivation is a restatement of that
  fact, the number is the anti-pattern wearing the rule's clothes. Re-derive
  it: does 7 concerns × stated lines-per-concern actually produce ~50
  independently of the current block?
- **A5 — the advisory must have a consumer.** Line count now "reports but
  never fails". Who reads the report? If nothing consumes it, it is dead
  code plus noise; if humans read it in CI logs, it can still induce the
  line-golf the ruling set out to kill — check what the advisory looks like
  in output and whether its framing invites minimisation.
- **A6 — "lossless" harvest is a diff-checkable claim.** The harvest commit
  removes ~66 lines from ROADMAP.md and adds ~19 to ROADMAP-DONE.md. A
  lossless *move* should conserve content up to formatting; a 3:1 ratio is
  prima facie compression. Verify item-by-item what was dropped and whether
  the drop is defensible summarisation-into-archive or silent loss.
- **A7 — fleet semantics flip silently at pin bump.** Children copy
  `floor.yml` statically; a pin bump swaps their gate's meaning (length →
  cold content) in one move. Is that transition stated where a child
  session will actually see it, and is the old gate's vocabulary
  (budget/GATED/limit) fully retired from every surface children copy?

Lens 2 — correctness & quality: re-run everything stamped "proven": the
suite count (267→282) and its pass; floor green at `main` HEAD; the retitled
ci.yml/floor.yml actually running sizescan in cold-content mode; no stale
line-count-gate phrasing at HEAD (grep sweep across method docs, build
templates, tools/README, skills); the two-line `910085f` code touch is what
its subject says (a date fix) and nothing more.

Lens 3 — completeness / harvest: what states the old size signal and wasn't
caught — REPO-STANDARD, the PROPAGATION child block *as templated for
children*, create-repo's scaffold, ROADMAP items elsewhere that reference
the line-count gate as live; whether the 07-19 tripwire-split artefacts are
coherently superseded or half-retired.

Live re-runs owed in scope: `test_sizescan.py` suite (count + pass);
`sizescan.py` against the worktree HEAD (and against a synthetic worklog
fixture probing A1's edges); the A6 item-by-item diff; the grep sweeps.
