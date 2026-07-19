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
