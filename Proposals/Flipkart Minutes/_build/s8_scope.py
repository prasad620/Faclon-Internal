from dml import *
from common import *


def column_header(ids, x, y, w, title, sub, icon_name, fill=AZURE, tcol=WHITE, scol="DCE8FE", icol=WHITE, icon_fill=None):
    parts = [rect(ids, "Column header", x, y, w, 0.30, fill=fill, radius=0.06)]
    if icon_fill:
        parts.append(rect(ids, "Icon box", x + 0.10, y + 0.05, 0.20, 0.20, fill=icon_fill, radius=0.04))
    parts.append(icon(ids, icon_name, x + 0.13, y + 0.08, 0.14, icol))
    parts.append(textbox(ids, "Column title", x + 0.40, y, w - 0.5, 0.30,
                         [para([run(title, FONT_BODY_SB, 7, tcol), run("   " + sub, FONT_BODY, 6.4, scol)], lnspc=7.5)], anchor="ctr"))
    return group(ids, "Column header " + title, parts, x, y, w, 0.30)


def group_card(ids, x, y, w, title, icon_name, items, size=6.6, pad=0.09):
    parts = []
    parts.append(rect(ids, "Icon box", x + pad, y + pad, 0.26, 0.26, fill=AZURE_050, radius=0.05))
    parts.append(icon(ids, icon_name, x + pad + 0.06, y + pad + 0.06, 0.14, AZURE))
    tx = x + pad + 0.36
    tw = w - pad * 2 - 0.36
    parts.append(textbox(ids, "Group title", tx, y + pad - 0.01, tw, 0.15, [para(run(title, FONT_BODY_SB, 7.4, HEADING), lnspc=8.5)]))
    by = y + pad + 0.16
    xml, bh = bullets(ids, tx, by, tw, items, size=size, gap=0.02, lnspc=size * 1.18)
    parts.append(xml)
    total = by + bh + pad - y
    return group(ids, "Group " + title, [card(ids, "Group card", x, y, w, total)] + parts, x, y, w, total), total


def build():
    ids = Ids()
    S = [header(ids, "BOTH WORKFLOWS  ·  SCOPE", "Scope of Work",
                "What Faclon Labs delivers and what Flipkart provides for the DG monitoring, refilling and maintenance workflows.")]

    top = 1.15
    lx, lw = 0.30, 6.05
    rx, rw = 6.50, 3.20
    S.append(column_header(ids, lx, top, lw, "Faclon Labs scope", "design, build, integrate, deploy and support", "package"))
    S.append(column_header(ids, rx, top, rw, "Flipkart scope", "inputs, access and infrastructure", "building-2",
                           fill=N100, tcol=HEADING, scol=SECOND, icol=SECOND))

    groups = [
        ("Hardware, connectivity & installation", "cpu", [
            ("Supply: ", "IoT device and gateway per store, 4G SIM and data \u2014 warranty and hardware AMC included"),
            ("Install & integrate: ", "commissioning at every store; existing DG controller read over RS-485 / Modbus"),
        ]),
        ("DG monitoring on IOsense", "activity", [
            ("Live DG views: ", "fuel level, volume, running hours, kWh and status; store, city and zone views"),
        ]),
        ("Workflow 01  \u00b7  Fuel management & vendor refilling", "fuel", [
            ("Masters & settings: ", "store, DG, vendor & SPOC masters; low-fuel limits; waiting time; rate cards"),
            ("Refill cycle: ", "alert \u2192 work order \u2192 assignment \u2192 vendor portal \u2192 completion, with audit history"),
        ]),
        ("Workflow 02  \u00b7  Preventive & breakdown maintenance", "wrench", [
            ("PM & breakdown: ", "triggers per DG; work order to the AMC vendor; details and proof; shared history"),
        ]),
        ("Billing, Oracle Fusion & services", "receipt", [
            ("Billing to Fusion: ", "line items, eligible transactions, invoice upload, locking, posting to Oracle Fusion"),
            ("Also included: ", "notifications, dashboards and downloads  \u00b7  SOP  \u00b7  training  \u00b7  UAT  \u00b7  go-live support"),
        ]),
    ]
    cy = top + 0.40
    for t, icn, items in groups:
        xml, h = group_card(ids, lx, cy, lw, t, icn, items)
        S.append(xml)
        cy += h + 0.07
    # optional strip
    oy = cy
    S.append(rect(ids, "Optional strip", lx, oy, lw, 0.30, fill=CIDER_050, line=CIDER, line_w=0.5, radius=0.06))
    S.append(icon(ids, "receipt", lx + 0.12, oy + 0.08, 0.14, CIDER_700))
    S.append(textbox(ids, "Optional text", lx + 0.34, oy, lw - 0.45, 0.30,
                     [para([run("Optional scope  ·  ", FONT_BODY_SB, 6.8, CIDER_700),
                            run("automated report scheduling and distribution \u2014 schedule and recipients to be finalised",
                                FONT_BODY, 6.6, BODY)], lnspc=7.6)], anchor="ctr"))
    left_bottom = oy + 0.30

    # Flipkart scope card
    items = [
        ("database", "Store master (zone, city, store, email IDs), DG master and the user list with roles"),
        ("users-round", "Refilling and AMC vendor list, SPOC contacts, vendor-to-DG mapping and rate cards"),
        ("sliders-horizontal", "Low-fuel limits, waiting time and PM settings (running-hours limit / fixed period) per DG"),
        ("map-pin", "Site access to each store and DG for installation and commissioning"),
        ("zap", "Power supply and mounting space for the gateway; store network access where used"),
        ("plug-zap", "Oracle Fusion interface specification, authentication and credentials"),
        ("message-circle-more", "WhatsApp Business account and email sender for the work-order notifications"),
    ]
    ry = top + 0.40
    ch = left_bottom - ry
    S.append(card(ids, "Flipkart scope card", rx, ry, rw, ch))
    iy = ry + 0.10
    tw = rw - 0.20 - 0.30
    rows = []
    for icn, t in items:
        p = para(run(t, FONT_BODY, 6.6, BODY), lnspc=7.7)
        h = para_height(p, tw)
        rows.append((icn, p, h))
    total_text = sum(h for _, _, h in rows)
    gap = max(0.04, (ch - 0.20 - total_text) / (len(rows) - 1)) if len(rows) > 1 else 0
    for i, (icn, p, h) in enumerate(rows):
        S.append(icon(ids, icn, rx + 0.12, iy + 0.005, 0.14, SECOND))
        S.append(textbox(ids, "Scope item", rx + 0.34, iy, tw, h, [p]))
        if i < len(rows) - 1:
            S.append(line(ids, "Divider", rx + 0.12, iy + h + gap / 2, rx + rw - 0.12, iy + h + gap / 2, color=N200, w=0.5))
        iy += h + gap
    right_bottom = iy - gap + 0.10

    # responsibility bar
    by = max(left_bottom, right_bottom) + 0.09
    S.append(rect(ids, "Responsibility bar", 0.30, by, 9.40, 0.24, fill=CIDER_050, radius=0.05))
    cxml, cw = chip(ids, 0.36, by + 0.045, "Responsibility to be agreed", "cider-solid", icon_name="circle-help")
    S.append(cxml)
    S.append(textbox(ids, "Responsibility items", 0.36 + cw + 0.10, by, 7.5, 0.24,
                     [para(run("Vendor SPOC account creation and onboarding   ·   WhatsApp message-template approval",
                               FONT_BODY, 6.6, BODY), lnspc=6.6)], anchor="ctr"))
    print(f"  s8: left {left_bottom:.2f} right {right_bottom:.2f} bar ends {by + 0.24:.2f} (gap {gap:.3f})")

    S.append(footer(ids, FOOTER))
    return slide_xml(S)
