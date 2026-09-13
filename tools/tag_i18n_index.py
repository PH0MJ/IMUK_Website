with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    # Top badge
    ('<span>Official Non-Profit Medical Association in the UK & Europe (Est. 1991)</span>',
     '<span data-i18n="verify_badge">Official Non-Profit Medical Association in the UK & Europe (Est. 1991)</span>'),

    # Nav
    ('>Home</a>', ' data-i18n="nav_home">Home</a>'),
    ('>About & Governance</a>', ' data-i18n="nav_about">About & Governance</a>'),
    ('>AGM 2025</a>', ' data-i18n="nav_agm">AGM 2025</a>'),
    ('>Membership</a>', ' data-i18n="nav_membership">Membership</a>'),
    ('>Education & CPD</a>', ' data-i18n="nav_education">Education & CPD</a>'),
    ('>Posters</a>', ' data-i18n="nav_posters">Posters</a>'),
    ('>Archive</a>', ' data-i18n="nav_archive">Archive</a>'),
    ('>News</a>', ' data-i18n="nav_news">News</a>'),
    ('>Contact</a>', ' data-i18n="nav_contact">Contact</a>'),

    # Nav CTA
    ('Member Enrolment\n        </a>', '<span data-i18n="btn_enrol">Member Enrolment</span>\n        </a>'),

    # Hero badge
    ('<span>The Premier Association for Iraqi Physicians Across the UK & Europe</span>',
     '<span data-i18n="hero_badge">The Premier Association for Iraqi Physicians Across the UK & Europe</span>'),

    # Hero title
    ('<h1>\n            Advancing Excellence in Healthcare, <span class="gold-accent">Connecting Leaders</span> Since 1991.\n          </h1>',
     '<h1 data-i18n="hero_title">Advancing Excellence in Healthcare, <span class="gold-accent">Connecting Leaders</span> Since 1991.</h1>'),

    # Hero lead
    ('<p class="hero-lead">\n            Founded following the Second Gulf War to unite Iraqi physicians, NHS consultants, academic faculties, and trainees in Great Britain and Ireland. We foster continuous medical education, Royal College accredited CPD, and humanitarian clinical training.\n          </p>',
     '<p class="hero-lead" data-i18n="hero_lead">Founded following the Second Gulf War to unite Iraqi physicians, NHS consultants, academic faculties, and trainees in Great Britain and Ireland. We foster continuous medical education, Royal College accredited CPD, and humanitarian clinical training.</p>'),

    # Hero buttons
    ('<span>AGM 2025 Official Conference</span>', '<span data-i18n="hero_agm_btn">AGM 2025 Official Conference</span>'),
    ('<span>Free Certified Membership</span>', '<span data-i18n="hero_member_btn">Free Certified Membership</span>'),

    # Stats
    ('<div class="hero-stat-label">Founded in London</div>', '<div class="hero-stat-label" data-i18n="stat_founded">Founded in London</div>'),
    ('<div class="hero-stat-label">Annual Scientific AGMs</div>', '<div class="hero-stat-label" data-i18n="stat_agms">Annual Scientific AGMs</div>'),
    ('<div class="hero-stat-label">Qualified Doctors</div>', '<div class="hero-stat-label" data-i18n="stat_doctors">Qualified Doctors</div>'),

    # Countdown labels
    ('<div style="font-size: 0.65rem; color: #9ca3af; text-transform: uppercase;">Days</div>',
     '<div style="font-size: 0.65rem; color: #9ca3af; text-transform: uppercase;" data-i18n="cd_days">Days</div>'),
    ('<div style="font-size: 0.65rem; color: #9ca3af; text-transform: uppercase;">Hours</div>',
     '<div style="font-size: 0.65rem; color: #9ca3af; text-transform: uppercase;" data-i18n="cd_hours">Hours</div>'),
    ('<div style="font-size: 0.65rem; color: #9ca3af; text-transform: uppercase;">Mins</div>',
     '<div style="font-size: 0.65rem; color: #9ca3af; text-transform: uppercase;" data-i18n="cd_mins">Mins</div>'),
    ('<div style="font-size: 0.65rem; color: #9ca3af; text-transform: uppercase;">Secs</div>',
     '<div style="font-size: 0.65rem; color: #9ca3af; text-transform: uppercase;" data-i18n="cd_secs">Secs</div>'),

    # Small AGM CTA
    ('Conference Registration & Abstract Guidelines →\n                </a>',
     '<span data-i18n="agm_btn_small">Conference Registration & Abstract Guidelines →</span>\n                </a>'),

    # Benefits section
    ('<span class="badge badge-gold">Professional Enrolment</span>\n        <h2>7 Pillars of IMA Certified Membership</h2>',
     '<span class="badge badge-gold" data-i18n="benefits_badge">Professional Enrolment</span>\n        <h2 data-i18n="benefits_title">7 Pillars of IMA Certified Membership</h2>'),
    ('<p class="section-lead">\n          Membership is 100% free of charge for all qualified Iraqi and European medical doctors, dental surgeons, and clinical researchers. Join over 1,200 colleagues.\n        </p>',
     '<p class="section-lead" data-i18n="benefits_lead">Membership is 100% free of charge for all qualified Iraqi and European medical doctors, dental surgeons, and clinical researchers. Join over 1,200 colleagues.</p>'),

    # B1 - B7
    ('<h4 class="card-title">Career Development</h4>', '<h4 class="card-title" data-i18n="b1_title">Career Development</h4>'),
    ('<p class="card-desc">Guidance through NHS specialist registers, CESR/portfolio pathways, fellowship applications, and consultant appointment panels.</p>',
     '<p class="card-desc" data-i18n="b1_desc">Guidance through NHS specialist registers, CESR/portfolio pathways, fellowship applications, and consultant appointment panels.</p>'),

    ('<h4 class="card-title">Peer Clinical Solidarity</h4>', '<h4 class="card-title" data-i18n="b2_title">Peer Clinical Solidarity</h4>'),
    ('<p class="card-desc">Uniting with highly qualified colleagues across medical sub-specialties, establishing clinical support and second-opinion networks.</p>',
     '<p class="card-desc" data-i18n="b2_desc">Uniting with highly qualified colleagues across medical sub-specialties, establishing clinical support and second-opinion networks.</p>'),

    ('<h4 class="card-title">Exclusive Event Privileges</h4>', '<h4 class="card-title" data-i18n="b3_title">Exclusive Event Privileges</h4>'),
    ('<p class="card-desc">Complimentary access and exclusive privileges to all IMA future scientific, cultural, and annual gala banquets across the UK and Europe.</p>',
     '<p class="card-desc" data-i18n="b3_desc">Complimentary access and exclusive privileges to all IMA future scientific, cultural, and annual gala banquets across the UK and Europe.</p>'),

    ('<h4 class="card-title">RCP-Approved CPD Points</h4>', '<h4 class="card-title" data-i18n="b4_title">RCP-Approved CPD Points</h4>'),
    ('<p class="card-desc">Earn formal Continuing Professional Development (CPD) credits approved by the Royal College of Physicians for annual GMC revalidation.</p>',
     '<p class="card-desc" data-i18n="b4_desc">Earn formal Continuing Professional Development (CPD) credits approved by the Royal College of Physicians for annual GMC revalidation.</p>'),

    ('<h4 class="card-title">International Lectures & Masterclasses</h4>', '<h4 class="card-title" data-i18n="b5_title">International Lectures & Masterclasses</h4>'),
    ('<p class="card-desc">Access to live and online symposia in London, European capitals, and joint academic masterclasses with Iraqi and Arab medical faculties.</p>',
     '<p class="card-desc" data-i18n="b5_desc">Access to live and online symposia in London, European capitals, and joint academic masterclasses with Iraqi and Arab medical faculties.</p>'),

    ('<h4 class="card-title">Specialty Interest Groups</h4>', '<h4 class="card-title" data-i18n="b6_title">Specialty Interest Groups</h4>'),
    ('<p class="card-desc">Join dedicated sub-specialty clinical forums (Cardiology, Surgery, Pediatrics, Women\'s Health, Primary Care, and Junior Trainees).</p>',
     '<p class="card-desc" data-i18n="b6_desc">Join dedicated sub-specialty clinical forums (Cardiology, Surgery, Pediatrics, Women\'s Health, Primary Care, and Junior Trainees).</p>'),

    ('<h4 class="card-title">Trainee Doctor International Bursaries</h4>', '<h4 class="card-title" data-i18n="b7_title">Trainee Doctor International Bursaries</h4>'),
    ('<p class="card-desc">Financial bursaries and sponsorship support for junior doctors and international medical graduates (IMGs) to present original research at international conferences.</p>',
     '<p class="card-desc" data-i18n="b7_desc">Financial bursaries and sponsorship support for junior doctors and international medical graduates (IMGs) to present original research at international conferences.</p>'),

    # Registration Form
    ('<span class="badge badge-gold">Official Registration</span>\n          <h2 style="font-size: 2rem; margin-top: 0.35rem;">Certified Member Enrolment</h2>',
     '<span class="badge badge-gold" data-i18n="form_badge">Official Registration</span>\n          <h2 style="font-size: 2rem; margin-top: 0.35rem;" data-i18n="form_title">Certified Member Enrolment</h2>'),
    ('<p style="font-size: 0.85rem; color: var(--c-text-muted); margin-top: 0.5rem;">\n            Registration is 100% free of charge. Open to qualified doctors, surgeons, dental practitioners, and academic clinical researchers in the UK and Europe.\n          </p>',
     '<p style="font-size: 0.85rem; color: var(--c-text-muted); margin-top: 0.5rem;" data-i18n="form_lead">Registration is 100% free of charge. Open to qualified doctors, surgeons, dental practitioners, and academic clinical researchers in the UK and Europe.</p>'),
    ('Submit Certified Member Enrolment\n          </button>',
     '<span data-i18n="form_submit">Submit Certified Member Enrolment</span>\n          </button>')
]

count = 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        count += 1

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Successfully applied {count} data-i18n tags to index.html")
