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
    _clean_captions,
    _clean_pipe_table_blockquotes,
    _grid_table_to_pipe,
    _merge_cell_parts,
    _find_col_positions,
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
