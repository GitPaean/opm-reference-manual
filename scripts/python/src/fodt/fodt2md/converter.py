"""Visitor that converts a parsed FODT tree to Markdown.

The converter is style-driven: it inspects the resolved style of each
``text:p`` / ``text:span`` to decide whether to wrap the content as a code
fence, bold/italic span, etc. It groups consecutive code paragraphs into a
single fenced ``eclipse`` block (so multi-line Eclipse DATA examples render
verbatim) and rewrites cross-document ``xlink:href`` values to point at the
generated Markdown files.

The output is then handed to :mod:`fodt.fodt2md.postprocess` which collapses
blank lines, normalises code fences and rewrites unresolved links.
"""

from __future__ import annotations

import base64
import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from lxml import etree

from .constants import ECLIPSE_FENCE_LANG, NS, q
from .mathml import latex_for_math
from .paths import relative_md_link, resolve_fodt_href
from .styles import StyleMap

# Markdown special characters that need escaping when emitting ordinary text.
_MD_ESCAPE_RE = re.compile(r"([\\`*_{}\[\]()#+\-!>|])")


def _md_escape(text: str) -> str:
    return _MD_ESCAPE_RE.sub(r"\\\1", text)


@dataclass
class ConversionResult:
    """Result of converting a single FODT file."""

    markdown: str
    title: str
    bookmarks: Dict[str, str]  # bookmark name -> heading anchor
    images: Dict[str, bytes]  # output filename -> raw bytes
    unresolved_links: List[str] = field(default_factory=list)
    fodt_links: List[Tuple[str, Optional[Path], str]] = field(default_factory=list)
    """``(raw_href, resolved_fodt_path_or_None, anchor)`` triples.

    Used by the post-processor to rewrite cross-document references once the
    full path map for the build is known.
    """


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text or "").strip().lower()
    return re.sub(r"[\s_]+", "-", text) or "section"


def _local_name(el: etree._Element) -> str:
    tag = el.tag
    if isinstance(tag, str) and tag.startswith("{"):
        return tag.split("}", 1)[1]
    return str(tag)


def _ns(tag: str) -> str:
    if tag.startswith("{"):
        return tag.split("}", 1)[0][1:]
    return ""


# ---------------------------------------------------------------------------
# Converter
# ---------------------------------------------------------------------------


class FodtConverter:
    """Convert a single FODT file (or string) to Markdown.

    Parameters
    ----------
    source:
        Absolute path to the source ``.fodt`` file. Used for resolving
        relative ``xlink:href`` values that point at sibling FODT files and
        for emitting source provenance in the YAML front matter.
    parts_root:
        The ``parts/`` directory at the root of the manual. Used for
        resolving fodt cross-references.
    image_prefix:
        Path prefix (relative URL) prepended to extracted image filenames in
        the emitted Markdown. Defaults to ``../_images/`` which works for
        any page nested under ``docs/``.
    """

    def __init__(
        self,
        source: Path,
        parts_root: Path,
        image_prefix: str = "../_images/",
    ) -> None:
        self.source = source
        self.parts_root = parts_root
        self.image_prefix = image_prefix
        self._title: str = source.stem
        self._bookmarks: Dict[str, str] = {}
        self._images: Dict[str, bytes] = {}
        self._fodt_links: List[Tuple[str, Optional[Path], str]] = []
        self._unresolved: List[str] = []
        self._style_map: Optional[StyleMap] = None

    # --- public API --------------------------------------------------------

    def convert(self) -> ConversionResult:
        """Parse :attr:`source` and return the conversion result."""
        parser = etree.XMLParser(huge_tree=True, recover=True)
        tree = etree.parse(str(self.source), parser=parser)
        return self.convert_root(tree.getroot())

    def convert_root(self, root: etree._Element) -> ConversionResult:
        self._style_map = StyleMap.from_root(root)
        meta_title = root.findtext(
            f"{q('office', 'meta')}/{q('dc', 'title')}"
        )
        if meta_title:
            self._title = meta_title.strip() or self._title

        body = root.find(f"{q('office', 'body')}/{q('office', 'text')}")
        if body is None:
            return ConversionResult("", self._title, {}, {}, [], [])

        # First pass: collect all bookmarks declared anywhere in the body so
        # that intra-page links can be rewritten to clean anchors.
        for bm in body.iter(q("text", "bookmark-start")):
            name = bm.get(q("text", "name"))
            if name:
                self._bookmarks[name] = _slugify(name)
        for bm in body.iter(q("text", "bookmark")):
            name = bm.get(q("text", "name"))
            if name:
                self._bookmarks[name] = _slugify(name)

        # Render the body and prepend YAML front matter.
        body_md = self._render_body(body)
        front = self._front_matter()
        return ConversionResult(
            markdown=front + body_md.rstrip() + "\n",
            title=self._title,
            bookmarks=self._bookmarks,
            images=self._images,
            unresolved_links=self._unresolved,
            fodt_links=self._fodt_links,
        )

    # --- front matter ------------------------------------------------------

    def _front_matter(self) -> str:
        try:
            rel_source = self.source.relative_to(self.parts_root.parent)
            source_str = rel_source.as_posix()
        except ValueError:
            source_str = self.source.name
        # YAML-escape the title (single-quote style is safe for our titles
        # since none of them contain single quotes; we still escape if so).
        title = self._title.replace("'", "''")
        return (
            "---\n"
            f"title: '{title}'\n"
            f"source: {source_str}\n"
            "generated_by: scripts/python/src/fodt/fodt2md\n"
            "---\n\n"
        )

    # --- body --------------------------------------------------------------

    def _render_body(self, body: etree._Element) -> str:
        out: List[str] = []
        # Walk only direct children (sections/paragraphs/headings/tables).
        # Sections wrap their children; we recurse through them transparently.
        out.extend(self._render_block_children(body))
        return "\n".join(out).strip() + "\n"

    def _render_block_children(self, parent: etree._Element) -> List[str]:
        out: List[str] = []
        # Buffer for grouping consecutive code paragraphs into one fence.
        code_buffer: List[str] = []

        def flush_code() -> None:
            if not code_buffer:
                return
            out.append(f"```{ECLIPSE_FENCE_LANG}")
            # Strip trailing blank lines from code blocks.
            while code_buffer and not code_buffer[-1].strip():
                code_buffer.pop()
            out.extend(code_buffer)
            out.append("```")
            out.append("")
            code_buffer.clear()

        for child in parent:
            tag = _local_name(child)
            ns = _ns(child.tag)
            if ns == NS["text"] and tag == "section":
                # Render section children inline, but flush any pending code
                # block first so it doesn't bleed across the boundary.
                flush_code()
                out.extend(self._render_block_children(child))
                continue
            if ns == NS["text"] and tag == "p":
                style = child.get(q("text", "style-name"))
                if self._style_map and self._style_map.is_code_paragraph(style):
                    code_buffer.append(self._render_code_paragraph(child))
                    continue
                flush_code()
                rendered = self._render_paragraph(child)
                if rendered.strip() or out and out[-1] != "":
                    out.append(rendered)
                continue
            if ns == NS["text"] and tag == "h":
                flush_code()
                out.extend(self._render_heading(child))
                continue
            if ns == NS["text"] and tag in {"list"}:
                flush_code()
                out.extend(self._render_list(child, level=0, ordered=False))
                out.append("")
                continue
            if ns == NS["table"] and tag == "table":
                flush_code()
                out.extend(self._render_table(child))
                out.append("")
                continue
            # Recurse into anything else that may contain block content.
            if len(child):
                flush_code()
                out.extend(self._render_block_children(child))
        flush_code()
        return out

    # --- headings ----------------------------------------------------------

    def _render_heading(self, el: etree._Element) -> List[str]:
        level = int(el.get(q("text", "outline-level"), "1") or "1")
        level = max(1, min(level, 6))
        text = self._inline(el).strip()
        # The first heading in the document becomes the page title.
        if not getattr(self, "_first_heading_seen", False) and text:
            # Strip any leading inline anchors (HTML <a id> emitted by
            # bookmark-start handling) to get a clean YAML title.
            clean = re.sub(r"<a id=\"[^\"]+\"></a>", "", text).strip()
            if clean:
                self._title = clean
            self._first_heading_seen = True
        return ["", f"{'#' * level} {text}", ""]

    # --- paragraphs --------------------------------------------------------

    def _render_paragraph(self, el: etree._Element) -> str:
        # Inline content; if the paragraph is empty, emit a blank line.
        text = self._inline(el)
        return text if text.strip() else ""

    def _render_code_paragraph(self, el: etree._Element) -> str:
        # For code paragraphs, preserve whitespace exactly. ``text:s
        # text:c="N"`` expands to N spaces, and ``text:tab`` to a tab.
        parts: List[str] = []
        if el.text:
            parts.append(el.text)
        for child in el:
            tag = _local_name(child)
            ns = _ns(child.tag)
            if ns == NS["text"]:
                if tag == "s":
                    count = int(child.get(q("text", "c"), "1") or "1")
                    parts.append(" " * count)
                elif tag == "tab":
                    parts.append("\t")
                elif tag == "line-break":
                    parts.append("\n")
                else:
                    parts.append(self._inline_text_only(child))
            else:
                parts.append(self._inline_text_only(child))
            if child.tail:
                parts.append(child.tail)
        return "".join(parts).rstrip()

    def _inline_text_only(self, el: etree._Element) -> str:
        return "".join(el.itertext())

    # --- inline runs -------------------------------------------------------

    def _inline(self, el: etree._Element) -> str:
        out: List[str] = []
        if el.text:
            out.append(_md_escape(el.text))
        for child in el:
            out.append(self._render_inline_child(child))
            if child.tail:
                out.append(_md_escape(child.tail))
        return "".join(out)

    def _render_inline_child(self, child: etree._Element) -> str:
        tag = _local_name(child)
        ns = _ns(child.tag)
        if ns == NS["text"]:
            if tag == "span":
                return self._render_span(child)
            if tag == "a":
                return self._render_link(child)
            if tag == "s":
                count = int(child.get(q("text", "c"), "1") or "1")
                return " " * count
            if tag == "tab":
                return "\t"
            if tag == "line-break":
                return "  \n"
            if tag == "bookmark-start" or tag == "bookmark":
                name = child.get(q("text", "name"))
                if name:
                    self._bookmarks[name] = _slugify(name)
                    return f'<a id="{_slugify(name)}"></a>'
                return ""
            if tag in {"bookmark-end", "soft-page-break", "sequence-decls"}:
                return ""
            if tag == "sequence":
                return _md_escape("".join(child.itertext()))
        if ns == NS["draw"] and tag == "frame":
            return self._render_frame(child)
        if ns == NS["draw"] and tag in {"image", "object"}:
            return self._render_frame(child.getparent() or child)
        if ns == NS["math"] and tag == "math":
            return latex_for_math(child) or ""
        # Fallback: render any nested children.
        if len(child):
            return self._inline(child)
        return _md_escape("".join(child.itertext()))

    def _render_span(self, el: etree._Element) -> str:
        inner = self._inline(el)
        if not inner.strip():
            return inner
        if not self._style_map:
            return inner
        style = el.get(q("text", "style-name"))
        sm = self._style_map
        if sm.is_superscript(style):
            return f"<sup>{inner}</sup>"
        if sm.is_subscript(style):
            return f"<sub>{inner}</sub>"
        if sm.is_monospace(style):
            return f"`{''.join(el.itertext())}`"
        if sm.is_bold(style) and sm.is_italic(style):
            return f"***{inner}***"
        if sm.is_bold(style):
            return f"**{inner}**"
        if sm.is_italic(style):
            return f"*{inner}*"
        return inner

    # --- links -------------------------------------------------------------

    def _render_link(self, el: etree._Element) -> str:
        href = el.get(q("xlink", "href"), "")
        text = self._inline(el).strip() or href
        if not href:
            return text
        if href.startswith("#"):
            target = href[1:]
            # Target may include "|outline" or other LibreOffice suffixes.
            target = target.split("|", 1)[0]
            anchor = self._bookmarks.get(target) or _slugify(target)
            return f"[{text}](#{anchor})"
        if href.startswith(("http://", "https://", "mailto:")):
            return f"[{text}]({href})"
        if href.endswith(".fodt") or ".fodt#" in href:
            href_path, _, anchor = href.partition("#")
            resolved = resolve_fodt_href(href_path, self.source, self.parts_root)
            self._fodt_links.append((href, resolved, anchor))
            if resolved is None:
                self._unresolved.append(href)
            # Emit a placeholder; the post-processor rewrites this to the
            # actual ``.md`` relative path once the full path map is known.
            placeholder = self._link_placeholder(href, anchor)
            return f"[{text}]({placeholder})"
        self._unresolved.append(href)
        return f"[{text}]({href})"

    def _link_placeholder(self, href: str, anchor: str) -> str:
        # The post-processor recognises ``fodt2md:<base64>`` placeholders.
        token = base64.urlsafe_b64encode(
            f"{href}\x00{anchor}".encode("utf-8")
        ).decode("ascii")
        return f"fodt2md:{token}"

    # --- images ------------------------------------------------------------

    def _render_frame(self, el: etree._Element) -> str:
        # Prefer a math object if present.
        math_el = el.find(f".//{q('math', 'math')}")
        if math_el is not None:
            return latex_for_math(math_el) or ""
        # Otherwise look for an image (binary or referenced).
        image_el = el.find(q("draw", "image"))
        if image_el is None:
            return ""
        binary = image_el.find(q("office", "binary-data"))
        href = image_el.get(q("xlink", "href"))
        alt = el.get(q("draw", "name")) or self.source.stem
        if binary is not None and binary.text:
            data = base64.b64decode("".join(binary.text.split()))
            digest = hashlib.sha1(data).hexdigest()[:12]
            ext = _guess_image_extension(data)
            filename = f"{_slugify(alt)}-{digest}.{ext}"
            self._images[filename] = data
            return f'<img src="{self.image_prefix}{filename}" alt="{alt}" />'
        if href:
            return f'<img src="{href}" alt="{alt}" />'
        return ""

    # --- lists -------------------------------------------------------------

    def _render_list(
        self, el: etree._Element, level: int, ordered: bool
    ) -> List[str]:
        out: List[str] = []
        indent = "    " * level
        for idx, item in enumerate(el.findall(q("text", "list-item")), 1):
            marker = f"{idx}." if ordered else "-"
            # First paragraph of the item goes on the marker line; subsequent
            # block content is indented under it.
            first_done = False
            for child in item:
                tag = _local_name(child)
                if tag == "p":
                    text = self._inline(child).strip()
                    if not first_done:
                        out.append(f"{indent}{marker} {text}")
                        first_done = True
                    else:
                        out.append(f"{indent}    {text}")
                elif tag == "list":
                    out.extend(self._render_list(child, level + 1, ordered))
                else:
                    text = "".join(child.itertext()).strip()
                    if text:
                        if not first_done:
                            out.append(f"{indent}{marker} {text}")
                            first_done = True
                        else:
                            out.append(f"{indent}    {text}")
            if not first_done:
                out.append(f"{indent}{marker}")
        return out

    # --- tables ------------------------------------------------------------

    def _render_table(self, el: etree._Element) -> List[str]:
        # Expand columns (handle ``table:number-columns-repeated``) so we
        # know the true column count.
        col_count = 0
        for col in el.findall(q("table", "table-column")):
            n = int(col.get(q("table", "number-columns-repeated"), "1") or "1")
            col_count += n
        rows: List[List[str]] = []
        header_rows: List[List[str]] = []
        complex_table = False

        def collect(row_parent: etree._Element, target: List[List[str]]) -> None:
            nonlocal complex_table
            for row in row_parent.findall(q("table", "table-row")):
                cells: List[str] = []
                for cell in row.findall(q("table", "table-cell")):
                    span = int(
                        cell.get(q("table", "number-columns-spanned"), "1")
                        or "1"
                    )
                    parts: List[str] = []
                    for sub in cell:
                        if _local_name(sub) == "p":
                            parts.append(self._inline(sub).strip())
                        elif _local_name(sub) == "list":
                            complex_table = True
                            parts.append(
                                " ".join(self._render_list(sub, 0, False))
                            )
                        elif _local_name(sub) == "table":
                            complex_table = True
                            parts.append("[nested table]")
                        else:
                            parts.append("".join(sub.itertext()).strip())
                    text = " ".join(p for p in parts if p)
                    if "\n" in text or len(parts) > 2:
                        complex_table = True
                    text = text.replace("|", r"\|").replace("\n", " ")
                    cells.append(text)
                    for _ in range(span - 1):
                        cells.append("")
                target.append(cells)

        for hdr in el.findall(q("table", "table-header-rows")):
            collect(hdr, header_rows)
        collect(el, rows)

        if not header_rows and not rows:
            return []
        if not header_rows:
            header_rows = [rows.pop(0)] if rows else [[""] * col_count]

        # Pad to col_count columns.
        def pad(r: List[str]) -> List[str]:
            return (r + [""] * col_count)[:col_count] if col_count else r

        header = pad(header_rows[0])
        out: List[str] = []
        if col_count == 0:
            col_count = len(header)
        out.append("| " + " | ".join(header) + " |")
        out.append("| " + " | ".join(["---"] * len(header)) + " |")
        for r in rows:
            out.append("| " + " | ".join(pad(r)) + " |")
        return out


# ---------------------------------------------------------------------------
# Image helpers
# ---------------------------------------------------------------------------


def _guess_image_extension(data: bytes) -> str:
    if data.startswith(b"\x89PNG"):
        return "png"
    if data.startswith(b"\xff\xd8\xff"):
        return "jpg"
    if data.startswith(b"GIF8"):
        return "gif"
    if data.startswith(b"<svg") or data.startswith(b"<?xml"):
        return "svg"
    if data[:4] == b"VCLM":  # LibreOffice formula metafile fallback.
        return "bin"
    return "bin"
