"""Unit tests for validate_docs.py and sync_summary_counts.py.

Uses only the standard library (unittest), so it runs anywhere validate_docs.py
runs, with no extra packages.

Run from the repository root:

    python Maintainers/Scripts/test_validate_docs.py
    python -m unittest -v   (from inside Maintainers/Scripts/)
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import sync_summary_counts
import validate_docs as vd


class PureFunctionTests(unittest.TestCase):
    def test_slugify_heading(self):
        self.assertEqual(vd.slugify_heading("Hello World"), "hello-world")
        self.assertEqual(vd.slugify_heading("Foo `Bar` *Baz*"), "foo-bar-baz")
        self.assertEqual(vd.slugify_heading("[Text](http://x)"), "text")
        self.assertEqual(vd.slugify_heading("개념 (Concept)"), "개념-concept")

    def test_split_table_cells_basic(self):
        self.assertEqual(vd.split_table_cells("| a | b | c |"), ["a", "b", "c"])

    def test_split_table_cells_code_span_with_pipe(self):
        self.assertEqual(vd.split_table_cells("| `x|y` | z |"), ["`x|y`", "z"])

    def test_split_table_cells_escaped_pipe(self):
        self.assertEqual(vd.split_table_cells("| a \\| b | c |"), ["a \\| b", "c"])

    def test_split_link_target(self):
        self.assertEqual(vd.split_link_target("path#anchor"), ("path", "anchor"))
        self.assertEqual(vd.split_link_target("p?x=1#f"), ("p", "f"))
        self.assertEqual(vd.split_link_target("plain.md"), ("plain.md", None))
        self.assertEqual(vd.split_link_target("<a b>"), ("a b", None))

    def test_is_external_link_target(self):
        self.assertTrue(vd.is_external_link_target("http://x"))
        self.assertTrue(vd.is_external_link_target("mailto:a@b.c"))
        self.assertFalse(vd.is_external_link_target("./a.md"))
        self.assertFalse(vd.is_external_link_target("../b/"))

    def test_disallowed_external_link_domain(self):
        self.assertTrue(vd.has_disallowed_external_link_domain("https://sci-hub.se/x"))
        self.assertTrue(vd.has_disallowed_external_link_domain("https://www.libgen.is/y"))
        self.assertFalse(vd.has_disallowed_external_link_domain("https://example.com"))

    def test_normalize_anchor_fragment(self):
        self.assertEqual(vd.normalize_anchor_fragment("User-Content-Foo"), "foo")
        self.assertEqual(vd.normalize_anchor_fragment("  Bar "), "bar")

    def test_parse_int_cell(self):
        self.assertEqual(vd.parse_int_cell("5"), 5)
        self.assertEqual(vd.parse_int_cell("191"), 191)
        self.assertEqual(vd.parse_int_cell("3 (extra)"), 3)
        self.assertIsNone(vd.parse_int_cell("none"))

    def test_parse_reference_coverage_cell(self):
        self.assertEqual(vd.parse_reference_coverage_cell("4/7 (4)"), (4, 7, 4))
        self.assertEqual(vd.parse_reference_coverage_cell("1/6 (7)*"), (1, 6, 7))
        self.assertIsNone(vd.parse_reference_coverage_cell("bad"))

    def test_clean_file_cell(self):
        self.assertEqual(vd.clean_file_cell("[X](Foo.md)"), "Foo.md")
        self.assertEqual(vd.clean_file_cell("`Bar.md`"), "Bar.md")
        self.assertEqual(vd.clean_file_cell("Plain.md"), "Plain.md")

    def test_is_markdown_link(self):
        self.assertTrue(vd.is_markdown_link("[a](b)"))
        self.assertFalse(vd.is_markdown_link("plain"))
        self.assertFalse(vd.is_markdown_link("`a`"))

    def test_normalized_reference_target(self):
        self.assertEqual(vd.normalized_reference_target("../../Systems/Networks/"), "Systems/Networks")
        self.assertEqual(vd.normalized_reference_target("Programming"), "Programming")
        self.assertEqual(vd.normalized_reference_target("../X#y"), "X")

    def test_count_table_columns(self):
        self.assertEqual(vd.count_table_columns("| a | b |"), 2)

    def test_metadata_block(self):
        lines = [
            "# 제목 (Title)",
            "",
            "- Level: Beginner",
            "- Prerequisites: 없음",
            "- Status: Draft",
            "---",
            "## 개념",
        ]
        self.assertEqual(
            vd.metadata_block(lines),
            {"Level": "Beginner", "Prerequisites": "없음", "Status": "Draft"},
        )


class LineCheckTests(unittest.TestCase):
    """Checks that operate on line lists; paths are lexical, no filesystem."""

    def setUp(self):
        self.root = Path("repo")
        self.path = self.root / "x.md"

    def test_table_shapes_valid(self):
        lines = ["| a | b | c |", "|---|---|---|", "| 1 | 2 | 3 |"]
        self.assertEqual(vd.check_table_shapes(self.path, self.root, lines), [])

    def test_table_shapes_mismatch(self):
        lines = ["| a | b | c |", "|---|---|---|", "| 1 | 2 |"]
        issues = vd.check_table_shapes(self.path, self.root, lines)
        self.assertTrue(any(i.type == "TableShape" for i in issues))

    def test_status_values(self):
        lines = ["| 주제 | Status |", "|---|---|", "| x | Draft |", "| y | Bogus |"]
        issues = vd.check_status_values(self.path, self.root, lines)
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].type, "BadStatus")
        self.assertIn("Bogus", issues[0].message)


class LinkCheckTests(unittest.TestCase):
    def test_links_existence_and_policy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "target.md").write_text("# T\n", encoding="utf-8")
            source = root / "source.md"
            lines = [
                "[ok](target.md)",
                "[broken](missing.md)",
                "[paper](https://sci-hub.se/10.1/x)",
                "[fine](https://example.com)",
            ]
            source.write_text("\n".join(lines), encoding="utf-8")

            issues = vd.check_links(source, root, lines)
            types = {i.type for i in issues}
            self.assertIn("BrokenLink", types)
            self.assertIn("DisallowedExternalLink", types)
            broken = [i for i in issues if i.type == "BrokenLink"]
            self.assertTrue(all("missing.md" in i.message for i in broken))


class SummaryCountTests(unittest.TestCase):
    """Integration tests for the generalized summary-count logic and the sync tool."""

    def _build_repo(self, review_cell: str) -> Path:
        tmp = tempfile.mkdtemp()
        root = Path(tmp)
        (root / "Programming").mkdir()
        (root / "Maintainers").mkdir()
        (root / "Programming" / "README.md").write_text(
            "\n".join(
                [
                    "# Programming",
                    "",
                    "| 주제 | 파일 | Status |",
                    "|---|---|---|",
                    "| a | [A.md](A.md) | Draft |",
                    "| b | [B.md](B.md) | Review |",
                    "| c | C.md | Planned |",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        (root / "Maintainers" / "Content-Backlog.md").write_text(
            "\n".join(
                [
                    "# Backlog",
                    "",
                    "| 영역 | Draft | Review | Planned | 역할 |",
                    "|---|---:|---:|---:|---|",
                    f"| Programming | 1 | {review_cell} | 1 | 출발점 |",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        return root

    def test_counts_in_sync_no_issues(self):
        root = self._build_repo(review_cell="1")
        issues = vd.check_maintainer_summary_counts(root)
        self.assertEqual(issues, [])

    def test_counts_mismatch_detected(self):
        root = self._build_repo(review_cell="9")
        issues = vd.check_maintainer_summary_counts(root)
        self.assertTrue(
            any(i.type == "SummaryCountMismatch" and "Review" in i.message for i in issues),
            msg=f"issues: {issues}",
        )

    def test_sync_fixes_stale_review_cell(self):
        root = self._build_repo(review_cell="9")
        counts = vd.collect_status_counts_by_area(root)
        path = root / "Maintainers" / "Content-Backlog.md"
        new_lines, changes = sync_summary_counts.sync_document(path, counts)
        self.assertTrue(changes)
        self.assertIn("| Programming | 1 | 1 | 1 | 출발점 |", new_lines)

    def test_status_columns_detection(self):
        header = ["영역", "현재 Draft", "Review", "남은 Planned", "우선 역할"]
        self.assertEqual(
            sync_summary_counts.status_columns(header),
            {"Draft": 1, "Review": 2, "Planned": 3},
        )


class RealRepoSmokeTest(unittest.TestCase):
    """The real repository must pass full validation."""

    def test_repo_validates(self):
        root = Path(__file__).resolve().parents[2]
        issues, checked = vd.validate(root)
        self.assertEqual(issues, [], msg=f"{len(issues)} issue(s): {issues[:5]}")
        self.assertGreater(checked, 0)


class ReviewFieldTests(unittest.TestCase):
    def setUp(self):
        self.root = Path("repo")
        self.path = self.root / "Programming" / "X.md"

    def _doc(self, status, reviewed=None, badge=None):
        lines = [
            "# X (Title)",
            "",
            "- Level: Beginner",
            "- Prerequisites: 없음",
            f"- Status: {status}",
        ]
        if reviewed is not None:
            lines.append(f"- Reviewed-by: {reviewed}")
        lines += ["", "---", ""]
        if badge is not None:
            lines += [badge, ""]
        return lines

    def test_parse_reviewed_by(self):
        self.assertIsNone(vd.parse_reviewed_by("-"))
        self.assertIsNone(vd.parse_reviewed_by("없음"))
        self.assertIsNone(vd.parse_reviewed_by(""))
        self.assertIsNone(vd.parse_reviewed_by("Alice"))
        self.assertEqual(
            vd.parse_reviewed_by("2ndSilverMan (2026-06-08)"),
            ("2ndSilverMan", "2026-06-08"),
        )

    def test_complete_requires_review(self):
        issues = vd.check_topic_metadata(self.path, self.root, self._doc("Complete", reviewed="-"))
        self.assertTrue(any(i.type == "MissingReview" for i in issues))

    def test_complete_with_review_passes(self):
        issues = vd.check_topic_metadata(self.path, self.root, self._doc("Complete", reviewed="A (2026-01-02)"))
        self.assertFalse(any(i.type == "MissingReview" for i in issues))

    def test_bad_review_format(self):
        issues = vd.check_topic_metadata(self.path, self.root, self._doc("Draft", reviewed="reviewed yesterday"))
        self.assertTrue(any(i.type == "BadReviewFormat" for i in issues))

    def test_badge_matches_field(self):
        lines = self._doc("Review", reviewed="A (2026-01-02)", badge="> ✅ **사람 검토 완료** — A, 2026-01-02")
        self.assertEqual(vd.check_review_badge(self.path, self.root, lines), [])

    def test_badge_missing_when_reviewed(self):
        lines = self._doc("Review", reviewed="A (2026-01-02)")
        issues = vd.check_review_badge(self.path, self.root, lines)
        self.assertTrue(any(i.type == "MissingReviewBadge" for i in issues))

    def test_badge_unexpected_when_not_reviewed(self):
        lines = self._doc("Draft", reviewed="-", badge="> ✅ **사람 검토 완료** — A, 2026-01-02")
        issues = vd.check_review_badge(self.path, self.root, lines)
        self.assertTrue(any(i.type == "UnexpectedReviewBadge" for i in issues))

    def test_badge_stale(self):
        lines = self._doc("Review", reviewed="A (2026-01-02)", badge="> ✅ **사람 검토 완료** — B, 2099-12-31")
        issues = vd.check_review_badge(self.path, self.root, lines)
        self.assertTrue(any(i.type == "StaleReviewBadge" for i in issues))


if __name__ == "__main__":
    unittest.main(verbosity=2)
