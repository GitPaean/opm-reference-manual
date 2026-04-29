"""Pandoc + LaTeX backend for rendering the manual as a single PDF.

The function concatenates every Markdown file in MkDocs nav order
(``index.md`` first, then chapters / sections / subsections / appendices
in natural numeric order) and shells out to ``pandoc`` with a custom
LaTeX template tuned for the OPM Flow Reference Manual.

This is the "fallback" PDF path described in the plan; the alternative is
the ``mkdocs-with-pdf`` plugin which renders directly from the built HTML.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import List

from .nav import _natural_key  # noqa: F401  (re-used for ordering)


def collect_md_files(docs_root: Path) -> List[Path]:
    """Return the Markdown files in nav order for PDF concatenation."""
    docs_root = docs_root.resolve()
    files: List[Path] = []
    index = docs_root / "index.md"
    if index.exists():
        files.append(index)
    for sub in sorted(docs_root.iterdir(), key=lambda p: p.name):
        if sub.is_dir() and not sub.name.startswith(("_", ".")):
            files.extend(
                sorted(
                    (p for p in sub.rglob("*.md")),
                    key=lambda p: [_natural_key(s) for s in p.relative_to(docs_root).parts],
                )
            )
    return files


def build_pdf_with_pandoc(docs_root: Path, output: Path, pandoc_root: Path) -> None:
    """Render the manual as a single PDF using pandoc + xelatex."""
    if shutil.which("pandoc") is None:
        raise RuntimeError(
            "pandoc is not installed; install pandoc and a TeX distribution "
            "(e.g. texlive-xetex) and try again."
        )
    files = collect_md_files(docs_root)
    if not files:
        raise RuntimeError(f"No Markdown files found under {docs_root}")
    template = pandoc_root / "opm.tex"
    syntax = pandoc_root / "eclipse.xml"
    cmd = [
        "pandoc",
        "--from=markdown+pipe_tables+yaml_metadata_block+raw_html+tex_math_dollars",
        "--to=pdf",
        "--pdf-engine=xelatex",
        f"--resource-path={docs_root}:{docs_root / '_images'}",
        "--toc",
        "--toc-depth=3",
        "--number-sections",
        "--top-level-division=chapter",
        f"--output={output}",
    ]
    if template.exists():
        cmd.append(f"--template={template}")
    if syntax.exists():
        cmd.append(f"--syntax-definition={syntax}")
    cmd.extend(str(f) for f in files)
    subprocess.check_call(cmd)
