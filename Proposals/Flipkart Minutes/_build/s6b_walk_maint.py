from dml import *
from common import *
from ui import *
from walk import *


def setting_row(ids, x, y, w, label, value, on=True):
    return [toggle(ids, x, y + 0.03, on=on, w=0.26, h=0.14),
            ptext(ids, x + 0.34, y, w - 0.34 - 0.72, 0.20, label, size=5.8, color=P_TXT, sb=True, anchor="ctr", lnspc=6.2),
            rect(ids, "Value box", x + w - 0.70, y - 0.01, 0.70, 0.22, fill=WHITE, line=P_LINE2, line_w=0.5, radius=0.03),
            ptext(ids, x + w - 0.70, y - 0.01, 0.70, 0.22, value, size=5.8, color=P_TXT, sb=True, align="ctr", anchor="ctr")]


def build():
    ids = Ids()
    S = [header(ids, "WORKFLOW 02  ·  PREVENTIVE & BREAKDOWN MAINTENANCE", "How It Works",
                "Three screens: the rules set per DG, the work order they raise, and the AMC vendor closing it on a phone.",
                badge="02", badge_fill=DARK)]
    S.append(sample_chip(ids))

    S += step_header(ids, 0, 1, "Maintenance due", "Super Admin", "shield-check")
    S += step_header(ids, 1, 2, "Work order raised", "System", "cpu")
    S += step_header(ids, 2, 3, "Vendor submits", "AMC vendor", "hard-hat")
    S += arrows(ids)

    # ------------------------------------------------------------ screen 1: settings + due
    x, w = COLS[0]
    fr, (cx, cy, cw, ch) = browser_frame(ids, x, FRAME_Y, w, FRAME_H, "app.iosense.io/dg/blr-014/dg-01", "DG Maintenance", "Super Admin")
    S += fr
    yy = cy
    ch1 = 1.02
    S.append(ui_card(ids, cx, yy, cw, ch1))
    S.append(ptext(ids, cx + 0.12, yy + 0.10, cw - 0.24, 0.16, "Preventive maintenance triggers", size=6.4, color=P_TXT, sb=True, lnspc=6.8))
    S += setting_row(ids, cx + 0.12, yy + 0.36, cw - 0.24, "Running-hours limit", "250 h")
    S += setting_row(ids, cx + 0.12, yy + 0.68, cw - 0.24, "Fixed period", "90 days")
    yy += ch1 + 0.16
    tw_ = (cw - 0.10) / 2
    S.append(kpi_tile(ids, cx, yy, tw_, 0.62, "Hours since last PM", "244", "h", bar=244 / 250, bar_color=P_NOT, fill=WHITE, line_c=P_LINE))
    S.append(kpi_tile(ids, cx + tw_ + 0.10, yy, tw_, 0.62, "Next PM due in", "6", "h", value_color=P_NOT7, fill=WHITE, line_c=P_LINE))
    yy += 0.62 + 0.16
    ab, ah = alert_banner(ids, cx, yy, cw, "Preventive maintenance due — 250 h reached",
                          "Maintenance work order MWO-0217 created", tone="notice", icon_name="bell-ring", size=6.4)
    S.append(ab)

    # ------------------------------------------------------------ screen 2: work order
    x, w = COLS[1]
    fr, (cx, cy, cw, ch) = browser_frame(ids, x, FRAME_Y, w, FRAME_H, "app.iosense.io/work-orders/MWO-0217", "Work orders", "Central User")
    S += fr
    S.append(prich(ids, cx, cy + 0.02, cw - 0.95, 0.20, [("MWO-0217", True, P_TXT), ("   Preventive", False, P_TXT2)], size=8.0, anchor="ctr", lnspc=8.6))
    b, bw = badge(ids, 0, 0, "Assigned", "primary", intense=True, size=5.4, h=0.17)
    b, bw = badge(ids, cx + cw - bw, cy + 0.05, "Assigned", "primary", intense=True, size=5.4, h=0.17)
    S.append(b)
    yy = cy + 0.32
    dh = 0.92
    S.append(ui_card(ids, cx, yy, cw, dh))
    fields = [("DG & store", "DG-01 · BLR-014"), ("Trigger", "Running hours · 250 h"),
              ("AMC vendor", "GenServ Engineers"), ("SPOC", "A. Mehta")]
    fw = (cw - 0.24 - 0.10) / 2
    for i, (lab, val) in enumerate(fields):
        r, c = divmod(i, 2)
        fx = cx + 0.12 + c * (fw + 0.10)
        fy = yy + 0.12 + r * 0.38
        S.append(ptext(ids, fx, fy, fw, 0.12, lab, size=5.2, color=P_TXT3, lnspc=5.4))
        S.append(ptext(ids, fx, fy + 0.14, fw, 0.16, val, size=6.4, color=P_TXT, sb=True, lnspc=6.8, wrap=False))
    yy += dh + 0.22
    st, sh = stepper(ids, cx + 0.06, yy, cw - 0.12, ["Created", "Assigned", "Acknowledged", "In progress", "Submitted", "Completed"],
                     done=2, current=2, size=4.4)
    S.append(st)
    yy += sh + 0.22
    S.append(icon(ids, "siren", cx, yy + 0.015, 0.14, P_NEG))
    S.append(prich(ids, cx + 0.20, yy, cw - 0.20, 0.18,
                   [("Breakdowns  ", True, P_TXT), ("raised in the platform by the store user", False, P_TXT2)], size=6.0, anchor="ctr"))
    yy += 0.24
    S.append(rect(ids, "Next strip", cx, yy, cw, 0.26, fill=P_INF_SUB, radius=0.04))
    S.append(icon(ids, "move-right", cx + 0.10, yy + 0.06, 0.14, P_INF7))
    S.append(ptext(ids, cx + 0.30, yy, cw - 0.40, 0.26, "Next: the AMC vendor acknowledges and attends", size=6.0, color=P_INF7, anchor="ctr"))

    # ------------------------------------------------------------ screen 3: AMC vendor phone
    x, w = COLS[2]
    pw = 1.62
    px = x + (w - pw) / 2
    fr, (cx, cy, cw, ch) = phone_frame(ids, px, FRAME_Y, pw, FRAME_H, "My work orders", "AMC Vendor SPOC · GenServ Engineers")
    S += fr
    S.append(ui_card(ids, cx, cy, cw, 0.48))
    S.append(prich(ids, cx + 0.09, cy + 0.05, cw - 0.18, 0.14, [("MWO-0217", True, P_TXT), ("  ·  Preventive", False, P_TXT2)], size=5.8, lnspc=6.2))
    S.append(ptext(ids, cx + 0.09, cy + 0.19, cw - 0.18, 0.12, "DG-01 · BLR-014 · 250 h reached", size=4.8, color=P_TXT2, lnspc=5.2))
    b, bw = badge(ids, cx + 0.09, cy + 0.32, "In progress", "information", size=4.6, h=0.13, icon_name="wrench")
    S.append(b)
    yy = cy + 0.56
    f, fh = input_field(ids, cx, yy, cw, "Action taken", "Oil & filter change", required=True, h=0.22)
    S += f
    yy += fh + 0.07
    f, fh = input_field(ids, cx, yy, cw, "Parts replaced", "Oil filter, fuel filter", h=0.22)
    S += f
    yy += fh + 0.07
    S.append(checkrow(ids, cx, yy, "Operational clearance given", size=5.4))
    yy += 0.17
    S.append(upload_zone(ids, cx, yy, cw, "Add proof", attached="service-report.pdf", h=0.26))
    yy += 0.26 + 0.06
    S.append(button(ids, cx, yy, cw, "Submit maintenance", variant="primary", icon_name="send", size=5.6, h=0.24))

    # ------------------------------------------------------------ captions
    caps = [("Rules set once per DG.", "Running-hours limit or fixed period — whichever comes first raises the work order."),
            ("Raised and assigned.", "Preventive from the trigger, breakdown from the store; routed to the AMC vendor."),
            ("Vendor closes it.", "Action taken, parts replaced, clearance and proof, submitted from a phone.")]
    for i, (lead, txt) in enumerate(caps):
        xml, h = caption(ids, i, lead, txt)
        S.append(xml)

    S.append(footer(ids, FOOTER))
    return slide_xml(S)
