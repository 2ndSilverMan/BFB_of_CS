"""Synchronize the status-count summary tables in the maintainer planning docs.

The summary tables in `Maintainers/Content-Backlog.md` and
`Maintainers/Coverage-Matrix.md` repeat per-area counts (Draft, Planned, and
optionally Review/Complete/Stub) that must match the topic tables in every
section README. Keeping them in sync by hand is error-prone, and
`validate_docs.py` only *checks* the counts — it does not fix them.

This script recomputes the counts from the section README tables (reusing the
exact same logic as the validator) and rewrites only the numeric status cells
of each summary table. Non-status columns (역할 / 우선 역할 etc.) are preserved
verbatim.

Usage:
    python Maintainers/Scripts/sync_summary_counts.py            # write changes
    python Maintainers/Scripts/sync_summary_counts.py --check     # CI: fail if stale
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from validate_docs import (
    VALID_STATUSES,
    collect_status_counts_by_area,
    split_table_cells,
)


SUMMARY_DOCS = (
    "Maintainers/Content-Backlog.md",
    "Maintainers/Coverage-Matrix.md",
)
SUMMARY_HEADER_FIRST_CELL = "영역"
SEPARATOR_RE = re.compile(r"^\|[\s:\-\|]+\|\s*$")
TABLE_ROW_RE = re.compile(r"^\|.*\|\s*$")


def render_row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def status_columns(header_cells: list[str]) -> dict[str, int]:
    """Map each status keyword to the column index whose header contains it."""
    columns: dict[str, int] = {}
    for index, cell in enumerate(header_cells):
        for status in VALID_STATUSES:
            if status in cell:
                columns[status] = index
    return columns


def sync_document(
    path: Path,
    counts: dict[str, dict[str, int]],
) -> tuple[list[str], list[str]]:
    """Return (new_lines, change_descriptions) for one planning doc."""
    lines = path.read_text(encoding="utf-8").splitlines()
    changes: list[str] = []

    index = 0
    while index < len(lines):
        line = lines[index]
        if not TABLE_ROW_RE.match(line):
            index += 1
            continue

        header_cells = split_table_cells(line)
        if not header_cells or header_cells[0] != SUMMARY_HEADER_FIRST_CELL:
            index += 1
            continue

        columns = status_columns(header_cells)
        if not columns:
            index += 1
            continue

        row = index + 2  # skip header + separator
        while row < len(lines) and TABLE_ROW_RE.match(lines[row]):
            if SEPARATOR_RE.match(lines[row]):
                row += 1
                continue

            row_cells = split_table_cells(lines[row])
            area = row_cells[0] if row_cells else ""
            if area in counts:
                changed = False
                for status, col_index in columns.items():
                    if col_index >= len(row_cells):
                        continue
                    expected = str(counts[area].get(status, 0))
                    if row_cells[col_index] != expected:
                        changes.append(
                            f"{path.name}: {area} {status} {row_cells[col_index]} -> {expected}"
                        )
                        row_cells[col_index] = expected
                        changed = True
                if changed:
                    lines[row] = render_row(row_cells)
            row += 1

        index = row

    return lines, changes


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync summary count tables.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Repository root. Defaults to the parent of Maintainers/.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write; exit 1 if any summary table is stale.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    counts = collect_status_counts_by_area(root)

    all_changes: list[str] = []
    for relative_path in SUMMARY_DOCS:
        path = root / relative_path
        if not path.exists():
            continue

        new_lines, changes = sync_document(path, counts)
        all_changes.extend(changes)
        if changes and not args.check:
            path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

    if not all_changes:
        print("Summary count tables already in sync.")
        return 0

    for change in all_changes:
        print(change)

    if args.check:
        print(f"\n{len(all_changes)} stale cell(s). Run sync_summary_counts.py to fix.")
        return 1

    print(f"\nUpdated {len(all_changes)} cell(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
