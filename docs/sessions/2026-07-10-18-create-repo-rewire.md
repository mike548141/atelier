# 2026-07-10 · create-repo rewired to inherit; templates moved into build/ (Opus)

The first stack on the cleared batch-review gate: the core Q1 fix. `create-repo`
was a *second source* of the repo standard — it re-encoded the file set, sizing
table, product-in-subfolder rule and processes from memory, alongside a private
`templates/` copy. Two sources drift. This session made the skill a pure
**delivery vehicle** over atelier as the **source**, and closed the two coupled
"owed" items (templates-move + rewire-to-inherit) in one pass.

## The keystone gap

The skill had **no CLAUDE.md template at all**. So every repo it scaffolded was
born with no inlined safety floor, no pointer up to atelier, no SHA pin, no drift
check — the entire `PROPAGATION.md` mechanism bypassed at the one moment it's
cheapest to install. A repo that inherits docs but not the doctrine block has
inherited the costume, not the doctrine. Fixing this was the point of the rewire,
not a side effect.

## What changed

**In atelier (the source):**

- **`docs/build/templates/`** populated (18 files) — moved from the skill's
  private copy, per REPO-STANDARD's already-decided direction. Added the missing
  **`CLAUDE.md`** template carrying the standard doctrine block (a *stamped copy*;
  canonical text stays in PROPAGATION.md, noted in a header comment so a future
  pin bump re-syncs it).
- **Scrubbed three instance-residue leaks** as the templates crossed into the
  shareable repo (atelier's whole reason to exist is that boundary): `NOTICE`
  copyright holder was hardcoded to a company → `<copyright holder>`;
  `ci-static.yml` opened "CI for Nova" (a project name) → generic; `reviews/
  README.md` used faves-specific examples (physics, DeviceOrientation/iOS) →
  type-neutral.
- **One live drift caught** — the grounding evidence that one-source is right,
  not just tidy: the `MODEL-ECONOMICS` template still named **ros** as the
  canonical fuller version, months after MODEL-ECONOMICS was extracted to atelier
  as canonical (session 11). A second copy had already drifted from the first.
  Fixed to point up to atelier.
- **REPO-STANDARD.md + build/README.md** moved from "owed" to done: templates
  live in `build/templates/`; the skill *inherits + stamps* rather than
  re-encodes; the seed→rename→fill→stamp→scan→push procedure and the dotfile
  renames (`gitignore`→`.gitignore`, `claude/`→`.claude/`,
  `workflows/`→`.github/workflows/`) documented.

**In the skill (machine-local delivery vehicle, `~/.claude/skills/create-repo/`):**

- Rewritten to **point up** to atelier (REPO-STANDARD, REPO-BOUNDARY,
  PROPAGATION, `build/templates/`) instead of restating them. Carries only the
  instance-local specifics a shareable doc must not: exemplars (ros/faves/rpi),
  git identity, `gh` account + private-default, `$PP`, default copyright holder
  (Competitive Edge Limited), NZ-English locale.
- **Stamp step made first-class** (step 5): fill the four doctrine-block
  placeholders — `<atelier-path>`, `<SHA>` via
  `git -C "$PP/atelier" rev-parse --short HEAD`, `<owner/repo>`,
  `<visibility fact>`. Plus a scan-hook wiring step (leakscan + secretscan).
- **Precondition stated honestly**: the skill hard-depends on `$PP/atelier` being
  present and **stops** if it is absent, rather than scaffolding wisdom-empty from
  memory — the exact failure this rewire exists to kill.
- Its private `templates/` removed (content preserved + pushed in atelier first),
  so there is one source, not two.

## Verification

Residue grep across the new template tree clean; `leakscan docs/build/templates/`
clean (structural + local). The stamp **mechanical core was dry-run-proven** in a
scratch scaffold (not a real repo): seed-from-templates + the three renames, sizing
dropped the unused CI, all four doctrine-block placeholders filled, and the
stamped drift-check ran verbatim and correctly read "current" (pin == HEAD); no
doctrine-block placeholder leaked. **Still owed**: a real-repo run (`gh repo
create`, the scan-hook install, a first commit) and a Fable sweep of the delivery
mechanism. Review-owed like the rest of the post-gate work.

## Close

Two coupled ROADMAP items closed (rewire + templates-move). The build/ layer's
"still owed" list is down to the deferred supply-chain/release standard. Next
natural stack: exercise create-repo on a real scaffold to prove the stamp, or
pick up the batch-review backlog (ros access map; REVIEW.md live-proven-re-run
line). ros pin unchanged (`f72031c` — no method/ change this session).
