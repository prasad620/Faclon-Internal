"""Billing & invoicing walk-through — the money leg of Workflow 01, plus the AMC invoice basis.

Follows SRS §18 / §21 and Flipkart §5: the vendor picks the period and method, the platform
renders unbilled completed transactions with line items, the vendor raises the invoice, the
work orders lock and the payload posts to Oracle Fusion.
"""
from dml import *
from common import *
from ui import *
from walk import COLS, step_header, caption, arrows, sample_chip

FY, FH = 1.40, 2.72
CAP_Y = FY + FH + 0.10
BAND_Y = 4.56


def build():
    ids = Ids()
    S = [header(ids, "WORKFLOW 01  ·  TRANSACTIONS, BILLING & ORACLE FUSION", "Invoicing Walk-through",
                "Every completed work order becomes a billable transaction; the vendor raises one invoice against them and it posts to Oracle Fusion.",
                badge="01")]
    S.append(sample_chip(ids))

    S += step_header(ids, 0, 1, "Eligible transactions", "Vendor SPOC", "user-check")
    S += step_header(ids, 1, 2, "Invoice raised", "Vendor SPOC", "receipt")
    S += step_header(ids, 2, 3, "Locked & posted", "System", "cpu")
    S += arrows(ids, FY, FH)

    # ---------------------------------------------------------- screen 1: eligible transactions
    x, w = COLS[0]
    fr, (cx, cy, cw, ch) = browser_frame(ids, x, FY, w, FH, "app.iosense.io/billing/new", "Billing", "Vendor SPOC")
    S += fr
    tb, th = tabs(ids, cx, cy, cw, ["Refilling", "AMC"], selected=0, size=5.4)
    S.append(tb)
    yy = cy + th + 0.12
    fx = cx
    for lab in ["Period: Sep 2026", "Method: Per litre"]:
        c, fw_ = filter_chip(ids, fx, yy, lab, size=4.8, h=0.18)
        S.append(c)
        fx += fw_ + 0.08
    yy += 0.24
    widths = [0.62, 0.52, 0.42, 0.52, 0.62]
    scale = cw / sum(widths)
    widths = [v * scale for v in widths]
    rows = [["WO-1042", "BLR-014", "380 L", "Per litre", "12 Sep"],
            ["WO-1039", "BLR-021", "420 L", "Per litre", "11 Sep"],
            ["WO-1036", "BLR-007", "300 L", "Per litre", "10 Sep"],
            ["WO-1031", "HYD-002", "360 L", "Per litre", "09 Sep"]]
    tbl, tblh = ui_table(ids, cx, yy, widths, ["WORK ORDER", "STORE", "LITRES", "BASIS", "DATE"], rows, size=4.8, row_h=0.19)
    S.append(tbl)
    yy += tblh + 0.08
    S.append(icon(ids, "filter", cx, yy + 0.01, 0.12, P_TXT3))
    S.append(ptext(ids, cx + 0.18, yy - 0.01, cw - 0.18, 0.16,
                   "Already-billed work orders are excluded automatically", size=5.2, color=P_TXT3, anchor="ctr"))
    yy += 0.20
    S.append(button(ids, cx, yy, cw, "Review line items", variant="primary", icon_name="arrow-right", size=5.6, h=0.22))

    # ---------------------------------------------------------- screen 2: invoice
    x, w = COLS[1]
    fr, (cx, cy, cw, ch) = browser_frame(ids, x, FY, w, FH, "app.iosense.io/billing/INV-2026-204", "Billing", "Vendor SPOC")
    S += fr
    S.append(prich(ids, cx, cy + 0.02, cw - 0.85, 0.20,
                   [("Invoice", True, P_TXT), ("   Sep 2026 · 4 work orders", False, P_TXT2)], size=7.6, anchor="ctr", lnspc=8.2))
    b, bw = badge(ids, 0, 0, "Draft", "notice", size=5.4, h=0.17)
    b, bw = badge(ids, cx + cw - bw, cy + 0.05, "Draft", "notice", size=5.4, h=0.17)
    S.append(b)
    yy = cy + 0.26
    items = [("Refilling charges", "4 refuelling events", "₹ 4,800"),
             ("Fuel charges", "1,460 L × rate per litre", "₹ 1,40,890")]
    for lab, basis, amt in items:
        S.append(ui_card(ids, cx, yy, cw, 0.36))
        S.append(ptext(ids, cx + 0.10, yy + 0.05, cw - 1.20, 0.14, lab, size=5.6, color=P_TXT, sb=True, lnspc=6.0))
        S.append(ptext(ids, cx + 0.10, yy + 0.19, cw - 1.20, 0.13, basis, size=4.8, color=P_TXT3, lnspc=5.2))
        S.append(ptext(ids, cx + cw - 1.10, yy, 1.00, 0.36, amt, size=6.4, color=P_TXT, sb=True, align="r", anchor="ctr"))
        yy += 0.36 + 0.05
    S.append(rect(ids, "Total row", cx, yy, cw, 0.32, fill=P_BRAND_SUB, radius=0.04))
    S.append(ptext(ids, cx + 0.10, yy, 1.4, 0.32, "Invoice amount", size=5.8, color=P_BRAND, sb=True, anchor="ctr"))
    S.append(ptext(ids, cx + cw - 1.10, yy, 1.00, 0.32, "₹ 1,45,690", size=7.0, color=P_BRAND, sb=True, align="r", anchor="ctr"))
    yy += 0.32 + 0.08
    f, fh_ = input_field(ids, cx, yy, cw * 0.46, "Invoice number", "FC/26-27/0412", required=True, h=0.20)
    S += f
    S.append(upload_zone(ids, cx + cw * 0.50, yy + 0.12, cw * 0.50, "Attach invoice PDF", attached="INV-204.pdf", h=0.20))
    yy += fh_ + 0.06
    S.append(button(ids, cx, yy, cw, "Submit invoice", variant="primary", icon_name="send", size=5.6, h=0.22))

    # ---------------------------------------------------------- screen 3: locked & posted
    x, w = COLS[2]
    fr, (cx, cy, cw, ch) = browser_frame(ids, x, FY, w, FH, "app.iosense.io/billing/INV-2026-204", "Billing", "Central User")
    S += fr
    S.append(prich(ids, cx, cy + 0.02, cw - 1.15, 0.20, [("INV-2026-204", True, P_TXT)], size=7.6, anchor="ctr", lnspc=8.2))
    b, bw = badge(ids, 0, 0, "Posted to Fusion", "positive", intense=True, size=5.4, h=0.17, icon_name="check")
    b, bw = badge(ids, cx + cw - bw, cy + 0.05, "Posted to Fusion", "positive", intense=True, size=5.4, h=0.17, icon_name="check")
    S.append(b)
    yy = cy + 0.28
    dh = 0.88
    S.append(ui_card(ids, cx, yy, cw, dh))
    fields = [("Vendor", "FuelCo Logistics"), ("Billing period", "Sep 2026"),
              ("Total refill charges", "₹ 4,800"), ("Total fuel charges", "₹ 1,40,890"),
              ("Invoice amount", "₹ 1,45,690"), ("Submitted", "01 Oct 2026 · 11:20")]
    fw = (cw - 0.24 - 0.10) / 2
    for i, (lab, val) in enumerate(fields):
        r, c = divmod(i, 2)
        fx = cx + 0.12 + c * (fw + 0.10)
        fy = yy + 0.06 + r * 0.28
        S.append(ptext(ids, fx, fy, fw, 0.11, lab, size=4.8, color=P_TXT3, lnspc=5.0))
        S.append(ptext(ids, fx, fy + 0.12, fw, 0.15, val, size=6.0, color=P_TXT, sb=True, lnspc=6.4, wrap=False))
    yy += dh + 0.10
    S.append(rect(ids, "Lock strip", cx, yy, cw, 0.28, fill=P_BG2, radius=0.04))
    S.append(icon(ids, "lock", cx + 0.10, yy + 0.08, 0.13, P_TXT2))
    S.append(prich(ids, cx + 0.30, yy, cw - 0.40, 0.28,
                   [("4 work orders locked", True, P_TXT), ("  ·  cannot be billed again", False, P_TXT2)], size=5.4, anchor="ctr"))
    yy += 0.28 + 0.07
    S.append(rect(ids, "Fusion strip", cx, yy, cw, 0.28, fill=P_POS_SUB, radius=0.04))
    S.append(icon(ids, "plug-zap", cx + 0.10, yy + 0.08, 0.13, P_POS7))
    S.append(prich(ids, cx + 0.30, yy, cw - 0.40, 0.28,
                   [("Oracle Fusion", True, P_POS7), ("  ·  API response logged on the audit trail", False, P_POS7)], size=5.4, anchor="ctr"))

    # ---------------------------------------------------------- captions
    caps = [("Vendor picks period and basis.", "The platform lists unbilled, completed work orders with their billing basis."),
            ("One invoice, itemised.", "Refilling charge per event plus the fuel or running-hours charge, from the vendor's rate card."),
            ("Locked and posted.", "Work orders can never be billed twice; the payload goes to Oracle Fusion via API.")]
    for i, (lead, txt) in enumerate(caps):
        xml, h = caption(ids, i, lead, txt, y=CAP_Y)
        S.append(xml)

    # ---------------------------------------------------------- invoice-type band
    bh = 5.20 - BAND_Y
    hw = (9.40 - 0.14) / 2
    blocks = [
        ("fuel", "Refilling invoice", AZURE, AZURE_050, AZURE_200,
         "Refill charge per refuelling event + fuel or running-hours charge",
         ["Per Litre Fuel Rate", "Running Hours Rate"], "azure", None),
        ("wrench", "AMC invoice", CIDER_700, CIDER_050, CIDER,
         "Maintenance work orders in the period, at the fixed contract rate per DG",
         ["Fixed Rate AMC"], "cider", "Proposed · to confirm"),
    ]
    for i, (icn, title, col, fill, line_c, desc, chips, ctone, note) in enumerate(blocks):
        bx = 0.30 + i * (hw + 0.14)
        S.append(card(ids, "Invoice type", bx, BAND_Y, hw, bh, fill=fill, line=line_c))
        S.append(rect(ids, "Icon tile", bx + 0.12, BAND_Y + 0.13, 0.30, 0.30, fill=WHITE, radius=0.05))
        S.append(icon(ids, icn, bx + 0.19, BAND_Y + 0.20, 0.16, col))
        S.append(textbox(ids, "Type title", bx + 0.52, BAND_Y + 0.11, hw - 0.64, 0.34,
                         [para(run(title, FONT_BODY_SB, 7.6, HEADING), lnspc=8.6),
                          para(run(desc, FONT_BODY, 6.4, SECOND), lnspc=7.6, spc_before=1.5)]))
        cy_ = BAND_Y + bh - 0.24
        cxs, _ = chips_row(ids, bx + 0.52, cy_, chips, ctone, max_w=hw - 0.64, h=0.16, size=5.8)
        S += cxs
        if note:
            nx, nw_ = chip(ids, 0, 0, note, "cider-solid", icon_name="circle-help", h=0.16, size=5.8)
            nx, nw_ = chip(ids, bx + hw - 0.12 - nw_, cy_, note, "cider-solid", icon_name="circle-help", h=0.16, size=5.8)
            S.append(nx)
    print(f"  s5c: frames {FY:.2f}–{FY + FH:.2f}, captions {CAP_Y:.2f}, band {BAND_Y:.2f}–{BAND_Y + bh:.2f}")

    S.append(footer(ids, FOOTER))
    return slide_xml(S)
