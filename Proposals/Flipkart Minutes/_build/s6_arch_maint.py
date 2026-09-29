from dml import *
from common import *
from s5_arch_refill import decision_block, vendor_tile


def build():
    ids = Ids()
    S = [header(ids, "WORKFLOW 02  ·  PREVENTIVE & BREAKDOWN MAINTENANCE", "Solution Architecture",
                "Preventive maintenance from running hours or a fixed period, breakdowns from the store — both closed by the AMC vendor.",
                badge="02", badge_fill=DARK)]

    S += [stage_label(ids, 0.30, 1.10, 1, "TRIGGERS"), stage_label(ids, 2.52, 1.10, 2, "EVALUATE & CREATE"),
          stage_label(ids, 5.10, 1.10, 3, "ASSIGN & EXECUTE"), stage_label(ids, 7.72, 1.10, 4, "OUTPUTS")]

    top = 1.36
    PAD = 0.08
    # ---------------------------------------------------------------- triggers
    ix, iw = 0.30, 2.05
    cy = top
    in_cards = [
        ("Running hours  ·  IoT", "Read from the DG controller", "timer", ["Limit per DG, e.g. 250 / 500 h"], "neutral"),
        ("Fixed maintenance period", "Configured per DG", "calendar-clock", ["Whichever occurs first"], "neutral"),
        ("Breakdown  ·  manual", "Raised by the store / maintenance team", "siren",
         ["Physical failure", "Leak", "Starting failure"], "crimson"),
        ("Master data", "AMC vendors, SPOCs and PM settings", "database", None, "neutral"),
    ]
    mids = []
    for t, s_, icn, chips, tone in in_cards:
        xml, h = titled_card(ids, t, ix, cy, iw, t, s_, icn, chips=chips, chip_tone=tone, pad=0.09)
        S.append(xml)
        mids.append(cy + h / 2)
        cy += h + 0.07
    inputs_bottom = cy - 0.07

    # ---------------------------------------------------------------- application block
    ax, aw = 2.50, 5.05
    S.append("APPBLOCK")
    S.append(icon(ids, "app-window", ax + 0.12, top + 0.09, 0.16, AZURE))
    S.append(textbox(ids, "Application label", ax + 0.34, top + 0.07, 3.3, 0.20,
                     [para([run("DG Maintenance Workflow", FONT_BODY_SB, 7.4, HEADING),
                            run("   ·   same application", FONT_BODY, 6.8, SECOND)], lnspc=8)], anchor="ctr"))
    _, cw_ = chip(ids, 0, 0, "Mobile-responsive web", "dark", icon_name="monitor")
    cxml, _ = chip(ids, ax + aw - 0.12 - cw_, top + 0.09, "Mobile-responsive web", "dark", icon_name="monitor")
    S.append(cxml)
    for v in mids:
        S.append(line(ids, "Input link", ix + iw, v, ax, v, color=AZURE, w=1.0, tail="triangle"))

    colw = 2.36
    lx, rx = ax + 0.12, ax + 0.12 + colw + 0.09
    cy = top + 0.36
    left = [
        ("gauge", "PM evaluation", "Hours limit or period reached → PM work order", None),
        ("tag", "Trigger type recorded", "Value or due date kept on the work order",
         ["Running Hours", "Scheduled Period", "Breakdown"]),
        ("triangle-alert", "Breakdown work order", "Created as soon as it is reported in the platform", None),
    ]
    ly = cy
    for icn, t, d, chips in left:
        xml, h = step_card(ids, t, lx, ly, colw, t, d, icn, chips=chips, chip_tone="azure", pad=PAD, desc_size=6.3)
        S.append(xml)
        ly += h + 0.07
    ry = cy
    xml, h = decision_block(ids, rx, ry, colw, "Auto-assignment  ·  AMC vendor",
                            "Active AMC vendor + SPOC mapped?", "Primary SPOC assigned", "Mapping required")
    S.append(xml)
    ry += h + 0.07
    xml, h = step_card(ids, "Initial notification", rx, ry, colw, "Initial notification",
                       "Email · WhatsApp · in-app, as per access", "send", pad=PAD, desc_size=6.3)
    S.append(xml)
    ry += h + 0.07
    xml, h = vendor_tile(ids, rx, ry, colw, "AMC vendor SPOC",
                         ["Acknowledge", "Carry out", "Details + proof", "Submit"],
                         note="Action taken · parts replaced · clearance", icon_name="hard-hat")
    S.append(xml)
    ry += h + 0.07
    cols_bottom = max(ly, ry) - 0.07

    fy = cols_bottom + 0.09
    S.append(textbox(ids, "Status label", lx, fy, 0.5, 0.17,
                     [para(run("STATUS", FONT_BODY_SB, 5.6, SECOND, spc=60, caps=True), lnspc=5.6)], anchor="ctr"))
    S += flow_pills(ids, lx + 0.52, fy, ["Created", "Assigned", "Acknowledged", "In Progress", "Submitted", "Completed"], aw - 0.24 - 0.52)
    app_bottom = fy + 0.17 + 0.11
    S[S.index("APPBLOCK")] = card(ids, "Application block", ax, top, aw, app_bottom - top, fill=AZURE_050, line=AZURE_200, radius=0.09)

    # ---------------------------------------------------------------- outputs
    ox, ow = 7.70, 2.00
    cy = top
    S.append(line(ids, "Output link", ax + aw, top + 0.30, ox, top + 0.30, color=AZURE, w=1.0, tail="triangle"))
    out_cards = [
        ("Shared visibility", "Store · central · maintenance · vendor", "eye",
         ["Breakdown tickets", "PM schedules", "Repair history"], "dark-ghost", AZURE, WHITE, "DCE8FE", WHITE),
        ("Service history per DG", "Kept with every work order", "history",
         ["Trigger & value", "Vendor & SPOC", "Details & proof"], "dark-ghost", DARK, WHITE, "B1C1D2", WHITE),
        ("Dashboards & downloads", "Open tickets, with filters", "download", None, "neutral", WHITE, HEADING, MUTED, AZURE),
        ("Audit history", "Maintenance alerts and user actions", "list-checks", None, "neutral", WHITE, HEADING, MUTED, AZURE),
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
        ("split", "Whichever first", "Hours limit or fixed period, set per DG"),
        ("users", "Multiple AMC vendors", "Several vendors mapped to one DG or site"),
        ("user-cog", "Same vendor, both roles", "Refilling and AMC, same or separate SPOCs"),
        ("arrow-right-left", "Reassignment", "Moved to another mapped vendor; same ID"),
        ("power-off", "Deactivation", "History kept when a DG or vendor is inactive"),
        ("pen-line", "Status names", "Finalised during UI design"),
    ]))
    print(f"  s6: app {top:.2f}–{app_bottom:.2f}  inputs {inputs_bottom:.2f}  outputs {outputs_bottom:.2f}  band {band_y:.2f} h={band_h:.2f}")

    S.append(footer(ids, FOOTER))
    return slide_xml(S)
