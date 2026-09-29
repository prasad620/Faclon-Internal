from dml import *
from common import *


def build():
    ids = Ids()
    S = [header(ids, "BOTH WORKFLOWS  ·  COMMERCIALS", "Commercials",
                "Commercial summary including hardware, software, billing and Oracle Fusion. Amounts to be filled in.")]

    top = 1.15
    cols = [0.40, 2.05, 4.55, 1.10, 1.30]
    heads = ["#", "LINE ITEM", "DESCRIPTION", "TYPE", "AMOUNT"]
    hdr = [dict(paras=[para(run(h, FONT_BODY_SB, 5.8, WHITE, spc=60, caps=True), lnspc=6.5,
                            align="ctr" if i in (0, 3, 4) else "l")], fill=AZURE, border_bottom=None) for i, h in enumerate(heads)]
    rows_data = [
        ("01", "Hardware supply & installation",
         "IoT device and gateway per store, mounting and accessories; installation, commissioning and integration to the "
         "existing DG controller at each store \u2014 warranty included", "One-time"),
        ("02", "Software development & implementation",
         "DG Fuel Management & Maintenance Application: monitoring, alerts, work orders, vendor portal, vendor billing and "
         "Oracle Fusion integration; deployment on the IOsense cloud", "One-time"),
        ("03", "IOsense platform licence",
         "Cloud platform licence for the DG monitoring and workflow application \u2014 licence basis (per DG / per store) TBC", "Annual"),
        ("04", "Connectivity",
         "4G SIM and data plan per store gateway", "Annual"),
        ("05", "Annual support / AMC",
         "Software support and hardware AMC after the warranty period", "Annual"),
        ("06", "Optional  \u00b7  Automated reports",
         "Scheduled report generation and distribution \u2014 schedule and recipients to be finalised", "One-time \u00b7 optional"),
    ]
    rows = [hdr]
    heights = [0.26]
    for n, item, desc, typ in rows_data:
        opt = n == "06"
        dp = para(run(desc, FONT_BODY, 6.4, BODY), lnspc=7.6)
        ip = para(run(item, FONT_BODY_SB, 6.8, CIDER_700 if opt else HEADING), lnspc=7.8)
        h = max(para_height(dp, cols[2] - 0.14), para_height(ip, cols[1] - 0.14)) + 0.14
        heights.append(max(h, 0.34))
        rows.append([
            dict(paras=[para(run(n, FONT_HEAD, 7.5, CIDER_700 if opt else AZURE), align="ctr", lnspc=8)], fill=CIDER_050 if opt else None),
            dict(paras=[ip], fill=CIDER_050 if opt else None),
            dict(paras=[dp], fill=CIDER_050 if opt else None),
            dict(paras=[para(run(typ, FONT_BODY_SB, 6.2, SECOND), align="ctr", lnspc=7)], fill=CIDER_050 if opt else None),
            dict(paras=[para(run("", FONT_BODY, 6.4, BODY), align="ctr", lnspc=7)], fill=CIDER_050 if opt else None),
        ])
    S.append(table(ids, "Commercial table", 0.30, top, cols, rows, heights, dict(border=N200)))
    tbl_bottom = top + sum(heights)

    # summary boxes
    sy = tbl_bottom + 0.26
    bw = (9.40 - 0.12) / 2
    boxes = [("One-time total", "Hardware supply & installation  +  Software development & implementation", "wallet"),
             ("Annual recurring total", "IOsense platform licence  +  Connectivity  +  Annual support / AMC", "repeat")]
    for i, (lab, items, icn) in enumerate(boxes):
        x = 0.30 + i * (bw + 0.12)
        S.append(card(ids, "Summary box", x, sy, bw, 0.62, fill=N050, line=N200))
        S.append(rect(ids, "Summary icon box", x + 0.12, sy + 0.16, 0.30, 0.30, fill=WHITE, line=N300, line_w=0.5, radius=0.05))
        S.append(icon(ids, icn, x + 0.195, sy + 0.235, 0.15, AZURE))
        S.append(textbox(ids, "Summary label", x + 0.54, sy + 0.12, bw - 2.0, 0.4,
                         [para(run(lab, FONT_BODY_SB, 7.4, HEADING), lnspc=8.5),
                          para(run(items, FONT_BODY, 6.3, SECOND), lnspc=7.4, spc_before=2)]))
        S.append(rect(ids, "Amount box", x + bw - 1.45, sy + 0.13, 1.33, 0.36, fill=WHITE, line=N300, line_w=0.5, radius=0.05))
        S.append(textbox(ids, "Amount placeholder", x + bw - 1.45, sy + 0.13, 1.33, 0.36,
                         [para(run("Amount", FONT_BODY, 6.2, TERT), align="ctr", lnspc=6.5)], anchor="ctr"))

    # notes
    ny = sy + 0.62 + 0.14
    notes = [("cpu", "Hardware quantities to be confirmed against the final store and DG count; existing DG controllers are read, not replaced."),
             ("receipt", "Taxes, payment terms and validity to be stated with the amounts."),
             ("life-buoy", "Warranty period, hardware AMC start, licence basis and post go-live support duration to be confirmed.")]
    nx = 0.30
    nw = 9.40 / 3
    for icn, t in notes:
        S.append(icon(ids, icn, nx + 0.02, ny + 0.01, 0.13, SECOND))
        p = para(run(t, FONT_BODY, 6.2, SECOND), lnspc=7.3)
        S.append(textbox(ids, "Note", nx + 0.22, ny, nw - 0.35, para_height(p, nw - 0.35), [p]))
        nx += nw
    print(f"  s12: table to {tbl_bottom:.2f}, notes at {ny:.2f}")

    S.append(footer(ids, FOOTER))
    return slide_xml(S)
