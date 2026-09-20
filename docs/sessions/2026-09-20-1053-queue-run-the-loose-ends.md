# 2026-09-20 · 1053 UTC — Queue run: the loose ends the last run named

**Tier:** Opus 5 (1M context) orchestrating, stated at open per `ECONOMICS.md`
§ *The orchestrated-run tier split* and the 2026-09-19 ruling; Sonnet 5 workers
in isolation worktrees.

**Onramp.** Tree clean, synced at `f85ab32`, no untracked files, no live claims
on the board. The 2026-09-19 run left a closing block in its own detail file, so
this opened on a clean close rather than an interruption — no recovery sweep
owed (`CONCURRENCY.md` § *Recovering after a cut*).

**Selection.** Loose ends and unblockers first, per § *Selecting the next item*.
The 2026-09-19 close named two live consequences of its own work (`020/400`,
`115/080`); `010/020` had been funded by Mike's BS1 ruling since 2026-08-17 and
never built. Claimed at `ed0b98a`: `020/400`, `010/020`, `020/160`. Claimed
separately at `3f55f54`: `020/390`.

## `020/390` — the scratchpad collision, measured rather than assumed

The item asked for the sharing to be **measured**, not assumed, before anything
was written. This run had three concurrent workers live, which is the condition
it names, so it was measured against them.

**What was measured, 2026-09-20 ~1057 UTC.** Subagent workers get **no scratch
directory of their own.** All three workers wrote into the orchestrating
session's single scratchpad — the same directory holding the orchestrator's own
files — with no per-agent namespacing at any depth. The dispatched E9 worker's
reproduction tree (`e9-repro/`) landed beside the orchestrator's own
`claim-msg.txt`. The git worktree isolates the repo; nothing isolates the
scratch space.

**The corroboration was accidental and is the better evidence.** The directory
every project's scratchpad hangs off holds loose files that outlive the sessions
that wrote them. Among them, written 1734–1926 UTC the same day:
`msg.txt`, `msgB.txt`, `msgD.txt`, `msgE.txt` — `msgE` being a commit message
about `020/380`'s stampscan work, so an earlier atelier sitting, not a peer. A
session suffixing B/D/E by hand is a session disambiguating inside a shared
namespace, which is what people do when the namespace will not do it for them.

**Two further files, `floor-canonical.md` and `floor-substituted.md`, were
written at 2256 and 2257 local — during the measurement.** Their content is the
inlined atelier doctrine block in canonical and substituted form, which is the
shape of the hand verification a child performs at a pin bump. **Attribution was
asked for over the channel rather than inferred**
(`dont-infer-mikes-setup-from-artefacts`), and the peer confirmed them as its
own, with a chain: a third file, `method-diff.txt` (72,319 bytes, 2255), landed
in that session's *correct* scratchpad one minute earlier, from the same worker,
and the canonical/substituted pair is 308 bytes apart in the direction filled
placeholders would produce.

**The peer's instance falsified the framing the item was drafted in, and that is
the run's most useful result.** Its worker wrote three files one minute apart:
the first into its own scratchpad, the next two into the shared parent. So this
is **not a namespace problem** — a worker does not reliably inherit its parent's
scratchpad at all, and the within-run and cross-project cases are one mechanism
at two radii. The draft clause ("a path unique to itself") would not have
described the failure that was actually measured.

**Delivered:** `CONCURRENCY.md` § *Orchestrated queue runs* gains a clause after
*What a worker inherits is bounded* — the worktree is the isolation, the scratch
space is not, so a dispatch prompt requires each worker to write scratch under a
path that is both **absolute and unique** to it. *Absolute* because a relative
write after a `cd` resolves against whatever the shell's cwd has become, a
hazard this estate has recorded three times and which recurred during this very
measurement. Written as a **prompt obligation, not a mechanism**, because the
scratch path is the harness's to allocate and not this repo's — the clause says
so, so it is spent rather than stale if the harness changes.

⚠️ **What this does not establish:** *why* the two files escaped. A cwd that
moved between the worker's first and second write is consistent with the
evidence and is not evidence. The hypothesis was handed to the peer, which alone
holds the transcript that could ground or kill it; the clause is written to hold
either way and says as much.

## The cross-session exchange with `kainga-9a`

A peer session opened a read-only orchestrated run against this tree pinned at
`f85ab32` and asked two questions; a third finding followed when invited.

- **BS1** — answered: ruled 2026-08-17, cycle **closed on the wording**, but
  `010/050` keeps its 🛑 on BS2–BS14 residue. The peer's item conflated the two
  and would have carried a stale block; it reported it would rewrite to track
  the residue. It also stood down from building the staged-plane check on being
  told `010/020` was claimed here — the correct child shape, and the duplication
  `PROPAGATION.md` exists to stop.
- **stampscan across a repo boundary** — answered: still received-and-open at
  `320/160`, nothing built or ruled. The peer's evidence covered obstacle 1
  only. It was asked to file the **sharper half that is its own**: if a
  compliant child reds by construction, hand verification is not a stopgap but
  the only instrument that can ever pass a compliant child — a claim about
  standing practice that `320/160` does not make, with a method and a cadence
  behind it. To be attached to `320/160` as a child's corroboration when it
  arrives.
- **fleet-rollout adopter inventory** — spent: the table has listed `kainga`
  (`c6e4479`, 323 → 103) since 2026-08-17. The peer's diagnosis was sound —
  under-counting is that item's own recorded defect class — it had simply
  already fired and been swept.

*Nothing was written to the peer's tree and nothing of the peer's was touched;
the two loose files above were read for measurement and left alone
(§ Stay in your lane).*

## `cbom-70` — PR #83, and an error of mine worth recording

A second peer filed PR #83 from a private child: `320/360` (a closure report
for `115/200`) and `320/370` (a declared placeholder with no admissible fill —
the floor's `Verify: gh repo view <owner/repo>` clause presumes a remote, and
that child has none). Both read in full before merge. Routing steered on three
points it acted on: split the two rather than fold the open finding into the
closeable one; rebuild the generated index on its own branch rather than leave
a shared-checkout habit to red its own PR; reserve `320/370` up front, because
two new files never text-conflict even when their numbers collide.

Its finding was **reframed rather than accepted as pitched**: it read the
defect as non-substitutability, but `<owner/repo>` is one of the four declared
placeholders, so that framing dies to a one-line rebuttal. The sharper true
claim is a declared placeholder with **no admissible fill** — doctrine that
looks satisfiable and is not. It verified both claims against the tree before
rewriting, and kept its first reading in the item marked wrong so nobody
re-derives it.

🛑 **I told that session its PR would red on wrapscan. It did not; the run
passed.** The reproduction was not comparable to the thing it claimed to
reproduce: I extracted the item into a scratch directory and scanned it there,
where there is no `.atelier-floor.json` to read, so it ran unscoped. The real
gate is scoped to `docs/method`, `docs/build`, `docs/decisions` by Mike's WS1
ruling, and `docs/roadmap/` is outside it by design. I checked the control
*after* telling the peer, which is the wrong order, and it cost that session
effort. The correction went out as soon as the run concluded, along with the
withdrawal of a false dilemma I had put to it about a hook/CI divergence that
does not exist.

**What the error bought, which is the only reason it is not pure cost.** The
same mistake explains an open item. `010/130` records a child blocked by
wrapscan on claim fragments, and reasons about the scanner's exemption logic.
That is not the discriminator: **atelier is immune by a local scope
declaration its children do not inherit**, so the parent cannot reproduce a
class its children meet on the most routine act the board asks for. Evidence
appended to `010/130`, including this session's own six-finding red hand run
against a green CI. The item's own recorded reproduction "here at HEAD" must
have been the same unscoped invocation — noted there rather than tidied away,
per the house rule that a defect quietly patched leaves nothing to count.
