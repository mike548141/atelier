- [ ] 🔎 **Defects the enforcement census found in slice 6.** Found
      2026-11-23 UTC by `020/220` slice 6
      (`docs/method/census/2026-11-23-1730-build-boundary-standard-templates-root-files.md`);
      reported, not fixed in passing.
      1. **Two CI templates declare no `permissions:` block**
         (`ci-python.yml`, `ci-static.yml`), so a child seeded from them
         runs with the repository's default token permissions; the floor
         workflows declare `contents: read` and a test pins it. A security
         gap in what children copy, not only a wording one.
      2. **`docs/build/README.md`'s contents list is stale**: it names
         `tools/linkscan.py` where `check_links.py` ships, omits the
         `SECURITY.md` template, and says "both CI workflows" over three.
      3. **`REPO-STANDARD.md`'s `floor.yml` bullet describes the retired
         scaffold**, and its man-page sentence says atelier's instrument
         tests pin the flag superset where 2 of 10 do.
      4. **`SECURITY.md` says the repo takes no third-party dependencies**,
         broader than `tools/README.md`; `instruments/browser-fetch` pins
         two under ADR 0006's addendum.
      5. **Root `CLAUDE.md` lists "a plugin/skills bundle" as the next
         widening** while `README.md` says it is already packaged.
      6. **Root `README.md` is stale in four places**: the STORAGE line,
         the Status paragraph, the skills list and the structure table.
      7. **The template `floor.yml` carries a clause dated 2026-12-09** that
         turns false in every child's copy on that date, with nothing to
         re-stamp it.
      8. **Atelier declares no repo type**, so its missing
         `ARCHITECTURE.md` and `CONTRIBUTING.md` read the same as a sizing
         choice.
      ✅ **Items 1–4 and 6 fixed 2026-11-23** (queue run 608d8123, a Sonnet
      worker, read by the run before landing; full tools suite green,
      3443 tests). 1: both CI templates declare `permissions: contents:
      read` (no job needs more), and `WorkflowLeastPrivilegeTest` pins the
      block in every template and every atelier workflow. 2: the build
      README names `check_links.py`, the `SECURITY.md` template and three
      CI workflows. 3: the `floor.yml` bullet describes the thin caller of
      the reusable floor (ADR 0008); the man-page sentence counts six of
      nine instruments pinning the flag superset (the census's "2 of 10"
      did not match the tree). 4: `SECURITY.md` scopes the claim to
      `tools/` and names the `browser-fetch` exception. 6: the root README
      in its four places. Cold pass queued as `160/1760`. **Still open:**
      5 (root `CLAUDE.md`'s widening sentence, which is the principal's
      autonomy floor: his word), 7 (a dated template clause, wants a
      design) and 8 (atelier's repo type, a choice).
      *Item 5 withdrawn 2026-11-23 ~19:40 UTC (run 608d8123):* on a second
      reading it is not a defect. The sentence is a rule about who may
      widen publication (announce, publish a package, distribute a plugin
      bundle), and it still reads true with the plugin's files in the
      repo; put to the principal twice, the question did not make sense to
      him, which is the run's failure to frame it, not his.
      ✅ **Item 7 fixed 2026-11-27 UTC** (queue run 9c5fa72c, an Opus 5.5
      worker). The child `floor.yml` template now states the sizescan bar
      undated and says the start date lives in atelier (`tools/floor.py`,
      explained in `docs/method/GUARDS.md`), with the floor's own line
      naming it until it starts: true before and after the date, so no
      copy needs a re-stamp for it. The bar, its date and its behaviour are
      unchanged. `TemplateSetCarriesNoFutureDateTest` in
      `tools/test_templates.py` stops the class coming back: no ISO date in
      the template set may be later than today (UTC), so it never reds on
      its own as the clock moves; it failed on the old text and passes on
      the new. Children seeded since `be217b1a` (2026-11-09) still hold the
      old comment, which is a comment only (the bar runs from atelier's
      registry); a copy changes only when its file is re-copied, and no
      sweep step re-copies `.github/workflows/floor.yml` today. No child
      was edited.
      review: not warranted — a wording correction that adds or changes no
      rule (the bar is `GRD21`, already reviewed under `160/790` and
      `160/340`), plus a tightening test that reds loudly on misuse; its
      only quiet miss, a dated clause whose date has already come, leaves
      the set exactly as it was before the test.
      **Still open:** 8 (atelier's repo type), a choice for the principal.
