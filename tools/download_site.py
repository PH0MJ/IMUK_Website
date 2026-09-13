import os
import re
import json
from urllib.parse import urljoin, urlparse, unquote
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.iraqimedicalassociation-uk-eu.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
OUT_DIR = os.path.join(os.getcwd(), "downloaded_site")
IMG_DIR = os.path.join(OUT_DIR, "images")
CSS_DIR = os.path.join(OUT_DIR, "css")
PAGES_DIR = os.path.join(OUT_DIR, "pages")

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(CSS_DIR, exist_ok=True)
os.makedirs(PAGES_DIR, exist_ok=True)

session = requests.Session()
session.headers.update(HEADERS)

print(f"[*] Fetching homepage: {BASE_URL}")
resp = session.get(BASE_URL, timeout=30)
resp.raise_for_status()

# 1. Save original raw index.html
raw_index_path = os.path.join(OUT_DIR, "index_raw.html")
with open(raw_index_path, "w", encoding="utf-8") as f:
    f.write(resp.text)
print(f"[+] Saved raw HTML to {raw_index_path}")

soup = BeautifulSoup(resp.text, "html.parser")

# 2. Download CSS stylesheets
print("\n[*] Downloading CSS files...")
css_mapping = {}
for i, link in enumerate(soup.find_all("link", rel="stylesheet")):
    href = link.get("href")
    if href:
        css_url = urljoin(BASE_URL, href)
        parsed_css = urlparse(css_url)
        fname = os.path.basename(parsed_css.path)
        if not fname or not fname.endswith(".css"):
            fname = f"style_{i}.css"
        fname = re.sub(r"[^a-zA-Z0-9_\-\.]", "_", fname)
        local_css = os.path.join(CSS_DIR, fname)
        try:
            c_resp = session.get(css_url, timeout=15)
            if c_resp.status_code == 200:
                with open(local_css, "wb") as cf:
                    cf.write(c_resp.content)
                css_mapping[href] = f"css/{fname}"
                print(f"  + Downloaded CSS: {fname} ({len(c_resp.content)} bytes)")
        except Exception as e:
            print(f"  - Error downloading {css_url}: {e}")

# 3. Collect and download images
print("\n[*] Collecting all images...")
img_urls = set()

for img in soup.find_all(["img", "source"]):
    for attr in ["src", "data-src", "data-image", "srcset"]:
        val = img.get(attr)
        if val:
            if attr == "srcset":
                for part in val.split(","):
                    src_part = part.strip().split()[0]
                    if src_part:
                        img_urls.add(urljoin(BASE_URL, src_part))
            else:
                img_urls.add(urljoin(BASE_URL, val))

for meta in soup.find_all("meta"):
    prop = meta.get("property") or meta.get("name") or ""
    if "image" in prop.lower() and meta.get("content"):
        img_urls.add(urljoin(BASE_URL, meta["content"]))

for style_tag in soup.find_all("style"):
    txt = style_tag.text or ""
    matches = re.findall(r'url\((["\']?)([^)"\']+)\1\)', txt)
    for quote, url_match in matches:
        if any(url_match.lower().endswith(ext) or ext in url_match.lower() for ext in [".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif"]):
            img_urls.add(urljoin(BASE_URL, url_match))

print(f"[*] Found {len(img_urls)} unique image URLs to download.")
downloaded_images = {}
for i, img_url in enumerate(sorted(img_urls)):
    parsed = urlparse(img_url)
    clean_name = os.path.basename(unquote(parsed.path))
    if not clean_name or "." not in clean_name:
        clean_name = f"image_{i}.jpg"
    clean_name = re.sub(r"[^a-zA-Z0-9_\-\.]", "_", clean_name)
    local_path = os.path.join(IMG_DIR, clean_name)
    try:
        iresp = session.get(img_url, timeout=15)
        if iresp.status_code == 200:
            with open(local_path, "wb") as f:
                f.write(iresp.content)
            rel_path = f"images/{clean_name}"
            downloaded_images[img_url] = rel_path
            downloaded_images[parsed.path] = rel_path
            print(f"  + [{i+1}/{len(img_urls)}] {clean_name} ({len(iresp.content)} bytes)")
    except Exception as e:
        print(f"  - Failed {img_url}: {e}")

print(f"\n[+] Total images downloaded: {len(downloaded_images)}")

# 4. Generate index_offline.html
print("\n[*] Generating offline index.html...")
offline_soup = BeautifulSoup(resp.text, "html.parser")

for link in offline_soup.find_all("link", rel="stylesheet"):
    href = link.get("href")
    if href in css_mapping:
        link["href"] = css_mapping[href]

for img in offline_soup.find_all("img"):
    src = img.get("src") or img.get("data-src") or img.get("data-image")
    if src:
        full = urljoin(BASE_URL, src)
        if full in downloaded_images:
            img["src"] = downloaded_images[full]
        elif urlparse(full).path in downloaded_images:
            img["src"] = downloaded_images[urlparse(full).path]

with open(os.path.join(OUT_DIR, "index_offline.html"), "w", encoding="utf-8") as f:
    f.write(str(offline_soup))
print("[+] Generated index_offline.html")

# 5. Extract structured text content
print("\n[*] Extracting text sections and content...")
content_data = {
    "title": soup.title.string.strip() if soup.title else "",
    "meta_description": (soup.find("meta", {"name": "description"}) or {}).get("content", ""),
    "navigation_links": [],
    "social_links": [],
    "sections": []
}

nav = soup.find("nav") or soup.find("header")
if nav:
    for a in nav.find_all("a", href=True):
        content_data["navigation_links"].append({
            "text": a.get_text(strip=True),
            "href": urljoin(BASE_URL, a["href"])
        })

for a in soup.find_all("a", href=True):
    href = a["href"]
    if any(s in href.lower() for s in ["facebook.com", "instagram.com", "twitter.com", "x.com", "linkedin.com", "forum"]):
        content_data["social_links"].append({
            "text": a.get_text(strip=True),
            "href": href
        })

for i, sec in enumerate(soup.find_all(["section", "article"])):
    sec_id = sec.get("id", f"section-{i}")
    sec_text = sec.get_text(separator="\n", strip=True)
    h_tags = [h.get_text(strip=True) for h in sec.find_all(["h1", "h2", "h3", "h4"])]
    if sec_text:
        content_data["sections"].append({
            "index": i,
            "id": sec_id,
            "headings": h_tags,
            "text": sec_text
        })

with open(os.path.join(OUT_DIR, "extracted_content.json"), "w", encoding="utf-8") as f:
    json.dump(content_data, f, indent=2, ensure_ascii=False)

md_lines = [
    f"# {content_data['title']}",
    f"\n**Description:** {content_data['meta_description']}\n",
    "## Social & Contact Channels Found",
]
for s in content_data["social_links"]:
    md_lines.append(f"- **{s['text'] or 'Link'}**: {s['href']}")

md_lines.append("\n## Main Sections & Text Content")
for sec in content_data["sections"]:
    md_lines.append(f"\n### Section {sec['index']}: {', '.join(sec['headings']) if sec['headings'] else sec['id']}")
    md_lines.append("```")
    md_lines.append(sec["text"][:1500] + ("..." if len(sec["text"]) > 1500 else ""))
    md_lines.append("```")

with open(os.path.join(OUT_DIR, "extracted_content.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print("[+] Saved extracted_content.json and extracted_content.md")

# 6. Download key sub-pages
other_pages = [
    ("about", "about.html"),
    ("upcoming-events", "upcoming_events.html"),
    ("services-store", "membership_services.html"),
    ("our-members", "our_members.html"),
    ("new-page-2", "news.html"),
    ("new-page-1", "archives.html"),
    ("new-page", "learning.html"),
    ("posters", "posters.html"),
    ("the-gallery", "the_gallery.html"),
    ("contact", "contact.html"),
    ("useful-links", "useful_links.html")
]

print("\n[*] Downloading sub-pages...")
for slug, filename in other_pages:
    sub_url = urljoin(BASE_URL, slug)
    try:
        sub_resp = session.get(sub_url, timeout=20)
        if sub_resp.status_code == 200:
            target_path = os.path.join(PAGES_DIR, filename)
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(sub_resp.text)
            print(f"  + Downloaded page [{slug}] -> {filename} ({len(sub_resp.text)} chars)")
        else:
            print(f"  - Page [{slug}] returned status {sub_resp.status_code}")
    except Exception as e:
        print(f"  - Failed downloading [{slug}]: {e}")

print("\n[✓] ALL DOWNLOADS COMPLETED SUCCESSFULLY!")
