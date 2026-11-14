# Held back — the principal's method for asking, and an answer is not a ruling

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer (`cclive` lists it as session `43c70bbb`), which did not
author the delta. Nothing here is a finding: these are questions, and facts read off the machine.

## The pointer's own questions

1. Does any bullet claim more than its grounding?
2. Is the sentence on words he types in reply to a question honest about what is unsettled? Since
   queued, `2a6d7a41` replaced that sentence on his 2026-11-12 pick. Was `e7370f78`'s version honest
   when it landed, and does anything else the delta wrote (`CHANGELOG.md`, `RECORD.md`, the open 🤔
   sub-bullet in `420/020`) still say the question is open?

## The brief-writer's questions

3. "One was built on 2026-08-09 and deleted the same day." `git log` shows a scanner scoped on
   2026-08-10 and removed on 2026-09-18 (fact 3). Was it the P5 rule inside that scanner, not the
   scanner, that was built and deleted the same day? If so, does the sentence misstate what was
   tried?
4. The "Written to him" bullet ends: "so the two-step rule above rests on its own grounds". At HEAD
   the rule above is text then device in the same turn, and the bullet's own nineteen same-turn
   asks now read as support for it. Does the sentence still say something true?
5. "Work proceeds on it, because it is his decision on what was asked" is not in his words. Does it
   give an answer weight he did not grant, or rightly stop an answer being ignored? Does it sit
   with the apex's "rulings conditioned on being informed"?
6. The section's title, *Asking for a ruling*, and the apex's "governance ruling" use the word the
   new distinction reserves for his own words. One sentence acknowledges it. Is that enough, or is
   it a contradiction every reader meets before the definition (V5)?
7. "A pick is never written as 'ruled'." Sweep `docs/method/` for lines landed after 2026-11-09 that
   still call a pick a ruling. Is the rule followed in the doctrine that states it?
8. ⚖️ "also tag[s] a session's own weighed note" in older lines. After this delta, what mark does a
   session's own weighed note carry? If none, will the old use keep growing?
9. The child template's asking bullet (`docs/build/templates/CLAUDE.md`, lines 48–61 at
   2026-11-14) carries neither one question at a time nor the answer/ruling marks, and still says
   "(one extra turn)". Was the template a mirror site this delta owed (V3), or `160/1440`'s ground,
   or neither because it only points?
10. "The ruling round of 2026-11-09 still asked up to four per box" is a dated incident inside a
    practice bullet. Is a practice bullet its right home, and is calling it a "ruling round" an
    instance of the conflation the same section forbids?
11. Privacy: "One session, 2026-11-06 to 11-08", the four quoted replies, and "nineteen asks" come
    from one child's transcript. Does any of it let a reader with access to the estate pick out
    which child or session, against the hand-up's class-only filing?
12. "Check parallel sessions before asking, by `CONCURRENCY.md` § *The channel*". Does that section
    give a session a way to find out that he has already answered the same question in another
    session? Or is the pointer a name for a duty with no method?
13. The unmet-term check sits in § *The axes a calibration covers*, a list of what calibration
    covers. Is a writing-time rule at home there, and is it one home with "The box makes sense on
    its own", which cites it (V4)?
14. The hand-up's part 3 (whether "completed message" means "end the turn") got "no rewording" in
    the landing note. The 2026-11-12 change then reversed the reading. Did leaving part 3 alone
    leave a contradiction in the tree between 2026-11-09 and 2026-11-12, and is any of it still
    there?

## Facts read off the machine (2026-11-14 UTC, from the worktree root)

1. Re-run lines: `git merge-base --is-ancestor e7370f78 HEAD` exit 0; `coldsweep --selftest` exit
   0; `coldsweep --commit e7370f78` exit 0, 180 lines; `coldsweep --commit 2a6d7a41 --path
   docs/method/COMMUNICATION.md` exit 0, 69 lines; `floor.py --plane ci --root .` exit 0, 34.7 s
   wall clock under `nice -n 10`, Python 3.14.6. The acceptance lines: `grep -c` prints 1; the
   2026-10-03 quote is present within lines 1–32 (wrapped across lines, so a one-line `grep -o` of
   the whole sentence misses it); the option label is present.
2. `e7370f78`'s stat: `CHANGELOG.md`, `docs/ROADMAP.md`, `docs/method/COMMUNICATION.md`,
   `docs/method/RECORD.md` and four board item files. Markdown only.
3. `git log -- docs/method/COMMUNICATION.md` lists `e390382a` (2026-08-10, subject begins
   "plainscan: scope the repo plane") and `f1d5b5e9` (2026-09-18, subject "merge: plainscan removed
   on Mike's ruling; engine archived (020/360)").
4. The `020` section README's P5 account: "90.6% of 6,764 replies fired", 23,857 findings, with a
   three-row table of fixes (90.7%, 90.7%, 90.6%).
5. ⚖️ appears in 28 files under `docs/roadmap/` and in none of `docs/ROADMAP.md`'s lines. The
   author's landing note in `420/020` gives "about 14 of 33 ⚖️ board lines", by a keyword count.
6. No file matching `tools/test_*.py` or `instruments/*.test.js` names `COMMUNICATION`.
7. Neighbouring passes: `160/1210` (the two-step rule as `0ba1ba03` wrote it) has an unrun brief,
   `docs/reviews/2026-11-09-0238-estate-root-reader-side-two-steps-cold.md`; `160/1440` (the
   2026-11-12 answers, `2a6d7a41`) had no brief in `docs/reviews/` when this was written.
