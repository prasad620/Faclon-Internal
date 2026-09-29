"""Build the Flipkart Minutes proposal deck.

usage: python3 build.py [--only 4,5] [--out path.pptx]
Slides 1-3 always come from the Welspun deck (re-titled cover); the rest are generated.
"""
import argparse
import importlib
import os
import subprocess
import sys

from PIL import Image

import package as pk
from dml import slide_rels_xml

HERE = os.path.dirname(os.path.abspath(__file__))
PROPOSAL_DIR = os.path.abspath(os.path.join(HERE, ".."))
SCRATCH = "/tmp/claude-1000/-home-ubuntu-workspace-e30acb92-4904-436d-bd9f-e319a4e74263/1ce9ab6a-de15-4fc8-ba21-5e329c9177b7/scratchpad"
OUT_NAME = "DG Online Monitoring, Refilling & Maintenance - Techno-Commercial Proposal.pptx"

SLIDES = [  # (module, description)
    ("s4_objective", "Objective & Business Outcome"),
    ("s5_arch_refill", "Solution Architecture · Workflow 01"),
    ("s5b_walk_refill", "Workflow Walk-through · Workflow 01"),
    ("s5c_walk_billing", "Invoicing Walk-through · Billing & Fusion"),
    ("s6_arch_maint", "Solution Architecture · Workflow 02"),
    ("s6b_walk_maint", "Workflow Walk-through · Workflow 02"),
    ("s7_network", "Network Architecture"),
    ("s8_scope", "Scope of Work"),
    ("s9_deliverables", "Software Deliverables"),
    ("s10_milestones", "Implementation Milestones"),
    ("s11_schedule", "Project Delivery Schedule"),
    ("s12_commercials", "Commercials"),
    ("s13_open_points", "Open Points to Confirm"),
]

COVER = dict(client="Flipkart Minutes", title="DG Online Monitoring, Refilling & Maintenance", date="Date: 19th Sep, 2026")


def make_logo():
    """Flipkart mark taken from the Key Customers slide (the DS4 SVG is corrupted)."""
    src = os.path.join(SCRATCH, "welspun_unpacked", "ppt", "media", "image85.png")
    im = Image.open(src).convert("RGBA")
    im = im.crop(im.getbbox())
    out = os.path.join(HERE, "flipkart_logo.png")
    im.save(out)
    return out, im.width / im.height


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None, help="comma list of slide numbers (4..16) to build")
    ap.add_argument("--out", default=None)
    ap.add_argument("--no-render", action="store_true")
    a = ap.parse_args()
    only = [int(s) for s in a.only.split(",")] if a.only else None
    out = a.out or os.path.join(PROPOSAL_DIR, OUT_NAME)
    work = os.path.join(SCRATCH, "deck_work")

    pk.unpack(work)
    pk.drop_slides(work, keep=3)
    logo, ratio = make_logo()
    # Welspun logo frame was at (0.50, 3.70) 2.61×0.73 in; keep the top-left, use the mark's height
    h = 0.78
    pk.retitle_cover(work, COVER["client"], COVER["title"], COVER["date"], logo_png=logo, logo_box=(0.50, 3.67, h * ratio, h))

    xmls = []
    for i, (mod, desc) in enumerate(SLIDES):
        n = i + 4
        if only and n not in only:
            continue
        m = importlib.import_module(mod)
        xmls.append(m.build())
        print(f"built slide {n}: {desc}")
    pk.add_slides(work, xmls, slide_rels_xml())
    pk.pack(work, out)
    print("wrote", out)
    if not a.no_render:
        imgs = pk.render(out, os.path.join(SCRATCH, "render"))
        print("\n".join(imgs))


if __name__ == "__main__":
    main()
