"""regwatch output renderers.

Render one synthesized document model into the delivery formats the project
owner asked for: a Word document (.docx), an email newsletter (HTML plus a
plain-text alternative), and a web posting (markdown with front matter). Pure
standard library: a .docx is a zip of WordprocessingML parts, built directly.

The document model is a plain dict so synthesis and rendering stay decoupled:

    {
      "title": str,
      "subtitle": str | None,
      "generated": "YYYY-MM-DD",
      "sections": [
        {"heading": str, "level": 2 | 3, "paragraphs": [str], "bullets": [str]}
      ],
      "disclaimer": str,
    }
"""

from __future__ import annotations

import html
import pathlib
import zipfile


def _xml_escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# --- markdown and web posting ----------------------------------------------


def render_markdown(doc: dict) -> str:
    lines = [f"# {doc['title']}", ""]
    if doc.get("subtitle"):
        lines += [f"_{doc['subtitle']}_", ""]
    lines += [f"Generated {doc['generated']}.", ""]
    for section in doc["sections"]:
        lines.append("#" * section.get("level", 2) + f" {section['heading']}")
        lines.append("")
        for paragraph in section.get("paragraphs", []):
            lines += [paragraph, ""]
        for bullet in section.get("bullets", []):
            lines.append(f"- {bullet}")
        if section.get("bullets"):
            lines.append("")
    lines += ["---", "", f"> {doc['disclaimer']}", ""]
    return "\n".join(lines).rstrip() + "\n"


def render_webpost(doc: dict, tags: list[str]) -> str:
    front = [
        "---",
        f"title: {doc['title']}",
        f"date: {doc['generated']}",
        f"summary: {doc.get('subtitle', '')}",
        "tags:",
    ]
    front += [f"  - {tag}" for tag in tags]
    front += ["draft: true", "---", ""]
    return "\n".join(front) + render_markdown(doc)


# --- email newsletter ------------------------------------------------------


def render_newsletter_text(doc: dict) -> str:
    lines = [doc["title"]]
    if doc.get("subtitle"):
        lines.append(doc["subtitle"])
    lines += [f"Generated {doc['generated']}.", ""]
    for section in doc["sections"]:
        lines += [section["heading"].upper(), ""]
        for paragraph in section.get("paragraphs", []):
            lines += [paragraph, ""]
        for bullet in section.get("bullets", []):
            lines.append(f"  * {bullet}")
        if section.get("bullets"):
            lines.append("")
    lines += ["--", doc["disclaimer"]]
    return "\n".join(lines).rstrip() + "\n"


def render_newsletter_html(doc: dict, subject: str) -> str:
    body = [
        "<!doctype html>",
        '<html><head><meta charset="utf-8">',
        f"<title>{html.escape(subject)}</title></head>",
        '<body style="margin:0;padding:0;background:#f4f4f4;">',
        '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f4;">',
        '<tr><td align="center" style="padding:24px 12px;">',
        '<table role="presentation" width="640" cellpadding="0" cellspacing="0" '
        'style="background:#ffffff;font-family:Helvetica,Arial,sans-serif;color:#1a1a1a;">',
        '<tr><td style="padding:28px 32px 8px 32px;">',
        f'<h1 style="margin:0;font-size:22px;line-height:1.3;">{html.escape(doc["title"])}</h1>',
    ]
    if doc.get("subtitle"):
        body.append(
            f'<p style="margin:6px 0 0 0;color:#555;font-size:14px;">{html.escape(doc["subtitle"])}</p>'
        )
    body.append(
        f'<p style="margin:6px 0 0 0;color:#888;font-size:12px;">Generated {html.escape(doc["generated"])}.</p>'
    )
    body.append("</td></tr>")
    for section in doc["sections"]:
        body.append('<tr><td style="padding:16px 32px 0 32px;">')
        body.append(
            f'<h2 style="margin:0 0 8px 0;font-size:16px;border-bottom:1px solid #eee;'
            f'padding-bottom:4px;">{html.escape(section["heading"])}</h2>'
        )
        for paragraph in section.get("paragraphs", []):
            body.append(
                f'<p style="margin:0 0 10px 0;font-size:14px;line-height:1.5;">{html.escape(paragraph)}</p>'
            )
        if section.get("bullets"):
            body.append('<ul style="margin:0 0 10px 0;padding-left:20px;font-size:14px;line-height:1.5;">')
            for bullet in section["bullets"]:
                body.append(f"<li>{html.escape(bullet)}</li>")
            body.append("</ul>")
        body.append("</td></tr>")
    body += [
        '<tr><td style="padding:16px 32px 28px 32px;">',
        f'<p style="margin:0;color:#888;font-size:11px;line-height:1.4;border-top:1px solid #eee;'
        f'padding-top:12px;">{html.escape(doc["disclaimer"])}</p>',
        "</td></tr>",
        "</table></td></tr></table></body></html>",
    ]
    return "\n".join(body) + "\n"


# --- docx ------------------------------------------------------------------

_CONTENT_TYPES = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/word/document.xml" '
    'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
    "</Types>"
)

_ROOT_RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" '
    'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
    'Target="word/document.xml"/>'
    "</Relationships>"
)

_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def _para(text: str, *, bold: bool = False, size: int | None = None, bullet: bool = False) -> str:
    runs = ""
    rpr = ""
    if bold:
        rpr += "<w:b/>"
    if size is not None:
        rpr += f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
    rpr = f"<w:rPr>{rpr}</w:rPr>" if rpr else ""
    prefix = "•  " if bullet else ""
    runs = f'<w:r>{rpr}<w:t xml:space="preserve">{_xml_escape(prefix + text)}</w:t></w:r>'
    spacing = '<w:spacing w:after="120"/>'
    return f"<w:p><w:pPr>{spacing}</w:pPr>{runs}</w:p>"


def render_document_xml(doc: dict) -> str:
    parts = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        f'<w:document xmlns:w="{_W}"><w:body>',
        _para(doc["title"], bold=True, size=36),
    ]
    if doc.get("subtitle"):
        parts.append(_para(doc["subtitle"], size=22))
    parts.append(_para(f"Generated {doc['generated']}.", size=18))
    for section in doc["sections"]:
        heading_size = 28 if section.get("level", 2) <= 2 else 24
        parts.append(_para(section["heading"], bold=True, size=heading_size))
        for paragraph in section.get("paragraphs", []):
            parts.append(_para(paragraph))
        for bullet in section.get("bullets", []):
            parts.append(_para(bullet, bullet=True))
    parts.append(_para(doc["disclaimer"], size=16))
    parts.append('<w:sectPr/></w:body></w:document>')
    return "".join(parts)


def write_docx(path: str, doc: dict) -> None:
    document_xml = render_document_xml(doc)
    target = pathlib.Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", _CONTENT_TYPES)
        archive.writestr("_rels/.rels", _ROOT_RELS)
        archive.writestr("word/document.xml", document_xml)
