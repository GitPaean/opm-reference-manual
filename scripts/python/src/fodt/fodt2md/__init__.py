"""FODT → Markdown conversion package.

This package provides a style-driven converter that walks the OpenDocument
Flat XML (FODT) tree and emits Markdown suitable for MkDocs / Pandoc. It also
exposes a :mod:`click` CLI used to convert single files or the whole
``parts/`` tree, build the static HTML site (MkDocs) and render the manual as
a single PDF.

The public entry point is :func:`fodt.fodt2md.cli.cli`.
"""

from .converter import FodtConverter, ConversionResult  # noqa: F401
