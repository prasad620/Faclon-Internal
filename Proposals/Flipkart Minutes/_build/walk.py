"""Storyboard scaffolding shared by the two workflow walk-through slides.

Three columns, larger frames, a short caption under each. No timestamps strip and no
notification bubble — the slide has to read from the back of a room.
"""
from dml import *
from common import *
from ui import *

COLS = [(0.30, 2.92), (3.54, 2.92), (6.78, 2.92)]
FRAME_Y, FRAME_H = 1.42, 3.02
CAPTION_Y = FRAME_Y + FRAME_H + 0.12


def step_header(ids, col, num, title, role, role_icon="circle-user"):
    x, w = COLS[col]
    y = 1.10
    parts = [number_badge(ids, x, y, num, size=0.21, fill=AZURE, font_size=7, square=False),
             textbox(ids, "Step title", x + 0.28, y - 0.01, w - 1.05, 0.23,
                     [para(run(title, FONT_BODY_SB, 8.0, HEADING), lnspc=8.6)], anchor="ctr")]
    rc, rw = chip(ids, 0, 0, role, "neutral", icon_name=role_icon, h=0.16, size=5.8)
    rc, rw = chip(ids, x + w - rw, y + 0.03, role, "neutral", icon_name=role_icon, h=0.16, size=5.8)
    parts.append(rc)
    return parts


def caption(ids, col, lead, text, size=7.0, y=None):
    x, w = COLS[col]
    p = para([run(lead + " ", FONT_BODY_SB, size, HEADING), run(text, FONT_BODY, size, BODY)], lnspc=size * 1.25)
    h = para_height(p, w)
    return textbox(ids, "Caption", x, CAPTION_Y if y is None else y, w, h, [p]), h


def arrows(ids, fy=None, fh=None):
    fy = FRAME_Y if fy is None else fy
    fh = FRAME_H if fh is None else fh
    out = []
    for i in range(len(COLS) - 1):
        x0, w0 = COLS[i]
        x1, _ = COLS[i + 1]
        gx = (x0 + w0 + x1) / 2 - 0.09
        out.append(icon(ids, "chevron-right", gx, fy + fh / 2 - 0.09, 0.18, N400))
    return out


def sample_chip(ids):
    xml, w = chip(ids, 0, 0, "Sample data  ·  illustrative values", "cider", icon_name="info", h=0.15, size=5.6)
    xml, w = chip(ids, 9.70 - w, 0.845, "Sample data  ·  illustrative values", "cider", icon_name="info", h=0.15, size=5.6)
    return xml
