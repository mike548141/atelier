# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-three-channels-cold.md` (`REVIEW.md` rule 1). Written
2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta. Open this
only after act 1 is committed. Everything here is a floor, never a fence, and none of it is a
finding.

## The queue pointer's questions (author-written, verbatim)

> whether 'meant to stand' is decidable by a session in the moment; whether the authorship caveat is
stated so an audit can follow it.

## The brief-writer's own questions

1. `GUARDS.md` now says something he "chose in the question box" is as binding as the opening
prompt. The house also holds that a pick from offered options is an answer, not a ruling. Do the two
agree?
2. Is three the right number? A slash command's typed arguments, a Stop-hook's feedback, a pasted
message: check against what the transcripts hold, and against the later `457f374d` commit.
3. Where do 3,020 and 1,305 come from? Find each figure's source.
4. "Before the turn ends" is the homing deadline. Is it followable for a turn that is mid-work when
the instruction arrives?
5. Who else in the instruments reads a single channel today, not only `cctranscript`?
6. The landing commit and the pointer commit are separate (`b12c4b15`, then `8ef6d59c`).

## What the brief-writer ran, and what it got

- `floor`: at c132cc1c: hook exit 0, ci exit 0. pathscan reports 3 findings, warn-only:
  docs/method/EVIDENCE.md:427, docs/method/session-open/session-open-prompt.md:13 and
  docs/method/session-open/template-history.md:10 (paths that do not exist from the repo root).
