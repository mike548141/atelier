# 2026-07-12 · session 48 — communication UX refinements + the close-ready signal

Conversational session, Opus 4.8 (1m). Mike gave two threads of calibration
feedback and one direct question about a behaviour drift.

## What Mike asked

1. **Widen the verdict-icon vocabulary** beyond ✅❌⚠️ (he'd liked a 🎉 once),
   and make actions/decisions/awareness-items **visually obvious** — something
   that draws the eye. He endorsed the guardrail I offered back: *an apt icon is
   signal, an overused one is noise*. Quote boxes help too. Also flagged that
   replies had been running **text-heavy and jargon-laden** — terms he doesn't
   know. Asked where this should live; suggested atelier communications.
2. **Declare when work is wrapped.** After a run of work, the tidy-up should be
   done and he should be told it's ready to close — he shouldn't have to ask
   "are we done?" before closing the session. Noted this *used to* be default
   and **changed in the last day or so** — asked what caused it.

## What was decided and done

**The drift, diagnosed honestly.** `RECORD.md` mandated the session-log
*artifact* but never the *close-ready signal* — so the behaviour ran on soft
habit and slipped after a model change (opus[1m] this session resets in-context
defaults). No single switch to blame; the fix is to encode what was only habit.

**Placement — both layers, per COMMUNICATION.md's own practice/instance split:**

- **atelier `method/COMMUNICATION.md`** (shareable practice) — Visual-structure
  axis extended: don't ration the icon vocabulary (🎉 🎯 🚩 examples) under the
  apt=signal/overused=noise guardrail; surface act-on items in an eye-catching
  device *apart from the reasoning*. New **Accessibility-of-language** axis:
  unfamiliar jargon or a prose wall costs a reread exactly as a missing
  colour-glyph does. Scrubbed worked example updated to match.
- **atelier `method/RECORD.md`** — session-log section: "Write it before
  finishing — **and declare the close**." Full tidy-up unprompted + say so;
  mid-run questions always fine; grounded-2026-07-12 drift note included.
- **global `~/.claude/CLAUDE.md`** (the personal instance, not this repo) —
  plain-over-jargon clause on Format; a "Signal when work's wrapped" bullet;
  the earlier icon-palette + action-callout bullets from this same day.
- **memory** — `verdict-icons-and-action-callouts` extended (jargon + quote
  box + atelier-doctrine note); new `session-close-declare` feedback memory.

No cold review owed — these are maintenance edits the COMMUNICATION.md doctrine
itself prescribes ("maintain it like a record; write calibration back, dated"),
not new doctrine surface. No personal context entered the public repo.
