from dml import *
from common import *


def device_card(ids, x, y, w, title, sub, icon_name, chips=None, chip_tone="cider", fill=WHITE, line_c=N300, tcol=HEADING,
                scol=MUTED, icol=AZURE, pad=0.07, icon_box=True, min_h=0.0):
    """Device / system card: icon in a tinted square on the left, title + sub, optional chips. Returns (xml, h)."""
    parts = []
    bx = x + pad
    tx = bx + 0.34
    tw = w - pad * 2 - 0.34
    tp = para(run(title, FONT_BODY_SB, 6.6, tcol), lnspc=7.6)
    sp = para(run(sub, FONT_BODY, 6.0, scol), lnspc=7.1, spc_before=1)
    th = para_height(tp, tw) + para_height(sp, tw)
    cy = y + pad
    parts.append(textbox(ids, f"{title} text", tx, cy, tw, th, [tp, sp]))
    cy += th
    if chips:
        cy += 0.05
        cx, ch = chips_row(ids, tx, cy, chips, chip_tone, max_w=tw, h=0.13, size=5.4)
        parts += cx
        cy += ch
    total = max(min_h, cy - y + pad)
    ib = [rect(ids, "Icon box", bx, y + pad, 0.24, 0.24, fill=AZURE_050 if fill == WHITE else "2A3B4F", radius=0.05),
          icon(ids, icon_name, bx + 0.05, y + pad + 0.05, 0.14, icol)]
    bg = card(ids, title, x, y, w, total, fill=fill, line=line_c, radius=0.07)
    return group(ids, title, [bg] + ib + parts, x, y, w, total), total


def link_badge(ids, x, y, n):
    return number_badge(ids, x, y, n, size=0.16, fill=AZURE, font_size=6, square=False)


def build():
    ids = Ids()
    S = [header(ids, "BOTH WORKFLOWS  ·  DEPLOYMENT", "Network Architecture",
                "Faclon supplies the field hardware and the cloud; data flows from each DG to IOsense and out to users, "
                "vendors and Oracle Fusion.")]

    top, zh = 1.22, 2.30
    # ---------------------------------------------------------------- zones
    zones = [(0.30, 2.50, "DARK STORE  ·  PER SITE", "store"), (3.20, 3.20, "IOSENSE CLOUD  ·  FACLON-HOSTED", "cloud"),
             (6.80, 2.90, "USERS & FLIPKART SYSTEMS", "users-round")]
    for zx, zw, lab, icn in zones:
        S.append(rect(ids, "Zone", zx, top, zw, zh, fill=N050, line=N300, line_w=0.75, radius=0.09, dash="dash"))
        S.append(zone_label(ids, zx + 0.12, top + 0.09, lab, icn, w=zw - 0.4))

    # dark store
    zx, zw = 0.30, 2.50
    cx, cw = zx + 0.12, zw - 0.24
    cy = top + 0.33
    xml, h = device_card(ids, cx, cy, cw, "DG + existing controller", "One or more DGs per store, each with its own DG ID", "zap",
                         chips=["Controller make TBC"])
    S.append(xml)
    dg_mid = cy + h / 2
    cy += h + 0.09
    xml, h = device_card(ids, cx, cy, cw, "IoT device + gateway", "Supplied, installed and commissioned by Faclon", "router",
                         chips=["RS-485 / Modbus"], chip_tone="azure")
    S.append(xml)
    gw_mid = cy + h / 2
    gw_top = cy
    cy += h + 0.09
    xml, h = device_card(ids, cx, cy, cw, "Connectivity", "4G SIM and data plan from Faclon", "wifi", chips=["Faclon supplied"], chip_tone="azure")
    S.append(xml)
    # DG → gateway link (vertical, at left)
    S.append(line(ids, "DG link", cx + 0.21, dg_mid + 0.30, cx + 0.21, gw_top, color=AZURE, w=1.0, tail="triangle"))

    # cloud zone
    zx, zw = 3.20, 3.20
    sx, sw = zx + 0.14, zw - 0.28
    sy = top + 0.36
    S.append(card(ids, "Server card", sx, sy, sw, zh - 0.50, fill=WHITE, line=AZURE_200, radius=0.08))
    S.append(rect(ids, "Server icon box", sx + 0.10, sy + 0.10, 0.26, 0.26, fill=AZURE_050, radius=0.05))
    S.append(icon(ids, "server", sx + 0.155, sy + 0.155, 0.15, AZURE))
    S.append(textbox(ids, "Server title", sx + 0.45, sy + 0.09, sw - 0.55, 0.30,
                     [para(run("IOsense cloud", FONT_BODY_SB, 7.2, HEADING), lnspc=8.2),
                      para(run("Hosted and operated by Faclon Labs; accessed over HTTPS", FONT_BODY, 6.2, MUTED), lnspc=7.3, spc_before=1)]))
    ly = sy + 0.50
    S.append(rect(ids, "Layer platform", sx + 0.10, ly, sw - 0.20, 0.30, fill=DARK, radius=0.05))
    S.append(icon(ids, "layers", sx + 0.19, ly + 0.08, 0.14, WHITE))
    S.append(textbox(ids, "Layer label", sx + 0.40, ly, sw - 0.55, 0.30,
                     [para([run("IOsense platform", FONT_BODY_SB, 6.8, WHITE), run("  ·  onboarding, data, dashboards", FONT_BODY, 6.2, "B1C1D2")], lnspc=7)], anchor="ctr"))
    ly += 0.38
    S.append(rect(ids, "Layer app", sx + 0.10, ly, sw - 0.20, 0.30, fill=AZURE, radius=0.05))
    S.append(icon(ids, "app-window", sx + 0.19, ly + 0.08, 0.14, WHITE))
    S.append(textbox(ids, "Layer label", sx + 0.40, ly, sw - 0.55, 0.30,
                     [para([run("DG Fuel Management & Maintenance Application", FONT_BODY_SB, 6.8, WHITE)], lnspc=7)], anchor="ctr"))
    ly += 0.38
    np_ = para(run("Evaluates low-fuel and PM conditions, creates and assigns work orders, sends the initial notification, "
                   "serves dashboards, transaction views and downloads by role.", FONT_BODY, 6.2, SECOND), lnspc=7.4)
    S.append(textbox(ids, "Server note", sx + 0.10, ly, sw - 0.20, para_height(np_, sw - 0.20), [np_]))

    # link 1: gateway → cloud
    S.append(line(ids, "Link 1", cx + cw, gw_mid, sx, gw_mid, color=AZURE, w=1.0, tail="triangle"))
    S.append(link_badge(ids, cx + cw + 0.10, gw_mid - 0.22, 1))
    S.append(textbox(ids, "Link label", cx + cw + 0.05, gw_mid + 0.06, 0.6, 0.12,
                     [para(run("MQTT / HTTPS push", FONT_BODY, 5.6, SECOND), lnspc=5.6)], anchor="t", wrap=False))

    # users zone
    zx, zw = 6.80, 2.90
    ux, uw = zx + 0.12, zw - 0.24
    uy = top + 0.33
    users = [
        ("Flipkart users", "Store · Central · Super Admin · maintenance team", "users-round", None, "neutral", 2),
        ("Vendor SPOCs", "Refilling & AMC vendors · mobile-responsive web", "user-check", None, "neutral", 3),
        ("Notifications", "Email · WhatsApp · in-app", "bell", ["WhatsApp Business account TBC"], "cider", 4),
        ("Oracle Fusion", "Invoice payload via API", "plug-zap", ["Interface spec TBC"], "cider", 5),
    ]
    for t, s_, icn, chips, tone, n in users:
        xml, h = device_card(ids, ux, uy, uw, t, s_, icn, chips=chips, chip_tone=tone)
        S.append(xml)
        mid = uy + h / 2
        tail = "triangle" if n in (4, 5) else None
        head = "triangle" if n in (2, 3) else None
        S.append(line(ids, f"Link {n}", sx + sw, mid, ux, mid, color=AZURE, w=1.0, tail=tail, head=head))
        S.append(link_badge(ids, sx + sw + 0.08, mid - 0.19, n))
        uy += h + 0.05

    # ---------------------------------------------------------------- table
    ty = top + zh + 0.08
    cols = [("REF", 0.40), ("LINK / COMPONENT", 1.70), ("WHAT FLOWS", 2.95), ("CONFIGURATION TO SET UP", 3.05), ("STATUS", 1.30)]
    tx = 0.30
    hh = 0.20
    S.append(rect(ids, "Table header", tx, ty, 9.40, hh, fill=N100))
    x = tx
    for lab, w in cols:
        S.append(textbox(ids, "Th", x + 0.06, ty, w - 0.1, hh, [para(run(lab, FONT_BODY_SB, 5.6, SECOND, spc=60, caps=True), lnspc=5.6)], anchor="ctr"))
        x += w
    rows = [
        ("1", "DG controller → IoT device", "Fuel %, litres, running hours, kWh, operating status per DG",
         "Controller make / model and Modbus register map per DG", "TBC"),
        ("2", "Gateway → IOsense cloud", "Buffered DG data pushed over MQTT / HTTPS on the Faclon 4G SIM",
         "Supplied, installed and commissioned by Faclon", "Defined"),
        ("3", "Flipkart & vendor users ↔ app", "Dashboards, masters, work orders, vendor submissions, downloads",
         "User list and roles; store, DG, vendor and SPOC masters", "TBC"),
        ("4", "Application → notifications", "Initial work-order notification",
         "Email sender; WhatsApp Business account and templates", "TBC"),
        ("5", "Application → Oracle Fusion", "Invoice payload with refill and fuel line items; API response logged",
         "Fusion API spec, authentication, codes and payload", "TBC"),
        ("•", "Hosting", "IOsense platform and the application",
         "Faclon-hosted cloud; HTTPS access over the internet", "Defined"),
        ("•", "Data retention", "Telemetry, transactions, audit history",
         "IOsense platform data-retention policy", "Defined"),
    ]
    ry = ty + hh
    for ref, comp, flows, conf, status in rows:
        # row height from the tallest cell
        pf = para(run(flows, FONT_BODY, 6.2, BODY), lnspc=7.4)
        pc = para(run(conf, FONT_BODY, 6.2, BODY), lnspc=7.4)
        pl = para(run(comp, FONT_BODY_SB, 6.4, HEADING), lnspc=7.6)
        rh = max(para_height(pf, cols[2][1] - 0.12), para_height(pc, cols[3][1] - 0.12), para_height(pl, cols[1][1] - 0.12)) + 0.09
        rh = max(rh, 0.195)
        x = tx
        if ref == "•":
            S.append(ellipse(ids, "Dot", x + 0.12, ry + rh / 2 - 0.03, 0.06, 0.06, fill=N300))
        else:
            S.append(link_badge(ids, x + 0.07, ry + rh / 2 - 0.08, ref))
        x += cols[0][1]
        S.append(textbox(ids, "Td", x + 0.06, ry, cols[1][1] - 0.12, rh, [pl], anchor="ctr"))
        x += cols[1][1]
        S.append(textbox(ids, "Td", x + 0.06, ry, cols[2][1] - 0.12, rh, [pf], anchor="ctr"))
        x += cols[2][1]
        S.append(textbox(ids, "Td", x + 0.06, ry, cols[3][1] - 0.12, rh, [pc], anchor="ctr"))
        x += cols[3][1]
        cxml, _ = status_chip(ids, x + 0.06, ry + rh / 2 - 0.075, status)
        S.append(cxml)
        S.append(line(ids, "Row divider", tx, ry + rh, tx + 9.40, ry + rh, color=N200, w=0.5))
        ry += rh
    print(f"  s7: table ends at {ry:.2f}")

    S.append(footer(ids, FOOTER))
    return slide_xml(S)
