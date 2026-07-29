# Session — the floor's posture, and seventeen rulings

- **Date:** 2026-07-29, 0637 UTC (work began 2026-07-28 ~2300 UTC)
- **Model:** Opus 5 (1M context), inline on `main`
- **Ask:** a full list of open work and open decisions, then a walk-through of
  the queued review verdicts

## What happened

Mike asked for the whole board in plain language, then for a walk-through of the
thirteen finished review passes sitting unruled. Batch 1 — the four passes that
closed with no MAJOR — was walked through with per-option impacts in prose and
the choice carried in a popup, per his standing preference. Fourteen findings
ruled, then three more, then three more again as his own correction widened.

## The rulings

**Batch 1 (14 findings, `7422f2a`).** TAA1–TAA3, C1F1–C1F3, ER1–ER4, SF1–SF4.
Twelve accepted as counselled. Two departed and are recorded with grounds: TAA3
held for a third instance (reviewer's counsel and the >2 promotion rule agree),
and C1F2 adds the day count to the floor line rather than correcting the record
to say board-only.

**E6 (3 rulings, `0e58850`), and the correction that produced it.** Explaining
SF2 to Mike, I described the `SLUG_RX` letters-only narrowing as "a documented
decision now being put to you". He rejected the premise: limiting it that way was
never his intention, and he stated the floor's purpose plainly — find every
secret, credential, private key and piece of personal data, so none of it reaches
a public or insecure place, while acknowledging the hard part is that some of what
looks like a secret is an example, random text, a file hash, or a hex rendering of
data.

Looking for where that intent was written down found two things neither of us
knew:

- **The two boundary scanners hold opposite postures and nothing records the
  difference.** `leakscan` states over-flagging as fail-safe in its own source.
  `secretscan` states no posture and its docstring sells the reverse. The scanner
  guarding personal data over-flags; the scanner guarding credentials
  under-flags. No record shows that being decided.
- **`secretscan`'s `severity` field is decorative** — every finding blocks
  equally. That is the whole explanation for the narrowing: with one dial, the
  only way to avoid crying wolf on every git SHA is to shrink detection. So it
  was not a disagreement with the principal's intent; it was the only lever
  available, and it was recorded as a code comment where it never reached him.

**E6d (3 further rulings, this commit).** Mike then corrected the tier itself:
confidence alone is the wrong axis, because a mid-confidence hit on a credential
that opens the estate outranks a high-confidence hit on something insignificant.
Checking the code sharpened his point — the field called `severity` already holds
confidence, graded on how specific a *pattern* is, and it grades a Stripe live key
and a test key identically while the token states its own blast radius.

## Honest notes

**The account below is why the queued pointer carries none of it.** The `⏳`
pointer is refs only, per this file's own ceiling and the third instance of that
breach found by a parallel session the same day.

- **Two flags I raised against my own recommendations, both unresolved and both
  for the reviewer rather than for me.** First, `leakscan` has no advisory form
  *by design* — a standing decision. My argument that E6b's advisory tier does not
  weaken the gate is that the blocking set is unchanged and everything new is
  coverage that did not exist. That argument sounds right and is exactly the shape
  that has been wrong in this repo before. Second, impact is least knowable
  precisely where it matters most: a shared scanner can class a vendor credential
  by construction but cannot know what a home-grown assignment opens.
- **I gave Mike a crossed explanation and he caught it.** Presenting SF1+SF2 I
  said both "the recent fix caused this" and "this is a pre-existing hole", which
  are both true of *different spellings of the same value* and read as
  contradiction. He paused the ruling rather than accept it. Re-explained from a
  live six-shape probe instead of the verdict's summary; the probe also falsified
  a reassurance the triage record still carries.
- **A ruling was recorded before the work that follows from it.** Batch 1 was
  committed mid-walk-through rather than at session end, because fourteen rulings
  living only in a transcript is the state-tracking failure this programme
  records.
- **The board I gave Mike went stale inside the hour.** A parallel session landed
  nine commits on Track B while we talked — B1 ruled and built, B2+B3 landed, B4
  built and shelved. Three items on the list I had just handed him were already
  answered. Flagged to him rather than left to be discovered.
- **Not swept:** whether `leakscan` reaches the personal-data half of Mike's
  stated intent as well as `secretscan` reaches the credential half. He named PII
  explicitly; only the credential side was examined this session.

## State at close

Records-only throughout — nothing built, no behaviour changed. E6a–E6d are owed
and unclaimed. The E6 intent is queued for a cold review; batches 2 and 3 of the
verdict walk-through are unstarted.
