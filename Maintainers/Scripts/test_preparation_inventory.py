"""Tests for evidence extraction and deterministic preparation-report exports."""

from __future__ import annotations

from contextlib import redirect_stdout, redirect_stderr
import io
import json
from pathlib import Path
import tempfile
import unittest

import build_preparation_inventory as inventory
import validate_docs


class ExtractionTests(unittest.TestCase):
    def sources(self, text):
        lines, _ = inventory.visible_markdown(text)
        return inventory.source_links(lines)

    def test_only_explicit_references_links_and_duplicate_lines(self):
        text = "\n".join([
            "# A", "[Body](https://docs.python.org/3/)",
            "## 참조 (References)",
            "[One](https://docs.python.org/3/)",
            "[Again](https://docs.python.org/3/)",
            "https://numpy.org/doc/stable/",
            "[Index](../../Reference/Books.md)",
            "[Example](https://api.example.com/demo)",
            "[Local](http://127.0.0.1/demo)",
            "![Image](https://numpy.org/a.png)",
            "### 추가 자료", "<https://numpy.org/doc/stable/>",
            "## 다른 내용", "[Outside](https://pytorch.org/docs/)",
        ])
        self.assertEqual(self.sources(text), [
            {"url": "https://docs.python.org/3/", "lines": [4, 5]},
            {"url": "https://numpy.org/doc/stable/", "lines": [12]},
        ])

    def test_fences_comments_inline_code_and_fake_headings_are_ignored(self):
        text = "\n".join([
            "## 참조", "```python", "[Fake](https://fake.org/)",
            "## 재작성 메모 (Rewrite Notes)", "<!--", "```",
            "<!-- [Hidden](https://hidden.org/)", "-->",
            "`[Inline](https://inline.org/)`",
            "``[More](https://more.org/)``",
            "[Visible](https://docs.python.org/3/)",
        ])
        visible, blocks = inventory.visible_markdown(text)
        self.assertNotIn("## 재작성 메모 (Rewrite Notes)", visible)
        self.assertEqual(len(blocks), 1)
        self.assertTrue(blocks[0]["closed"])
        self.assertEqual(self.sources(text), [{"url": "https://docs.python.org/3/", "lines": [11]}])

    def test_reference_definitions_require_use_and_can_live_elsewhere(self):
        text = "\n".join([
            "[doc]: https://docs.python.org/3/ \"Python\"",
            "[unused]: https://unused.org/",
            "[automatic]: <https://numpy.org/doc/stable/>",
            "## References",
            "[Python][DOC] and [doc][] and [doc]",
            "[automatic]",
        ])
        self.assertEqual(self.sources(text), [
            {"url": "https://docs.python.org/3/", "lines": [5]},
            {"url": "https://numpy.org/doc/stable/", "lines": [6]},
        ])

    def test_code_only_link_labels_survive_but_links_inside_code_do_not(self):
        text = "\n".join([
            "## References",
            "[`svd`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html)",
            "[``scipy.linalg.svd``](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.svd.html)",
            "`[Fake](https://fake.org/)`",
            "``[`Fake`](https://other-fake.org/)``",
        ])
        self.assertEqual(self.sources(text), [
            {"url": "https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.svd.html", "lines": [3]},
            {"url": "https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html", "lines": [2]},
        ])

    def test_distinct_code_only_reference_labels_do_not_collapse(self):
        text = "\n".join([
            "[`numpy`]: https://numpy.org/",
            "[`scipy`]: https://scipy.org/",
            "## References",
            "[`numpy`] and [`scipy`][]",
        ])
        self.assertEqual(self.sources(text), [
            {"url": "https://numpy.org/", "lines": [4]},
            {"url": "https://scipy.org/", "lines": [4]},
        ])

    def test_balanced_parentheses_angle_destinations_and_titles(self):
        text = "\n".join([
            "## 참조",
            '[A](https://en.wikipedia.org/wiki/Type_(type_theory) "Title")',
            '[B](<https://docs.python.org/3/library/typing.html> "Typing")',
            '[Broken](https://broken.org/no-closing-parenthesis',
        ])
        self.assertEqual([s["url"] for s in self.sources(text)], [
            "https://docs.python.org/3/library/typing.html",
            "https://en.wikipedia.org/wiki/Type_(type_theory)",
        ])

    def test_image_destinations_and_reference_suffixes_are_not_sources(self):
        text = "\n".join([
            "[picture]: https://numpy.org/picture.png",
            "[caption]: https://docs.python.org/caption.png",
            "## References",
            "![Picture](<https://numpy.org/picture.png>)",
            "![Description][picture]",
            "![caption][]",
            "![picture]",
        ])
        self.assertEqual(self.sources(text), [])

    def test_reserved_urls_are_not_source_evidence(self):
        for url in [
            "https://example.com/x", "https://a.example.org/x", "https://host.test/x",
            "http://localhost:3000/x", "http://[::1]/x", "http://192.168.1.1/x",
            "mailto:author@python.org", "../Books.md", "http://[invalid",
        ]:
            with self.subTest(url=url):
                self.assertFalse(inventory.is_source_url(url))
        self.assertTrue(inventory.is_source_url("https://docs.python.org/3/"))

    def test_fence_size_language_and_unclosed_blocks(self):
        text = "\n".join([
            "````python", "```", "x = 1", "````",
            "~~~mermaid", "flowchart LR", "~~~",
            "```text", "notes", "```", "```", "unknown", "```",
            "```bash", "echo test",
        ])
        _, blocks = inventory.visible_markdown(text)
        self.assertEqual([b["language"] for b in blocks], ["python", "mermaid", "text", "unspecified", "bash"])
        self.assertEqual(sum(b["implementation_candidate"] for b in blocks), 2)
        self.assertEqual(blocks[0]["end_line"], 4)
        self.assertFalse(blocks[-1]["closed"])

    def test_comments_cannot_create_fences_or_hide_after_inline_code(self):
        text = "\n".join([
            "<!--", "```python", "-->", "`<!--` is inline code",
            "## 참조", "[Source](https://docs.python.org/3/)",
        ])
        _, blocks = inventory.visible_markdown(text)
        self.assertEqual(blocks, [])
        self.assertEqual(len(self.sources(text)), 1)


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.topic = self.root / "Programming" / "A.md"
        self.topic.parent.mkdir()
        self.topic.write_text("# A\n\n- Status: Draft\n\n---\n\n## 참조\n", encoding="utf-8")

    def run_main(self, *args):
        output = io.StringIO()
        with redirect_stdout(output):
            result = inventory.main(["--root", str(self.root), *args])
        return result, output.getvalue()

    def test_scope_notes_and_json_provenance(self):
        for name in ["Programming/README.md", "Maintainers/Private.md", "Templates/Topic.md", "Other/Test.md"]:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# Not a topic\n", encoding="utf-8")
        self.topic.write_text(self.topic.read_text(encoding="utf-8") +
            "[Python](https://docs.python.org/3/)\n\n## 재작성 메모 (Rewrite Notes)\n\n"
            "재사용: 작은 구현.\n\n```python\nprint(1)\n```\n", encoding="utf-8")
        result, output = self.run_main("--format", "json")
        data = json.loads(output)
        self.assertEqual(result, 0)
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual(data["summary"]["topic_count"], 1)
        topic = data["topics"][0]
        self.assertEqual(topic["path"], "Programming/A.md")
        self.assertEqual(topic["status"], "Draft")
        self.assertEqual(topic["code_language_counts"], {"python": 1})
        self.assertEqual(topic["sources"][0]["lines"], [8])
        self.assertEqual(topic["rewrite_notes_lines"], [10])
        self.assertEqual(len(topic["content_sha256"]), 64)
        self.assertEqual(topic["flags"], [])
        self.assertFalse((self.root / inventory.REPORT_PATH).exists())

    def test_missing_fenced_notes_and_unclosed_fence_flags(self):
        with self.topic.open("a", encoding="utf-8") as handle:
            handle.write("```python\n## 재작성 메모 (Rewrite Notes)\n")
        data = inventory.inspect_topic(self.topic, self.root)
        self.assertFalse(data["has_rewrite_notes"])
        self.assertEqual(data["flags"], ["missing-source", "missing-notes", "unclosed-code-fence"])

    def test_write_check_detects_inventory_change_and_is_deterministic(self):
        self.assertEqual(self.run_main("--check")[0], 1)
        self.assertEqual(self.run_main("--write")[0], 0)
        initial = (self.root / inventory.REPORT_PATH).read_bytes()
        self.assertEqual(self.run_main("--check")[0], 0)
        self.run_main("--write")
        self.assertEqual((self.root / inventory.REPORT_PATH).read_bytes(), initial)
        with self.topic.open("a", encoding="utf-8") as handle:
            handle.write("[Python](https://docs.python.org/3/)\n")
        self.assertEqual(self.run_main("--check")[0], 1)
        self.assertEqual((self.root / inventory.REPORT_PATH).read_bytes(), initial)
        self.run_main("--write")
        self.assertEqual(self.run_main("--check")[0], 0)

    def test_default_stdout_does_not_write_and_has_valid_links_and_tables(self):
        result, output = self.run_main()
        self.assertEqual(result, 0)
        report_path = self.root / inventory.REPORT_PATH
        self.assertFalse(report_path.exists())
        lines = output.splitlines()
        self.assertEqual(validate_docs.check_links(report_path, self.root, lines), [])
        self.assertEqual(validate_docs.check_table_shapes(report_path, self.root, lines), [])
        self.assertEqual(validate_docs.check_status_values(report_path, self.root, lines), [])

    def test_report_uses_sorted_topics_and_area_totals(self):
        for name in ["Math/Z.md", "Algorithms/C.md", "Math/A.md"]:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("# A\n\n- Status: Draft\n", encoding="utf-8")
        data = inventory.build_inventory(self.root)
        self.assertEqual([topic["path"] for topic in data["topics"]], ["Algorithms/C.md", "Math/A.md", "Math/Z.md", "Programming/A.md"])
        self.assertEqual(data["areas"]["Math"]["topic_count"], 2)
        self.assertEqual(data["summary"]["without_direct_sources"], 4)
        self.assertEqual(data["summary"]["without_rewrite_notes"], 4)

    def test_json_cannot_overwrite_markdown_report(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as raised:
            inventory.main(["--root", str(self.root), "--format", "json", "--write"])
        self.assertEqual(raised.exception.code, 2)
        self.assertFalse((self.root / inventory.REPORT_PATH).exists())


if __name__ == "__main__":
    unittest.main()
