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
