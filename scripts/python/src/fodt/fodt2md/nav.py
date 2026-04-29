"""Build a deterministic MkDocs navigation tree from ``docs/``.

The function walks the generated Markdown tree and produces a list of
``{title: path}`` mappings that can be inserted into ``mkdocs.yml`` or used
by an MkDocs hook (``hooks: [nav.py]``). Numeric ordering ensures Chapter 2
sorts before Chapter 10.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, List

import os


def _natural_key(name: str) -> List[Any]:
    """Sort key that keeps numeric prefixes in numeric order."""
    parts = re.split(r"(\d+)", name)
    return [int(p) if p.isdigit() else p.lower() for p in parts]


def _title_for(md_path: Path) -> str:
    try:
        head = md_path.read_text(encoding="utf-8").splitlines()[:20]
    except OSError:
        return md_path.stem
    in_front = False
    for line in head:
        if line.strip() == "---":
            in_front = not in_front
            continue
        if in_front and line.startswith("title:"):
            return line.split(":", 1)[1].strip().strip("'\"")
    return md_path.stem


def build_nav(docs_root: Path) -> List[Dict[str, Any]]:
    """Return an MkDocs ``nav`` data structure mirroring ``docs_root``."""
    docs_root = docs_root.resolve()
    if not docs_root.exists():
        return []

    def walk(folder: Path) -> List[Dict[str, Any]]:
        entries: List[Dict[str, Any]] = []
        children = sorted(
            (p for p in folder.iterdir() if not p.name.startswith("_") and not p.name.startswith(".")),
            key=lambda p: (p.is_file(), _natural_key(p.name)),
        )
        for child in children:
            if child.is_dir():
                sub = walk(child)
                if sub:
                    entries.append({_pretty_dir(child.name): sub})
                continue
            if child.suffix != ".md" or child.name == "index.md":
                continue
            rel = child.relative_to(docs_root).as_posix()
            entries.append({_title_for(child): rel})
        return entries

    nav: List[Dict[str, Any]] = []
    index = docs_root / "index.md"
    if index.exists():
        nav.append({"Home": "index.md"})
    nav.extend(walk(docs_root))
    return nav


def _pretty_dir(name: str) -> str:
    if name.lower() == "chapters":
        return "Chapters"
    if name.lower() == "appendices":
        return "Appendices"
    if name.lower() == "sections":
        return "Sections"
    if name.lower() == "subsections":
        return "Keywords"
    if re.fullmatch(r"\d+(\.\d+)?", name):
        return f"Chapter {name}" if "." not in name else f"Section {name}"
    return name.replace("_", " ")


def write_mkdocs_nav_yaml(docs_root: Path, output: Path) -> None:
    """Write the nav as YAML for inclusion in ``mkdocs.yml`` (debug helper)."""
    import yaml  # local import; pyyaml is optional for the converter itself

    nav = build_nav(docs_root)
    output.write_text(yaml.safe_dump({"nav": nav}, sort_keys=False), encoding="utf-8")


# ---------------------------------------------------------------------------
# MkDocs hook entry point: ``hooks: [scripts/python/src/fodt/fodt2md/nav.py]``
# ---------------------------------------------------------------------------


def on_config(config, **kwargs):  # noqa: D401 - mkdocs hook signature
    """MkDocs hook that injects the auto-generated navigation."""
    docs_root = Path(config.get("docs_dir") or os.getcwd())
    nav = build_nav(docs_root)
    if nav:
        config["nav"] = nav
    return config
