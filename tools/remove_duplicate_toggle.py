import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'preview_concepts.html']

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the nav-container duplicate switcher
    target_nav_switcher = re.compile(
        r'\s*<div class="nav-lang-switcher" style="margin-left: 0\.5rem;">\s*<button class="lang-btn[^"]*" data-lang="en">EN</button>\s*<button class="lang-btn[^"]*" data-lang="ar">العربية</button>\s*</div>',
        re.DOTALL
    )
    new_content = target_nav_switcher.sub('', content)

    # 2. Also remove redundant static <span class="arabic-subtitle">الجمعية الطبية العراقية</span> right before the top toggle
    new_content = new_content.replace('<span class="arabic-subtitle">الجمعية الطبية العراقية</span>\n', '')
    new_content = new_content.replace('<span class="arabic-subtitle">الجمعية الطبية العراقية</span>', '')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Cleaned {fname}")

print("SUCCESS: Duplicate language toggle completely removed!")
