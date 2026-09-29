from dml import *
from common import *


def decision_block(ids, x, y, w, title, question, yes_chip, no_chip, pad=0.08, title_size=7.0):
    """Decision tile: title → question pill → Yes / No branches. Returns (xml, height)."""
    parts = []
    tp = para(run(title, FONT_BODY_SB, title_size, HEADING), lnspc=title_size * 1.15)
    tw = w - pad * 2 - 0.24
    th = para_height(tp, tw)
    parts.append(icon(ids, "git-branch", x + pad, y + pad + 0.005, 0.15, AZURE))
    parts.append(textbox(ids, "Decision title", x + pad + 0.24, y + pad, tw, th, [tp]))
    qy = y + pad + th + 0.07
    qw = text_width(question, FONT_BODY_SB, 6.3) + 0.24
    qx = x + pad
    parts.append(rect(ids, "Question", qx, qy, qw, 0.19, fill=N100, line=N300, line_w=0.5, radius=0.04))
    parts.append(textbox(ids, "Question text", qx, qy, qw, 0.19,
                         [para(run(question, FONT_BODY_SB, 6.3, HEADING), align="ctr", lnspc=6.3)], anchor="ctr"))
    by = qy + 0.19 + 0.13
    c1, w1 = chip(ids, qx, by, yes_chip, "emerald", icon_name="circle-check")
    c2, w2 = chip(ids, qx + w1 + 0.12, by, no_chip, "cider", icon_name="circle-alert")
    parts.append(line(ids, "Yes link", qx + 0.12, qy + 0.19, qx + 0.12, by, color=N400, w=0.5))
    parts.append(line(ids, "No link", qx + qw - 0.05, qy + 0.19, qx + qw - 0.05, qy + 0.19 + 0.065, color=N400, w=0.5))
    parts.append(line(ids, "No link b", qx + qw - 0.05, qy + 0.19 + 0.065, qx + w1 + 0.12 + 0.12, qy + 0.19 + 0.065, color=N400, w=0.5))
    parts.append(line(ids, "No link c", qx + w1 + 0.12 + 0.12, qy + 0.19 + 0.065, qx + w1 + 0.12 + 0.12, by, color=N400, w=0.5))
    parts += [c1, c2]
    total = by + 0.15 + pad - y
    bg = card(ids, "Decision card", x, y, w, total, fill=WHITE, line=N300, radius=0.07)
    return group(ids, "Decision", [bg] + parts, x, y, w, total), total


def vendor_tile(ids, x, y, w, title, steps, note=None, pad=0.08, icon_name="user-check"):
    """Dark execution tile with chevron-joined step chips. Returns (xml, height)."""
    parts = [icon(ids, icon_name, x + pad, y + pad + 0.005, 0.15, AZURE_300)]
    tp = para([run(title, FONT_BODY_SB, 7.2, WHITE), run("  ·  web portal", FONT_BODY, 6.4, "B1C1D2")], lnspc=8.3)
    parts.append(textbox(ids, "Vendor title", x + pad + 0.24, y + pad, w - pad * 2 - 0.24, 0.13, [tp]))
    sy = y + pad + 0.13 + 0.07
    row_h = 0.15
    avail = w - pad * 2
    rows, cur = [[]], 0.0
    for lab in steps:
        _, cw_ = chip(ids, 0, 0, lab, "dark-ghost", size=5.8)
        add = cw_ if not rows[-1] else 0.15 + cw_
        if cur + add > avail and rows[-1]:
            rows.append([(lab, cw_)])
            cur = cw_
        else:
            rows[-1].append((lab, cw_))
            cur += add
    for r, row in enumerate(rows):
        sx = x + pad
        for i, (lab, cw_) in enumerate(row):
            c, _ = chip(ids, sx, sy, lab, "dark-ghost", size=5.8)
            parts.append(c)
            sx += cw_
            if i < len(row) - 1:
                parts.append(icon(ids, "chevron-right", sx + 0.02, sy + 0.025, 0.10, "5A8DF7"))
                sx += 0.15
        if r < len(rows) - 1:
            sy += row_h + 0.05
    sy += row_h
    if note:
        sy += 0.06
        np_ = para(run(note, FONT_BODY, 6.2, "B1C1D2"), lnspc=7.4)
        nh = para_height(np_, w - pad * 2)
        parts.append(textbox(ids, "Vendor note", x + pad, sy, w - pad * 2, nh, [np_]))
        sy += nh
    h = sy + pad - y
    bg = card(ids, "Vendor card", x, y, w, h, fill=DARK, line=DARK, radius=0.07)
    return group(ids, "Vendor execution", [bg] + parts, x, y, w, h), h


def build():
    ids = Ids()
    S = [header(ids, "WORKFLOW 01  ·  FUEL MONITORING & VENDOR REFILLING", "Solution Architecture",
                "What comes in from each DG, what the application decides, and what the vendor and Flipkart users get.",
                badge="01")]

    S += [stage_label(ids, 0.30, 1.10, 1, "INPUTS"), stage_label(ids, 2.52, 1.10, 2, "MONITOR & TRIGGER"),
          stage_label(ids, 5.10, 1.10, 3, "ASSIGN & EXECUTE"), stage_label(ids, 7.72, 1.10, 4, "OUTPUTS")]

    top = 1.36
    PAD = 0.08
    # ---------------------------------------------------------------- inputs
    ix, iw = 0.30, 2.05
    cy = top
    in_cards = [
        ("IoT device + gateway", "Faclon supplied · polls the controller", "cpu",
         ["Fuel %", "Litres", "Running hours", "kWh", "Status"], "azure"),
        ("Master data", "Set up in the application", "database",
         ["Zone → City → Store", "Vendors & SPOCs", "Low-fuel limits"], "neutral"),
        ("Manual trigger", "Store · Central · Super Admin", "square-pen", ["On-demand refill"], "neutral"),
    ]
    mids = []
    for t, s_, icn, chips, tone in in_cards:
        xml, h = titled_card(ids, t, ix, cy, iw, t, s_, icn, chips=chips, chip_tone=tone, pad=0.10)
        S.append(xml)
        mids.append(cy + h / 2)
        cy += h + 0.07
    inputs_bottom = cy - 0.07

    # ---------------------------------------------------------------- application block
    ax, aw = 2.50, 5.05
    S.append("APPBLOCK")
    S.append(icon(ids, "app-window", ax + 0.12, top + 0.09, 0.16, AZURE))
    S.append(textbox(ids, "Application label", ax + 0.34, top + 0.07, 3.3, 0.20,
                     [para([run("DG Fuel Management Application", FONT_BODY_SB, 7.4, HEADING),
                            run("   ·   IOsense cloud", FONT_BODY, 6.8, SECOND)], lnspc=8)], anchor="ctr"))
    _, cw_ = chip(ids, 0, 0, "Mobile-responsive web", "dark", icon_name="monitor")
    cxml, _ = chip(ids, ax + aw - 0.12 - cw_, top + 0.09, "Mobile-responsive web", "dark", icon_name="monitor")
    S.append(cxml)
    for v in mids:
        S.append(line(ids, "Input link", ix + iw, v, ax, v, color=AZURE, w=1.0, tail="triangle"))

    colw = 2.36
    lx, rx = ax + 0.12, ax + 0.12 + colw + 0.09
    cy = top + 0.36
    left = [
        ("activity", "Live monitoring", "Fuel, hours, energy and status per DG", None),
        ("gauge", "Low-fuel evaluation", "Below the limit for the waiting time",
         ["DG › Store › City › Zone › Global"]),
        ("bell-ring", "Alert + refill work order", "One alert, one work order, unique ID", None),
    ]
    ly = cy
    for icn, t, d, chips in left:
        xml, h = step_card(ids, t, lx, ly, colw, t, d, icn, chips=chips, chip_tone="azure", pad=PAD, desc_size=6.3)
        S.append(xml)
        ly += h + 0.07
    ry = cy
    xml, h = decision_block(ids, rx, ry, colw, "Auto-assignment  ·  primary vendor",
                            "Active vendor + SPOC mapped to the DG?", "Primary SPOC assigned", "Mapping required")
    S.append(xml)
    ry += h + 0.07
    xml, h = step_card(ids, "Initial notification", rx, ry, colw, "Initial notification",
                       "Email · WhatsApp · in-app, as per access", "send", pad=PAD, desc_size=6.3)
    S.append(xml)
    ry += h + 0.07
    xml, h = vendor_tile(ids, rx, ry, colw, "Vendor SPOC",
                         ["Acknowledge", "Refuel", "Enter litres", "Proof", "Submit"])
    S.append(xml)
    ry += h + 0.07
    cols_bottom = max(ly, ry) - 0.07

    fy = cols_bottom + 0.09
    S.append(textbox(ids, "Status label", lx, fy, 0.5, 0.17,
                     [para(run("STATUS", FONT_BODY_SB, 5.6, SECOND, spc=60, caps=True), lnspc=5.6)], anchor="ctr"))
    S += flow_pills(ids, lx + 0.52, fy, ["Created", "Assigned", "Acknowledged", "Refueling", "Submitted", "Completed"], aw - 0.24 - 0.52)
    app_bottom = fy + 0.17 + 0.11
    S[S.index("APPBLOCK")] = card(ids, "Application block", ax, top, aw, app_bottom - top, fill=AZURE_050, line=AZURE_200, radius=0.09)

    # ---------------------------------------------------------------- outputs
    ox, ow = 7.70, 2.00
    cy = top
    S.append(line(ids, "Output link", ax + aw, top + 0.30, ox, top + 0.30, color=AZURE, w=1.0, tail="triangle"))
    out_cards = [
        ("Dashboards & views", "Store, city and zone by access", "layout-dashboard",
         ["Fuel status", "Alerts", "Work orders"], "dark-ghost", AZURE, WHITE, "DCE8FE", WHITE),
        ("Billing & Oracle Fusion", "Line items → invoice → Fusion", "receipt",
         ["Refill charge", "Fuel / hours", "Invoice locked"], "dark-ghost", DARK, WHITE, "B1C1D2", WHITE),
        ("Transactions & downloads", "Filter by zone, city, store, vendor", "download", None, "neutral", WHITE, HEADING, MUTED, AZURE),
        ("Audit history", "Alerts, actions and transactions", "history", None, "neutral", WHITE, HEADING, MUTED, AZURE),
    ]
    for t, s_, icn, chips, ctone, fill, tcol, scol, icol in out_cards:
        xml, h = titled_card(ids, t, ox, cy, ow, t, s_, icn, fill=fill, line=fill if fill != WHITE else N300,
                             title_color=tcol, sub_color=scol, icon_color=icol, chips=chips, chip_tone=ctone, pad=0.09)
        S.append(xml)
        cy += h + 0.07
    outputs_bottom = cy - 0.07

    # ---------------------------------------------------------------- band
    band_y = max(app_bottom, outputs_bottom, inputs_bottom) + 0.11
    band_h = 5.25 - band_y
    S.append(band(ids, 0.30, band_y, 9.40, band_h, "Built-in rules & safeguards", "as per the SRS", [
        ("copy-x", "Duplicate prevention", "No second alert for the same condition"),
        ("user-x", "No valid vendor", "Work order held; DG flagged for mapping"),
        ("arrow-right-left", "Reassignment", "Moved to another mapped vendor; same ID"),
        ("power-off", "Inactive DG", "No new work orders; history kept"),
        ("text-cursor-input", "Litres by vendor", "Entered, not derived from IoT readings"),
        ("timer", "Waiting time", "Set on the DG data frequency", "TBC"),
    ]))
    print(f"  s5: app {top:.2f}–{app_bottom:.2f}  inputs {inputs_bottom:.2f}  outputs {outputs_bottom:.2f}  band {band_y:.2f} h={band_h:.2f}")

    S.append(footer(ids, FOOTER))
    return slide_xml(S)
