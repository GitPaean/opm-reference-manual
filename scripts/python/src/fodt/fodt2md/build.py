"""Orchestrator: convert all FODT files in a tree to Markdown in parallel.

The orchestrator first walks ``parts/`` to build a ``{fodt_path: PathMap}``
table, then runs :class:`FodtConverter` over each file in a process pool.
Because the post-processor needs every file's bookmark table to rewrite
cross-document links, conversion happens in two stages:

1. Workers parse each FODT file and emit a :class:`ConversionResult` with
   ``fodt2md:`` placeholders for cross-document links.
2. The main process gathers all bookmarks and rewrites placeholders.

This keeps the workers stateless (no shared bookmark dict) and means a full
rebuild of the manual scales linearly with the number of CPUs available.
"""

from __future__ import annotations

import json
import os
import pickle
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional

from .converter import ConversionResult, FodtConverter
from .paths import PathMap, build_path_map
from .postprocess import postprocess


@dataclass
class BuildSummary:
    """High-level result of converting an entire FODT tree."""

    converted: int
    unchanged: int
    failed: int
    unresolved_links: int
    output_root: Path
    failures: List[str]


def find_fodt_files(parts_root: Path) -> List[Path]:
    """Return all ``.fodt`` files under ``parts_root`` sorted deterministically."""
    return sorted(p.resolve() for p in parts_root.rglob("*.fodt"))


def _convert_one(args: tuple[str, str]) -> tuple[str, bytes, Optional[str]]:
    """Worker: parse one FODT file and return a pickled :class:`ConversionResult`."""
    src_str, parts_str = args
    try:
        result = FodtConverter(Path(src_str), Path(parts_str)).convert()
        return (src_str, pickle.dumps(result), None)
    except Exception as exc:  # pragma: no cover - reported via summary
        return (src_str, b"", f"{type(exc).__name__}: {exc}")


def convert_tree(
    parts_root: Path,
    docs_root: Path,
    sources: Optional[Iterable[Path]] = None,
    workers: Optional[int] = None,
    write: bool = True,
    check: bool = False,
) -> BuildSummary:
    """Convert every FODT file under ``parts_root`` to Markdown under ``docs_root``.

    Parameters
    ----------
    sources:
        Optional explicit subset of FODT files to convert; if ``None``, all
        ``.fodt`` files under ``parts_root`` are converted.
    workers:
        Process pool size. Defaults to ``os.cpu_count()``.
    write:
        If False, run the conversion entirely in memory and return without
        writing any files. Useful for ``--check``.
    check:
        If True, compare each generated file against any committed version
        on disk and treat differences as failures (without writing).
    """
    parts_root = parts_root.resolve()
    docs_root = docs_root.resolve()
    src_list = list(sources) if sources is not None else find_fodt_files(parts_root)
    path_map = build_path_map(src_list, parts_root, docs_root)

    workers = workers or os.cpu_count() or 1
    bookmarks_by_source: Dict[Path, Dict[str, str]] = {}
    raw_results: Dict[Path, ConversionResult] = {}
    failures: List[str] = []

    if workers > 1 and len(src_list) > 1:
        with ProcessPoolExecutor(max_workers=workers) as ex:
            futures = [
                ex.submit(_convert_one, (str(p), str(parts_root))) for p in src_list
            ]
            for fut in as_completed(futures):
                src_str, blob, err = fut.result()
                if err:
                    failures.append(f"{src_str}: {err}")
                    continue
                src = Path(src_str)
                result: ConversionResult = pickle.loads(blob)
                raw_results[src] = result
                bookmarks_by_source[src] = result.bookmarks
    else:
        for src in src_list:
            try:
                result = FodtConverter(src, parts_root).convert()
                raw_results[src] = result
                bookmarks_by_source[src] = result.bookmarks
            except Exception as exc:  # pragma: no cover
                failures.append(f"{src}: {type(exc).__name__}: {exc}")

    converted = unchanged = unresolved = 0
    images_root = docs_root / "_images"
    if write:
        images_root.mkdir(parents=True, exist_ok=True)

    for src, result in raw_results.items():
        pm = path_map[src]
        final = postprocess(result, pm.target, path_map, bookmarks_by_source)
        unresolved += len(final.unresolved_links)
        existing: Optional[str] = None
        if pm.target.exists():
            try:
                existing = pm.target.read_text(encoding="utf-8")
            except OSError:
                existing = None
        if check:
            if existing != final.markdown:
                failures.append(f"check: {pm.target} differs from generated output")
            continue
        if existing == final.markdown:
            unchanged += 1
        else:
            converted += 1
            if write:
                pm.target.parent.mkdir(parents=True, exist_ok=True)
                pm.target.write_text(final.markdown, encoding="utf-8")
        if write:
            for filename, data in final.images.items():
                target = images_root / filename
                if not target.exists() or target.read_bytes() != data:
                    target.write_bytes(data)

    if write:
        report = {
            "converted": converted,
            "unchanged": unchanged,
            "failed": len(failures),
            "unresolved_links": unresolved,
            "failures": failures,
        }
        (docs_root / "links_report.json").write_text(
            json.dumps(report, indent=2, sort_keys=True), encoding="utf-8"
        )

    return BuildSummary(
        converted=converted,
        unchanged=unchanged,
        failed=len(failures),
        unresolved_links=unresolved,
        output_root=docs_root,
        failures=failures,
    )
