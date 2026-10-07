"""SICVEC 2026 poster: AC's image of 2026-09-28 with the corrections AC approved the same day.

Base: Versiones/2026-09-28_pre_flyers_comunicaciones/photo_2026-09-28_12-38-47.jpg (1024x1536).
Output: Afiche_SICVEC_2026{,_EN,_PT}.png (2048x3072) and .pdf. Run from this folder: `python editar_afiche.py [es|en|pt]`.
Box coordinates are in the base image's pixels; they are doubled on the upscaled canvas.
AC, 2026-09-30: "the flyers/afiche in 3 languages" -> texts baked into the base image are painted over and rewritten
for en/pt (subtitle, date, heading, hybrid block, contact label, country names, "Dra.").
"""
import pathlib
import sys
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
GRIS = (92, 94, 92)

LANG = sys.argv[1] if len(sys.argv) > 1 else "es"
SUFFIX = {"es": "", "en": "_EN", "pt": "_PT"}[LANG]
T = {
    "es": dict(sub=None, date=None, conf=None, hybrid=None, contact=None, colombia=None,
               countries=None, dra="Dra.", valli2="Bologna (en línea)", italy="Italia",
               lugar="Lugar:", venue="C.C. Guacarí", city="Sincelejo, Sucre",
               qr=["QR", "Página web", "Inscripción, resúmenes", "y programa"],
               call=["Convocatoria abierta", "Resúmenes hasta el", "12 de octubre", "Ponencias orales · Pósteres"],
               axes="EJES TEMÁTICOS", sdg="ODS 12 · 13 · 15 · 17", org="ORGANIZA", sup="APOYAN"),
    "en": dict(sub=["1ST INTERNATIONAL SYMPOSIUM ON GREEN", "SCIENCE AND CIRCULAR ECONOMY"], date=["19–20", "October"],
               conf="KEYNOTE SPEAKERS", hybrid=["IN PERSON + ONLINE", "HYBRID"], contact="Contact:", colombia=None,
               countries=["Mexico", "Peru", "Brazil", "Colombia"], dra="Dr.", valli2="Bologna (online)", italy="Italy",
               lugar="Venue:", venue="C.C. Guacarí", city="Sincelejo, Sucre",
               qr=["QR", "Website", "Registration, abstracts", "and programme"],
               call=["Call for abstracts", "Abstracts due by", "12 October", "Oral talks · Posters"],
               axes="THEMATIC AXES", sdg="SDGs 12 · 13 · 15 · 17", org="ORGANISED BY", sup="SUPPORTED BY"),
    "pt": dict(sub=["I SIMPÓSIO INTERNACIONAL DE CIÊNCIA", "VERDE E ECONOMIA CIRCULAR"], date=["19 e 20", "de outubro"],
               conf="PALESTRANTES", hybrid=None, contact="Contato:", colombia="(Colômbia)",
               countries=["México", "Peru", "Brasil", "Colômbia"], dra="Dra.", valli2="Bologna (on-line)", italy="Itália",
               lugar="Local:", venue="C.C. Guacarí", city="Sincelejo, Sucre",
               qr=["QR", "Site", "Inscrição, resumos", "e programação"],
               call=["Chamada aberta", "Resumos até", "12 de outubro", "Apresentações orais · Pôsteres"],
               axes="EIXOS TEMÁTICOS", sdg="ODS 12 · 13 · 15 · 17", org="ORGANIZAÇÃO", sup="APOIO"),
}[LANG]

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


def spaced(cx, y, s, size, font, fill, track):
    """Letter-spaced text centred on cx (base px); track in em."""
    f = ImageFont.truetype(font, int(size * K))
    ws = [d.textlength(ch, font=f) for ch in s]
    total = sum(ws) + track * size * K * (len(s) - 1)
    x = cx * K - total / 2
    for ch, w in zip(s, ws):
        d.text((x, y * K), ch, font=f, fill=fill, anchor="la")
        x += w + track * size * K
    return total / K


def fit(s, size, font, maxw):
    """Largest size <= size so that s fits in maxw base px."""
    while size > 8 and d.textlength(s, font=ImageFont.truetype(font, int(size * K))) / K > maxw:
        size -= 0.5
    return size


# 0. Translation of the texts baked into the base image (en/pt only).
if T["sub"]:
    erase(510, 262, 990, 304)
    sz = min(fit(T["sub"][0], 16.5, BOLD, 470), fit(T["sub"][1], 16.5, BOLD, 470))
    write(515, 265, T["sub"][0], sz, BOLD, GRIS, "la")
    write(515, 284, T["sub"][1], sz, BOLD, GRIS, "la")
if T["date"]:
    erase(728, 322, 990, 412)
    write(735, 322, T["date"][0], 44, HEAVY, VERDE_OSC, "la")
    write(735, 368, T["date"][1], 40, REG, VERDE_OSC, "la")
if T["conf"]:
    erase(34, 474, 990, 510)
    w = spaced(512, 480, T["conf"], 26, HEAVY, VERDE_OSC, 0.22)
    for a, b in [(40, 512 - w / 2 - 18), (512 + w / 2 + 18, 984)]:
        d.line(box(a, 492, b, 492), fill=(60, 110, 90), width=2)
if T["hybrid"]:
    erase(388, 1036, 644, 1090)
    spaced(516, 1041, T["hybrid"][0], 17, HEAVY, VERDE_OSC, 0.08)
    w = spaced(516, 1066, T["hybrid"][1], 15, BOLD, VERDE_OSC, 0.45)
    for a, b in [(400, 516 - w / 2 - 12), (516 + w / 2 + 12, 632)]:
        d.line(box(a, 1075, b, 1075), fill=(120, 150, 135), width=2)
if T["contact"]:
    erase(693, 1182, 838, 1212)
    write(700, 1186, T["contact"], 20, BOLD, TINTA, "la")
if T["colombia"]:
    erase(186, 1180, 364, 1244)                     # both lines: "Sincelejo, Sucre" has descenders in the way
    write(190, 1183, "Sincelejo, Sucre", 20, BOLD, (30, 58, 48), "la")
    write(190, 1212, T["colombia"], 19, REG, TINTA, "la")

# 1. Speaker names (AC, 2026-09-28): "Dr. Wilson M. Castro", "Dra. Marianny Y. Combariza"
for cx, l1, l2 in [(404, "Dr. Wilson M.", "Castro"), (878, T["dra"] + " Marianny Y.", "Combariza")]:
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
dv.text((cx, 1500 - oy), T["valli2"], font=ImageFont.truetype(REG, 15.5 * K), fill=TINTA, anchor="ma")
fx0, fy0, fx1, fy1 = 1104 - ox, 1618 - oy, 1228 - ox, 1698 - oy       # Italian flag, same size as the Brazilian one
w3 = (fx1 - fx0) / 3
for i, c in enumerate([(0, 146, 70), (244, 245, 240), (206, 43, 55)]):
    dv.rectangle([int(fx0 + i * w3), fy0, int(fx0 + (i + 1) * w3), fy1], fill=c)
dv.rounded_rectangle([fx0, fy0, fx1, fy1], radius=6, outline=(205, 210, 200), width=2)
dv.text(((fx0 + fx1) // 2, 1712 - oy), T["italy"], font=ImageFont.truetype(REG, 15 * K), fill=TINTA, anchor="ma")
seal = Image.open(LOGOS / "logo_unibo_sigillo.png").convert("RGBA")   # Wikimedia Commons, Seal of the University of Bologna
seal = seal.resize((118, 118), Image.LANCZOS)
valli.paste(seal, (1379 - ox - 59, 1681 - oy - 59), seal)

# Card texts in en/pt: country names; "Dra." -> "Dr." in English (Escobar, Renon Eller; Combariza is in step 1).
if T["countries"]:
    for c, name in zip(cards, T["countries"]):
        fill_blend(c, 34, 648, 198, 690)
        ImageDraw.Draw(c).text((116, 652), name, font=ImageFont.truetype(REG, 15 * K), fill=TINTA, anchor="ma")
if T["dra"] != "Dra.":
    for i, first in [(0, "Beatriz"), (2, "Monique")]:
        c = cards[i]
        fill_blend(c, 60, 275, c.width - 60, 318)
        ImageDraw.Draw(c).text((c.width // 2, 278), T["dra"] + " " + first, font=ImageFont.truetype(HEAVY, 19 * K),
                               fill=VERDE_OSC, anchor="ma")
    fill_blend(valli, 60, 275, valli.width - 60, 318)   # Valli card is a copy of Renon Eller's: keep "Prof. Enrico"
    ImageDraw.Draw(valli).text((valli.width // 2, 278), "Prof. Enrico", font=ImageFont.truetype(HEAVY, 19 * K),
                               fill=VERDE_OSC, anchor="ma")

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
GAP, TOP, f = 22, 1030, 0.70   # 0.70 (was 0.80) to make room for the axes/SDG strip (step 3b)
widths = [round(c.width * f) for c in row]
x = (2048 - sum(widths) - GAP * (len(row) - 1)) / 2
for c in row:
    c = c.resize((round(c.width * f), round(c.height * f)), Image.LANCZOS)
    im.paste(c, (round(x), TOP))
    x += c.width + GAP
d = ImageDraw.Draw(im)

# 2. Venue (AC, 2026-09-28): "Lugar: CC Guacarí, Sincelejo ..." in the map block; the online (PDF) version links to Maps.
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=Centro+Comercial+Guacar%C3%AD+Sincelejo+Sucre"  # same as the app
# AC, 2026-09-30: Guacarí logo (official, parquecomercialguacari.com, 01_Propuesta/Logos/logo_guacari.png) in place of
# the map icon, and the venue written out next to it ("ESCRIBE CC GUACARÍ EXPLÍCITAMENTE": the logo's text is too small).
erase(480, 1172, 582, 1262)
write(483, 1187, T["lugar"], 17, BOLD, VERDE_OSC, "la")
write(483, 1209, T["venue"], 15.5, BOLD, TINTA, "la")
write(483, 1230, T["city"], 13, REG, TINTA, "la")
erase(386, 1172, 472, 1264)
gl = Image.open(LOGOS / "logo_guacari.png").convert("RGBA")
gl = gl.crop(gl.getbbox())
gl = gl.resize((round(gl.width * 82 * K / gl.height), 82 * K), Image.LANCZOS)
im.paste(gl, (round(429 * K - gl.width / 2), 1177 * K), gl)
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
write(200, 984, T["qr"][0], 24, BOLD, TINTA, "la")
write(200, 1012, T["qr"][1], 22, BOLD, TINTA, "la")
write(200, 1046, T["qr"][2], 11, REG, TINTA, "la")
write(200, 1061, T["qr"][3], 11, REG, TINTA, "la")
erase(712, 950, 990, 1102)
write(851, 962, T["call"][0], 19, BOLD, TINTA)
write(851, 992, T["call"][1], 15, REG, TINTA)
write(851, 1013, T["call"][2], 24, HEAVY, VERDE_OSC)
write(851, 1052, T["call"][3], fit(T["call"][3], 13, REG, 270), REG, TINTA)
QR_LINKS = [((30, 945, 345, 1110), SITE), ((695, 945, 995, 1110), SITE + "/enviar")]

# 3b. Axes and SDGs (AC, 2026-09-30: "¿podríamos meter ejes temáticos y ODS en el afiche?"): the FigureLabs figures
# (the site's Spanish copies) in a strip under the speaker cards; the QR row moves down 120 px (full resolution) into
# the space the smaller cards left. Venue row, wave and footer stay where they were.
qr_row = im.crop((0, 1885, 2048, 2225))
fill_blend(im, 8, 1550, 2040, 2345)
im.paste(qr_row, (0, 2005))
QR_LINKS = [((x0, y0 + 60, x1, y1 + 60), url) for (x0, y0, x1, y1), url in QR_LINKS]
FIG = ROOT / "app/sicvec/static"
H = 400
ejes = Image.open(FIG / f"fig_ejes_{LANG}.jpg").convert("RGB")
ods = Image.open(FIG / f"fig_ods_{LANG}.jpg").convert("RGB")
ejes = ejes.resize((round(ejes.width * H / ejes.height), H), Image.LANCZOS)
ods = ods.resize((round(ods.width * H / ods.height), H), Image.LANCZOS)
FGAP = 50
fx = (2048 - ejes.width - ods.width - FGAP) // 2
for img, x, title in [(ejes, fx, T["axes"]), (ods, fx + ejes.width + FGAP, T["sdg"])]:
    m = Image.new("L", img.size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, img.width - 1, img.height - 1], radius=18, fill=255)
    im.paste(img, (x, 1592), m)
    d.rounded_rectangle([x - 1, 1591, x + img.width, 1592 + img.height], radius=18, outline=(200, 214, 204), width=2)
    d.text((x + img.width // 2, 1552), title, font=ImageFont.truetype(BOLD, 13 * K), fill=VERDE_OSC, anchor="ma")

# 4. Footer
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


# AC, 2026-10-07: single row -- ORGANIZA = IN SILICO (smaller); APOYAN = the four departments; UNISUCRE at the
# right end of the same row (was centred on a row below; AC: "no me gusta el pie... logo insilico mas pequeno...
# logo unisucre a la derecha").
heading(110, FY + 6, T["org"], 85)
logo(LOGOS / "Logo_insilico.jpeg", 110, FY + 52, 45, 150)
d.line(box(205, FY + 8, 205, FY + 84), fill=LINE, width=2)
heading(530, FY + 6, T["sup"], 310)
for cx, f in zip([320, 460, 600, 740], ["Logo_Bio.png", "logo_agroin.png", "logo_ingagrocola.png",
                                         "logo_fisica_lifi_transparente.png"]):
    logo(LOGOS / f, cx, FY + 52, 58, 120)
d.line(box(845, FY + 8, 845, FY + 84), fill=LINE, width=2)
logo(LOGOS / "logo_unisucre.png", 935, FY + 52, 55, 160)

OUT = f"Afiche_SICVEC_2026{SUFFIX}"
im.save(HERE / f"{OUT}.png", optimize=True)
DPI = 260  # 2048 px / 260 dpi = 20 cm wide
im.save(HERE / f"{OUT}.pdf", resolution=DPI)

# clickable links (PDF only): Google Maps over the venue blocks, the site over the QR codes
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
w = PdfWriter(clone_from=PdfReader(HERE / f"{OUT}.pdf"))
pt = 72 / DPI * K
H = 1536 * pt
for (x0, y0, x1, y1), url in [(b, MAPS_URL) for b in LINK_BOXES] + QR_LINKS:
    ann = Link(rect=(x0 * pt, H - y1 * pt, x1 * pt, H - y0 * pt), url=url)
    w.add_annotation(page_number=0, annotation=ann)
w.write(HERE / f"{OUT}.pdf")
print("ok", im.size)
