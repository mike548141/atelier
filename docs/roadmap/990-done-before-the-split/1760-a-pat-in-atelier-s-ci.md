- [x] **A — PAT in atelier's CI.** True continuous enforcement, catches drift
      within a day, no human in the loop. Cost: a read token spanning the whole
      private estate, living in the **public** repo's secret store. GitHub does
      withhold secrets from fork PRs, so it is not trivially stealable, but it is
      the largest concentration of the four. Needs rotation discipline.
      *(Not chosen 2026-07-28: B is strictly better for the same outcome.)*
