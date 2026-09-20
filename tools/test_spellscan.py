"""Stdlib-only tests for spellscan (no pytest needed): `python3 -m unittest`."""

import shutil
import sys
import tempfile
import time
import unittest
from pathlib import Path

import spellscan as ss
import memprobe

TOOLS_DIR = Path(__file__).resolve().parent


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
        self._write(".spellscanignore", "# a reasoned fixture exemption\ndocs/note.md\n")
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


class Allowances(unittest.TestCase):
    """GUARDS.md — narrow, noisy, reasoned, declared."""

    def test_marker_with_reason_exempts_and_is_counted(self):
        tally = ss.Tally()
        found = ss.scan_text(
            "t", "the color choice <!-- spellscan:allow: quoting an API field -->\n",
            tally)
        self.assertEqual([], found)
        self.assertEqual({"color": 1}, tally.by_marker)

    # Rule (c) — a marker with no reason is a mention, not an exemption.
    def test_bare_marker_without_reason_does_not_exempt(self):
        self.assertTrue(ss.scan_text("t", "the color choice <!-- spellscan:allow -->\n"))

    def test_prose_mention_does_not_exempt(self):
        self.assertTrue(ss.scan_text(
            "t", "we use the spellscan:allow marker for color words\n"))

    # Rule (a) — the word is the narrowest unit this scanner has.
    def test_scoped_marker_exempts_only_its_own_word(self):
        found = ss.scan_text(
            "t", "the color and the organized plan "
                 "<!-- spellscan:allow:color: an API field name -->\n")
        self.assertEqual(["organized"], [f.match for f in found])

    def test_clean_tally_reports_known_zeros(self):
        self.assertIn("0 by allow-marker", ss.Tally().summary())


class PathUrlStripIsLinearTime(unittest.TestCase):
    """020/380 — `_PATH_OR_URL_RX` used to be `\\S*/\\S+`: `\\S*` includes
    "/" itself, so for a long run of non-whitespace characters with NO "/"
    at all, the engine backtracked one character at a time at EVERY starting
    position looking for a "/" that never comes — classic O(n^2) regex
    behaviour. Measured while building this fix: 0.0019s at 1,000 characters,
    0.19s at 10,000 (~100x for a 10x input — the quadratic signature), 21.6s
    at 100,000. This is what made `spellscan one-huge-line` hang past the
    board item's own 120s measurement-harness ceiling even at a mere 1 MB
    input. Fixed by excluding "/" from the prefix's character class
    (`[^\\s/]*/\\S+`) — same matches, no overlap to backtrack through."""

    def test_long_slash_free_token_is_fast(self):
        line = "x" * 200_000
        t0 = time.monotonic()
        ss.scan_text("t", line)
        dt = time.monotonic() - t0
        # Linear-time code does this in a few milliseconds; the pre-fix
        # quadratic code would take tens of seconds at this length (the
        # 100,000-character measurement alone took 21.6s). 2s is generous
        # headroom for a slow CI box while still failing hard if the
        # quadratic behaviour comes back.
        self.assertLess(dt, 2.0,
                        f"took {dt:.2f}s on a 200,000-char slash-free token — "
                        "the O(n^2) _PATH_OR_URL_RX backtracking is back (020/380)")

    def test_matching_behaviour_is_unchanged(self):
        # The path/URL token is blanked whole, length preserved — every
        # existing path/URL-stripping test elsewhere in this file already
        # pins that a slash-shaped token is exempted from the denylist; this
        # just checks the multi-slash case the fix's own reasoning leans on.
        line = "see docs/method/PRINCIPLES.md for the rule"
        token = "docs/method/PRINCIPLES.md"
        expected = line.replace(token, " " * len(token))
        self.assertEqual(expected, ss._strip_paths_and_urls(line))

    def test_trailing_bare_slash_now_blanked_too(self):
        # The one HONEST widening from the pre-fix regex (see
        # `_strip_paths_and_urls`'s docstring): a token that is nothing but a
        # trailing "/" with no character after it used to survive; now it is
        # blanked like any other slash-shaped token. Never a narrower match —
        # it cannot cause a real US spelling to go unflagged.
        line = "prefix abc/ suffix"
        expected = line.replace("abc/", " " * len("abc/"))
        self.assertEqual(expected, ss._strip_paths_and_urls(line))


class BoundedMemory(unittest.TestCase):
    """020/380 — applying 020/370's bounded-memory fix to spellscan. Mike's
    ruling, verbatim: "it should not matter how much it scans it should no
    have this affect". Measured BEFORE this fix (see the board item's own
    before/after table): a 23 MB larger many-line docs file drove ~94 MB of
    peak-RSS growth from the old `read_text()` whole-file string plus
    `text.splitlines()` whole-file list (the same shape secretscan's
    `020/370` fixed); a SINGLE huge line TIMED OUT the 120s measurement
    harness outright — see `PathUrlStripIsLinearTime` above for that half.

    Runs the real CLI as a SUBPROCESS via `memprobe.run_and_measure` and
    reads peak RSS back from the kernel — see `tools/memprobe.py`.

    Content is plain filler prose with no US spelling anywhere, so both runs
    produce zero findings — the only thing that differs is how many bytes
    there are to read."""

    SPELLSCAN = str(TOOLS_DIR / "spellscan.py")
    SMALL_BYTES = 1 * 1024 * 1024
    LARGE_BYTES = 8 * 1024 * 1024
    # See test_datescan.BoundedMemory's identical comment: a literal, not a
    # reference to `ss._READ_CHUNK_BYTES`/`_MAX_LINE_BYTES`, grounded in the
    # same fixed per-file state (a 1 MiB read chunk plus one physical line
    # capped at 8 KiB — `spellscan._iter_physical_lines`), 8x over for
    # allocator noise.
    GROWTH_BOUND_BYTES = 8 * (1 * 1024 * 1024 + 8 * 1024)

    @staticmethod
    def _build_many_line(target_bytes: int, path: Path) -> None:
        with open(path, "w") as f:
            written = 0
            i = 0
            while written < target_bytes:
                line = f"this is filler prose line number {i} nothing to see here\n"
                f.write(line)
                written += len(line)
                i += 1

    def _peak_rss_for(self, size_bytes: int) -> int:
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        docs = tmp / "docs"
        docs.mkdir()
        self._build_many_line(size_bytes, docs / "note.md")
        result = memprobe.run_and_measure(
            [sys.executable, self.SPELLSCAN, "--root", str(tmp), str(docs)],
            timeout=60, rss_limit_bytes=900 * 1024 * 1024)
        self.assertFalse(result.timed_out, "scan did not finish in time")
        self.assertFalse(result.killed_over_limit,
                         "scan exceeded the 900 MB safety limit")
        self.assertEqual(0, result.returncode,
                         "filler content must not itself flag anything")
        return result.peak_rss_bytes

    def test_peak_memory_does_not_scale_with_many_line_file_size(self):
        small_peak = self._peak_rss_for(self.SMALL_BYTES)
        large_peak = self._peak_rss_for(self.LARGE_BYTES)
        growth = large_peak - small_peak
        self.assertLess(
            growth, self.GROWTH_BOUND_BYTES,
            f"peak RSS grew {growth / 1e6:.1f} MB for a "
            f"{(self.LARGE_BYTES - self.SMALL_BYTES) / 1e6:.1f} MB larger "
            f"many-line file (small={small_peak / 1e6:.1f} MB, "
            f"large={large_peak / 1e6:.1f} MB) — memory is scaling with "
            "input size again (020/380).")
