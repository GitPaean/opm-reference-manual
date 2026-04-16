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
   using ``pandoc``.
2. Parses each ``.fodt`` file for ``<text:section-source … xlink:href="…"/>``
   links to other ``.fodt`` files.  After conversion the corresponding
   Markdown file gets MkDocs *snippets* inclusion directives
   (``--8<-- "path/to/file.md"``) appended so that the modular structure is
   preserved.
3. Copies the resulting ``.md`` tree into ``docs/`` mirroring the original
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
import os
import re
import shutil
import subprocess
import sys
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
# 2.  Pandoc conversion
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

    Returns ``True`` on success, ``False`` otherwise.
    """
    md_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "pandoc",
        "--from=opendocument",
        "--to=markdown",
        "--wrap=none",
        str(fodt_path),
        "-o",
        str(md_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        logger.error("pandoc failed for %s:\n%s", fodt_path, result.stderr)
        return False
    return True


# ---------------------------------------------------------------------------
# 3.  Snippet injection
# ---------------------------------------------------------------------------

def _fodt_href_to_md_path(href: str) -> str:
    """Convert a relative ``.fodt`` href to its ``.md`` counterpart."""
    return re.sub(r"\.fodt$", ".md", href)


def inject_snippets(md_path: Path, links: list[str], source_dir: Path) -> None:
    """Append MkDocs snippet inclusion tags to *md_path*.

    Each linked ``.fodt`` is translated to its ``.md`` sibling path and
    written as ``--8<-- "docs/relative/path.md"``.

    *source_dir* is the directory that contained the original ``.fodt`` file
    so that relative hrefs can be resolved to their location under ``docs/``.
    """
    if not links:
        return

    snippet_lines: list[str] = ["\n"]
    for href in links:
        md_href = _fodt_href_to_md_path(href)
        # Resolve to a docs-root-relative path.
        resolved = (source_dir / md_href).resolve()
        try:
            rel = resolved.relative_to(Path.cwd() / "docs")
        except ValueError:
            # Fall back to preserving the relative path unchanged.
            rel = md_href
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
# 4.  Orchestration
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

    converted = 0
    for fodt_path in fodt_files:
        rel = fodt_path.relative_to(parts_dir)
        md_rel = rel.with_suffix(".md")
        md_dest = docs_dir / md_rel

        logger.info("Converting %s → %s", rel, md_dest)

        # --- Convert ---
        if not convert_fodt_to_md(fodt_path, md_dest):
            continue
        converted += 1

        # --- Extract links & inject snippets ---
        links = extract_fodt_links(fodt_path)
        if links:
            inject_snippets(md_dest, links, source_dir=md_dest.parent)

    logger.info(
        "Migration complete: %d / %d file(s) converted.", converted, len(fodt_files)
    )


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
