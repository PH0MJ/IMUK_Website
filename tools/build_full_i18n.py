# build_full_i18n.py
import json

# Comprehensive bilingual translation dictionary covering 100% of index.html
translations_dict = {
  "en": {
    # Brand & Verification
    "verify_badge": "Official Non-Profit Medical Association in the UK & Europe (Est. 1991)",
    "brand_name": "Iraqi Medical Association",
    "brand_sub": "United Kingdom & Europe",
    "brand_ar": "الجمعية الطبية العراقية في المملكة المتحدة وأوروبا",

    # Navigation
    "nav_home": "Home",
    "nav_about": "About & Governance",
    "nav_agm": "AGM 2025",
    "nav_membership": "Membership",
    "nav_education": "Education & CPD",
    "nav_posters": "Posters",
    "nav_archive": "Archive",
    "nav_news": "News",
    "nav_contact": "Contact",
    "btn_enrol": "Member Enrolment",
    "btn_join_free": "Join Certified Membership (Free)",

    # Hero Section
    "hero_badge": "The Premier Association for Iraqi Physicians Across the UK & Europe",
    "hero_title": "Advancing Excellence in Healthcare, <span class=\"gold-accent\">Connecting Leaders</span> Since 1991.",
    "hero_lead": "Founded following the Second Gulf War to unite Iraqi physicians, NHS consultants, academic faculties, and trainees in Great Britain and Ireland. We foster continuous medical education, Royal College accredited CPD, and humanitarian clinical training.",
    "hero_agm_btn": "AGM 2025 Official Conference",
    "hero_member_btn": "Free Certified Membership",
    "stat_founded": "Founded in London",
    "stat_agms": "Annual Scientific AGMs",
    "stat_doctors": "Qualified Doctors",
    "poster_badge": "Annual General Meeting 2025",
    "poster_title": "Annual Scientific Conference & AGM",
    "poster_sub": "Keynote Symposia · RCP Approved CPD · Junior Doctor Research Posters",
    "cd_days": "Days",
    "cd_hours": "Hours",
    "cd_mins": "Mins",
    "cd_secs": "Secs",
    "agm_btn_small": "Conference Registration & Abstract Guidelines →",

    # Anti-Fraud Advisory
    "advisory_badge": "Official Security Advisory & Anti-Fraud Notice (Dated 12.05.2026):",
    "advisory_text": "The IMA UK & Europe is aware that unauthorised entities are circulating counterfeit invitations in Iraq using the association's name and logo. The IMA does <em>not</em> employ any agents or representatives inside Iraq. All official conferences, certified memberships, and registrations are coordinated exclusively through our official executive secretariat and website domain.",
    "advisory_link": "Read Full Legal Disclaimer →",

    # About & Heritage
    "about_badge": "Enduring Legacy & Governance",
    "about_title": "Over Three Decades of Medical Solidarity",
    "about_p1": "The <strong>Iraqi Medical Association</strong> was founded in 1991 following the end of the Second Gulf War and the critical infrastructure challenges facing our homeland. The association's founding charter was established to unite Iraqi doctors in the United Kingdom and Ireland, providing a democratic, collegial, and scientific platform.",
    "about_p2": "The association was headed in its inaugural year by <strong>Dr. Hisham Hassan</strong>, followed by democratically elected presidents including <em>Dr. Maher Al-Hilali, Dr. Ferial Ahmed, Dr. Ismail Al-Jalili, Dr. Khaled Al-Shafi, Dr. Walid Al-Wali, Dr. Mohamad Al-Sadi, Dr. Farhan Baqir, Dr. Zuhair Al-Bahrani, Dr. Ihsan Al-Bahrani, Dr. Khaled Naji, Dr. Abdul Amir Alawi, Dr. Salem Al-Damluji, Dr. Abdul Majeed</em>, and active leaders including <em>Dr. Manal Nasih</em> and <em>Dr. Tahsin Mizhar</em>.",
    "about_btn_history": "Read Full History & Executive Charter",
    "about_btn_gallery": "View Archival Gallery (1999–2026)",
    "archive_card_badge": "Historical Archive Record",
    "archive_card_title": "Inaugural Assembly in London — August 1999",
    "archive_card_desc": "Commemorative photograph uniting foundational Iraqi NHS consultants, surgeons, and academic leaders.",

    # 7 Pillars of Membership
    "benefits_badge": "Professional Enrolment",
    "benefits_title": "7 Pillars of IMA Certified Membership",
    "benefits_lead": "Membership is 100% free of charge for all qualified Iraqi and European medical doctors, dental surgeons, and clinical researchers. Join over 1,200 colleagues.",
    "b1_title": "Career Development",
    "b1_desc": "Guidance through NHS specialist registers, CESR/portfolio pathways, fellowship applications, and consultant appointment panels.",
    "b2_title": "Peer Clinical Solidarity",
    "b2_desc": "Uniting with highly qualified colleagues across medical sub-specialties, establishing clinical support and second-opinion networks.",
    "b3_title": "Exclusive Event Privileges",
    "b3_desc": "Complimentary access and exclusive privileges to all IMA future scientific, cultural, and annual gala banquets across the UK and Europe.",
    "b4_title": "RCP-Approved CPD Points",
    "b4_desc": "Earn formal Continuing Professional Development (CPD) credits approved by the Royal College of Physicians for annual GMC revalidation.",
    "b5_title": "International Lectures & Masterclasses",
    "b5_desc": "Access to live and online symposia in London, European capitals, and joint academic masterclasses with Iraqi and Arab medical faculties.",
    "b6_title": "Specialty Interest Groups",
    "b6_desc": "Join dedicated sub-specialty clinical forums (Cardiology, Surgery, Pediatrics, Women's Health, Primary Care, and Junior Trainees).",
    "b7_title": "Trainee Doctor International Bursaries",
    "b7_desc": "Financial bursaries and sponsorship support for junior doctors and international medical graduates (IMGs) to present original research at international conferences.",
    "benefits_cta_btn": "Apply for Certified Membership (Free)",

    # AGM 2025 Portal Section
    "agm_sec_badge": "Academic Conference",
    "agm_sec_title": "Annual General Meeting & Scientific Conference 2025",
    "agm_sec_lead": "London, United Kingdom & Hybrid European Broadcast · Royal College of Physicians CPD Accreditation",
    "agm_c1_badge": "Plenary Sessions",
    "agm_c1_title": "Keynote Scientific Lectures",
    "agm_c1_desc": "Distinguished NHS and European consultant speakers presenting breakthroughs in surgical robotics, cardiology intervention, oncology care, and modern healthcare leadership.",
    "agm_c1_li1": "✓ Keynote consultant panel discussions",
    "agm_c1_li2": "✓ Multi-disciplinary team (MDT) case reviews",
    "agm_c1_li3": "✓ Clinical ethics & healthcare reform",
    "agm_c2_badge": "Research Competition",
    "agm_c2_title": "Junior Doctor & IMG Posters",
    "agm_c2_desc": "Annual research poster presentation open to foundation doctors, specialty trainees, and medical students. Gold, Silver, and Bronze awards presented at the Gala Dinner.",
    "agm_c2_li1": "✓ Abstract deadline: 30 September 2025",
    "agm_c2_li2": "✓ Peer-reviewed poster publication",
    "agm_c2_li3": "✓ Travel bursaries for winners",
    "agm_c3_badge": "Dinner & Culture",
    "agm_c3_title": "Annual Gala & Awards Banquet",
    "agm_c3_desc": "An evening of collegial fellowship, recognition of lifetime achievements in the NHS, authentic Iraqi musical entertainment, and networking across generations of doctors.",
    "agm_c3_li1": "✓ Black tie / Formal attire",
    "agm_c3_li2": "✓ Lifetime service award ceremonies",
    "agm_c3_li3": "✓ Family and guest welcome reception",
    "agm_sec_btn": "Explore Complete AGM 2025 Programme & Registration",

    # Education & Humanitarian
    "edu_sec_badge": "Humanitarian & Educational Impact",
    "edu_sec_title": "Red Crescent Training & Surgical Masterclasses",
    "edu_sec_desc": "In continuous partnership with the <strong>Iraqi Red Crescent Society</strong> and European academic medical institutions, our fellows conduct clinical skills workshops, advanced trauma life support simulation, and specialized obstetrics & gynaecology preparation (including the Karbala MRCOG workshop).",
    "edu_card1_title": "Trauma & Resuscitation",
    "edu_card1_desc": "Hands-on simulation and disaster medicine protocols.",
    "edu_card2_title": "Postgraduate MRCOG & FRCS",
    "edu_card2_desc": "Exam workshops supporting doctors pursuing British College diplomas.",
    "edu_sec_btn": "View All Training Programs & Lecture Recordings",

    # Scientific Posters
    "posters_sec_badge": "Research Repository",
    "posters_sec_title": "Scientific Posters & Clinical Research",
    "posters_sec_lead": "Peer-reviewed medical research, clinical audits, and quality improvement projects presented by our members.",
    "p1_badge": "Surgical Audit",
    "p1_title": "Acute Abdominal Surgical Interventions in the NHS",
    "p1_desc": "Review of operative timing, post-surgical complications, and mortality reduction protocols.",
    "p1_btn": "View Full Poster (PDF)",
    "p2_badge": "Cardiovascular Medicine",
    "p2_title": "Secondary Prevention Pathways in Ischemic Heart Disease",
    "p2_desc": "Analysis of lipid management, anti-platelet therapy adherence, and cardiac rehabilitation.",
    "p2_btn": "View Full Poster (PDF)",
    "p3_badge": "Medical Education",
    "p3_title": "Transitioning International Medical Graduates to NHS Practice",
    "p3_desc": "Evaluating structured induction programs, GMC communication, and supervised clinical fellowships.",
    "p3_btn": "View Full Poster (PDF)",
    "posters_sec_btn": "Explore All 2025 Posters & Submit Abstract",

    # Registration Form
    "form_badge": "Official Registration",
    "form_title": "Certified Member Enrolment",
    "form_lead": "Registration is 100% free of charge. Open to qualified doctors, surgeons, dental practitioners, and academic clinical researchers in the UK and Europe.",
    "form_label_name": "Full Legal Name (with titles) *",
    "form_label_email": "Professional / NHS Email *",
    "form_label_country": "Country of Practice *",
    "form_label_specialty": "Clinical Specialty *",
    "form_label_gmc": "Medical Reg / GMC No.",
    "form_label_hospital": "Current Hospital / Academic Institution",
    "form_label_interests": "Areas of Interest / Collaboration",
    "form_privacy_note": "🔒 <strong>Data Privacy Guarantee:</strong> Your information is retained strictly for official association records and communications in accordance with UK GDPR. We never share member details with commercial entities.",
    "form_submit": "Submit Certified Member Enrolment",

    # Sister Societies
    "links_sec_badge": "Global Diaspora & Academia",
    "links_sec_title": "Sister Associations & Medical Faculties",
    "links_sec_lead": "Collaborating with Iraqi medical societies across the globe and universities across Iraq.",
    "links_card_all": "All 12 Colleges →",
    "links_card_all_sub": "Explore Full University Directory",

    # Footer
    "footer_p": "Established in London in 1991 to unite, support, and advance Iraqi medical professionals across Great Britain and continental Europe. A non-profit, non-political professional body dedicated to clinical excellence and humanitarian education.",
    "footer_col2_title": "Association Portals",
    "footer_col3_title": "Integrity & Trust",
    "footer_col4_title": "Official Channels",
    "footer_copyright": "© 1991–2026 Iraqi Medical Association UK & Europe. All rights reserved."
  },

  "ar": {
    # Brand & Verification
    "verify_badge": "الجمعية الطبية الرسمية غير الربحية في المملكة المتحدة وأوروبا (تأسست عام 1991)",
    "brand_name": "الجمعية الطبية العراقية",
    "brand_sub": "المملكة المتحدة وأوروبا",
    "brand_ar": "Iraqi Medical Association UK & Europe",

    # Navigation
    "nav_home": "الرئيسية",
    "nav_about": "عن الجمعية والقيادة",
    "nav_agm": "المؤتمر السنوي 2025",
    "nav_membership": "العضوية والامتيازات",
    "nav_education": "التعليم الطبي والتطوير",
    "nav_posters": "الأبحاث والملصقات",
    "nav_archive": "الأرشيف التذكاري",
    "nav_news": "الأخبار والتنويهات",
    "nav_contact": "الاتصال بالأمانة العامة",
    "btn_enrol": "تسجيل الأطباء",
    "btn_join_free": "الانضمام للعضوية مجاناً",

    # Hero Section
    "hero_badge": "المؤسسة المهنية الرائدة للأطباء العراقيين في بريطانيا وأوروبا",
    "hero_title": "نلتقي لنرتقي برعاية صحية رائدة، <span class=\"gold-accent\">ونجمع قادة الطب</span> منذ عام 1991.",
    "hero_lead": "تأسست الجمعية الطبية العراقية عقب حرب الخليج الثانية لتوحيد الأطباء واستشاريي هيئة الخدمات الصحية البريطانية (NHS) والباحثين والأكاديميين في بريطانيا وإيرلندا وأوروبا. نلتزم بالتعليم الطبي المستمر والتدريب الإنساني والاعتماد المهني.",
    "hero_agm_btn": "مؤتمر الجمعية السنوي 2025",
    "hero_member_btn": "الانضمام للعضوية المعتمدة (مجاناً)",
    "stat_founded": "سنة التأسيس في لندن",
    "stat_agms": "مؤتمراً علمياً سنوياً",
    "stat_doctors": "طبيباً مؤهلاً في شبكتنا",
    "poster_badge": "المؤتمر السنوي العام 2025",
    "poster_title": "المؤتمر العلمي السنوي والاجتماع العام",
    "poster_sub": "ندوات استشارية · نقاط معتمدة من الكلية الملكية · مسابقة أبحاث الأطباء المقيمين",
    "cd_days": "أيام",
    "cd_hours": "ساعات",
    "cd_mins": "دقائق",
    "cd_secs": "ثواني",
    "agm_btn_small": "التسجيل في المؤتمر وإرشادات الأبحاث ←",

    # Anti-Fraud Advisory
    "advisory_badge": "تنويه رسمي هام وتحذير أمني ضد الاحتيال (تاريخ 12.05.2026):",
    "advisory_text": "تود الجمعية الطبية العراقية في المملكة المتحدة وأوروبا أن تلفت عناية الزملاء الأطباء في العراق إلى أن هناك جهات غير مخولة تقوم بإرسال دعوات مزورة. نؤكد أنه <em>لا يوجد</em> أي وكيل أو ممثل رسمي للجمعية داخل العراق، وجميع المؤتمرات والعضويات تُدار حصراً عبر موقعنا الرسمي وأمانتنا العامة في لندن.",
    "advisory_link": "قراءة التنويه القانوني الكامل ←",

    # About & Heritage
    "about_badge": "إرث تاريخي وقيادة ديمقراطية",
    "about_title": "أكثر من ثلاثة عقود من التضامن الطبي والعلمي",
    "about_p1": "تأسست <strong>الجمعية الطبية العراقية</strong> عام 1991 عقب انتهاء حرب الخليج الثانية وما نتج عنها من تحديات كبيرة أثرت على البنية التحتية في الوطن. انبثق ميثاق الجمعية لتوحيد الأطباء العراقيين في المملكة المتحدة وإيرلندا وتوفير منصة ديمقراطية وعلمية واجتماعية جامعة.",
    "about_p2": "ترأس الجمعية في عامها التأسيسي الأول <strong>د. هشام حسن</strong>، وتوالى على رئاستها أطباء كرام فازوا في انتخابات ديمقراطية شفافة: <em>د. ماهر الهلالي، د. فريال أحمد، د. إسماعيل الجليلي، د. خالد الشافي، د. وليد الوالي، د. محمد السعدي، د. فرحان باقر، د. زهير البحراني، د. إحسان البحراني، د. خالد ناجي، د. عبد الأمير علاوي، د. سالم الدملوجي، د. عبد المجيد</em>، إلى جانب جهود مميزة من زملاء مثل <em>د. منال نصيح</em> و<em>د. تحسين مزهر</em>.",
    "about_btn_history": "قراءة التاريخ الكامل وميثاق الشرف",
    "about_btn_gallery": "مشاهدة الأرشيف التذكاري (1999–2026)",
    "archive_card_badge": "وثيقة من الأرشيف التاريخي",
    "archive_card_title": "الاجتماع التأسيسي في لندن — أغسطس 1999",
    "archive_card_desc": "صورة تذكارية تجمع الرعيل الأول من استشاريي وجراحي وأكاديميي العراق في بريطانيا.",

    # 7 Pillars of Membership
    "benefits_badge": "العضوية المهنية المعتمدة",
    "benefits_title": "الأركان السبعة لعضوية الجمعية الطبية العراقية",
    "benefits_lead": "العضوية مجانية بالكامل لجميع الأطباء البشريين وأطباء الأسنان والباحثين السريريين المؤهلين في بريطانيا وأوروبا. انضم لأكثر من 1,200 زميل.",
    "b1_title": "التطوير والارتقاء المهني",
    "b1_desc": "إرشاد تخصصي عبر سجلات الاختصاص في الـ NHS، مسار CESR/Portfolio، والمساعدة في لجان تعيين الاستشاريين.",
    "b2_title": "التضامن السريري والعمل المشترك",
    "b2_desc": "التواصل مع زملاء المهنة من ذوي الكفاءات العالية عبر مختلف التخصصات وتوفير فرق عمل طبية وموارد استشارية متقدمة.",
    "b3_title": "امتيازات خاصة بالمؤتمرات",
    "b3_desc": "أولوية وحسومات وإعفاءات للأعضاء في جميع المؤتمرات العلمية والمحاضرات وحفلات العشاء السنوية الفاخرة.",
    "b4_title": "نقاط CPD معتمدة من الكلية الملكية للأطباء",
    "b4_desc": "مواكبة أحدث التطورات الطبية واكتساب نقاط التطوير المهني المستمر (CPD) المعتمدة من Royal College of Physicians لإعادة الترخيص GMC.",
    "b5_title": "محاضرات دولية وورش عمل تدريبية",
    "b5_desc": "المشاركة في المحاضرات الحية والافتراضية في لندن وعواصم أوروبا، والفعاليات الأكاديمية المشتركة مع كليات الطب في العراق والعالم العربي.",
    "b6_title": "مجموعات التخصص والاهتمام المهني",
    "b6_desc": "الانضمام إلى لجان التخصصات السريرية (القلبية، الجراحة، طب الأطفال، صحة المرأة، الرعاية الأولية، والأطباء المقيمين).",
    "b7_title": "منح سفر وتغطية للأطباء المتدربين",
    "b7_desc": "منح مالية ورعاية مخصصة للأطباء الشباب وخريجي كليات الطب الدولية (IMGs) لتقديم أبحاثهم المبتكرة في المؤتمرات الطبية الدولية.",
    "benefits_cta_btn": "التقديم على العضوية المعتمدة (مجاناً)",

    # AGM 2025 Section
    "agm_sec_badge": "مؤتمر أكاديمي دولي",
    "agm_sec_title": "المؤتمر العلمي والاجتماع العام السنوي 2025",
    "agm_sec_lead": "لندن، المملكة المتحدة وبث افتراضي مباشر لعموم أوروبا · معتمد بنقاط CPD من الكلية الملكية للأطباء",
    "agm_c1_badge": "الجلسات العامة",
    "agm_c1_title": "محاضرات علمية استشارية متقدمة",
    "agm_c1_desc": "استشاريون بارزون من بريطانيا وأوروبا يقدمون أحدث الابتكارات في الجراحة الروبوتية، قسطرة القلب التداخلية، وعلاج الأورام.",
    "agm_c1_li1": "✓ جلسات حوارية ونقاشات مع كبار الاستشاريين",
    "agm_c1_li2": "✓ مراجعة حالات سريرية معقدة متعددة التخصصات (MDT)",
    "agm_c1_li3": "✓ أخلاقيات الممارسة الطبية وتطوير الرعاية الصحية",
    "agm_c2_badge": "مسابقة البحوث الطبية",
    "agm_c2_title": "أبحاث وملصقات الأطباء المقيمين والـ IMGs",
    "agm_c2_desc": "مسابقة علمية سنوية مفتوحة للأطباء المتدربين وطلبة الطب لتقديم أبحاثهم، مع تكريم الفائزين بجوائز ذهبية وفضية في حفل العشاء.",
    "agm_c2_li1": "✓ الموعد النهائي لاستلام الملخصات: 30 سبتمبر 2025",
    "agm_c2_li2": "✓ نشر الملصقات العلمية المحكمة",
    "agm_c2_li3": "✓ منح سفر للأبحاث الفائزة",
    "agm_c3_badge": "حفل العشاء واللقاء الثقافي",
    "agm_c3_title": "حفل العشاء السنوي وتكريم رواد الطب",
    "agm_c3_desc": "أمسية راقية لتعزيز أواصر الزمالة وتكريم الأطباء أصحاب المسيرة الطويلة في خدمة الـ NHS، مع فقرات ثقافية مميزة.",
    "agm_c3_li1": "✓ الزي الرسمي / ربطة عنق سوداء",
    "agm_c3_li2": "✓ تكريم رواد الخدمة الطبية مدى الحياة",
    "agm_c3_li3": "✓ حفل استقبال ترحيبي بالعائلات والضيوف",
    "agm_sec_btn": "استكشاف برنامج المؤتمر الكامل والتسجيل",

    # Education & Humanitarian
    "edu_sec_badge": "أثر إنساني وأكاديمي",
    "edu_sec_title": "تدريب الهلال الأحمر والورش الجراحية المتقدمة",
    "edu_sec_desc": "بالتعاون المستمر مع <strong>جمعية الهلال الأحمر العراقي</strong> والمؤسسات الطبية الأوروبية، ينظم زملاؤنا ورش عمل للإنعاش المتقدم في طب الطوارئ، والمحاكاة الجراحية، ودورات تخصصية للتحضير للزمالات البريطانية كورشة كربلاء لامتحانات MRCOG.",
    "edu_card1_title": "طب الطوارئ والإنعاش المتقدم",
    "edu_card1_desc": "تدريب محاكاة سريري للتعامل مع الإصابات والحوادث الكبرى.",
    "edu_card2_title": "الزمالات الملكية MRCOG و FRCS",
    "edu_card2_desc": "ورش تدريبية لدعم الأطباء المتقدمين لامتحانات الكليات الملكية البريطانية.",
    "edu_sec_btn": "مشاهدة جميع البرامج التدريبية وتسجيلات المحاضرات",

    # Scientific Posters
    "posters_sec_badge": "مستودع الأبحاث",
    "posters_sec_title": "الملصقات العلمية والتدقيق السريري",
    "posters_sec_lead": "أبحاث طبية محكمة ومشاريع تحسين الجودة السريرية المقدمة من أعضاء الجمعية في المؤتمرات السنوية.",
    "p1_badge": "تدقيق جراحي",
    "p1_title": "التدخلات الجراحية للحالات البطنية الحادة في الـ NHS",
    "p1_desc": "مراجعة توقيت العمليات الجراحية وتقليل المضاعفات بعد الجراحة لدى كبار السن.",
    "p1_btn": "عرض الملصق البحثي (PDF)",
    "p2_badge": "طب القلب والأوعية",
    "p2_title": "مسارات الوقاية الثانوية لمرضى نقص التروية القلبية",
    "p2_desc": "تحليل ضبط الدهون الدوائي والالتزام بالعلاج المضاد للصفيحات وإعادة التأهيل القلبي.",
    "p2_btn": "عرض الملصق البحثي (PDF)",
    "p3_badge": "التعليم الطبي",
    "p3_title": "انتقال الأطباء خريجي الجامعات الدولية للعمل في الـ NHS",
    "p3_desc": "تقييم برامج التدريب التوجيهي، التواصل المهني مع الـ GMC، والزمالات السريرية الخاضعة للإشراف.",
    "p3_btn": "عرض الملصق البحثي (PDF)",
    "posters_sec_btn": "استعراض جميع أبحاث 2025 وتقديم ملخص بحثي",

    # Registration Form
    "form_badge": "بوابة التسجيل الرسمية",
    "form_title": "تسجيل عضوية معتمدة مجانية",
    "form_lead": "التسجيل مجاني بالكامل 100%. متاح لجميع الأطباء البشريين وأطباء الأسنان والباحثين السريريين المؤهلين في بريطانيا وأوروبا.",
    "form_label_name": "الاسم القانوني الكامل (مع الألقاب الطبية) *",
    "form_label_email": "البريد الإلكتروني المهني / NHS *",
    "form_label_country": "بلد الممارسة السريرية *",
    "form_label_specialty": "التخصص الطبي السريري *",
    "form_label_gmc": "رقم التسجيل الطبي / GMC",
    "form_label_hospital": "المستشفى أو المؤسسة الصحية الحالية",
    "form_label_interests": "مجالات الاهتمام / مقترحات التعاون",
    "form_privacy_note": "🔒 <strong>ضمان خصوصية البيانات:</strong> تُحفظ بياناتكم بسرية تامة لسجلات الجمعية الرسمية وفقاً للقانون البريطاني لحماية البيانات UK GDPR. لن نشارك بياناتكم مطلقاً مع أي جهة تجارية.",
    "form_submit": "إرسال طلب العضوية المعتمدة",

    # Sister Societies
    "links_sec_badge": "شبكة الأطباء والأكاديميا",
    "links_sec_title": "الجمعيات الزميلة وكليات الطب في العراق",
    "links_sec_lead": "تعاون وشراكة علمية مع جمعيات الأطباء العراقيين في المهجر وكليات الطب في الجامعات العراقية.",
    "links_card_all": "جميع كليات الطب (12 كلية) ←",
    "links_card_all_sub": "استعراض الدليل الجامعي الكامل",

    # Footer
    "footer_p": "تأسست في لندن عام 1991 لتوحيد ودعم الأطباء العراقيين في بريطانيا وعموم أوروبا. هيئة مهنية غير ربحية وغير سياسية مكرسة للتميز السريري والتعليم الطبي الإنساني.",
    "footer_col2_title": "بوابات الجمعية",
    "footer_col3_title": "المصداقية والأمان",
    "footer_col4_title": "القنوات الرسمية",
    "footer_copyright": "© 1991–2026 الجمعية الطبية العراقية في المملكة المتحدة وأوروبا. جميع الحقوق محفوظة."
  }
}

# Write this dictionary into assets/js/translations.json or directly inside main.js
with open('assets/js/translations.json', 'w', encoding='utf-8') as f:
    json.dump(translations_dict, f, ensure_ascii=False, indent=2)

print("Saved assets/js/translations.json successfully!")
