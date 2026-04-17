#!/usr/bin/env python3
"""migrate_docs.py – Convert the OPM Reference Manual from FODT to Markdown/MkDocs.

Prerequisites
-------------
* Python ≥ 3.10
* Pandoc installed and available on ``$PATH``  (https://pandoc.org/installing.html)
* No additional Python packages are required beyond the standard library.

What the script does
--------------------
1. Recursively walks ``parts/`` and converts every ``.fodt`` file to ``.md``
   using ``pandoc``.  Since ``.fodt`` (flat ODT) files are not directly
   supported by pandoc's ``odt`` reader (which expects a zipped archive),
   each file is first repackaged into a temporary ``.odt`` zip.
2. Applies post-processing to clean up the pandoc output: strips wrapper
   ``<div>`` tags, removes empty anchor spans, and normalises internal links.
3. Parses each ``.fodt`` file for ``<text:section-source … xlink:href="…"/>``
   links to other ``.fodt`` files.  After conversion the corresponding
   Markdown file gets MkDocs *snippets* inclusion directives
   (``--8<-- "path/to/file.md"``) appended so that the modular structure is
   preserved.
4. Copies the resulting ``.md`` tree into ``docs/`` mirroring the original
   directory layout, ready for ``mkdocs build``.

Usage
-----
Run from the repository root::

    python scripts/python/migrate_docs.py            # uses default paths
    python scripts/python/migrate_docs.py --parts-dir parts --docs-dir docs
"""
from __future__ import annotations

import argparse
import logging
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# 1.  FODT link extraction
# ---------------------------------------------------------------------------

# Matches   xlink:href="chapters/4.fodt"   or   xlink:href="subsections/8.3/PVTO.fodt"
# inside a <text:section-source …/> element.
_SECTION_SOURCE_RE = re.compile(
    r'<text:section-source\b[^>]*\bxlink:href="([^"]+\.fodt)"',
    re.DOTALL,
)


def extract_fodt_links(fodt_path: Path) -> list[str]:
    """Return a list of relative ``.fodt`` hrefs referenced by *fodt_path*.

    The hrefs are exactly as they appear in the XML (relative to the file that
    contains them).
    """
    try:
        text = fodt_path.read_text(encoding="utf-8")
    except Exception:
        logger.warning("Could not read %s – skipping link extraction", fodt_path)
        return []
    return _SECTION_SOURCE_RE.findall(text)


# ---------------------------------------------------------------------------
# 2.  FODT → ODT repackaging
# ---------------------------------------------------------------------------

_ODT_MIMETYPE = "application/vnd.oasis.opendocument.text"

_ODT_MANIFEST = """\
<?xml version="1.0" encoding="UTF-8"?>
<manifest:manifest xmlns:manifest=\
"urn:oasis:names:tc:opendocument:xmlns:manifest:1.0" manifest:version="1.2">
 <manifest:file-entry manifest:media-type="{mimetype}" \
manifest:version="1.2" manifest:full-path="/"/>
 <manifest:file-entry manifest:media-type="text/xml" \
manifest:full-path="content.xml"/>
 <manifest:file-entry manifest:media-type="text/xml" \
manifest:full-path="styles.xml"/>
 <manifest:file-entry manifest:media-type="text/xml" \
manifest:full-path="meta.xml"/>
</manifest:manifest>""".format(mimetype=_ODT_MIMETYPE)


def _fodt_to_odt(fodt_path: Path, odt_path: Path) -> None:
    """Repackage a flat-ODT file into a zipped ODT that Pandoc can read.

    The flat-ODT ``<office:document>`` root element is renamed to
    ``<office:document-content>`` for ``content.xml``.  Minimal
    ``styles.xml`` and ``meta.xml`` stubs are created so that Pandoc's
    ODT reader finds the files it expects.
    """
    fodt_text = fodt_path.read_text(encoding="utf-8")

    # Build content.xml by renaming the root element.
    content_xml = fodt_text.replace(
        "<office:document ", "<office:document-content ", 1
    )
    last_close = content_xml.rfind("</office:document>")
    if last_close == -1:
        raise ValueError(f"Cannot find </office:document> in {fodt_path}")
    content_xml = content_xml[:last_close] + "</office:document-content>"

    # Extract namespace declarations from the original root element so that
    # the stub files use the same prefixes.
    match = re.search(r"<office:document\s([^>]+)>", fodt_text)
    ns_attrs = match.group(1) if match else (
        'xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"'
    )

    styles_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f"<office:document-styles {ns_attrs}>\n"
        "</office:document-styles>"
    )
    meta_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f"<office:document-meta {ns_attrs}>\n"
        "<office:meta/>\n"
        "</office:document-meta>"
    )

    with zipfile.ZipFile(str(odt_path), "w", zipfile.ZIP_DEFLATED) as zf:
        # mimetype must be first and stored uncompressed per the ODF spec.
        zf.writestr("mimetype", _ODT_MIMETYPE, compress_type=zipfile.ZIP_STORED)
        zf.writestr("META-INF/manifest.xml", _ODT_MANIFEST)
        zf.writestr("content.xml", content_xml)
        zf.writestr("styles.xml", styles_xml)
        zf.writestr("meta.xml", meta_xml)


# ---------------------------------------------------------------------------
# 3.  Pandoc conversion
# ---------------------------------------------------------------------------


def _check_pandoc() -> None:
    """Abort early when Pandoc is not installed."""
    if shutil.which("pandoc") is None:
        logger.error(
            "Pandoc is not installed or not on $PATH.  "
            "Install it from https://pandoc.org/installing.html"
        )
        sys.exit(1)


def convert_fodt_to_md(fodt_path: Path, md_path: Path) -> bool:
    """Convert a single ``.fodt`` file to Markdown via Pandoc.

    The file is first repackaged into a temporary ``.odt`` zip because
    Pandoc's ODT reader does not support flat-ODT XML directly.

    Returns ``True`` on success, ``False`` otherwise.
    """
    md_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        odt_path = Path(tmp) / (fodt_path.stem + ".odt")
        try:
            _fodt_to_odt(fodt_path, odt_path)
        except Exception:
            logger.exception("Failed to repackage %s as ODT", fodt_path)
            return False

        cmd = [
            "pandoc",
            "--from=odt",
            "--to=markdown+pipe_tables-grid_tables-multiline_tables-simple_tables",
            "--wrap=none",
            str(odt_path),
            "-o",
            str(md_path),
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            logger.error("pandoc failed for %s:\n%s", fodt_path, result.stderr)
            return False

    # Post-process the generated Markdown.
    _postprocess_md(md_path)
    return True


# ---------------------------------------------------------------------------
# 4.  Grid-table → pipe-table conversion
# ---------------------------------------------------------------------------

# A grid-table separator line:  +---+---+  or  +===+===+
_GRID_SEP_RE = re.compile(r"^\+(?:[-=]+\+)+\s*$")
# A grid-table data row:  | … | … |
_GRID_DATA_RE = re.compile(r"^\|.*\|\s*$")
# Fenced code-block markers (``` or ~~~).
_FENCED_CODE_RE = re.compile(r"^(`{3,}|~{3,})")


def _find_col_positions(sep_line: str) -> list[int]:
    """Return the character positions of ``+`` in a grid-table separator."""
    return [i for i, ch in enumerate(sep_line.rstrip()) if ch == "+"]


def _merge_cell_parts(parts: list[str]) -> str:
    """Join multi-line cell content.

    Consecutive non-empty lines are joined with a space.  An empty line
    (from a blank data row) inserts a ``<br>`` to preserve paragraph breaks.
    """
    paragraphs: list[str] = []
    current: list[str] = []
    for part in parts:
        if part:
            current.append(part)
        else:
            if current:
                paragraphs.append(" ".join(current))
                current = []
    if current:
        paragraphs.append(" ".join(current))
    return "<br>".join(paragraphs) if paragraphs else ""


def _grid_table_to_pipe(table_lines: list[str]) -> str:
    """Convert a grid table (list of raw lines) to a pipe table."""
    col_pos = _find_col_positions(table_lines[0])
    if len(col_pos) < 2:
        return "\n".join(table_lines)

    num_cols = len(col_pos) - 1

    # ---- Collect row groups (data lines between separators) ---------------
    row_groups: list[list[str]] = []
    current_group: list[str] = []
    has_header_sep = False
    header_row_count = 0

    for line in table_lines:
        stripped = line.rstrip()
        if _GRID_SEP_RE.match(stripped):
            if current_group:
                row_groups.append(current_group)
                current_group = []
            # An '=' separator marks the preceding rows as the header.
            if "=" in stripped.replace("+", ""):
                has_header_sep = True
                header_row_count = len(row_groups)
        else:
            current_group.append(line)

    if current_group:
        row_groups.append(current_group)

    if not row_groups:
        return "\n".join(table_lines)

    # ---- Extract cell text for each logical row --------------------------
    def _extract_row(data_lines: list[str]) -> list[str]:
        cells: list[list[str]] = [[] for _ in range(num_cols)]
        for dl in data_lines:
            for ci in range(num_cols):
                start = col_pos[ci] + 1
                end = (
                    col_pos[ci + 1]
                    if col_pos[ci + 1] <= len(dl)
                    else len(dl)
                )
                raw = dl[start:end].strip() if start < len(dl) else ""
                # Strip block-quote artifact "> " produced by Pandoc.
                raw = re.sub(r"^>\s*", "", raw)
                cells[ci].append(raw)
        return [_merge_cell_parts(parts) for parts in cells]

    rows = [_extract_row(rg) for rg in row_groups]

    # ---- Build pipe table ------------------------------------------------
    if not has_header_sep:
        header_row_count = 1  # treat the first row as the header

    result: list[str] = []
    for idx, row in enumerate(rows):
        result.append("| " + " | ".join(row) + " |")
        if idx == header_row_count - 1:
            result.append("| " + " | ".join(["---"] * num_cols) + " |")

    return "\n".join(result)


def _convert_grid_tables(text: str) -> str:
    """Find grid tables in *text* and replace them with pipe tables."""
    lines = text.split("\n")
    output: list[str] = []
    i = 0
    in_code_fence = False

    while i < len(lines):
        # Track fenced code blocks so we never touch tables inside them.
        if _FENCED_CODE_RE.match(lines[i]):
            in_code_fence = not in_code_fence
            output.append(lines[i])
            i += 1
            continue

        if in_code_fence:
            output.append(lines[i])
            i += 1
            continue

        if _GRID_SEP_RE.match(lines[i]):
            table_lines = [lines[i]]
            i += 1
            while i < len(lines) and (
                _GRID_SEP_RE.match(lines[i]) or _GRID_DATA_RE.match(lines[i])
            ):
                table_lines.append(lines[i])
                i += 1

            # A valid grid table starts and ends with a separator (≥ 3 lines).
            if (
                len(table_lines) >= 3
                and _GRID_SEP_RE.match(table_lines[-1])
            ):
                output.append(_grid_table_to_pipe(table_lines))
            else:
                output.extend(table_lines)
        else:
            output.append(lines[i])
            i += 1

    return "\n".join(output)


# ---------------------------------------------------------------------------
# 4b. Pipe-table cell clean-up
# ---------------------------------------------------------------------------

_PIPE_ROW_RE = re.compile(r"^\|.*\|\s*$")
_PIPE_CELL_BQ_RE = re.compile(r"\| > ")


def _clean_pipe_table_blockquotes(text: str) -> str:
    r"""Strip ``> `` block-quote markers inside pipe-table cells.

    Pandoc sometimes emits ``| > content |`` for styled ODT paragraphs.
    """
    out: list[str] = []
    for line in text.split("\n"):
        if _PIPE_ROW_RE.match(line):
            line = _PIPE_CELL_BQ_RE.sub("| ", line)
        out.append(line)
    return "\n".join(out)


# ---------------------------------------------------------------------------
# 4c. Caption clean-up
# ---------------------------------------------------------------------------

_CAPTION_BLOCK_RE = re.compile(
    r"^::: caption\n(.+?)\n:::\s*$", re.MULTILINE
)
# Empty caption blocks left over after a caption has already been converted.
_EMPTY_CAPTION_RE = re.compile(r"^::: caption\n:::\s*$", re.MULTILINE)


def _clean_captions(text: str) -> str:
    r"""Convert Pandoc ``:::caption … :::`` fenced divs to italic text."""
    text = _CAPTION_BLOCK_RE.sub(r"*\1*", text)
    text = _EMPTY_CAPTION_RE.sub("", text)
    return text


# ---------------------------------------------------------------------------
# 4d. Broken cross-reference link clean-up
# ---------------------------------------------------------------------------
#
# The original FODT was a monolithic document.  When it was split into
# per-keyword pages the internal cross-reference anchors (e.g.
# ``#__RefHeading___Toc…``) no longer resolve because the target heading
# lives on a *different* page.  MkDocs ``--strict`` mode treats these as
# errors, so we strip them and keep only the display text.

# Markdown: [text](#__RefHeading___...) → text
_REFHEADING_LINK_RE = re.compile(
    r"\[([^\[\]]+)\]\(#__RefHeading___[^)]+\)"
)

# HTML: <a href="#__RefHeading___...">text</a> → text
_REFHEADING_HTML_LINK_RE = re.compile(
    r'<a href="#__RefHeading___[^"]*">([^<]*)</a>'
)

# Markdown: [text](#REF_HEADING_KEYWORD_...) → text
_REFHEADING_KW_LINK_RE = re.compile(
    r"\[([^\[\]]*)\]\(#REF_HEADING_KEYWORD_[^)]+\)"
)

# Standalone empty-text anchors pointing nowhere: [](#anchor-N)
_EMPTY_ANCHOR_LINK_RE = re.compile(r"\[]\(#anchor(?:-\d+)?\)")

# Empty HTML anchor tags from FODT cross-references: <a id="__RefHeading___..."></a>
_EMPTY_HTML_ANCHOR_RE = re.compile(r'<a id="__RefHeading___[^"]*"></a>\s*')

# Consecutive underscores (2+) in HTML anchor IDs trigger Jinja2 "Missing end
# of comment tag" errors in the MkDocs macros plugin.  Replace them with a
# single underscore so the anchor still works but doesn't confuse Jinja.
_DOUBLE_UNDERSCORE_ANCHOR_RE = re.compile(r'(<a id="[^"]*?)__+([^"]*")', re.DOTALL)


def _strip_outline_links(text: str) -> str:
    r"""Remove ``[text](#…|outline)`` links, keeping only the display text.

    Because the display text can contain nested Markdown links
    (e.g. ``[[inner](#anchor)](#…|outline)``) and the URL can contain
    literal parentheses, a pure regex approach risks catastrophic
    backtracking on large files with many ``[`` characters.  Instead we
    scan for the distinctive ``|outline)`` marker and work backwards to
    locate the matching ``](#`` and opening ``[``.
    """
    MARKER = "|outline)"
    result: list[str] = []
    search_start = 0

    while True:
        marker_pos = text.find(MARKER, search_start)
        if marker_pos == -1:
            result.append(text[search_start:])
            break

        # Find the start of the URL: "](#" before "|outline)".
        # The URL is between ](#...|outline), walk backwards past balanced
        # parentheses to find the "](#" that opens this link's URL.
        url_start = text.rfind("](#", search_start, marker_pos)
        if url_start == -1:
            # No link syntax found — keep text as-is up through marker.
            result.append(text[search_start : marker_pos + len(MARKER)])
            search_start = marker_pos + len(MARKER)
            continue

        # ``url_start`` points to the ``]`` of ``](#…|outline)``.
        # The display text is between a matching ``[`` and this ``]``.
        # Walk backwards, counting brackets to handle one level of nesting.
        bracket_pos = url_start - 1
        depth = 1
        while bracket_pos >= search_start and depth > 0:
            ch = text[bracket_pos]
            if ch == "]":
                depth += 1
            elif ch == "[":
                depth -= 1
            bracket_pos -= 1

        if depth != 0:
            # Unbalanced — keep as-is.
            result.append(text[search_start : marker_pos + len(MARKER)])
            search_start = marker_pos + len(MARKER)
            continue

        open_bracket = bracket_pos + 1  # position of the ``[``
        display_text = text[open_bracket + 1 : url_start]

        result.append(text[search_start:open_bracket])
        result.append(display_text)
        search_start = marker_pos + len(MARKER)

    return "".join(result)


def _clean_broken_links(text: str) -> str:
    """Strip broken cross-reference links, keeping only their display text."""
    text = _REFHEADING_LINK_RE.sub(r"\1", text)
    text = _REFHEADING_HTML_LINK_RE.sub(r"\1", text)
    text = _REFHEADING_KW_LINK_RE.sub(r"\1", text)
    text = _strip_outline_links(text)
    text = _EMPTY_ANCHOR_LINK_RE.sub("", text)
    # Remove empty HTML anchor tags from FODT cross-references.
    text = _EMPTY_HTML_ANCHOR_RE.sub("", text)
    # Collapse double/triple underscores in remaining HTML anchor IDs so the
    # MkDocs macros plugin (Jinja2) does not interpret them as comment markers.
    prev = text
    while True:
        text = _DOUBLE_UNDERSCORE_ANCHOR_RE.sub(r"\1_\2", text)
        if text == prev:
            break
        prev = text
    return text


# ---------------------------------------------------------------------------
# 5.  General post-processing
# ---------------------------------------------------------------------------

# Pandoc wraps ODT output in <div>…</div> — strip those.
_LEADING_DIV_RE = re.compile(r"^<div>\s*\n?", re.MULTILINE)
_TRAILING_DIV_RE = re.compile(r"\n?</div>\s*$", re.MULTILINE)

# Convert Pandoc markdown-style anchors ``[]{#id}`` to HTML ``<a id="id"></a>``.
# The ``{#`` sequence triggers Jinja2 comment parsing in the MkDocs macros
# plugin, causing "Missing end of comment tag" errors.
_MD_ANCHOR_TO_HTML_RE = re.compile(r"\[]\{#([^}]+)\}")

# Empty anchor spans: <a id="anchor"></a> or <a id="anchor-1"></a> etc.
# (These were ``[]{#anchor-N}`` before the markdown→HTML anchor conversion.)
_EMPTY_ANCHOR_RE = re.compile(r'<a id="anchor(?:-\d+)?"></a>\s*')

# Block-quote markers on lines that are really normal paragraphs.
_BLOCK_QUOTE_RE = re.compile(r"^> ", re.MULTILINE)


def _postprocess_md(md_path: Path) -> None:
    """Clean up common artefacts in the Pandoc-generated Markdown."""
    try:
        text = md_path.read_text(encoding="utf-8")
    except OSError:
        return

    # Convert grid tables to pipe tables (must run before block-quote strip).
    text = _convert_grid_tables(text)
    # Strip "> " inside pipe-table cells (artifact from ODT paragraph styles).
    text = _clean_pipe_table_blockquotes(text)
    # Convert ::: caption ... ::: blocks to italic captions.
    text = _clean_captions(text)
    # Convert []{#id} anchors to <a id="id"></a> so the {# sequence does not
    # trigger Jinja2 comment parsing in the MkDocs macros plugin.
    text = _MD_ANCHOR_TO_HTML_RE.sub(r'<a id="\1"></a>', text)
    # Strip broken FODT cross-reference links (must run before anchor strip).
    text = _clean_broken_links(text)

    text = _LEADING_DIV_RE.sub("", text)
    text = _TRAILING_DIV_RE.sub("", text)
    text = _EMPTY_ANCHOR_RE.sub("", text)
    text = _BLOCK_QUOTE_RE.sub("", text)

    # Collapse runs of blank lines to at most two.
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    # Strip trailing whitespace on each line.
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)

    md_path.write_text(text, encoding="utf-8")


# ---------------------------------------------------------------------------
# 6.  Snippet injection
# ---------------------------------------------------------------------------

def _fodt_href_to_md_path(href: str) -> str:
    """Convert a relative ``.fodt`` href to its ``.md`` counterpart."""
    return re.sub(r"\.fodt$", ".md", href)


def inject_snippets(
    md_path: Path, links: list[str], source_dir: Path, docs_dir: Path
) -> None:
    """Append MkDocs snippet inclusion tags to *md_path*.

    Each linked ``.fodt`` is translated to its ``.md`` sibling path and
    written as ``--8<-- "relative/path.md"`` where the path is relative to
    *docs_dir* (matching the ``base_path`` in ``pymdownx.snippets``).

    *source_dir* is the directory of the output ``.md`` file so that
    relative hrefs can be resolved.
    """
    if not links:
        return

    docs_abs = docs_dir.resolve()
    snippet_lines: list[str] = ["\n"]
    for href in links:
        md_href = _fodt_href_to_md_path(href)
        # Resolve to an absolute path, then make it relative to docs root.
        resolved = (source_dir / md_href).resolve()
        try:
            rel = resolved.relative_to(docs_abs)
        except ValueError:
            # Fall back to preserving the relative path unchanged.
            rel = Path(md_href)
        snippet_lines.append(f'--8<-- "{rel}"\n')

    try:
        with open(md_path, "a", encoding="utf-8") as fh:
            fh.writelines(snippet_lines)
        logger.info(
            "  ↳ injected %d snippet include(s) into %s", len(links), md_path
        )
    except OSError as exc:
        logger.error("Could not write snippets to %s: %s", md_path, exc)


# ---------------------------------------------------------------------------
# 7.  Orchestration
# ---------------------------------------------------------------------------


def postprocess_existing(docs_dir: Path) -> None:
    """Re-run post-processing on all existing ``.md`` files in *docs_dir*.

    This is useful for fixing tables and other artefacts in previously
    converted files without repeating the full FODT → Markdown conversion.
    """
    md_files = sorted(docs_dir.rglob("*.md"))
    if not md_files:
        logger.warning("No .md files found under %s", docs_dir)
        return

    logger.info("Post-processing %d .md file(s) under %s", len(md_files), docs_dir)
    for md_path in md_files:
        _postprocess_md(md_path)
    logger.info("Post-processing complete.")


def migrate(parts_dir: Path, docs_dir: Path) -> None:
    """Walk *parts_dir*, convert every ``.fodt`` → ``.md``, inject snippets,
    and mirror the result under *docs_dir*.
    """
    _check_pandoc()

    fodt_files = sorted(parts_dir.rglob("*.fodt"))
    if not fodt_files:
        logger.warning("No .fodt files found under %s", parts_dir)
        return

    logger.info("Found %d .fodt file(s) under %s", len(fodt_files), parts_dir)

    errors: list[str] = []
    converted = 0
    for fodt_path in fodt_files:
        rel = fodt_path.relative_to(parts_dir)
        md_rel = rel.with_suffix(".md")
        md_dest = docs_dir / md_rel

        logger.info("Converting %s → %s", rel, md_dest)

        # --- Convert ---
        if not convert_fodt_to_md(fodt_path, md_dest):
            errors.append(str(rel))
            continue
        converted += 1

        # --- Extract links & inject snippets ---
        links = extract_fodt_links(fodt_path)
        if links:
            inject_snippets(
                md_dest, links, source_dir=md_dest.parent, docs_dir=docs_dir
            )

    logger.info(
        "Migration complete: %d / %d file(s) converted.", converted, len(fodt_files)
    )
    if errors:
        logger.warning("Failed files (%d): %s", len(errors), ", ".join(errors))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Migrate OPM Reference Manual from FODT to Markdown / MkDocs."
    )
    parser.add_argument(
        "--parts-dir",
        type=Path,
        default=Path("parts"),
        help="Root directory containing .fodt files (default: parts)",
    )
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=Path("docs"),
        help="Output directory for Markdown files (default: docs)",
    )
    parser.add_argument(
        "--postprocess-only",
        action="store_true",
        help="Only re-run post-processing on existing .md files in docs-dir "
        "(skip FODT-to-Markdown conversion).",
    )
    args = parser.parse_args()
    if args.postprocess_only:
        postprocess_existing(args.docs_dir)
    else:
        migrate(args.parts_dir, args.docs_dir)


if __name__ == "__main__":
    main()
