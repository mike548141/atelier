# Sibling to the template-history privacy cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-18-0511-template-history-privacy-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the
brief are committed.** Written 2026-10-18 UTC by the Opus brief-writer named in the
brief's provenance; it forms no finding. Fold this file in below the reconcile and
delete it at phase 2.

## Intent record

- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/060-the-opening-prompt-template-history-from-the-transcripts.md`
  — read in full by the brief-writer. Lines 3–13 are the principal's words (the
  brief's acceptance test). Lines 14–21 say what existed before (an earlier
  reconstruction folded in by subtree merge, `0a949b4`, by version and "not audited for
  the two exclusions") and what was owed. Lines 23–40 are the author's closing account:
  sources and counts, who mined and who checked, how many units were dropped and why,
  one name replaced by a placeholder, some borderline units kept, scanners clean, one
  spelling exemption, what could not be recovered. Read it now as the author's claims
  to reconcile against.
- The bodies of `7033378` and `ec37c6b` — not read by the brief-writer.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-10-18, from its worktree root, on this machine,
with the local term list present:

- The 50 extracted versions: leakscan `--require-terms` exit 0, secretscan exit 0,
  datescan exit 0.
- The 52 delta messages (`7033378^..ec37c6b`): secretscan exit 0; **leakscan exit 1**.
  By rule name only: `email` ×52 and `nz-phone` ×1. The file holds 52 Co-Authored-By
  trailers, which matches the email count; the brief-writer did not look at any
  matched text, including the `nz-phone` hit, and forms no view on it.

## Prior verdicts on nearby surfaces (named by filename, not opened, not exhaustive)

- `docs/reviews/2026-10-16-1550-first-prompt-prefix-cold.md` — name suggests the
  session-open prompt; not opened.

## Overlap with other surfaces

- The current prompt file `docs/method/session-open/session-open-prompt.md` carries the
  earlier reconstruction's history (V1–V9, subtree merge `0a949b4`), which the intent
  record says was never audited for the two exclusions. It is outside this pointer's
  delta. A grep of `docs/roadmap/160-doctrine-review-owed/` found three queued passes
  naming that file (330, 540, 900), each for a doctrine change to it, none (by grep
  for "privacy") for its history's privacy. Whether one is owed is a reconcile
  question.

## The pointer's own lens hints

It asks for every one of the 50 versions to be tested against the two exclusions
quoted in the intent record. Nothing else.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. One unit keeps its frame with a private repo's name replaced by a placeholder. Does
   the frame, or the placeholder's role label, still let a reader infer what it
   replaced, given what else in this public repo names roles in the estate?
2. The author kept some borderline units as "generic selection wording". Which are
   they, and does each pass exclusion 2 on its own text rather than on the author's
   description of it?
3. Dropped units named private repos, tools or devices. Did a reworded or partial form
   of any of them survive in a different version, where an exact-match recurrence
   filter would treat it as a separate unit?
4. The README's *What was taken out* bullet names classes of private detail it removed.
   Is naming the classes (with their kinds of object) itself more than a public reader
   needs?
5. Author dates set to each version's first use, plus usage and re-paste counts in the
   bodies, publish a dated timeline of how often the principal opened sessions with
   this prompt. Is that within his stated aim, or personal information in the sense of
   exclusion 1?
6. The `.spellscanignore` entry cites a 2026-07-23 ruling that historical text is not
   retro-spelled. Was that ruling about text already in a repo, and does it reach text
   newly mined from private transcripts?
7. The `nz-phone` hit above: what does it match, and is it in a version commit's body
   or in one of the two author bodies?
8. A unit that recurred in two or more sessions can still be specific work if one run
   pasted it into its own workers. Does the recurrence count distinguish sessions the
   principal opened from sessions a run spawned?
