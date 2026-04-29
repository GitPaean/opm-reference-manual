"""Post-processing pipeline applied after the FODT visitor produces Markdown.

These passes operate on the raw Markdown string and the side-channel state
collected by :class:`fodt.fodt2md.converter.FodtConverter` (the path map of
all FODT files in the build, the per-file bookmark tables). They are kept
small and composable so they can be reused by a future ``--postprocess-only``
mode that fixes already-generated Markdown without re-parsing the FODT.
"""

from __future__ import annotations

import base64
import re
from pathlib import Path
from typing import Dict, List

from .constants import ECLIPSE_FENCE_LANG
from .converter import ConversionResult
from .paths import PathMap, relative_md_link


_PLACEHOLDER_RE = re.compile(r"fodt2md:([A-Za-z0-9_\-=]+)")
_BLANKLINE_RE = re.compile(r"\n{3,}")


def collapse_blank_lines(md: str) -> str:
    """Replace any run of 3+ blank lines with 2."""
    return _BLANKLINE_RE.sub("\n\n", md)


def normalise_code_fences(md: str) -> str:
    """Trim trailing whitespace inside ``eclipse`` fenced blocks."""
    out_lines: List[str] = []
    in_fence = False
    for line in md.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            out_lines.append(line.rstrip())
            continue
        if in_fence:
            out_lines.append(line.rstrip())
        else:
            out_lines.append(line)
    return "\n".join(out_lines) + ("\n" if md.endswith("\n") else "")


def rewrite_fodt_links(
    md: str,
    source_md_path: Path,
    path_map: Dict[Path, PathMap],
    bookmarks: Dict[Path, Dict[str, str]],
    unresolved_sink: List[str],
) -> str:
    """Rewrite ``fodt2md:`` placeholders to ``./...md#anchor`` links.

    Placeholders are emitted by the converter for every cross-document
    ``xlink:href`` that pointed at another ``.fodt`` file. We resolve them
    here because we need the full per-build map of FODT → MD targets, plus
    the bookmark tables of *other* files, which aren't known when a single
    file is converted in isolation.
    """

    def _replace(match: re.Match) -> str:
        token = match.group(1)
        try:
            decoded = base64.urlsafe_b64decode(token + "===").decode("utf-8")
        except Exception:  # pragma: no cover - defensive
            return match.group(0)
        href, _, anchor = decoded.partition("\x00")
        href_path, _, embedded_anchor = href.partition("#")
        anchor = anchor or embedded_anchor
        # Find the FODT file by suffix-matching its absolute path against
        # the values in ``path_map``. The href may be relative ("../9/2.fodt")
        # which the converter has already attempted to resolve.
        target: PathMap | None = None
        for src, pm in path_map.items():
            if src.as_posix().endswith(href_path):
                target = pm
                break
        if target is None:
            unresolved_sink.append(href)
            return f"#unresolved-{href_path}"
        anchor_id = ""
        if anchor:
            bm = bookmarks.get(target.source, {})
            anchor_id = bm.get(anchor) or _slug(anchor)
        return relative_md_link(source_md_path, target.target, anchor_id)

    return _PLACEHOLDER_RE.sub(_replace, md)


def _slug(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text or "").strip().lower()
    return re.sub(r"[\s_]+", "-", text) or "section"


def postprocess(
    result: ConversionResult,
    source_md_path: Path,
    path_map: Dict[Path, PathMap],
    bookmarks: Dict[Path, Dict[str, str]],
) -> ConversionResult:
    """Apply all post-processing passes and return an updated result."""
    md = result.markdown
    md = rewrite_fodt_links(
        md, source_md_path, path_map, bookmarks, result.unresolved_links
    )
    md = normalise_code_fences(md)
    md = collapse_blank_lines(md)
    return ConversionResult(
        markdown=md,
        title=result.title,
        bookmarks=result.bookmarks,
        images=result.images,
        unresolved_links=result.unresolved_links,
        fodt_links=result.fodt_links,
    )
