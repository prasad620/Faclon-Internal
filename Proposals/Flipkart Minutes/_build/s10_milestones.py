from dml import *
from common import *

MILESTONES = [
    ("flag", "Kick-off & requirement sign-off",
     "Scope, masters, thresholds, PM settings, billing rates and the Fusion interface signed off",
     ["SRS sign-off", "Store & DG masters", "Limits & PM settings"], "Signed-off SRS"),
    ("cpu", "Hardware supply & installation",
     "IoT devices, gateways and SIMs delivered, installed and commissioned; DG controllers integrated",
     ["Site access", "Power & mounting", "Store & DG list"], "DGs live on IOsense"),
    ("code-xml", "Application development",
     "Masters, alert engine, work orders, vendor portal, billing engine and dashboards",
     ["Clarifications on rules"], "Build complete"),
    ("plug-zap", "Configuration & integration",
     "Masters loaded, notifications connected and the Oracle Fusion interface integrated",
     ["Vendor & SPOC list", "WhatsApp / email setup", "Fusion API spec"], "System configured"),
    ("clipboard-check", "UAT",
     "End-to-end refill, maintenance and billing cycles with store, central and vendor users",
     ["Users for UAT", "Test stores / DGs"], "UAT sign-off"),
    ("rocket", "Go-live & handover",
     "Go-live across stores, user manual / SOP and training; post go-live support begins",
     ["Rollout store list", "Go-live schedule"], "Live + handover"),
]


def build():
    ids = Ids()
    S = [header(ids, "BOTH WORKFLOWS  ·  PLAN", "Implementation Milestones",
                "From kick-off to go-live — hardware, application, billing and Fusion; the week-by-week plan follows on the next slide.")]

    top = 1.20
    ph = 2.30
    # identity block
    S.append(rect(ids, "Identity", 0.30, top, 1.50, ph, fill=AZURE, radius=0.08))
    S.append(rect(ids, "Identity corner", 0.30, top, 1.50, ph, fill=AZURE, radius=0.08))
    S.append(icon(ids, "fuel", 1.42, top + 0.16, 0.22, WHITE))
    S.append(textbox(ids, "Project number", 0.46, top + 0.10, 0.9, 0.42, [para(run("01–02", FONT_HEAD, 20, WHITE), lnspc=22)], anchor="ctr"))
    S.append(textbox(ids, "Project name", 0.46, top + 0.62, 1.25, 0.5,
                     [para(run("DG Online Monitoring", FONT_HEAD, 11, WHITE), lnspc=12.5),
                      para(run("Refilling  ·  Maintenance", FONT_BODY, 6.6, "DCE8FE"), lnspc=8, spc_before=2)]))
    S.append(line(ids, "Divider", 0.46, top + 1.28, 1.64, top + 1.28, color=AZURE_400, w=0.5))
    S.append(textbox(ids, "Applications label", 0.46, top + 1.36, 1.25, 0.14,
                     [para(run("APPLICATION", FONT_BODY_SB, 5.5, "B8D0FD", spc=82, caps=True), lnspc=5.5)]))
    S.append(textbox(ids, "Applications", 0.46, top + 1.52, 1.25, 0.4,
                     [para(run("DG Fuel Management & Maintenance Application on the IOsense cloud", FONT_BODY_SB, 6.6, WHITE), lnspc=7.9)]))

    # milestone panel
    px, pw = 1.80, 7.90
    S.append(card(ids, "Milestone panel", px, top, pw, ph, fill=N050, line=N200))
    n = len(MILESTONES)
    colw = (pw - 0.30) / n
    cy = top + 0.28
    r = 0.36
    # connector line through the icons
    x0 = px + 0.15 + colw / 2
    S.append(line(ids, "Track", x0, cy + r / 2, x0 + (n - 1) * colw, cy + r / 2, color=AZURE_200, w=1.5))
    for i, (icn, title, desc, inputs, output) in enumerate(MILESTONES):
        cx = px + 0.15 + i * colw
        mx = cx + colw / 2
        S.append(ellipse(ids, "Milestone circle", mx - r / 2, cy, r, r, fill=AZURE if i < n - 1 else DARK))
        S.append(icon(ids, icn, mx - 0.085, cy + r / 2 - 0.085, 0.17, WHITE))
        S.append(textbox(ids, "Milestone label", cx, cy + r + 0.10, colw, 0.14,
                         [para(run(f"MILESTONE {i + 1}", FONT_BODY_SB, 5.6, AZURE, spc=82, caps=True), align="ctr", lnspc=5.6)], anchor="ctr"))
        tp = para(run(title, FONT_BODY_SB, 7.4, HEADING), align="ctr", lnspc=8.6)
        th = para_height(tp, colw - 0.16)
        S.append(textbox(ids, "Milestone title", cx + 0.08, cy + r + 0.27, colw - 0.16, th, [tp]))
        dp = para(run(desc, FONT_BODY, 6.3, SECOND), align="ctr", lnspc=7.5)
        dh = para_height(dp, colw - 0.16)
        S.append(textbox(ids, "Milestone description", cx + 0.08, cy + r + 0.27 + th + 0.04, colw - 0.16, dh, [dp]))
        oxml, ow = chip(ids, 0, 0, output, "emerald", icon_name="circle-check")
        oxml, ow = chip(ids, mx - ow / 2, top + ph - 0.32, output, "emerald", icon_name="circle-check")
        S.append(oxml)

    # inputs panel
    iy = top + ph + 0.12
    ih = 5.25 - iy
    S.append(card(ids, "Inputs panel", 0.30, iy, 9.40, ih, fill=WHITE, line=N300))
    S.append(rect(ids, "Inputs icon box", 0.44, iy + 0.14, 0.26, 0.26, fill=N100, radius=0.05))
    S.append(icon(ids, "building-2", 0.50, iy + 0.20, 0.14, SECOND))
    S.append(textbox(ids, "Inputs title", 0.44, iy + 0.48, 1.25, ih - 0.55,
                     [para(run("Inputs needed from Flipkart", FONT_BODY_SB, 7.2, HEADING), lnspc=8.4),
                      para(run("at each milestone, so the plan holds", FONT_BODY, 6.2, MUTED), lnspc=7.3, spc_before=1)]))
    for i, (icn, title, desc, inputs, output) in enumerate(MILESTONES):
        cx = px + 0.15 + i * colw
        if i > 0:
            S.append(line(ids, "Divider", cx - 0.02, iy + 0.14, cx - 0.02, iy + ih - 0.14, color=N200, w=0.5))
        S.append(textbox(ids, "Inputs label", cx + 0.06, iy + 0.14, colw - 0.12, 0.13,
                         [para(run(f"M{i + 1}", FONT_BODY_SB, 5.6, TERT, spc=82, caps=True), lnspc=5.6)], anchor="ctr"))
        yy = iy + 0.33
        for lab in inputs:
            xml, w = chip(ids, cx + 0.06, yy, lab, "neutral", icon_name="corner-down-right", h=0.17, size=5.8)
            S.append(xml)
            yy += 0.17 + 0.07
    S.append(footer(ids, FOOTER))
    return slide_xml(S)
