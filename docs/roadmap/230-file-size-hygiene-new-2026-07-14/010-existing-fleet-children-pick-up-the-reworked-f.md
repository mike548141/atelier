- [ ] **Existing fleet children pick up the reworked `floor.yml` gate** — children
      copy `floor.yml` statically, so they adopt the cold-content gate at their
      next pin bump / harvest. **At the same bump, apply the 2026-07-23 trigger
      ruling (Mike): private children that take no fork PRs drop the
      `pull_request` trigger** — halves metered-minute burn; the merge-preview
      scan is consciously traded away where the owner is the only contributor;
      public children keep both (free). They also inherit the SHA-pinned
      actions + the SECURITY.md template from the security-canon close, **and the
      new docs-scoped `datescan` blocking step (added to the template 2026-07-23
      on Mike's flip ruling) — a child RE-BASELINES its records first (ISO-fix or
      `datescan:allow` the genuine breaches; that first red is the signal) and
      adjusts the path if it keeps records outside `docs/`.** **The rebalance dissolves the all-open-roadmap
      red**: a wholly-open ROADMAP (ros's ~125 open items) no longer reds on
      length — with no cold content to relocate it is advisory now, not a standing
      red — so the class-grounded-budget workaround is no longer needed for that
      case. A child that still reds does so on un-harvested `[x]` items, its own
      harvest lane. faves and ros run bespoke CI without `sizescan --check` — a
      separate floor-adoption step.
      **At the same bump, untrack `.claude/settings.json`** (Mike's 2026-07-29
      ruling ⓑ, Sharing § Publication surface): `git rm --cached` it and take
      the reworked ignore lines from the template. **Eleven children track it**
      (swept 2026-07-29, not estimated: Baby Brain, FoodTracker, docker-heap,
      ec2_builder, hitchbots_guide, homenetwork, kainga, nova, numen, ros,
      shed); `rpi` and atelier are done. On a private child this is latent, not
      live — which is the point of doing it before any flip rather than during
      one. `publishscan` reds each of them the moment they take the registry,
      so a child that cannot clean up in the same bump declares it **advisory
      with a `why` and a `review-by`** rather than being blocked mid-work.
