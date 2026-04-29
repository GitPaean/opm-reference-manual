"""Tests for the path mapping and nav generation helpers."""

from __future__ import annotations

from pathlib import Path

from fodt.fodt2md.nav import build_nav
from fodt.fodt2md.paths import (
    build_path_map,
    fodt_to_md_target,
    relative_md_link,
)


def test_main_fodt_maps_to_index_md(tmp_path):
    parts = tmp_path / "parts"
    docs = tmp_path / "docs"
    parts.mkdir()
    docs.mkdir()
    main = parts / "main.fodt"
    main.touch()
    target = fodt_to_md_target(main, parts, docs)
    assert target == (docs / "index.md").resolve()


def test_subsection_fodt_mirrors_layout(tmp_path):
    parts = tmp_path / "parts"
    docs = tmp_path / "docs"
    sub = parts / "chapters" / "subsections" / "4.3"
    sub.mkdir(parents=True)
    docs.mkdir()
    src = sub / "COLUMNS.fodt"
    src.touch()
    target = fodt_to_md_target(src, parts, docs)
    assert target.relative_to(docs.resolve()) == Path(
        "chapters/subsections/4.3/COLUMNS.md"
    )


def test_relative_md_link_uses_dotdot(tmp_path):
    a = tmp_path / "docs" / "chapters" / "4.md"
    b = tmp_path / "docs" / "chapters" / "subsections" / "4.3" / "X.md"
    a.parent.mkdir(parents=True, exist_ok=True)
    b.parent.mkdir(parents=True, exist_ok=True)
    a.touch()
    b.touch()
    assert relative_md_link(a, b, "anchor") == "subsections/4.3/X.md#anchor"


def test_build_path_map_round_trip(tmp_path):
    parts = tmp_path / "parts"
    docs = tmp_path / "docs"
    (parts / "chapters").mkdir(parents=True)
    docs.mkdir()
    a = parts / "main.fodt"
    b = parts / "chapters" / "1.fodt"
    a.touch()
    b.touch()
    pmap = build_path_map([a, b], parts, docs)
    assert pmap[a.resolve()].target.name == "index.md"
    assert pmap[b.resolve()].rel_target == Path("chapters/1.md")


def test_build_nav_orders_chapters_naturally(tmp_path):
    docs = tmp_path / "docs"
    (docs / "chapters").mkdir(parents=True)
    (docs / "index.md").write_text("---\ntitle: Home\n---\n")
    for n in ("1", "2", "10"):
        (docs / "chapters" / f"{n}.md").write_text(f"---\ntitle: Chapter {n}\n---\n")
    nav = build_nav(docs)
    chapters = next(item["Chapters"] for item in nav if "Chapters" in item)
    titles = [list(entry.keys())[0] for entry in chapters]
    assert titles == ["Chapter 1", "Chapter 2", "Chapter 10"]
