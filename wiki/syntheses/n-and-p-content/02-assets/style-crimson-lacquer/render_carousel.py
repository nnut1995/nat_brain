"""
N&P Muay Thai — '02 Three Ways to Train' carousel,
re-skinned in the Crimson Lacquer design philosophy.
Six 1080x1080 PNGs, written to ./carousel/.
"""

import os, sys, math
HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)

from PIL import Image, ImageDraw
import crimson_lacquer as cl

OUT = os.path.join(HERE, "carousel")
os.makedirs(OUT, exist_ok=True)

W = H = 1080
MARGIN = 60

# ---------- shared chrome ----------
def slide_base(idx, sunburst=("tr", 220), seed=11):
    """Returns (img, draw). Lays down crimson canvas, sunburst, brand lockup, slide index."""
    img = cl.base_canvas(W, H, seed=seed)

    # corner sunburst — placement varies by slide for series rhythm
    pos, R = sunburst
    sx = {"tr": int(W * 0.86), "tl": int(W * 0.14), "br": int(W * 0.86), "bl": int(W * 0.14)}[pos]
    sy = {"tr": int(H * 0.14), "tl": int(H * 0.14), "br": int(H * 0.86), "bl": int(H * 0.86)}[pos]
    cl.corner_sunburst(img, x=sx, y=sy, R=R)

    d = ImageDraw.Draw(img)

    # brand lockup top-left
    cl.brand_lockup(img, x=MARGIN, y=MARGIN + 4, scale=0.92)

    # slide index top-right (avoid sunburst when sunburst sits top-right)
    idx_pos = (W - MARGIN - 8, MARGIN + 18) if pos != "tr" else (W - MARGIN - 8, MARGIN + 12)
    if pos == "tr":
        # tuck index under the burst by drawing it on the bottom-right instead
        idx_pos = (W - MARGIN - 8, H - MARGIN - 22)
    d.text((idx_pos[0] - cl.latin_font("mono", 22).getlength(f"{idx} / 06"), idx_pos[1]),
           f"{idx} / 06", font=cl.latin_font("mono", 22), fill=cl.GOLD_HOT)

    return img, d

def footer_strip(img, contact=True):
    """Bottom rule + footer signature line. Contact capsule when contact=True."""
    d = ImageDraw.Draw(img)
    # hairline rule
    d.line([(MARGIN, H - MARGIN - 60), (W - MARGIN, H - MARGIN - 60)],
           fill=cl.GOLD_DEEP, width=1)
    cl.gold_fleuron(d, W // 2, H - MARGIN - 60, 220)
    # signature
    sig = "ค่ายมวย ป.เปาอินทร์  ·  พระราม 2  ·  กรุงเทพฯ"
    f_sig = cl.thai_font("body", 18)
    sw = f_sig.getlength(sig)
    d.text((W // 2 - sw / 2, H - MARGIN - 38), sig, font=f_sig, fill=cl.IVORY_CARD)
    en = "N&P MUAY THAI CAMP  ·  RAMA 2  ·  BANGKOK"
    f_en = cl.latin_font("mono", 14)
    ew = f_en.getlength(en)
    d.text((W // 2 - ew / 2, H - MARGIN - 14), en, font=f_en, fill=cl.GOLD_HOT)

# ---------- Slide 1: Cover ----------
def slide_1():
    img, d = slide_base(1, sunburst=("tr", 230), seed=11)

    # Thai headline
    cl.headline_gold(d, (W // 2, 270), "3 วิธีฝึกที่ N&P",
                     cl.thai_font("display", 96), anchor="mm", outline_w=3)

    # English subline
    sub = "THREE  WAYS  TO  TRAIN"
    f_sub = cl.latin_font("section", 26)
    sw = f_sub.getlength(sub)
    d.text((W // 2 - sw / 2, 340), sub, font=f_sub, fill=cl.IVORY_CARD)

    # Fleuron under subtitle
    cl.gold_fleuron(d, W // 2, 392, 360)

    # Three preview pills, side by side, each numbered
    tracks = [
        ("01", "คลาสกลุ่ม",   "GROUP",      "60′  ·  AFTERNOON"),
        ("02", "ส่วนตัว",      "PRIVATE",    "90′  ·  MORNING"),
        ("03", "สเตย์เคชั่น",  "STAYCATION", "TRAIN · EAT · SLEEP"),
    ]
    pill_top = 450
    pill_h = 280
    gap = 22
    pill_w = (W - 2 * MARGIN - gap * 2) // 3

    for i, (num, th, en, meta) in enumerate(tracks):
        x0 = MARGIN + i * (pill_w + gap)
        bbox = (x0, pill_top, x0 + pill_w, pill_top + pill_h)
        cl.white_pill(img, bbox, radius=20)

        # number in gold at top
        f_num = cl.latin_font("display", 64)
        nw = f_num.getlength(num)
        d.text((x0 + pill_w / 2 - nw / 2, pill_top + 22), num,
               font=f_num, fill=cl.GOLD_DEEP)

        # Thai track name
        f_th = cl.thai_font("display", 36)
        tw = f_th.getlength(th)
        d.text((x0 + pill_w / 2 - tw / 2, pill_top + 110),
               th, font=f_th, fill=cl.INK_BODY)

        # English track name
        f_en = cl.latin_font("section", 22)
        ew = f_en.getlength(en)
        d.text((x0 + pill_w / 2 - ew / 2, pill_top + 168),
               en, font=f_en, fill=cl.LACQUER)

        # hairline + meta
        d.line([(x0 + 28, pill_top + 210), (x0 + pill_w - 28, pill_top + 210)],
               fill=cl.IVORY_LINE, width=1)
        f_m = cl.latin_font("mono", 16)
        mw = f_m.getlength(meta)
        d.text((x0 + pill_w / 2 - mw / 2, pill_top + 230),
               meta, font=f_m, fill=(110, 80, 80))

    # tagline capsule
    cl.contact_capsule(img,
                       bbox=(MARGIN + 40, 800, W - MARGIN - 40, 866),
                       text="เลือกเส้นทางมวยไทยของคุณ",
                       font=cl.thai_font("display", 30))

    footer_strip(img)
    img.save(os.path.join(OUT, "slide-1-cover.png"))

# ---------- Track-slide builder (slides 2, 3) ----------
def track_slide(idx, num_str, th_name, en_name, time_window, time_meta,
                prices, hot_idx, blurb_th, sunburst_pos, filename):
    img, d = slide_base(idx, sunburst=(sunburst_pos, 200), seed=20 + idx)

    # Track number (gold, top center)
    f_track = cl.latin_font("display", 30)
    track_label = f"TRACK  {idx - 1:02d}"  # slide 2 → TRACK 01, slide 3 → TRACK 02
    tw = f_track.getlength(track_label)
    d.text((W // 2 - tw / 2, 200), track_label, font=f_track, fill=cl.GOLD_HOT)

    # Headline (Thai, gold outlined)
    cl.headline_gold(d, (W // 2, 270), th_name,
                     cl.thai_font("display", 96), anchor="mm", outline_w=3)

    # English
    f_en = cl.latin_font("section", 28)
    ew = f_en.getlength(en_name)
    d.text((W // 2 - ew / 2, 332), en_name, font=f_en, fill=cl.IVORY_CARD)

    cl.gold_fleuron(d, W // 2, 380, 320)

    # Top white pill — the duration / time window
    pill_a = (MARGIN + 30, 410, W - MARGIN - 30, 540)
    cl.white_pill(img, pill_a, radius=20)
    # huge numeral on left
    f_num = cl.latin_font("display", 110)
    d.text((pill_a[0] + 50, pill_a[1] + 6), num_str, font=f_num, fill=cl.LACQUER)
    # 'min' label
    nw = f_num.getlength(num_str)
    d.text((pill_a[0] + 50 + nw + 10, pill_a[1] + 70),
           "min", font=cl.latin_font("body_bold", 30), fill=cl.LACQUER)
    # time window on right
    f_time = cl.latin_font("display", 56)
    f_tlabel = cl.latin_font("mono", 18)
    d.text((pill_a[2] - 48 - f_time.getlength(time_window), pill_a[1] + 22),
           time_window, font=f_time, fill=cl.INK_BODY)
    d.text((pill_a[2] - 48 - f_tlabel.getlength(time_meta), pill_a[1] + 84),
           time_meta, font=f_tlabel, fill=(110, 80, 80))

    # Bottom white pill — pricing rows
    pill_b = (MARGIN + 30, 565, W - MARGIN - 30, 820)
    cl.white_pill(img, pill_b, radius=20)
    # title row
    title = "อัตราค่าเรียน  /  PRICING"
    f_title = cl.thai_font("display", 26)
    d.text((pill_b[0] + 36, pill_b[1] + 16), title, font=f_title, fill=cl.LACQUER)
    d.text((pill_b[2] - 36 - cl.latin_font("mono", 18).getlength("THB"),
            pill_b[1] + 24),
           "THB", font=cl.latin_font("mono", 18), fill=(140, 100, 100))
    # divider under title
    d.line([(pill_b[0] + 36, pill_b[1] + 64), (pill_b[2] - 36, pill_b[1] + 64)],
           fill=cl.IVORY_LINE, width=1)

    # rows
    row_top = pill_b[1] + 76
    row_h = (pill_b[3] - 36 - row_top) / len(prices)
    for i, (count, price, note) in enumerate(prices):
        ry = row_top + row_h * (i + 0.5)
        # count
        d.text((pill_b[0] + 70, ry - 22),
               count, font=cl.thai_font("display", 30), fill=cl.INK_BODY)
        # price (centered)
        pf = cl.latin_font("mono", 44)
        pw = pf.getlength(price)
        d.text(((pill_b[0] + pill_b[2]) / 2 - pw / 2, ry - 28),
               price, font=pf, fill=cl.LACQUER)
        # note (right)
        if note:
            nf = cl.thai_font("body", 18)
            nw = nf.getlength(note)
            d.text((pill_b[2] - 50 - nw, ry - 12),
                   note, font=nf, fill=(120, 80, 80))
        # row hairline (between rows)
        if i > 0:
            d.line([(pill_b[0] + 36, row_top + row_h * i),
                    (pill_b[2] - 36, row_top + row_h * i)],
                   fill=cl.IVORY_LINE, width=1)
        # HOT badge straddling pill edge on featured row
        if i == hot_idx:
            cl.hot_badge(img, pill_b[0] + 8, int(ry), size=52, label="HOT!", angle_deg=-14)

    # blurb under pills (just above footer)
    if blurb_th:
        f_b = cl.thai_font("display", 22)
        bw = f_b.getlength(blurb_th)
        d.text((W // 2 - bw / 2, 858), blurb_th, font=f_b, fill=cl.IVORY_CARD)

    footer_strip(img)
    img.save(os.path.join(OUT, filename))

# ---------- Slide 2: Group ----------
def slide_2():
    track_slide(
        idx=2,
        num_str="60",
        th_name="คลาสกลุ่ม",
        en_name="GROUP  CLASS",
        time_window="14:00 → 19:00",
        time_meta="HOURLY · SIX START TIMES",
        prices=[
            ("1 ครั้ง",  "400",   ""),
            ("10 ครั้ง", "3,500", "อายุ 3 เดือน"),
            ("30 ครั้ง", "9,000", "อายุ 6 เดือน"),
        ],
        hot_idx=1,
        blurb_th="เริ่มต้นทุกชั่วโมงตอนบ่าย",
        sunburst_pos="tr",
        filename="slide-2-group.png",
    )

# ---------- Slide 3: Private ----------
def slide_3():
    track_slide(
        idx=3,
        num_str="90",
        th_name="ส่วนตัว",
        en_name="PRIVATE  TRAINING",
        time_window="07:00 → 12:00",
        time_meta="MORNINGS · ONE-ON-ONE",
        prices=[
            ("1 ครั้ง",  "700",    ""),
            ("10 ครั้ง", "5,990",  "อายุ 3 เดือน"),
            ("30 ครั้ง", "14,990", "อายุ 6 เดือน"),
        ],
        hot_idx=1,
        blurb_th="เลือกเวลาเรียนได้ ตั้งแต่ 7.00 - 12.00 น.",
        sunburst_pos="bl",
        filename="slide-3-private.png",
    )

# ---------- Slide 4: Staycation ----------
def slide_4():
    img, d = slide_base(4, sunburst=("br", 200), seed=24)

    f_track = cl.latin_font("display", 30)
    track_label = "TRACK  03"
    tw = f_track.getlength(track_label)
    d.text((W // 2 - tw / 2, 200), track_label, font=f_track, fill=cl.GOLD_HOT)

    cl.headline_gold(d, (W // 2, 270), "สเตย์เคชั่น",
                     cl.thai_font("display", 100), anchor="mm", outline_w=3)
    f_en = cl.latin_font("section", 28)
    ew = f_en.getlength("STAYCATION")
    d.text((W // 2 - ew / 2, 334), "STAYCATION", font=f_en, fill=cl.IVORY_CARD)

    # ritual line
    f_rit = cl.thai_font("display", 28)
    rit = "ฝึก  ·  กิน  ·  นอน  ·  ทำซ้ำ"
    rw = f_rit.getlength(rit)
    d.text((W // 2 - rw / 2, 376), rit, font=f_rit, fill=cl.GOLD_HOT)

    cl.gold_fleuron(d, W // 2, 422, 360)

    # Top inclusions pill
    pill_a = (MARGIN + 30, 450, W - MARGIN - 30, 668)
    cl.white_pill(img, pill_a, radius=20)
    title = "สิ่งที่รวมในแพ็กเกจ  /  WHAT'S INCLUDED"
    f_title = cl.thai_font("display", 24)
    d.text((pill_a[0] + 36, pill_a[1] + 16), title, font=f_title, fill=cl.LACQUER)
    d.line([(pill_a[0] + 36, pill_a[1] + 58), (pill_a[2] - 36, pill_a[1] + 58)],
           fill=cl.IVORY_LINE, width=1)

    items = [
        ("I.",   "ฝึก 2 รอบต่อวัน",          "TWO TRAINING SESSIONS DAILY"),
        ("II.",  "ที่พักในแคมป์",             "ON-SITE ACCOMMODATION"),
        ("III.", "อาหารเช้า + อาหารเย็น",   "BREAKFAST + DINNER INCLUDED"),
    ]
    iy = pill_a[1] + 80
    for roman, th_t, en_t in items:
        d.text((pill_a[0] + 60, iy), roman, font=cl.latin_font("mono", 24), fill=cl.GOLD_DEEP)
        d.text((pill_a[0] + 110, iy - 4), th_t, font=cl.thai_font("display", 26), fill=cl.INK_BODY)
        d.text((pill_a[0] + 110, iy + 28), en_t, font=cl.latin_font("mono", 14), fill=(140, 100, 100))
        iy += 50

    # Bottom pricing pill
    pill_b = (MARGIN + 30, 690, W - MARGIN - 30, 820)
    cl.white_pill(img, pill_b, radius=20)
    # left half: per day
    d.text((pill_b[0] + 50, pill_b[1] + 18),
           "ต่อวัน / PER DAY", font=cl.thai_font("body", 18), fill=(120, 80, 80))
    d.text((pill_b[0] + 50, pill_b[1] + 42),
           "1,000", font=cl.latin_font("mono", 56), fill=cl.LACQUER)
    d.text((pill_b[0] + 220, pill_b[1] + 70),
           "บาท", font=cl.thai_font("body", 22), fill=cl.INK_BODY)

    # divider
    midx = (pill_b[0] + pill_b[2]) // 2
    d.line([(midx, pill_b[1] + 18), (midx, pill_b[3] - 18)],
           fill=cl.IVORY_LINE, width=1)

    # right half: per month
    d.text((midx + 40, pill_b[1] + 18),
           "ต่อเดือน / PER MONTH", font=cl.thai_font("body", 18), fill=(120, 80, 80))
    d.text((midx + 40, pill_b[1] + 42),
           "25,000", font=cl.latin_font("mono", 56), fill=cl.LACQUER)
    d.text((midx + 240, pill_b[1] + 70),
           "บาท", font=cl.thai_font("body", 22), fill=cl.INK_BODY)

    # HOT! on right (per month is the standout offer)
    cl.hot_badge(img, midx + 18, pill_b[1] + 64, size=46, label="HOT!", angle_deg=-12)

    # tagline
    f_b = cl.thai_font("display", 22)
    blurb = "อยู่ ฝึก กิน นอน ที่ค่ายเดียวกัน"
    bw = f_b.getlength(blurb)
    d.text((W // 2 - bw / 2, 858), blurb, font=f_b, fill=cl.IVORY_CARD)

    footer_strip(img)
    img.save(os.path.join(OUT, "slide-4-staycation.png"))

# ---------- Slide 5: Pricing snapshot ----------
def slide_5():
    img, d = slide_base(5, sunburst=("tr", 220), seed=27)

    cl.headline_gold(d, (W // 2, 240), "อัตราค่าเรียน",
                     cl.thai_font("display", 88), anchor="mm", outline_w=3)
    f_en = cl.latin_font("section", 24)
    ew = f_en.getlength("PRICING  SNAPSHOT")
    d.text((W // 2 - ew / 2, 296), "PRICING  SNAPSHOT", font=f_en, fill=cl.IVORY_CARD)
    cl.gold_fleuron(d, W // 2, 344, 360)

    # three vertical pills side-by-side
    cols = [
        {
            "tag":  "01",
            "th":   "คลาสกลุ่ม",
            "en":   "GROUP",
            "meta": "60′ · 14:00–19:00",
            "rows": [("1", "400"), ("10", "3,500"), ("30", "9,000")],
        },
        {
            "tag":  "02",
            "th":   "ส่วนตัว",
            "en":   "PRIVATE",
            "meta": "90′ · 07:00–12:00",
            "rows": [("1", "700"), ("10", "5,990"), ("30", "14,990")],
        },
        {
            "tag":  "03",
            "th":   "สเตย์เคชั่น",
            "en":   "STAYCATION",
            "meta": "TRAIN · EAT · SLEEP",
            "rows": [("DAY", "1,000"), ("MONTH", "25,000"), ("INCL.", "MEALS")],
        },
    ]
    pill_top = 380
    pill_h = 470
    gap = 18
    pill_w = (W - 2 * MARGIN - gap * 2) // 3
    for i, c in enumerate(cols):
        x0 = MARGIN + i * (pill_w + gap)
        bbox = (x0, pill_top, x0 + pill_w, pill_top + pill_h)
        cl.white_pill(img, bbox, radius=20)

        # tag
        f_tag = cl.latin_font("mono", 22)
        d.text((x0 + 24, pill_top + 18), c["tag"], font=f_tag, fill=cl.GOLD_DEEP)

        # Thai name
        f_th = cl.thai_font("display", 32)
        tw = f_th.getlength(c["th"])
        d.text((x0 + pill_w / 2 - tw / 2, pill_top + 64),
               c["th"], font=f_th, fill=cl.INK_BODY)

        # English name
        f_en2 = cl.latin_font("section", 22)
        ew2 = f_en2.getlength(c["en"])
        d.text((x0 + pill_w / 2 - ew2 / 2, pill_top + 116),
               c["en"], font=f_en2, fill=cl.LACQUER)

        # meta
        f_m = cl.latin_font("mono", 13)
        mw = f_m.getlength(c["meta"])
        d.text((x0 + pill_w / 2 - mw / 2, pill_top + 154),
               c["meta"], font=f_m, fill=(120, 80, 80))

        # divider
        d.line([(x0 + 22, pill_top + 188), (x0 + pill_w - 22, pill_top + 188)],
               fill=cl.IVORY_LINE, width=1)

        # rows
        ry = pill_top + 220
        for label, val in c["rows"]:
            f_l = cl.latin_font("mono", 16)
            lw = f_l.getlength(label)
            d.text((x0 + pill_w / 2 - lw / 2, ry), label, font=f_l, fill=cl.GOLD_DEEP)

            f_v = cl.latin_font("mono", 38)
            vw = f_v.getlength(val)
            d.text((x0 + pill_w / 2 - vw / 2, ry + 22),
                   val, font=f_v, fill=cl.LACQUER)
            ry += 88

    # currency line
    f_c = cl.thai_font("body", 18)
    cap = "ทุกราคาเป็นเงินบาท  ·  ALL PRICES IN THAI BAHT"
    cw = f_c.getlength(cap)
    d.text((W // 2 - cw / 2, 870), cap, font=f_c, fill=cl.IVORY_CARD)

    footer_strip(img)
    img.save(os.path.join(OUT, "slide-5-pricing.png"))

# ---------- Slide 6: CTA ----------
def slide_6():
    img, d = slide_base(6, sunburst=("tr", 220), seed=33)
    # mirror sunburst bottom-left for symmetry
    cl.corner_sunburst(img, x=int(W * 0.14), y=int(H * 0.86), R=170)

    # Headline
    cl.headline_gold(d, (W // 2, 244), "ส่ง  TRAIN  มาทักเรา",
                     cl.thai_font("display", 76), anchor="mm", outline_w=3)
    f_en = cl.latin_font("section", 24)
    ew = f_en.getlength("SEND  ‘TRAIN’  AND WE'LL FIND YOUR PATH")
    d.text((W // 2 - ew / 2, 308), "SEND  ‘TRAIN’  AND WE'LL FIND YOUR PATH",
           font=f_en, fill=cl.IVORY_CARD)
    cl.gold_fleuron(d, W // 2, 356, 360)

    # Big white pill with the keyword
    pill_a = (MARGIN + 50, 390, W - MARGIN - 50, 540)
    cl.white_pill(img, pill_a, radius=24)
    quote = "“TRAIN”"
    f_q = cl.latin_font("display", 130)
    qw = f_q.getlength(quote)
    d.text(((pill_a[0] + pill_a[2]) / 2 - qw / 2, pill_a[1] + 4),
           quote, font=f_q, fill=cl.LACQUER)

    # Contact pill (white, with phone, IG, LINE QR)
    pill_b = (MARGIN + 30, 570, W - MARGIN - 30, 820)
    cl.white_pill(img, pill_b, radius=20)

    # Left side: textual contact
    f_lab = cl.latin_font("mono", 18)
    f_val = cl.latin_font("display", 30)
    f_th_v = cl.thai_font("display", 24)
    lx = pill_b[0] + 44

    rows = [
        ("PHONE",     "081-4455844", None),
        ("INSTAGRAM", "@PPAOINMUAYTHAI", None),
        ("TIKTOK",    "@PPAOINMUAYTHAI", None),
        ("LOCATION",  "พระราม 2  ·  กรุงเทพฯ", "thai"),
    ]
    ry = pill_b[1] + 30
    for label, val, kind in rows:
        d.text((lx, ry), label, font=f_lab, fill=cl.GOLD_DEEP)
        if kind == "thai":
            d.text((lx, ry + 22), val, font=f_th_v, fill=cl.INK_BODY)
        else:
            d.text((lx, ry + 18), val, font=f_val, fill=cl.INK_BODY)
        ry += 56

    # Right side: LINE QR (placeholder pattern)
    qr_size = 180
    qr_x = pill_b[2] - 44 - qr_size
    qr_y = pill_b[1] + 30
    d.rounded_rectangle([qr_x, qr_y, qr_x + qr_size, qr_y + qr_size],
                        radius=10, fill=cl.IVORY_CARD,
                        outline=cl.GOLD_DEEP, width=2)
    import random as _r
    rng = _r.Random(11)
    cell = (qr_size - 16) // 22
    for ix in range(22):
        for iy in range(22):
            if rng.random() > 0.55:
                d.rectangle([qr_x + 8 + ix * cell, qr_y + 8 + iy * cell,
                             qr_x + 8 + ix * cell + cell - 1,
                             qr_y + 8 + iy * cell + cell - 1],
                            fill=cl.INK_BODY)
    # corner finder patterns
    for (cx_, cy_) in [(qr_x + 12, qr_y + 12),
                       (qr_x + qr_size - 50, qr_y + 12),
                       (qr_x + 12, qr_y + qr_size - 50)]:
        d.rectangle([cx_, cy_, cx_ + 38, cy_ + 38], fill=cl.IVORY_CARD)
        d.rectangle([cx_ + 4, cy_ + 4, cx_ + 34, cy_ + 34], fill=cl.INK_BODY)
        d.rectangle([cx_ + 10, cy_ + 10, cx_ + 28, cy_ + 28], fill=cl.IVORY_CARD)
    f_line = cl.latin_font("display", 24)
    line_w = f_line.getlength("LINE")
    d.text((qr_x + qr_size / 2 - line_w / 2, qr_y + qr_size + 6),
           "LINE", font=f_line, fill=cl.LACQUER)

    # yellow capsule across bottom
    cl.contact_capsule(img,
                       bbox=(MARGIN + 50, 850, W - MARGIN - 50, 902),
                       text="มาร่วมสร้างสุขภาพดี  ที่ ค่ายมวย ป.เปาอินทร์",
                       font=cl.thai_font("display", 24))

    footer_strip(img)
    img.save(os.path.join(OUT, "slide-6-cta.png"))

# ---------- Run ----------
slide_1()
slide_2()
slide_3()
slide_4()
slide_5()
slide_6()
print("done")
