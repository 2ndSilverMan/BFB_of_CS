from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from urllib.parse import unquote


VALID_STATUSES = {"Planned", "Stub", "Draft", "Review", "Complete"}
VALID_LEVELS = {"Beginner", "Intermediate", "Advanced"}
TOPIC_METADATA_FIELDS = ("Level", "Prerequisites", "Status")
TOPIC_REQUIRED_HEADINGS = (
    "## 개념",
    "## 직관",
    "## 이론",
    "## 구현",
    "## 복잡도",
    "## 응용",
    "## 흔한 오해",
    "## 연습 / 확인 문제",
    "## 이어서 읽기",
    "## 참조",
)
NON_TOPIC_DIRS = {"Maintainers", "Reference", "Roadmaps", "Templates"}
LEARNING_DIRS = {
    "Programming",
    "Math",
    "Data-Structures",
    "Algorithms",
    "Systems",
    "CS-Theory",
    "AI",
    "Engineering",
}
REQUIRED_MAINTAINER_DOCS = (
    "Maintainers/README.md",
    "Maintainers/Content-Backlog.md",
    "Maintainers/Coverage-Matrix.md",
    "Maintainers/Topic-Classification.md",
    "Maintainers/Reference-Coverage.md",
)
REQUIRED_SUPPORT_FILES = (
    ".gitattributes",
    ".gitignore",
    ".github/workflows/docs.yml",
    "CONTRIBUTING.md",
    "README.md",
    "Reference/README.md",
    "Roadmaps/README.md",
    "Maintainers/Scripts/README.md",
    "Maintainers/Scripts/validate_docs.py",
    "Templates/README.md",
    "Templates/Topic-Template.md",
    "Templates/Topic-Index-README-Template.md",
    "Templates/Section-README-Template.md",
    "Templates/Roadmap-Template.md",
    "Templates/Reference-List-Template.md",
    "Templates/Glossary-Template.md",
)
PLANNING_DOCS = (
    "Maintainers/Content-Backlog.md",
    "Maintainers/Coverage-Matrix.md",
    "Maintainers/Topic-Classification.md",
)
TOPIC_CLASSIFICATION_DOC = "Maintainers/Topic-Classification.md"
REFERENCE_DOCS = {
    "Books": "Reference/Books.md",
    "Courses": "Reference/Courses.md",
    "Papers": "Reference/Papers.md",
}
REFERENCE_COVERAGE_DOC = "Maintainers/Reference-Coverage.md"
REFERENCE_AREA_HEADINGS = {
    "프로그래밍 (Programming)": "Programming",
    "수학 (Math)": "Math",
    "자료구조 (Data Structures)": "Data-Structures",
    "알고리즘 (Algorithms)": "Algorithms",
    "시스템 (Systems)": "Systems",
    "CS 이론 (CS Theory)": "CS-Theory",
    "인공지능 (AI)": "AI",
    "엔지니어링 (Engineering)": "Engineering",
}


@dataclass(frozen=True)
class Issue:
    type: str
    file: str
    line: int
    message: str


def strip_inline_code(line: str) -> str:
    return re.sub(r"`[^`]*`", "", line)


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.parts
    )


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def check_markdown_encoding(path: Path, root: Path) -> list[Issue]:
    if path.read_bytes().startswith(b"\xef\xbb\xbf"):
        return [
            Issue(
                "Utf8Bom",
                relative(path, root),
                1,
                "Remove UTF-8 BOM from Markdown file",
            )
        ]
    return []


def is_external_link_target(target: str) -> bool:
    return re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) is not None


def split_link_target(target: str) -> tuple[str, str | None]:
    target = target.strip()
    angle_match = re.match(r"^<([^>]*)>", target)
    if angle_match:
        target = angle_match.group(1)
    else:
        target = target.split(None, 1)[0]

    path_part, fragment = target, None
    if "#" in target:
        path_part, fragment = target.split("#", 1)
    path_part = path_part.split("?", 1)[0]
    return unquote(path_part.strip()), unquote(fragment.strip()) if fragment is not None else None


def slugify_heading(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[`*_~]", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")


@lru_cache(maxsize=None)
def heading_anchors(path: Path) -> set[str]:
    if not path.exists() or not path.is_file() or path.suffix.lower() != ".md":
        return set()

    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue

        base = slugify_heading(match.group(1))
        if not base:
            continue

        count = counts.get(base, 0)
        anchors.add(base if count == 0 else f"{base}-{count}")
        counts[base] = count + 1

    return anchors


def normalize_anchor_fragment(fragment: str) -> str:
    fragment = fragment.strip().lower()
    if fragment.startswith("user-content-"):
        fragment = fragment.removeprefix("user-content-")
    return fragment


def check_links(path: Path, root: Path, lines: list[str]) -> list[Issue]:
    issues: list[Issue] = []
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

    for line_number, line in enumerate(lines, start=1):
        line_without_code = strip_inline_code(line)
        for match in link_pattern.finditer(line_without_code):
            target = match.group(1).strip()
            if not target:
                continue

            clean_target, fragment = split_link_target(target)
            if clean_target and is_external_link_target(clean_target):
                continue

            resolved = (path.parent / clean_target.replace("\\", "/")).resolve() if clean_target else path.resolve()

            if not resolved.exists():
                issues.append(
                    Issue(
                        "BrokenLink",
                        relative(path, root),
                        line_number,
                        f"Missing target: {target}",
                    )
                )
                continue

            if fragment is None:
                continue

            anchor_path = resolved / "README.md" if resolved.is_dir() else resolved
            anchor = normalize_anchor_fragment(fragment)
            if not anchor:
                continue

            anchors = heading_anchors(anchor_path)
            if anchor not in anchors and slugify_heading(anchor) not in anchors:
                issues.append(
                    Issue(
                        "BrokenAnchor",
                        relative(path, root),
                        line_number,
                        f"Missing anchor: {target}",
                    )
                )

    return issues


def count_table_columns(line: str) -> int:
    return len(split_table_cells(line))


def check_table_shapes(path: Path, root: Path, lines: list[str]) -> list[Issue]:
    issues: list[Issue] = []

    for index in range(len(lines) - 1):
        header = lines[index]
        separator = lines[index + 1]
        if re.match(r"^\|.*\|\s*$", header) and re.match(r"^\|[\s:\-\|]+\|\s*$", separator):
            header_columns = count_table_columns(header)
            separator_columns = count_table_columns(separator)
            if header_columns != separator_columns:
                issues.append(
                    Issue(
                        "TableShape",
                        relative(path, root),
                        index + 1,
                        f"Header has {header_columns} columns, separator has {separator_columns} columns",
                    )
                )

            row = index + 2
            while row < len(lines) and re.match(r"^\|.*\|\s*$", lines[row]):
                if re.match(r"^\|[\s:\-\|]+\|\s*$", lines[row]):
                    row += 1
                    continue

                row_columns = count_table_columns(lines[row])
                if row_columns != header_columns:
                    issues.append(
                        Issue(
                            "TableShape",
                            relative(path, root),
                            row + 1,
                            f"Row has {row_columns} columns, header has {header_columns} columns",
                        )
                    )
                row += 1

    return issues


def split_table_cells(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]

    cells: list[str] = []
    current: list[str] = []
    escaped = False
    in_code = False
    index = 0

    while index < len(stripped):
        char = stripped[index]
        if escaped:
            current.append(char)
            escaped = False
            index += 1
            continue

        if char == "\\":
            current.append(char)
            escaped = True
            index += 1
            continue

        if char == "`":
            tick_start = index
            while index < len(stripped) and stripped[index] == "`":
                index += 1
            current.append(stripped[tick_start:index])
            in_code = not in_code
            continue

        if char == "|" and not in_code:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
        index += 1

    cells.append("".join(current).strip())
    return cells


def clean_file_cell(cell: str) -> str:
    cell = cell.strip().strip("`")
    link_match = re.match(r"\[[^\]]+\]\(([^)]+)\)", cell)
    if link_match:
        return link_match.group(1).strip()
    return cell


def is_topic_doc(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    if len(rel.parts) == 1:
        return False
    if path.name == "README.md":
        return False
    if rel.parts[0] in NON_TOPIC_DIRS:
        return False
    return path.suffix.lower() == ".md"


def metadata_block(lines: list[str]) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for line in lines[:20]:
        if line.strip() == "---":
            break
        match = re.match(r"^-\s*([^:]+):\s*(.*)$", line)
        if match:
            metadata[match.group(1).strip()] = match.group(2).strip()
    return metadata


def topic_table_rows(path: Path, root: Path, lines: list[str]) -> list[tuple[int, str, str]]:
    if path.relative_to(root).parts[0] in NON_TOPIC_DIRS:
        return []

    rows: list[tuple[int, str, str]] = []
    for index, line in enumerate(lines):
        if not re.match(r"^\|.*\|\s*$", line):
            continue

        header_cells = split_table_cells(line)
        if "Status" not in header_cells:
            continue

        file_index = -1
        for candidate in ("파일", "File"):
            if candidate in header_cells:
                file_index = header_cells.index(candidate)
                break
        if file_index < 0:
            continue

        status_index = header_cells.index("Status")
        row = index + 2
        while row < len(lines) and re.match(r"^\|.*\|\s*$", lines[row]):
            if re.match(r"^\|[\s:\-\|]+\|\s*$", lines[row]):
                row += 1
                continue

            row_cells = split_table_cells(lines[row])
            if file_index < len(row_cells) and status_index < len(row_cells):
                filename = clean_file_cell(row_cells[file_index])
                status = row_cells[status_index]
                if filename.endswith(".md"):
                    rows.append((row + 1, filename, status))
            row += 1

    return rows


def is_markdown_link(cell: str) -> bool:
    return re.match(r"^\[[^\]]+\]\([^)]+\)$", cell.strip()) is not None


def check_topic_file_link_policy(path: Path, root: Path, lines: list[str]) -> list[Issue]:
    if path.name != "README.md" or path.relative_to(root).parts[0] in NON_TOPIC_DIRS:
        return []

    issues: list[Issue] = []
    rel = relative(path, root)

    for index, line in enumerate(lines):
        if not re.match(r"^\|.*\|\s*$", line):
            continue

        header_cells = split_table_cells(line)
        if "Status" not in header_cells:
            continue

        file_index = -1
        for candidate in ("파일", "File"):
            if candidate in header_cells:
                file_index = header_cells.index(candidate)
                break
        if file_index < 0:
            continue

        status_index = header_cells.index("Status")
        row = index + 2
        while row < len(lines) and re.match(r"^\|.*\|\s*$", lines[row]):
            if re.match(r"^\|[\s:\-\|]+\|\s*$", lines[row]):
                row += 1
                continue

            row_cells = split_table_cells(lines[row])
            if file_index < len(row_cells) and status_index < len(row_cells):
                file_cell = row_cells[file_index]
                filename = clean_file_cell(file_cell)
                status = row_cells[status_index]

                if filename.endswith(".md") and status != "Planned" and not is_markdown_link(file_cell):
                    issues.append(
                        Issue(
                            "UnlinkedAvailableTopic",
                            rel,
                            row + 1,
                            f"{filename} has status {status}; link the file cell",
                        )
                    )

            row += 1

    return issues


def check_status_values(path: Path, root: Path, lines: list[str]) -> list[Issue]:
    issues: list[Issue] = []

    for index, line in enumerate(lines):
        if not re.match(r"^\|.*\|\s*$", line):
            continue

        cells = split_table_cells(line)
        try:
            status_index = cells.index("Status")
        except ValueError:
            continue

        row = index + 2
        while row < len(lines) and re.match(r"^\|.*\|\s*$", lines[row]):
            if re.match(r"^\|[\s:\-\|]+\|\s*$", lines[row]):
                row += 1
                continue

            row_cells = split_table_cells(lines[row])
            if status_index < len(row_cells):
                status = row_cells[status_index]
                if status and status not in VALID_STATUSES:
                    issues.append(
                        Issue(
                            "BadStatus",
                            relative(path, root),
                            row + 1,
                            f"Invalid status: {status}",
                        )
                    )
            row += 1

    return issues


def check_topic_metadata(path: Path, root: Path, lines: list[str]) -> list[Issue]:
    if not is_topic_doc(path, root):
        return []

    issues: list[Issue] = []
    metadata = metadata_block(lines)
    rel = relative(path, root)

    for field in TOPIC_METADATA_FIELDS:
        if field not in metadata:
            issues.append(Issue("MissingMetadata", rel, 1, f"Missing metadata field: {field}"))

    status = metadata.get("Status")
    if status and status not in VALID_STATUSES:
        issues.append(Issue("BadMetadataStatus", rel, 1, f"Invalid metadata status: {status}"))

    level = metadata.get("Level")
    if level and level not in VALID_LEVELS:
        issues.append(Issue("BadMetadataLevel", rel, 1, f"Invalid metadata level: {level}"))

    prerequisites = metadata.get("Prerequisites", "")
    if status in {"Draft", "Review", "Complete"} and not prerequisites.strip():
        issues.append(Issue("MissingPrerequisites", rel, 1, "Draft or higher topic must declare prerequisites or 없음"))

    if status in {"Draft", "Review", "Complete"}:
        headings = {line.strip() for line in lines if line.startswith("## ")}
        for required in TOPIC_REQUIRED_HEADINGS:
            if not any(heading.startswith(required) for heading in headings):
                issues.append(Issue("MissingHeading", rel, 1, f"Missing required heading: {required}"))

    return issues


def check_topic_table_consistency(path: Path, root: Path, lines: list[str]) -> list[Issue]:
    issues: list[Issue] = []
    rel = relative(path, root)

    for line_number, filename, status in topic_table_rows(path, root, lines):
        target = path.parent / filename
        exists = target.exists()

        if status == "Planned" and exists:
            issues.append(
                Issue(
                    "PlannedFileExists",
                    rel,
                    line_number,
                    f"{filename} exists but table status is Planned",
                )
            )
            continue

        if status != "Planned" and not exists:
            issues.append(
                Issue(
                    "MissingTopicFile",
                    rel,
                    line_number,
                    f"{filename} has status {status} but file is missing",
                )
            )
            continue

        if exists and is_topic_doc(target, root):
            target_lines = target.read_text(encoding="utf-8").splitlines()
            target_status = metadata_block(target_lines).get("Status")
            if target_status and target_status != status:
                issues.append(
                    Issue(
                        "StatusMismatch",
                        rel,
                        line_number,
                        f"{filename} table status is {status}, metadata status is {target_status}",
                    )
                )

    return issues


def check_required_maintainer_docs(root: Path) -> list[Issue]:
    issues: list[Issue] = []

    for relative_path in REQUIRED_MAINTAINER_DOCS:
        if not (root / relative_path).exists():
            issues.append(
                Issue(
                    "MissingMaintainerDoc",
                    relative_path,
                    1,
                    "Required maintainer planning document is missing",
                )
            )

    return issues


def check_required_support_files(root: Path) -> list[Issue]:
    issues: list[Issue] = []

    for relative_path in REQUIRED_SUPPORT_FILES:
        if not (root / relative_path).exists():
            issues.append(
                Issue(
                    "MissingSupportFile",
                    relative_path,
                    1,
                    "Required project support file is missing",
                )
            )

    return issues


def check_no_root_scripts_directory(root: Path) -> list[Issue]:
    scripts_path = root / "Scripts"
    if scripts_path.exists():
        return [
            Issue(
                "RootScriptsDirectory",
                "Scripts",
                1,
                "Keep maintainer scripts under Maintainers/Scripts/ so learners do not see Scripts/ as a study area",
            )
        ]
    return []


def has_heading(lines: list[str], heading: str) -> bool:
    return any(line.strip() == heading for line in lines)


def has_status_table(lines: list[str]) -> bool:
    return any(
        re.match(r"^\|.*\|\s*$", line)
        and "Status" in split_table_cells(line)
        for line in lines
    )


def has_root_status_meaning_table(lines: list[str]) -> bool:
    for index, line in enumerate(lines):
        header_cells = split_table_cells(line)
        if header_cells != ["상태", "학습자에게 의미"]:
            continue

        if index + 1 >= len(lines):
            return False

        separator_cells = split_table_cells(lines[index + 1])
        if not separator_cells or len(separator_cells) != len(header_cells):
            return False

        seen_statuses: set[str] = set()
        row = index + 2
        while row < len(lines) and re.match(r"^\|.*\|\s*$", lines[row]):
            row_cells = split_table_cells(lines[row])
            if len(row_cells) >= 2 and row_cells[0] in VALID_STATUSES and row_cells[1]:
                seen_statuses.add(row_cells[0])
            row += 1

        return seen_statuses == VALID_STATUSES

    return False


def check_learner_availability_guidance(path: Path, root: Path, lines: list[str]) -> list[Issue]:
    issues: list[Issue] = []
    rel = path.relative_to(root)
    rel_text = rel.as_posix()

    if rel_text == "README.md":
        if not has_root_status_meaning_table(lines):
            issues.append(
                Issue(
                    "MissingLearnerStatusExplanation",
                    rel_text,
                    1,
                    "Root README must include a learner-facing status table for Planned, Stub, Draft, Review, and Complete",
                )
            )
        return issues

    if len(rel.parts) >= 1 and rel.parts[0] == "Roadmaps" and path.name.endswith(".md"):
        if not has_heading(lines, "## 현재 가용성"):
            issues.append(
                Issue(
                    "MissingRoadmapAvailability",
                    rel_text,
                    1,
                    "Roadmap documents must explain current learner availability",
                )
            )
        return issues

    if path.name == "README.md" and len(rel.parts) >= 1 and rel.parts[0] in LEARNING_DIRS:
        has_learner_heading = has_heading(lines, "## 읽는 법") or has_heading(lines, "## 현재 가용성")
        if not has_learner_heading:
            issues.append(
                Issue(
                    "MissingLearnerAvailabilityGuide",
                    rel_text,
                    1,
                    "Learning README must distinguish currently readable docs from planned topics",
                )
            )
        if has_status_table(lines):
            text = "\n".join(lines)
            if "`Draft`" not in text or "`Planned`" not in text:
                issues.append(
                    Issue(
                        "MissingStatusGuideTerms",
                        rel_text,
                        1,
                        "README with a Status table must explain `Draft` and `Planned` for learners",
                    )
                )

    return issues


def check_learning_directory_readmes(root: Path) -> list[Issue]:
    issues: list[Issue] = []

    for area in sorted(LEARNING_DIRS):
        area_path = root / area
        if not area_path.exists() or not area_path.is_dir():
            issues.append(
                Issue(
                    "MissingLearningDirectory",
                    area,
                    1,
                    "Required learning directory is missing",
                )
            )
            continue

        for directory in sorted(path for path in area_path.rglob("*") if path.is_dir() and not path.name.startswith(".")):
            readme = directory / "README.md"
            if not readme.exists():
                issues.append(
                    Issue(
                        "MissingDirectoryReadme",
                        relative(directory, root),
                        1,
                        "Learning directory must contain README.md",
                    )
                )

        if not (area_path / "README.md").exists():
            issues.append(
                Issue(
                    "MissingDirectoryReadme",
                    area,
                    1,
                    "Learning directory must contain README.md",
                )
            )

    return issues


def collect_topic_table_entries(root: Path) -> dict[str, list[tuple[str, int, str]]]:
    entries: dict[str, list[tuple[str, int, str]]] = {}

    for path in markdown_files(root):
        if path.name != "README.md":
            continue

        lines = path.read_text(encoding="utf-8").splitlines()
        for line_number, filename, status in topic_table_rows(path, root, lines):
            basename = Path(filename).name
            entries.setdefault(basename, []).append((relative(path, root), line_number, status))

    return entries


def check_duplicate_topic_filenames(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    entries = collect_topic_table_entries(root)

    for filename, locations in sorted(entries.items()):
        if len(locations) <= 1:
            continue

        first_file, first_line, _ = locations[0]
        location_text = ", ".join(f"{file}:{line}" for file, line, _ in locations)
        issues.append(
            Issue(
                "DuplicateTopicFilename",
                first_file,
                first_line,
                f"{filename} appears in multiple topic tables: {location_text}",
            )
        )

    return issues


def collect_status_counts_by_area(root: Path) -> dict[str, dict[str, int]]:
    counts: dict[str, dict[str, int]] = {}

    for path in markdown_files(root):
        if path.name != "README.md":
            continue
        if path.relative_to(root).parts[0] in NON_TOPIC_DIRS:
            continue

        area = path.relative_to(root).parts[0]
        lines = path.read_text(encoding="utf-8").splitlines()
        for _, _, status in topic_table_rows(path, root, lines):
            if status in VALID_STATUSES:
                area_counts = counts.setdefault(area, {})
                area_counts[status] = area_counts.get(status, 0) + 1

    return counts


def parse_int_cell(cell: str) -> int | None:
    match = re.search(r"\d+", cell)
    if not match:
        return None
    return int(match.group(0))


def check_maintainer_summary_counts(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    counts = collect_status_counts_by_area(root)

    for relative_path in ("Maintainers/Content-Backlog.md", "Maintainers/Coverage-Matrix.md"):
        path = root / relative_path
        if not path.exists():
            continue

        lines = path.read_text(encoding="utf-8").splitlines()
        seen_areas: set[str] = set()
        summary_table_line = 1
        for index, line in enumerate(lines):
            if not re.match(r"^\|.*\|\s*$", line):
                continue

            header_cells = split_table_cells(line)
            if not header_cells or header_cells[0] != "영역":
                continue

            summary_table_line = index + 1
            draft_index = next((i for i, cell in enumerate(header_cells) if "Draft" in cell), -1)
            planned_index = next((i for i, cell in enumerate(header_cells) if "Planned" in cell), -1)
            if draft_index < 0 or planned_index < 0:
                continue

            row = index + 2
            while row < len(lines) and re.match(r"^\|.*\|\s*$", lines[row]):
                if re.match(r"^\|[\s:\-\|]+\|\s*$", lines[row]):
                    row += 1
                    continue

                row_cells = split_table_cells(lines[row])
                if max(draft_index, planned_index) < len(row_cells):
                    area = row_cells[0]
                    if area:
                        seen_areas.add(area)
                    if area not in counts:
                        issues.append(
                            Issue(
                                "UnexpectedSummaryArea",
                                relative_path,
                                row + 1,
                                f"{area} is not a current top-level section",
                            )
                        )
                    else:
                        expected_draft = counts[area].get("Draft", 0)
                        expected_planned = counts[area].get("Planned", 0)
                        actual_draft = parse_int_cell(row_cells[draft_index])
                        actual_planned = parse_int_cell(row_cells[planned_index])

                        if actual_draft != expected_draft:
                            issues.append(
                                Issue(
                                    "SummaryCountMismatch",
                                    relative_path,
                                    row + 1,
                                    f"{area} Draft is {actual_draft}, expected {expected_draft}",
                                )
                            )
                        if actual_planned != expected_planned:
                            issues.append(
                                Issue(
                                    "SummaryCountMismatch",
                                    relative_path,
                                    row + 1,
                                    f"{area} Planned is {actual_planned}, expected {expected_planned}",
                                )
                            )

                row += 1

        for area in sorted(set(counts) - seen_areas):
            issues.append(
                Issue(
                    "MissingSummaryArea",
                    relative_path,
                    summary_table_line,
                    f"{area} is missing from summary table",
                )
            )

    return issues


def reference_area_totals(root: Path) -> dict[str, int]:
    totals: dict[str, int] = {}

    for area in REFERENCE_AREA_HEADINGS.values():
        area_path = root / area
        if not area_path.exists() or not area_path.is_dir():
            continue

        subdirectories = [
            path
            for path in area_path.iterdir()
            if path.is_dir() and not path.name.startswith(".")
        ]
        totals[area] = len(subdirectories) if subdirectories else 1

    return totals


def reference_area_from_heading(line: str) -> str | None:
    match = re.match(r"^##\s+(.+?)\s*$", line)
    if not match:
        return None
    return REFERENCE_AREA_HEADINGS.get(match.group(1).strip())


def markdown_link_targets(cell: str) -> list[str]:
    return [match.group(1).strip() for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", cell)]


def markdown_file_link_references(line: str) -> list[str]:
    references: list[str] = []
    for target in markdown_link_targets(line):
        clean_target, _ = split_link_target(target)
        if clean_target.endswith(".md") and not is_external_link_target(clean_target):
            references.append(Path(clean_target).name)
    return references


def normalized_reference_target(target: str) -> str:
    target = target.split("#", 1)[0].replace("\\", "/").strip()
    while target.startswith("../"):
        target = target[3:]
    return target.strip("/")


def reference_coverage_key(area: str, target: str, totals: dict[str, int]) -> str | None:
    normalized = normalized_reference_target(target)
    if not normalized:
        return None

    if totals.get(area, 0) <= 1:
        if normalized == area or normalized.startswith(f"{area}/"):
            return area
        return None

    if not normalized.startswith(f"{area}/"):
        return None

    parts = normalized.split("/")
    if len(parts) < 2:
        return None
    return f"{parts[0]}/{parts[1]}"


def collect_reference_coverage(root: Path) -> dict[str, dict[str, tuple[int, int, int]]]:
    totals = reference_area_totals(root)
    coverage: dict[str, dict[str, tuple[int, int, int]]] = {}

    for label, relative_path in REFERENCE_DOCS.items():
        path = root / relative_path
        if not path.exists():
            continue

        area_items: dict[str, int] = {}
        area_covered: dict[str, set[str]] = {}
        current_area: str | None = None
        lines = path.read_text(encoding="utf-8").splitlines()

        for index, line in enumerate(lines):
            heading_area = reference_area_from_heading(line)
            if heading_area:
                current_area = heading_area
                continue

            if current_area is None or not re.match(r"^\|.*\|\s*$", line):
                continue

            header_cells = split_table_cells(line)
            if "섹션" not in header_cells:
                continue

            section_index = header_cells.index("섹션")
            row = index + 2
            while row < len(lines) and re.match(r"^\|.*\|\s*$", lines[row]):
                if re.match(r"^\|[\s:\-\|]+\|\s*$", lines[row]):
                    row += 1
                    continue

                row_cells = split_table_cells(lines[row])
                if section_index < len(row_cells):
                    area_items[current_area] = area_items.get(current_area, 0) + 1
                    covered = area_covered.setdefault(current_area, set())
                    for target in markdown_link_targets(row_cells[section_index]):
                        key = reference_coverage_key(current_area, target, totals)
                        if key:
                            covered.add(key)

                row += 1

        coverage[label] = {
            area: (len(area_covered.get(area, set())), totals.get(area, 0), area_items.get(area, 0))
            for area in totals
        }

    return coverage


def parse_reference_coverage_cell(cell: str) -> tuple[int, int, int] | None:
    match = re.match(r"^(\d+)/(\d+)\s+\((\d+)\)\*?$", cell.strip())
    if not match:
        return None
    return (int(match.group(1)), int(match.group(2)), int(match.group(3)))


def check_reference_coverage_summary(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    path = root / REFERENCE_COVERAGE_DOC
    if not path.exists():
        return issues

    expected = collect_reference_coverage(root)
    expected_areas = set(reference_area_totals(root))
    lines = path.read_text(encoding="utf-8").splitlines()

    seen_areas: set[str] = set()
    for index, line in enumerate(lines):
        if not re.match(r"^\|.*\|\s*$", line):
            continue

        header_cells = split_table_cells(line)
        if not header_cells or header_cells[0] != "섹션":
            continue

        label_indexes = {
            label: header_cells.index(label)
            for label in REFERENCE_DOCS
            if label in header_cells
        }
        row = index + 2
        while row < len(lines) and re.match(r"^\|.*\|\s*$", lines[row]):
            if re.match(r"^\|[\s:\-\|]+\|\s*$", lines[row]):
                row += 1
                continue

            row_cells = split_table_cells(lines[row])
            if row_cells:
                area = row_cells[0]
                seen_areas.add(area)
                if area not in expected_areas:
                    issues.append(
                        Issue(
                            "UnexpectedReferenceCoverageArea",
                            REFERENCE_COVERAGE_DOC,
                            row + 1,
                            f"{area} is not a current top-level section",
                        )
                    )

                for label, label_index in label_indexes.items():
                    if label_index >= len(row_cells):
                        continue

                    actual = parse_reference_coverage_cell(row_cells[label_index])
                    expected_for_label = expected.get(label, {}).get(area)
                    if actual is None:
                        issues.append(
                            Issue(
                                "ReferenceCoverageShape",
                                REFERENCE_COVERAGE_DOC,
                                row + 1,
                                f"{label} cell must be formatted as covered/total (items)",
                            )
                        )
                    elif expected_for_label and actual != expected_for_label:
                        issues.append(
                            Issue(
                                "ReferenceCoverageMismatch",
                                REFERENCE_COVERAGE_DOC,
                                row + 1,
                                f"{area} {label} is {actual[0]}/{actual[1]} ({actual[2]}), expected {expected_for_label[0]}/{expected_for_label[1]} ({expected_for_label[2]})",
                            )
                        )

            row += 1

    for area in sorted(set(reference_area_totals(root)) - seen_areas):
        issues.append(
            Issue(
                "MissingReferenceCoverageArea",
                REFERENCE_COVERAGE_DOC,
                1,
                f"{area} is missing from reference coverage summary",
            )
        )

    return issues


def check_planning_doc_references(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    entries = collect_topic_table_entries(root)
    planned = {
        filename
        for filename, locations in entries.items()
        if any(status == "Planned" for _, _, status in locations)
    }
    referenced: set[str] = set()
    required_refs: dict[str, list[tuple[str, int]]] = {}
    classified_refs: dict[str, list[tuple[int, str]]] = {}
    code_ref_pattern = re.compile(r"`([^`]+\.md)`")

    for relative_path in PLANNING_DOCS:
        path = root / relative_path
        if not path.exists():
            continue

        lines = path.read_text(encoding="utf-8").splitlines()
        classification = ""
        for line_number, line in enumerate(lines, start=1):
            heading_match = re.match(r"^##\s+(.+?)\s*$", line)
            if relative_path == TOPIC_CLASSIFICATION_DOC and heading_match:
                classification = heading_match.group(1).strip()

            code_references = [(match.group(1).strip(), True) for match in code_ref_pattern.finditer(line)]
            link_references = [(reference, False) for reference in markdown_file_link_references(line)]

            for reference, is_code_reference in code_references + link_references:
                basename = Path(reference).name

                if is_code_reference and ("/" in reference or "\\" in reference):
                    issues.append(
                        Issue(
                            "PathLikePlanningRef",
                            relative_path,
                            line_number,
                            f"Use a bare topic filename instead of a path-like code span: {reference}",
                        )
                    )

                if basename not in entries:
                    if not is_code_reference:
                        continue
                    issues.append(
                        Issue(
                            "UnknownPlanningRef",
                            relative_path,
                            line_number,
                            f"{reference} is not listed in any topic README table",
                        )
                    )
                    continue

                referenced.add(basename)
                if relative_path == TOPIC_CLASSIFICATION_DOC and classification in {"Optional", "Deferred"}:
                    classified_refs.setdefault(basename, []).append((line_number, classification))
                elif relative_path != TOPIC_CLASSIFICATION_DOC:
                    required_refs.setdefault(basename, []).append((relative_path, line_number))

    for filename in sorted(planned - referenced):
        first_file, first_line, _ = entries[filename][0]
        issues.append(
            Issue(
                "UnclassifiedPlannedTopic",
                first_file,
                first_line,
                f"{filename} is Planned but not classified in planning docs",
            )
        )

    for filename, locations in sorted(classified_refs.items()):
        classifications = {classification for _, classification in locations}
        if len(classifications) > 1:
            first_line = locations[0][0]
            issues.append(
                Issue(
                    "MultipleTopicClassification",
                    TOPIC_CLASSIFICATION_DOC,
                    first_line,
                    f"{filename} appears in multiple classifications: {', '.join(sorted(classifications))}",
                )
            )

        if filename in required_refs:
            required_locations = ", ".join(f"{file}:{line}" for file, line in required_refs[filename])
            for line_number, classification in locations:
                issues.append(
                    Issue(
                        "PlanningClassificationConflict",
                        TOPIC_CLASSIFICATION_DOC,
                        line_number,
                        f"{filename} is {classification} but also Required in {required_locations}",
                    )
                )

    return issues


def validate(root: Path) -> tuple[list[Issue], int]:
    root = root.resolve()
    files = markdown_files(root)
    issues: list[Issue] = check_required_maintainer_docs(root)
    issues.extend(check_required_support_files(root))
    issues.extend(check_no_root_scripts_directory(root))
    issues.extend(check_learning_directory_readmes(root))
    issues.extend(check_duplicate_topic_filenames(root))
    issues.extend(check_planning_doc_references(root))
    issues.extend(check_maintainer_summary_counts(root))
    issues.extend(check_reference_coverage_summary(root))

    for path in files:
        issues.extend(check_markdown_encoding(path, root))
        lines = path.read_text(encoding="utf-8").splitlines()
        issues.extend(check_links(path, root, lines))
        issues.extend(check_table_shapes(path, root, lines))
        issues.extend(check_status_values(path, root, lines))
        issues.extend(check_learner_availability_guidance(path, root, lines))
        issues.extend(check_topic_file_link_policy(path, root, lines))
        issues.extend(check_topic_metadata(path, root, lines))
        issues.extend(check_topic_table_consistency(path, root, lines))

    return sorted(issues, key=lambda issue: (issue.type, issue.file, issue.line)), len(files)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Markdown docs.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Repository root. Defaults to the parent of Maintainers/.",
    )
    args = parser.parse_args()

    issues, checked_count = validate(args.root)
    if issues:
        for issue in issues:
            print(f"{issue.type}\t{issue.file}:{issue.line}\t{issue.message}")
        return 1

    print(f"Documentation validation passed: {checked_count} Markdown files checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
