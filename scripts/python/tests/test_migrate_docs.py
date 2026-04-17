"""Tests for the migrate_docs.py post-processing helpers."""
from __future__ import annotations

import sys
import textwrap
from pathlib import Path

import pytest

# Ensure the migrate_docs module is importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from migrate_docs import (
    _convert_grid_tables,
    _clean_broken_links,
    _clean_captions,
    _clean_pipe_table_blockquotes,
    _grid_table_to_pipe,
    _merge_cell_parts,
    _find_col_positions,
    _strip_outline_links,
    _MD_ANCHOR_TO_HTML_RE,
    _EMPTY_ANCHOR_RE,
)


# ---------------------------------------------------------------------------
# _find_col_positions
# ---------------------------------------------------------------------------

class TestFindColPositions:
    def test_simple(self):
        assert _find_col_positions("+---+---+") == [0, 4, 8]

    def test_unequal_widths(self):
        assert _find_col_positions("+--+------+") == [0, 3, 10]

    def test_trailing_whitespace(self):
        assert _find_col_positions("+---+---+   ") == [0, 4, 8]


# ---------------------------------------------------------------------------
# _merge_cell_parts
# ---------------------------------------------------------------------------

class TestMergeCellParts:
    def test_single_part(self):
        assert _merge_cell_parts(["hello"]) == "hello"

    def test_consecutive_parts_joined_with_space(self):
        assert _merge_cell_parts(["a", "b", "c"]) == "a b c"

    def test_paragraph_break(self):
        assert _merge_cell_parts(["a", "", "b"]) == "a<br>b"

    def test_empty(self):
        assert _merge_cell_parts([]) == ""

    def test_all_empty(self):
        assert _merge_cell_parts(["", "", ""]) == ""

    def test_multiple_paragraphs(self):
        assert _merge_cell_parts(["a", "", "b", "", "c"]) == "a<br>b<br>c"


# ---------------------------------------------------------------------------
# _grid_table_to_pipe
# ---------------------------------------------------------------------------

class TestGridTableToPipe:
    def test_simple_no_header_separator(self):
        lines = [
            "+------+-------+",
            "| > H1 | > H2  |",
            "+------+-------+",
            "| > D1 | > D2  |",
            "+------+-------+",
        ]
        result = _grid_table_to_pipe(lines)
        assert result == (
            "| H1 | H2 |\n"
            "| --- | --- |\n"
            "| D1 | D2 |"
        )

    def test_header_separator_with_equals(self):
        lines = [
            "+------+-------+",
            "| > H1 | > H2  |",
            "+======+=======+",
            "| > D1 | > D2  |",
            "+------+-------+",
        ]
        result = _grid_table_to_pipe(lines)
        assert result == (
            "| H1 | H2 |\n"
            "| --- | --- |\n"
            "| D1 | D2 |"
        )

    def test_multi_line_cell(self):
        lines = [
            "+------+-------+",
            "| > A  | > B   |",
            "+------+-------+",
            "| > C  | > D   |",
            "|      |       |",
            "| > E  | > F   |",
            "+------+-------+",
        ]
        result = _grid_table_to_pipe(lines)
        assert result == (
            "| A | B |\n"
            "| --- | --- |\n"
            "| C<br>E | D<br>F |"
        )

    def test_blockquote_stripped(self):
        lines = [
            "+------+------+",
            "| > X  | > Y  |",
            "+------+------+",
        ]
        result = _grid_table_to_pipe(lines)
        assert ">" not in result

    def test_four_columns(self):
        lines = [
            "+-----+------+-------+---------+",
            "| No. | Name | Desc  | Default |",
            "+-----+------+-------+---------+",
            "| 1   | FOO  | Stuff | 42      |",
            "+-----+------+-------+---------+",
        ]
        result = _grid_table_to_pipe(lines)
        assert result.count("|") == 5 * 3  # 5 pipes per row × 3 rows (header, sep, data)
        assert "| --- | --- | --- | --- |" in result


# ---------------------------------------------------------------------------
# _convert_grid_tables  (integration-level)
# ---------------------------------------------------------------------------

class TestConvertGridTables:
    def test_basic_conversion(self):
        text = textwrap.dedent("""\
            Some text before.

            +---+---+
            | A | B |
            +---+---+
            | 1 | 2 |
            +---+---+

            Some text after.""")
        result = _convert_grid_tables(text)
        assert "+---+---+" not in result
        assert "| A | B |" in result
        assert "| --- | --- |" in result
        assert "Some text before." in result
        assert "Some text after." in result

    def test_code_block_not_converted(self):
        text = textwrap.dedent("""\
            ```
            +---+---+
            | A | B |
            +---+---+
            ```""")
        result = _convert_grid_tables(text)
        # Table inside code fence should be untouched.
        assert "+---+---+" in result

    def test_text_without_tables_unchanged(self):
        text = "Hello world\nNo tables here."
        assert _convert_grid_tables(text) == text

    def test_incomplete_grid_table_not_converted(self):
        text = "+---+---+\n| A | B |"
        result = _convert_grid_tables(text)
        # Missing closing separator → kept as-is.
        assert "+---+---+" in result


# ---------------------------------------------------------------------------
# _clean_pipe_table_blockquotes
# ---------------------------------------------------------------------------

class TestCleanPipeTableBlockquotes:
    def test_strips_blockquote_in_pipe_row(self):
        text = "| > Col1 | > Col2 |\n|---|---|\n| > Data | > Data |"
        result = _clean_pipe_table_blockquotes(text)
        assert "> " not in result
        assert "| Col1 | Col2 |" in result

    def test_non_table_lines_untouched(self):
        text = "> This is a real blockquote"
        assert _clean_pipe_table_blockquotes(text) == text


# ---------------------------------------------------------------------------
# _clean_captions
# ---------------------------------------------------------------------------

class TestCleanCaptions:
    def test_caption_converted_to_italic(self):
        text = "::: caption\nTable 1: Title\n:::"
        result = _clean_captions(text)
        assert result.strip() == "*Table 1: Title*"

    def test_empty_caption_removed(self):
        text = "::: caption\n:::"
        result = _clean_captions(text)
        assert result.strip() == ""

    def test_text_around_caption_preserved(self):
        text = "Before\n\n::: caption\nTable 1: Title\n:::\n\nAfter"
        result = _clean_captions(text)
        assert "Before" in result
        assert "After" in result
        assert "*Table 1: Title*" in result


# ---------------------------------------------------------------------------
# _strip_outline_links
# ---------------------------------------------------------------------------

class TestStripOutlineLinks:
    def test_simple_outline_link(self):
        text = "[RUNSPEC](#3.RUNSPEC SECTION|outline)"
        assert _strip_outline_links(text) == "RUNSPEC"

    def test_nested_brackets_in_display(self):
        text = "[[text](#anchor)](#url|outline)"
        assert _strip_outline_links(text) == "[text](#anchor)"

    def test_parens_in_url(self):
        text = (
            "[[HWKRO -- Kro(Swl) (High Salinity)](#a-391)]"
            "(#8.3.67.HWKRO – Kro(Swl) (High Salinity)|outline)"
        )
        result = _strip_outline_links(text)
        assert "|outline" not in result
        assert "HWKRO" in result

    def test_no_outline(self):
        text = "no outline here"
        assert _strip_outline_links(text) == text

    def test_empty_display(self):
        text = "[](#empty|outline)"
        assert _strip_outline_links(text) == ""

    def test_multiple_outline_links(self):
        text = "[A](#x|outline) and [B](#y|outline)"
        assert _strip_outline_links(text) == "A and B"

    def test_no_backtracking_on_pipe_table(self):
        """Ensure that pipe tables with many [text](#anchor) links are fast."""
        row = "| " + " | ".join(
            f"[KW{i}](#anchor-{i})" for i in range(50)
        ) + " |"
        import time
        start = time.time()
        result = _strip_outline_links(row)
        elapsed = time.time() - start
        assert elapsed < 1.0  # must not cause catastrophic backtracking
        assert result == row  # no |outline → unchanged


# ---------------------------------------------------------------------------
# _clean_broken_links  (integration-level)
# ---------------------------------------------------------------------------

class TestCleanBrokenLinks:
    def test_refheading_stripped(self):
        text = "[WAGHYSTR](#__RefHeading___Toc207827_2026549522)"
        assert _clean_broken_links(text) == "WAGHYSTR"

    def test_refheading_html_stripped(self):
        text = '<a href="#__RefHeading___Toc27871_3671211675">CPR</a>'
        assert _clean_broken_links(text) == "CPR"

    def test_ref_heading_keyword_stripped(self):
        text = "[H2STORE](#REF_HEADING_KEYWORD_H2STORE)"
        assert _clean_broken_links(text) == "H2STORE"

    def test_outline_stripped(self):
        text = "[RUNSPEC](#3.RUNSPEC SECTION|outline)"
        assert _clean_broken_links(text) == "RUNSPEC"

    def test_empty_anchor_link_stripped(self):
        text = "section [](#anchor-2)"
        assert _clean_broken_links(text) == "section "

    def test_normal_links_preserved(self):
        text = "[Google](https://google.com)"
        assert _clean_broken_links(text) == text

    def test_mixed_content(self):
        text = (
            "The [FOO](#__RefHeading___Toc123_456) keyword "
            "in the [RUNSPEC](#3.RUNSPEC SECTION|outline) section."
        )
        result = _clean_broken_links(text)
        assert result == "The FOO keyword in the RUNSPEC section."

    def test_empty_html_refheading_anchor_stripped(self):
        text = '<a id="__RefHeading___Toc548127_947687768"></a>\nHello'
        assert _clean_broken_links(text) == "Hello"

    def test_double_underscore_in_anchor_id_collapsed(self):
        text = '<a id="REF_TABLE_OPM_FLOW_2025_04___APPENDIX_E"></a>'
        result = _clean_broken_links(text)
        assert "__" not in result
        assert '<a id="REF_TABLE_OPM_FLOW_2025_04_APPENDIX_E"></a>' == result

    def test_multiple_double_underscores_collapsed(self):
        text = '<a id="REF_TABLE_RESTART_DATA___G__KEYWORDS_F_7"></a>'
        result = _clean_broken_links(text)
        assert "__" not in result
        assert '<a id="REF_TABLE_RESTART_DATA_G_KEYWORDS_F_7"></a>' == result


class TestMdAnchorToHtml:
    """Tests for markdown []{#id} → <a id="id"></a> conversion."""

    def test_basic_conversion(self):
        text = "[]{#my_anchor}Some text"
        result = _MD_ANCHOR_TO_HTML_RE.sub(r'<a id="\1"></a>', text)
        assert result == '<a id="my_anchor"></a>Some text'

    def test_ref_table_anchor_in_caption(self):
        text = "*[]{#REF_TABLE_OPM_FLOW_2025_04___APPENDIX_E}Table A.1: Options*"
        result = _MD_ANCHOR_TO_HTML_RE.sub(r'<a id="\1"></a>', text)
        assert "{#" not in result
        assert '<a id="REF_TABLE_OPM_FLOW_2025_04___APPENDIX_E"></a>' in result

    def test_anchor_then_double_underscore_collapse(self):
        """Full pipeline: md→html conversion then double-underscore collapse."""
        text = "*[]{#REF_TABLE_OPM_FLOW_2025_04___APPENDIX_E}Table A.1*"
        text = _MD_ANCHOR_TO_HTML_RE.sub(r'<a id="\1"></a>', text)
        text = _clean_broken_links(text)
        assert "{#" not in text
        assert "__" not in text
        assert '*<a id="REF_TABLE_OPM_FLOW_2025_04_APPENDIX_E"></a>Table A.1*' == text

    def test_empty_anchor_stripped_after_conversion(self):
        """[]{#anchor-5} is converted to HTML then stripped by EMPTY_ANCHOR_RE."""
        text = "[]{#anchor-5} following text"
        text = _MD_ANCHOR_TO_HTML_RE.sub(r'<a id="\1"></a>', text)
        text = _EMPTY_ANCHOR_RE.sub("", text)
        assert text == "following text"

    def test_no_match_on_non_anchor(self):
        text = "Normal text without anchors"
        result = _MD_ANCHOR_TO_HTML_RE.sub(r'<a id="\1"></a>', text)
        assert result == text
