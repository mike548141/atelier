# Sibling to the deferral-side-doors cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-18-0508-deferral-side-doors-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-18 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Facts held back

1. **Intent and commissioning record:** `320/720` (the hand-up item whose path the brief bars) —
   **not opened by the brief-writer**. The landing commit's message body was not read either, so
   this sibling carries no account of the author's reasons; read both at reconcile.
2. **The neighbouring pass.** The paragraph's last sentence hands the commit-message door to
   `130/030`. That item's fix landed the same day as `8132805` (`tools/coldsweep.py --commit`)
   and `30aa8dc` (`skills/review-brief/SKILL.md`), and is queued for its own cold pass at
   `160/930`, briefed in the same sitting by this same brief-writer. The two passes share a
   brief-writer's framing; neither was told what the other found.
3. **Prior verdicts on these surfaces** (named by filename only, not opened, not exhaustive):
   the passes on rule 1's split (2026-07-29 and the DF series, 2026-08-02) and on the coldsweep
   ruling (2026-08-17) are the nearest; find them with
   `ls docs/reviews | grep -iE 'defer|split|coldsweep|cold-sweep'` at reconcile.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. **Subjects versus bodies.** The paragraph lists "recent commit subjects" as a door read at
   onramp, then says "the commit-message door is `130/030`'s". As landed, `130/030`'s fix is a
   body-free read of a landing commit *during* the review; it does nothing about subjects read at
   onramp by `git log --oneline`. Is the subject door covered by this paragraph's own "file and
   count only" duty, by `130/030`, or by neither?
2. **Scope sentence.** Rule 1 sits under a scope sentence binding rules 1–2 "whenever the brief
   is written by, or on the framing of, the work's author". The grounding case was a non-author
   brief-writer. Does placing the side-door duty inside rule 1 leave a non-author brief-writer
   (the grounding case's own writer) outside the rule's stated reach?
3. **Unnamed writers.** A queue-run orchestrator that dispatches a brief-writer writes the pointer
   claim, the index line in `docs/ROADMAP.md`, the session entry and commit subjects, and may
   relay the brief-writer's hand-back into its own records. It is neither "the author" nor "the
   brief-writer". Is it bound? The same question for the generated `docs/ROADMAP.md` line, which
   repeats the pointer's headline.
4. **The `RECORD.md` placement.** The sentence is appended to a bullet about keeping the index
   short and about a size-budget grounding. Will a session writing its close entry meet it there,
   and does the session-close skill (or its template) carry the same duty?
5. **One instance.** The paragraph is grounded in one episode ("Neither steered a finding").
   `PROPAGATION.md` § *When a rule keeps breaking* sets when a lesson becomes doctrine. Is this a
   gap closed in existing doctrine (no threshold owed) or a new rule minted on one instance, and
   does the text say which?
