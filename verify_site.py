import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'preview_concepts.html']
print(f"Checking {len(html_files)} new website HTML files: {html_files}")

all_ok = True
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check images
    img_matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    for src in img_matches:
        if not src.startswith('http') and not src.startswith('data:'):
            clean_src = src.split('?')[0].split('#')[0]
            if not os.path.exists(clean_src):
                print(f"  [!] Missing image in {hf}: {src}")
                all_ok = False
                
    # Check internal links
    link_matches = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', content)
    for href in link_matches:
        if href.endswith('.html') or '.html#' in href:
            target = href.split('#')[0]
            if not os.path.exists(target):
                print(f"  [!] Broken link in {hf}: {href}")
                all_ok = False

if all_ok:
    print("\n[SUCCESS] ALL internal links, images, and sub-pages are 100% valid and verified locally!")
else:
    print("\n[WARNING] Found issues above.")
