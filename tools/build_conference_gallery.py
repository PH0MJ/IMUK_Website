#!/usr/bin/env python3
"""Build the unlisted 35th-conference photo pages (UK and Iraq versions).

Reads c35/photos.json, then writes into c35/:
  photos/<slug>.jpg   framed full-size photo (sponsor strip along the bottom)
  thumbs/<slug>.jpg   framed thumbnail used in the gallery
  IMA-UK-EU-35th-Conference-Photos.zip   all framed photos
  <uk page>/index.html, <iq page>/index.html   the two unlisted pages

The original photos are NOT kept in the repo. Point --src at the folder that holds them
(file names are listed in c35/photos.json). To add photos later, add an entry to
photos.json (give it a "group") and run this script again; existing photos are kept
unless you pass --force (needed after changing the frame design).

usage: python tools/build_conference_gallery.py --src "C:/path/to/original/photos"
"""
import argparse
import hashlib
import html
import json
import urllib.parse
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent.parent
C35 = ROOT / "c35"
FONT = ROOT / "tools" / "fonts" / "PlusJakartaSans-Variable.ttf"
LOGO = C35 / "assets" / "caregrid-lockup.png"
CREST = "../../assets/images/WhatsApp_Image_2025-07-27_at_18.50.18-removebg-preview.png"

NAVY = (0, 51, 106)
TEAL = (6, 158, 133)
WHITE = (255, 255, 255)
MUTED = (100, 122, 146)
MAX_SIDE = 2400
THUMB_SIDE = 800
QUALITY = 82
ZIP_NAME = "IMA-UK-EU-35th-Conference-Photos.zip"
WHATSAPP = "9647823997303"
EMAIL = "founders@caregr.id"
IMA_EMAIL = "ima.uk.eu91@gmail.com"


# --------------------------------------------------------------------------- frame
def font(size, bold):
    f = ImageFont.truetype(str(FONT), size)
    f.set_variation_by_name("Bold" if bold else "Regular")
    return f


def text_w(draw, text, f):
    return draw.textlength(text, font=f)


def add_frame(photo, event):
    """Return the photo with the event + media-sponsor strip added below it."""
    photo = ImageOps.exif_transpose(photo).convert("RGB")
    scale = min(1.0, MAX_SIDE / max(photo.size))
    if scale < 1:
        photo = photo.resize((round(photo.width * scale), round(photo.height * scale)), Image.LANCZOS)
    w, h = photo.size
    sh = max(round(w * 0.08), 100)  # strip height
    out = Image.new("RGB", (w, h + sh), NAVY)
    out.paste(photo, (0, 0))
    d = ImageDraw.Draw(out)
    d.rectangle([0, h, w, h + max(3, sh // 26)], fill=TEAL)

    pad = round(sh * 0.3)
    # media-sponsor pill (right)
    pill_h = round(sh * 0.76)
    logo = Image.open(LOGO).convert("RGBA")
    logo_h = round(pill_h * 0.46)
    logo = logo.resize((round(logo.width * logo_h / logo.height), logo_h), Image.LANCZOS)
    label_f = font(max(11, round(pill_h * 0.17)), True)
    label = "MEDIA SPONSOR"
    inner = round(pill_h * 0.16)
    pill_w = max(logo.width, round(text_w(d, label, label_f))) + 2 * inner
    px, py = w - pad - pill_w, h + (sh - pill_h) // 2
    d.rounded_rectangle([px, py, px + pill_w, py + pill_h], radius=round(pill_h * 0.16), fill=WHITE)
    d.text((px + pill_w / 2, py + round(pill_h * 0.10)), label, font=label_f, fill=MUTED, anchor="ma")
    out.paste(logo, (px + (pill_w - logo.width) // 2, py + pill_h - logo_h - round(pill_h * 0.12)), logo)

    # event text (left), shrunk until it fits beside the pill
    max_w = px - 2 * pad
    size = round(sh * 0.27)
    while size > 10:
        tf, sf = font(size, True), font(round(size * 0.78), False)
        if max(text_w(d, event["frame_line_1"], tf), text_w(d, event["frame_line_2"], sf)) <= max_w:
            break
        size -= 1
    block = size + round(size * 0.78) + round(size * 0.3)
    y0 = h + (sh - block) // 2
    d.text((pad, y0), event["frame_line_1"], font=tf, fill=WHITE)
    d.text((pad, y0 + size + round(size * 0.3)), event["frame_line_2"], font=sf, fill=(190, 214, 235))
    return out


# --------------------------------------------------------------------------- html
def bi(en, ar, tag="span"):
    # keep the brand name on one line in both languages
    en = en.replace("Care Grid", '<span class="nw">Care Grid</span>')
    ar = ar.replace("كير گرد", '<span class="nw">كير گرد</span>')
    return f'<{tag} class="l-en">{en}</{tag}><{tag} class="l-ar" lang="ar">{ar}</{tag}>'


def asset_version(name):
    """Short content hash so browsers pick up CSS/JS changes right away."""
    return hashlib.md5((C35 / name).read_bytes()).hexdigest()[:8]


def esc(s):
    return html.escape(s, quote=True)


def arabic_digits(n):
    return str(n).translate(str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩"))


def shot(p):
    link = f"../photos/{p['slug']}.jpg"
    dl = p["dl"]
    return f"""      <figure class="shot">
        <a href="{link}" class="shot-link" data-lightbox data-en="{esc(p['en'])}" data-ar="{esc(p['ar'])}" data-download="{dl}">
          <img src="../thumbs/{p['slug']}.jpg" width="{p['tw']}" height="{p['th']}" alt="{esc(p['alt_en'])}" data-alt-ar="{esc(p['alt_ar'])}" loading="lazy" />
        </a>
        <figcaption>
          <span class="shot-cap">{bi(esc(p['en']), esc(p['ar']))}</span>
          <a class="shot-dl" href="{link}" download="{dl}">{bi('Download', 'تحميل')}</a>
        </figcaption>
      </figure>"""


def head(lang, title, desc):
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{'rtl' if lang == 'ar' else 'ltr'}" data-lang="{lang}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}" />
  <!-- Unlisted page: shared by direct link only. Not in the menu or sitemap, and kept out of search results. -->
  <meta name="robots" content="noindex, nofollow, noarchive, nosnippet" />
  <meta name="referrer" content="no-referrer" />
  <link rel="stylesheet" href="../../assets/css/style.css" />
  <link rel="stylesheet" href="../conference.css?v={asset_version('conference.css')}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
</head>"""


def header():
    return f"""  <header class="c35-header">
    <div class="container c35-header-row">
      <a href="../../index.html" class="brand-wrapper">
        <img src="{CREST}" alt="IMA crest" class="brand-logo" width="52" height="52" />
        <div class="brand-text">
          <h1>{bi('Iraqi Medical Association', 'الجمعية الطبية العراقية')}</h1>
          <div class="brand-sub">{bi('United Kingdom &amp; Europe', 'في المملكة المتحدة وأوروبا')}</div>
        </div>
      </a>
      <div class="c35-lang" role="group" aria-label="Language">
        <button type="button" data-set-lang="en">EN</button>
        <button type="button" data-set-lang="ar">العربية</button>
      </div>
    </div>
  </header>"""


def hero(event, lang, with_print, zip_mb):
    print_btn = (f'<button type="button" class="btn btn-outline c35-btn-light" data-print>{bi("Print brochure", "طباعة البروشور")}</button>'
                 if with_print else "")
    return f"""  <section class="hero-royal c35-hero">
    <div class="container text-center">
      <span class="badge badge-gold">{bi('Conference photographs', 'صور المؤتمر')}</span>
      <h2 class="c35-title">{bi(esc(event['name_en']), esc(event['name_ar']))}</h2>
      <p class="c35-meta">{bi(esc(event['place_en'] + ' · ' + event['dates_en']), esc(event['place_ar'] + ' · ' + event['dates_ar']))}</p>
      <p class="c35-credit">{bi('In cooperation with the Iraqi Red Crescent Society · Media sponsor: Care Grid', 'بالتعاون مع جمعية الهلال الأحمر العراقي · الراعي الإعلامي: كير گرد')}</p>
      <div class="c35-actions">
        <a class="btn btn-gold" href="../{ZIP_NAME}" download>{bi(f'Download all photos (ZIP, {zip_mb} MB)', f'تحميل كل الصور (ZIP، {arabic_digits(zip_mb)} ميغابايت)')}</a>
        {print_btn}
      </div>
    </div>
  </section>"""


def sponsor_uk():
    return f"""  <section class="section c35-sponsor" id="media-sponsor">
    <div class="container">
      <div class="sponsor-card">
        <div class="sponsor-logo"><img src="../assets/caregrid-lockup.png" alt="Care Grid" width="214" height="51" /></div>
        <div class="sponsor-body">
          <span class="badge badge-navy">{bi('Media sponsor', 'الراعي الإعلامي')}</span>
          <h3>{bi('Care Grid: smart healthcare, made for Iraq', 'كير گرد: رعاية صحية ذكية صُنعت للعراق')}</h3>
          <p>{bi('Care Grid is a healthcare platform founded in Iraq and the UK. Its first product, Clinic Grid, is available now: appointments and the walk-in queue, patient files, visits and prescriptions, and referrals with WhatsApp reminders.',
                 'كير گرد منصة رعاية صحية تأسست في العراق وبريطانيا. أول منتجاتها Clinic Grid متاح الآن: المواعيد وطابور المراجعين، وملف المريض والزيارات والوصفات، والتحويلات وتذكيرات الواتساب.', 'span')}</p>
          <p>{bi('Lab Grid, Pharma Grid and Hospital Grid are coming soon.', 'Lab Grid وPharma Grid وHospital Grid قريباً.', 'span')}</p>
          <p>{bi(f'Care Grid supported the 35th conference as media sponsor. To learn more, write to <a href="mailto:{EMAIL}?subject=Care%20Grid%20(from%20the%20IMA%20conference%20photos)">{EMAIL}</a> or visit <a href="https://caregr.id" target="_blank" rel="noopener noreferrer">caregr.id</a>.',
                 f'دعمت كير گرد المؤتمر الخامس والثلاثين بصفتها الراعي الإعلامي. لمعرفة المزيد راسلونا على <a href="mailto:{EMAIL}?subject=Care%20Grid%20(from%20the%20IMA%20conference%20photos)">{EMAIL}</a> أو زوروا <a href="https://caregr.id" target="_blank" rel="noopener noreferrer">caregr.id</a>.', 'span')}</p>
        </div>
      </div>
    </div>
  </section>"""


def sponsor_iq():
    wa_text = urllib.parse.quote("مرحباً، شفت صور مؤتمر لندن وأحب أشوف شلون يشتغل كير گرد بعيادتي")
    return f"""  <section class="section c35-sponsor" id="media-sponsor">
    <div class="container">
      <div class="sponsor-card">
        <div class="sponsor-logo"><img src="../assets/caregrid-lockup.png" alt="Care Grid" width="214" height="51" /></div>
        <div class="sponsor-body">
          <span class="badge badge-navy">{bi('Media sponsor', 'الراعي الإعلامي')}</span>
          <h3>{bi('Care Grid: smart healthcare, made for Iraq', 'كير گرد: رعاية صحية ذكية صُنعت للعراق')}</h3>
          <p>{bi('Care Grid supported the 35th conference as media sponsor. Its first product, Clinic Grid, is available now for clinics in Iraq: patient files, visits and prescriptions, appointments and the walk-in queue, and referrals with WhatsApp reminders.',
                 'كير گرد هي الراعي الإعلامي للمؤتمر. أول منتجاتنا Clinic Grid متاح الآن للعيادات في العراق: ملف المريض والزيارات والوصفات، والمواعيد وطابور المراجعين، والتحويلات وتذكيرات الواتساب.', 'span')}</p>
          <p>{bi('Coming soon: Lab Grid · Pharma Grid · Hospital Grid.', 'قريباً: <bdi>Lab Grid</bdi> · <bdi>Pharma Grid</bdi> · <bdi>Hospital Grid</bdi>', 'span')}</p>
          <p class="sponsor-cta">{bi('Ask for a walkthrough inside your clinic: message us and let us show you how it works.', 'اطلب عرضاً داخل عيادتك: راسلنا وخلّينا نشوفك شلون يشتغل.', 'span')}</p>
          <div class="sponsor-links">
            <a class="btn btn-gold" href="https://wa.me/{WHATSAPP}?text={wa_text}" target="_blank" rel="noopener noreferrer">{bi('Message us on WhatsApp', 'راسلنا على الواتساب')}</a>
            <a class="btn btn-outline" href="https://caregr.id" target="_blank" rel="noopener noreferrer">caregr.id</a>
          </div>
          <p class="sponsor-contact"><span dir="ltr">+964 782 399 7303</span> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
        </div>
      </div>
    </div>
  </section>"""


def footer():
    return f"""  <footer class="c35-footer">
    <div class="container text-center">
      <p>{bi(f'Photographs were taken at the 35th conference and are shared with attendees. If you would like a photo removed, please email the IMA secretariat at <a href="mailto:{IMA_EMAIL}">{IMA_EMAIL}</a>.',
             f'التُقطت الصور في المؤتمر الخامس والثلاثين وتُشارك مع الحاضرين. إن رغبتم بحذف صورة، راسلوا أمانة الجمعية على <a href="mailto:{IMA_EMAIL}">{IMA_EMAIL}</a>.', 'span')}</p>
      <p><a href="../../index.html">{bi('Iraqi Medical Association UK &amp; Europe', 'الجمعية الطبية العراقية في المملكة المتحدة وأوروبا')}</a></p>
    </div>
  </footer>

  <div id="c35-lightbox" class="c35-lightbox" hidden role="dialog" aria-modal="true" aria-label="Photo viewer">
    <button type="button" class="lb-close" aria-label="Close">&times;</button>
    <button type="button" class="lb-nav lb-prev" aria-label="Previous">&#8249;</button>
    <button type="button" class="lb-nav lb-next" aria-label="Next">&#8250;</button>
    <figure class="lb-figure">
      <img class="lb-img" alt="" />
      <figcaption class="lb-cap"><span class="lb-text"></span> <a class="lb-dl" href="#" download>{bi('Download', 'تحميل')}</a></figcaption>
    </figure>
  </div>

  <script src="../conference.js?v={asset_version('conference.js')}" defer></script>
</body>
</html>"""


def page(kind, event, groups, photos, zip_mb):
    lang = "en" if kind == "uk" else "ar"
    if kind == "uk":
        title = "35th IMA UK & EU International Medical Conference: photographs"
        desc = "Photographs from the 35th IMA UK & EU International Medical Conference, shared with attendees."
    else:
        title = "صور المؤتمر الطبي الدولي الخامس والثلاثين للجمعية الطبية العراقية"
        desc = "صور من المؤتمر الطبي الدولي الخامس والثلاثين، تُشارك مع الحاضرين."
    jump = "\n".join(
        f'        <a href="#g-{g["key"]}">{bi(esc(g["en"]), esc(g["ar"]))} <span class="count">{sum(1 for p in photos if p["group"] == g["key"])}</span></a>'
        for g in groups)
    sections = []
    for g in groups:
        items = "\n".join(shot(p) for p in photos if p["group"] == g["key"])
        sections.append(f"""      <h3 class="gallery-title" id="g-{g['key']}">{bi(esc(g['en']), esc(g['ar']))}</h3>
      <div class="gallery">
{items}
      </div>""")
    body = f"""<body class="c35 c35-{kind}">
{header()}

{hero(event, lang, with_print=(kind == 'uk'), zip_mb=zip_mb)}

  <section class="section c35-gallery-section">
    <div class="container">
      <nav class="c35-jump" aria-label="Sections">
{jump}
      </nav>
{chr(10).join(sections)}
    </div>
  </section>

{sponsor_uk() if kind == 'uk' else sponsor_iq()}

{footer()}"""
    return head(lang, title, desc) + "\n" + body


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="folder with the original photos")
    ap.add_argument("--force", action="store_true", help="re-make photos that already exist (use after changing the frame)")
    args = ap.parse_args()
    src = Path(args.src)

    cfg = json.loads((C35 / "photos.json").read_text(encoding="utf-8"))
    event, pages, groups, photos = cfg["event"], cfg["pages"], cfg["groups"], cfg["photos"]
    gmap = {g["key"]: g for g in groups}
    (C35 / "photos").mkdir(exist_ok=True)
    (C35 / "thumbs").mkdir(exist_ok=True)

    # captions, alt text and download names come from the group + the photo's number inside it
    counters = {}
    for p in photos:
        g = gmap[p["group"]]
        n = counters[p["group"]] = counters.get(p["group"], 0) + 1
        p["en"] = f"{g['caption_en']} · {n}"
        p["ar"] = f"{g['caption_ar']} · {arabic_digits(n)}"
        p["alt_en"], p["alt_ar"] = g["alt_en"], g["alt_ar"]
        p["dl"] = f"IMA-UK-EU-35th-conference-{p['group']}-{n:02d}.jpg"

    for p in photos:
        full, thumb_path = C35 / "photos" / f"{p['slug']}.jpg", C35 / "thumbs" / f"{p['slug']}.jpg"
        if args.force or not (full.exists() and thumb_path.exists()):
            framed = add_frame(Image.open(src / p["src"]), event)
            framed.save(full, quality=QUALITY, optimize=True, progressive=True)
            thumb = framed.copy()
            thumb.thumbnail((THUMB_SIDE, THUMB_SIDE), Image.LANCZOS)
            thumb.save(thumb_path, quality=78, optimize=True, progressive=True)
            print("framed", p["slug"], framed.size)
        with Image.open(thumb_path) as t:
            p["tw"], p["th"] = t.size

    with zipfile.ZipFile(C35 / ZIP_NAME, "w", zipfile.ZIP_STORED) as z:
        for p in photos:
            z.write(C35 / "photos" / f"{p['slug']}.jpg", p["dl"])
    zip_mb = round((C35 / ZIP_NAME).stat().st_size / 1e6)

    for kind in ("uk", "iq"):
        out = C35 / pages[kind]
        out.mkdir(exist_ok=True)
        (out / "index.html").write_text(page(kind, event, groups, photos, zip_mb), encoding="utf-8")
        print("wrote", out / "index.html")
    print(f"{len(photos)} photos, ZIP {zip_mb} MB")


if __name__ == "__main__":
    main()
