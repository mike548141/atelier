# Data protection — the one you never get back

Protecting data — the owner's and other people's — sits at the top of the
precedence ladder (rule 1: protect the estate). A lost byte you can't recover
outranks any missed feature, any deadline, any elegance. Code can be rewritten;
data that's gone is gone. This doc is that principle made operational — and it
is the restore case of the posture principle (engineer for the failure being
cheap; exercise the recovery), whose canonical statement is
[`PRINCIPLES.md`](PRINCIPLES.md) §10; this doc carries the case, not the rule.

## Read before write, everywhere

Look at what's actually there before touching it. If it contradicts what you
expected — a file you were told was stale but isn't, a dataset with more in it
than the task implied — **stop and say so**, don't proceed on the assumption.

## A verified way back — before any destructive or irreversible op

Before deleting, overwriting, moving-that-loses-the-original, truncating,
dropping, or reconfiguring in a way that can lose data:

1. **A restore point must exist** — snapshot, backup, dump, or object-version.
2. **It must be verified** — confirmed present *and* confirmed restorable, not
   assumed. "There's probably a backup" is not a restore point.
3. **Only then act.** The way back is built *before* the way forward, not after.

Snapshot-first where the platform offers it: **ZFS/filesystem snapshots**,
**DB dumps**, **object-store versioning**. Taking a fresh snapshot immediately
before a risky op is cheap; it is the difference between "undo" and "gone".

## Where the act is irreversible, a report is not evidence

**Where an action cannot be undone, a tool's own report is not sufficient
evidence for it: corroborate from the artefacts.** Narrow on purpose. "Distrust
your tools" would be ignored within a day, and should be; this binds only at
the irreversible act, where the cost of a wrong report is the data.

A tool's report can be corrupted independently of its work (`EVIDENCE.md` §14
makes the same point from the side of the tool you built). The case that earned
the rule: a large deletion was authorised by a verdict tick that a corrupted
process had printed. The check that caught it was re-deriving the result from
the manifests on disk (five digests recomputed, the raw diffs re-run) instead
of reading the run's own summary. The two agreed; they did not have to, and the
rule exists for the gap between those two sentences. Two of the three
instances in that session were found only because the owner asked for evidence
he could check rather than accepting a verdict.

**Never overwrite an executable that a running invocation is reading.** Write
to a new path and rename over it, or version the filename. Bash reads a script
by byte offset, so replacing the file underneath resumes execution at an offset
that now lands mid-token, and the process keeps going and keeps printing. The
rename is atomic; an in-place write is not.

Mike adopted both on 2026-11-09 as data-integrity doctrine (board item
`370/010`; his pick from options offered, an answer, not a ruling in his
words). **No scanner:** there is no grep for "this output came from a
corrupted process". The write-then-rename convention belongs in whatever
governs how a tool is written, and a tool that rewrites itself or a sibling
script should follow it. See also `EVIDENCE.md` §18 (a negative needs a
positive control), which covers the opposite failure, a report that is empty.

## The data plane is the slow lane

Broad autonomy grants (commit/push/PR, and any per-domain write grant) **do not
extend to destructive data-plane operations**. Those are always-confirm +
verified-restore-first, regardless of how broad the grant is. Adding data is
routine; removing or overwriting it is gated. A domain that holds real data
(a NAS, a Drive, an object store, a production DB) keeps this narrower posture
even when its owner has granted broad write — the grant buys capability, not a
licence to lose data.

**Enforce the plane split with the credential, not with discipline.** Where a
system separates data from control, take **two scoped credentials** — a *data*
credential (read/write to the data, bound by the restore-before-destructive
gate) and a separate *control/config* credential that **cannot touch the data at
all**. Then a mistake in the control plane physically can't lose data — the
boundary is in the token's scope, not in an agent remembering to be careful.

## Reproducibility is data insurance

Anything rebuildable from code (containers, VMs, config, derived artefacts) has
a second life — losing it costs minutes, not data. Prefer reproducible state so
that the *irreplaceable* set is as small as possible, and guard that small set
hardest. (This is the reproducibility principle pointed at data specifically.)

## Other people's data is not yours to risk

Third-party and personal data (a client's records, PII in a mailbox or a session
transcript) carries privacy and retention obligations (e.g. the NZ Privacy Act).
Hold the minimum, never widen its exposure, never move it somewhere less
protected, and honour deletion/retention. "Protect data — mine *and others'*"
is the whole rule, not half of it.

## Encode it, don't just remember it

A "never delete X" or "snapshot before Y" rule that lives only in a session's
memory protects nothing — the next session never saw it. Move it into a gate,
a check, a script, a schema. The restore-before-destructive step should be
something the tooling enforces, not something an agent has to recall. (See
AUTONOMY "who acts": policy in memory protects nothing.)
