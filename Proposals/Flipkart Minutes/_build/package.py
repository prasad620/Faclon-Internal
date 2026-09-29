"""Assemble the Flipkart Minutes deck: Welspun intro slides 1-3 (re-titled) + generated slides."""
import os
import re
import shutil
import subprocess
import sys
import zipfile

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
PROPOSALS = os.path.abspath(os.path.join(HERE, ".."))
WELSPUN_PPTX = os.path.join(PROPOSALS, "..", "Welspun", "SAP Integration - Techno-Commercial Proposal.pptx")
SKILL = "/home/ubuntu/.claude/skills/synced/2b363d32-2fc6-4ef0-b4d8-dd1e675f656b_5974eced-6fd2-4830-9f66-b957a965449f/pptx/scripts"
SLIDE_CT = "application/vnd.openxmlformats-officedocument.presentationml.slide+xml"
REL_SLIDE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide"


def unpack(work):
    if os.path.exists(work):
        shutil.rmtree(work)
    os.makedirs(work)
    zipfile.ZipFile(WELSPUN_PPTX).extractall(work)


def drop_slides(work, keep=3):
    """Remove every slide after `keep` from the presentation, then clean orphaned parts."""
    pres = os.path.join(work, "ppt", "presentation.xml")
    x = open(pres, encoding="utf-8").read()
    ids = re.findall(r'<p:sldId id="\d+" r:id="rId\d+"/>', x)
    for s in ids[keep:]:
        x = x.replace(s, "")
    open(pres, "w", encoding="utf-8").write(x)
    subprocess.run([sys.executable, os.path.join(SKILL, "clean.py"), work], check=True)


def retitle_cover(work, client, title, date, logo_png=None, logo_box=None):
    """Edit slide 1 text and swap the client logo (media/image12.png in the Welspun deck)."""
    p = os.path.join(work, "ppt", "slides", "slide1.xml")
    x = open(p, encoding="utf-8").read()
    import html
    for old, new in [("Welspun Corporation", client),
                     ("SAP Integration for Pipe Testing Stations", title),
                     ("Date: 15th Sep, 2026", date)]:
        assert old in x, old
        x = x.replace(old, html.escape(new, quote=False))
    if logo_png:
        rels = open(os.path.join(work, "ppt", "slides", "_rels", "slide1.xml.rels"), encoding="utf-8").read()
        m = re.search(r'Id="(rId\d+)"[^>]*Target="\.\./media/image12\.png"', rels) or \
            re.search(r'Target="\.\./media/image12\.png"[^>]*Id="(rId\d+)"', rels)
        assert m, "logo rel not found"
        rid = m.group(1)
        shutil.copy(logo_png, os.path.join(work, "ppt", "media", "image12.png"))
        if logo_box:
            # resize the picture frame that references the logo (keep its top-left)
            E = 914400
            bx, by, bw, bh = logo_box
            pat = re.compile(r'(<p:pic>(?:(?!</p:pic>).)*?r:embed="%s"(?:(?!</p:pic>).)*?</p:pic>)' % rid, re.S)
            m2 = pat.search(x)
            assert m2, "pic not found"
            pic = m2.group(1)
            pic2 = re.sub(r'<a:off x="\d+" y="\d+"/><a:ext cx="\d+" cy="\d+"/>',
                          f'<a:off x="{int(bx * E)}" y="{int(by * E)}"/><a:ext cx="{int(bw * E)}" cy="{int(bh * E)}"/>', pic, count=1)
            x = x.replace(pic, pic2)
    open(p, "w", encoding="utf-8").write(x)


def add_slides(work, slides, rels_xml):
    """slides: list of slide XML strings, appended after the existing ones."""
    pres_p = os.path.join(work, "ppt", "presentation.xml")
    rels_p = os.path.join(work, "ppt", "_rels", "presentation.xml.rels")
    ct_p = os.path.join(work, "[Content_Types].xml")
    pres = open(pres_p, encoding="utf-8").read()
    rels = open(rels_p, encoding="utf-8").read()
    ct = open(ct_p, encoding="utf-8").read()
    existing = [int(n) for n in re.findall(r'slides/slide(\d+)\.xml', rels)]
    next_slide = max(existing) + 1
    next_rid = max(int(n) for n in re.findall(r'Id="rId(\d+)"', rels)) + 1
    next_sid = max(int(n) for n in re.findall(r'<p:sldId id="(\d+)"', pres)) + 1
    for xml in slides:
        n = next_slide
        open(os.path.join(work, "ppt", "slides", f"slide{n}.xml"), "w", encoding="utf-8").write(xml)
        open(os.path.join(work, "ppt", "slides", "_rels", f"slide{n}.xml.rels"), "w", encoding="utf-8").write(rels_xml)
        rels = rels.replace("</Relationships>",
                            f'<Relationship Id="rId{next_rid}" Type="{REL_SLIDE}" Target="slides/slide{n}.xml"/></Relationships>')
        ct = ct.replace("</Types>", f'<Override PartName="/ppt/slides/slide{n}.xml" ContentType="{SLIDE_CT}"/></Types>')
        pres = pres.replace("</p:sldIdLst>", f'<p:sldId id="{next_sid}" r:id="rId{next_rid}"/></p:sldIdLst>')
        next_slide += 1
        next_rid += 1
        next_sid += 1
    open(pres_p, "w", encoding="utf-8").write(pres)
    open(rels_p, "w", encoding="utf-8").write(rels)
    open(ct_p, "w", encoding="utf-8").write(ct)


def pack(work, out_pptx):
    if os.path.exists(out_pptx):
        os.remove(out_pptx)
    with zipfile.ZipFile(out_pptx, "w", zipfile.ZIP_DEFLATED) as z:
        # [Content_Types].xml first
        z.write(os.path.join(work, "[Content_Types].xml"), "[Content_Types].xml")
        for root, _, files in os.walk(work):
            for f in files:
                full = os.path.join(root, f)
                arc = os.path.relpath(full, work)
                if arc == "[Content_Types].xml":
                    continue
                z.write(full, arc)


def render(out_pptx, out_dir):
    """PPTX → PDF → JPEG pages for visual QA. Returns list of image paths."""
    os.makedirs(out_dir, exist_ok=True)
    subprocess.run([sys.executable, os.path.join(SKILL, "office", "soffice.py"), "--headless", "--convert-to", "pdf",
                    "--outdir", out_dir, out_pptx], check=True, capture_output=True)
    pdf = os.path.join(out_dir, os.path.splitext(os.path.basename(out_pptx))[0] + ".pdf")
    for f in os.listdir(out_dir):
        if f.startswith("slide-") and f.endswith(".jpg"):
            os.remove(os.path.join(out_dir, f))
    subprocess.run(["pdftoppm", "-jpeg", "-r", "150", pdf, os.path.join(out_dir, "slide")], check=True)
    return sorted(os.path.join(out_dir, f) for f in os.listdir(out_dir) if f.startswith("slide-") and f.endswith(".jpg"))
