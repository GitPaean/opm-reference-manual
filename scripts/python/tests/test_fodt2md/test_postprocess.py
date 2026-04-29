"""Tests for the post-processing pipeline."""

from __future__ import annotations

import base64
from pathlib import Path

from fodt.fodt2md.converter import ConversionResult
from fodt.fodt2md.paths import PathMap
from fodt.fodt2md.postprocess import (
    collapse_blank_lines,
    normalise_code_fences,
    postprocess,
    rewrite_fodt_links,
)


def test_collapse_blank_lines():
    md = "a\n\n\n\nb\n\n\nc\n"
    assert collapse_blank_lines(md) == "a\n\nb\n\nc\n"


def test_normalise_code_fence_strips_trailing_whitespace():
    md = "```eclipse\nINCLUDE   \n   'foo' /  \n```\n"
    out = normalise_code_fences(md)
    assert "INCLUDE\n" in out
    assert "'foo' /\n" in out
    assert out.endswith("\n")


def test_rewrite_fodt_links_resolves_to_relative_md(tmp_path):
    src_other = tmp_path / "parts" / "chapters" / "subsections" / "4.3" / "OTHER.fodt"
    src_other.parent.mkdir(parents=True, exist_ok=True)
    src_other.touch()
    src_self = tmp_path / "parts" / "chapters" / "4.fodt"
    src_self.touch()
    docs_root = tmp_path / "docs"
    self_md = docs_root / "chapters" / "4.md"
    other_md = docs_root / "chapters" / "subsections" / "4.3" / "OTHER.md"

    path_map = {
        src_self.resolve(): PathMap(
            source=src_self.resolve(),
            target=self_md,
            rel_target=Path("chapters/4.md"),
        ),
        src_other.resolve(): PathMap(
            source=src_other.resolve(),
            target=other_md,
            rel_target=Path("chapters/subsections/4.3/OTHER.md"),
        ),
    }
    bookmarks = {src_other.resolve(): {"someAnchor": "some-anchor"}}
    href = "subsections/4.3/OTHER.fodt"
    token = base64.urlsafe_b64encode(f"{href}\x00someAnchor".encode()).decode()
    md = f"see [other](fodt2md:{token}) please"
    sink: list[str] = []
    out = rewrite_fodt_links(md, self_md, path_map, bookmarks, sink)
    assert "subsections/4.3/OTHER.md#some-anchor" in out
    assert sink == []


def test_postprocess_pipeline_keeps_metadata():
    result = ConversionResult(
        markdown="title\n\n\n\nmore\n",
        title="t",
        bookmarks={"a": "a"},
        images={},
        unresolved_links=[],
        fodt_links=[],
    )
    final = postprocess(
        result, Path("/tmp/x.md"), path_map={}, bookmarks={}
    )
    assert final.title == "t"
    assert "\n\n\n" not in final.markdown
