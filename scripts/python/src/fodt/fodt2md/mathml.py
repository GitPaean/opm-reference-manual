"""Convert a small but useful subset of MathML to LaTeX.

The OPM manual embeds MathML inside ``draw:object/math:math`` elements.
This module renders the common operators, identifiers, fractions, roots,
sub/superscripts and matrices used in the manual to LaTeX. Anything we don't
recognise falls back to the StarMath ``<annotation>`` text or the raw text
content so we never lose information.
"""

from __future__ import annotations

from typing import Optional

from lxml import etree

from .constants import NS

_MATH_NS = NS["math"]


def _local(el: etree._Element) -> str:
    tag = el.tag
    if isinstance(tag, str) and tag.startswith("{"):
        return tag.split("}", 1)[1]
    return str(tag)


# Operator map for common Unicode → LaTeX replacements found in the manual.
_OP_MAP = {
    "×": r"\times",
    "·": r"\cdot",
    "−": r"-",
    "≤": r"\leq",
    "≥": r"\geq",
    "≠": r"\neq",
    "≈": r"\approx",
    "→": r"\rightarrow",
    "∞": r"\infty",
    "∑": r"\sum",
    "∏": r"\prod",
    "∫": r"\int",
    "√": r"\sqrt",
    "α": r"\alpha",
    "β": r"\beta",
    "γ": r"\gamma",
    "δ": r"\delta",
    "ε": r"\varepsilon",
    "θ": r"\theta",
    "λ": r"\lambda",
    "μ": r"\mu",
    "π": r"\pi",
    "ρ": r"\rho",
    "σ": r"\sigma",
    "τ": r"\tau",
    "φ": r"\varphi",
    "ω": r"\omega",
    "Δ": r"\Delta",
    "Ω": r"\Omega",
    "Σ": r"\Sigma",
}

_LATEX_ESCAPE = str.maketrans(
    {"#": r"\#", "$": r"\$", "%": r"\%", "&": r"\&", "_": r"\_"}
)


def _esc(text: str) -> str:
    return (text or "").translate(_LATEX_ESCAPE)


def _render(el: etree._Element) -> str:
    tag = _local(el)
    text = (el.text or "").strip()
    if tag == "math":
        return "".join(_render(c) for c in el)
    if tag == "semantics":
        # Strip annotation children and render just the presentation MathML.
        out = []
        for c in el:
            if _local(c) == "annotation":
                continue
            out.append(_render(c))
        return "".join(out)
    if tag in {"mrow", "mstyle", "mpadded", "mphantom"}:
        return "".join(_render(c) for c in el)
    if tag == "mi":
        if not text:
            return ""
        if el.get("mathvariant") == "italic":
            return f"\\mathit{{{_esc(text)}}}"
        if len(text) == 1 and text.isalpha():
            return text
        return f"\\mathrm{{{_esc(text)}}}"
    if tag == "mn":
        return _esc(text)
    if tag == "mo":
        return " " + _OP_MAP.get(text, _esc(text)) + " " if text else ""
    if tag == "mtext":
        return f"\\text{{{_esc(text)}}}"
    if tag == "mspace":
        return r"\,"
    if tag == "msub" and len(el) >= 2:
        return f"{{{_render(el[0])}}}_{{{_render(el[1])}}}"
    if tag == "msup" and len(el) >= 2:
        return f"{{{_render(el[0])}}}^{{{_render(el[1])}}}"
    if tag == "msubsup" and len(el) >= 3:
        return f"{{{_render(el[0])}}}_{{{_render(el[1])}}}^{{{_render(el[2])}}}"
    if tag == "mfrac" and len(el) >= 2:
        return f"\\frac{{{_render(el[0])}}}{{{_render(el[1])}}}"
    if tag == "msqrt":
        return f"\\sqrt{{{''.join(_render(c) for c in el)}}}"
    if tag == "mroot" and len(el) >= 2:
        return f"\\sqrt[{_render(el[1])}]{{{_render(el[0])}}}"
    if tag == "mfenced":
        opener = el.get("open", "(")
        closer = el.get("close", ")")
        sep = el.get("separators", ",")
        sep0 = sep[0] if sep else ","
        inner = sep0.join(_render(c) for c in el)
        return f"{opener}{inner}{closer}"
    if tag == "mtable":
        rows = []
        for row in el:
            if _local(row) != "mtr":
                continue
            cells = [
                _render(cell) for cell in row if _local(cell) == "mtd"
            ]
            rows.append(" & ".join(cells))
        body = " \\\\ ".join(rows)
        return f"\\begin{{matrix}} {body} \\end{{matrix}}"
    if tag == "annotation":
        return ""  # ignore StarMath fallback
    # Generic fallback: concatenate children + own text.
    return _esc(text) + "".join(_render(c) for c in el)


def mathml_to_latex(math_el: etree._Element) -> str:
    """Convert a MathML element tree to a LaTeX string (no ``$`` delimiters).

    Falls back to the StarMath 5.0 ``<annotation>`` text (verbatim) if the
    presentation MathML produces an empty result.
    """
    rendered = _render(math_el).strip()
    if rendered:
        return rendered
    # Fallback: look for StarMath annotation.
    for ann in math_el.iter(f"{{{_MATH_NS}}}annotation"):
        if (ann.text or "").strip():
            return f"\\text{{{_esc(ann.text.strip())}}}"
    return ""


def is_display_math(math_el: etree._Element) -> bool:
    """True if the MathML element should render as a display equation."""
    return (math_el.get("display") or "").lower() == "block"


def latex_for_math(math_el: etree._Element) -> Optional[str]:
    """Return LaTeX with ``$..$`` or ``$$..$$`` delimiters (or ``None``)."""
    body = mathml_to_latex(math_el)
    if not body:
        return None
    return f"$$ {body} $$" if is_display_math(math_el) else f"${body}$"
