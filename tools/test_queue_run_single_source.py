"""The /atelier:queue-run skill and the principal's hand copy are one text.

Mike, 2026-10-18 (180/090): "You need to ensure the there is no drift between
the command and the text file unless I authorise the drift." The skill loads
docs/method/session-open/session-open-prompt.md and restates none of it, so
the command runs exactly the file he can open and paste. This test fails if
the skill stops pointing at the file, starts copying the file's lines into
itself (a second copy is the start of drift), or grows an instruction the
delivery job does not need. It cannot catch a paraphrase; the skill's own
header bars that.

160/900 (Mike, 2026-11-08: "Keep edit; read committed only"): the command
runs the committed copy of the prompt, never the working file, and warns when
an edit to it is pending (QK1). The skill's body is therefore not only a
pointer, so the "nothing but delivery" check below holds the line (QK9): every
paragraph must be one of the known delivery paragraphs and may name only the
known files.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "queue-run" / "SKILL.md"
PROMPT = ROOT / "docs" / "method" / "session-open" / "session-open-prompt.md"
REF = "docs/method/session-open/session-open-prompt.md"
DOCTRINE_REF = "docs/method/CONCURRENCY.md"

# The only files the skill body may name (QK9, mutation m7: an instruction
# pointed at another file passed the old test).
ALLOWED_FILES = {REF, DOCTRINE_REF}

# Each body paragraph must carry one of these anchors: they are the delivery
# jobs (QK1 committed read, QK3 bundled doctrine path, the typed text) and
# nothing else. A new paragraph of rules matches none and fails.
DELIVERY_ANCHORS = (
    "session-open prompt",      # the opening paragraph: whose text it runs
    "session-open-prompt.md",   # where the prompt is
    "committed copy",           # QK1: read the committed copy
    "CONCURRENCY.md",           # QK3: the bundled doctrine path
    "typed after",              # where the typed text goes
)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def flatten(text: str) -> str:
    """Prose with markup stripped (QK9, mutation m3: a bullet copied without
    its dash was never a match): list markers, emphasis and code ticks go,
    each paragraph is one line."""
    lines = []
    for line in text.splitlines():
        line = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line)
        lines.append(line)
    text = "\n".join(lines)
    text = re.sub(r"[*`]", "", text)
    return text


def copied_sentences(skill_text: str, prompt_text: str, minimum: int = 40):
    skill = norm(flatten(skill_text))
    copied = []
    for para in flatten(prompt_text).split("\n\n"):
        # a list's items are separate sentences, not one run of text
        for item in para.split("\n"):
            for sentence in re.split(r"(?<=[.!?:])\s+", norm(item)):
                if len(sentence) >= minimum and sentence in skill:
                    copied.append(sentence)
    return copied


def skill_body(text: str) -> str:
    """The skill with its front matter, HTML comment and title removed."""
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return re.sub(r"^# .*$", "", text, flags=re.M)


class QueueRunSingleSource(unittest.TestCase):
    def test_prompt_file_exists(self):
        self.assertTrue(PROMPT.is_file(), f"{PROMPT} is missing")

    def test_skill_points_at_the_prompt(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("${CLAUDE_PLUGIN_ROOT}/" + REF, text)
        self.assertIn("../../" + REF, text)

    def test_skill_restates_no_prompt_line(self):
        copied = copied_sentences(SKILL.read_text(encoding="utf-8"),
                                  PROMPT.read_text(encoding="utf-8"))
        self.assertEqual(copied, [], "the skill copies prompt text; point at "
                         "the file instead: " + "; ".join(copied))

    # QK9: the copy check sees the shapes real drift takes.
    def test_copy_check_catches_a_bullet_copied_without_its_dash(self):
        prompt = "Intro line.\n\n- Claim before you work, never after and a live claim beats a direct instruction.\n- Another short rule.\n"
        skill = "Do this. Claim before you work, never after and a live claim beats a direct instruction."
        self.assertEqual(len(copied_sentences(skill, prompt)), 1)

    def test_copy_check_catches_emphasis_and_numbering_differences(self):
        prompt = "1. Summarise what was **learnt, progressed, or delivered** and end with the session identifiers.\n"
        skill = "Summarise what was learnt, progressed, or delivered and end with the session identifiers."
        self.assertEqual(len(copied_sentences(skill, prompt)), 1)

    def test_copy_check_still_passes_unrelated_text(self):
        prompt = "- Claim before you work, never after and a live claim beats a direct instruction.\n"
        self.assertEqual(copied_sentences("Read the file at the path.", prompt), [])

    # QK9 (mutations m2 and m7): the skill adds delivery and nothing else.
    def test_skill_body_is_delivery_only(self):
        body = skill_body(SKILL.read_text(encoding="utf-8"))
        paragraphs = [p for p in re.split(r"\n\s*\n", flatten(body)) if p.strip()]
        self.assertTrue(paragraphs)
        for para in paragraphs:
            flat = norm(para)
            self.assertTrue(
                any(a in flat for a in DELIVERY_ANCHORS),
                "a paragraph of the skill body is not one of its delivery "
                "jobs (fetch the prompt, the committed copy, the bundled "
                "doctrine path, the typed text); a rule belongs in the "
                f"principal's prompt, not here: {flat[:80]!r}")

    def test_skill_body_names_only_known_files(self):
        body = skill_body(SKILL.read_text(encoding="utf-8"))
        named = set(re.findall(r"[\w./${}-]*\w+\.(?:md|py|json|ya?ml|sh)\b", body))
        for ref in named:
            self.assertTrue(
                any(ref.endswith(ok) for ok in ALLOWED_FILES),
                f"the skill body names {ref!r}, which is not one of "
                f"{sorted(ALLOWED_FILES)}")

    # QK1: the command runs the committed copy and warns on a pending edit.
    def test_skill_reads_the_committed_copy_not_the_working_file(self):
        flat = norm(flatten(SKILL.read_text(encoding="utf-8")))
        self.assertIn("committed copy", flat)
        self.assertIn('git -C "${CLAUDE_PLUGIN_ROOT}" show HEAD:' + REF, flat)
        self.assertIn("do not open the working file", flat)

    def test_skill_warns_when_an_edit_to_the_prompt_is_pending(self):
        flat = norm(flatten(SKILL.read_text(encoding="utf-8")))
        self.assertIn('git -C "${CLAUDE_PLUGIN_ROOT}" status --porcelain -- ' + REF, flat)
        self.assertIn("edits to the prompt are pending", flat)
        self.assertIn("you do not commit it", flat)

    def test_skill_says_what_happens_without_a_checkout(self):
        flat = norm(flatten(SKILL.read_text(encoding="utf-8")))
        self.assertIn("not a git checkout", flat)
        self.assertIn("say which of the two applied", flat)

    # QK3: the doctrine anchor resolves in a GitHub install too.
    def test_skill_gives_the_bundled_doctrine_path(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("${CLAUDE_PLUGIN_ROOT}/" + DOCTRINE_REF, text)
        self.assertTrue((ROOT / DOCTRINE_REF).is_file())


if __name__ == "__main__":
    unittest.main()
