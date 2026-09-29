"""Minimal DrawingML emitter for the Faclon proposal decks.

All geometry is in inches; text sizes in points. Text widths/heights are measured with the
real Inter / TASA Orbiter TTFs so wrapping and box heights are computed, not guessed.
"""
import html
import json
import os
import re
import uuid
from functools import lru_cache

from PIL import ImageFont

EMU = 914400
HERE = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ palette (DS4 marketing)
AZURE, AZURE_600, AZURE_700 = "165FF2", "124ED0", "0E3FAA"
AZURE_050, AZURE_100, AZURE_200, AZURE_300, AZURE_400 = "F4F8FF", "DCE8FE", "B8D0FD", "8AB1FB", "5A8DF7"
HEADING, BODY, SECOND, MUTED, TERT, N600 = "0C1927", "243547", "40566D", "6C849D", "90A5BB", "768EA7"
WHITE, N050, N100, N200, N300, N400 = "FFFFFF", "F8FAFC", "F1F5FA", "E3EAF3", "CBD5E2", "B1C1D2"
EMERALD, EMERALD_700, EMERALD_050, EMERALD_100, EMERALD_200 = "00A251", "008743", "EBFAF3", "DAF5E8", "B6ECD1"
CRIMSON, CRIMSON_700, CRIMSON_050, CRIMSON_100 = "D92D20", "B42318", "FFF5F5", "FEE4E2"
CIDER, CIDER_700, CIDER_050 = "E9690C", "C65C10", "FFF7F0"
DARK, DARK_2, DARK_LINE = "0C1927", "192839", "40566D"

FONT_BODY = "Inter"
FONT_BODY_SB = "Inter SemiBold"
FONT_HEAD = "TASA Orbiter SemiBold"

_FONT_FILES = {
    FONT_BODY: "Inter-Regular.ttf",
    FONT_BODY_SB: "Inter-SemiBold.ttf",
    FONT_HEAD: "TASAOrbiter-SemiBold.ttf",
}
_FONT_DIRS = [os.path.expanduser("~/.local/share/fonts/faclon"),
              os.path.join(HERE, "..", "..", "Welspun", "Fonts")]


def _font_path(name):
    for d in _FONT_DIRS:
        p = os.path.join(d, _FONT_FILES[name])
        if os.path.exists(p):
            return p
    raise FileNotFoundError(name)


@lru_cache(maxsize=None)
def _pil_font(name, size_pt):
    # render at 10× for measurement precision
    return ImageFont.truetype(_font_path(name), int(round(size_pt * 10)))


def text_width(text, font=FONT_BODY, size=7.0, spc=0):
    """Width in inches of a single line (spc = character spacing in 1/100 pt)."""
    if not text:
        return 0.0
    f = _pil_font(font, size)
    w = f.getlength(text) / 10.0  # in points
    w += len(text) * spc / 100.0
    return w / 72.0


def wrap_text(text, width_in, font=FONT_BODY, size=7.0, spc=0):
    """Greedy word wrap → list of lines. Honors explicit \n."""
    lines = []
    for para in text.split("\n"):
        words = para.split(" ")
        cur = ""
        for w in words:
            cand = w if not cur else cur + " " + w
            if text_width(cand, font, size, spc) <= width_in or not cur:
                cur = cand
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def emu(v):
    return int(round(v * EMU))


def esc(s):
    return html.escape(str(s), quote=False)


# ------------------------------------------------------------------ id allocation
class Ids:
    def __init__(self):
        self.n = 1

    def next(self):
        self.n += 1
        return self.n


# ------------------------------------------------------------------ text
def run(text, font=FONT_BODY, size=7.0, color=BODY, spc=0, caps=False, bold=False, italic=False):
    return dict(text=text, font=font, size=size, color=color, spc=spc, caps=caps, bold=bold, italic=italic)


def _run_xml(r):
    attrs = f'lang="en-US" sz="{int(round(r["size"] * 100))}" b="{1 if r.get("bold") else 0}" i="{1 if r.get("italic") else 0}"'
    if r.get("caps"):
        attrs += ' cap="all"'
    attrs += f' spc="{int(r.get("spc", 0))}" dirty="0"'
    f = r["font"]
    return (f'<a:r><a:rPr {attrs}><a:solidFill><a:srgbClr val="{r["color"]}"/></a:solidFill>'
            f'<a:latin typeface="{f}"/><a:ea typeface="{f}"/><a:cs typeface="{f}"/><a:sym typeface="{f}"/></a:rPr>'
            f'<a:t>{esc(r["text"])}</a:t></a:r>')


def para(runs, align="l", lnspc=None, spc_before=0, bullet=None, bullet_color=AZURE, indent=0.11):
    """runs: str | run dict | list of run dicts. lnspc in points (exact)."""
    if isinstance(runs, (str, dict)):
        runs = [runs]
    runs = [run(r) if isinstance(r, str) else r for r in runs]
    return dict(runs=runs, align=align, lnspc=lnspc, spc_before=spc_before, bullet=bullet,
                bullet_color=bullet_color, indent=indent)


def _para_xml(p, default_lnspc_factor=1.2):
    size = max(r["size"] for r in p["runs"]) if p["runs"] else 7
    lnspc = p["lnspc"] or size * default_lnspc_factor
    ppr = f'<a:pPr algn="{p["align"]}"'
    if p.get("bullet"):
        ppr += f' marL="{emu(p["indent"])}" indent="-{emu(p["indent"])}"'
    ppr += '>'
    ppr += f'<a:lnSpc><a:spcPts val="{int(round(lnspc * 100))}"/></a:lnSpc>'
    ppr += f'<a:spcBef><a:spcPts val="{int(round(p["spc_before"] * 100))}"/></a:spcBef>'
    if p.get("bullet"):
        ppr += (f'<a:buClr><a:srgbClr val="{p["bullet_color"]}"/></a:buClr><a:buSzPct val="100000"/>'
                f'<a:buFont typeface="Arial"/><a:buChar char="{esc(p["bullet"])}"/>')
    else:
        ppr += '<a:buNone/>'
    ppr += '</a:pPr>'
    f = p["runs"][0]["font"] if p["runs"] else FONT_BODY
    end = f'<a:endParaRPr lang="en-US" sz="{int(round(size * 100))}" dirty="0"><a:latin typeface="{f}"/></a:endParaRPr>'
    return '<a:p>' + ppr + ''.join(_run_xml(r) for r in p["runs"]) + end + '</a:p>'


def para_height(p, width_in, default_lnspc_factor=1.2):
    """Height in inches this paragraph needs when wrapped into width_in."""
    size = max(r["size"] for r in p["runs"])
    lnspc = p["lnspc"] or size * default_lnspc_factor
    # measure by concatenating runs with their own fonts — approximate with the widest font weight
    text = "".join(r["text"] for r in p["runs"])
    font = p["runs"][0]["font"]
    spc = p["runs"][0].get("spc", 0)
    for r in p["runs"]:
        if r["font"] == FONT_BODY_SB:
            font = FONT_BODY_SB
    avail = width_in - (p["indent"] if p.get("bullet") else 0)
    n = len(wrap_text(text, avail, font, size, spc))
    return (n * lnspc + p["spc_before"]) / 72.0


def textbox(ids, name, x, y, w, h, paras, anchor="t", wrap=True, lnspc_factor=1.2, align=None):
    if isinstance(paras, (str, dict, list)) and not (isinstance(paras, list) and paras and isinstance(paras[0], dict) and "runs" in paras[0]):
        paras = [para(paras, align=align or "l")]
    body = ''.join(_para_xml(p, lnspc_factor) for p in paras)
    return (f'<p:sp><p:nvSpPr><p:cNvPr id="{ids.next()}" name="{esc(name)}"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(w)}" cy="{emu(h)}"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/><a:ln><a:noFill/></a:ln></p:spPr>'
            f'<p:txBody><a:bodyPr wrap="{"square" if wrap else "none"}" lIns="0" tIns="0" rIns="0" bIns="0" anchor="{anchor}" rtlCol="0"><a:noAutofit/></a:bodyPr>'
            f'<a:lstStyle/>{body}</p:txBody></p:sp>')


def text(ids, name, x, y, w, h, content, font=FONT_BODY, size=7.0, color=BODY, align="l", anchor="t",
         spc=0, caps=False, lnspc=None, wrap=True, bold=False, italic=False):
    """Simple single-style text box. content may be str (\\n → paragraphs)."""
    paras = [para(run(line, font, size, color, spc, caps, bold, italic), align=align, lnspc=lnspc) for line in str(content).split("\n")]
    return textbox(ids, name, x, y, w, h, paras, anchor=anchor, wrap=wrap)


# ------------------------------------------------------------------ shapes
def _fill_xml(fill, alpha=None):
    if fill is None:
        return '<a:noFill/>'
    a = f'<a:alpha val="{int(alpha * 1000)}"/>' if alpha is not None else ''
    return f'<a:solidFill><a:srgbClr val="{fill}">{a}</a:srgbClr></a:solidFill>'


def _line_xml(line, line_w=0.75, dash=None, head=None, tail=None, cap=None):
    if line is None:
        return '<a:ln><a:noFill/></a:ln>'
    capa = f' cap="{cap}"' if cap else ''
    s = f'<a:ln w="{int(round(line_w * 12700))}"{capa}><a:solidFill><a:srgbClr val="{line}"/></a:solidFill>'
    if dash:
        s += f'<a:prstDash val="{dash}"/>'
    s += '<a:round/>'
    if head:
        s += f'<a:headEnd type="{head}" w="med" len="med"/>'
    if tail:
        s += f'<a:tailEnd type="{tail}" w="med" len="med"/>'
    return s + '</a:ln>'


def rect(ids, name, x, y, w, h, fill=WHITE, line=None, line_w=0.75, radius=None, alpha=None, dash=None, shadow=False):
    if radius:
        adj = int(round(min(50000, radius / min(w, h) * 100000)))
        geom = f'<a:prstGeom prst="roundRect"><a:avLst><a:gd name="adj" fmla="val {adj}"/></a:avLst></a:prstGeom>'
    else:
        geom = '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>'
    eff = ('<a:effectLst><a:outerShdw blurRad="152400" dist="19050" dir="5400000" algn="t" rotWithShape="0">'
           '<a:srgbClr val="192839"><a:alpha val="9000"/></a:srgbClr></a:outerShdw></a:effectLst>') if shadow else ''
    return (f'<p:sp><p:nvSpPr><p:cNvPr id="{ids.next()}" name="{esc(name)}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(w)}" cy="{emu(h)}"/></a:xfrm>'
            f'{geom}{_fill_xml(fill, alpha)}{_line_xml(line, line_w, dash)}{eff}</p:spPr>'
            f'<p:txBody><a:bodyPr rtlCol="0" anchor="ctr"/><a:lstStyle/><a:p><a:pPr algn="ctr"/><a:endParaRPr lang="en-US" sz="700"/></a:p></p:txBody></p:sp>')


def ellipse(ids, name, x, y, w, h, fill=AZURE, line=None, line_w=0.75):
    return (f'<p:sp><p:nvSpPr><p:cNvPr id="{ids.next()}" name="{esc(name)}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(w)}" cy="{emu(h)}"/></a:xfrm>'
            f'<a:prstGeom prst="ellipse"><a:avLst/></a:prstGeom>{_fill_xml(fill)}{_line_xml(line, line_w)}</p:spPr>'
            f'<p:txBody><a:bodyPr rtlCol="0" anchor="ctr"/><a:lstStyle/><a:p><a:pPr algn="ctr"/><a:endParaRPr lang="en-US" sz="700"/></a:p></p:txBody></p:sp>')


def line(ids, name, x1, y1, x2, y2, color=N200, w=0.75, dash=None, head=None, tail=None):
    """Straight connector. Supports any direction via flipH/flipV."""
    x, y = min(x1, x2), min(y1, y2)
    cx, cy = abs(x2 - x1), abs(y2 - y1)
    flip = ''
    if x2 < x1:
        flip += ' flipH="1"'
    if y2 < y1:
        flip += ' flipV="1"'
    return (f'<p:cxnSp><p:nvCxnSpPr><p:cNvPr id="{ids.next()}" name="{esc(name)}"/><p:cNvCxnSpPr/><p:nvPr/></p:nvCxnSpPr>'
            f'<p:spPr><a:xfrm{flip}><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(cx)}" cy="{emu(cy)}"/></a:xfrm>'
            f'<a:prstGeom prst="straightConnector1"><a:avLst/></a:prstGeom><a:noFill/>{_line_xml(color, w, dash, head, tail)}</p:spPr></p:cxnSp>')


def elbow(ids, name, x1, y1, x2, y2, color=N300, w=0.75, dash=None, tail="triangle", via="h"):
    """Two-segment orthogonal connector: horizontal then vertical (via='h') or vertical then horizontal (via='v')."""
    if via == "h":
        mid = (x2, y1)
    else:
        mid = (x1, y2)
    return (line(ids, name + " a", x1, y1, mid[0], mid[1], color, w, dash) +
            line(ids, name + " b", mid[0], mid[1], x2, y2, color, w, dash, tail=tail))


_ICONS = None


def _icons():
    global _ICONS
    if _ICONS is None:
        _ICONS = json.load(open(os.path.join(HERE, "icons.json")))
    return _ICONS


def icon(ids, name, x, y, size, color=AZURE, stroke=None):
    """Lucide icon as native custom geometry. stroke = line width in pt (default scales with size)."""
    pathlst = _icons()[name]
    lw = stroke if stroke is not None else max(0.5, size * 72 * 2.2 / 24)  # ≈2.2/24 of the icon size, in pt
    return (f'<p:sp><p:nvSpPr><p:cNvPr id="{ids.next()}" name="Icon {esc(name)}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(size)}" cy="{emu(size)}"/></a:xfrm>'
            f'<a:custGeom><a:avLst/><a:gdLst/><a:ahLst/><a:cxnLst/><a:rect l="l" t="t" r="r" b="b"/>{pathlst}</a:custGeom>'
            f'<a:noFill/><a:ln w="{int(round(lw * 12700))}" cap="rnd"><a:solidFill><a:srgbClr val="{color}"/></a:solidFill><a:round/></a:ln></p:spPr></p:sp>')


def group(ids, name, children, x, y, w, h):
    return (f'<p:grpSp><p:nvGrpSpPr><p:cNvPr id="{ids.next()}" name="{esc(name)}"/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>'
            f'<p:grpSpPr><a:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(w)}" cy="{emu(h)}"/>'
            f'<a:chOff x="{emu(x)}" y="{emu(y)}"/><a:chExt cx="{emu(w)}" cy="{emu(h)}"/></a:xfrm></p:grpSpPr>'
            + ''.join(children) + '</p:grpSp>')


# ------------------------------------------------------------------ composite widgets
def chip(ids, x, y, label, tone="neutral", icon_name=None, size=5.8, h=0.15, solid=False, font=FONT_BODY_SB, pad=0.045):
    """Small pill. tone: neutral | azure | emerald | crimson | cider | dark | white | outline.
    Returns (xml, width)."""
    tones = {
        "neutral": (N100, SECOND, None, None),
        "neutral2": (N200, BODY, None, None),
        "azure": (AZURE, AZURE_700, 9, None),
        "azure-solid": (AZURE, WHITE, None, None),
        "emerald": (EMERALD, EMERALD_700, 9, None),
        "emerald-solid": (EMERALD, WHITE, None, None),
        "crimson": (CRIMSON, CRIMSON_700, 9, None),
        "cider": (CIDER, CIDER_700, 9, None),
        "cider-solid": (CIDER, WHITE, None, None),
        "dark": (DARK, WHITE, None, None),
        "dark-ghost": (WHITE, WHITE, 12, None),
        "dark-ghost2": (WHITE, "CBD5E2", 10, None),
        "white": (WHITE, BODY, None, N300),
        "outline": (None, SECOND, None, N300),
        "azure-outline": (WHITE, AZURE, None, AZURE_200),
    }
    fill, tc, alpha, border = tones[tone]
    tw = text_width(label, font, size)
    ix = x + pad + 0.02
    icon_w = (h * 0.62 + 0.035) if icon_name else 0
    w = pad * 2 + icon_w + tw + 0.03
    parts = [rect(ids, "Chip fill", x, y, w, h, fill=fill, line=border, line_w=0.5, radius=h * 0.2, alpha=alpha)]
    if icon_name:
        isz = h * 0.62
        parts.append(icon(ids, icon_name, ix, y + (h - isz) / 2, isz, tc))
    parts.append(textbox(ids, "Chip label", x + pad + icon_w + 0.015, y, tw + 0.03, h,
                         [para(run(label, font, size, tc), lnspc=size)], anchor="ctr", wrap=False))
    return group(ids, f"Chip {label}", parts, x, y, w, h), w


def chips_row(ids, x, y, labels, tone="neutral", max_w=None, gap=0.05, h=0.15, size=5.8, icon_names=None, vgap=0.04):
    """Lay chips left→right, wrapping to a new row when max_w is exceeded. Returns (xml_list, height_used)."""
    out, cx, cy, rowh = [], x, y, 0
    for i, lab in enumerate(labels):
        icn = icon_names[i] if icon_names else None
        xml, w = chip(ids, cx, cy, lab, tone, icn, size=size, h=h)
        if max_w and cx + w > x + max_w + 1e-6 and cx > x:
            cy += h + vgap
            cx = x
            xml, w = chip(ids, cx, cy, lab, tone, icn, size=size, h=h)
        out.append(xml)
        cx += w + gap
    return out, (cy - y) + h


def number_badge(ids, x, y, num, size=0.21, fill=AZURE, color=WHITE, font_size=7.5, square=True):
    parts = [rect(ids, "Badge", x, y, size, size, fill=fill, radius=size * 0.22) if square
             else ellipse(ids, "Badge", x, y, size, size, fill=fill)]
    parts.append(textbox(ids, "Badge number", x, y, size, size,
                         [para(run(str(num), FONT_HEAD, font_size, color), align="ctr", lnspc=font_size)], anchor="ctr"))
    return group(ids, f"Badge {num}", parts, x, y, size, size)


def header(ids, eyebrow, title, subtitle, badge=None, badge_fill=AZURE):
    """Slide header: eyebrow (optionally with a numbered badge), title, subtitle and the Faclon logo."""
    parts = []
    ex = 0.30
    if badge is not None:
        parts.append(number_badge(ids, 0.30, 0.25, badge, size=0.21, fill=badge_fill))
        ex = 0.58
    parts.append(textbox(ids, "Eyebrow", ex, 0.25, 6.2, 0.21,
                         [para(run(eyebrow, FONT_BODY_SB, 7, AZURE, spc=98, caps=True), lnspc=7)], anchor="ctr"))
    parts.append(textbox(ids, "Title", 0.30, 0.49, 7.9, 0.34,
                         [para(run(title, FONT_HEAD, 18, HEADING), lnspc=20.16)], anchor="t"))
    parts.append(textbox(ids, "Subtitle", 0.30, 0.84, 8.6, 0.19,
                         [para(run(subtitle, FONT_BODY, 8.5, SECOND), lnspc=10.2)], anchor="t"))
    logo = open(os.path.join(HERE, "faclon_logo.xml"), encoding="utf-8").read()
    logo = re.sub(r'\s+xmlns:[A-Za-z0-9]+="[^"]*"', '', logo)
    parts.append(logo)
    return group(ids, "Header", parts, 0.30, 0.24, 9.46, 0.79)


def footer(ids, text_left):
    parts = [textbox(ids, "Footer text", 0.30, 5.33, 5.0, 0.15,
                     [para(run(text_left, FONT_BODY, 6.5, TERT), lnspc=6.5)], anchor="ctr")]
    fld = (f'<p:sp><p:nvSpPr><p:cNvPr id="{ids.next()}" name="Slide number"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>'
           f'<p:spPr><a:xfrm><a:off x="{emu(9.10)}" y="{emu(5.33)}"/><a:ext cx="{emu(0.60)}" cy="{emu(0.15)}"/></a:xfrm>'
           f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/><a:ln><a:noFill/></a:ln></p:spPr>'
           f'<p:txBody><a:bodyPr wrap="square" lIns="0" tIns="0" rIns="0" bIns="0" anchor="ctr" rtlCol="0"><a:noAutofit/></a:bodyPr><a:lstStyle/>'
           f'<a:p><a:pPr algn="r"><a:buNone/></a:pPr><a:fld id="{{{str(uuid.uuid4()).upper()}}}" type="slidenum">'
           f'<a:rPr lang="en-US" sz="700" dirty="0"><a:solidFill><a:srgbClr val="{TERT}"/></a:solidFill>'
           f'<a:latin typeface="Inter"/><a:ea typeface="Inter"/><a:cs typeface="Inter"/><a:sym typeface="Inter"/></a:rPr>'
           f'<a:t>&#8249;#&#8250;</a:t></a:fld><a:endParaRPr lang="en-US" sz="700" dirty="0"/></a:p></p:txBody></p:sp>')
    parts.append(fld)
    return group(ids, "Footer", parts, 0.30, 5.33, 9.40, 0.15)


def stage_label(ids, x, y, digit, name, color=AZURE):
    parts = [number_badge(ids, x, y, digit, size=0.17, fill=color, font_size=6.5, square=False),
             textbox(ids, "Stage name", x + 0.23, y - 0.005, 2.0, 0.18,
                     [para(run(name, FONT_BODY_SB, 6.8, color, spc=82, caps=True), lnspc=6.8)], anchor="ctr")]
    return group(ids, f"Stage {digit}", parts, x, y, 2.23, 0.18)


# ------------------------------------------------------------------ table (native)
def table(ids, name, x, y, col_widths, rows, row_heights, styles):
    """rows: list of list of cell dicts {paras:[...], fill:..., } ; styles: dict for borders."""
    gf = (f'<p:graphicFrame><p:nvGraphicFramePr><p:cNvPr id="{ids.next()}" name="{esc(name)}"/><p:cNvGraphicFramePr><a:graphicFrameLocks noGrp="1"/></p:cNvGraphicFramePr><p:nvPr/></p:nvGraphicFramePr>'
          f'<p:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(sum(col_widths))}" cy="{emu(sum(row_heights))}"/></p:xfrm>'
          f'<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/table"><a:tbl><a:tblPr/><a:tblGrid>')
    gf += ''.join(f'<a:gridCol w="{emu(w)}"/>' for w in col_widths) + '</a:tblGrid>'
    for ri, row in enumerate(rows):
        gf += f'<a:tr h="{emu(row_heights[ri])}">'
        for ci, cell in enumerate(row):
            paras = cell["paras"]
            body = ''.join(_para_xml(p) for p in paras)
            fill = cell.get("fill")
            border = cell.get("border_bottom", styles.get("border", N200))
            bw = cell.get("border_w", 0.5)
            lnB = (f'<a:lnB w="{int(bw * 12700)}"><a:solidFill><a:srgbClr val="{border}"/></a:solidFill></a:lnB>'
                   if border else '<a:lnB><a:noFill/></a:lnB>')
            tc = (f'<a:tc><a:txBody><a:bodyPr/><a:lstStyle/>{body}</a:txBody>'
                  f'<a:tcPr marL="{emu(cell.get("padl", 0.08))}" marR="{emu(0.06)}" marT="{emu(0.05)}" marB="{emu(0.05)}" anchor="{cell.get("anchor", "ctr")}">'
                  f'<a:lnL><a:noFill/></a:lnL><a:lnR><a:noFill/></a:lnR><a:lnT><a:noFill/></a:lnT>{lnB}'
                  + (f'<a:solidFill><a:srgbClr val="{fill}"/></a:solidFill>' if fill else '<a:noFill/>') + '</a:tcPr></a:tc>')
            gf += tc
        gf += '</a:tr>'
    gf += '</a:tbl></a:graphicData></a:graphic></p:graphicFrame>'
    return gf


# ------------------------------------------------------------------ slide wrapper
SLIDE_NS = ('xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
            'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"')


def slide_xml(shapes, notes=None):
    x = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
         f'<p:sld {SLIDE_NS}><p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>'
         '<p:grpSpPr/>' + ''.join(shapes) + '</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>')
    # Re-number all cNvPr ids sequentially and uniquely (the logo group carries its own ids).
    counter = [1]

    def renum(m):
        counter[0] += 1
        return f'<p:cNvPr id="{counter[0]}"'

    return re.sub(r'<p:cNvPr id="\d+"', renum, x)


def slide_rels_xml(layout="../slideLayouts/slideLayout23.xml"):
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            f'<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="{layout}"/>'
            '</Relationships>')
