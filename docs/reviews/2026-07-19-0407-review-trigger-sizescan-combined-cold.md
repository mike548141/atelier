# Cold review — the review-trigger/design-review deltas + the sizescan doctrine deltas (combined pass)

**Date**: 2026-07-19 · 0407 UTC · **Status**: brief written, review pending

## Spawn provenance (REVIEW.md rule 4)

This review is spawned by a session Mike opened fresh with "Do any reviews, use
a worktree" — a session the deltas' authors neither started nor instructed. The
authors (two Opus sessions, 2026-07-18 and 2026-07-19, one of which also
authored the sizescan gate split) queued the `⏳` pointer and wrote no brief,
per rule 4. This brief is written by the taking session (Fable), which authored
none of the deltas under review. The cold reviewer is a fresh-context agent
spawned by the taker. Claim: `d43ca75` on `main`; work in worktree
`fable-cold-pass`.

## Subject (refs only)

Three doctrine deltas, queued as **one pass**. Review the named files **at
HEAD** (`d43ca75`) — later records commits amended wording, so the diffs are
how the deltas arrived, HEAD is what is binding.

1. **`method/REVIEW.md` § "Review the design, not only the build"** + the
   review-line convention. Commit `30c9cd9`. Intent record (deferred — see
   divider rule): `docs/decisions/2026-07-18-0820-review-the-design-not-only-the-build.md`.
   A sibling application exists in the private `ros` repo at `ros@55d0d51`
   (`~/.pets/ros`: `CLAUDE.md` + ROADMAP review policy) — in scope at your
   discretion; findings about it stay repo-generic in this public file.
2. **The trigger re-key + fork→pointer conversion.** Commit `4c17f59`:
   `method/REVIEW.md` (§ "Whether work earns a review at all"),
   `build/templates/docs/reviews/README.md`, `method/MODEL-ECONOMICS.md`,
   `build/templates/CONTRIBUTING.md`. Intent record (deferred):
   `docs/decisions/2026-07-19-0100-review-trigger-is-commitment-not-artefact.md`.
   A same-day records follow-up widened the delta (`REVIEW.md` intro,
   `method/PROPAGATION.md` enforcement clause) — those lines are in scope at
   HEAD.
3. **The sizescan doctrine deltas**: the grounded-budgets rule in
   `tools/sizescan.py`'s module doc, the `GATED` tripwire/advisory gate split
   (+ `tools/test_sizescan.py`), and the
   `build/templates/workflows/floor.yml` comment rewrite. ⚠️ Provenance fact
   you need to locate the delta: this code entered history inside `4fb09a7`,
   a *different* session's records commit that absorbed it from a shared tree —
   that commit's message does not describe it (acknowledged in `b33f072`).

Also before this pass, from the queue: **rule on the open question** whether
`method/PRINCIPLES.md`'s header ("every build is measured against") keeping the
build grammar is a defect the commitment re-key should have caught, or
correctly out of scope (design principles bind at design time).

## Ask

Review deep, not fast, all three lenses (`method/REVIEW.md` § What a review
actually checks): approach & assumptions — name and attack the load-bearing
assumptions yourself, as your **first act**; correctness & quality —
overclaims, silent scope-cuts, honesty of the records; completeness/harvest —
what the deltas should have covered and didn't, what they duplicated or
ignored. The framing of this brief, including its account of what the work is,
is itself attackable.

**Sequencing (rules 1–2, binding):**

1. Commit your own attack surface to your verdict draft **first**.
2. Only then open anything below the divider (the intent records, the authoring
   sessions' log entries) and any prior verdict files — to reconcile, never to
   anchor.

**Re-run every recorded proof in scope** — a proof you have not re-run is not a
proof you can close on. Recorded proofs include: the tool suite green
(`cd tools && python3 -m unittest` — records claim 267), the template drift
test (`tools/test_templates.py`), both live sizescan gate behaviours (a gated
file over budget → exit 1; a judgement doc over budget → `[advisory]`, exit 0 —
scratch fixtures are fine), the scans clean at HEAD (secretscan, leakscan,
linkscan, sizescan), and the claim that the stamped reviews-template pointer
resolves in a `create-repo`-shaped child (the old template's relative link is
recorded as having been broken in every stamped child — verify the new wiring,
don't assume it).

**Verdict**: append below this file's `---` divider. Stable IDs (F1…), severity
MAJOR / MEDIUM / LOW, per-lens coverage, spawn provenance repeated, your
attack-surface commit named, every re-run proof listed with its result. Apply
**nothing** (rule 3 — self-authored doctrine): the findings go to the
principal; the taker will add author-independent counsel but the decisions are
Mike's. Cycle close rule: this cycle closes only on a no-MAJOR pass plus the
principal's ruling.

---

## Deferred — open only after your attack surface is committed

Author-side evaluative accounts (the authors seeded no questions; these records
carry their framing):

- `docs/decisions/2026-07-18-0820-review-the-design-not-only-the-build.md`
- `docs/decisions/2026-07-19-0100-review-trigger-is-commitment-not-artefact.md`
- `docs/sessions/2026-07-19-0111-review-trigger-commitment-not-artefact.md`
  (author's log + a Fable retrospective addendum — the retrospective is itself
  an author-adjacent account, not a cold verdict)
- `docs/sessions/2026-07-18-1655-fleet-file-size-sweep-ros-shed.md` (the
  sizescan deltas' authoring session; its 1830 and tripwire addenda)
- Prior verdicts in `docs/reviews/` (notably `2026-07-14-2048-lean-files-sizescan-cold.md`
  — the grounded-budgets rule's origin) — rule 2: reconcile-step only.

---

# Verdict

**Reviewer**: cold-context agent (Fable), spawned by the rule-4 taking session.
Attack surface written and committed 2026-07-19 ~0404 UTC, before any deferred
material (intent records, authoring sessions' logs, prior verdicts, the brief's
below-divider section) was opened.

## Attack surface — the load-bearing assumptions I will attack (chosen cold)

Named from the brief's top section, `method/` docs, and the subject files/diffs
at HEAD only.

1. **The grounding narrative's internal consistency.** `REVIEW.md`'s
   enforcement paragraph still asserts the 2026-07-18 `ros` session broke the
   rule "while the correct rule sat in three places it had access to" — yet the
   follow-on delta (`4c17f59`) established one of those places (the stamped
   reviews template) carried the *broken* diff-shaped formulation. Does the
   doctrine's own grounding story survive its own later findings at HEAD?
2. **"Enforcement is structural" as a claim.** The review-line convention is
   itself prose: no template carries the field (admitted, queued), no scanner or
   CI checks for the line. Is "structural" an overclaim of the same class the
   apex forbids — and does atelier's *own* record-keeping since `30c9cd9`
   comply with the rule it wrote?
3. **The consolidation claim** ("four independent statements → one, plus three
   pointers"). Sweep `method/` + `build/templates/` at HEAD for residual
   artefact-shaped trigger grammar the re-key missed beyond the queued
   PRINCIPLES.md header.
4. **Fork→pointer actually achieved?** The template's new header bans restating
   the parent's trigger list — then the file restates a four-bullet trigger
   list. Is this a pointer with a thin floor, or a re-marked fork still free to
   drift? And does any line *narrow* the parent (its own "narrowing-free"
   claim)?
5. **The `<atelier-path>` pointer wiring.** The recorded claim is that the old
   relative link was broken in every stamped child and the new wiring resolves.
   Verify in a create-repo-shaped child: does the skill actually fill the
   placeholder, and does anything mechanical (linkscan, close-out grep) guard
   it?
6. **The remedy-class split's core premise** — "obeying the gate cannot damage
   content" for ROADMAP/SESSIONS. An all-open roadmap (ros's 125 open items is
   the live case) has nothing to relocate: the lossless remedy does not exist
   for it, so the gate's teeth *can* demand rewording or a budget hatch. Is the
   doctrine honest about that case, or does the class claim overreach?
7. **Gate mechanics at the edges.** GATED keyed by basename: interaction with
   `sizescan:budget=N` overrides (a gated file with a declared budget still
   gates?), `sizescan:allow`, `.sizescanignore`, ROOT_ONLY, the JSON schema
   change (new `gated` field — any consumer assumptions?), and whether the
   fail-safe exit-2 paths survived the change.
8. **Every recorded proof re-runs.** Suite green (records claim 267), template
   drift test, live gate behaviours both classes (gated over → exit 1;
   judgement doc over → `[advisory]`, exit 0), the four scans clean at HEAD,
   the stamped pointer resolving in a child. A proof that fails to reproduce is
   a finding.
9. **The budgets' own grounding.** The module doc demands class-grounded
   budgets and forbids deriving from current length — do the DEFAULT_BUDGETS
   and the new normative text meet the doc's own standard, and is the one-sided
   (no thinness floor) design defensible rather than merely asserted?
10. **The PRINCIPLES.md header question.** Rule it against PRINCIPLES' own
    first sentence ("The design doctrine for all technical work") and §1's
    design-time cases — does the header's build grammar contradict the file's
    own scope, and was deferring it to this pass correct?
11. **The pass structure itself (the brief is attackable).** Three deltas in
    one pass risks dilution; the sizescan delta has *no honest describing
    commit* (silent-absorbed into `4fb09a7`, whose message describes different
    work) — is "review the files at HEAD" sufficient mitigation, and is the
    absorb's acknowledgement mechanism adequate? Also: the combined pass's
    authors overlap (the 07-19 trigger delta's author is the 07-18 delta's
    applier; the sizescan text is the same session cluster) — does the one-pass
    fold weaken rule 4's independence in any way the brief hasn't named?
12. **Self-compliance of this very cycle.** Does the live queue/records trail
    since `30c9cd9` carry the review lines the new rule demands (the ⏳
    pointer, the ROADMAP items, the CHANGELOG entries), or is the repo already
    manufacturing the blank it declared to be the bug?
