"""Social banners derived directly from the approved poster (Flyers_Posters/Afiche_SICVEC_2026*.png) --
no new design, just crops/resizes of the existing artwork, per AC's request 2026-10-07.

Post (1080x1080): top square crop (hero + dates + CONFERENCISTAS). The poster is 2048 wide, so this
is literally the top 2048x2048 px, resized down to 1080x1080.

Story (1080x1920): the full poster height, width-trimmed to the 9:16 ratio (keeps every section,
just crops the decorative side margins), resized down to 1080x1920.

Run from this folder: `python crear_banners.py`.
"""
import pathlib
from PIL import Image

HERE = pathlib.Path(__file__).parent
POSTERS = HERE / "../Flyers_Posters"
SUFFIXES = {"es": "", "en": "_EN", "pt": "_PT"}

for lang, suf in SUFFIXES.items():
    src = POSTERS / f"Afiche_SICVEC_2026{suf}.png"
    im = Image.open(src).convert("RGB")
    w, h = im.size  # 2048 x 3072

    # Post: top square crop, resized to 1080x1080.
    post = im.crop((0, 0, w, w)).resize((1080, 1080), Image.LANCZOS)
    post.save(HERE / f"Banner_Post_SICVEC_2026{suf}.png", optimize=True)

    # Story: the footer band (Organiza/Apoyan/Universidad de Sucre) runs edge to edge, so trimming its
    # width like the rest clips "ORGANIZA"/"ORGANISED BY" and "Universidad de Sucre" at the sides (AC,
    # 2026-10-07: "se salen las cosas de la imagen"). Instead, keep the footer's full width and shrink it
    # to fit; only the content above it (which already has margin) gets width-trimmed to the 9:16 ratio.
    FOOTER_Y = 2760
    target_ratio = 1080 / 1920
    crop_w = round(h * target_ratio)
    x0 = (w - crop_w) // 2
    main = im.crop((x0, 0, x0 + crop_w, FOOTER_Y))
    footer = im.crop((0, FOOTER_Y, w, h))
    footer = footer.resize((crop_w, round(footer.height * crop_w / w)), Image.LANCZOS)
    combined = Image.new("RGB", (crop_w, main.height + footer.height), (255, 255, 255))
    combined.paste(main, (0, 0))
    combined.paste(footer, (0, main.height))
    story = combined.resize((1080, 1920), Image.LANCZOS)
    story.save(HERE / f"Banner_Story_SICVEC_2026{suf}.png", optimize=True)

    print(f"{lang}: post {post.size}, story {story.size}")
