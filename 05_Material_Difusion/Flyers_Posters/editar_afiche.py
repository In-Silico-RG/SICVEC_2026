"""SICVEC 2026 poster: AC's image of 2026-09-28 with the corrections AC approved the same day.

Base: Versiones/2026-09-28_pre_flyers_comunicaciones/photo_2026-09-28_12-38-47.jpg (1024x1536).
Output: Afiche_SICVEC_2026.png (2048x3072) and .pdf. Run from this folder.
Box coordinates are in the base image's pixels; they are doubled on the upscaled canvas.
"""
import pathlib
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = pathlib.Path(__file__).parent
ROOT = HERE / "../.."
BASE = ROOT / "Versiones/2026-09-28_pre_flyers_comunicaciones/photo_2026-09-28_12-38-47.jpg"
LOGOS = ROOT / "01_Propuesta/Logos"
K = 2
BOLD = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"
HEAVY = "/usr/share/fonts/truetype/lato/Lato-Black.ttf"
REG = "/usr/share/fonts/truetype/lato/Lato-Regular.ttf"
VERDE_OSC = (14, 62, 42)
TINTA = (40, 52, 46)

im = Image.open(BASE).convert("RGB").resize((1024 * K, 1536 * K), Image.LANCZOS)
im = im.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
d = ImageDraw.Draw(im)


def box(x0, y0, x1, y1):
    return [int(v * K) for v in (x0, y0, x1, y1)]


def erase(x0, y0, x1, y1):
    """Fill a box with a horizontal blend of the colours just outside its left and right edges."""
    X0, Y0, X1, Y1 = box(x0, y0, x1, y1)
    for y in range(Y0, Y1):
        l, r = im.getpixel((X0 - 3, y)), im.getpixel((X1 + 3, y))
        for x in range(X0, X1):
            t = (x - X0) / max(1, X1 - X0)
            im.putpixel((x, y), tuple(int(l[i] + (r[i] - l[i]) * t) for i in range(3)))


def write(cx, y, s, size, font=BOLD, fill=VERDE_OSC, anchor="ma"):
    d.text((cx * K, y * K), s, font=ImageFont.truetype(font, int(size * K)), fill=fill, anchor=anchor)


# 1. Speaker names (AC, 2026-09-28): "Dr. Wilson M. Castro", "Dra. Marianny Y. Combariza"
for cx, l1, l2 in [(404, "Dr. Wilson M.", "Castro"), (878, "Dra. Marianny Y.", "Combariza")]:
    erase(cx - 105, 667, cx + 105, 717)
    write(cx, 668, l1, 19, HEAVY)
    write(cx, 692, l2, 19, HEAVY)

# 1b. Five keynotes (AC, 2026-09-30): Enrico Valli (Università di Bologna, online) added as a fifth card, built from
# the Renon Eller card; the four cards are scaled down to fit five in the row. Order as on the website (Valli first).
# Coordinates here are full-resolution pixels of the upscaled canvas (base * K).
def fill_blend(img, x0, y0, x1, y1):
    """Like erase(), on any image and in its own pixels."""
    for y in range(y0, y1):
        l, r = img.getpixel((x0 - 3, y)), img.getpixel((x1 + 3, y))
        for x in range(x0, x1):
            t = (x - x0) / max(1, x1 - x0)
            img.putpixel((x, y), tuple(int(l[i] + (r[i] - l[i]) * t) for i in range(3)))


CARDS = [(88, 1062, 556, 1780), (580, 1062, 1034, 1780), (1056, 1062, 1503, 1780), (1525, 1062, 1983, 1780)]
cards = [im.crop((x0 - 4, y0 - 4, x1 + 5, y1 + 5)) for x0, y0, x1, y1 in CARDS]
valli = cards[2].copy()                      # Renon Eller card; its crop origin is (1052, 1058)
ox, oy = 1052, 1058
for x0, y0, x1, y1 in [(1150, 1335, 1420, 1432), (1100, 1440, 1460, 1548),      # name, institution
                       (1096, 1608, 1238, 1706), (1086, 1706, 1250, 1748),      # flag, country
                       (1298, 1612, 1462, 1750)]:                               # logo
    fill_blend(valli, x0 - ox, y0 - oy, x1 - ox, y1 - oy)
dv = ImageDraw.Draw(valli)
cx = valli.width // 2
dv.text((cx, 1336 - oy), "Prof. Enrico", font=ImageFont.truetype(HEAVY, 19 * K), fill=VERDE_OSC, anchor="ma")
dv.text((cx, 1384 - oy), "Valli", font=ImageFont.truetype(HEAVY, 19 * K), fill=VERDE_OSC, anchor="ma")
dv.text((cx, 1462 - oy), "Università di", font=ImageFont.truetype(REG, 15.5 * K), fill=TINTA, anchor="ma")
dv.text((cx, 1500 - oy), "Bologna (en línea)", font=ImageFont.truetype(REG, 15.5 * K), fill=TINTA, anchor="ma")
fx0, fy0, fx1, fy1 = 1104 - ox, 1618 - oy, 1228 - ox, 1698 - oy       # Italian flag, same size as the Brazilian one
w3 = (fx1 - fx0) / 3
for i, c in enumerate([(0, 146, 70), (244, 245, 240), (206, 43, 55)]):
    dv.rectangle([int(fx0 + i * w3), fy0, int(fx0 + (i + 1) * w3), fy1], fill=c)
dv.rounded_rectangle([fx0, fy0, fx1, fy1], radius=6, outline=(205, 210, 200), width=2)
dv.text(((fx0 + fx1) // 2, 1712 - oy), "Italia", font=ImageFont.truetype(REG, 15 * K), fill=TINTA, anchor="ma")
seal = Image.open(LOGOS / "logo_unibo_sigillo.png").convert("RGBA")   # Wikimedia Commons, Seal of the University of Bologna
seal = seal.resize((118, 118), Image.LANCZOS)
valli.paste(seal, (1379 - ox - 59, 1681 - oy - 59), seal)

# Speaker photos (AC, 2026-09-30: "¿y las fotos de los ponentes?") in the round frames, instead of the silhouettes.
# Same square crops as the website (app/sicvec/static/speaker_*.jpg). Circle: centre 1.5 px right of the card centre,
# y = 1199.5, radius 108 (measured on the Renon Eller card).
STATIC = ROOT / "app/sicvec/static"


def put_photo(card, card_box, photo):
    x0, y0, x1, y1 = card_box
    cx, cy, r = (x1 - x0) / 2 + 1.5 + 4, 1199.5 - (y0 - 4), 106
    ph = Image.open(STATIC / photo).convert("RGB").resize((2 * r, 2 * r), Image.LANCZOS)
    mask = Image.new("L", (8 * r, 8 * r), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, 8 * r - 1, 8 * r - 1], fill=255)
    mask = mask.resize((2 * r, 2 * r), Image.LANCZOS)            # anti-aliased edge
    card.paste(ph, (round(cx - r), round(cy - r)), mask)
    ImageDraw.Draw(card).ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], outline=(27, 94, 58), width=4)


for c, b, ph in zip(cards, CARDS, ["speaker_escobar.jpg", "speaker_castro.jpg", "speaker_renon.jpg", "speaker_combariza.jpg"]):
    put_photo(c, b, ph)
put_photo(valli, CARDS[2], "speaker_valli.jpg")

fill_blend(im, 62, 1040, 2008, 1802)          # clear the row (page background)
row = [valli] + cards
GAP, X0, X1, TOP, BOT = 22, 70, 1998, 1062, 1780
f = (X1 - X0 - GAP * (len(row) - 1)) / sum(c.width for c in row)
x = X0
for c in row:
    c = c.resize((round(c.width * f), round(c.height * f)), Image.LANCZOS)
    im.paste(c, (round(x), TOP + (BOT - TOP - c.height) // 2))
    x += c.width + GAP
d = ImageDraw.Draw(im)

# 2. Venue (AC, 2026-09-28): "Lugar: CC Guacarí, Sincelejo ..." in the map block; the online (PDF) version links to Maps.
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=Centro+Comercial+Guacar%C3%AD+Sincelejo+Sucre"  # same as the app
erase(480, 1190, 580, 1250)
write(483, 1187, "Lugar:", 17, BOLD, VERDE_OSC, "la")
write(483, 1209, "C.C. Guacarí", 15.5, BOLD, TINTA, "la")
write(483, 1230, "Sincelejo, Sucre", 13, REG, TINTA, "la")
LINK_BOXES = [(120, 1180, 580, 1260)]  # pin + map blocks, base-image pixels

# 3. QR code (AC, 2026-09-30: "only one QR needed now, pointing to the web page"). Left box: QR to the home page,
# label "QR Página web"; right box: the QR is replaced by the call for abstracts (calendar of 30 Sept).
# Needs `segno` (pip install segno). The PDF also links both boxes to the site.
import io
import segno
SITE = "https://sicvec2026.eu.pythonanywhere.com"
erase(70, 983, 152, 1064)
buf = io.BytesIO()
segno.make(SITE, error="m").save(buf, kind="png", scale=10, border=1, dark="#0e3e2a", light="#ffffff")
qr = Image.open(buf).convert("RGB").resize((78 * K, 78 * K), Image.NEAREST)
im.paste(qr, (int(72 * K), int(985 * K)))
erase(190, 975, 338, 1066)
write(200, 984, "QR", 24, BOLD, TINTA, "la")
write(200, 1012, "Página web", 22, BOLD, TINTA, "la")
write(200, 1046, "Inscripción, resúmenes", 11, REG, TINTA, "la")
write(200, 1061, "y programa", 11, REG, TINTA, "la")
erase(712, 950, 990, 1102)
write(851, 962, "Convocatoria abierta", 19, BOLD, TINTA)
write(851, 992, "Resúmenes hasta el", 15, REG, TINTA)
write(851, 1013, "10 de octubre", 24, HEAVY, VERDE_OSC)
write(851, 1052, "Ponencias orales · Pósteres", 13, REG, TINTA)
QR_LINKS = [((30, 945, 345, 1110), SITE), ((695, 945, 995, 1110), SITE + "/enviar")]

# 4. Footer (AC, 2026-09-28): ORGANIZAN IN SILICO + UNISUCRE; COLABORAN the departments; no sponsors
FY = 1394
d.rectangle(box(0, FY, 1024, 1536), fill=(255, 255, 255))
LINE = (150, 190, 185)


def heading(cx, y, s, half):
    f = ImageFont.truetype(BOLD, 13 * K)
    w = d.textlength(s, font=f) / K
    write(cx, y, s, 13, BOLD, VERDE_OSC)
    for a, b in [(cx - half, cx - w / 2 - 14), (cx + w / 2 + 14, cx + half)]:
        d.line(box(a, y + 9, b, y + 9), fill=LINE, width=2)


def logo(path, cx, cy, h, maxw=10**6, white_to_alpha=False):
    lg = Image.open(path).convert("RGBA")
    s = min(h * K / lg.height, maxw * K / lg.width)
    lg = lg.resize((int(lg.width * s), int(lg.height * s)), Image.LANCZOS)
    im.paste(lg, (int(cx * K - lg.width / 2), int(cy * K - lg.height / 2)), lg)


heading(215, FY + 25, "ORGANIZAN", 170)
logo(LOGOS / "logo_unisucre.png", 135, FY + 88, 72, 150)
logo(LOGOS / "Logo_insilico.jpeg", 300, FY + 88, 72, 150)
d.line(box(430, FY + 25, 430, FY + 130), fill=LINE, width=2)
heading(727, FY + 25, "COLABORAN", 260)
for i, f in enumerate(["Logo_Bio.png", "logo_agroin.png", "logo_ingagrocola.png"]):
    logo(LOGOS / f, 537 + i * 125, FY + 88, 68, 110)
# Física: LIFI logo sent by AC 2026-09-30 (was a text box "Departamento de Física")
logo(LOGOS / "logo_fisica_lifi_transparente.png", 920, FY + 88, 68, 110)

im.save(HERE / "Afiche_SICVEC_2026.png", optimize=True)
DPI = 260  # 2048 px / 260 dpi = 20 cm wide
im.save(HERE / "Afiche_SICVEC_2026.pdf", resolution=DPI)

# clickable links (PDF only): Google Maps over the venue blocks, the site over the QR codes
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
w = PdfWriter(clone_from=PdfReader(HERE / "Afiche_SICVEC_2026.pdf"))
pt = 72 / DPI * K
H = 1536 * pt
for (x0, y0, x1, y1), url in [(b, MAPS_URL) for b in LINK_BOXES] + QR_LINKS:
    ann = Link(rect=(x0 * pt, H - y1 * pt, x1 * pt, H - y0 * pt), url=url)
    w.add_annotation(page_number=0, annotation=ann)
w.write(HERE / "Afiche_SICVEC_2026.pdf")
print("ok", im.size)
