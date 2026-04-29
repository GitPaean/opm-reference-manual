"""Map source FODT paths to output Markdown paths and resolve cross-links.

The output tree mirrors the source tree under ``parts/`` so reviewers can
diff intuitively. Mapping the few special files (``main.fodt`` →
``index.md``) is centralised here so the converter and the navigation
builder agree.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Optional


@dataclass(frozen=True)
class PathMap:
    """Resolved mapping for a single source FODT file."""

    source: Path
    """Absolute path to the source FODT file."""

    target: Path
    """Absolute path to the output Markdown file."""

    rel_target: Path
    """Path of ``target`` relative to the docs root (``docs/``)."""


def fodt_to_md_target(source: Path, parts_root: Path, docs_root: Path) -> Path:
    """Return the ``.md`` output path for the given ``source`` FODT file.

    ``parts/main.fodt`` becomes ``docs/index.md``; everything else mirrors
    the source layout (``parts/X/Y.fodt`` → ``docs/X/Y.md``).
    """
    source = source.resolve()
    parts_root = parts_root.resolve()
    docs_root = docs_root.resolve()
    rel = source.relative_to(parts_root)
    if rel.as_posix() == "main.fodt":
        return docs_root / "index.md"
    return (docs_root / rel).with_suffix(".md")


def build_path_map(
    sources: Iterable[Path], parts_root: Path, docs_root: Path
) -> Dict[Path, PathMap]:
    """Build a ``{source: PathMap}`` for every FODT file in ``sources``."""
    out: Dict[Path, PathMap] = {}
    for src in sources:
        target = fodt_to_md_target(src, parts_root, docs_root)
        out[src.resolve()] = PathMap(
            source=src.resolve(),
            target=target,
            rel_target=target.relative_to(docs_root.resolve()),
        )
    return out


def relative_md_link(from_md: Path, to_md: Path, anchor: str = "") -> str:
    """Return a ``./foo/bar.md#anchor`` link from ``from_md`` to ``to_md``."""
    rel = Path(*_relparts(from_md.parent.resolve(), to_md.resolve()))
    href = rel.as_posix()
    if anchor:
        href = f"{href}#{anchor}"
    return href


def _relparts(base: Path, target: Path) -> list[str]:
    """Return ``target`` expressed relative to ``base`` as path parts.

    Pure-Python implementation so it works even when ``target`` is not a
    descendant of ``base`` (Python ≥ 3.12 has ``walk_up=True`` but we keep
    compatibility with 3.10).
    """
    base_parts = list(base.parts)
    target_parts = list(target.parts)
    common = 0
    for a, b in zip(base_parts, target_parts):
        if a != b:
            break
        common += 1
    up = [".."] * (len(base_parts) - common)
    down = target_parts[common:]
    return up + down or ["."]


def resolve_fodt_href(href: str, source: Path, parts_root: Path) -> Optional[Path]:
    """Resolve an ``xlink:href`` from a FODT file to an absolute FODT path.

    Handles ``../`` style relative references and the ``foo.fodt`` /
    ``foo.fodt#anchor`` forms used by the master and chapter documents.
    Returns ``None`` for non-fodt URLs (http://, mailto:, plain anchors).
    """
    if not href or href.startswith(("http://", "https://", "mailto:", "#")):
        return None
    href_path = href.split("#", 1)[0]
    if not href_path.endswith(".fodt"):
        return None
    candidate = (source.parent / href_path).resolve()
    if candidate.exists():
        return candidate
    # Try parts_root relative.
    candidate = (parts_root / href_path).resolve()
    if candidate.exists():
        return candidate
    return None
