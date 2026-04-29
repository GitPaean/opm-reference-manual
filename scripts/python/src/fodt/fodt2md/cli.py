"""Click CLI for the FODT → Markdown pipeline.

Subcommands:

* ``fodt2md convert <FILE>`` — convert a single FODT to Markdown.
* ``fodt2md convert-all`` — convert every ``.fodt`` under ``parts/``.
* ``fodt2md build-html`` — run ``mkdocs build``.
* ``fodt2md build-pdf`` — render the manual as a single PDF (Pandoc).
* ``fodt2md make-nav`` — write the auto-generated MkDocs nav YAML.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

import click

from .build import convert_tree, find_fodt_files
from .converter import FodtConverter
from .nav import build_nav, write_mkdocs_nav_yaml
from .paths import build_path_map
from .postprocess import postprocess


def _default_repo_root() -> Path:
    """Locate the repo root by walking up looking for ``parts/main.fodt``."""
    here = Path(__file__).resolve()
    for parent in [here, *here.parents]:
        if (parent / "parts" / "main.fodt").exists():
            return parent
    return Path.cwd()


@click.group(
    help="Convert OPM Flow Reference Manual FODT files to Markdown and "
    "build the HTML / PDF manual."
)
def cli() -> None:
    pass


@cli.command("convert")
@click.argument("source", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option(
    "-o",
    "--output",
    type=click.Path(dir_okay=False, path_type=Path),
    default=None,
    help="Output Markdown file. Defaults to stdout.",
)
@click.option(
    "--parts-root",
    type=click.Path(file_okay=False, path_type=Path),
    default=None,
    help="Path to the manual's parts/ directory. Auto-detected by default.",
)
def convert_cmd(source: Path, output: Optional[Path], parts_root: Optional[Path]) -> None:
    """Convert a single FODT file to Markdown."""
    parts_root = (parts_root or (_default_repo_root() / "parts")).resolve()
    converter = FodtConverter(source.resolve(), parts_root)
    result = converter.convert()
    # Single-file mode: we still run the post-processor so blank lines and
    # code fences are normalised. Cross-document links stay as placeholders.
    docs_root = (output.parent if output else _default_repo_root() / "docs").resolve()
    target = output.resolve() if output else (docs_root / source.with_suffix(".md").name)
    path_map = build_path_map([source.resolve()], parts_root, docs_root)
    final = postprocess(result, target, path_map, {source.resolve(): result.bookmarks})
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(final.markdown, encoding="utf-8")
        click.echo(f"Wrote {output}")
    else:
        click.echo(final.markdown)


@cli.command("convert-all")
@click.option(
    "--parts-root",
    type=click.Path(file_okay=False, path_type=Path),
    default=None,
    help="Path to the manual's parts/ directory. Auto-detected by default.",
)
@click.option(
    "--docs-root",
    type=click.Path(file_okay=False, path_type=Path),
    default=None,
    help="Path to the output docs/ directory. Auto-detected by default.",
)
@click.option(
    "--workers",
    type=int,
    default=None,
    help="Number of worker processes. Defaults to all available CPUs.",
)
@click.option(
    "--check",
    is_flag=True,
    help="Verify generated Markdown matches committed files; exit non-zero on diff.",
)
@click.option(
    "--only",
    type=click.Path(exists=True, path_type=Path),
    multiple=True,
    help="Restrict conversion to the given FODT file(s) (repeatable).",
)
def convert_all_cmd(
    parts_root: Optional[Path],
    docs_root: Optional[Path],
    workers: Optional[int],
    check: bool,
    only: tuple[Path, ...],
) -> None:
    """Convert every FODT file in the manual to Markdown."""
    repo = _default_repo_root()
    parts_root = (parts_root or (repo / "parts")).resolve()
    docs_root = (docs_root or (repo / "docs")).resolve()
    sources = [p.resolve() for p in only] if only else find_fodt_files(parts_root)
    summary = convert_tree(
        parts_root,
        docs_root,
        sources=sources,
        workers=workers,
        write=not check,
        check=check,
    )
    click.echo(
        f"Converted {summary.converted}, unchanged {summary.unchanged}, "
        f"failed {summary.failed}, unresolved links {summary.unresolved_links}"
    )
    for failure in summary.failures[:20]:
        click.echo(f"  ! {failure}", err=True)
    if summary.failed:
        sys.exit(1)


@cli.command("make-nav")
@click.option(
    "--docs-root",
    type=click.Path(file_okay=False, path_type=Path),
    default=None,
    help="Path to the docs/ directory. Auto-detected by default.",
)
@click.option(
    "-o",
    "--output",
    type=click.Path(dir_okay=False, path_type=Path),
    default=None,
    help="Where to write the generated nav YAML (defaults to stdout).",
)
def make_nav_cmd(docs_root: Optional[Path], output: Optional[Path]) -> None:
    """Print or write the auto-generated MkDocs navigation tree."""
    docs_root = (docs_root or (_default_repo_root() / "docs")).resolve()
    if output:
        write_mkdocs_nav_yaml(docs_root, output)
        click.echo(f"Wrote {output}")
    else:
        import yaml

        click.echo(yaml.safe_dump({"nav": build_nav(docs_root)}, sort_keys=False))


@cli.command("build-html")
@click.option("--strict/--no-strict", default=False)
def build_html_cmd(strict: bool) -> None:
    """Run ``mkdocs build`` (must be installed)."""
    if shutil.which("mkdocs") is None:
        raise click.ClickException(
            "mkdocs is not installed. Run: pip install mkdocs mkdocs-material"
        )
    cmd = ["mkdocs", "build"]
    if strict:
        cmd.append("--strict")
    subprocess.check_call(cmd, cwd=_default_repo_root())


@cli.command("build-pdf")
@click.option(
    "--output",
    type=click.Path(dir_okay=False, path_type=Path),
    default=None,
    help="Output PDF file. Defaults to dist/opm-flow-reference-manual.pdf.",
)
@click.option(
    "--engine",
    type=click.Choice(["pandoc", "mkdocs"]),
    default="pandoc",
    help="PDF backend to use. ``pandoc`` requires pandoc + a TeX engine; "
    "``mkdocs`` requires the mkdocs-with-pdf plugin.",
)
def build_pdf_cmd(output: Optional[Path], engine: str) -> None:
    """Render the whole manual as a single PDF."""
    repo = _default_repo_root()
    output = (output or (repo / "dist" / "opm-flow-reference-manual.pdf")).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    if engine == "pandoc":
        from .pdf import build_pdf_with_pandoc

        build_pdf_with_pandoc(repo / "docs", output, repo / "pandoc")
    else:
        if shutil.which("mkdocs") is None:
            raise click.ClickException("mkdocs is not installed.")
        env = {"ENABLE_PDF_EXPORT": "1"}
        subprocess.check_call(
            ["mkdocs", "build"], cwd=repo, env={**__import__("os").environ, **env}
        )
    click.echo(f"PDF written to {output}")


if __name__ == "__main__":
    cli()
