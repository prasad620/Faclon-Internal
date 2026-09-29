"""Lucide icon → DrawingML custom-geometry converter.

Downloads the named Lucide icons (pinned tag) into icons_svg/ and converts each one
into an <a:pathLst> fragment on a 24000 × 24000 grid, the same encoding the Welspun
deck used, so the icons render as native vector shapes in PowerPoint.
"""
import json
import math
import os
import re
import subprocess
import xml.etree.ElementTree as ET

LUCIDE_TAG = "0.475.0"
HERE = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(HERE, "icons_svg")
CACHE = os.path.join(HERE, "icons.json")
SCALE = 1000  # 24 px grid → 24000 units

# ---------------------------------------------------------------- SVG path parsing
_num = re.compile(r"[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?")


def _tokens(d):
    for m in re.finditer(r"[MmLlHhVvCcSsQqTtAaZz]|" + _num.pattern, d):
        t = m.group(0)
        yield t if t.isalpha() else float(t)


def _arc_to_cubics(x1, y1, rx, ry, phi_deg, large, sweep, x2, y2):
    """SVG elliptical arc → list of cubic Bézier control tuples (endpoint parameterisation)."""
    if rx == 0 or ry == 0 or (x1 == x2 and y1 == y2):
        return [(x1, y1, x2, y2, x2, y2)]
    phi = math.radians(phi_deg)
    cp, sp = math.cos(phi), math.sin(phi)
    dx, dy = (x1 - x2) / 2.0, (y1 - y2) / 2.0
    x1p = cp * dx + sp * dy
    y1p = -sp * dx + cp * dy
    rx, ry = abs(rx), abs(ry)
    lam = (x1p ** 2) / (rx ** 2) + (y1p ** 2) / (ry ** 2)
    if lam > 1:
        s = math.sqrt(lam)
        rx, ry = rx * s, ry * s
    num = rx ** 2 * ry ** 2 - rx ** 2 * y1p ** 2 - ry ** 2 * x1p ** 2
    den = rx ** 2 * y1p ** 2 + ry ** 2 * x1p ** 2
    coef = 0.0 if den == 0 else math.sqrt(max(0.0, num / den))
    if large == sweep:
        coef = -coef
    cxp = coef * (rx * y1p / ry)
    cyp = coef * -(ry * x1p / rx)
    cx = cp * cxp - sp * cyp + (x1 + x2) / 2.0
    cy = sp * cxp + cp * cyp + (y1 + y2) / 2.0

    def ang(ux, uy, vx, vy):
        d = ux * vx + uy * vy
        l = math.hypot(ux, uy) * math.hypot(vx, vy)
        a = math.acos(max(-1.0, min(1.0, d / l)))
        if ux * vy - uy * vx < 0:
            a = -a
        return a

    t1 = ang(1, 0, (x1p - cxp) / rx, (y1p - cyp) / ry)
    dt = ang((x1p - cxp) / rx, (y1p - cyp) / ry, (-x1p - cxp) / rx, (-y1p - cyp) / ry)
    if not sweep and dt > 0:
        dt -= 2 * math.pi
    elif sweep and dt < 0:
        dt += 2 * math.pi
    n = max(1, int(math.ceil(abs(dt) / (math.pi / 2) - 1e-9)))
    step = dt / n
    out = []
    t = t1
    for _ in range(n):
        t2 = t + step
        k = 4.0 / 3.0 * math.tan((t2 - t) / 4.0)

        def pt(theta):
            return (cx + rx * math.cos(theta) * cp - ry * math.sin(theta) * sp,
                    cy + rx * math.cos(theta) * sp + ry * math.sin(theta) * cp)

        def dpt(theta):
            return (-rx * math.sin(theta) * cp - ry * math.cos(theta) * sp,
                    -rx * math.sin(theta) * sp + ry * math.cos(theta) * cp)

        p0, p3 = pt(t), pt(t2)
        d0, d3 = dpt(t), dpt(t2)
        out.append((p0[0] + k * d0[0], p0[1] + k * d0[1],
                    p3[0] - k * d3[0], p3[1] - k * d3[1], p3[0], p3[1]))
        t = t2
    return out


def parse_path(d):
    """Return list of subpaths; each is a list of ('M',x,y) | ('L',x,y) | ('C',x1,y1,x2,y2,x,y) | ('Z',)."""
    toks = list(_tokens(d))
    i = 0
    subpaths, cur = [], []
    x = y = sx = sy = 0.0
    lcx = lcy = None  # last cubic control (for S)
    lqx = lqy = None  # last quad control (for T)
    cmd = None

    def take(n):
        nonlocal i
        vals = toks[i:i + n]
        i += n
        return vals

    def flush():
        nonlocal cur
        if cur:
            subpaths.append(cur)
        cur = []

    while i < len(toks):
        t = toks[i]
        if isinstance(t, str):
            cmd = t
            i += 1
            if cmd in "Zz":
                if cur:
                    cur.append(("Z",))
                flush()
                x, y = sx, sy
                lcx = lcy = lqx = lqy = None
                continue
        if cmd is None:
            raise ValueError("path must start with a command: " + d)
        rel = cmd.islower()
        c = cmd.upper()
        if c == "M":
            px, py = take(2)
            if rel:
                px += x
                py += y
            flush()
            x, y = sx, sy = px, py
            cur = [("M", x, y)]
            cmd = "l" if rel else "L"
            lcx = lcy = lqx = lqy = None
        elif c == "L":
            px, py = take(2)
            if rel:
                px += x
                py += y
            x, y = px, py
            cur.append(("L", x, y))
            lcx = lcy = lqx = lqy = None
        elif c == "H":
            (px,) = take(1)
            x = x + px if rel else px
            cur.append(("L", x, y))
            lcx = lcy = lqx = lqy = None
        elif c == "V":
            (py,) = take(1)
            y = y + py if rel else py
            cur.append(("L", x, y))
            lcx = lcy = lqx = lqy = None
        elif c == "C":
            x1, y1, x2, y2, px, py = take(6)
            if rel:
                x1 += x; y1 += y; x2 += x; y2 += y; px += x; py += y
            cur.append(("C", x1, y1, x2, y2, px, py))
            lcx, lcy = x2, y2
            lqx = lqy = None
            x, y = px, py
        elif c == "S":
            x2, y2, px, py = take(4)
            if rel:
                x2 += x; y2 += y; px += x; py += y
            x1, y1 = (2 * x - lcx, 2 * y - lcy) if lcx is not None else (x, y)
            cur.append(("C", x1, y1, x2, y2, px, py))
            lcx, lcy = x2, y2
            lqx = lqy = None
            x, y = px, py
        elif c == "Q":
            qx, qy, px, py = take(4)
            if rel:
                qx += x; qy += y; px += x; py += y
            c1 = (x + 2 / 3 * (qx - x), y + 2 / 3 * (qy - y))
            c2 = (px + 2 / 3 * (qx - px), py + 2 / 3 * (qy - py))
            cur.append(("C", c1[0], c1[1], c2[0], c2[1], px, py))
            lqx, lqy = qx, qy
            lcx = lcy = None
            x, y = px, py
        elif c == "T":
            px, py = take(2)
            if rel:
                px += x; py += y
            qx, qy = (2 * x - lqx, 2 * y - lqy) if lqx is not None else (x, y)
            c1 = (x + 2 / 3 * (qx - x), y + 2 / 3 * (qy - y))
            c2 = (px + 2 / 3 * (qx - px), py + 2 / 3 * (qy - py))
            cur.append(("C", c1[0], c1[1], c2[0], c2[1], px, py))
            lqx, lqy = qx, qy
            lcx = lcy = None
            x, y = px, py
        elif c == "A":
            rx, ry, rot, large, sweep, px, py = take(7)
            if rel:
                px += x; py += y
            for seg in _arc_to_cubics(x, y, rx, ry, rot, int(large), int(sweep), px, py):
                cur.append(("C",) + seg)
            lcx = lcy = lqx = lqy = None
            x, y = px, py
        else:
            raise ValueError("unsupported command " + cmd)
    flush()
    return subpaths


def _circle(cx, cy, rx, ry):
    k = 0.5522847498
    return [[("M", cx + rx, cy),
             ("C", cx + rx, cy + k * ry, cx + k * rx, cy + ry, cx, cy + ry),
             ("C", cx - k * rx, cy + ry, cx - rx, cy + k * ry, cx - rx, cy),
             ("C", cx - rx, cy - k * ry, cx - k * rx, cy - ry, cx, cy - ry),
             ("C", cx + k * rx, cy - ry, cx + rx, cy - k * ry, cx + rx, cy),
             ("Z",)]]


def svg_to_subpaths(svg_text):
    root = ET.fromstring(svg_text)
    subs = []
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        g = lambda k, d=0.0: float(el.get(k, d))
        if tag == "path":
            subs += parse_path(el.get("d"))
        elif tag == "line":
            subs.append([("M", g("x1"), g("y1")), ("L", g("x2"), g("y2"))])
        elif tag == "circle":
            subs += _circle(g("cx"), g("cy"), g("r"), g("r"))
        elif tag == "ellipse":
            subs += _circle(g("cx"), g("cy"), g("rx"), g("ry"))
        elif tag == "rect":
            x, y, w, h = g("x"), g("y"), g("width"), g("height")
            rx = g("rx", 0) or g("ry", 0)
            ry = g("ry", 0) or rx
            if rx <= 0:
                subs.append([("M", x, y), ("L", x + w, y), ("L", x + w, y + h), ("L", x, y + h), ("Z",)])
            else:
                d = (f"M{x + rx} {y}H{x + w - rx}A{rx} {ry} 0 0 1 {x + w} {y + ry}V{y + h - ry}"
                     f"A{rx} {ry} 0 0 1 {x + w - rx} {y + h}H{x + rx}A{rx} {ry} 0 0 1 {x} {y + h - ry}"
                     f"V{y + ry}A{rx} {ry} 0 0 1 {x + rx} {y}Z")
                subs += parse_path(d)
        elif tag in ("polyline", "polygon"):
            pts = [float(v) for v in re.findall(_num.pattern, el.get("points"))]
            pairs = list(zip(pts[0::2], pts[1::2]))
            sp = [("M",) + pairs[0]] + [("L",) + p for p in pairs[1:]]
            if tag == "polygon":
                sp.append(("Z",))
            subs.append(sp)
    return subs


def subpaths_to_pathlst(subs):
    def P(v):
        return str(int(round(v * SCALE)))

    out = []
    for sp in subs:
        parts = [f'<a:path w="{24 * SCALE}" h="{24 * SCALE}" fill="none">']
        for seg in sp:
            if seg[0] == "M":
                parts.append(f'<a:moveTo><a:pt x="{P(seg[1])}" y="{P(seg[2])}"/></a:moveTo>')
            elif seg[0] == "L":
                parts.append(f'<a:lnTo><a:pt x="{P(seg[1])}" y="{P(seg[2])}"/></a:lnTo>')
            elif seg[0] == "C":
                parts.append('<a:cubicBezTo>' + ''.join(
                    f'<a:pt x="{P(seg[k])}" y="{P(seg[k + 1])}"/>' for k in (1, 3, 5)) + '</a:cubicBezTo>')
            elif seg[0] == "Z":
                parts.append('<a:close/>')
        parts.append('</a:path>')
        out.append(''.join(parts))
    return '<a:pathLst>' + ''.join(out) + '</a:pathLst>'


def fetch(name):
    path = os.path.join(SVG_DIR, name + ".svg")
    if os.path.exists(path) and os.path.getsize(path) > 0:
        return open(path, encoding="utf-8").read()
    url = f"https://raw.githubusercontent.com/lucide-icons/lucide/refs/tags/{LUCIDE_TAG}/icons/{name}.svg"
    r = subprocess.run(["curl", "-sf", "-m", "20", url], capture_output=True, text=True)
    if r.returncode != 0 or "<svg" not in r.stdout:
        raise RuntimeError(f"could not fetch Lucide icon '{name}' ({url})")
    os.makedirs(SVG_DIR, exist_ok=True)
    open(path, "w", encoding="utf-8").write(r.stdout)
    return r.stdout


def load_icons(names):
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    missing = [n for n in names if n not in cache]
    for n in missing:
        cache[n] = subpaths_to_pathlst(svg_to_subpaths(fetch(n)))
    if missing:
        json.dump(cache, open(CACHE, "w"), indent=0)
    return {n: cache[n] for n in names}


if __name__ == "__main__":
    import sys
    icons = load_icons(sys.argv[1:] or ["fuel", "circle-help", "wrench"])
    for k, v in icons.items():
        print(k, len(v), "chars")
