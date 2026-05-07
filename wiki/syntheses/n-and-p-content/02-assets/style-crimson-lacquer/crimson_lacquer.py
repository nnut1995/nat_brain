"""
Crimson Lacquer — visual primitives for the N&P showbill design philosophy.

Public functions:
    base_canvas(W, H)               -> PIL.Image: lacquered crimson field, marbled, vignetted.
    corner_sunburst(img, x, y, R)   -> draws a gold sunburst around (x,y).
    gold_fleuron(draw, cx, cy, w)   -> ── ❖ ── divider centered at (cx,cy).
    white_pill(img, bbox, radius)   -> ivory rounded card with soft shadow + hairline gold edge.
    hot_badge(img, x, y, size, label="HOT!")  -> jagged flame starburst with text.
    contact_capsule(draw, bbox, text) -> yellow rounded capsule with motivational copy.
    brand_lockup(img, x, y, scale)  -> small N&P boxing-ring + stars + Thai-script logo.
    marble_overlay(img)             -> low-opacity white veining across the field.
    headline_gold(draw, xy, text, font, anchor) -> gold fill + thin dark outline.

Fonts: see TH_FONTS / LATIN_FONTS dicts. Thai fonts come from /System/Library/Fonts/Supplemental.
Latin fonts come from the canvas-design fonts directory (resolved at module load).
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import math, os, random

# ---------- palette tokens ----------
LACQUER       = (122, 11, 22)
LACQUER_DEEP  = (90, 7, 16)
LACQUER_HIGH  = (156, 26, 38)
GOLD_HOT      = (242, 197, 61)
GOLD_DEEP     = (201, 149, 42)
IVORY_CARD    = (252, 247, 235)
IVORY_LINE    = (228, 214, 184)
INK_BODY      = (42, 16, 16)
FLAME_HOT     = (233, 76, 32)
FLAME_EDGE    = (122, 26, 6)
CAPSULE_YEL   = (244, 210, 107)
GOLD_OUTLINE  = (110, 75, 18)

# ---------- font discovery ----------
LATIN_DIR = "/Users/natnunpanichphong/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/9ecbae48-c30b-4d4c-812b-72d64c0a068d/b8f8b6ef-274e-4625-ab49-986cc79bcfb6/skills/canvas-design/canvas-fonts"
TH_DIR = "/System/Library/Fonts/Supplemental"

def _try(*paths):
    for p in paths:
        if os.path.exists(p):
            return p
    return None

# SukhumvitSet.ttc is the only Thai TTC that PIL reliably renders here, so use it for
# both display and body. Index 0 = Light, 2 = Medium, 3 = Bold (typical layout).
TH_FONTS = {
    "display": _try(os.path.join(TH_DIR, "SukhumvitSet.ttc"),
                    os.path.join(TH_DIR, "Ayuthaya.ttf")),
    "body":    _try(os.path.join(TH_DIR, "SukhumvitSet.ttc"),
                    os.path.join(TH_DIR, "Ayuthaya.ttf")),
}
TH_FACE = {"display": 3, "body": 2}  # bold for display, medium for body

LATIN_FONTS = {
    "display":     os.path.join(LATIN_DIR, "BigShoulders-Bold.ttf"),
    "display_alt": os.path.join(LATIN_DIR, "Boldonse-Regular.ttf"),
    "section":     os.path.join(LATIN_DIR, "Outfit-Bold.ttf"),
    "body_bold":   os.path.join(LATIN_DIR, "Outfit-Bold.ttf"),
    "body":        os.path.join(LATIN_DIR, "Outfit-Regular.ttf"),
    "mono":        os.path.join(LATIN_DIR, "GeistMono-Bold.ttf"),
    "mono_reg":    os.path.join(LATIN_DIR, "GeistMono-Regular.ttf"),
    "italic":      os.path.join(LATIN_DIR, "InstrumentSerif-Italic.ttf"),
}

def latin_font(role, size):
    return ImageFont.truetype(LATIN_FONTS[role], size)

def thai_font(role, size, index=None):
    path = TH_FONTS[role]
    if index is None:
        index = TH_FACE.get(role, 0)
    # try the requested face, fall back through 3,2,1,0 if PIL rejects it
    for idx in [index, 3, 2, 1, 0]:
        try:
            return ImageFont.truetype(path, size, index=idx)
        except (TypeError, OSError):
            continue
    return ImageFont.truetype(path, size)

# ---------- canvas + texture ----------
def base_canvas(W=1080, H=1080, seed=7):
    """Crimson lacquer field with marbled veining and a warm pool of light."""
    img = Image.new("RGB", (W, H), LACQUER)

    # warm pool of highlight, upper-right (where the sunburst lives)
    glow = Image.new("RGB", (W, H), LACQUER)
    g = ImageDraw.Draw(glow)
    cx, cy = int(W * 0.78), int(H * 0.18)
    for r in range(640, 0, -8):
        f = 1 - r / 640
        col = (
            min(255, LACQUER[0] + int(58 * f)),
            min(255, LACQUER[1] + int(38 * f)),
            min(255, LACQUER[2] + int(20 * f)),
        )
        g.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
    glow = glow.filter(ImageFilter.GaussianBlur(60))
    img = Image.blend(img, glow, 0.65)

    # vignette pool corners (deeper crimson)
    vig = Image.new("RGB", (W, H), LACQUER)
    vg = ImageDraw.Draw(vig)
    for r in range(900, 0, -10):
        f = r / 900
        col = (
            int(LACQUER[0] * (1 - 0.45 * f) + LACQUER_DEEP[0] * 0.45 * f),
            int(LACQUER[1] * (1 - 0.45 * f) + LACQUER_DEEP[1] * 0.45 * f),
            int(LACQUER[2] * (1 - 0.45 * f) + LACQUER_DEEP[2] * 0.45 * f),
        )
        vg.ellipse([W//2 - r, H//2 - r, W//2 + r, H//2 + r], outline=col, width=10)
    vig = vig.filter(ImageFilter.GaussianBlur(120))
    img = Image.blend(img, vig, 0.35)

    # marble veining (faint white wisps)
    marble_overlay(img, seed=seed)

    # film grain
    rnd = random.Random(seed)
    px = img.load()
    for _ in range(int(W * H * 0.012)):
        x = rnd.randint(0, W - 1); y = rnd.randint(0, H - 1)
        r, gn, b = px[x, y]
        d = rnd.randint(-9, 11)
        px[x, y] = (max(0, min(255, r + d)), max(0, min(255, gn + d)), max(0, min(255, b + d)))
    return img

def marble_overlay(img, seed=11, strands=18, opacity=0.10):
    """Faint white wispy veining laid over the lacquer."""
    W, H = img.size
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    rnd = random.Random(seed)
    for _ in range(strands):
        x0 = rnd.randint(-100, W); y0 = rnd.randint(-100, H)
        pts = [(x0, y0)]
        for _ in range(rnd.randint(40, 90)):
            x0 += rnd.randint(-10, 16)
            y0 += rnd.randint(-6, 10)
            pts.append((x0, y0))
        a = rnd.randint(35, 70)
        d.line(pts, fill=(255, 240, 230, a), width=rnd.randint(1, 2))
    layer = layer.filter(ImageFilter.GaussianBlur(2.2))
    img.paste(Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB"))

# ---------- sunburst ----------
def corner_sunburst(img, x, y, R, rays=22, ray_color=GOLD_HOT,
                    glow_color=(255, 220, 130), bright_core=(255, 245, 180)):
    """Sharp triangular gold rays radiating from (x,y) over a soft glow + bright core."""
    W, H = img.size
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)

    # soft halo
    for r in range(R, 0, -8):
        f = r / R
        a = int(120 * (1 - f) ** 1.6)
        if a <= 0: continue
        d.ellipse([x - r, y - r, x + r, y + r],
                  fill=(glow_color[0], glow_color[1], glow_color[2], a))

    # rays
    inner_r = R * 0.18
    outer_r = R * 1.00
    half_w = math.radians(360 / rays * 0.34)
    for i in range(rays):
        a = (i / rays) * 2 * math.pi
        x1 = x + math.cos(a - half_w) * inner_r
        y1 = y + math.sin(a - half_w) * inner_r
        x2 = x + math.cos(a) * outer_r
        y2 = y + math.sin(a) * outer_r
        x3 = x + math.cos(a + half_w) * inner_r
        y3 = y + math.sin(a + half_w) * inner_r
        d.polygon([(x1, y1), (x2, y2), (x3, y3)],
                  fill=(ray_color[0], ray_color[1], ray_color[2], 235))

    # bright core
    for r in range(int(R * 0.22), 0, -1):
        f = r / (R * 0.22)
        a = int(255 * (1 - f) ** 0.8)
        d.ellipse([x - r, y - r, x + r, y + r],
                  fill=(bright_core[0], bright_core[1], bright_core[2], a))

    layer = layer.filter(ImageFilter.GaussianBlur(0.8))
    out = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")
    img.paste(out)

# ---------- gold fleuron divider ----------
def gold_fleuron(draw, cx, cy, w, color=GOLD_DEEP, line_w=2):
    """── ❖ ── style: two thin rules with a four-petal diamond between."""
    half = w / 2
    pad = 22
    # left rule
    draw.line([(cx - half, cy), (cx - pad, cy)], fill=color, width=line_w)
    # right rule
    draw.line([(cx + pad, cy), (cx + half, cy)], fill=color, width=line_w)
    # diamond fleuron — four petals
    s = 8
    pts_outer = [(cx, cy - s), (cx + s, cy), (cx, cy + s), (cx - s, cy)]
    draw.polygon(pts_outer, outline=color)
    # inner small diamond
    s2 = 3
    pts_inner = [(cx, cy - s2), (cx + s2, cy), (cx, cy + s2), (cx - s2, cy)]
    draw.polygon(pts_inner, fill=color)
    # tiny spurs
    draw.line([(cx - s - 6, cy), (cx - s - 2, cy)], fill=color, width=line_w)
    draw.line([(cx + s + 2, cy), (cx + s + 6, cy)], fill=color, width=line_w)

# ---------- white pill ----------
def white_pill(img, bbox, radius=22, fill=IVORY_CARD, edge=GOLD_DEEP, edge_w=2,
               shadow=True, shadow_offset=(0, 6), shadow_blur=14, shadow_alpha=110):
    """Ivory rounded card with soft drop shadow + hairline gold edge.
    bbox: (x0, y0, x1, y1)."""
    x0, y0, x1, y1 = bbox
    W, H = img.size

    if shadow:
        s_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sd = ImageDraw.Draw(s_layer)
        sx, sy = shadow_offset
        sd.rounded_rectangle([x0 + sx, y0 + sy, x1 + sx, y1 + sy],
                             radius=radius, fill=(0, 0, 0, shadow_alpha))
        s_layer = s_layer.filter(ImageFilter.GaussianBlur(shadow_blur))
        img.paste(Image.alpha_composite(img.convert("RGBA"), s_layer).convert("RGB"))

    d = ImageDraw.Draw(img)
    d.rounded_rectangle(bbox, radius=radius, fill=fill, outline=edge, width=edge_w)
    # inner hairline accent for the lacquered-sticker feel
    d.rounded_rectangle((x0 + 4, y0 + 4, x1 - 4, y1 - 4),
                        radius=radius - 4, outline=IVORY_LINE, width=1)

# ---------- HOT! flame badge ----------
def hot_badge(img, cx, cy, size=58, label="HOT!", angle_deg=-12):
    """Jagged red-orange starburst with rotated label. size = approx radius."""
    W, H = img.size
    spikes = 14
    inner = size * 0.62
    outer = size * 1.05

    pts = []
    for i in range(spikes * 2):
        r = outer if i % 2 == 0 else inner
        a = (i / (spikes * 2)) * 2 * math.pi - math.pi / 2
        # add slight irregularity for a hand-stamped feel
        rj = r * (1 + ((i * 37) % 7 - 3) * 0.012)
        pts.append((cx + math.cos(a) * rj, cy + math.sin(a) * rj))

    # draw onto a rotation layer
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.polygon(pts, fill=FLAME_HOT, outline=FLAME_EDGE)
    # inner echo for depth
    inner_pts = [(cx + (px - cx) * 0.78, cy + (py - cy) * 0.78) for (px, py) in pts]
    d.polygon(inner_pts, outline=GOLD_HOT)

    # label
    f = latin_font("display", int(size * 0.62))
    bbox = d.textbbox((0, 0), label, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text((cx - tw / 2 - bbox[0], cy - th / 2 - bbox[1] + 2),
           label, font=f, fill=(255, 250, 230))

    # rotate
    if angle_deg:
        layer = layer.rotate(angle_deg, resample=Image.BICUBIC, center=(cx, cy))

    out = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")
    img.paste(out)

# ---------- yellow contact capsule ----------
def contact_capsule(img, bbox, text, font=None):
    x0, y0, x1, y1 = bbox
    d = ImageDraw.Draw(img)
    radius = (y1 - y0) // 2
    d.rounded_rectangle(bbox, radius=radius, fill=CAPSULE_YEL,
                        outline=GOLD_DEEP, width=2)
    if font is None:
        font = latin_font("body_bold", 26)
    bb = d.textbbox((0, 0), text, font=font)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    d.text(((x0 + x1) / 2 - tw / 2 - bb[0],
            (y0 + y1) / 2 - th / 2 - bb[1]),
           text, font=font, fill=INK_BODY)

# ---------- brand lockup ----------
def brand_lockup(img, x, y, scale=1.0, en_top="N&P BOXING GYM",
                 th_line="ค่ายมวย ป.เปาอินทร์", town="พระราม 2",
                 year="2009"):
    """Small ring + stars + name lockup, top-left corner."""
    d = ImageDraw.Draw(img)
    s = scale
    # boxing-ring badge: rounded square with ring corner posts
    bx, by = int(x), int(y)
    badge_w = int(72 * s); badge_h = int(72 * s)
    d.rounded_rectangle([bx, by, bx + badge_w, by + badge_h],
                        radius=int(8 * s), fill=None,
                        outline=GOLD_HOT, width=max(2, int(2 * s)))
    # corner ring posts
    for (px, py) in [(bx, by), (bx + badge_w, by), (bx, by + badge_h), (bx + badge_w, by + badge_h)]:
        d.ellipse([px - 4*s, py - 4*s, px + 4*s, py + 4*s], fill=GOLD_HOT)
    # ring ropes (3 horizontal lines)
    for k in range(3):
        ry = by + int(badge_h * (0.35 + k * 0.18))
        d.line([(bx + 6, ry), (bx + badge_w - 6, ry)], fill=GOLD_HOT, width=1)
    # stars across the top of the badge
    for k in range(3):
        sx = bx + int(badge_w * (0.25 + k * 0.25))
        sy = by + int(badge_h * 0.18)
        _star(d, sx, sy, 5 * s, GOLD_HOT)
    # central monogram
    f_mon = latin_font("display", int(20 * s))
    mb = d.textbbox((0, 0), "P.PAO-IN", font=f_mon)
    mw, mh = mb[2] - mb[0], mb[3] - mb[1]
    d.text((bx + badge_w / 2 - mw / 2 - mb[0],
            by + badge_h * 0.55 - mh / 2 - mb[1]),
           "P.PAO-IN", font=f_mon, fill=GOLD_HOT)
    # year strip under monogram
    f_yr = latin_font("mono_reg", int(10 * s))
    yb = d.textbbox((0, 0), year, font=f_yr)
    yw, yh = yb[2] - yb[0], yb[3] - yb[1]
    d.text((bx + badge_w / 2 - yw / 2 - yb[0],
            by + badge_h * 0.78 - yh / 2 - yb[1]),
           year, font=f_yr, fill=GOLD_HOT)

    # text stack to the right
    tx = bx + badge_w + 12
    f_en = latin_font("section", int(15 * s))
    d.text((tx, by + 4), en_top, font=f_en, fill=IVORY_CARD)
    f_th = thai_font("body", int(15 * s))
    d.text((tx, by + 4 + int(20 * s)), th_line, font=f_th, fill=IVORY_CARD)
    d.text((tx, by + 4 + int(40 * s)), town, font=f_th, fill=GOLD_HOT)

def _star(draw, cx, cy, R, color):
    pts = []
    for i in range(10):
        r = R if i % 2 == 0 else R * 0.42
        a = (i / 10) * 2 * math.pi - math.pi / 2
        pts.append((cx + math.cos(a) * r, cy + math.sin(a) * r))
    draw.polygon(pts, fill=color)

# ---------- gold headline (fill + thin outline) ----------
def headline_gold(draw, xy, text, font, anchor="mm",
                  fill=GOLD_HOT, outline=GOLD_OUTLINE, outline_w=2):
    """Gold text with a thin dark outline — temple-gilt feel."""
    x, y = xy
    bb = draw.textbbox((0, 0), text, font=font)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    ax, ay = anchor[0], anchor[1]
    if ax == "m": tx = x - tw / 2 - bb[0]
    elif ax == "r": tx = x - tw - bb[0]
    else: tx = x - bb[0]
    if ay == "m": ty = y - th / 2 - bb[1]
    elif ay == "b": ty = y - th - bb[1]
    else: ty = y - bb[1]
    # outline (8-direction stroke)
    for ox in range(-outline_w, outline_w + 1):
        for oy in range(-outline_w, outline_w + 1):
            if ox == 0 and oy == 0: continue
            draw.text((tx + ox, ty + oy), text, font=font, fill=outline)
    draw.text((tx, ty), text, font=font, fill=fill)
