"""Stdlib-only tests for spellscan (no pytest needed): `python3 -m unittest`."""

import unittest

import spellscan as ss


def scan(text):
    return ss.scan_text("t", text)


def matches(text):
    return [f.match for f in scan(text)]


def suggestions(text):
    return [f.suggestion for f in scan(text)]


class IzeFamily(unittest.TestCase):
    def test_bare_verb_flagged(self):
        self.assertIn("organize", matches("we organize the docs"))

    def test_inflections_flagged(self):
        self.assertIn("organizes", matches("it organizes the docs"))
        self.assertIn("organized", matches("it organized the docs"))
        self.assertIn("organizing", matches("it is organizing the docs"))

    def test_noun_capable_stem_flagged(self):
        self.assertIn("organization", matches("the organization of docs"))

    def test_irregular_noun_not_generated(self):
        # recognize's noun is "recognition" (irregular) — must not invent
        # "recognization"/"recognisation".
        self.assertNotIn("recognization", ss.DENYLIST)
        self.assertNotIn("recognisation", ss.DENYLIST.values())

    def test_synthesize_has_no_generated_noun(self):
        # synthesize -> synthesis is irregular and identical in both
        # dialects, so no noun form should be in the denylist at all.
        self.assertNotIn("synthesization", ss.DENYLIST)

    def test_hypothesize_jeopardize_penalize_have_no_generated_noun(self):
        # SS1 (2026-07-23 review): these three have irregular nouns
        # (hypothesis, jeopardy, penalty) — the docstring claims such stems
        # are excluded from IZE_NOUN_CAPABLE, but these three were left in
        # by mistake, inventing near-nonwords ("hypothesisation" etc). Fixed
        # by dropping them from IZE_NOUN_CAPABLE; the verb forms still fire.
        for noun in ("hypothesization", "jeopardization", "penalization"):
            self.assertNotIn(noun, ss.DENYLIST)
        for verb in ("hypothesize", "jeopardize", "penalize"):
            self.assertIn(verb, ss.DENYLIST)
            self.assertIn(verb + "s", ss.DENYLIST)
            self.assertIn(verb + "d", ss.DENYLIST)
            self.assertIn(verb[:-1] + "ing", ss.DENYLIST)

    def test_hypothesize_jeopardize_penalize_verb_still_flagged(self):
        # The verb `-ize`->`-ise` transform must keep firing even though
        # the noun form was dropped.
        self.assertEqual(["hypothesise"], suggestions("we hypothesize this"))
        self.assertEqual(["jeopardise"], suggestions("this could jeopardize it"))
        self.assertEqual(["penalise"], suggestions("don't penalize them"))

    def test_suggestion_is_ise_form(self):
        self.assertEqual(["organise"], suggestions("we organize this"))
        self.assertEqual(["synthesise"], suggestions("we synthesize this"))

    def test_case_insensitive_detection(self):
        self.assertIn("Organize", matches("Organize the docs first"))
        self.assertIn("Synchronize", matches("Synchronize the two lists"))

    def test_title_case_preserved_in_suggestion(self):
        self.assertEqual(["Organise"], suggestions("Organize the docs first"))

    def test_words_never_alternating_are_not_denylisted(self):
        # "size", "seize", "capsize" always use z in both dialects — never
        # on the stem list, so never flagged.
        self.assertEqual([], scan("the size of the seized, capsized boat"))


class YzeFamily(unittest.TestCase):
    def test_analyze_flagged(self):
        self.assertIn("analyze", matches("we analyze the data"))
        self.assertEqual(["analyse"], suggestions("we analyze the data"))

    def test_analyzed_analyzing_flagged(self):
        self.assertIn("analyzed", matches("it analyzed fine"))
        self.assertIn("analyzing", matches("it is analyzing now"))

    def test_analysis_not_flagged(self):
        # "analysis"/"analyses" (the plural noun) is spelled the same in
        # both dialects — never on the stem list.
        self.assertEqual([], scan("the analysis and its analyses are done"))


class StandalonePairs(unittest.TestCase):
    def test_artifact_flagged(self):
        self.assertEqual(["artefact"], suggestions("the build artifact here"))

    def test_color_family_flagged(self):
        self.assertIn("color", matches("pick a color"))
        self.assertIn("colored", matches("a colored pencil"))
        self.assertIn("colorful", matches("a colorful scene"))

    def test_behavior_flagged(self):
        self.assertEqual(["behaviour"], suggestions("odd behavior today"))

    def test_defense_flagged(self):
        self.assertEqual(["defence"], suggestions("a strong defense"))

    def test_center_flagged(self):
        self.assertEqual(["centre"], suggestions("the town center"))

    def test_catalog_flagged(self):
        self.assertEqual(["catalogue"], suggestions("browse the catalog"))

    def test_favor_and_favorite_flagged(self):
        self.assertIn("favor", matches("do me a favor"))
        self.assertIn("favorite", matches("my favorite colour"))

    def test_honor_flagged(self):
        self.assertEqual(["honour"], suggestions("an honor to be here"))

    def test_fulfill_flagged(self):
        self.assertEqual(["fulfil"], suggestions("we fulfill the order"))

    def test_fulfilled_and_fulfilling_not_flagged(self):
        # Identical spelling in both dialects — not on the denylist.
        self.assertEqual([], scan("the order was fulfilled by fulfilling it"))

    def test_license_deliberately_not_denylisted(self):
        # A documented judgement call (see module docstring): license/
        # practice are noun/verb homographs this scanner can't safely
        # split, so they're excluded entirely rather than flagged noisily.
        self.assertEqual([], scan("a software license and a driving license"))
        self.assertEqual([], scan("we practice what we preach"))


class ExemptionFencedCode(unittest.TestCase):
    def test_fenced_block_exempt(self):
        text = "prose\n```\nartifact stays artifact in this fenced block\n```\nmore prose\n"
        self.assertEqual([], scan(text))

    def test_tilde_fence_exempt(self):
        text = "prose\n~~~\norganize this fenced block\n~~~\nmore\n"
        self.assertEqual([], scan(text))


class ExemptionInlineCode(unittest.TestCase):
    def test_inline_code_span_exempt(self):
        self.assertEqual([], scan("`artifact` is just an example in code"))

    def test_prose_outside_span_still_flagged(self):
        self.assertEqual(["artifact"],
                          matches("the real artifact vs `artifact` the example"))


class ExemptionUrlAndPath(unittest.TestCase):
    def test_file_path_exempt(self):
        self.assertEqual([], scan("see docs/method/artifact-notes.md for detail"))

    def test_url_exempt(self):
        self.assertEqual(
            [], scan("visit https://example.com/artifact-guide for detail"))

    def test_bare_prose_still_flagged_elsewhere_on_line(self):
        fs = matches("the artifact is at docs/method/artifact-notes.md")
        self.assertEqual(["artifact"], fs)


class ExemptionBlockquote(unittest.TestCase):
    def test_blockquote_exempt(self):
        self.assertEqual([], scan("> this quoted text says color, verbatim"))

    def test_blockquote_with_leading_space_exempt(self):
        self.assertEqual([], scan("   > indented quote says organize"))


class ExemptionQuotedMention(unittest.TestCase):
    def test_double_quoted_mention_exempt(self):
        self.assertEqual(
            [], scan('the term "artifact" is discussed here as a naming choice'))

    def test_single_quoted_mention_exempt(self):
        self.assertEqual([], scan("the word 'color' is banned here"))

    def test_curly_quoted_mention_exempt(self):
        self.assertEqual([], scan("the word “organize” is banned here"))

    def test_unquoted_use_still_flagged(self):
        self.assertIn("artifact", matches("the build artifact lives here"))


class ExemptionAllowlistPhrase(unittest.TestCase):
    def test_artifact_attestations_exempt(self):
        self.assertEqual(
            [], scan("read the GitHub artifact attestations feature docs"))

    def test_upload_artifact_exempt(self):
        self.assertEqual([], scan("the upload-artifact action does this"))

    def test_bare_artifact_elsewhere_still_flagged(self):
        fs = matches("an artifact, unlike artifact attestations, is different")
        self.assertEqual(["artifact"], fs)

    def test_ci_build_release_sbom_artifact_sense_exempt(self):
        # SS3 (2026-07-23 review): the CI/build/release/SBOM software-
        # supply-chain sense of "artifact" is a term of art, not a genuine
        # NZ breach — the reviewer found ~48 of 53 live "artifact" hits were
        # this sense.
        self.assertEqual([], scan("Release-artifact signing + SBOM stays deferred"))
        self.assertEqual([], scan("scoped to repos with a deployable-artifact"))
        self.assertEqual([], scan("scoped to repos with a deployable artifact"))
        self.assertEqual([], scan("shares a name with a build-artifact convention"))
        self.assertEqual([], scan("layer 2 (artifact signing + SBOM) stays deferred"))
        self.assertEqual([], scan("rejected artifact-signing-now, each with why"))
        self.assertEqual([], scan("the first real published artifact; GitHub"))
        self.assertEqual([], scan("the open sub-item (step 1 Mike), artifact layer"))

    def test_general_sense_artifact_still_flagged(self):
        # The *general* "a produced thing" sense (a session record, a web
        # page) is deliberately NOT exempted — it stays a genuine NZ
        # breach, unlike the CI/build/release/SBOM term of art above.
        self.assertEqual(["artifact"], matches("no atelier artifact — the clean call"))
        self.assertEqual(["artifact"], matches("one responsive artifact already serves"))

    def test_owasp_chapter_proper_nouns_exempt(self):
        # SS3: OWASP ASVS/SAMM proper-noun chapter titles are a standards
        # body's own published names, not this repo's prose to re-spell.
        self.assertEqual([], scan("**PO** Prepare the Organization"))
        self.assertEqual([], scan("ch.1 now Encoding & Sanitization, verified live"))
        self.assertEqual(
            [], scan("V5 Validation, Sanitization & Encoding"))


class ExemptionAllCaps(unittest.TestCase):
    def test_all_caps_identifier_exempt(self):
        self.assertEqual([], scan("the env var COLOR is an identifier"))

    def test_all_caps_license_file_exempt(self):
        self.assertEqual([], scan("see the LICENSE file for terms"))

    def test_lowercase_use_still_flagged(self):
        self.assertIn("color", matches("pick a color for the theme"))


class AllowMarker(unittest.TestCase):
    def test_inline_allow_marker_exempts_line(self):
        self.assertEqual(
            [], scan("used color here  <!-- spellscan:allow: selftest fixture -->"))


class Ignore(unittest.TestCase):
    def test_exact_glob(self):
        self.assertTrue(ss._ignored("docs/fixture.md", ["docs/fixture.md"]))

    def test_subtree_glob(self):
        self.assertTrue(ss._ignored("docs/sessions/x.md", ["docs/sessions/"]))
        self.assertTrue(ss._ignored("docs/sessions/x.md", ["docs/sessions"]))

    def test_non_match(self):
        self.assertFalse(ss._ignored("docs/real.md", ["docs/fixture.md"]))


class FailOpenGuard(unittest.TestCase):
    """A malformed/edge input must never silently pass or crash-to-exit-0."""

    def test_unterminated_fence_treated_as_open_to_eof(self):
        # An unterminated fence swallows the rest of the file as quoted —
        # this is the same conservative (under-flag) behaviour datescan/
        # linkscan accept, not a crash and not a false "clean" on content
        # that was never actually inside a real fence pair. Documented
        # here so the behaviour is asserted, not accidental.
        text = "prose organize\n```\norganize inside unterminated fence\n"
        # The opening "organize" (before the fence) is still live prose.
        self.assertEqual(["organize"], matches(text))

    def test_empty_file_is_clean_not_a_crash(self):
        self.assertEqual([], scan(""))

    def test_binary_ish_content_does_not_crash(self):
        # Decoded-with-replacement bytes (as scan_paths does via
        # errors="replace") must not raise.
        text = "organize �� binary-ish bytes here\n"
        self.assertIn("organize", matches(text))

    def test_mismatched_backtick_lengths_do_not_crash(self):
        # Three backticks opened, two closed elsewhere — not a valid close;
        # must not raise, and must not silently swallow the whole line as
        # code (that would be a false-negative on live prose).
        text = "organize `` not really closed ``` still prose"
        self.assertIn("organize", matches(text))


class WholeTree(unittest.TestCase):
    def setUp(self):
        import shutil
        import tempfile
        self.tmp = ss.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _write(self, rel, text):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def _main(self, argv):
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()):
            return ss.main(argv)

    def test_defaults_to_docs_subdir(self):
        self._write("README.md", "an artifact outside docs\n")
        self._write("docs/note.md", "an artifact inside docs\n")
        self.assertEqual(1, self._main(["--root", str(self.tmp)]))
        findings = ss.scan_paths([self.tmp / "docs"], self.tmp)
        self.assertEqual(1, len(findings))
        self.assertEqual("docs/note.md", findings[0].path)

    def test_falls_back_to_root_when_no_docs_dir(self):
        self._write("note.md", "an artifact, no docs dir here\n")
        self.assertEqual(1, self._main(["--root", str(self.tmp)]))

    def test_nonexistent_path_is_an_error_not_a_pass(self):
        self.assertEqual(
            2, self._main(["--root", str(self.tmp), str(self.tmp / "gone")]))

    def test_warn_always_exits_zero(self):
        self._write("docs/note.md", "an artifact here\n")
        self.assertEqual(
            0, self._main(["--warn", "--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_without_warn_findings_exit_one(self):
        self._write("docs/note.md", "an artifact here\n")
        self.assertEqual(
            1, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_clean_tree_exits_zero(self):
        self._write("docs/note.md", "all NZ-English: artefact, colour, organise.\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_spellscanignore_exempts_path(self):
        self._write("docs/note.md", "an artifact here\n")
        self.assertEqual(
            1, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))
        self._write(".spellscanignore", "docs/note.md\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_non_markdown_files_skipped(self):
        self._write("docs/note.txt", "an artifact, not markdown\n")
        self.assertEqual(
            0, self._main(["--root", str(self.tmp), str(self.tmp / "docs")]))

    def test_json_output_shape(self):
        import json
        self._write("docs/note.md", "an artifact here\n")
        import contextlib
        import io
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            ss.main(["--json", "--root", str(self.tmp), str(self.tmp / "docs")])
        payload = json.loads(buf.getvalue())
        self.assertFalse(payload["clean"])
        self.assertEqual(1, len(payload["findings"]))
        self.assertEqual("artefact", payload["findings"][0]["suggestion"])


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(0, ss._selftest())


if __name__ == "__main__":
    unittest.main()
