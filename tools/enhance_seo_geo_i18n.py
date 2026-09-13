import os
import re

SEO_GEO_HEAD = """  <!-- ======================================================================
       SEO & GEO OPTIMIZATION (Search Engines & Generative AI Search)
       ====================================================================== -->
  <meta name="geo.region" content="GB-LND" />
  <meta name="geo.placename" content="London, United Kingdom" />
  <meta name="geo.position" content="51.5074;-0.1278" />
  <meta name="ICBM" content="51.5074, -0.1278" />
  <meta name="coverage" content="United Kingdom, Europe, Iraq" />
  <meta name="audience" content="Medical Doctors, NHS Consultants, Surgeons, Healthcare Researchers" />
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />

  <!-- Multilingual Alternates for International SEO -->
  <link rel="alternate" hreflang="en-GB" href="https://www.iraqimedicalassociation-uk-eu.com/" />
  <link rel="alternate" hreflang="ar" href="https://www.iraqimedicalassociation-uk-eu.com/?lang=ar" />
  <link rel="alternate" hreflang="x-default" href="https://www.iraqimedicalassociation-uk-eu.com/" />

  <!-- Arabic & Latin Web Fonts (Cairo, Amiri, Playfair, Plus Jakarta Sans) -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Cairo:wght@400;600;700;800&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />

  <!-- Schema.org JSON-LD Structured Data: MedicalOrganization -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "MedicalOrganization",
    "name": "Iraqi Medical Association UK & Europe",
    "alternateName": ["IMA UK & Europe", "الجمعية الطبية العراقية في المملكة المتحدة وأوروبا", "IMA UK"],
    "url": "https://www.iraqimedicalassociation-uk-eu.com/",
    "logo": "https://www.iraqimedicalassociation-uk-eu.com/assets/images/WhatsApp_Image_2025-07-27_at_18.50.18-removebg-preview.png",
    "foundingDate": "1991",
    "description": "Non-profit professional medical association uniting Iraqi NHS consultants, physicians, dental surgeons, and researchers across the UK and Europe. Established in London in 1991.",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "London",
      "addressCountry": "GB"
    },
    "areaServed": [
      { "@type": "Country", "name": "United Kingdom" },
      { "@type": "Country", "name": "Ireland" },
      { "@type": "Country", "name": "Germany" },
      { "@type": "Country", "name": "France" },
      { "@type": "Country", "name": "Iraq" }
    ],
    "sameAs": [
      "https://www.facebook.com/IMAUK",
      "https://www.instagram.com/iraqimedicalassociation.uk.eu/#",
      "https://x.com/ima_uk",
      "https://ima-uk.forumotion.com/register"
    ],
    "memberOf": {
      "@type": "Organization",
      "name": "British & European Healthcare Diaspora Council"
    }
  }
  </script>

  <!-- Schema.org JSON-LD Structured Data: Conference Event (AGM 2025) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Event",
    "name": "Iraqi Medical Association UK & Europe AGM 2025 | Annual Scientific Conference",
    "description": "Annual scientific congress featuring consultant keynote lectures, Royal College of Physicians CPD points, junior doctor research posters, and formal gala dinner.",
    "startDate": "2025-10-18T09:00:00+01:00",
    "endDate": "2025-10-18T22:30:00+01:00",
    "eventAttendanceMode": "https://schema.org/MixedEventAttendanceMode",
    "eventStatus": "https://schema.org/EventScheduled",
    "location": [
      {
        "@type": "Place",
        "name": "London Conference Centre",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "London",
          "addressCountry": "GB"
        }
      },
      {
        "@type": "VirtualLocation",
        "url": "https://www.iraqimedicalassociation-uk-eu.com/agm2025.html"
      }
    ],
    "organizer": {
      "@type": "MedicalOrganization",
      "name": "Iraqi Medical Association UK & Europe",
      "url": "https://www.iraqimedicalassociation-uk-eu.com/"
    },
    "offers": {
      "@type": "Offer",
      "url": "https://www.iraqimedicalassociation-uk-eu.com/agm2025.html#register-conference",
      "price": "0",
      "priceCurrency": "GBP",
      "availability": "https://schema.org/InStock"
    }
  }
  </script>

  <!-- Schema.org JSON-LD: FAQPage for AI Search (Gemini, Google AI Overviews, Perplexity) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is the Iraqi Medical Association UK & Europe (IMA UK)?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Iraqi Medical Association UK & Europe is a non-profit, non-political professional body established in London in 1991. It unites Iraqi physicians, NHS consultants, dental surgeons, and clinical researchers practicing throughout Great Britain and continental Europe."
        }
      },
      {
        "@type": "Question",
        "name": "Is membership in the Iraqi Medical Association free?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, certified membership in the IMA UK & Europe is 100% free of charge for all qualified medical practitioners, NHS trainees, and clinical researchers in the UK and Europe."
        }
      },
      {
        "@type": "Question",
        "name": "Does the IMA UK & Europe have representatives or agents inside Iraq?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. In an official anti-fraud legal disclaimer issued on 12 May 2026, the IMA UK & Europe confirmed that it does not have any agents or representatives inside Iraq. All official invitations and conferences are conducted solely through verified executive channels and the official website."
        }
      },
      {
        "@type": "Question",
        "name": "Are the IMA Annual General Meetings accredited for CPD points?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes, the IMA Annual General Meeting and Scientific Conference (AGM) provides formal CPD credits approved by the Royal College of Physicians (RCP) for annual GMC revalidation."
        }
      }
    ]
  }
  </script>
"""

LANG_SWITCHER_TOP = """        <div class="lang-switcher">
          <button class="lang-btn active" data-lang="en">EN</button>
          <button class="lang-btn" data-lang="ar">العربية</button>
        </div>"""

NAV_LANG_SWITCHER = """        <div class="nav-lang-switcher" style="margin-left: 0.5rem;">
          <button class="lang-btn active" data-lang="en">EN</button>
          <button class="lang-btn" data-lang="ar">العربية</button>
        </div>"""

files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'preview_concepts.html']

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Inject SEO/GEO Head if not present
    if "<!-- Multilingual Alternates for International SEO -->" not in html:
        html = html.replace("</head>", f"{SEO_GEO_HEAD}\n</head>")

    # 2. Inject Top bar language switcher
    if '<span class="arabic-subtitle">' in html and 'class="lang-switcher"' not in html:
        html = html.replace(
            '<span class="arabic-subtitle">الجمعية الطبية العراقية</span>',
            f'<span class="arabic-subtitle">الجمعية الطبية العراقية</span>\n{LANG_SWITCHER_TOP}'
        )

    # 3. Inject Nav language switcher near mobile button
    if '<button class="mobile-nav-toggle"' in html and 'class="nav-lang-switcher"' not in html:
        html = html.replace(
            '<button class="mobile-nav-toggle"',
            f'{NAV_LANG_SWITCHER}\n        <button class="mobile-nav-toggle"'
        )

    # 4. Inject mobile drawer switcher
    if '<div class="mobile-drawer">' in html and 'data-lang="ar"' not in html.split('<div class="mobile-drawer">')[1]:
        drawer_insert = """    <div class="mobile-drawer">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--c-border);">
        <span style="font-size: 0.8rem; font-weight: 700; color: var(--c-navy-900);">Language / اللغة:</span>
        <div class="nav-lang-switcher">
          <button class="lang-btn active" data-lang="en">English</button>
          <button class="lang-btn" data-lang="ar">العربية</button>
        </div>
      </div>"""
        html = html.replace('<div class="mobile-drawer">', drawer_insert)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated SEO/GEO and language switcher in {fname}")

print("\n[✓] ALL HTML files successfully boosted with SEO, GEO tags, JSON-LD Schemas, and EN/AR language toggle!")
