"""Constants used by the FODT → Markdown converter."""

# OpenDocument XML namespaces. Keep keys short; values are the URIs used in
# the FODT files produced by LibreOffice.
NS = {
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    "table": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
    "draw": "urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
    "style": "urn:oasis:names:tc:opendocument:xmlns:style:1.0",
    "fo": "urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0",
    "svg": "urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0",
    "xlink": "http://www.w3.org/1999/xlink",
    "dc": "http://purl.org/dc/elements/1.1/",
    "math": "http://www.w3.org/1998/Math/MathML",
    "loext": "urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0",
}


def q(prefix: str, local: str) -> str:
    """Return the Clark-notation qualified name ``{ns}local``."""
    return "{%s}%s" % (NS[prefix], local)


# Paragraph styles in the OPM manual whose name (or ancestor name) marks the
# content as a verbatim Eclipse DATA / monospace example. Resolved via the
# style inheritance chain. ``@Example`` is the source-of-truth name in
# LibreOffice, serialized as ``_40_Example``.
CODE_STYLE_NAMES = {
    "_40_Example",
    "@Example",
    "Preformatted_20_Text",
    "Preformatted Text",
}

# Internal-link target prefix used by ``text:bookmark-ref`` style hrefs in
# the manual. Stripped before lookup in the bookmark map.
BOOKMARK_HREF_PREFIX = "#"

# Output language tag for fenced Eclipse DATA blocks.
ECLIPSE_FENCE_LANG = "eclipse"
