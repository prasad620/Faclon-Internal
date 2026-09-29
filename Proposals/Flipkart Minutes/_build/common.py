"""Shared composite widgets for the proposal slides."""
from dml import *

FOOTER = "DG Online Monitoring Proposal  ·  Flipkart Minutes"


def card(ids, name, x, y, w, h, fill=WHITE, line=N300, radius=0.08, line_w=0.75, dash=None, alpha=None):
    return rect(ids, name, x, y, w, h, fill=fill, line=line, radius=radius, line_w=line_w, dash=dash, alpha=alpha)


def item_stack(ids, x, y, w, items, icon_color=AZURE, size=7.0, gap=0.08, icon_size=0.14, color=BODY,
               lead_color=HEADING, icon_gap=0.07, lnspc=None, bullet=None):
    """Vertical list of (icon_name, text) rows. text may be str, or list of runs, or ('lead', 'rest')
    which renders the lead in semibold. Returns (xml list, total height)."""
    out, cy = [], y
    tx = x + icon_size + icon_gap if icon_size else x
    tw = w - (icon_size + icon_gap if icon_size else 0)
    for it in items:
        icn, content = it[0], it[1]
        if isinstance(content, tuple):
            runs = [run(content[0], FONT_BODY_SB, size, lead_color), run(content[1], FONT_BODY, size, color)]
        elif isinstance(content, str):
            runs = [run(content, FONT_BODY, size, color)]
        else:
            runs = content
        p = para(runs, lnspc=lnspc or size * 1.2)
        h = para_height(p, tw)
        row = []
        if icn and icon_size:
            row.append(icon(ids, icn, x, cy + 0.01, icon_size, icon_color))
        row.append(textbox(ids, "Item text", tx, cy, tw, h, [p]))
        out.append(group(ids, "Item", row, x, cy, w, h))
        cy += h + gap
    return out, cy - y - gap


def bullets(ids, x, y, w, items, size=7.0, color=BODY, lead_color=HEADING, gap=0.03, bullet_color=AZURE, lnspc=None):
    """Bulleted paragraphs in one text box. items: str | (lead, rest). Returns (xml, height)."""
    paras = []
    for it in items:
        if isinstance(it, tuple):
            runs = [run(it[0], FONT_BODY_SB, size, lead_color), run(it[1], FONT_BODY, size, color)]
        else:
            runs = [run(it, FONT_BODY, size, color)]
        paras.append(para(runs, lnspc=lnspc or size * 1.22, spc_before=gap * 72, bullet="•", bullet_color=bullet_color))
    paras[0]["spc_before"] = 0
    h = sum(para_height(p, w) for p in paras)
    return textbox(ids, "Bullets", x, y, w, h, paras), h


def titled_card(ids, name, x, y, w, title, sub=None, icon_name=None, fill=WHITE, line=N300, title_color=HEADING,
                sub_color=MUTED, icon_color=AZURE, chips=None, chip_tone="neutral", pad=0.11, h=None, dark=False,
                title_size=7.2, sub_size=6.3, chip_h=0.15, chip_size=5.8, min_h=0.0, radius=0.08, icon_size=0.16):
    """Card with icon + title (+ sub) and optional chip row; height computed unless given."""
    inner_x = x + pad
    tx = inner_x + (icon_size + 0.09 if icon_name else 0)
    tw = w - pad * 2 - (icon_size + 0.09 if icon_name else 0)
    cy = y + pad
    parts = []
    tp = para(run(title, FONT_BODY_SB, title_size, title_color), lnspc=title_size * 1.15)
    th = para_height(tp, tw)
    body_paras = [tp]
    if sub:
        sp = para(run(sub, FONT_BODY, sub_size, sub_color), lnspc=sub_size * 1.22, spc_before=1.5)
        th += para_height(sp, tw)
        body_paras.append(sp)
    if icon_name:
        parts.append(icon(ids, icon_name, inner_x, cy + 0.005, icon_size, icon_color))
    parts.append(textbox(ids, f"{name} title", tx, cy, tw, th, body_paras))
    cy += th
    if chips:
        cy += 0.08
        cx, ch = chips_row(ids, inner_x, cy, chips, chip_tone, max_w=w - pad * 2, h=chip_h, size=chip_size)
        parts += cx
        cy += ch
    total = max(min_h, cy - y + pad)
    if h is not None:
        total = h
    bg = card(ids, name, x, y, w, total, fill=fill, line=line, radius=radius)
    return group(ids, name, [bg] + parts, x, y, w, total), total


def step_card(ids, name, x, y, w, title, desc, icon_name, dark=False, pad=0.10, title_size=7.2, desc_size=6.4,
              chips=None, chip_tone="neutral", h=None, min_h=0.0, icon_color=None, desc_runs=None):
    """White (or dark) step tile: icon top-left, bold title, small description. Returns (xml, height)."""
    fill, line_c = (DARK_2, "2A3B4F") if dark else (WHITE, N300)
    tcol, dcol = (WHITE, "B1C1D2") if dark else (HEADING, SECOND)
    icol = icon_color or (AZURE_300 if dark else AZURE)
    inner_x = x + pad
    tx = inner_x + 0.24
    tw = w - pad * 2 - 0.24
    cy = y + pad
    parts = [icon(ids, icon_name, inner_x, cy + 0.005, 0.15, icol)]
    tp = para(run(title, FONT_BODY_SB, title_size, tcol), lnspc=title_size * 1.15)
    th = para_height(tp, tw)
    parts.append(textbox(ids, f"{name} title", tx, cy, tw, th, [tp]))
    cy += th + 0.035
    dw = w - pad * 2
    if desc or desc_runs:
        if desc_runs:
            dparas = desc_runs
        else:
            dparas = [para(run(d, FONT_BODY, desc_size, dcol), lnspc=desc_size * 1.24) for d in desc.split("\n")]
        dh = sum(para_height(p, dw) for p in dparas)
        parts.append(textbox(ids, f"{name} desc", inner_x, cy, dw, dh, dparas))
        cy += dh
    if chips:
        cy += 0.07
        cx, ch = chips_row(ids, inner_x, cy, chips, chip_tone, max_w=dw)
        parts += cx
        cy += ch
    total = max(min_h, cy - y + pad)
    if h is not None:
        total = h
    bg = card(ids, name, x, y, w, total, fill=fill, line=line_c, radius=0.07)
    return group(ids, name, [bg] + parts, x, y, w, total), total


def band(ids, x, y, w, h, title, sub, tiles, icon_name="shield-check", tile_desc_size=6.2):
    """Bottom 'built-in rules' band: title block on the left + n tiles with vertical dividers."""
    parts = [card(ids, "Band", x, y, w, h, fill=WHITE, line=N300, radius=0.08)]
    lx = x + 0.13
    parts.append(icon(ids, icon_name, lx, y + 0.11, 0.19, AZURE))
    parts.append(textbox(ids, "Band title", lx, y + 0.35, 1.05, h - 0.4,
                         [para(run(title, FONT_BODY_SB, 7, HEADING), lnspc=8.4),
                          para(run(sub, FONT_BODY, 6.2, MUTED), lnspc=7.4, spc_before=1)]))
    tx = x + 1.25
    tw = (w - 1.25 - 0.10) / len(tiles)
    for i, t in enumerate(tiles):
        cx = tx + i * tw
        if i > 0:
            parts.append(line(ids, "Divider", cx - 0.06, y + 0.14, cx - 0.06, y + h - 0.14, color=N200, w=0.5))
        icn, ttl, desc = t[0], t[1], t[2]
        chip_lbl = t[3] if len(t) > 3 else None
        parts.append(icon(ids, icn, cx, y + 0.13, 0.13, AZURE))
        ttp = para(run(ttl, FONT_BODY_SB, 6.6, HEADING), lnspc=7.6)
        tth = para_height(ttp, tw - 0.30)
        parts.append(textbox(ids, "Tile title", cx + 0.19, y + 0.11, tw - 0.30, tth, [ttp]))
        dp = para(run(desc, FONT_BODY, tile_desc_size, SECOND), lnspc=tile_desc_size * 1.24)
        dh = para_height(dp, tw - 0.16)
        dy = y + 0.11 + tth + 0.04
        parts.append(textbox(ids, "Tile description", cx, dy, tw - 0.16, dh, [dp]))
        if chip_lbl:
            cxml, _ = chip(ids, cx, dy + dh + 0.05, chip_lbl, "cider")
            parts.append(cxml)
    return group(ids, "Band", parts, x, y, w, h)


def zone_label(ids, x, y, label, icon_name, color=AZURE, w=2.6):
    parts = [icon(ids, icon_name, x, y, 0.14, color),
             textbox(ids, "Zone label", x + 0.20, y - 0.01, w, 0.16,
                     [para(run(label, FONT_BODY_SB, 6.6, color, spc=82, caps=True), lnspc=6.6)], anchor="ctr")]
    return group(ids, "Zone " + label, parts, x, y, w + 0.2, 0.16)


def status_chip(ids, x, y, status):
    tone = {"TBC": "cider", "Defined": "emerald", "Optional": "azure", "Cadence TBC": "cider"}.get(status, "cider")
    icn = {"TBC": "circle-help", "Defined": "circle-check", "Optional": "circle-dot"}.get(status, "circle-help")
    return chip(ids, x, y, status, tone, icon_name=icn)


def flow_pills(ids, x, y, labels, w_total, h=0.17, size=5.8, gap_arrow=0.13, tone_fill=AZURE_050, tone_line=AZURE_200,
               tone_text=AZURE_700, last_tone=("EBFAF3", EMERALD_200, EMERALD_700)):
    """Status flow: pills joined by small chevrons. Font shrinks (min 4.8pt) until everything fits w_total."""
    while True:
        widths = [text_width(l, FONT_BODY_SB, size) + 0.13 for l in labels]
        total = sum(widths) + gap_arrow * (len(labels) - 1)
        if total <= w_total or size <= 4.8:
            break
        size -= 0.2
    out = []
    cx = x
    for i, (l, w) in enumerate(zip(labels, widths)):
        fill, ln, tc = (last_tone if i == len(labels) - 1 else (tone_fill, tone_line, tone_text))
        out.append(rect(ids, "Pill", cx, y, w, h, fill=fill, line=ln, line_w=0.5, radius=h * 0.2))
        out.append(textbox(ids, "Pill label", cx, y, w, h, [para(run(l, FONT_BODY_SB, size, tc), align="ctr", lnspc=size)],
                           anchor="ctr", wrap=False))
        cx += w
        if i < len(labels) - 1:
            out.append(icon(ids, "chevron-right", cx + (gap_arrow - 0.10) / 2, y + (h - 0.10) / 2, 0.10, TERT))
            cx += gap_arrow
    return out
