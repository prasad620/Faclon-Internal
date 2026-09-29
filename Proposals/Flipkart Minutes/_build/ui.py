"""Mock IOsense product UI, drawn as native shapes.

Colours come from the design-sdk / Figma token export (light theme): brand azure-500 #305EFF,
bluegray neutrals, emerald / crimson / cider / sapphire feedback ramps, 4 / 8 / 12 px radii.
The product font is Noto Sans; the deck renders it in Inter so nothing substitutes on other
machines.
"""
from dml import *
from icons import parse_path

# ------------------------------------------------------------------ product palette
P_BRAND, P_BRAND_300, P_BRAND_SUB = "305EFF", "75A3FF", "ECF0FF"
P_TXT, P_TXT2, P_TXT3, P_TXT4 = "192839", "40566D", "768EA7", "90A5BB"
P_BG, P_BG2, P_LINE, P_LINE2 = "F8FAFC", "F1F5FA", "E3EAF3", "CBD5E2"
P_POS, P_POS7, P_POS_SUB = "00A251", "008743", "EBFAF3"
P_NEG, P_NEG7, P_NEG_SUB, P_NEG2 = "D92D20", "B42318", "FFF5F5", "FEC6C3"
P_NOT, P_NOT7, P_NOT_SUB = "E9690C", "C65C10", "FFF3EB"
P_INF, P_INF7, P_INF_SUB = "1291D0", "0F78AD", "E7F6FE"
IOS_MARK = "342DFB"
WA_GREEN, WA_SUB = "25D366", "EAF9F0"

TONES = {  # tone → (subtle bg, subtle text, intense bg)
    "positive": (P_POS_SUB, P_POS7, P_POS), "negative": (P_NEG_SUB, P_NEG7, P_NEG),
    "notice": (P_NOT_SUB, P_NOT7, P_NOT), "information": (P_INF_SUB, P_INF7, P_INF),
    "neutral": (P_BG2, P_TXT2, P_TXT2), "primary": (P_BRAND_SUB, P_BRAND, P_BRAND),
}


def ptext(ids, x, y, w, h, text, size=5.6, color=P_TXT, sb=False, align="l", anchor="t", wrap=True, lnspc=None, name="UI text"):
    f = FONT_BODY_SB if sb else FONT_BODY
    paras = [para(run(t, f, size, color), align=align, lnspc=lnspc or size * 1.2) for t in str(text).split("\n")]
    return textbox(ids, name, x, y, w, h, paras, anchor=anchor, wrap=wrap)


def prich(ids, x, y, w, h, runs, size=5.6, align="l", anchor="t", lnspc=None):
    """runs: list of (text, bold, color)."""
    rs = [run(t, FONT_BODY_SB if b else FONT_BODY, size, c or P_TXT) for t, b, c in runs]
    return textbox(ids, "UI text", x, y, w, h, [para(rs, align=align, lnspc=lnspc or size * 1.2)], anchor=anchor)


def badge(ids, x, y, label, tone="positive", intense=False, size=4.6, h=0.13, icon_name=None, name="Badge"):
    bg, tc, ibg = TONES[tone]
    fill, col = (ibg, WHITE) if intense else (bg, tc)
    tw = text_width(label, FONT_BODY_SB, size)
    iw = (h * 0.6 + 0.03) if icon_name else 0
    w = 0.10 + iw + tw
    parts = [rect(ids, name, x, y, w, h, fill=fill, radius=h * 0.25)]
    if icon_name:
        parts.append(icon(ids, icon_name, x + 0.05, y + h * 0.2, h * 0.6, col))
    parts.append(textbox(ids, "Badge label", x + 0.05 + iw, y, tw + 0.02, h,
                         [para(run(label, FONT_BODY_SB, size, col), lnspc=size)], anchor="ctr", wrap=False))
    return group(ids, name, parts, x, y, w, h), w


def button(ids, x, y, w, label, variant="primary", size=5.0, h=0.19, icon_name=None, tone="primary"):
    if variant == "primary":
        fill, ln, col = (TONES[tone][2], None, WHITE)
    elif variant == "secondary":
        fill, ln, col = (WHITE, P_LINE2, P_TXT)
    else:  # tertiary / ghost
        fill, ln, col = (None, None, P_BRAND)
    parts = [rect(ids, "Button", x, y, w, h, fill=fill, line=ln, line_w=0.5, radius=0.03)]
    tw = text_width(label, FONT_BODY_SB, size)
    iw = (0.11 + 0.04) if icon_name else 0
    sx = x + (w - tw - iw) / 2
    if icon_name:
        parts.append(icon(ids, icon_name, sx, y + (h - 0.11) / 2, 0.11, col))
    parts.append(textbox(ids, "Button label", sx + iw, y, tw + 0.04, h, [para(run(label, FONT_BODY_SB, size, col), lnspc=size)],
                         anchor="ctr", wrap=False))
    return group(ids, "Button " + label, parts, x, y, w, h)


def ui_card(ids, x, y, w, h, fill=WHITE, line_c=P_LINE, radius=0.06, name="Card"):
    return rect(ids, name, x, y, w, h, fill=fill, line=line_c, line_w=0.5, radius=radius)


def divider(ids, x, y, w, color=P_LINE):
    return line(ids, "Divider", x, y, x + w, y, color=color, w=0.5)


def input_field(ids, x, y, w, label, value, icon_name=None, h=0.19, required=False, placeholder=False, lines=1):
    """Label above a bordered box. Returns (xml list, total height)."""
    parts = []
    lab = label + (" *" if required else "")
    parts.append(ptext(ids, x, y, w, 0.11, lab, size=4.4, color=P_TXT2, sb=True, lnspc=4.6))
    by = y + 0.12
    bh = h if lines == 1 else h + 0.09 * (lines - 1)
    parts.append(rect(ids, "Input", x, by, w, bh, fill=WHITE, line=P_LINE2, line_w=0.5, radius=0.03))
    parts.append(ptext(ids, x + 0.06, by, w - 0.12 - (0.16 if icon_name else 0), bh, value, size=5.0,
                       color=P_TXT4 if placeholder else P_TXT, anchor="ctr" if lines == 1 else "t", lnspc=5.6))
    if icon_name:
        parts.append(icon(ids, icon_name, x + w - 0.17, by + (bh - 0.11) / 2, 0.11, P_TXT3))
    return parts, 0.12 + bh


def toggle(ids, x, y, on=True, w=0.22, h=0.12):
    parts = [rect(ids, "Toggle", x, y, w, h, fill=P_BRAND if on else P_LINE2, radius=h / 2)]
    kx = x + w - h + 0.015 if on else x + 0.015
    parts.append(ellipse(ids, "Knob", kx, y + 0.015, h - 0.03, h - 0.03, fill=WHITE))
    return group(ids, "Toggle", parts, x, y, w, h)


def radio(ids, x, y, label, selected=False, size=4.9):
    d = 0.11
    parts = [ellipse(ids, "Radio", x, y, d, d, fill=WHITE, line=P_BRAND if selected else P_LINE2, line_w=0.75)]
    if selected:
        parts.append(ellipse(ids, "Radio dot", x + 0.03, y + 0.03, d - 0.06, d - 0.06, fill=P_BRAND))
    lw = text_width(label, FONT_BODY, size) + 0.06
    parts.append(ptext(ids, x + d + 0.05, y - 0.02, lw, d + 0.04, label, size=size, color=P_TXT, anchor="ctr", wrap=False))
    return group(ids, "Radio " + label, parts, x, y, d + 0.05 + lw, d)


def checkrow(ids, x, y, label, size=4.9):
    d = 0.11
    parts = [rect(ids, "Check", x, y, d, d, fill=P_BRAND, radius=0.02), icon(ids, "check", x + 0.02, y + 0.02, d - 0.04, WHITE),
             ptext(ids, x + d + 0.05, y - 0.02, text_width(label, FONT_BODY, size) + 0.06, d + 0.04, label, size=size, color=P_TXT, anchor="ctr", wrap=False)]
    return group(ids, "Check " + label, parts, x, y, d + 0.11 + text_width(label, FONT_BODY, size), d)


def upload_zone(ids, x, y, w, text, attached=None, h=0.30):
    parts = [rect(ids, "Upload zone", x, y, w, h, fill=P_BG, line=P_LINE2, line_w=0.5, radius=0.03, dash="dash")]
    parts.append(icon(ids, "upload", x + 0.08, y + 0.05, 0.11, P_BRAND))
    parts.append(ptext(ids, x + 0.24, y + 0.03, w - 0.3, 0.13, text, size=4.6, color=P_TXT2, anchor="ctr"))
    if attached:
        b, bw = badge(ids, x + 0.24, y + 0.16, attached, "positive", size=4.2, h=0.11, icon_name="paperclip")
        parts.append(b)
    return group(ids, "Upload", parts, x, y, w, h)


def stepper(ids, x, y, w, steps, done, current, size=4.0):
    """Horizontal status stepper: done steps filled brand, current outlined, rest grey."""
    n = len(steps)
    d = 0.11
    seg = (w - d) / (n - 1)
    parts = []
    for i in range(n - 1):
        cx = x + d / 2 + i * seg
        parts.append(line(ids, "Step link", cx + d / 2, y + d / 2, cx + seg - d / 2 + d / 2, y + d / 2,
                          color=P_BRAND if i < done else P_LINE2, w=0.75))
    for i, s in enumerate(steps):
        cx = x + i * seg
        if i < done:
            parts.append(ellipse(ids, "Step", cx, y, d, d, fill=P_BRAND))
            parts.append(icon(ids, "check", cx + 0.025, y + 0.025, d - 0.05, WHITE, stroke=0.6))
        elif i == current:
            parts.append(ellipse(ids, "Step", cx, y, d, d, fill=WHITE, line=P_BRAND, line_w=1.0))
            parts.append(ellipse(ids, "Step dot", cx + 0.035, y + 0.035, d - 0.07, d - 0.07, fill=P_BRAND))
        else:
            parts.append(ellipse(ids, "Step", cx, y, d, d, fill=WHITE, line=P_LINE2, line_w=0.75))
        parts.append(ptext(ids, cx + d / 2 - 0.25, y + d + 0.03, 0.50, 0.10, s, size=size,
                           color=P_TXT if i <= current else P_TXT4, sb=i == current, align="ctr", lnspc=size))
    return group(ids, "Stepper", parts, x, y, w, d + 0.14), d + 0.14


def kpi_tile(ids, x, y, w, h, label, value, unit="", value_color=P_TXT, bar=None, bar_color=P_BRAND, fill=P_BG, line_c=None):
    parts = [rect(ids, "KPI tile", x, y, w, h, fill=fill, line=line_c, line_w=0.5, radius=0.04),
             ptext(ids, x + 0.06, y + 0.04, w - 0.12, 0.10, label, size=4.3, color=P_TXT3, lnspc=4.5),
             prich(ids, x + 0.06, y + 0.14, w - 0.12, 0.16, [(value, True, value_color), (" " + unit, False, P_TXT3)], size=7.2, lnspc=7.6)]
    if bar is not None:
        by = y + h - 0.08
        parts.append(rect(ids, "Bar track", x + 0.06, by, w - 0.12, 0.04, fill=P_LINE, radius=0.02))
        parts.append(rect(ids, "Bar fill", x + 0.06, by, (w - 0.12) * bar, 0.04, fill=bar_color, radius=0.02))
    return group(ids, "KPI " + label, parts, x, y, w, h)


def alert_banner(ids, x, y, w, title, body, tone="negative", icon_name="triangle-alert", size=4.9):
    bg, tc, ibg = TONES[tone]
    tp = para(run(title, FONT_BODY_SB, size, tc), lnspc=size * 1.2)
    bp = para(run(body, FONT_BODY, size - 0.3, P_TXT2), lnspc=(size - 0.3) * 1.2, spc_before=1)
    tw = w - 0.36
    h = para_height(tp, tw) + para_height(bp, tw) + 0.12
    parts = [rect(ids, "Alert", x, y, w, h, fill=bg, line=ibg, line_w=0.5, radius=0.04),
             icon(ids, icon_name, x + 0.08, y + 0.07, 0.13, ibg),
             textbox(ids, "Alert text", x + 0.28, y + 0.06, tw, h - 0.1, [tp, bp])]
    return group(ids, "Alert", parts, x, y, w, h), h


def ui_table(ids, x, y, widths, header, rows, size=4.3, row_h=0.15, badge_col=None, badge_tones=None):
    """Compact data table. rows: list of lists of str. Returns (xml, height)."""
    parts = []
    w = sum(widths)
    parts.append(rect(ids, "Table header", x, y, w, row_h, fill=P_BG2, radius=0.02))
    cx = x
    for i, (hd, cw) in enumerate(zip(header, widths)):
        parts.append(ptext(ids, cx + 0.04, y, cw - 0.06, row_h, hd, size=size - 0.2, color=P_TXT3, sb=True, anchor="ctr", lnspc=size, wrap=False))
        cx += cw
    ry = y + row_h
    for r, row in enumerate(rows):
        cx = x
        for i, (val, cw) in enumerate(zip(row, widths)):
            if badge_col is not None and i == badge_col:
                tone = (badge_tones or {}).get(val, "positive")
                b, bw = badge(ids, cx + 0.04, ry + (row_h - 0.11) / 2, val, tone, size=3.9, h=0.11)
                parts.append(b)
            else:
                parts.append(ptext(ids, cx + 0.04, ry, cw - 0.06, row_h, val, size=size, color=P_TXT if i == 0 else P_TXT2,
                                   sb=i == 0, anchor="ctr", lnspc=size, wrap=False))
            cx += cw
        parts.append(divider(ids, x, ry + row_h, w))
        ry += row_h
    return group(ids, "Table", parts, x, y, w, ry - y), ry - y


def tabs(ids, x, y, w, labels, selected=0, size=4.8):
    parts = [divider(ids, x, y + 0.20, w, color=P_LINE)]
    cx = x
    for i, l in enumerate(labels):
        tw = text_width(l, FONT_BODY_SB, size) + 0.16
        col = P_BRAND if i == selected else P_TXT2
        parts.append(ptext(ids, cx, y, tw, 0.20, l, size=size, color=col, sb=i == selected, align="ctr", anchor="ctr", wrap=False))
        if i == selected:
            parts.append(line(ids, "Tab indicator", cx + 0.04, y + 0.20, cx + tw - 0.04, y + 0.20, color=P_BRAND, w=1.5))
        cx += tw + 0.04
    return group(ids, "Tabs", parts, x, y, w, 0.21), 0.21


def filter_chip(ids, x, y, label, size=4.3, h=0.13):
    tw = text_width(label, FONT_BODY, size) + 0.24
    parts = [rect(ids, "Filter chip", x, y, tw, h, fill=WHITE, line=P_LINE2, line_w=0.5, radius=h / 2),
             ptext(ids, x + 0.06, y, tw - 0.2, h, label, size=size, color=P_TXT2, anchor="ctr", wrap=False),
             icon(ids, "chevron-down", x + tw - 0.14, y + (h - 0.09) / 2, 0.09, P_TXT3)]
    return group(ids, "Filter " + label, parts, x, y, tw, h), tw


# ------------------------------------------------------------------ brand mark
_IOS_MONO = ("M 32.314 72 L 13.9 19.734 L 7.066 40.76 L 18.158 49.111 L 20.136 57.854 L 0 43.308 L 14.489 0 L 32.314 52.543 "
             "L 49.945 0.77 L 64 44.493 L 43.903 58.931 L 46.082 49.503 L 56.771 41.445 L 49.642 20.619 L 32.314 72 Z")


def iosense_mark(ids, x, y, size):
    """IOsense app mark from the brand repository: rounded square + white monogram (182 × 182 viewBox)."""
    subs = parse_path(_IOS_MONO)
    parts = []
    parts.append(rect(ids, "IOsense tile", x, y, size, size, fill=IOS_MARK, radius=size * 15.654 / 182))
    S = 1000
    P = lambda v: str(int(round(v * S)))
    path = '<a:path w="182000" h="182000">'
    for sp in subs:
        for seg in sp:
            if seg[0] == "M":
                path += f'<a:moveTo><a:pt x="{P(seg[1] + 31.889)}" y="{P(seg[2] + 36.445)}"/></a:moveTo>'
            elif seg[0] == "L":
                path += f'<a:lnTo><a:pt x="{P(seg[1] + 31.889)}" y="{P(seg[2] + 36.445)}"/></a:lnTo>'
            elif seg[0] == "Z":
                path += '<a:close/>'
    path += '</a:path>'
    parts.append(f'<p:sp><p:nvSpPr><p:cNvPr id="{ids.next()}" name="IOsense monogram"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
                 f'<p:spPr><a:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(size)}" cy="{emu(size)}"/></a:xfrm>'
                 f'<a:custGeom><a:avLst/><a:gdLst/><a:ahLst/><a:cxnLst/><a:rect l="l" t="t" r="r" b="b"/><a:pathLst>{path}</a:pathLst></a:custGeom>'
                 f'<a:solidFill><a:srgbClr val="{WHITE}"/></a:solidFill><a:ln><a:noFill/></a:ln></p:spPr></p:sp>')
    return group(ids, "IOsense mark", parts, x, y, size, size)


# ------------------------------------------------------------------ device frames
def browser_frame(ids, x, y, w, h, url, section, role_label, role_icon="circle-user"):
    """Browser window + IOsense app bar. Returns (xml list, (cx, cy, cw, ch)) for the page content area."""
    parts = [rect(ids, "Browser", x, y, w, h, fill=WHITE, line=P_LINE2, line_w=0.75, radius=0.07, shadow=True)]
    # window bar
    parts.append(rect(ids, "Window bar", x, y, w, 0.19, fill=P_BG2, radius=0.07))
    parts.append(rect(ids, "Window bar square", x, y + 0.10, w, 0.09, fill=P_BG2))
    for i, c in enumerate(["F96C62", "FFB020", "48D08C"]):
        parts.append(ellipse(ids, "Dot", x + 0.08 + i * 0.09, y + 0.07, 0.05, 0.05, fill=c))
    parts.append(rect(ids, "URL", x + 0.40, y + 0.04, w - 0.5, 0.11, fill=WHITE, radius=0.03))
    parts.append(ptext(ids, x + 0.46, y + 0.04, w - 0.6, 0.11, url, size=4.0, color=P_TXT4, anchor="ctr", wrap=False))
    # app bar
    ay = y + 0.19
    parts.append(rect(ids, "App bar", x, ay, w, 0.24, fill=WHITE))
    parts.append(divider(ids, x, ay + 0.24, w))
    parts.append(iosense_mark(ids, x + 0.08, ay + 0.05, 0.14))
    parts.append(prich(ids, x + 0.26, ay, w - 1.2, 0.24, [("IOsense", True, P_TXT), ("  ·  " + section, False, P_TXT2)], size=5.0, anchor="ctr"))
    rw = text_width(role_label, FONT_BODY, 4.4) + 0.2
    parts.append(icon(ids, role_icon, x + w - rw - 0.08, ay + 0.06, 0.12, P_TXT2))
    parts.append(ptext(ids, x + w - rw + 0.07, ay, rw - 0.07, 0.24, role_label, size=4.4, color=P_TXT2, anchor="ctr", wrap=False))
    # page background
    cy = ay + 0.25
    parts.append(rect(ids, "Page", x + 0.005, cy, w - 0.01, y + h - cy - 0.005, fill=P_BG))
    parts.append(rect(ids, "Page corner", x, y + h - 0.12, w, 0.12, fill=P_BG, radius=0.07))
    parts.append(rect(ids, "Page corner square", x, y + h - 0.12, w, 0.06, fill=P_BG))
    return parts, (x + 0.10, cy + 0.09, w - 0.20, y + h - cy - 0.16)


def phone_frame(ids, x, y, w, h, title, role_label):
    """Phone with status bar and brand app header. Returns (xml list, (cx, cy, cw, ch))."""
    parts = [rect(ids, "Phone", x, y, w, h, fill=P_TXT, radius=0.20, shadow=True),
             rect(ids, "Screen", x + 0.05, y + 0.05, w - 0.10, h - 0.10, fill=P_BG, radius=0.16)]
    sx, sy, sw = x + 0.05, y + 0.05, w - 0.10
    # status bar
    parts.append(ptext(ids, sx + 0.14, sy + 0.04, 0.4, 0.12, "9:41", size=4.6, color=P_TXT, sb=True, anchor="ctr"))
    parts.append(icon(ids, "signal", sx + sw - 0.44, sy + 0.06, 0.09, P_TXT))
    parts.append(icon(ids, "wifi", sx + sw - 0.32, sy + 0.06, 0.09, P_TXT))
    parts.append(icon(ids, "battery-medium", sx + sw - 0.20, sy + 0.06, 0.09, P_TXT))
    # notch
    parts.append(rect(ids, "Notch", x + w / 2 - 0.18, y + 0.05, 0.36, 0.07, fill=P_TXT, radius=0.035))
    # app header
    hy = sy + 0.20
    parts.append(rect(ids, "App header", sx, hy, sw, 0.26, fill=P_BRAND))
    parts.append(iosense_mark(ids, sx + 0.10, hy + 0.06, 0.14))
    parts.append(ptext(ids, sx + 0.29, hy, sw - 0.6, 0.26, title, size=5.4, color=WHITE, sb=True, anchor="ctr", wrap=False))
    parts.append(icon(ids, "circle-user", sx + sw - 0.24, hy + 0.07, 0.12, WHITE))
    # role label under header (small)
    parts.append(ptext(ids, sx + 0.10, hy + 0.28, sw - 0.2, 0.11, role_label, size=4.2, color=P_TXT3, lnspc=4.4))
    # home indicator
    parts.append(rect(ids, "Home indicator", x + w / 2 - 0.20, y + h - 0.10, 0.40, 0.03, fill=P_TXT4, radius=0.015))
    return parts, (sx + 0.09, hy + 0.42, sw - 0.18, y + h - (hy + 0.42) - 0.18)


def notif_bubble(ids, x, y, w, sender, text, channel="WhatsApp", time="10:42"):
    tp = para([run(sender, FONT_BODY_SB, 4.6, P_TXT), run("  ·  " + channel + "  ·  " + time, FONT_BODY, 4.2, P_TXT3)], lnspc=5.2)
    bp = para(run(text, FONT_BODY, 4.7, P_TXT), lnspc=5.6, spc_before=1.5)
    tw = w - 0.36
    h = para_height(tp, tw) + para_height(bp, tw) + 0.14
    parts = [rect(ids, "Bubble", x, y, w, h, fill=WHITE, line=P_LINE2, line_w=0.5, radius=0.06, shadow=True),
             ellipse(ids, "Channel icon bg", x + 0.08, y + 0.08, 0.20, 0.20, fill=WA_SUB),
             icon(ids, "message-circle-more", x + 0.115, y + 0.115, 0.13, "1FA855"),
             textbox(ids, "Bubble text", x + 0.34, y + 0.07, tw, h - 0.1, [tp, bp])]
    return group(ids, "Notification bubble", parts, x, y, w, h), h


def step_arrow(ids, x, y):
    return icon(ids, "chevron-right", x, y, 0.16, TERT)
