from dml import *
from common import *
from ui import *
from walk import *


def build():
    ids = Ids()
    S = [header(ids, "WORKFLOW 01  ·  FUEL MONITORING & VENDOR REFILLING", "How It Works",
                "Three screens: the alert the store sees, the work order the system raises, and the vendor closing it on a phone.",
                badge="01")]
    S.append(sample_chip(ids))

    S += step_header(ids, 0, 1, "Low-fuel alert", "Store User")
    S += step_header(ids, 1, 2, "Work order assigned", "System", "cpu")
    S += step_header(ids, 2, 3, "Vendor submits", "Vendor SPOC", "user-check")
    S += arrows(ids)

    # ------------------------------------------------------------ screen 1: dashboard + alert
    x, w = COLS[0]
    fr, (cx, cy, cw, ch) = browser_frame(ids, x, FRAME_Y, w, FRAME_H, "app.iosense.io/dg/blr-014", "DG Monitoring", "Store User")
    S += fr
    yy = cy
    S.append(ui_card(ids, cx, yy, cw, 1.27))
    S.append(prich(ids, cx + 0.12, yy + 0.10, cw - 1.0, 0.18, [("DG-01", True, P_TXT), ("   BLR-014 · Bengaluru", False, P_TXT2)], size=7.0, anchor="ctr"))
    b, bw = badge(ids, 0, 0, "Running", "positive", size=5.4, h=0.17, icon_name="circle-dot")
    b, bw = badge(ids, cx + cw - 0.12 - bw, yy + 0.12, "Running", "positive", size=5.4, h=0.17, icon_name="circle-dot")
    S.append(b)
    S.append(divider(ids, cx + 0.12, yy + 0.36, cw - 0.24))
    tw_ = (cw - 0.24 - 0.10) / 2
    S.append(kpi_tile(ids, cx + 0.12, yy + 0.46, tw_, 0.66, "Fuel level", "14", "%", value_color=P_NEG, bar=0.14, bar_color=P_NEG))
    S.append(kpi_tile(ids, cx + 0.12 + tw_ + 0.10, yy + 0.46, tw_, 0.66, "Estimated fuel", "168", "L"))
    yy += 1.27 + 0.20
    ab, ah = alert_banner(ids, cx, yy, cw, "Low fuel — below the 20 % limit for 15 minutes",
                          "Alert raised · refill work order WO-1042 created", tone="negative", icon_name="triangle-alert", size=6.4)
    S.append(ab)
    yy += ah + 0.20
    S.append(button(ids, cx, yy, 1.55, "Raise refill work order", variant="secondary", icon_name="square-pen", size=5.6, h=0.24))
    S.append(ptext(ids, cx + 1.64, yy, cw - 1.64, 0.24, "Manual trigger, any time", size=5.4, color=P_TXT3, anchor="ctr", lnspc=6))

    # ------------------------------------------------------------ screen 2: work order
    x, w = COLS[1]
    fr, (cx, cy, cw, ch) = browser_frame(ids, x, FRAME_Y, w, FRAME_H, "app.iosense.io/work-orders/WO-1042", "Work orders", "Central User")
    S += fr
    S.append(prich(ids, cx, cy + 0.02, cw - 0.85, 0.20, [("WO-1042", True, P_TXT), ("   Refill", False, P_TXT2)], size=8.0, anchor="ctr", lnspc=8.6))
    b, bw = badge(ids, 0, 0, "Assigned", "primary", intense=True, size=5.4, h=0.17)
    b, bw = badge(ids, cx + cw - bw, cy + 0.05, "Assigned", "primary", intense=True, size=5.4, h=0.17)
    S.append(b)
    yy = cy + 0.32
    dh = 0.92
    S.append(ui_card(ids, cx, yy, cw, dh))
    fields = [("DG & store", "DG-01 · BLR-014"), ("Trigger", "Low fuel · 14 %"),
              ("Vendor", "FuelCo Logistics"), ("SPOC", "R. Kumar")]
    fw = (cw - 0.24 - 0.10) / 2
    for i, (lab, val) in enumerate(fields):
        r, c = divmod(i, 2)
        fx = cx + 0.12 + c * (fw + 0.10)
        fy = yy + 0.12 + r * 0.38
        S.append(ptext(ids, fx, fy, fw, 0.12, lab, size=5.2, color=P_TXT3, lnspc=5.4))
        S.append(ptext(ids, fx, fy + 0.14, fw, 0.16, val, size=6.4, color=P_TXT, sb=True, lnspc=6.8, wrap=False))
    yy += dh + 0.22
    st, sh = stepper(ids, cx + 0.06, yy, cw - 0.12, ["Created", "Assigned", "Acknowledged", "Refueling", "Submitted", "Completed"],
                     done=2, current=2, size=4.4)
    S.append(st)
    yy += sh + 0.22
    S.append(icon(ids, "send", cx, yy + 0.015, 0.14, P_BRAND))
    S.append(prich(ids, cx + 0.20, yy, cw - 0.20, 0.18,
                   [("Notified  ", True, P_TXT), ("email · WhatsApp · in-app", False, P_TXT2)], size=6.0, anchor="ctr"))
    yy += 0.24
    S.append(rect(ids, "Next strip", cx, yy, cw, 0.26, fill=P_INF_SUB, radius=0.04))
    S.append(icon(ids, "move-right", cx + 0.10, yy + 0.06, 0.14, P_INF7))
    S.append(ptext(ids, cx + 0.30, yy, cw - 0.40, 0.26, "Next: the vendor SPOC acknowledges and refuels", size=6.0, color=P_INF7, anchor="ctr"))

    # ------------------------------------------------------------ screen 3: vendor phone
    x, w = COLS[2]
    pw = 1.62
    px = x + (w - pw) / 2
    fr, (cx, cy, cw, ch) = phone_frame(ids, px, FRAME_Y, pw, FRAME_H, "My work orders", "Vendor SPOC · FuelCo Logistics")
    S += fr
    S.append(ui_card(ids, cx, cy, cw, 0.54))
    S.append(prich(ids, cx + 0.09, cy + 0.07, cw - 0.18, 0.14, [("WO-1042", True, P_TXT), ("  ·  Refill", False, P_TXT2)], size=5.8, lnspc=6.2))
    S.append(ptext(ids, cx + 0.09, cy + 0.22, cw - 0.18, 0.12, "DG-01 · BLR-014, Bengaluru", size=4.8, color=P_TXT2, lnspc=5.2))
    b, bw = badge(ids, cx + 0.09, cy + 0.37, "Acknowledged", "positive", size=4.6, h=0.13, icon_name="check")
    S.append(b)
    yy = cy + 0.62
    f, fh = input_field(ids, cx, yy, cw, "Litres added", "380", required=True, h=0.22)
    S += f
    yy += fh + 0.08
    f, fh = input_field(ids, cx, yy, cw, "Refuelling date", "12 Sep 2026", icon_name="calendar", h=0.22)
    S += f
    yy += fh + 0.08
    S.append(upload_zone(ids, cx, yy, cw, "Add proof (optional)", attached="invoice.jpg", h=0.30))
    yy += 0.30 + 0.09
    S.append(button(ids, cx, yy, cw, "Submit refuelling", variant="primary", icon_name="send", size=5.6, h=0.24))

    # ------------------------------------------------------------ captions
    caps = [("Fuel drops below the limit.", "One alert and one refill work order — or the store raises one on demand."),
            ("Assigned automatically.", "Unique work order ID, routed to the mapped vendor SPOC and notified."),
            ("Vendor closes it.", "Acknowledge, refuel, enter litres and submit with proof from a phone.")]
    for i, (lead, txt) in enumerate(caps):
        xml, h = caption(ids, i, lead, txt)
        S.append(xml)

    S.append(footer(ids, FOOTER))
    return slide_xml(S)
