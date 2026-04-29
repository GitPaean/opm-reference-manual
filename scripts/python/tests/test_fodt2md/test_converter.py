"""Unit tests for the FODT → Markdown converter.

These tests build small in-memory FODT documents and assert the converter
produces the expected Markdown. They do not depend on real FODT files in
``parts/`` so they remain fast and stable.
"""

from __future__ import annotations

from pathlib import Path
from textwrap import dedent

import pytest
from lxml import etree

from fodt.fodt2md.converter import FodtConverter
from fodt.fodt2md.mathml import mathml_to_latex


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


_NS_DECLS = (
    'xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" '
    'xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" '
    'xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" '
    'xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" '
    'xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" '
    'xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" '
    'xmlns:xlink="http://www.w3.org/1999/xlink" '
    'xmlns:dc="http://purl.org/dc/elements/1.1/" '
    'xmlns:math="http://www.w3.org/1998/Math/MathML"'
)


def _build_doc(body: str, styles: str = "") -> etree._Element:
    xml = (
        f"<office:document {_NS_DECLS}>"
        f"<office:styles>{styles}</office:styles>"
        f"<office:automatic-styles></office:automatic-styles>"
        f"<office:body><office:text>{body}</office:text></office:body>"
        f"</office:document>"
    )
    return etree.fromstring(xml)


def _convert(body: str, styles: str = "", tmp_path: Path | None = None) -> str:
    root = _build_doc(body, styles)
    src = (tmp_path or Path("/tmp")) / "fake.fodt"
    src.touch()
    conv = FodtConverter(src, src.parent)
    result = conv.convert_root(root)
    return result.markdown


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_heading_levels_match_outline_level(tmp_path):
    body = (
        '<text:h text:outline-level="1">Top</text:h>'
        '<text:h text:outline-level="3">Deep</text:h>'
    )
    md = _convert(body, tmp_path=tmp_path)
    assert "# Top" in md
    assert "### Deep" in md


def test_paragraph_with_bold_and_italic_spans(tmp_path):
    styles = (
        '<style:style style:name="B" style:family="text">'
        '  <style:text-properties fo:font-weight="bold"/>'
        '</style:style>'
        '<style:style style:name="I" style:family="text">'
        '  <style:text-properties fo:font-style="italic"/>'
        '</style:style>'
    )
    body = (
        '<text:p>plain '
        '<text:span text:style-name="B">bold</text:span> and '
        '<text:span text:style-name="I">italic</text:span> end.</text:p>'
    )
    md = _convert(body, styles, tmp_path=tmp_path)
    assert "**bold**" in md
    assert "*italic*" in md


def test_consecutive_code_paragraphs_grouped_into_eclipse_fence(tmp_path):
    styles = (
        '<style:style style:name="EX" style:family="paragraph">'
        '  <style:text-properties style:font-family-generic="modern"/>'
        '</style:style>'
    )
    body = (
        '<text:p>preamble</text:p>'
        '<text:p text:style-name="EX">INCLUDE</text:p>'
        '<text:p text:style-name="EX"><text:s text:c="3"/>\'foo.inc\' /</text:p>'
        '<text:p>after</text:p>'
    )
    md = _convert(body, styles, tmp_path=tmp_path)
    assert "```eclipse\nINCLUDE\n   'foo.inc' /\n```" in md
    assert "preamble" in md and "after" in md


def test_pipe_table(tmp_path):
    body = (
        '<table:table>'
        '<table:table-column/><table:table-column/>'
        '<table:table-row>'
        '  <table:table-cell><text:p>A</text:p></table:table-cell>'
        '  <table:table-cell><text:p>B</text:p></table:table-cell>'
        '</table:table-row>'
        '<table:table-row>'
        '  <table:table-cell><text:p>1</text:p></table:table-cell>'
        '  <table:table-cell><text:p>2</text:p></table:table-cell>'
        '</table:table-row>'
        '</table:table>'
    )
    md = _convert(body, tmp_path=tmp_path)
    assert "| A | B |" in md
    assert "| --- | --- |" in md
    assert "| 1 | 2 |" in md


def test_internal_anchor_link_uses_bookmark_slug(tmp_path):
    body = (
        '<text:h text:outline-level="2">'
        '<text:bookmark-start text:name="MyAnchor"/>Heading'
        '<text:bookmark-end text:name="MyAnchor"/>'
        '</text:h>'
        '<text:p><text:a xlink:href="#MyAnchor">link</text:a></text:p>'
    )
    md = _convert(body, tmp_path=tmp_path)
    assert "(#myanchor)" in md
    assert "[link]" in md


def test_fodt_cross_link_emits_placeholder(tmp_path):
    body = (
        '<text:p><text:a xlink:href="../../other/FOO.fodt#X">x</text:a></text:p>'
    )
    md = _convert(body, tmp_path=tmp_path)
    assert "fodt2md:" in md  # placeholder for postprocessor


def test_image_extracted_to_bytes(tmp_path):
    # 1x1 transparent PNG, base64 encoded.
    png_b64 = (
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjC"
        "B0C8AAAAASUVORK5CYII="
    )
    body = (
        f'<text:p><draw:frame draw:name="logo">'
        f'<draw:image><office:binary-data>{png_b64}</office:binary-data>'
        f'</draw:image></draw:frame></text:p>'
    )
    root = _build_doc(body)
    src = tmp_path / "fake.fodt"
    src.touch()
    conv = FodtConverter(src, src.parent)
    result = conv.convert_root(root)
    assert any(name.endswith(".png") for name in result.images)
    assert "<img " in result.markdown


def test_mathml_to_latex_basic_fraction():
    xml = (
        '<math xmlns="http://www.w3.org/1998/Math/MathML">'
        '<mfrac><mi>a</mi><mi>b</mi></mfrac>'
        '</math>'
    )
    el = etree.fromstring(xml)
    assert mathml_to_latex(el) == "\\frac{a}{b}"


def test_mathml_to_latex_handles_msub():
    xml = (
        '<math xmlns="http://www.w3.org/1998/Math/MathML">'
        '<msub><mi>x</mi><mn>0</mn></msub>'
        '</math>'
    )
    el = etree.fromstring(xml)
    assert mathml_to_latex(el) == "{x}_{0}"


def test_nested_unordered_list(tmp_path):
    body = (
        '<text:list>'
        '<text:list-item><text:p>one</text:p></text:list-item>'
        '<text:list-item>'
        '  <text:p>two</text:p>'
        '  <text:list>'
        '    <text:list-item><text:p>two-a</text:p></text:list-item>'
        '  </text:list>'
        '</text:list-item>'
        '</text:list>'
    )
    md = _convert(body, tmp_path=tmp_path)
    assert "- one" in md
    assert "- two" in md
    assert "    - two\\-a" in md or "    - two-a" in md
