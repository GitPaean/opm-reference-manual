# Markdown migration guide

This document describes the new Markdown publishing pipeline for the OPM
Flow Reference Manual. It is the developer reference for the
[`fodt2md`](../src/fodt/fodt2md/) package and the surrounding MkDocs / Pandoc
configuration.

The original `parts/**/*.fodt` (LibreOffice flat XML) files remain the
**canonical source** of the manual. The Markdown tree under `docs/` is
generated from them and is intended to be rebuilt — and reviewed in a PR —
whenever an FODT file is changed. Once the migration is complete the team
can choose to flip the canonical source to Markdown and decommission the
FODT files; until then both can coexist.

## What gets generated

| Source                                | Generated artefact                |
| ------------------------------------- | --------------------------------- |
| `parts/main.fodt`                     | `docs/index.md` (handwritten cover, generator skips overwrite) |
| `parts/chapters/<n>.fodt`             | `docs/chapters/<n>.md`            |
| `parts/chapters/sections/<n>/<m>.fodt`| `docs/chapters/sections/<n>/<m>.md` |
| `parts/chapters/subsections/<n>.<m>/<KW>.fodt` | `docs/chapters/subsections/<n>.<m>/<KW>.md` |
| `parts/appendices/<X>.fodt`           | `docs/appendices/<X>.md`          |
| any embedded image                    | `docs/_images/<slug>-<sha1>.<ext>` |
| build report                          | `docs/links_report.json`          |

The output layout is a 1:1 mirror of the source so PR reviewers can easily
diff the generated Markdown against the FODT change that produced it.

## Quick start

```bash
# one-time install (replace with poetry install if you prefer Poetry)
pip install -e ./scripts/python
pip install mkdocs mkdocs-material 'pymdown-extensions>=10.0'

# convert every FODT file to Markdown (uses all CPU cores)
fodt2md convert-all

# preview the manual locally at http://127.0.0.1:8000
mkdocs serve

# render the static HTML site into ./site
fodt2md build-html

# render the manual as a single PDF (requires pandoc + a TeX engine)
sudo apt-get install pandoc texlive-xetex
fodt2md build-pdf -o dist/opm-flow-reference-manual.pdf
```

`make convert-all`, `make build-html` and `make build-pdf` are convenience
wrappers around the same commands.

## CLI reference

```text
fodt2md convert <file.fodt> [-o file.md]   # convert one file
fodt2md convert-all [--workers N] [--check] [--only file]…
fodt2md make-nav [-o nav.yml]              # print the auto-generated nav
fodt2md build-html [--strict]
fodt2md build-pdf [--engine pandoc|mkdocs] [--output PATH]
```

`--check` re-runs the converter and exits non-zero if any committed
Markdown file would change. Use it in CI to catch FODT edits whose
regenerated Markdown was forgotten.

## What the converter handles

The converter is style-driven and walks the ODF tree with `lxml`. It
produces:

* **Headings** from `text:h` (`text:outline-level` → `#` … `######`).
  The first heading text becomes the page's YAML `title`.
* **Inline emphasis** (`**bold**`, `*italic*`, `` `monospace` ``) based on
  the resolved style chain — not just the leaf style — so child styles
  inheriting from `Text body` automatically pick up the parent's bold/
  italic/monospace properties.
* **Eclipse DATA blocks**: consecutive paragraphs whose paragraph style
  inherits from `@Example` (`_40_Example`) or whose font is `style:font-
  family-generic="modern"` are grouped into a single `` ```eclipse `` fenced
  block. Whitespace is preserved verbatim, including `<text:s text:c="N"/>`
  expansions and tabs.
* **Tables** as Markdown pipe tables, including `table:number-columns-
  repeated` and `table:number-columns-spanned`. Tables with multi-paragraph
  or list-bearing cells fall back to raw HTML so nothing is lost.
* **Cross-document links**: `xlink:href` values pointing at sibling FODT
  files are emitted as opaque `fodt2md:<base64>` placeholders, then rewritten
  in the post-processing step to `./<relative>/<file>.md#<anchor>` once the
  full path map and bookmark tables for the build are known.
* **Internal anchors**: `text:bookmark-start` becomes
  `<a id="…"></a>` (HTML) so the Pandoc `[]{#…}` syntax doesn't collide with
  the Jinja `{#` comment marker in the MkDocs Macros plugin.
* **Images** (binary base64 in `office:binary-data` or `xlink:href`) are
  written under `docs/_images/` with content-addressed file names and
  referenced via `<img>` tags.
* **Formulas** (`math:math` MathML) are converted to LaTeX with a small
  Presentation MathML walker (fractions, sub/superscripts, roots, fences,
  matrices, common operators). Display math (`display="block"`) renders as
  `$$ … $$`; inline as `$ … $`. The HTML site renders them with MathJax v3
  (`docs/assets/js/mathjax.js`) and the PDF renders them with the LaTeX
  amsmath/amssymb packages bundled in `pandoc/opm.tex`.

## HTML site (MkDocs Material)

The HTML configuration lives in `mkdocs.yml`. The navigation tree is
generated from `docs/` by the hook in
`scripts/python/src/fodt/fodt2md/nav.py` so we don't have to maintain a
1500-entry `nav:` block. Theme tweaks live in `docs/assets/css/opm.css`
(typography, table zebra striping, Eclipse DATA block accent colour,
formula sizing) and `overrides/main.html` (a "Keyword" badge on subsection
pages).

## PDF book (Pandoc + xelatex)

`fodt2md build-pdf` (default `--engine=pandoc`) concatenates every
Markdown file in nav order and shells out to:

```
pandoc --from=markdown+pipe_tables+yaml_metadata_block+raw_html+tex_math_dollars \
       --to=pdf --pdf-engine=xelatex \
       --template=pandoc/opm.tex \
       --syntax-definition=pandoc/eclipse.xml \
       --toc --toc-depth=3 --number-sections --top-level-division=chapter
```

* `pandoc/opm.tex` is a custom LaTeX book template with a title page,
  hyperref links, fancy headers, and proper monospace/serif fonts.
* `pandoc/eclipse.xml` is a Kate-syntax definition that highlights the
  `RUNSPEC`/`GRID`/… section keywords, line comments (`--`), single-quoted
  filenames and the trailing `/` record terminator in Eclipse DATA listings.

The alternative `--engine=mkdocs` path uses the
[`mkdocs-with-pdf`](https://github.com/orzih/mkdocs-with-pdf) plugin so the
HTML and PDF stay 1:1 identical (install separately).

## Editing the Markdown directly

Once the team flips the canonical source to Markdown:

* Use the template in `docs/_templates/keyword.md` for new keyword pages.
* Eclipse DATA examples should always go inside ` ```eclipse ` fenced blocks.
* Math should use `$ … $` (inline) or `$$ … $$` (display), not raw `\(`/`\)`.
* Cross-page links should be relative `.md` paths plus a slug anchor, e.g.
  `[INCLUDE](INCLUDE.md)` or `[Section 4.3](../sections/4/3.md#some-anchor)`.

## Tests

```bash
pip install pytest lxml pyyaml click
pytest scripts/python/tests/test_fodt2md/ --noconftest -q
```

The tests cover heading levels, list nesting, pipe tables, code-block
grouping, MathML → LaTeX, internal/external link rewriting and image
extraction. The `--noconftest` flag is required because the parent
`conftest.py` imports `gitpython`, which the converter does not depend on.
