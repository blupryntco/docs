#!/usr/bin/env python3
"""Draw numbered callouts and redactions on a screenshot.

Usage: scripts/annotate.py in.png out.png spec.json

spec.json:
  {"scale": 2,                       # device pixel ratio of in.png (coords below are CSS px)
   "callouts": [{"box": [x, y, w, h], "n": 1}],
   "redact":   [[x, y, w, h]]}
Callouts: 3px #007BFF rounded box plus a numbered badge at its top-left corner.
Redactions: solid #E5E7EB fill (use for emails, names, keys, wallet balances).
Refer to the badge numbers from the page text ("1 Search your company").
"""
import json, sys
from PIL import Image, ImageDraw, ImageFont

BLUE = (0, 123, 255)
src, dst, spec_path = sys.argv[1:4]
spec = json.load(open(spec_path))
s = spec.get("scale", 2)
img = Image.open(src).convert("RGB")
d = ImageDraw.Draw(img)
for x, y, w, h in spec.get("redact", []):
    d.rounded_rectangle([x * s, y * s, (x + w) * s, (y + h) * s], radius=4 * s, fill=(229, 231, 235))
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(13 * s))
except OSError:
    font = ImageFont.load_default()
for c in spec.get("callouts", []):
    x, y, w, h = c["box"]
    d.rounded_rectangle([x * s, y * s, (x + w) * s, (y + h) * s], radius=8 * s, outline=BLUE, width=3 * s)
    r = 12 * s
    cx, cy = x * s, y * s
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLUE, outline=(255, 255, 255), width=2 * s)
    d.text((cx, cy), str(c["n"]), fill=(255, 255, 255), font=font, anchor="mm")
img.save(dst, optimize=True)
