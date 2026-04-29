"""Resolve ODF style inheritance for the FODT → Markdown converter.

ODF paragraph and text styles inherit text properties through
``style:parent-style-name``. The converter needs a flat view of "is this
style monospaced / bold / italic / a code paragraph?" so it can decide
whether a sequence of ``text:p`` elements should be grouped into a fenced
code block or whether a ``text:span`` should be wrapped in ``**...**``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Optional

from lxml import etree

from .constants import CODE_STYLE_NAMES, NS, q


@dataclass
class StyleProps:
    """Flattened text/paragraph properties for a single ODF style."""

    name: str
    family: str = ""
    parent: Optional[str] = None
    font_name: Optional[str] = None
    font_weight: Optional[str] = None
    font_style: Optional[str] = None
    font_family_generic: Optional[str] = None
    color: Optional[str] = None
    is_code_style: bool = False  # set after inheritance resolution
    text_position: Optional[str] = None  # super/sub
    raw_props: Dict[str, str] = field(default_factory=dict)


class StyleMap:
    """Lookup table for ODF styles in a single FODT file.

    Resolves inheritance lazily; queries return the flattened
    :class:`StyleProps` for a style name. Unknown names return a default
    record so callers never need to handle ``None``.
    """

    def __init__(self) -> None:
        self._styles: Dict[str, StyleProps] = {}
        self._resolved: Dict[str, StyleProps] = {}

    @classmethod
    def from_root(cls, root: etree._Element) -> "StyleMap":
        """Build a :class:`StyleMap` from a parsed FODT document root."""
        sm = cls()
        for container_tag in ("styles", "automatic-styles"):
            container = root.find(q("office", container_tag))
            if container is None:
                continue
            for style_el in container.findall(q("style", "style")):
                sm._add(style_el)
        return sm

    def _add(self, el: etree._Element) -> None:
        name = el.get(q("style", "name"))
        if not name:
            return
        props = StyleProps(
            name=name,
            family=el.get(q("style", "family"), ""),
            parent=el.get(q("style", "parent-style-name")),
        )
        text_props = el.find(q("style", "text-properties"))
        if text_props is not None:
            props.font_name = text_props.get(q("style", "font-name"))
            props.font_weight = text_props.get(q("fo", "font-weight"))
            props.font_style = text_props.get(q("fo", "font-style"))
            props.font_family_generic = text_props.get(
                q("style", "font-family-generic")
            )
            props.color = text_props.get(q("fo", "color"))
            props.text_position = text_props.get(q("style", "text-position"))
        self._styles[name] = props

    # ------------------------------------------------------------------
    # Lookup
    # ------------------------------------------------------------------
    def get(self, name: Optional[str]) -> StyleProps:
        """Return resolved properties for ``name`` (default record if unknown)."""
        if not name:
            return StyleProps(name="")
        if name in self._resolved:
            return self._resolved[name]
        props = self._resolve(name, set())
        self._resolved[name] = props
        return props

    def _resolve(self, name: str, seen: set) -> StyleProps:
        if name in seen or name not in self._styles:
            return StyleProps(name=name)
        seen.add(name)
        own = self._styles[name]
        if own.parent:
            parent = self._resolve(own.parent, seen)
            merged = StyleProps(
                name=own.name,
                family=own.family or parent.family,
                parent=own.parent,
                font_name=own.font_name or parent.font_name,
                font_weight=own.font_weight or parent.font_weight,
                font_style=own.font_style or parent.font_style,
                font_family_generic=(
                    own.font_family_generic or parent.font_family_generic
                ),
                color=own.color or parent.color,
                text_position=own.text_position or parent.text_position,
            )
        else:
            merged = own
        # Walk the parent chain to detect explicit "code" style names.
        chain = []
        cur: Optional[str] = name
        guard = 0
        while cur and guard < 32:
            chain.append(cur)
            cur = self._styles.get(cur, StyleProps(name="")).parent
            guard += 1
        merged.is_code_style = bool(set(chain) & CODE_STYLE_NAMES) or (
            (merged.font_family_generic or "").lower() == "modern"
        )
        return merged

    # Convenience helpers used by the visitor.
    def is_code_paragraph(self, name: Optional[str]) -> bool:
        return self.get(name).is_code_style and self.get(name).family != "text"

    def is_bold(self, name: Optional[str]) -> bool:
        w = (self.get(name).font_weight or "").lower()
        return w in {"bold", "700", "800", "900"}

    def is_italic(self, name: Optional[str]) -> bool:
        return (self.get(name).font_style or "").lower() == "italic"

    def is_monospace(self, name: Optional[str]) -> bool:
        sp = self.get(name)
        return sp.is_code_style or (
            (sp.font_family_generic or "").lower() == "modern"
        )

    def is_superscript(self, name: Optional[str]) -> bool:
        return "super" in (self.get(name).text_position or "").lower()

    def is_subscript(self, name: Optional[str]) -> bool:
        return "sub" in (self.get(name).text_position or "").lower()
