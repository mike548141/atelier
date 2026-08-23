# 🔐 Where the failure is data loss, verification must be exact — Mike-commissioned, 2026-08-23

His words, on an agent that had built a data-integrity check comparing the first
16 hex characters of a SHA-256 and then argued the residual risk away:

> *"assumptions like '64 bits is still far past accidental collision on manifests
> this size' are not acceptable when we are talking about potential for data
> loss… I need you to understand that I consider that unacceptable in all future
> endeavours."*

**Pointed up from docker-heap**, where a `zfs`-dataset split was verifying ~25 TB
of media by comparing manifests of per-file SHA-256 digests. The tool truncated
the rolled-up digest to 16 hex characters *before comparing* — so every verdict
it printed as a SHA-256 comparison was decided on 64 bits of a 256-bit hash. The
agent found and fixed it, and then defended the window in which it had shipped by
estimating the collision probability. **That estimate is the thing he is
objecting to, not the bug.**

## Why this is a doctrine question and not a bug report

The estimate was probably even correct. That is exactly what makes it worth
filing: the agent was not wrong about the arithmetic, it was wrong about what
kind of argument was admissible.

🔑 **A probability is a model. The apex asks for evidence.** "Never a claim
stronger than its evidence" is already house doctrine, and a collision-likelihood
argument is a claim whose backing is a model of the world rather than a
measurement of it. Where the downside is bounded and recoverable, reasoning from
a model is ordinary engineering. Where the downside is **irreversible** — a
deletion authorised by the check — it is a substitution.

🛑 **And here the exact option was FREE.** Comparing 64 hex characters costs
exactly what comparing 16 costs. Nothing was traded for the risk; a display habit
had leaked into the comparison and the risk was then rationalised after the fact.
**When the safe option is free, "the residual is negligible" is not a reason. It
is a rationalisation of an accident.**

## What it should NOT be read to say

⚠️ Probability cannot be banished from verification and a rule that pretends
otherwise will be ignored the first time it collides with reality. SHA-256 is
*itself* a probabilistic guarantee; so is every checksum, every hash-based
comparison, every sampling strategy.

The defensible line is narrower and it is about **self-inflicted** discounting:
**use the full strength of the primitive you chose, and do not weaken it by your
own hand.** Choosing SHA-256 and then comparing a quarter of it is not accepting
the residual risk of SHA-256 — it is inventing a new and much larger one, and
labelling the output with the name of the stronger thing.

## The three corollaries worth having, if this becomes a rule

- **Exactness over estimation where the failure is irreversible.** Do not argue a
  residual risk down; remove it, if removing it is possible at all.
- **If exactness is genuinely impossible, the residual belongs in the OUTPUT the
  person reads — not in the author's head.** A check that carries a known
  limitation and says so is honest. One that carries it silently is not, however
  small the number.
- **A display convenience must never touch the comparison.** Truncate, sample and
  abbreviate for the reader as much as helps them; compare in full. The two
  concerns look alike and are not, and conflating them is precisely how this
  defect arose.

## The related items

This sits beside `330` (SHA-2 or better for every hash) and `340` (long-running
operations need a way back), both also pointed up from the same docker-heap job.
330 governs *which* primitive; this governs *not discounting it afterwards*. They
are worth deciding together — and probably worth living in the same place, since
a reader who needs one needs the other.
