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
            "--to=markdown",
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
# 4.  Post-processing
# ---------------------------------------------------------------------------

# Pandoc wraps ODT output in <div>…</div> — strip those.
_LEADING_DIV_RE = re.compile(r"^<div>\s*\n?", re.MULTILINE)
_TRAILING_DIV_RE = re.compile(r"\n?</div>\s*$", re.MULTILINE)

# Empty anchor spans: []{#anchor} or []{#anchor-1} etc.
_EMPTY_ANCHOR_RE = re.compile(r"\[]\{#anchor(?:-\d+)?}\s*")

# Block-quote markers on lines that are really normal paragraphs.
_BLOCK_QUOTE_RE = re.compile(r"^> ", re.MULTILINE)


def _postprocess_md(md_path: Path) -> None:
    """Clean up common artefacts in the Pandoc-generated Markdown."""
    try:
        text = md_path.read_text(encoding="utf-8")
    except OSError:
        return

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
# 5.  Snippet injection
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
# 6.  Orchestration
# ---------------------------------------------------------------------------


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
    args = parser.parse_args()
    migrate(args.parts_dir, args.docs_dir)


if __name__ == "__main__":
    main()
