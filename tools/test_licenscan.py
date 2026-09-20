"""Stdlib-only tests for licenscan (no pytest needed): `python3 -m unittest`.

Every licence body/declaration here is a fictional fixture — the SPDX *shape* is
what's under test, not any real project's licence choice.
"""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

import licenscan as lc
import memprobe

TOOLS_DIR = Path(__file__).resolve().parent

APACHE = ("Apache License\nVersion 2.0, January 2004\n"
          "http://www.apache.org/licenses/\n")
MIT = ("MIT License\n\nPermission is hereby granted, free of charge, to any "
       "person obtaining a copy of this software and associated documentation")
BSD3 = ("Redistribution and use in source and binary forms, with or without "
        "modification, are permitted provided that ... Neither the name of the "
        "copyright holder nor the names")
BSD2 = ("Redistribution and use in source and binary forms, with or without "
        "modification, are permitted provided that the following conditions")
GPL3 = "GNU GENERAL PUBLIC LICENSE\nVersion 3, 29 June 2007"
AGPL3 = "GNU AFFERO GENERAL PUBLIC LICENSE\nVersion 3, 19 November 2007"
LGPL3 = "GNU LESSER GENERAL PUBLIC LICENSE\nVersion 3, 29 June 2007"
MPL2 = "Mozilla Public License Version 2.0\n1. Definitions"
ISC = ("ISC License\n\nPermission to use, copy, modify, and/or distribute this "
       "software for any purpose with or without fee")
# A proprietary LICENSE body: present and deliberate, but no SPDX id names it.
PROPRIETARY = ("Copyright (c) 2026 Fictional Holdings. ALL RIGHTS RESERVED.\n"
               "No licence to copy, modify or redistribute is granted.")
LICENSEREF = ("This software is distributed under LicenseRef-Fictional-EULA.\n"
              "See the accompanying agreement for terms.")


def kinds(rep):
    return {f.kind for f in rep.findings}


class IdentifyText(unittest.TestCase):
    def test_apache(self):
        self.assertEqual(lc.identify_license_text(APACHE), "Apache-2.0")

    def test_mit(self):
        self.assertEqual(lc.identify_license_text(MIT), "MIT")

    def test_bsd3_before_bsd2(self):
        # BSD-3 is BSD-2 + a clause; the 3-clause signature must win.
        self.assertEqual(lc.identify_license_text(BSD3), "BSD-3-Clause")

    def test_bsd2(self):
        self.assertEqual(lc.identify_license_text(BSD2), "BSD-2-Clause")

    def test_agpl_before_gpl(self):
        self.assertEqual(lc.identify_license_text(AGPL3), "AGPL-3.0")

    def test_lgpl_before_gpl(self):
        self.assertEqual(lc.identify_license_text(LGPL3), "LGPL-3.0")

    def test_gpl3(self):
        self.assertEqual(lc.identify_license_text(GPL3), "GPL-3.0")

    def test_mpl(self):
        self.assertEqual(lc.identify_license_text(MPL2), "MPL-2.0")

    def test_isc(self):
        self.assertEqual(lc.identify_license_text(ISC), "ISC")

    def test_unrecognised(self):
        self.assertIsNone(lc.identify_license_text("all rights reserved, no really"))


class Normalise(unittest.TestCase):
    def test_bare_ids(self):
        self.assertEqual(lc.normalise_spdx("Apache-2.0"), "Apache-2.0")
        self.assertEqual(lc.normalise_spdx("MIT"), "MIT")

    def test_aliases(self):
        self.assertEqual(lc.normalise_spdx("GPLv3"), "GPL-3.0")
        self.assertEqual(lc.normalise_spdx("apache 2.0"), "Apache-2.0")
        self.assertEqual(lc.normalise_spdx("gpl-3.0-or-later"), "GPL-3.0")

    def test_only_or_later_plus_suffixes(self):
        # Review B2: the modern canonical -only/-or-later (and deprecated `+`)
        # forms must resolve to the base id, or a strong-copyleft header
        # mis-tiers from a high/incompatible block to a medium warn.
        self.assertEqual(lc.normalise_spdx("GPL-2.0-only"), "GPL-2.0")
        self.assertEqual(lc.normalise_spdx("AGPL-3.0-only"), "AGPL-3.0")
        self.assertEqual(lc.normalise_spdx("LGPL-2.1-only"), "LGPL-2.1")
        self.assertEqual(lc.normalise_spdx("LGPL-2.1-or-later"), "LGPL-2.1")
        self.assertEqual(lc.normalise_spdx("GPL-2.0+"), "GPL-2.0")

    def test_only_suffix_header_still_blocks(self):
        # The end-to-end teeth for B2: a GPL-2.0-only header in a permissive
        # repo must be the high/incompatible BLOCK, not unknown-declaration.
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", APACHE),
            ("vendor/v.c", "/* SPDX-License-Identifier: GPL-2.0-only */\n"),  # licenscan:allow: test fixture, not a real header
        ], None)
        self.assertIn("incompatible", kinds(rep))
        self.assertNotIn("unknown-declaration", kinds(rep))

    def test_classifier(self):
        self.assertEqual(
            lc.normalise_spdx("License :: OSI Approved :: MIT License"), "MIT")
        self.assertEqual(
            lc.normalise_spdx("License :: OSI Approved :: Apache Software License"),
            "Apache-2.0")  # the correct PyPI spelling of Apache-2.0

    def test_trove_classifiers_resolve(self):
        # E2: these are the published OSI trove strings, the CORRECT way a
        # Python package names its licence. Reading them as unrecognised
        # blocked repos that had done the right thing.
        cases = {
            "Apache Software License": "Apache-2.0",
            "ISC License (ISCL)": "ISC",
            "Mozilla Public License 2.0 (MPL 2.0)": "MPL-2.0",
            "GNU General Public License v2 (GPLv2)": "GPL-2.0",
            "GNU General Public License v3 or later (GPLv3+)": "GPL-3.0",
            "GNU Lesser General Public License v3 (LGPLv3)": "LGPL-3.0",
            "GNU Affero General Public License v3": "AGPL-3.0",
            "The Unlicense (Unlicense)": "Unlicense",
        }
        for tail, spdx in cases.items():
            with self.subTest(classifier=tail):
                self.assertEqual(lc.normalise_spdx(tail), spdx)
                self.assertEqual(
                    lc.normalise_spdx(f"License :: OSI Approved :: {tail}"), spdx)

    def test_ambiguous_trove_classifier_degrades(self):
        # A family name covering several versions must NOT be guessed a version
        # — it falls through to the unknown-declaration warn.
        for tail in ("BSD License",
                     "GNU General Public License (GPL)",
                     "GNU Library or Lesser General Public License (LGPL)"):
            with self.subTest(classifier=tail):
                self.assertIsNone(
                    lc.normalise_spdx(f"License :: OSI Approved :: {tail}"))

    def test_unknown(self):
        self.assertIsNone(lc.normalise_spdx("WTFPL"))


class Family(unittest.TestCase):
    def test_families(self):
        self.assertEqual(lc.family("MIT"), "permissive")
        self.assertEqual(lc.family("MPL-2.0"), "weak-copyleft")
        self.assertEqual(lc.family("GPL-3.0"), "strong-copyleft")
        self.assertEqual(lc.family("WTFPL"), "unknown")


class Compatibility(unittest.TestCase):
    def test_same_is_ok(self):
        self.assertEqual(lc.compatibility("MIT", "MIT"), "ok")

    def test_copyleft_into_permissive_blocks(self):
        self.assertEqual(lc.compatibility("Apache-2.0", "GPL-3.0"), "block")
        self.assertEqual(lc.compatibility("MIT", "AGPL-3.0"), "block")
        self.assertEqual(lc.compatibility("MIT", "MPL-2.0"), "block")

    def test_permissive_into_permissive_warns(self):
        self.assertEqual(lc.compatibility("Apache-2.0", "MIT"), "warn")

    def test_permissive_into_copyleft_warns(self):
        self.assertEqual(lc.compatibility("GPL-3.0", "MIT"), "warn")


class ScanRepo(unittest.TestCase):
    def test_clean(self):
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", APACHE),
            ("pyproject.toml", 'license = "Apache-2.0"\n'),
            ("README.md", "some prose"),
        ], None)
        self.assertTrue(rep.clean)
        self.assertEqual(rep.repo_license, "Apache-2.0")

    def test_no_license(self):
        rep = lc.scan_repo(lc.Path("."), [("pyproject.toml", 'license="MIT"\n')], None)
        self.assertIn("no-license", kinds(rep))

    def test_unknown_license_body(self):
        rep = lc.scan_repo(lc.Path("."), [("LICENSE", "proprietary, do not copy")],
                           None)
        self.assertIn("unknown-license", kinds(rep))

    def test_declaration_mismatch_is_high(self):
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", APACHE),
            ("pyproject.toml", 'license = "MIT"\n'),
        ], None)
        mismatch = [f for f in rep.findings if f.kind == "mismatch"]
        self.assertTrue(mismatch)
        self.assertEqual(mismatch[0].severity, "high")
        self.assertEqual(mismatch[0].path, "pyproject.toml")

    def test_copyleft_header_blocks(self):
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", MIT),
            ("vendor/x.c", "/* SPDX-License-Identifier: GPL-2.0 */\nint main(){}"),
        ], None)
        inc = [f for f in rep.findings if f.kind == "incompatible"]
        self.assertTrue(inc)
        self.assertEqual(inc[0].severity, "high")

    def test_permissive_header_is_medium_only(self):
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", APACHE),
            ("vendor/y.py", "# SPDX-License-Identifier: MIT\n"),
        ], None)
        self.assertTrue(any(f.kind == "mismatch" and f.severity == "medium"
                            for f in rep.findings))
        self.assertFalse(any(f.severity == "high" for f in rep.findings))

    def test_matching_header_is_clean(self):
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", APACHE),
            ("src/a.py", "# SPDX-License-Identifier: Apache-2.0\n"),
        ], None)
        self.assertTrue(rep.clean)

    def test_unknown_declaration(self):
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", APACHE),
            ("package.json", '{"license": "WTFPL"}\n'),
        ], None)
        self.assertIn("unknown-declaration", kinds(rep))

    def test_package_json_agrees(self):
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", MIT),
            ("package.json", '{\n  "name": "x",\n  "license": "MIT"\n}\n'),
        ], None)
        self.assertTrue(rep.clean)

    def test_trove_classifier_agrees(self):
        # E2's required case: the correct PyPI classifier beside a matching
        # `license` field used to be read as an unrecognised declaration and
        # blocked a repo that had declared itself properly.
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", APACHE),
            ("pyproject.toml",
             '[project]\nname = "x"\nlicense = "Apache-2.0"\nclassifiers = [\n'
             '    "License :: OSI Approved :: Apache Software License",\n'
             '    "Programming Language :: Python :: 3",\n]\n'),
        ], None)
        self.assertTrue(rep.clean, [f.message for f in rep.findings])

    def test_trove_classifier_contradiction_is_high(self):
        # Resolving classifiers gives them teeth as well as amnesty: one naming
        # a different licence from LICENSE is now the high self-contradiction.
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", APACHE),
            ("pyproject.toml",
             'classifiers = ["License :: OSI Approved :: MIT License"]\n'),
        ], None)
        mismatch = [f for f in rep.findings if f.kind == "mismatch"]
        self.assertTrue(mismatch)
        self.assertEqual(mismatch[0].severity, "high")

    def test_ambiguous_classifier_still_warns(self):
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", BSD3),
            ("pyproject.toml",
             'classifiers = ["License :: OSI Approved :: BSD License"]\n'),
        ], None)
        self.assertIn("unknown-declaration", kinds(rep))

    def test_readme_badge(self):
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", APACHE),
            ("README.md",
             "![license](https://img.shields.io/badge/license-MIT-blue.svg)"),
        ], None)
        self.assertTrue(any(f.kind == "mismatch" for f in rep.findings))

    def test_allow_marker_suppresses(self):
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", APACHE),
            ("vendor/z.py",
             "# SPDX-License-Identifier: GPL-3.0  # licenscan:allow: dual-licensed\n"),
        ], None)
        self.assertTrue(rep.clean)

    def test_line_number_accuracy(self):
        # the captured id ("MIT") also appears earlier as prose — the finding must
        # point at the header line, not the first textual occurrence.
        text = "MIT is a great licence\n\n# SPDX-License-Identifier: MIT\n"
        rep = lc.scan_repo(lc.Path("."), [("LICENSE", APACHE), ("a.py", text)], None)
        mism = [f for f in rep.findings if f.kind == "mismatch"]
        self.assertTrue(mism)
        self.assertEqual(mism[0].line, 3)


class CustomRepoLicense(unittest.TestCase):
    """E1 — a LICENSE we can't name is still a LICENSE. It used to stop the scan
    at one unknown-license finding, so the per-file header checks never ran: a
    proprietary repo could publish vendored copyleft in silence."""

    def test_proprietary_license_still_catches_copyleft(self):
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", PROPRIETARY),
            ("vendor/x.c", "/* SPDX-License-Identifier: GPL-2.0 */\nint main(){}"),  # licenscan:allow: test fixture, not a real header
        ], None)
        inc = [f for f in rep.findings if f.kind == "incompatible"]
        self.assertTrue(inc)
        self.assertEqual(inc[0].severity, "high")
        self.assertEqual(inc[0].path, "vendor/x.c")

    def test_proprietary_license_is_declared_not_absent(self):
        rep = lc.scan_repo(lc.Path("."), [("LICENSE", PROPRIETARY)], None)
        self.assertIsNone(rep.repo_license)
        self.assertEqual(rep.repo_license_declared, lc.CUSTOM_LICENSE)
        self.assertNotIn("no-license", kinds(rep))
        self.assertIn("unknown-license", kinds(rep))

    def test_licenseref_body_needs_no_warning(self):
        # An explicit SPDX LicenseRef- id is a deliberate custom declaration,
        # not a failure to recognise — it carries its own reason.
        rep = lc.scan_repo(lc.Path("."), [("LICENSE", LICENSEREF)], None)
        self.assertEqual(rep.repo_license_declared, "LicenseRef-Fictional-EULA")
        self.assertTrue(rep.clean)

    def test_licenseref_body_still_catches_copyleft(self):
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", LICENSEREF),
            ("vendor/x.py", "# SPDX-License-Identifier: AGPL-3.0\n"),  # licenscan:allow: test fixture, not a real header
        ], None)
        self.assertIn("incompatible", kinds(rep))

    def test_allow_marker_on_license_restores_the_checks(self):
        # The marker retires the unrecognised-body warn — it must NOT retire the
        # header checks with it, which is what the old early-stop did.
        body = PROPRIETARY + "\n# licenscan:allow: proprietary by design\n"
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", body),
            ("vendor/x.py", "# SPDX-License-Identifier: GPL-3.0\n"),  # licenscan:allow: test fixture, not a real header
        ], None)
        self.assertNotIn("unknown-license", kinds(rep))
        self.assertIn("incompatible", kinds(rep))

    def test_permissive_header_under_custom_license_is_quiet(self):
        # The documented limit: "differs from the repo licence" is unanswerable
        # when the repo licence has no name, so only the copyleft call is made.
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", PROPRIETARY + "\n# licenscan:allow: proprietary\n"),
            ("vendor/y.py", "# SPDX-License-Identifier: MIT\n"),
        ], None)
        self.assertTrue(rep.clean)

    def test_declarations_are_not_compared_to_a_custom_license(self):
        # Nothing to compare against — but an unrecognisable declaration is
        # still its own warn, exactly as before.
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", PROPRIETARY + "\n# licenscan:allow: proprietary\n"),
            ("pyproject.toml", 'license = "MIT"\n'),
            ("package.json", '{"license": "WTFPL"}\n'),
        ], None)
        self.assertEqual(kinds(rep), {"unknown-declaration"})

    def test_no_license_at_all_is_unchanged(self):
        rep = lc.scan_repo(lc.Path("."), [
            ("vendor/x.py", "# SPDX-License-Identifier: GPL-3.0\n"),  # licenscan:allow: test fixture, not a real header
        ], None)
        self.assertEqual(kinds(rep), {"no-license"})


class Expect(unittest.TestCase):
    def test_expect_mismatch(self):
        rep = lc.scan_repo(lc.Path("."), [("LICENSE", APACHE)], "MIT")
        self.assertIn("expect-mismatch", kinds(rep))

    def test_expect_ok(self):
        rep = lc.scan_repo(lc.Path("."), [("LICENSE", APACHE)], "Apache-2.0")
        self.assertTrue(rep.clean)

    def test_expect_accepts_alias(self):
        rep = lc.scan_repo(lc.Path("."), [("LICENSE", GPL3)], "GPLv3")
        self.assertTrue(rep.clean)

    def test_expect_against_a_custom_license_fails(self):
        # A CI assertion of Apache-2.0 must not pass just because the body is
        # unnameable — the allow marker retires the warn, not the assertion.
        rep = lc.scan_repo(lc.Path("."), [
            ("LICENSE", PROPRIETARY + "\n# licenscan:allow: proprietary\n"),
        ], "Apache-2.0")
        self.assertIn("expect-mismatch", kinds(rep))

    def test_expect_matches_an_explicit_licenseref(self):
        rep = lc.scan_repo(lc.Path("."), [("LICENSE", LICENSEREF)],
                           "LicenseRef-Fictional-EULA")
        self.assertTrue(rep.clean)


class Allowances(unittest.TestCase):
    """GUARDS.md rule (c) — a marker with no reason is a mention.

    (Moved above the __main__ block 2026-08-06, LC3: defined after
    `unittest.main()`, these ran under discovery but were silently dropped
    by a direct `python3 tools/test_licenscan.py` run.)"""

    def test_bare_marker_without_reason_is_not_an_allowance(self):
        self.assertIsNone(lc.parse_allow("# licenscan:allow"))
        self.assertIsNone(lc.parse_allow("# licenscan:allow:"))

    def test_marker_with_reason_allows(self):
        self.assertEqual("", lc.parse_allow("# licenscan:allow: vendored"))

    def test_bare_marker_in_license_body_does_not_retire_the_warn(self):
        # LC1 (ruled 2026-08-06): the unknown-license site used a raw
        # substring test, so a bare marker — or prose merely MENTIONING the
        # marker text — silently retired the warn. Rule (c): a marker with
        # no reason is a mention.
        for body in (PROPRIETARY + "\nlicenscan:allow\n",
                     PROPRIETARY + "\nTo exempt, write licenscan:allow here.\n"):
            rep = lc.scan_repo(lc.Path("."), [("LICENSE", body)], None)
            self.assertIn("unknown-license", kinds(rep))
            self.assertEqual(rep.suppressed_declarations, 0)

    def test_reasoned_marker_retires_the_warn_and_is_tallied(self):
        # LC2 (ruled 2026-08-06): the retirement counts in the rule (b)
        # tally, so a clean report cannot look identical to an exempted one.
        body = PROPRIETARY + "\n# licenscan:allow: proprietary by design\n"
        rep = lc.scan_repo(lc.Path("."), [("LICENSE", body)], None)
        self.assertNotIn("unknown-license", kinds(rep))
        self.assertEqual(rep.suppressed_declarations, 1)


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(lc._selftest(), 0)


class BoundedMemory(unittest.TestCase):
    """020/380 — the machine-thrash defect, this tool's own shape of it.

    `collect_files` used to read EVERY tracked file's full decoded text into
    one list before `scan_repo` checked a single declaration: for a real
    repo, the whole tree's text held in memory at once. Same defect class
    `secretscan`'s old `_walk_files` fixed one layer up (there, `Path`
    objects; here, far heavier decoded file bodies that do not stop growing
    at the tree's file count). Fixed by `_RepoFiles`
    (`tools/licenscan.py`), which re-walks the tree from disk on each of
    `scan_repo`'s two passes over `files` instead of caching a corpus.

    Measured the same way as `test_secretscan.py::BoundedMemory`: peak RSS is
    a whole-process number a Python-heap-only measurement (`tracemalloc`)
    cannot see (`tools/memprobe.py`'s module docstring), so this runs the
    real CLI as a subprocess and reads its peak RSS back from the kernel.
    """

    LICENSCAN = str(TOOLS_DIR / "licenscan.py")
    # Same file COUNT both runs, different SIZE per file: this isolates the
    # defect the fix targets — total TEXT held simultaneously — from the walk
    # itself (that shape is pathscan's own BoundedMemory test, file COUNT
    # rather than file SIZE).
    FILE_COUNT = 40
    SMALL_FILE_BYTES = 100 * 1024      # 100 KiB/file -> ~4 MB tree total
    LARGE_FILE_BYTES = 1024 * 1024     # 1 MiB/file -> ~40 MB tree total
    # Grounded in the FIX's design (`ground-numeric-limits`), not fitted to a
    # measurement: `_RepoFiles` holds at most ONE file's content at a time
    # (capped at `licenscan.MAX_FILE_BYTES`, 8 MiB), so growth between a 4 MB
    # and a 40 MB tree should be close to zero. The pre-fix code held the
    # whole tree's decoded text simultaneously, so the same delta measured,
    # while building this fix, a growth close to the ~36 MB difference in
    # total tree content. 20 MB leaves generous headroom above
    # interpreter/allocator noise while staying well below that pre-fix
    # figure — a fact recorded for context, not what set the number.
    GROWTH_BOUND_BYTES = 20 * 1024 * 1024

    @staticmethod
    def _build(root: Path, file_bytes: int, count: int) -> None:
        filler = ("no licence-shaped content here, just filler text. " * (
            file_bytes // 52 + 1))[:file_bytes]
        for i in range(count):
            (root / f"file_{i}.txt").write_text(filler)

    def _peak_rss_for(self, file_bytes: int) -> int:
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        self._build(tmp, file_bytes, self.FILE_COUNT)
        # Safety (020/370's own incident: a previous probe thrashed the
        # principal's machine doing exactly this kind of measurement): a hard
        # kill past ~900 MB, and a 60s ceiling so a regression that
        # reintroduces the whole-tree-in-memory shape fails the test instead
        # of hanging CI.
        result = memprobe.run_and_measure(
            [sys.executable, self.LICENSCAN, str(tmp)],
            timeout=60, rss_limit_bytes=900 * 1024 * 1024)
        self.assertFalse(result.timed_out, "scan did not finish in time")
        self.assertFalse(result.killed_over_limit,
                         "scan exceeded the 900 MB safety limit")
        return result.peak_rss_bytes

    def test_peak_memory_does_not_scale_with_total_tree_size(self):
        small_peak = self._peak_rss_for(self.SMALL_FILE_BYTES)
        large_peak = self._peak_rss_for(self.LARGE_FILE_BYTES)
        growth = large_peak - small_peak
        total_delta = (self.LARGE_FILE_BYTES - self.SMALL_FILE_BYTES) * self.FILE_COUNT
        self.assertLess(
            growth, self.GROWTH_BOUND_BYTES,
            f"peak RSS grew {growth / 1e6:.1f} MB for a tree whose total text "
            f"content grew by {total_delta / 1e6:.1f} MB (small="
            f"{small_peak / 1e6:.1f} MB, large={large_peak / 1e6:.1f} MB) — "
            "memory is scaling with tree size again (020/380).")


class LinkedWorktreeSkipped(unittest.TestCase):
    """020/160 (E9): `_walk_files` must prune a directory whose `.git` entry
    is a regular FILE (`gitdir: <path>`, the linked-worktree/submodule
    marker) — not just one literally named `.git` that is a directory.
    Before this fix a session's own gitignored `.claude/worktrees/<name>/`
    grew into a full second checkout of the tree that the walk descended
    into anyway, double-counting every finding (measured in `faves`
    2026-08-15)."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _write(self, rel, text):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def _found(self):
        return {str(p.relative_to(self.tmp))
                for p in lc._walk_files(self.tmp)}

    def test_linked_worktree_directory_is_pruned(self):
        self._write("real.txt", "content\n")
        self._write(".claude/worktrees/wt1/.git",
                    "gitdir: /elsewhere/.git/worktrees/wt1\n")
        self._write(".claude/worktrees/wt1/real.txt", "content\n")
        found = self._found()
        self.assertIn("real.txt", found)
        self.assertNotIn(".claude/worktrees/wt1/real.txt", found)
        self.assertNotIn(".claude/worktrees/wt1/.git", found)

    def test_independent_nested_repos_own_git_dir_still_pruned(self):
        """Unaffected by this fix: a nested repo whose `.git` is a
        DIRECTORY, not a linked worktree, was already excluded by the
        existing skip-dir-names rule matching the bare name `.git` at any
        depth inside it — this pins that it still holds."""
        self._write("nested/.git/objects/pack/dummy", "not real git data\n")
        self._write("nested/real.txt", "content\n")
        found = self._found()
        self.assertIn("nested/real.txt", found)
        self.assertNotIn("nested/.git/objects/pack/dummy", found)

    def test_ordinary_dotgit_file_is_treated_as_a_marker_too(self):
        """Deliberate, not a bug: the check is file-ness only, never
        content (see `_walk_files`'s comment) — a bare regular file
        literally named `.git` anywhere is treated as a worktree/submodule
        marker and prunes its parent, even holding no real `gitdir:` line
        as here. Accepted cost of the item's own stated minimum fix:
        nothing else legitimately creates a file with that exact name."""
        self._write("weird/.git", "not a real worktree marker\n")
        self._write("weird/real.txt", "content\n")
        found = self._found()
        self.assertNotIn("weird/real.txt", found)


if __name__ == "__main__":
    unittest.main()
