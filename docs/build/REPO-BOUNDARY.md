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
is only hypothetical; let the real need draw the boundary.
