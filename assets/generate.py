#!/usr/bin/env python3
"""Build the front-page image for the news-image-20261120 entry.

Draws a 1024x1024 newspaper front page summing up Friday 20 November
2026's world news with PIL (DejaVu / Liberation fonts). This script runs
on the builder's machine only; the entry program (main.py) ships the
finished entry.png and copies it to /output, so grading needs no fonts
and no network. Deterministic: no randomness, no timestamps.

Stories (all reported 19-20 Nov 2026):
  lead  -- GTA VI day-one records: ~$1.84bn, 19.05m copies (Sensor Tower),
           7.9m peak stream viewers, record 33 Tbps internet traffic
  row 2 -- Trump-Xi-Putin trilateral summit in Shenzhen
           Houthi missile damages Riyadh's PIF Tower (KAFD)
  row 3 -- Cyclone Akvan: 80,000 evacuated in Odisha
           ICJ: Myanmar military "likely" intended Rohingya genocide
  ticker-- Kerch Bridge rail halted; Anthropic $1.5tn; Nicholls century;
           Voyager 1 one light-day; Fiji drought disaster; Seoul court
           clears ex-PM Han Duck-soo
"""

import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

PAPER = (247, 243, 232)
INK = (18, 22, 30)
NAVY = (22, 35, 63)
NAVY2 = (30, 48, 84)
MAGENTA = (196, 44, 112)
ORANGE = (232, 122, 48)
RED = (178, 34, 34)
GOLD = (212, 160, 23)
GOLD_LT = (232, 190, 80)
TEAL = (27, 127, 122)
SKY = (174, 214, 241)
SKY2 = (133, 193, 233)
SEA = (46, 94, 122)
GRAY = (120, 124, 128)
GRAY_DK = (90, 94, 98)
GRAY_LT = (210, 208, 198)
WHITE = (255, 255, 255)
SAND = (222, 196, 138)

FONTS = "/usr/share/fonts/truetype"


def serif(size, bold=False):
    name = "LiberationSerif-Bold.ttf" if bold else "LiberationSerif-Regular.ttf"
    return ImageFont.truetype(os.path.join(FONTS, "liberation", name), size)


def sans(size, bold=False):
    name = "LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf"
    return ImageFont.truetype(os.path.join(FONTS, "liberation", name), size)


def wrap(draw, text, font, max_w):
    """Greedy word wrap; returns a list of lines fitting max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def center(draw, cx, y, text, font, fill):
    draw.text((cx - draw.textlength(text, font=font) / 2, y), text,
              font=font, fill=fill)


# ------------------------------------------------------------------ pictures
def draw_vice_city(d, x, y, w, h):
    """Vice City at sunset: gradient bands, skyline, palms, neon VI."""
    bands = [(NAVY2, 0.34), (MAGENTA, 0.33), (ORANGE, 0.33)]
    yy = y
    for color, frac in bands:
        bh = int(h * frac)
        d.rectangle([x, yy, x + w, yy + bh], fill=color)
        yy += bh
    d.rectangle([x, yy, x + w, y + h], fill=ORANGE)
    # sun low over the skyline
    d.ellipse([x + w // 2 - 34, y + h - 118, x + w // 2 + 34, y + h - 50],
              fill=GOLD_LT)
    # stars in the dark band
    for sx, sy in ((x + 28, y + 14), (x + 96, y + 26), (x + 250, y + 12),
                   (x + 318, y + 30), (x + 186, y + 8), (x + 350, y + 18)):
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=WHITE)
    # skyline with lit windows
    base = y + h
    for bx, bw, bh in ((0, 52, 92), (56, 44, 126), (104, 60, 84),
                       (168, 48, 138), (220, 56, 100), (280, 60, 122),
                       (344, 36, 88)):
        d.rectangle([x + bx, base - bh, x + bx + bw, base], fill=INK)
        for wy in range(base - bh + 10, base - 8, 18):
            for wx in range(x + bx + 8, x + bx + bw - 8, 16):
                d.rectangle([wx, wy, wx + 5, wy + 6], fill=GOLD_LT)
    # palm silhouettes
    for px in (x + 26, x + w - 30):
        d.line([px, base, px + 4, base - 62], fill=INK, width=4)
        for dx, dy in ((-18, -8), (18, -8), (-14, -18), (14, -18),
                       (-4, -24), (6, -24)):
            d.line([px + 4, base - 60, px + 4 + dx, base - 60 + dy],
                   fill=INK, width=3)
    # neon VI
    f = serif(64, bold=True)
    center(d, x + w // 2, y + 26, "VI", f, WHITE)
    d.rectangle([x, y, x + w - 1, y + h - 1], outline=INK, width=2)


def draw_flags(d, x, y, w, h):
    """Three flags on poles: USA, China, Russia."""
    d.rectangle([x, y, x + w, y + h], fill=SKY2)
    d.rectangle([x, y + h - 24, x + w, y + h], fill=NAVY)
    for wx in range(x + 14, x + w - 14, 26):
        d.rectangle([wx, y + h - 18, wx + 5, y + h - 12], fill=GOLD_LT)
    fw, fh = (w - 60) // 3, 48
    poles = [x + 20, x + 20 + fw + 18, x + 20 + 2 * (fw + 18)]
    for px in poles:
        d.line([px, y + 8, px, y + h - 24], fill=WHITE, width=3)
    # USA
    ux = poles[0] + 3
    for s in range(7):
        d.rectangle([ux, y + 10 + s * (fh // 7), ux + fw,
                     y + 10 + (s + 1) * (fh // 7) + 1],
                    fill=RED if s % 2 == 0 else WHITE)
    d.rectangle([ux, y + 10, ux + fw // 2, y + 10 + fh // 2], fill=NAVY)
    for sy in range(3):
        for sx in range(3):
            d.ellipse([ux + 3 + sx * 7, y + 13 + sy * 7,
                       ux + 5 + sx * 7, y + 15 + sy * 7], fill=WHITE)
    # China
    cx = poles[1] + 3
    d.rectangle([cx, y + 10, cx + fw, y + 10 + fh], fill=(150, 40, 30))
    d.polygon([(cx + 12, y + 14), (cx + 15, y + 22), (cx + 23, y + 22),
               (cx + 17, y + 27), (cx + 19, y + 35), (cx + 12, y + 30),
               (cx + 5, y + 35), (cx + 7, y + 27), (cx + 1, y + 22),
               (cx + 9, y + 22)], fill=GOLD_LT)
    # Russia
    rx = poles[2] + 3
    d.rectangle([rx, y + 10, rx + fw, y + 10 + fh // 3 + 1], fill=WHITE)
    d.rectangle([rx, y + 10 + fh // 3, rx + fw, y + 10 + 2 * fh // 3 + 1],
                fill=(0, 87, 184))
    d.rectangle([rx, y + 10 + 2 * fh // 3, rx + fw, y + 10 + fh], fill=RED)
    d.rectangle([x, y, x + w - 1, y + h - 1], outline=INK, width=2)


def draw_tower(d, x, y, w, h):
    """PIF Tower in Riyadh: tall glass tower, blast, smoke."""
    d.rectangle([x, y, x + w, y + h], fill=(226, 214, 186))
    d.rectangle([x, y + h - 18, x + w, y + h], fill=GRAY_DK)
    # neighbouring blocks
    for bx, bw, bh in ((x + 8, 44, 52), (x + w - 56, 48, 64),
                       (x + w - 110, 40, 44)):
        d.rectangle([bx, y + h - 18 - bh, bx + bw, y + h - 18], fill=GRAY)
    # the tower: tall, twisted-glass look via diagonal sheen
    tx, tw = x + w // 2 - 42, 84
    d.rectangle([tx, y + 8, tx + tw, y + h - 18], fill=(70, 90, 110))
    d.polygon([(tx + 10, y + 8), (tx + 32, y + 8), (tx + 10, y + h - 18),
               (tx, y + h - 18)], fill=(120, 145, 165))
    for wy in range(y + 16, y + h - 26, 12):
        d.rectangle([tx + 6, wy, tx + tw - 6, wy + 4], fill=(200, 215, 225))
    # blast on the tower's upper floors
    bx, by = tx + tw // 2, y + 34
    for r, col in ((20, RED), (12, ORANGE), (6, GOLD_LT)):
        d.ellipse([bx - r, by - r, bx + r, by + r], fill=col)
    # smoke puffs
    for sx, sy, r in ((bx - 18, by - 20, 9), (bx + 16, by - 26, 11),
                      (bx + 2, by - 34, 8)):
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=GRAY)
    d.rectangle([x, y, x + w - 1, y + h - 1], outline=INK, width=2)


def draw_cyclone(d, x, y, w, h):
    """Cyclone Akvan: spiral over the Bay of Bengal."""
    d.rectangle([x, y, x + w, y + h], fill=SKY)
    d.rectangle([x, y + h - 30, x + w, y + h], fill=SEA)
    # land strip (Odisha coast) bottom-left
    d.polygon([(x, y + h - 30), (x + 90, y + h - 52), (x + 150, y + h - 34),
               (x + 120, y + h), (x, y + h)], fill=(120, 160, 110))
    # spiral bands
    cx, cy = x + w // 2 + 20, y + h // 2 - 6
    for r, col in ((44, WHITE), (34, (200, 225, 240)), (24, WHITE),
                   (14, (200, 225, 240))):
        d.arc([cx - r, cy - r, cx + r, cy + r], start=200, end=60,
              fill=col, width=7)
        d.arc([cx - r, cy - r, cx + r, cy + r], start=20, end=240,
              fill=col, width=7)
    d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=GOLD_LT)
    # rain slashes
    for rx, ry in ((x + 20, y + 16), (x + 60, y + 30), (x + w - 40, y + 20),
                   (x + w - 80, y + 36), (x + 30, y + 60)):
        d.line([rx, ry, rx - 8, ry + 16], fill=(90, 130, 170), width=3)
    d.rectangle([x, y, x + w - 1, y + h - 1], outline=INK, width=2)


def draw_scales(d, x, y, w, h):
    """The World Court: scales of justice over the Peace Palace."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 226, 205))
    d.rectangle([x, y + h - 22, x + w, y + h], fill=(150, 130, 100))
    # palace silhouette
    d.rectangle([x + w // 2 - 60, y + h - 66, x + w // 2 + 60, y + h - 22],
                fill=(170, 150, 115))
    d.polygon([(x + w // 2 - 66, y + h - 66), (x + w // 2, y + h - 88),
               (x + w // 2 + 66, y + h - 66)], fill=(140, 110, 80))
    # scales
    cx, top = x + w // 2, y + 18
    d.line([cx, top + 8, cx, y + h - 66], fill=INK, width=4)
    d.line([cx - 52, top + 14, cx + 52, top + 14], fill=INK, width=4)
    d.ellipse([cx - 4, top, cx + 4, top + 8], fill=GOLD)
    for sx in (cx - 52, cx + 52):
        d.line([sx, top + 14, sx - 16, top + 44], fill=INK, width=2)
        d.line([sx, top + 14, sx + 16, top + 44], fill=INK, width=2)
        d.arc([sx - 18, top + 36, sx + 18, top + 62], start=0, end=180,
              fill=GOLD, width=4)
    d.rectangle([x, y, x + w - 1, y + h - 1], outline=INK, width=2)


# ------------------------------------------------------------------ layout
def masthead(d):
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.rectangle([0, 114, W, 118], fill=GOLD)
    center(d, W // 2, 14, "THE WORLD IN ONE DAY", serif(54, bold=True), WHITE)
    center(d, W // 2, 80, "FRIDAY  20  NOVEMBER  2026",
           sans(24, bold=True), GOLD_LT)
    d.text((24, 20), "MAKE.FUN", font=sans(18, bold=True), fill=GRAY_LT)
    tag = "20 NOV 2026"
    d.text((W - 24 - d.textlength(tag, font=sans(18, bold=True)), 20), tag,
           font=sans(18, bold=True), fill=GRAY_LT)


def lead(d):
    draw_vice_city(d, 24, 140, 380, 232)
    tx, tw = 428, 572
    d.text((tx, 140), "GAMES", font=sans(20, bold=True), fill=RED)
    head = serif(47, bold=True)
    d.text((tx, 166), "GTA VI SMASHES", font=head, fill=INK)
    d.text((tx, 218), "EVERY RECORD", font=head, fill=INK)
    deck = ("Rockstar's sequel sold an estimated 19.05 million copies "
            "worth $1.84 billion in its first 24 hours, Sensor Tower "
            "reports \u2014 the biggest entertainment launch ever. A peak "
            "of 7.9 million people watched streams at once, and internet "
            "traffic hit a record 33 terabits a second. Take-Two's first "
            "official figures are expected today.")
    body = serif(20)
    yy = 276
    for line in wrap(d, deck, body, tw):
        d.text((tx, yy), line, font=body, fill=INK)
        yy += 24
    d.line([0, 396, W, 396], fill=GRAY_LT, width=2)


def panel(d, x, y, w, picto, kicker, headline, body_text):
    picto(d, x + 24, y + 16, w - 48, 96)
    ty = y + 124
    d.text((x + 24, ty), kicker, font=sans(17, bold=True), fill=RED)
    head = serif(29, bold=True)
    yy = ty + 24
    for line in wrap(d, headline, head, w - 48):
        d.text((x + 24, yy), line, font=head, fill=INK)
        yy += 33
    body = serif(18)
    yy += 2
    for line in wrap(d, body_text, body, w - 48):
        d.text((x + 24, yy), line, font=body, fill=INK)
        yy += 22


def ticker(d):
    y0 = 928
    d.rectangle([0, y0, W, H], fill=INK)
    d.rectangle([0, y0, W, y0 + 3], fill=GOLD)
    f = sans(17, bold=True)
    items = ("ALSO TODAY: KERCH BRIDGE RAIL LINK HALTED \u2022 ANTHROPIC "
             "VALUED AT $1.5TN \u2022 NICHOLLS CENTURY IN WELLINGTON TEST "
             "\u2022 VOYAGER 1 REACHES ONE LIGHT-DAY \u2022 FIJI DECLARES "
             "DROUGHT DISASTER \u2022 SEOUL COURT CLEARS EX-PM HAN "
             "DUCK-SOO \u2022 US, VENEZUELA RESTORE MILITARY TIES")
    lines = wrap(d, items, f, W - 48)
    for i, line in enumerate(lines[:3]):
        d.text((24, y0 + 12 + i * 26), line, font=f, fill=WHITE)


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    masthead(d)
    lead(d)
    panel(d, 0, 396, 512, draw_flags, "DIPLOMACY",
          "THREE LEADERS, ONE TABLE",
          "Trump, Xi and Putin hold the first-ever three-way summit in "
          "Shenzhen, talking nuclear arms control and global security.")
    panel(d, 512, 396, 512, draw_tower, "MIDDLE EAST",
          "MISSILE HITS RIYADH TOWER",
          "A Houthi strike damages the PIF Tower, the Saudi wealth fund's "
          "HQ and the city's tallest building \u2014 the second hit on the "
          "financial district in two weeks. No injuries.")
    panel(d, 0, 664, 512, draw_cyclone, "WEATHER",
          "CYCLONE AKVAN BEARS DOWN",
          "80,000 people evacuated in Odisha as the storm nears India's "
          "east coast; Andhra Pradesh on high alert as heavy rain begins.")
    panel(d, 512, 664, 512, draw_scales, "JUSTICE",
          "COURT: MYANMAR 'LIKELY' GENOCIDE",
          "The World Court rules Myanmar's military likely intended to "
          "destroy a substantial part of the Rohingya in 2017.")
    d.line([511, 396, 511, 928], fill=GRAY_LT, width=2)
    d.line([0, 664, W, 664], fill=GRAY_LT, width=2)
    ticker(d)
    return img


def main():
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "..", "entry.png")
    img = build()
    img.save(out, format="PNG", optimize=True)
    size = os.path.getsize(out)
    print(f"wrote {out}: {size} bytes, {img.size[0]}x{img.size[1]}")
    assert size <= 1_048_576, "over the 1 MiB cap"


if __name__ == "__main__":
    main()
