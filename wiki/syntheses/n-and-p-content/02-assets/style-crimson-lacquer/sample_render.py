"""
Demo render — apply the Crimson Lacquer style to a single N&P pricing slide.
Mirrors the source flyer's information density: headline, three pricing pill clusters,
HOT! badges, sunburst, fleuron dividers, brand lockup, contact capsule.
"""

import os, sys
HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)

from PIL import Image, ImageDraw
import crimson_lacquer as cl

OUT = os.path.join(HERE, "sample-pricing.png")

W, H = 1080, 1350  # tall poster ratio so the three clusters can breathe

img = cl.base_canvas(W, H, seed=11)
d = ImageDraw.Draw(img)

# ---- corner sunburst (top-right) ----
cl.corner_sunburst(img, x=int(W * 0.86), y=int(H * 0.13), R=260)

# ---- brand lockup (top-left) ----
cl.brand_lockup(img, x=58, y=64, scale=1.0)

# ---- headline ----
cl.headline_gold(d, (W // 2 + 60, 130),
                 "อัตราค่าเรียน",
                 cl.thai_font("display", 96),
                 anchor="mm", outline_w=3)
# english subline
d.text((W // 2 + 60 - 200, 196), "TUITION RATES",
       font=cl.latin_font("section", 24), fill=cl.IVORY_CARD)

# fleuron under headline
cl.gold_fleuron(d, W // 2, 245, 360)

# ---- section heading ----
def section_heading(y, th_text, en_text):
    cl.headline_gold(d, (W // 2, y), th_text,
                     cl.thai_font("display", 44), anchor="mm",
                     fill=cl.IVORY_CARD, outline=cl.LACQUER_DEEP, outline_w=2)
    d.text((W // 2 - d.textlength(en_text, font=cl.latin_font("mono", 18)) / 2,
            y + 30),
           en_text, font=cl.latin_font("mono", 18), fill=cl.GOLD_HOT)

# ---- pill cluster: a single pill with multiple price rows ----
def price_pill(y_top, rows, height_per_row=64, hot_rows=()):
    """rows: list of (count_label, price, note)."""
    pad_x = 80
    inner_pad_y = 22
    h = inner_pad_y * 2 + height_per_row * len(rows)
    bbox = (pad_x, y_top, W - pad_x, y_top + h)
    cl.white_pill(img, bbox, radius=20)

    d2 = ImageDraw.Draw(img)
    for i, (count, price, note) in enumerate(rows):
        ry = y_top + inner_pad_y + height_per_row * (i + 0.5)
        # row hairline (between rows)
        if i > 0:
            d2.line([(pad_x + 30, y_top + inner_pad_y + height_per_row * i),
                     (W - pad_x - 30, y_top + inner_pad_y + height_per_row * i)],
                    fill=cl.IVORY_LINE, width=1)
        # count column (Thai content → Thai font)
        count_font = cl.thai_font("display", 28)
        d2.text((pad_x + 56, ry - 20), count,
                font=count_font, fill=cl.INK_BODY)
        # price column (centered)
        price_font = cl.latin_font("mono", 38)
        pb = d2.textbbox((0, 0), price, font=price_font)
        pw = pb[2] - pb[0]
        d2.text((W // 2 - pw / 2 - pb[0], ry - 22),
                price, font=price_font, fill=cl.LACQUER)
        # baht label
        d2.text((W // 2 + pw / 2 + 14, ry - 16),
                "บาท", font=cl.thai_font("body", 22), fill=cl.INK_BODY)
        # note (right side, Thai)
        if note:
            note_font = cl.thai_font("body", 19)
            nw = d2.textlength(note, font=note_font)
            d2.text((W - pad_x - 26 - nw, ry - 12),
                    note, font=note_font, fill=(110, 80, 80))
        # HOT! badge — sits straddling the pill's left edge
        if i in hot_rows:
            cl.hot_badge(img, pad_x + 6, int(ry), size=58, label="HOT!", angle_deg=-14)
    return y_top + h

# ---- Cluster 1: regular group ----
section_heading(290, "แพ็กเกจคลาสธรรมดา", "REGULAR  GROUP  CLASS")
y = price_pill(330,
               rows=[
                   ("1 ครั้ง",   "400",   ""),
                   ("10 ครั้ง",  "3,500", "อายุแพ็กเกจ 3 เดือน"),
                   ("30 ครั้ง",  "9,000", "อายุแพ็กเกจ 6 เดือน"),
               ],
               hot_rows=(1,))

# fleuron divider
cl.gold_fleuron(d, W // 2, y + 30, 420)

# ---- Cluster 2: monthly ----
section_heading(y + 70, "แพ็กเกจรายเดือน", "MONTHLY  PACKAGES")
y2 = price_pill(y + 110,
                rows=[
                    ("1 เดือน",   "3,990",  ""),
                    ("3 เดือน",   "9,990",  ""),
                    ("6 เดือน",   "17,990", ""),
                    ("12 เดือน",  "29,990", ""),
                ],
                height_per_row=58,
                hot_rows=(0, 1))

cl.gold_fleuron(d, W // 2, y2 + 26, 420)

# ---- Cluster 3: private ----
section_heading(y2 + 64, "แพ็กเกจคลาสส่วนตัว", "PRIVATE  CLASS")
y3 = price_pill(y2 + 104,
                rows=[
                    ("1 ครั้ง",   "700",    ""),
                    ("10 ครั้ง",  "5,990",  "อายุแพ็กเกจ 3 เดือน"),
                    ("30 ครั้ง",  "14,990", "อายุแพ็กเกจ 6 เดือน"),
                ],
                hot_rows=(1,))

# ---- yellow contact capsule ----
cap_top = y3 + 36
cl.contact_capsule(img,
                   bbox=(140, cap_top, W - 140, cap_top + 64),
                   text="มาร่วมสร้างสุขภาพดีและพลังบวก  ที่ ค่ายมวย ป.เปาอินทร์",
                   font=cl.thai_font("display", 22))

# ---- foot strip: phone + IG/TT + LINE QR placeholder ----
foot_y = cap_top + 92
d.text((90, foot_y),
       "ADD LINE", font=cl.latin_font("section", 22), fill=cl.IVORY_CARD)
d.text((90, foot_y + 30),
       "•  สอบถามเพิ่มเติม\n•  ลงทะเบียนเรียน\n•  จองคลาสเรียน",
       font=cl.thai_font("body", 18), fill=cl.IVORY_CARD)
d.text((90, foot_y + 124),
       "081-4455844", font=cl.latin_font("display", 30), fill=cl.GOLD_HOT)
d.text((90, foot_y + 162),
       "@PPAOINMUAYTHAI", font=cl.latin_font("section", 18), fill=cl.IVORY_CARD)

# QR placeholder (right)
qr_size = 150
qr_x = W - 90 - qr_size
qr_y = foot_y + 16
d.rounded_rectangle([qr_x, qr_y, qr_x + qr_size, qr_y + qr_size],
                    radius=10, fill=cl.IVORY_CARD, outline=cl.GOLD_DEEP, width=2)
# fake qr pattern
import random as _r
rng = _r.Random(7)
cell = qr_size // 18
for ix in range(18):
    for iy in range(18):
        if rng.random() > 0.55:
            d.rectangle([qr_x + 8 + ix * cell, qr_y + 8 + iy * cell,
                         qr_x + 8 + ix * cell + cell - 1, qr_y + 8 + iy * cell + cell - 1],
                        fill=cl.INK_BODY)
# QR corner blocks
for (cx, cy) in [(qr_x + 12, qr_y + 12),
                 (qr_x + qr_size - 38 - 12, qr_y + 12),
                 (qr_x + 12, qr_y + qr_size - 38 - 12)]:
    d.rectangle([cx, cy, cx + 38, cy + 38], fill=cl.IVORY_CARD)
    d.rectangle([cx + 4, cy + 4, cx + 34, cy + 34], fill=cl.INK_BODY)
    d.rectangle([cx + 10, cy + 10, cx + 28, cy + 28], fill=cl.IVORY_CARD)
d.text((qr_x + qr_size / 2 - 16, qr_y + qr_size + 6),
       "LINE", font=cl.latin_font("display", 22), fill=cl.IVORY_CARD)

# ---- mirrored small sunburst bottom-left for symmetry ----
cl.corner_sunburst(img, x=int(W * 0.10), y=int(H * 0.92), R=170)

img.save(OUT)
print("wrote", OUT)
