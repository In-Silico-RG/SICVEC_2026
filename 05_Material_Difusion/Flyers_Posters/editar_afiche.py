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

# 2. Venue (AC, 2026-09-28): "Lugar: CC Guacarí, Sincelejo ..." in the map block; the online (PDF) version links to Maps.
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=Centro+Comercial+Guacar%C3%AD+Sincelejo+Sucre"  # same as the app
erase(480, 1190, 580, 1250)
write(483, 1187, "Lugar:", 17, BOLD, VERDE_OSC, "la")
write(483, 1209, "C.C. Guacarí", 15.5, BOLD, TINTA, "la")
write(483, 1230, "Sincelejo, Sucre", 13, REG, TINTA, "la")
LINK_BOXES = [(120, 1180, 580, 1260)]  # pin + map blocks, base-image pixels

# 3. QR codes do not exist yet (no public URL): placeholder text inside the brackets
for x in (70, 740):
    erase(x, 983, x + 82, 1064)
    write(x + 41, 1012, "Próxima-", 13, BOLD, VERDE_OSC)
    write(x + 41, 1029, "mente", 13, BOLD, VERDE_OSC)

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
# Física: logo not available yet
d.rounded_rectangle(box(870, FY + 60, 970, FY + 116), radius=8 * K, fill=(232, 238, 234))
write(920, FY + 67, "Departamento", 11, BOLD, VERDE_OSC)
write(920, FY + 84, "de Física", 15, BOLD, VERDE_OSC)

im.save(HERE / "Afiche_SICVEC_2026.png", optimize=True)
DPI = 260  # 2048 px / 260 dpi = 20 cm wide
im.save(HERE / "Afiche_SICVEC_2026.pdf", resolution=DPI)

# clickable Google Maps link over the venue blocks (PDF only)
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
w = PdfWriter(clone_from=PdfReader(HERE / "Afiche_SICVEC_2026.pdf"))
pt = 72 / DPI * K
H = 1536 * pt
for x0, y0, x1, y1 in LINK_BOXES:
    ann = Link(rect=(x0 * pt, H - y1 * pt, x1 * pt, H - y0 * pt), url=MAPS_URL)
    w.add_annotation(page_number=0, annotation=ann)
w.write(HERE / "Afiche_SICVEC_2026.pdf")
print("ok", im.size)
