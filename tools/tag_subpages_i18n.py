import os

files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ['index.html', 'preview_concepts.html']]

sub_replacements = [
    # Top badge
    ('<span>Official Non-Profit Medical Association in the UK & Europe (Est. 1991)</span>',
     '<span data-i18n="verify_badge">Official Non-Profit Medical Association in the UK & Europe (Est. 1991)</span>'),

    # Brand text
    ('<h1>Iraqi Medical Association</h1>', '<h1 data-i18n="brand_name">Iraqi Medical Association</h1>'),
    ('<div class="brand-sub">United Kingdom & Europe</div>', '<div class="brand-sub" data-i18n="brand_sub">United Kingdom & Europe</div>'),
    ('<div class="brand-ar">الجمعية الطبية العراقية في المملكة المتحدة وأوروبا</div>', '<div class="brand-ar" data-i18n="brand_ar">الجمعية الطبية العراقية في المملكة المتحدة وأوروبا</div>'),

    # Nav links
    ('>Home</a>', ' data-i18n="nav_home">Home</a>'),
    ('>About & Governance</a>', ' data-i18n="nav_about">About & Governance</a>'),
    ('>AGM 2025</a>', ' data-i18n="nav_agm">AGM 2025</a>'),
    ('>Membership</a>', ' data-i18n="nav_membership">Membership</a>'),
    ('>Education & CPD</a>', ' data-i18n="nav_education">Education & CPD</a>'),
    ('>Posters</a>', ' data-i18n="nav_posters">Posters</a>'),
    ('>Archive</a>', ' data-i18n="nav_archive">Archive</a>'),
    ('>News</a>', ' data-i18n="nav_news">News</a>'),
    ('>Contact</a>', ' data-i18n="nav_contact">Contact</a>'),

    # Footer
    ('© 1991–2026 Iraqi Medical Association UK & Europe. Registered Non-Profit Association.',
     '<span data-i18n="footer_copyright">© 1991–2026 Iraqi Medical Association UK & Europe. Registered Non-Profit Association.</span>')
]

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    for old, new in sub_replacements:
        content = content.replace(old, new)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Tagged nav and brand in {fname}")

print("All sub-pages successfully tagged with i18n!")
