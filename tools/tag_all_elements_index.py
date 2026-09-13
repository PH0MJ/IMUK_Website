# tag_all_elements_index.py
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Brand logo text
    ('<h1>Iraqi Medical Association</h1>', '<h1 data-i18n="brand_name">Iraqi Medical Association</h1>'),
    ('<div class="brand-sub">United Kingdom & Europe</div>', '<div class="brand-sub" data-i18n="brand_sub">United Kingdom & Europe</div>'),
    ('<div class="brand-ar">الجمعية الطبية العراقية في المملكة المتحدة وأوروبا</div>', '<div class="brand-ar" data-i18n="brand_ar">الجمعية الطبية العراقية في المملكة المتحدة وأوروبا</div>'),

    # Hero Poster Card
    ('<span class="badge badge-gold">Annual General Meeting 2025</span>', '<span class="badge badge-gold" data-i18n="poster_badge">Annual General Meeting 2025</span>'),
    ('<h3>Annual Scientific Conference & AGM</h3>', '<h3 data-i18n="poster_title">Annual Scientific Conference & AGM</h3>'),
    ('<p style="font-size: 0.8rem; color: #cbd5e1; margin-top: 0.25rem;">Keynote Symposia · RCP Approved CPD · Junior Doctor Research Posters</p>', '<p style="font-size: 0.8rem; color: #cbd5e1; margin-top: 0.25rem;" data-i18n="poster_sub">Keynote Symposia · RCP Approved CPD · Junior Doctor Research Posters</p>'),

    # Advisory
    ('<strong>Official Security Advisory & Anti-Fraud Notice (Dated 12.05.2026):</strong>', '<strong data-i18n="advisory_badge">Official Security Advisory & Anti-Fraud Notice (Dated 12.05.2026):</strong>'),
    ('The IMA UK & Europe is aware that unauthorised entities are circulating counterfeit invitations in Iraq using the association\'s name and logo. The IMA does <em>not</em> employ any agents or representatives inside Iraq. All official conferences, certified memberships, and registrations are coordinated exclusively through our official executive secretariat and website domain.', '<span data-i18n="advisory_text">The IMA UK & Europe is aware that unauthorised entities are circulating counterfeit invitations in Iraq using the association\'s name and logo. The IMA does <em>not</em> employ any agents or representatives inside Iraq. All official conferences, certified memberships, and registrations are coordinated exclusively through our official executive secretariat and website domain.</span>'),
    ('Read Full Legal Disclaimer →</a>', '<span data-i18n="advisory_link">Read Full Legal Disclaimer →</span></a>'),

    # About
    ('Over Three Decades of Medical Solidarity\n          </h2>', 'Over Three Decades of Medical Solidarity\n          </h2>'), # already tagged or let's check
    ('<p style="font-size: 0.95rem; color: var(--c-text-muted); line-height: 1.7;">\n            The <strong>Iraqi Medical Association</strong> was founded in 1991 following the end of the Second Gulf War and the critical infrastructure challenges facing our homeland. The association\'s founding charter was established to unite Iraqi doctors in the United Kingdom and Ireland, providing a democratic, collegial, and scientific platform.\n          </p>',
     '<p style="font-size: 0.95rem; color: var(--c-text-muted); line-height: 1.7;" data-i18n="about_p1">The <strong>Iraqi Medical Association</strong> was founded in 1991 following the end of the Second Gulf War and the critical infrastructure challenges facing our homeland. The association\'s founding charter was established to unite Iraqi doctors in the United Kingdom and Ireland, providing a democratic, collegial, and scientific platform.</p>'),

    ('<p style="font-size: 0.95rem; color: var(--c-text-muted); line-height: 1.7;">\n            The association was headed in its inaugural year by <strong>Dr. Hisham Hassan</strong>, followed by democratically elected presidents including <em>Dr. Maher Al-Hilali, Dr. Ferial Ahmed, Dr. Ismail Al-Jalili, Dr. Khaled Al-Shafi, Dr. Walid Al-Wali, Dr. Mohamad Al-Sadi, Dr. Farhan Baqir, Dr. Zuhair Al-Bahrani, Dr. Ihsan Al-Bahrani, Dr. Khaled Naji, Dr. Abdul Amir Alawi, Dr. Salem Al-Damluji, Dr. Abdul Majeed</em>, and active leaders including <em>Dr. Manal Nasih</em> and <em>Dr. Tahsin Mizhar</em>.\n          </p>',
     '<p style="font-size: 0.95rem; color: var(--c-text-muted); line-height: 1.7;" data-i18n="about_p2">The association was headed in its inaugural year by <strong>Dr. Hisham Hassan</strong>, followed by democratically elected presidents including <em>Dr. Maher Al-Hilali, Dr. Ferial Ahmed, Dr. Ismail Al-Jalili, Dr. Khaled Al-Shafi, Dr. Walid Al-Wali, Dr. Mohamad Al-Sadi, Dr. Farhan Baqir, Dr. Zuhair Al-Bahrani, Dr. Ihsan Al-Bahrani, Dr. Khaled Naji, Dr. Abdul Amir Alawi, Dr. Salem Al-Damluji, Dr. Abdul Majeed</em>, and active leaders including <em>Dr. Manal Nasih</em> and <em>Dr. Tahsin Mizhar</em>.</p>'),

    ('<span>Read Full History & Executive Charter</span>', '<span data-i18n="about_btn_history">Read Full History & Executive Charter</span>'),
    ('<span>View Archival Gallery (1999–2026)</span>', '<span data-i18n="about_btn_gallery">View Archival Gallery (1999–2026)</span>'),
    ('<span class="badge badge-navy" style="font-size: 0.65rem;">Historical Archive Record</span>', '<span class="badge badge-navy" style="font-size: 0.65rem;" data-i18n="archive_card_badge">Historical Archive Record</span>'),
    ('<h4 style="font-size: 1rem; margin-top: 0.35rem;">Inaugural Assembly in London — August 1999</h4>', '<h4 style="font-size: 1rem; margin-top: 0.35rem;" data-i18n="archive_card_title">Inaugural Assembly in London — August 1999</h4>'),
    ('<p style="font-size: 0.8rem; color: var(--c-text-muted); margin-top: 0.25rem;">\n                Commemorative photograph uniting foundational Iraqi NHS consultants, surgeons, and academic leaders.\n              </p>',
     '<p style="font-size: 0.8rem; color: var(--c-text-muted); margin-top: 0.25rem;" data-i18n="archive_card_desc">Commemorative photograph uniting foundational Iraqi NHS consultants, surgeons, and academic leaders.</p>'),

    # Benefits CTA button
    ('<span>Apply for Certified Membership (Free)</span>', '<span data-i18n="benefits_cta_btn">Apply for Certified Membership (Free)</span>'),

    # AGM 2025 Section
    ('<span class="badge badge-navy" style="color: var(--c-gold-400); border-color: var(--c-gold-600);">Academic Conference</span>\n        <h2>Annual General Meeting & Scientific Conference 2025</h2>',
     '<span class="badge badge-navy" style="color: var(--c-gold-400); border-color: var(--c-gold-600);" data-i18n="agm_sec_badge">Academic Conference</span>\n        <h2 data-i18n="agm_sec_title">Annual General Meeting & Scientific Conference 2025</h2>'),
    ('<p class="section-lead">\n          London, United Kingdom & Hybrid European Broadcast · Royal College of Physicians CPD Accreditation\n        </p>',
     '<p class="section-lead" data-i18n="agm_sec_lead">London, United Kingdom & Hybrid European Broadcast · Royal College of Physicians CPD Accreditation</p>'),

    ('<div class="badge badge-gold" style="margin-bottom: 0.85rem;">Plenary Sessions</div>', '<div class="badge badge-gold" style="margin-bottom: 0.85rem;" data-i18n="agm_c1_badge">Plenary Sessions</div>'),
    ('<h3 style="color: #ffffff; font-size: 1.25rem; margin-bottom: 0.5rem;">Keynote Scientific Lectures</h3>', '<h3 style="color: #ffffff; font-size: 1.25rem; margin-bottom: 0.5rem;" data-i18n="agm_c1_title">Keynote Scientific Lectures</h3>'),
    ('<p style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.6;">\n            Distinguished NHS and European consultant speakers presenting breakthroughs in surgical robotics, cardiology intervention, oncology care, and modern healthcare leadership.\n          </p>',
     '<p style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.6;" data-i18n="agm_c1_desc">Distinguished NHS and European consultant speakers presenting breakthroughs in surgical robotics, cardiology intervention, oncology care, and modern healthcare leadership.</p>'),
    ('<li>✓ Keynote consultant panel discussions</li>', '<li data-i18n="agm_c1_li1">✓ Keynote consultant panel discussions</li>'),
    ('<li>✓ Multi-disciplinary team (MDT) case reviews</li>', '<li data-i18n="agm_c1_li2">✓ Multi-disciplinary team (MDT) case reviews</li>'),
    ('<li>✓ Clinical ethics & healthcare reform</li>', '<li data-i18n="agm_c1_li3">✓ Clinical ethics & healthcare reform</li>'),

    ('<div class="badge badge-gold" style="margin-bottom: 0.85rem;">Research Competition</div>', '<div class="badge badge-gold" style="margin-bottom: 0.85rem;" data-i18n="agm_c2_badge">Research Competition</div>'),
    ('<h3 style="color: #ffffff; font-size: 1.25rem; margin-bottom: 0.5rem;">Junior Doctor & IMG Posters</h3>', '<h3 style="color: #ffffff; font-size: 1.25rem; margin-bottom: 0.5rem;" data-i18n="agm_c2_title">Junior Doctor & IMG Posters</h3>'),
    ('<p style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.6;">\n            Annual research poster presentation open to foundation doctors, specialty trainees, and medical students. Gold, Silver, and Bronze awards presented at the Gala Dinner.\n          </p>',
     '<p style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.6;" data-i18n="agm_c2_desc">Annual research poster presentation open to foundation doctors, specialty trainees, and medical students. Gold, Silver, and Bronze awards presented at the Gala Dinner.</p>'),
    ('<li>✓ Abstract deadline: 30 September 2025</li>', '<li data-i18n="agm_c2_li1">✓ Abstract deadline: 30 September 2025</li>'),
    ('<li>✓ Peer-reviewed poster publication</li>', '<li data-i18n="agm_c2_li2">✓ Peer-reviewed poster publication</li>'),
    ('<li>✓ Travel bursaries for winners</li>', '<li data-i18n="agm_c2_li3">✓ Travel bursaries for winners</li>'),

    ('<div class="badge badge-gold" style="margin-bottom: 0.85rem;">Dinner & Culture</div>', '<div class="badge badge-gold" style="margin-bottom: 0.85rem;" data-i18n="agm_c3_badge">Dinner & Culture</div>'),
    ('<h3 style="color: #ffffff; font-size: 1.25rem; margin-bottom: 0.5rem;">Annual Gala & Awards Banquet</h3>', '<h3 style="color: #ffffff; font-size: 1.25rem; margin-bottom: 0.5rem;" data-i18n="agm_c3_title">Annual Gala & Awards Banquet</h3>'),
    ('<p style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.6;">\n            An evening of collegial fellowship, recognition of lifetime achievements in the NHS, authentic Iraqi musical entertainment, and networking across generations of doctors.\n          </p>',
     '<p style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.6;" data-i18n="agm_c3_desc">An evening of collegial fellowship, recognition of lifetime achievements in the NHS, authentic Iraqi musical entertainment, and networking across generations of doctors.</p>'),
    ('<li>✓ Black tie / Formal attire</li>', '<li data-i18n="agm_c3_li1">✓ Black tie / Formal attire</li>'),
    ('<li>✓ Lifetime service award ceremonies</li>', '<li data-i18n="agm_c3_li2">✓ Lifetime service award ceremonies</li>'),
    ('<li>✓ Family and guest welcome reception</li>', '<li data-i18n="agm_c3_li3">✓ Family and guest welcome reception</li>'),
    ('<span>Explore Complete AGM 2025 Programme & Registration</span>', '<span data-i18n="agm_sec_btn">Explore Complete AGM 2025 Programme & Registration</span>'),

    # Education & Humanitarian
    ('<span class="badge badge-gold">Humanitarian & Educational Impact</span>\n          <h2 style="font-size: 2.25rem; margin-top: 0.5rem; margin-bottom: 1rem;">\n            Red Crescent Training & Surgical Masterclasses\n          </h2>',
     '<span class="badge badge-gold" data-i18n="edu_sec_badge">Humanitarian & Educational Impact</span>\n          <h2 style="font-size: 2.25rem; margin-top: 0.5rem; margin-bottom: 1rem;" data-i18n="edu_sec_title">Red Crescent Training & Surgical Masterclasses</h2>'),
    ('<p style="font-size: 0.95rem; color: var(--c-text-muted); line-height: 1.7;">\n            In continuous partnership with the <strong>Iraqi Red Crescent Society</strong> and European academic medical institutions, our fellows conduct clinical skills workshops, advanced trauma life support simulation, and specialized obstetrics & gynaecology preparation (including the Karbala MRCOG workshop).\n          </p>',
     '<p style="font-size: 0.95rem; color: var(--c-text-muted); line-height: 1.7;" data-i18n="edu_sec_desc">In continuous partnership with the <strong>Iraqi Red Crescent Society</strong> and European academic medical institutions, our fellows conduct clinical skills workshops, advanced trauma life support simulation, and specialized obstetrics & gynaecology preparation (including the Karbala MRCOG workshop).</p>'),
    ('<h4 style="font-size: 0.95rem;">Trauma & Resuscitation</h4>', '<h4 style="font-size: 0.95rem;" data-i18n="edu_card1_title">Trauma & Resuscitation</h4>'),
    ('<p style="font-size: 0.8rem; color: var(--c-text-muted); margin-top: 0.25rem;">Hands-on simulation and disaster medicine protocols.</p>', '<p style="font-size: 0.8rem; color: var(--c-text-muted); margin-top: 0.25rem;" data-i18n="edu_card1_desc">Hands-on simulation and disaster medicine protocols.</p>'),
    ('<h4 style="font-size: 0.95rem;">Postgraduate MRCOG & FRCS</h4>', '<h4 style="font-size: 0.95rem;" data-i18n="edu_card2_title">Postgraduate MRCOG & FRCS</h4>'),
    ('<p style="font-size: 0.8rem; color: var(--c-text-muted); margin-top: 0.25rem;">Exam workshops supporting doctors pursuing British College diplomas.</p>', '<p style="font-size: 0.8rem; color: var(--c-text-muted); margin-top: 0.25rem;" data-i18n="edu_card2_desc">Exam workshops supporting doctors pursuing British College diplomas.</p>'),
    ('<span>View All Training Programs & Lecture Recordings</span>', '<span data-i18n="edu_sec_btn">View All Training Programs & Lecture Recordings</span>'),

    # Scientific Posters
    ('<span class="badge badge-gold">Research Repository</span>\n        <h2>Scientific Posters & Clinical Research</h2>',
     '<span class="badge badge-gold" data-i18n="posters_sec_badge">Research Repository</span>\n        <h2 data-i18n="posters_sec_title">Scientific Posters & Clinical Research</h2>'),
    ('<p class="section-lead">\n          Peer-reviewed medical research, clinical audits, and quality improvement projects presented by our members.\n        </p>',
     '<p class="section-lead" data-i18n="posters_sec_lead">Peer-reviewed medical research, clinical audits, and quality improvement projects presented by our members.</p>'),
    ('<span class="badge badge-navy" style="font-size: 0.65rem;">Surgical Audit</span>', '<span class="badge badge-navy" style="font-size: 0.65rem;" data-i18n="p1_badge">Surgical Audit</span>'),
    ('<h4 class="card-title" style="margin-top: 0.5rem; font-size: 1.05rem;">Acute Abdominal Surgical Interventions in the NHS</h4>', '<h4 class="card-title" style="margin-top: 0.5rem; font-size: 1.05rem;" data-i18n="p1_title">Acute Abdominal Surgical Interventions in the NHS</h4>'),
    ('<p class="card-desc">Review of operative timing, post-surgical complications, and mortality reduction protocols.</p>', '<p class="card-desc" data-i18n="p1_desc">Review of operative timing, post-surgical complications, and mortality reduction protocols.</p>'),
    ('>View Full Poster (PDF)</a>', ' data-i18n="p1_btn">View Full Poster (PDF)</a>'),

    ('<span class="badge badge-navy" style="font-size: 0.65rem;">Cardiovascular Medicine</span>', '<span class="badge badge-navy" style="font-size: 0.65rem;" data-i18n="p2_badge">Cardiovascular Medicine</span>'),
    ('<h4 class="card-title" style="margin-top: 0.5rem; font-size: 1.05rem;">Secondary Prevention Pathways in Ischemic Heart Disease</h4>', '<h4 class="card-title" style="margin-top: 0.5rem; font-size: 1.05rem;" data-i18n="p2_title">Secondary Prevention Pathways in Ischemic Heart Disease</h4>'),
    ('<p class="card-desc">Analysis of lipid management, anti-platelet therapy adherence, and cardiac rehabilitation.</p>', '<p class="card-desc" data-i18n="p2_desc">Analysis of lipid management, anti-platelet therapy adherence, and cardiac rehabilitation.</p>'),

    ('<span class="badge badge-navy" style="font-size: 0.65rem;">Medical Education</span>', '<span class="badge badge-navy" style="font-size: 0.65rem;" data-i18n="p3_badge">Medical Education</span>'),
    ('<h4 class="card-title" style="margin-top: 0.5rem; font-size: 1.05rem;">Transitioning International Medical Graduates to NHS Practice</h4>', '<h4 class="card-title" style="margin-top: 0.5rem; font-size: 1.05rem;" data-i18n="p3_title">Transitioning International Medical Graduates to NHS Practice</h4>'),
    ('<p class="card-desc">Evaluating structured induction programs, GMC communication, and supervised clinical fellowships.</p>', '<p class="card-desc" data-i18n="p3_desc">Evaluating structured induction programs, GMC communication, and supervised clinical fellowships.</p>'),
    ('<span>Explore All 2025 Posters & Submit Abstract</span>', '<span data-i18n="posters_sec_btn">Explore All 2025 Posters & Submit Abstract</span>'),

    # Form labels
    ('<label class="form-label" for="full_name">Full Legal Name (with titles) *</label>', '<label class="form-label" for="full_name" data-i18n="form_label_name">Full Legal Name (with titles) *</label>'),
    ('<label class="form-label" for="email">Professional / NHS Email *</label>', '<label class="form-label" for="email" data-i18n="form_label_email">Professional / NHS Email *</label>'),
    ('<label class="form-label" for="country">Country of Practice *</label>', '<label class="form-label" for="country" data-i18n="form_label_country">Country of Practice *</label>'),
    ('<label class="form-label" for="specialty">Clinical Specialty *</label>', '<label class="form-label" for="specialty" data-i18n="form_label_specialty">Clinical Specialty *</label>'),
    ('<label class="form-label" for="gmc_number">Medical Reg / GMC No.</label>', '<label class="form-label" for="gmc_number" data-i18n="form_label_gmc">Medical Reg / GMC No.</label>'),
    ('<label class="form-label" for="hospital">Current Hospital / Academic Institution</label>', '<label class="form-label" for="hospital" data-i18n="form_label_hospital">Current Hospital / Academic Institution</label>'),
    ('<label class="form-label" for="interests">Areas of Interest / Collaboration</label>', '<label class="form-label" for="interests" data-i18n="form_label_interests">Areas of Interest / Collaboration</label>'),
    ('🔒 <strong>Data Privacy Guarantee:</strong> Your information is retained strictly for official association records and communications in accordance with UK GDPR. We never share member details with commercial entities.',
     '<span data-i18n="form_privacy_note">🔒 <strong>Data Privacy Guarantee:</strong> Your information is retained strictly for official association records and communications in accordance with UK GDPR. We never share member details with commercial entities.</span>'),

    # Sister societies
    ('<span class="badge badge-gold">Global Diaspora & Academia</span>\n        <h2>Sister Associations & Medical Faculties</h2>',
     '<span class="badge badge-gold" data-i18n="links_sec_badge">Global Diaspora & Academia</span>\n        <h2 data-i18n="links_sec_title">Sister Associations & Medical Faculties</h2>'),
    ('<p class="section-lead">Collaborating with Iraqi medical societies across the globe and universities across Iraq.</p>',
     '<p class="section-lead" data-i18n="links_sec_lead">Collaborating with Iraqi medical societies across the globe and universities across Iraq.</p>'),
    ('<h4 style="font-size: 0.95rem; color: var(--c-navy-900);">All 12 Colleges →</h4>', '<h4 style="font-size: 0.95rem; color: var(--c-navy-900);" data-i18n="links_card_all">All 12 Colleges →</h4>'),
    ('<p style="font-size: 0.75rem; color: var(--c-text-muted); margin-top: 0.25rem;">Explore Full University Directory</p>', '<p style="font-size: 0.75rem; color: var(--c-text-muted); margin-top: 0.25rem;" data-i18n="links_card_all_sub">Explore Full University Directory</p>'),

    # Footer
    ('<p style="font-size: 0.8rem; line-height: 1.6; color: #9ca3af;">\n            Established in London in 1991 to unite, support, and advance Iraqi medical professionals across Great Britain and continental Europe. A non-profit, non-political professional body dedicated to clinical excellence and humanitarian education.\n          </p>',
     '<p style="font-size: 0.8rem; line-height: 1.6; color: #9ca3af;" data-i18n="footer_p">Established in London in 1991 to unite, support, and advance Iraqi medical professionals across Great Britain and continental Europe. A non-profit, non-political professional body dedicated to clinical excellence and humanitarian education.</p>'),
    ('<h4>Association Portals</h4>', '<h4 data-i18n="footer_col2_title">Association Portals</h4>'),
    ('<h4>Integrity & Trust</h4>', '<h4 data-i18n="footer_col3_title">Integrity & Trust</h4>'),
    ('<h4>Official Channels</h4>', '<h4 data-i18n="footer_col4_title">Official Channels</h4>'),
    ('© 1991–2026 Iraqi Medical Association UK & Europe. All rights reserved.', '<span data-i18n="footer_copyright">© 1991–2026 Iraqi Medical Association UK & Europe. All rights reserved.</span>')
]

updated = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)
        updated += 1

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Tagged {updated} additional sections with data-i18n in index.html!")
