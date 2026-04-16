# OPM Flow Reference Manual

Welcome to the **OPM Flow Reference Manual** — the comprehensive reference for
the [OPM Flow](https://opm-project.org/) reservoir simulator.

---

## About this Manual

This manual was originally maintained as a single LibreOffice Flat-ODT
(``.fodt``) master document with externally linked chapter, section, and keyword
sub-documents.  It has been migrated to a **Docs-as-Code** architecture using
[MkDocs](https://www.mkdocs.org/) and the
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme,
enabling collaborative editing in Markdown and automated PDF generation via CI.

---

## Chapters

| # | Chapter | Description |
|---|---------|-------------|
| 1 | [Introduction](chapters/1.md) | Overview of OPM Flow and this manual |
| 2 | [Tutorial](chapters/2.md) | Getting started with a simple simulation |
| 3 | [File Formats](chapters/3.md) | Input / output file format reference |
| 4 | [Run-Time Options](chapters/4.md) | Command-line and run-time keywords |
| 5 | [RUNSPEC Section](chapters/5.md) | RUNSPEC input-deck section keywords |
| 6 | [GRID Section](chapters/6.md) | GRID input-deck section keywords |
| 7 | [EDIT Section](chapters/7.md) | EDIT input-deck section keywords |
| 8 | [PROPS Section](chapters/8.md) | PROPS input-deck section keywords |
| 9 | [REGIONS Section](chapters/9.md) | REGIONS input-deck section keywords |
| 10 | [SOLUTION Section](chapters/10.md) | SOLUTION input-deck section keywords |
| 11 | [SUMMARY Section](chapters/11.md) | SUMMARY input-deck section keywords |
| 12 | [SCHEDULE Section](chapters/12.md) | SCHEDULE input-deck section keywords |

## Appendices

| Appendix | Link |
|----------|------|
| A | [Appendix A](appendices/A.md) |
| B | [Appendix B](appendices/B.md) |
| C | [Appendix C](appendices/C.md) |
| D | [Appendix D](appendices/D.md) |
| E | [Appendix E](appendices/E.md) |
| F | [Appendix F](appendices/F.md) |

---

## Building Locally

```bash
# Install prerequisites (one-time)
pip install mkdocs mkdocs-material mkdocs-macros-plugin mkdocs-with-pdf

# Live preview
mkdocs serve

# Build static site
mkdocs build

# Build with PDF export
ENABLE_PDF_EXPORT=1 mkdocs build
```

## Running the Migration Script

If you need to re-generate the Markdown files from the source ``.fodt`` files:

```bash
# Requires Pandoc: https://pandoc.org/installing.html
python scripts/python/migrate_docs.py --parts-dir parts --docs-dir docs
```

---

*This site is generated automatically from the OPM Reference Manual sources.*
