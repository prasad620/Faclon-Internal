from dml import *
from common import *

# (phase, duration text, start week, end week, group, bar note)
PHASES = [
    ("Application Design & Project Kickoff", "1 week", 1, 1, "onb", "Kick Off"),
    ("Hardware Supply", "6 weeks", 2, 7, "onb", "IoT Devices and Gateway"),
    ("Installation and Commissioning", "12 weeks", 6, 17, "onb", "Installation and Commissioning of Hardware at each store"),
    ("Application Development", "8 weeks", 2, 9, "imp", "DG Fuel Monitoring and Maintenance Application"),
    ("Configuration & Integration", "12 weeks", 7, 18, "imp", "Configuration and Integration with Fusion"),
    ("UAT & Training", "3 weeks", 19, 21, "gol", "UAT and user training"),
    ("Go-live, Handover & Hypercare", "1 week", 22, 22, "gol", "Go Live"),
]
GROUPS = {
    "onb": ("Project Onboarding Phase", "Kick-off, hardware supply and installation", AZURE, AZURE_100, AZURE_700),
    "imp": ("Implementation Phase", "Application build and Fusion integration", CIDER_700, "FDE4CF", CIDER_700),
    "gol": ("Go-live Phase", "UAT, training, handover and hypercare", EMERALD_700, EMERALD_100, EMERALD_700),
}
WEEKS = 22
TOTAL = "22 weeks"


def build():
    ids = Ids()
    S = [header(ids, "BOTH WORKFLOWS  ·  PLAN", "Project Delivery Schedule",
                "Indicative plan from kick-off. Hardware supply and store-by-store installation run alongside the application build.")]

    # ---------------------------------------------------------------- summary table
    ty = 1.12
    hh, rh = 0.40, 0.32
    cols = [1.55] + [(9.40 - 1.55 - 1.85) / len(PHASES)] * len(PHASES) + [1.85]
    heads = ["Objective"] + [p[0] for p in PHASES] + ["Total delivery time"]
    x = 0.30
    S.append(rect(ids, "Summary header", 0.30, ty, 9.40, hh, fill=AZURE, radius=0.05))
    for w, h_ in zip(cols, heads):
        S.append(textbox(ids, "Summary head", x + 0.04, ty, w - 0.08, hh,
                         [para(run(h_, FONT_BODY_SB, 6.2, WHITE), align="ctr", lnspc=7.0)], anchor="ctr"))
        x += w
    S.append(rect(ids, "Summary body", 0.30, ty + hh, 9.40, rh, fill=N050, line=N200, line_w=0.5))
    x = 0.30
    S.append(textbox(ids, "Objective", x + 0.06, ty + hh, cols[0] - 0.12, rh,
                     [para(run("DG Online Monitoring", FONT_BODY_SB, 6.8, HEADING), align="ctr", lnspc=7.6),
                      para(run("Refilling  ·  Maintenance", FONT_BODY, 6, MUTED), align="ctr", lnspc=6.8, spc_before=1)], anchor="ctr"))
    x += cols[0]
    for (name, dur, a, b, grp, note), w in zip(PHASES, cols[1:]):
        col = GROUPS[grp][4]
        S.append(textbox(ids, "Duration", x, ty + hh, w, rh, [para(run(dur, FONT_BODY_SB, 7.6, col), align="ctr", lnspc=8.4)], anchor="ctr"))
        x += w
    S.append(rect(ids, "Total cell", x, ty + hh, cols[-1], rh, fill=N100))
    S.append(textbox(ids, "Total", x, ty + hh, cols[-1], rh, [para(run(TOTAL, FONT_BODY_SB, 8.5, HEADING), align="ctr", lnspc=9.5)], anchor="ctr"))

    # ---------------------------------------------------------------- group brackets
    by = ty + hh + rh + 0.10
    gx = 0.30 + cols[0]
    spans = {}
    for (name, dur, a, b, grp, note), w in zip(PHASES, cols[1:]):
        spans.setdefault(grp, [gx, gx])
        spans[grp][1] = gx + w
        gx += w
    for grp, (x1, x2) in spans.items():
        title, sub, col, fill, tcol = GROUPS[grp]
        S.append(line(ids, "Bracket", x1 + 0.06, by, x2 - 0.06, by, color=col, w=1.0))
        S.append(line(ids, "Bracket end", x1 + 0.06, by, x1 + 0.06, by + 0.07, color=col, w=1.0))
        S.append(line(ids, "Bracket end", x2 - 0.06, by, x2 - 0.06, by + 0.07, color=col, w=1.0))
        S.append(textbox(ids, "Group label", x1, by + 0.09, x2 - x1, 0.28,
                         [para(run(title, FONT_BODY_SB, 6.6, HEADING), align="ctr", lnspc=7.6),
                          para(run(sub, FONT_BODY, 6, col), align="ctr", lnspc=6.8, spc_before=1)]))

    # ---------------------------------------------------------------- ruler + gantt
    ry = by + 0.44
    tx0, tw = 1.95, 7.75
    wk = tw / WEEKS
    S.append(textbox(ids, "Ruler label", 0.30, ry, 1.55, 0.17,
                     [para(run("WEEK", FONT_BODY_SB, 5.6, SECOND, spc=82, caps=True), align="r", lnspc=5.6)], anchor="ctr"))
    for i in range(WEEKS // 2):
        cx = tx0 + i * 2 * wk
        S.append(rect(ids, "Ruler cell", cx, ry, 2 * wk, 0.17, fill=N050, line=N200, line_w=0.5))
        S.append(textbox(ids, "Week number", cx, ry, 2 * wk, 0.17,
                         [para(run(f"{2 * i + 1}–{2 * i + 2}", FONT_BODY, 5.8, SECOND), align="ctr", lnspc=5.8)], anchor="ctr"))
    gy = ry + 0.22
    row_h, gap = 0.27, 0.05
    for i, (name, dur, a, b, grp, note) in enumerate(PHASES):
        y = gy + i * (row_h + gap)
        title, sub, col, fill, tcol = GROUPS[grp]
        S.append(card(ids, "Phase name card", 0.30, y, 1.55, row_h, fill=WHITE, line=N300, radius=0.04))
        S.append(textbox(ids, "Phase name", 0.38, y, 1.42, row_h, [para(run(name, FONT_BODY_SB, 6.2, HEADING), lnspc=6.9)], anchor="ctr"))
        S.append(rect(ids, "Track", tx0, y, tw, row_h, fill=WHITE, line=N300, line_w=0.5, dash="sysDash"))
        bx = tx0 + (a - 1) * wk + 0.02
        bw = (b - a + 1) * wk - 0.04
        S.append(rect(ids, "Bar", bx, y + 0.035, bw, row_h - 0.07, fill=fill, radius=0.03))
        # shrink the in-bar note until it fits; never spill outside the bar
        size = 5.8
        while text_width(note, FONT_BODY_SB, size) > bw - 0.05 and size > 4.0:
            size -= 0.2
        S.append(textbox(ids, "Bar note", bx + 0.025, y + 0.035, bw - 0.05, row_h - 0.07,
                         [para(run(note, FONT_BODY_SB, size, tcol), align="ctr", lnspc=size * 1.1)], anchor="ctr"))
    gantt_bottom = gy + len(PHASES) * (row_h + gap) - gap

    # basis
    basis_y = gantt_bottom + 0.08
    S.append(rect(ids, "Basis", 0.30, basis_y, 9.40, 5.25 - basis_y, fill=N050, radius=0.04))
    S.append(textbox(ids, "Basis text", 0.40, basis_y, 9.2, 5.25 - basis_y,
                     [para([run("Basis: ", FONT_BODY_SB, 6.2, HEADING),
                            run("indicative durations from kick-off. Installation and commissioning run store by store and depend on the final store "
                                "count; Fusion integration depends on the specification from Flipkart.",
                                FONT_BODY, 6.2, BODY)], lnspc=7.2)], anchor="ctr"))
    print(f"  s11: gantt to {gantt_bottom:.2f}, basis {basis_y:.2f}–5.25")

    S.append(footer(ids, FOOTER))
    return slide_xml(S)
