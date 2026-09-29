from dml import *
from common import *

GROUPS = [
    ("Hardware & site", "cpu", [
        ("DG controller make / model, protocol and Modbus register map per DG \u2014 for the gateway integration", ["01", "02"]),
        ("Store and DG count for the rollout \u2014 drives hardware quantities, licence basis and installation plan", ["01", "02"]),
        ("Site readiness at each store: power supply, mounting space and network / signal availability", ["01", "02"]),
        ("Estimated fuel volume (L): read from the controller or derived on IOsense from tank capacity", ["01"]),
    ]),
    ("Business rules", "sliders-horizontal", [
        ("Low-fuel limits per level and the waiting time before an alert is raised", ["01"]),
        ("PM running-hours limits and fixed maintenance periods per DG (e.g. 250 / 500 h)", ["02"]),
        ("Work-order status names \u2014 to be finalised during UI design", ["01", "02"]),
    ]),
    ("Billing & Oracle Fusion", "receipt", [
        ("Fusion interface specification: endpoint, authentication, codes and payload format", ["01"]),
        ("Rate cards: diesel rate, running-hours rate and vendor refilling charges; billing type per site", ["01"]),
        ("AMC vendor billing (Fixed Rate AMC in Flipkart\u2019s version) \u2014 not covered by the SRS billing flow", ["02"]),
    ]),
    ("Users, notifications & plan", "users-round", [
        ("User list and roles; vendor and SPOC onboarding \u2014 who creates and maintains the accounts", ["01", "02"]),
        ("WhatsApp Business account, message templates and email sender for the initial notification", ["01", "02"]),
        ("Warranty period, hardware AMC start, post go-live support duration and schedule confirmation", ["01", "02"]),
    ]),
]


def build():
    ids = Ids()
    S = [header(ids, "BOTH WORKFLOWS  ·  NEXT STEPS", "Open Points to Confirm",
                "Items to close with Flipkart before requirement sign-off. Tags show the workflow each point applies to: 01 refilling, 02 maintenance.")]

    top = 1.15
    cw = (9.40 - 0.14) / 2
    n = 1
    # measure each group to size the two columns evenly
    col_y = [top, top]
    for gi, (title, icn, points) in enumerate(GROUPS):
        col = gi % 2
        x = 0.30 + col * (cw + 0.14)
        y = col_y[col]
        parts = []
        parts.append(rect(ids, "Group icon box", x + 0.12, y + 0.12, 0.26, 0.26, fill=CIDER_050, radius=0.05))
        parts.append(icon(ids, icn, x + 0.18, y + 0.18, 0.14, CIDER_700))
        parts.append(textbox(ids, "Group title", x + 0.48, y + 0.12, cw - 0.6, 0.26,
                             [para(run(title, FONT_BODY_SB, 7.6, HEADING), lnspc=8.5)], anchor="ctr"))
        py = y + 0.50
        for text_, tags in points:
            tag_w = 0.19 * len(tags) + 0.04 * (len(tags) - 1)
            tw = cw - 0.12 - 0.34 - tag_w - 0.18
            p = para(run(text_, FONT_BODY, 6.6, BODY), lnspc=7.8)
            ph = para_height(p, tw)
            parts.append(textbox(ids, "Point number", x + 0.12, py, 0.24, ph, [para(run(f"{n:02d}", FONT_HEAD, 7, CIDER_700), lnspc=7.8)]))
            parts.append(textbox(ids, "Point", x + 0.42, py, tw, ph, [p]))
            tx = x + cw - 0.12 - tag_w
            for t in tags:
                fill = AZURE if t == "01" else DARK
                parts.append(rect(ids, "Tag", tx, py + 0.005, 0.19, 0.15, fill=fill, radius=0.03))
                parts.append(textbox(ids, "Tag label", tx, py + 0.005, 0.19, 0.15,
                                     [para(run(t, FONT_BODY_SB, 5.4, WHITE), align="ctr", lnspc=5.4)], anchor="ctr"))
                tx += 0.23
            py += ph + 0.05
            parts.append(line(ids, "Point divider", x + 0.42, py, x + cw - 0.12, py, color=N200, w=0.5))
            py += 0.06
            n += 1
        gh = py - y + 0.04
        S.append(group(ids, "Group " + title, [card(ids, "Group card", x, y, cw, gh)] + parts, x, y, cw, gh))
        col_y[col] = y + gh + 0.12
    # next steps strip
    ny = max(col_y) + 0.02
    nh = 5.25 - ny
    S.append(card(ids, "Next steps", 0.30, ny, 9.40, nh, fill=N050, line=N200))
    S.append(icon(ids, "route", 0.44, ny + nh / 2 - 0.09, 0.18, AZURE))
    S.append(textbox(ids, "Next steps title", 0.70, ny, 1.2, nh,
                     [para(run("Proposed next steps", FONT_BODY_SB, 7.2, HEADING), lnspc=8.2)], anchor="ctr"))
    steps = [("Walk-through of this proposal with Flipkart", "book-open"),
             ("Close the open points and sign off the SRS", "square-check"),
             ("Site survey and hardware order for the first stores", "cpu"),
             ("Kick-off and start of the delivery schedule", "flag")]
    sx = 1.95
    sw = (9.70 - sx - 0.1) / len(steps)
    for i, (t, icn) in enumerate(steps):
        x = sx + i * sw
        S.append(number_badge(ids, x, ny + nh / 2 - 0.10, i + 1, size=0.20, fill=AZURE, font_size=6.5, square=False))
        S.append(textbox(ids, "Step", x + 0.27, ny, sw - 0.4, nh, [para(run(t, FONT_BODY, 6.6, BODY), lnspc=7.6)], anchor="ctr"))
    print(f"  s13: columns end at {col_y[0]:.2f} / {col_y[1]:.2f}; next steps {ny:.2f}–5.25")

    S.append(footer(ids, FOOTER))
    return slide_xml(S)
