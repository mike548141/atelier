# REPO-BOUNDARY — is this a repo, a component, or a folder?

`REPO-STANDARD.md` says how a repo is shaped. This says **whether a piece of work
should be its own repo at all** — the decision that comes *before* the standard.
Getting it wrong is expensive both ways: a repo split too fine drowns real work in
scaffolding ceremony; a repo that should have split becomes a tangle nothing can
be released or reviewed independently.

**Standing behaviour: advise proactively.** When a new piece of work appears —
a tool, a client engagement, a spike, a service — say which boundary it wants and
why, before scaffolding anything. Don't wait to be asked; the boundary is the
first design decision, not an afterthought.

## The test: what has an independent lifecycle?

A repository is a **unit of independent lifecycle** — independent version
history, release cadence, review, access/visibility, and licence. The question
is never "is this a lot of code" but "does this thing version, ship, get reviewed,
and get *seen* on its own clock?" (This is loose-coupling / Unix-composition from
`method/PRINCIPLES.md` applied to the repo boundary itself.)

Run these discriminators; the strongest one usually decides it:

- **Visibility / audience** — does part of it go public (or to a client) while
  part stays private? A visibility seam is the hardest boundary to fake inside one
  repo; it usually *forces* a split (the private-first default and the
  publish-is-a-floor-action rule, `method/AUTONOMY.md`, make a mixed-visibility
  repo a standing hazard).
- **Release cadence** — does it ship on its own schedule, or only ever as part of
  something else? Independent release → its own repo.
- **Ownership / access** — different people, different `gh` account, a client's
  org rather than yours? Ownership boundaries are repo boundaries. (Never
  reshape a repo you don't own — `REPO-STANDARD.md`.)
- **Reuse** — is it consumed by more than one other thing? A shared library that
  two projects depend on wants its own versioned home; a helper only one project
  will ever call does not.
- **Blast radius / lifecycle divergence** — will it outlive, or die before, its
  neighbours? Things that are born and retired together belong together.

If none of these fire, it is **not** a repo yet. Prefer the smallest boundary
that still satisfies the ones that do fire.

## The three shapes

**Standalone repo** — when the discriminators fire: its own visibility, its own
release, its own owner, real reuse, or a lifecycle that diverges from everything
around it. This is the default for a genuine project or a shared library. Apply
`REPO-STANDARD.md` in full, sized to type.

**Component (folder in an existing repo)** — when it shares the parent's
lifecycle: same visibility, ships when the parent ships, same owner, consumed only
by the parent. This is `REPO-STANDARD.md`'s product-in-a-subfolder rule doing its
job — a component is just another subfolder under a root whose scaffolding it
shares. Don't mint a repo for something that has no independent clock; the
ceremony is pure overhead.

**Monorepo folder (a repo deliberately holding several products)** — when
multiple related products share *tooling, review, and access* but each is a
distinct deliverable. Justified by a **shared operational surface** (one CI, one
doctrine block, one access boundary) across pieces that are individually
meaningful. The classic case is a **rich client engagement**: several
deliverables for one client, one private boundary, one review cadence, delivered
together — one repo, one folder per deliverable, each folder following the
product-in-a-subfolder discipline. The trap is the *accidental* monorepo — things
piled together for convenience that actually have divergent visibility or
cadence; if a folder wants to go public or ship on its own clock, it has already
outgrown the monorepo and should split.

## When it's genuinely ambiguous

Prefer the **reversible** direction. Splitting a folder out into its own repo
later is cheap (`git filter-repo`/subtree, history intact); merging N repos that
should have been one is painful (history reconciliation, cross-repo change
choreography). So when the discriminators are balanced, **start as a component or
monorepo folder and split when a discriminator actually fires** — not on
speculation that one might. Don't pre-split for a reuse or a public release that
is only hypothetical; let the real need draw the boundary. And when one *does*
fire, split **promptly**: the cheapness of splitting decays as a folder accretes
cross-references, its own CI, and a doctrine block — deferring a fired
discriminator is how the accidental monorepo above actually forms. How to
split is the last section, below.

## Splitting a repo — how, once a discriminator has fired

*Added 2026-11-09 from `320/580`, as a draft of what could be grounded and no
more; Mike's pick from options offered, so an answer and not a ruling in his
words. Class only: the evidence is two splits a private child summarised by
shape in a hand-up of 2026-10-11, and the detail stays in the children's
private records. Every element below is that hand-up's testimony. atelier has
not re-driven it (`PROPAGATION.md` § Pointing up: a hand-up's mechanism claim
is re-driven before it becomes house text), so read this as a checklist to
test against the next split, not as a settled method.*

**The two splits.** A tool moved out of a private engagement repo into a new
public repo, over about two weeks, recorded as done. Estate data moved out of a
product repo into the estate root, begun months earlier, stalled behind other
work, and re-planned by studying the first. The first's lessons are reported to
have transferred almost one for one, which is why one section covers both.

**What the first split developed, and the second reused:**

1. **State the bar and the capability list before the first move.** What the
   split must achieve, and what the new home must be able to do.
2. **A four-line routing test, placed in every onramp a session on either side
   reads** (the user-global one too, when one side may not name the other). It
   came from the private side, so it goes private. It is generic and written
   with synthetic examples, so it goes public. It is both, so split it and
   never carry the motive across. Unsure goes private.
3. **Records never cross, however well cleaned.** Session logs, history, board
   items and decisions stay with the side that made them.
4. **One home per fact, one direction of flow, never fork.** A change the new
   repo needs is made upstream, not in a local copy.
5. **Build the guard first and prove it fails.** A guard that skips silently
   when its data is absent is the defect both splits hit (compare `320/230`).
   One was found only because the second split studied the first, before the
   deletion that would have exposed it.
6. **Judge by meaning; keywords back it up.** The gate's first layer is a read
   for meaning, attested by hash, with token lists as a backstop only.
7. **Migrate in measured stages, and a moved result stops the stage.**
8. **Give every temporary bridge a dated delete-item.**
9. **Rename refuse-first**, with a script that also copies the assistant memory
   keyed by path, so the move does not orphan it.
10. **Cold reviews at stage boundaries.**
11. **A handoff file with a "settled, do not re-ask" list**, so a fresh session
    does not reopen a ruling.

**What the principal had to correct, so it is not re-learned:** keywords
used where meaning was needed (three times in the first split), forking where
upstreaming was needed (twice in four minutes), a settled ruling asked again,
and the silent-skip guard above.

**What could not be grounded here, and is therefore not written.** The
hand-up names the gate's first layer and says nothing of its others, or of the
token-list format. It gives no sizes for the stages and does not say what
"measured" measures. It does not say when the rename refuses, what the handoff
file's fields are, or where a stage boundary falls. Items 1 and 11 are
headings, not contents: the bar and capability list were not itemised. How a
split of data differs from a split of a tool is unknown, since the second is
unfinished. The extraction from the children's private records, and its cold
review, are owed before this section is more than a checklist.
