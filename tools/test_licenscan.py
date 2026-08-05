"""Stdlib-only tests for licenscan (no pytest needed): `python3 -m unittest`.

Every licence body/declaration here is a fictional fixture — the SPDX *shape* is
what's under test, not any real project's licence choice.
"""

import unittest

import licenscan as lc

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


class SelfTest(unittest.TestCase):
    def test_selftest_passes(self):
        self.assertEqual(lc._selftest(), 0)


if __name__ == "__main__":
    unittest.main()
