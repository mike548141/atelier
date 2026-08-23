# 🎭 The report can lie while the work is fine — 2026-08-23

A tool's **output channel** can be corrupted independently of the **work it
reports on**. When that happens the artefacts on disk are correct and the message
on the screen is not — which is the one failure mode no amount of care about the
*work* will catch, because care about the work is exactly what produced the good
artefacts.

Six instances across two docker-heap sessions on one day, found the hard way,
each with a different mechanism and the same shape — and the sixth is the
checker written to enforce *this item*, which failed the same way within the
hour of the fifth being filed (`030`):

| what broke | mechanism | what it printed |
|---|---|---|
| a credential diagnostic | `python3 - <<PY` — **a heredoc replaces stdin**, so the piped secret never arrived | a real `401`, from an empty password |
| a long-running script | **`scp` over the file while it was executing** — bash reads a script by byte offset, so it resumed mid-token | `✅ Photos is proven` followed by `syntax error near unexpected token ')'` |
| a compose dump | `$$` rendering in `docker compose config` | a value that looked wrong and was not |
| a gateway check | its filter selected addresses **longer than 15 characters** — and a *correct* IPv6 gateway is shorter, so the check could only ever display the broken form | `no v6` for all thirteen networks, nearly reported as success |
| a self-restart **guard** | two copies of one tool held **different internal names**, so the guard's own exclusion strings matched neither | nothing — it reported no job to exclude, and would have killed a live 366 GB transfer |
| the **corroboration check** written for this very item | `sha256sum` on an **absent** manifest wrote to stderr and left the digest empty — on both sides, so empty equalled empty | `IDENTICAL` for a dimension it had never read |

🔑 **The last three are the sharp ones and they are one sentence with the noun
changed.** *A verification that cannot display the passing state is not a
verification* → **a guard that cannot recognise the state it exists to detect is
not a guard** → **a check that cannot distinguish "the same" from "nothing at
all" is not a check.** All three fail by being quiet, and in each the
instrument's blind spot is exactly the condition it was built for. `020` carries
the guard case, which is the harder of the three because a guard has no reader
to corroborate it; `030` carries the check, which is the most damning because
its author was holding this item in mind while writing the defect.

🔑 **The danger is asymmetric, and both directions cost.** A false *failure*
sends you hunting: the first case above produced a confident, published finding
that the owner's secret store did not match its database — with an evidence table
— and cost an hour before he disproved it in one line. A false *success* is
worse: the second case printed `proven` for a 348 GB folder whose original was
about to be deleted, and it was only not acted on because the artefacts were
checked separately.

## The rule that would have caught the report cases — and the one it cannot reach

**Prefer artefacts over reports.** A report is a *claim*; an artefact is
*evidence*. Where they disagree the artefact wins, and where only a report exists
that is a gap rather than a result. This is the apex rule — *never a claim
stronger than its evidence* — applied to the tool's own voice, which is the place
it is least often applied because the tool feels like a witness rather than a
claimant.

In the `Photos` case that is precisely what saved it: the verdict was re-derived
from the manifests on disk — five digests recomputed, raw diffs re-run — rather
than taken from the run's own `✅`. The two agreed. They did not have to.

⚠️ **It reaches five of the six, and stops at the guard.** Corroboration needs a
*reader* — someone holding the report against the artefacts — and a guard's whole
purpose is to fire when nobody is looking (`020`). And `030` is the reminder that
the corroborating instrument is itself a tool with an output channel: the rule
does not discharge until that instrument has been shown a known-bad input and
seen to say so.

## The cheap preventions, one per mechanism

- **Never overwrite an executable a running invocation is reading.** Write to a
  new path and swap by rename, or version the filename. One line, and it removes
  the byte-offset class entirely.
- **Prove the harness carried what you think it carried** before drawing any
  conclusion from it — hash what you sent against what you meant to send, assert a
  length, check a precondition. Sits directly beside roadmap `350`.
- **Treat an unexpected exception as UNDIAGNOSED, not as evidence.** The heredoc
  case had already *succeeded* on its first attempt and died unpacking the
  response; a crash-on-success was read as a failure and chased for an hour in the
  wrong direction.

## ⚠️ What this is not

It is not an argument for distrusting tools generally, and a rule phrased that way
would be ignored within a day. It is narrower: **where an action is irreversible,
the report is not sufficient evidence for it.** Deleting 348 GB on the strength of
a `✅` is the case this exists to prevent. Reading a progress line and believing it
is fine.
