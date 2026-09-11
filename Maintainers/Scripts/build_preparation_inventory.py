"""Inventory reusable Markdown material without judging or executing its content.

By default print Markdown; --write updates Maintainers/Preparation-Inventory.md,
--check detects a stale report, and --format json exports migration evidence.
Only Python's standard library is required. No network requests are made.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import ipaddress
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote, urlsplit

from validate_docs import LEARNING_DIRS, is_topic_doc, markdown_files, metadata_block


REPORT_PATH = Path("Maintainers/Preparation-Inventory.md")
NOTES_HEADING = "재작성 메모 (Rewrite Notes)"
REFERENCE_HEADINGS = {"참조", "참조 (References)", "References"}
NON_IMPLEMENTATION_LANGUAGES = {
    "", "text", "txt", "plaintext", "plain", "none", "mermaid", "math", "latex", "tex",
}
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
LABEL_RE = re.compile(r"(?<!\\)\[([^\[\]\n]+)\]")
DEFINITION_RE = re.compile(r"^ {0,3}\[([^\]]+)\]:\s*(.*)$")
INLINE_CODE_RE = re.compile(r"(?<!`)(`+)(?!`)(.*?)(?<!`)\1(?!`)")


def visible_markdown(text: str) -> tuple[list[str], list[dict]]:
    """Remove comments/code while keeping line numbers and fence evidence.

    Recognizes backtick/tilde fences with up to three leading spaces, as used
    by this repository. Indented code is excluded from prose, not inventoried.
    This is a focused scanner, not a complete CommonMark renderer.
    """
    visible: list[str] = []
    blocks: list[dict] = []
    active: tuple[str, int] | None = None
    in_comment = False
    for number, raw in enumerate(text.splitlines(), 1):
        if active is not None:
            fence_char, fence_size = active
            if re.fullmatch(r" {0,3}" + re.escape(fence_char) + "{" + str(fence_size) + r",}\s*", raw):
                blocks[-1]["end_line"] = number
                blocks[-1]["closed"] = True
                active = None
            visible.append("")
            continue

        # Remove comments before interpreting a fence, but do not let a comment
        # marker inside an inline code span hide subsequent document content.
        # Keep a nonempty, markup-free token so [`svd`](url) stays a link.
        # Encoding the span also keeps different code-only reference labels
        # distinct while hiding any fake link syntax inside the code itself.
        line = INLINE_CODE_RE.sub(
            lambda match: "\ufffc" + match.group(0).encode("utf-8").hex(), raw
        ) if not FENCE_RE.match(raw) else raw
        parts: list[str] = []
        cursor = 0
        while cursor < len(line):
            if in_comment:
                end = line.find("-->", cursor)
                if end < 0:
                    break
                in_comment = False
                cursor = end + 3
            else:
                start = line.find("<!--", cursor)
                if start < 0:
                    parts.append(line[cursor:])
                    break
                parts.append(line[cursor:start])
                in_comment = True
                cursor = start + 4
        line = "".join(parts)
        fence = FENCE_RE.match(line)
        if fence and not (fence.group(1)[0] == "`" and "`" in fence.group(2)):
            marker, info = fence.groups()
            language = info.strip().split(None, 1)[0].lower() if info.strip() else ""
            blocks.append({
                "line": number,
                "end_line": None,
                "language": language or "unspecified",
                "closed": False,
                "implementation_candidate": language not in NON_IMPLEMENTATION_LANGUAGES,
            })
            active = (marker[0], len(marker))
            visible.append("")
        elif line.startswith(("    ", "\t")):
            visible.append("")
        else:
            visible.append(line)
    return visible, blocks


def destination(text: str, start: int = 0) -> tuple[str, int] | None:
    """Read a link destination, including balanced parentheses or angle form."""
    while start < len(text) and text[start].isspace():
        start += 1
    if start >= len(text):
        return None
    if text[start] == "<":
        end = text.find(">", start + 1)
        return (text[start + 1:end], end + 1) if end >= 0 else None
    cursor = start
    depth = 0
    while cursor < len(text):
        char = text[cursor]
        if char == "\\" and cursor + 1 < len(text):
            cursor += 2
            continue
        if char.isspace() or (char == ")" and depth == 0):
            break
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
        cursor += 1
    if depth or cursor == start:
        return None
    return re.sub(r"\\([()<>])", r"\1", text[start:cursor]), cursor


def reference_label(label: str) -> str:
    return " ".join(label.split()).casefold()


def is_source_url(url: str) -> bool:
    """Accept HTTP(S) destinations except reserved example/local addresses."""
    try:
        parsed = urlsplit(url)
        hostname = (parsed.hostname or "").lower().rstrip(".")
    except ValueError:
        return False
    if parsed.scheme.lower() not in {"http", "https"} or not hostname:
        return False
    for reserved in ("example.com", "example.org", "example.net", "example", "invalid", "test", "localhost"):
        if hostname == reserved or hostname.endswith("." + reserved):
            return False
    try:
        if not ipaddress.ip_address(hostname).is_global:
            return False
    except ValueError:
        pass
    return True


def source_links(lines: list[str]) -> list[dict]:
    """Collect distinct explicit Markdown URLs used inside References sections.

    Definitions may be elsewhere, but must be used in the section. Inline,
    full/collapsed/shortcut reference links and angle autolinks are supported.
    Images, bare URLs and reference definitions alone are not citations.
    """
    definitions: dict[str, str] = {}
    for line in lines:
        match = DEFINITION_RE.match(line)
        if match:
            target = destination(match.group(2))
            if target:
                definitions.setdefault(reference_label(match.group(1)), target[0])

    found: dict[str, set[int]] = {}
    in_references = False
    for number, line in enumerate(lines, 1):
        heading = HEADING_RE.match(line)
        if heading and len(heading.group(1)) <= 2:
            in_references = len(heading.group(1)) == 2 and heading.group(2) in REFERENCE_HEADINGS
        if not in_references or heading or DEFINITION_RE.match(line):
            continue
        urls: list[str] = []
        consumed_until = 0
        inline_ranges: list[tuple[int, int]] = []
        for match in LABEL_RE.finditer(line):
            if match.start() < consumed_until:
                continue
            cursor = match.end()
            label = match.group(1)
            is_image = match.start() > 0 and line[match.start() - 1] == "!"
            if line[cursor:cursor + 1] == "(":
                target = destination(line, cursor + 1)
                if target:
                    rest = line[target[1]:]
                    # Permit an optional quoted title, but require a closing ')'.
                    closing = re.match(r'''^\s*(?:"[^"\n]*"|'[^'\n]*'|\([^()\n]*\))?\s*\)''', rest)
                    if closing:
                        consumed_until = target[1] + closing.end()
                        inline_ranges.append((match.start(), consumed_until))
                        if not is_image:
                            urls.append(target[0])
            elif line[cursor:cursor + 1] == "[":
                end = line.find("]", cursor + 1)
                if end >= 0:
                    consumed_until = end + 1
                    key = reference_label(line[cursor + 1:end] or label)
                    if not is_image and key in definitions:
                        urls.append(definitions[key])
            else:
                key = reference_label(label)
                if not is_image and key in definitions:
                    urls.append(definitions[key])
        for autolink in re.finditer(r"(?<!\\)<(https?://[^<>\s]+)>", line, re.IGNORECASE):
            if not any(start <= autolink.start() < end for start, end in inline_ranges):
                urls.append(autolink.group(1))
        for url in urls:
            if is_source_url(url):
                found.setdefault(url, set()).add(number)
    return [{"url": url, "lines": sorted(found[url])} for url in sorted(found)]


def inspect_topic(path: Path, root: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    lines, blocks = visible_markdown(text)
    sources = source_links(lines)
    note_lines = [
        number for number, line in enumerate(lines, 1)
        if (heading := HEADING_RE.match(line))
        and heading.group(1) == "##" and heading.group(2) == NOTES_HEADING
    ]
    flags = []
    if not sources:
        flags.append("missing-source")
    if not note_lines:
        flags.append("missing-notes")
    if any(not block["closed"] for block in blocks):
        flags.append("unclosed-code-fence")
    return {
        "path": path.relative_to(root).as_posix(),
        "area": path.relative_to(root).parts[0],
        "status": metadata_block(lines).get("Status", "Unknown"),
        "content_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "sources": sources,
        "direct_source_count": len(sources),
        "code_blocks": blocks,
        "code_language_counts": dict(sorted(Counter(block["language"] for block in blocks).items())),
        "implementation_block_count": sum(block["implementation_candidate"] for block in blocks),
        "has_rewrite_notes": bool(note_lines),
        "rewrite_notes_lines": note_lines,
        "flags": flags,
    }


def summarize(topics: list[dict]) -> dict:
    return {
        "topic_count": len(topics),
        "with_direct_sources": sum(bool(topic["sources"]) for topic in topics),
        "without_direct_sources": sum(not topic["sources"] for topic in topics),
        "unique_source_urls": len({source["url"] for topic in topics for source in topic["sources"]}),
        "implementation_block_count": sum(topic["implementation_block_count"] for topic in topics),
        "with_implementation_blocks": sum(bool(topic["implementation_block_count"]) for topic in topics),
        "with_rewrite_notes": sum(topic["has_rewrite_notes"] for topic in topics),
        "without_rewrite_notes": sum(not topic["has_rewrite_notes"] for topic in topics),
        "status_counts": dict(sorted(Counter(topic["status"] for topic in topics).items())),
    }


def build_inventory(root: Path) -> dict:
    root = root.resolve()
    topics = [
        inspect_topic(path, root) for path in markdown_files(root)
        if path.relative_to(root).parts[0] in LEARNING_DIRS and is_topic_doc(path, root)
    ]
    return {
        "schema_version": 1,
        "generator": "Maintainers/Scripts/build_preparation_inventory.py",
        "definitions": {
            "direct_sources": "Distinct literal HTTP(S) Markdown link destinations used in H2 References/참조 sections; excludes code, comments, images, bare URLs and reserved example/local hosts. URL availability and support for claims are not checked.",
            "implementation_blocks": "Fences with a language other than unspecified, text/txt/plaintext/plain/none, mermaid, math/latex/tex; these are candidates, not verified executable examples.",
            "rewrite_notes": "Presence of H2 재작성 메모 (Rewrite Notes), not an assessment of its contents.",
            "content_sha256": "SHA-256 of UTF-8 source text with line endings normalized to LF.",
            "scope": "Existing topic Markdown files in learning directories, following validate_docs.is_topic_doc; README and planned-but-absent files are excluded.",
            "limitations": "Focused Markdown scanner, not a full CommonMark parser; top-level ATX sections and fences with up to 3 leading spaces. No correctness, execution or human-review assessment.",
        },
        "summary": summarize(topics),
        "areas": {area: summarize([topic for topic in topics if topic["area"] == area]) for area in sorted({topic["area"] for topic in topics})},
        "topics": topics,
    }


def table_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def render_markdown(inventory: dict) -> str:
    total = inventory["summary"]
    lines = [
        "# 재작성 준비 인벤토리 (Preparation Inventory)",
        "",
        "새 문서 프로젝트로 옮길 재료와 추가 조사 대상을 찾기 위한 자동 생성 목록입니다.",
        "출처 수·구현 후보 수·메모 유무는 관측값이며, 정확성·실행 성공·사람 검토·문서 완성도를 뜻하지 않습니다.",
        "",
        "## 집계 기준",
        "",
        "- 범위: 학습 영역의 실제 주제 Markdown 파일. README와 아직 파일이 없는 Planned 항목은 제외합니다.",
        "- 직접 출처: `## 참조`, `## 참조 (References)`, `## References` 아래에서 사용하는 명시적 HTTP(S) Markdown 링크의 서로 다른 URL 수입니다. 하위 섹션도 포함합니다.",
        "- 인라인·참조형·각괄호 자동링크를 인식합니다. 코드·HTML 주석·이미지·단독 URL·예약 예시 도메인·로컬 주소는 제외합니다. 같은 URL의 반복은 한 번만 세며, URL의 fragment/query가 다르면 별도로 셉니다.",
        "- 링크가 살아 있는지, 원문이 주장을 뒷받침하는지는 확인하지 않습니다. 본문에만 있는 외부 링크와 중앙 참고목록을 가리키는 상대링크는 직접 출처 수에 포함하지 않습니다.",
        "- 구현 후보: 언어가 지정된 코드 fence 수에서 텍스트(text/txt/plaintext/plain/none), Mermaid, 수식(math/latex/tex)을 제외합니다. 셸 명령·설정·의사코드도 포함될 수 있으며 실행하지 않습니다.",
        "- 메모: `## 재작성 메모 (Rewrite Notes)` 제목의 존재 여부입니다. 내용의 충실도는 판단하지 않습니다.",
        "- `missing-source`·`missing-notes`는 집계 대상 링크·제목이 없다는 뜻입니다. `unclosed-code-fence`는 닫히지 않은 코드 fence가 있다는 뜻입니다. 모두 작업 대상을 찾기 위한 표시입니다.",
        "- 파서는 이 저장소의 ATX 제목과 최대 3칸 들여쓴 backtick/tilde fence를 대상으로 합니다. 모든 CommonMark 문법을 지원하지는 않습니다.",
        "",
        "## 영역별 요약",
        "",
        f"전체 주제 {total['topic_count']}개 중 직접 출처가 있는 문서는 {total['with_direct_sources']}개, 재작성 메모가 있는 문서는 {total['with_rewrite_notes']}개입니다.",
        "",
        "| 영역 | 주제 수 | 출처 있음 | 출처 없음 | 구현 후보 블록 | 메모 있음 | 메모 없음 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for area, summary in inventory["areas"].items():
        lines.append(f"| {area} | {summary['topic_count']} | {summary['with_direct_sources']} | {summary['without_direct_sources']} | {summary['implementation_block_count']} | {summary['with_rewrite_notes']} | {summary['without_rewrite_notes']} |")
    lines += [
        "",
        "## 주제별 재료",
        "",
        "| 문서 | Status | 직접 출처 수 | 구현 후보 블록 | 재작성 메모 | 확인할 표시 |",
        "| --- | --- | ---: | ---: | --- | --- |",
    ]
    for topic in inventory["topics"]:
        path = topic["path"]
        link = "../" + quote(path, safe="/-._~")
        notes = "있음" if topic["has_rewrite_notes"] else "없음"
        flags = ", ".join(topic["flags"]) or "-"
        lines.append(f"| [{table_cell(path)}]({link}) | {table_cell(topic['status'])} | {topic['direct_source_count']} | {topic['implementation_block_count']} | {notes} | {flags} |")
    lines += [
        "",
        "## 다시 생성하기",
        "",
        "저장소 루트에서 실행합니다. 생성 시각을 넣지 않아 같은 입력은 같은 결과를 만듭니다.",
        "",
        "```powershell",
        "python Maintainers/Scripts/build_preparation_inventory.py --write",
        "python Maintainers/Scripts/build_preparation_inventory.py --check",
        "python Maintainers/Scripts/build_preparation_inventory.py --format json",
        "```",
        "",
        "JSON은 원문 경로·내용 해시·출처 URL과 줄 번호·코드 언어와 범위·메모 위치를 포함합니다. Markdown 보고서의 `--check`는 집계/표시가 바뀌었는지만 비교하며, 일반 본문 변경 전체를 감지하는 검사는 아닙니다.",
    ]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Update the Markdown inventory.")
    mode.add_argument("--check", action="store_true", help="Exit 1 if the Markdown inventory is missing or stale.")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    args = parser.parse_args(argv)
    if args.format == "json" and (args.write or args.check):
        parser.error("--format json is a stdout export; use it without --write or --check")
    if not args.root.is_dir():
        parser.error(f"Repository root is not a directory: {args.root}")

    inventory = build_inventory(args.root)
    if args.format == "json":
        print(json.dumps(inventory, ensure_ascii=False, indent=2))
        return 0
    rendered = render_markdown(inventory)
    output = args.root / REPORT_PATH
    if args.check:
        if not output.is_file() or output.read_text(encoding="utf-8") != rendered:
            print(f"Preparation inventory is missing or stale: {REPORT_PATH.as_posix()}. Run with --write.")
            return 1
        print(f"Preparation inventory is current: {inventory['summary']['topic_count']} topics.")
    elif args.write:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"Wrote {REPORT_PATH.as_posix()}: {inventory['summary']['topic_count']} topics.")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
