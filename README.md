# Iraqi Medical Association UK & Europe (IMA UK)

Official portal for the **Iraqi Medical Association United Kingdom & Europe (IMA UK & Europe)** — established in London in 1991 to unite Iraqi physicians, NHS consultants, dental surgeons, and clinical researchers practicing across Great Britain and Europe.

## 🌐 Live Website
The website is hosted via GitHub Pages:
**[https://ph0mj.github.io/IMUK_Website/](https://ph0mj.github.io/IMUK_Website/)**

---

## 📋 Features
- **Bilingual Interface**: Full English and Arabic (العربية) translation switch with RTL typography.
- **Academic & Professional Portal**:
  - Annual General Meeting (AGM 2025) registration and schedule.
  - RCP CPD accreditation details.
  - Member enrolment and directory.
  - Education, clinical training, and humanitarian initiatives.
  - Scientific poster gallery and historical archive.
- **Search Engine & Generative AI Optimization (SEO / GEO)**: Rich Schema.org JSON-LD microdata (MedicalOrganization, Event, FAQPage), OpenGraph tags, and geolocation tags.
- **Pure Modern Web Stack**: Built with semantic HTML5, modern vanilla CSS3 design system, and responsive vanilla JavaScript — zero heavy framework dependencies for maximum performance and instant load times.

---

## 📁 Repository Structure
`	ext
IMUK_Website/
├── index.html              # Homepage
├── about.html              # About & Governance
├── agm2025.html            # AGM 2025 Conference
├── membership.html         # Member Enrolment
├── education.html          # Education & RCP CPD
├── posters.html            # Scientific Posters Gallery
├── gallery.html            # Photographic Archive
├── news.html               # News & Announcements
├── contact.html            # Executive Contact & Registry
├── useful-links.html       # NHS & General Medical Council Links
├── preview_concepts.html   # Design Concept Demos
├── assets/
│   ├── css/style.css       # Complete modern styling & themes
│   ├── js/main.js          # Interactive navigation & i18n logic
│   └── images/             # Optimized brand imagery & assets
├── tools/                  # Build & enhancement automation scripts
├── robots.txt              # Search engine crawler instructions
├── sitemap.xml             # XML Sitemap
└── .nojekyll               # Disables Jekyll processing on GitHub Pages
`

---

## 🚀 Local Development
To view the website locally, open index.html in any browser or launch a simple HTTP server:
`ash
# Using Python
python -m http.server 8000
`
Then navigate to http://localhost:8000/.
