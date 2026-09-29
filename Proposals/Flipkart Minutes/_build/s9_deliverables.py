from dml import *
from common import *

BLOCKS = [
    ("01", "DG Monitoring on IOsense", "activity",
     "Every DG live — fuel level, volume, running hours, energy and operating status, from store to zone."),
    ("02", "Alerts & Work Orders", "bell-ring",
     "Low fuel, maintenance due and breakdown raise a work order automatically and assign it to the mapped vendor."),
    ("03", "Vendor Portal", "user-check",
     "Vendor SPOCs acknowledge, execute and submit litres or maintenance details with proof, from any device."),
    ("04", "Billing & Oracle Fusion", "receipt",
     "Line items per transaction, invoice with upload and locking, posted to Oracle Fusion over the API."),
    ("05", "Dashboards & Reports", "layout-dashboard",
     "Operational and financial views, filters and CSV / Excel downloads, limited to each user's access."),
    ("06", "Access Control & Audit", "shield-check",
     "Store, central, vendor, maintenance and super-admin roles, with a full audit history of every action."),
]


def build():
    ids = Ids()
    S = [header(ids, "BOTH WORKFLOWS  ·  DELIVERABLES", "Software Deliverables",
                "One application on the IOsense cloud, delivered as six capabilities.")]

    top = 1.15
    # banner
    S.append(rect(ids, "Banner", 0.30, top, 9.40, 0.34, fill=AZURE, radius=0.07))
    S.append(rect(ids, "Banner icon box", 0.42, top + 0.06, 0.22, 0.22, fill=WHITE, alpha=18, radius=0.04))
    S.append(icon(ids, "app-window", 0.46, top + 0.10, 0.14, WHITE))
    S.append(textbox(ids, "Deliverable name", 0.74, top, 5.6, 0.34,
                     [para(run("DG Fuel Management & Maintenance Application", FONT_BODY_SB, 9.5, WHITE), lnspc=10.5)], anchor="ctr"))
    cx = 9.58
    for lab, icn in [("Mobile-responsive web", "monitor"), ("IOsense cloud", "cloud")][::-1]:
        _, w = chip(ids, 0, 0, lab, "dark", icon_name=icn, h=0.17, size=6.0)
        cx -= w
        xml, _ = chip(ids, cx, top + 0.085, lab, "dark", icon_name=icn, h=0.17, size=6.0)
        S.append(xml)
        cx -= 0.07

    gx, gy = 0.30, top + 0.47
    gap = 0.14
    cw = (9.40 - 2 * gap) / 3
    rh = 1.34
    for i, (num, title, icn, line1) in enumerate(BLOCKS):
        r, c = divmod(i, 3)
        x = gx + c * (cw + gap)
        y = gy + r * (rh + gap)
        parts = [card(ids, "Block card", x, y, cw, rh)]
        parts.append(rect(ids, "Icon tile", x + 0.16, y + 0.18, 0.40, 0.40, fill=AZURE_050, radius=0.07))
        parts.append(icon(ids, icn, x + 0.26, y + 0.28, 0.20, AZURE))
        parts.append(textbox(ids, "Block number", x + cw - 0.62, y + 0.14, 0.46, 0.26,
                             [para(run(num, FONT_HEAD, 13, N300), align="r", lnspc=14)]))
        tp = para(run(title, FONT_BODY_SB, 10, HEADING), lnspc=11.5)
        th = para_height(tp, cw - 0.32)
        parts.append(textbox(ids, "Block title", x + 0.16, y + 0.68, cw - 0.32, th, [tp]))
        bp = para(run(line1, FONT_BODY, 7.4, SECOND), lnspc=9.6)
        parts.append(textbox(ids, "Block line", x + 0.16, y + 0.68 + th + 0.07, cw - 0.32,
                             para_height(bp, cw - 0.32), [bp]))
        S.append(group(ids, "Block " + num, parts, x, y, cw, rh))
    grid_bottom = gy + 2 * rh + gap

    # services strip
    sy = grid_bottom + 0.14
    sh = 5.15 - sy
    S.append(card(ids, "Services strip", 0.30, sy, 9.40, sh, fill=N050, line=N200))
    S.append(icon(ids, "package", 0.44, sy + sh / 2 - 0.09, 0.18, AZURE))
    S.append(textbox(ids, "Strip title", 0.70, sy, 1.30, sh,
                     [para([run("Services included", FONT_BODY_SB, 7.4, HEADING)], lnspc=8.4)], anchor="ctr"))
    labels = ["User manual / SOP", "Operator & vendor training", "UAT and go-live support", "Post go-live support"]
    bx = 2.10
    for lab in labels:
        xml, w = chip(ids, bx, sy + sh / 2 - 0.09, lab, "white", icon_name="circle-check", h=0.18, size=6.2)
        S.append(xml)
        bx += w + 0.10
    print(f"  s9: grid to {grid_bottom:.2f}, services {sy:.2f}–{sy + sh:.2f}, chips end {bx:.2f}")

    S.append(footer(ids, FOOTER))
    return slide_xml(S)
