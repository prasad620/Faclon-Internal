from dml import *
from common import *


def build():
    ids = Ids()
    S = [header(ids, "DG ONLINE MONITORING  ·  OVERVIEW", "Objective & Business Outcome",
                "Bring every DG onto IOsense, and turn low-fuel and maintenance conditions into vendor work orders "
                "that are tracked from creation to completion.")]

    # column headers
    hy = 1.13
    for x, icn, lab, col in [(1.95, "history", "CURRENT PROCEDURE", SECOND), (4.60, "crosshair", "OBJECTIVE", AZURE),
                             (7.25, "badge-check", "BUSINESS OUTCOME", EMERALD_700)]:
        S.append(icon(ids, icn, x, hy + 0.03, 0.15, col))
        S.append(textbox(ids, "Column header", x + 0.20, hy, 2.2, 0.20,
                         [para(run(lab, FONT_BODY_SB, 6.6, col, spc=82, caps=True), lnspc=6.6)], anchor="ctr"))

    rows = [
        dict(y=1.40, num="01", name="DG Refilling", sub="Fuel monitoring  ·  vendor refuelling", icon="fuel",
             fill=AZURE, divider=AZURE_400, label="WORKFLOW", value="Low-fuel alert → refill work order → invoice",
             current=[("eye", ("Fuel level checked physically ", "at the store; no live view across stores")),
                      ("phone", ("Refill request raised by phone / message; ", "litres and proof tracked offline")),
                      ("file-text", ("No consolidated record ", "of litres, vendor and timing per store for reconciliation"))],
             current_chips=[("No live visibility", "eye")],
             objective=[("activity", ("Monitor every DG live: ", "fuel %, litres, running hours, kWh and operating status")),
                        ("bell-ring", ("Raise one alert and one refill work order ", "when the level stays below the limit for the waiting time")),
                        ("user-check", ("Assign to the primary refilling vendor's SPOC: ", "acknowledge, refuel, enter litres, upload proof, submit"))],
             outcome=[("Refills triggered by data: ", "one alert, one work order, no duplicates"),
                      ("Every litre on record: ", "quantity, vendor, SPOC and timestamps against one Work Order ID"),
                      ("Store-to-zone visibility: ", "dashboards and downloads by zone, city, store and vendor"),
                      ("Billed from the same record: ", "line items roll into an invoice posted to Oracle Fusion")]),
        dict(y=3.37, num="02", name="DG Maintenance", sub="Preventive  ·  breakdown", icon="wrench",
             fill=DARK, divider=DARK_LINE, label="WORKFLOW", value="Running hours / period / breakdown → maintenance work order",
             current=[("calendar-days", ("Service due tracked manually ", "per DG from hour-meter readings and dates")),
                      ("phone", ("Breakdowns reported by phone; ", "no central view of open jobs or history")),
                      ("history", ("Service history scattered ", "across vendor reports and messages"))],
             current_chips=[("Manual tracking", "calendar-days")],
             objective=[("timer", ("PM due on running-hours limit or fixed period, ", "whichever occurs first — set per DG")),
                        ("triangle-alert", ("Breakdown work order raised in the platform ", "by the store user / maintenance team")),
                        ("clipboard-check", ("AMC vendor SPOC acknowledges, ", "carries out maintenance, submits details and proof"))],
             outcome=[("PM never missed: ", "work order created automatically when a limit or period is reached"),
                      ("Shared visibility: ", "open tickets, PM schedules and repair history for store, central and vendor users"),
                      ("Complete service history per DG: ", "trigger, vendor, timestamps and details"),
                      ("One platform: ", "same work-order logic and access rules for both workflows")]),
    ]

    H = 1.85
    for r in rows:
        y = r["y"]
        # identity panel
        dark = r["fill"] == DARK
        P = [rect(ids, "Panel", 0.30, y, 1.50, H, fill=r["fill"], radius=0.08),
             icon(ids, r["icon"], 0.46, y + 0.17, 0.30, WHITE),
             textbox(ids, "Project number", 1.00, y + 0.10, 0.66, 0.42,
                     [para(run(r["num"], FONT_HEAD, 24, WHITE if not dark else "B1C1D2"), align="r", lnspc=26)], anchor="ctr"),
             textbox(ids, "Project name", 0.46, y + 0.64, 1.25, 0.24, [para(run(r["name"], FONT_HEAD, 11.5, WHITE), lnspc=13)]),
             textbox(ids, "Project station", 0.46, y + 0.88, 1.25, 0.28,
                     [para(run(r["sub"], FONT_BODY, 6.3, "DCE8FE" if not dark else "B1C1D2"), lnspc=7.5)]),
             line(ids, "Divider", 0.46, y + 1.20, 1.64, y + 1.20, color=r["divider"], w=0.5),
             textbox(ids, "Applications label", 0.46, y + 1.28, 1.25, 0.14,
                     [para(run(r["label"], FONT_BODY_SB, 5.5, "B8D0FD" if not dark else "90A5BB", spc=82, caps=True), lnspc=5.5)]),
             textbox(ids, "Applications", 0.46, y + 1.44, 1.25, 0.36, [para(run(r["value"], FONT_BODY_SB, 6.6, WHITE), lnspc=7.9)])]
        S.append(group(ids, f"Workflow {r['num']} identity", P, 0.30, y, 1.50, H))

        # current procedure card
        C = [card(ids, "Current procedure card", 1.93, y, 2.40, H, fill=N050, line=N200)]
        items, ih = item_stack(ids, 2.06, y + 0.15, 2.15, r["current"], icon_color=MUTED, size=7, gap=0.09, lead_color=HEADING)
        C += items
        C.append(line(ids, "Divider", 2.06, y + H - 0.39, 4.20, y + H - 0.39, color=N200, w=0.5))
        cx = 2.06
        for lab, icn in r["current_chips"]:
            xml, w = chip(ids, cx, y + H - 0.30, lab, "crimson", icon_name=icn)
            C.append(xml)
            cx += w + 0.06
        dx, _ = chip(ids, cx, y + H - 0.30, "Draft · for review", "cider", icon_name="pen-line")
        C.append(dx)
        S.append(group(ids, f"Workflow {r['num']} current procedure", C, 1.93, y, 2.40, H))

        S.append(icon(ids, "chevron-right", 4.38, y + 0.85, 0.16, TERT))

        # objective card
        O = [card(ids, "Objective card", 4.58, y, 2.40, H, fill=AZURE_050, line=AZURE_200)]
        items, ih = item_stack(ids, 4.71, y + 0.15, 2.15, r["objective"], icon_color=AZURE, size=7, gap=0.09)
        O += items
        S.append(group(ids, f"Workflow {r['num']} objective", O, 4.58, y, 2.40, H))

        S.append(icon(ids, "chevron-right", 7.03, y + 0.85, 0.16, TERT))

        # business outcome card
        B = [card(ids, "Business outcome card", 7.23, y, 2.47, H, fill=EMERALD_050, line=EMERALD_200)]
        items, ih = item_stack(ids, 7.36, y + 0.15, 2.22, [("circle-check", t) for t in r["outcome"]],
                               icon_color=EMERALD, size=7, gap=0.085)
        B += items
        S.append(group(ids, f"Workflow {r['num']} business outcome", B, 7.23, y, 2.47, H))

    S.append(footer(ids, FOOTER))
    return slide_xml(S)
