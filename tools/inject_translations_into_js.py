# inject_translations_into_js.py
with open('assets/js/translations.json', 'r', encoding='utf-8') as f:
    dict_content = f.read()

prefix = """/**
 * Iraqi Medical Association UK & Europe (IMA UK)
 * Concept 1: Institutional Heritage Engine
 * Lightweight Vanilla JS (< 15KB, 0 dependencies)
 * Features: Mobile Nav, Dynamic Countdown, Form Validation, Poster Filter, Lightbox, Multilingual EN/AR Toggle
 */

document.addEventListener('DOMContentLoaded', () => {
  initLanguageToggle();
  initMobileNav();
  initCountdown();
  initRegistrationForm();
  initPosterFilters();
  initLightbox();
});

/* --------------------------------------------------------------------------
   Multilingual EN / AR Toggle System
   -------------------------------------------------------------------------- */
const translations = """

suffix = """;

function initLanguageToggle() {
  const urlParams = new URLSearchParams(window.location.search);
  const langQuery = urlParams.get('lang');
  const storedLang = localStorage.getItem('ima_language');
  
  const currentLang = (langQuery === 'ar' || storedLang === 'ar') ? 'ar' : 'en';
  setLanguage(currentLang, false);

  // Attach event listeners to all lang toggle buttons
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const targetLang = btn.dataset.lang;
      setLanguage(targetLang, true);
    });
  });
}

function setLanguage(lang, animate) {
  if (typeof animate === 'undefined') animate = true;
  const isArabic = (lang === 'ar');
  document.documentElement.lang = isArabic ? 'ar' : 'en-GB';
  document.documentElement.dir = isArabic ? 'rtl' : 'ltr';

  try {
    localStorage.setItem('ima_language', lang);
  } catch (e) {}

  // Update active state on toggle buttons
  document.querySelectorAll('.lang-btn').forEach(btn => {
    if (btn.dataset.lang === lang) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  if (animate) {
    document.body.style.transition = 'opacity 0.15s ease';
    document.body.style.opacity = '0.75';
  }

  // Apply translations to data-i18n elements
  const t = translations[lang] || translations.en;
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (t[key]) {
      if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
        el.placeholder = t[key];
      } else {
        el.innerHTML = t[key];
      }
    }
  });

  if (animate) {
    setTimeout(() => {
      document.body.style.opacity = '1';
    }, 120);
  }
}

/* --------------------------------------------------------------------------
   Mobile Navigation Drawer
   -------------------------------------------------------------------------- */
function initMobileNav() {
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const drawer = document.querySelector('.mobile-drawer');

  if (!toggleBtn || !drawer) return;

  toggleBtn.addEventListener('click', () => {
    const isOpen = drawer.classList.toggle('open');
    toggleBtn.setAttribute('aria-expanded', isOpen);
  });

  drawer.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      drawer.classList.remove('open');
      toggleBtn.setAttribute('aria-expanded', 'false');
    });
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('open')) {
      drawer.classList.remove('open');
      toggleBtn.setAttribute('aria-expanded', 'false');
    }
  });
}

/* --------------------------------------------------------------------------
   AGM 2025 Dynamic Countdown Clock
   -------------------------------------------------------------------------- */
function initCountdown() {
  const countdownEl = document.getElementById('agm-countdown');
  if (!countdownEl) return;

  const targetDate = new Date('2026-11-14T09:00:00Z').getTime();

  function updateClock() {
    const now = new Date().getTime();
    const diff = targetDate - now;

    if (diff <= 0) {
      countdownEl.innerHTML = '<div class="text-c1gold-500 font-bold p-2">AGM 2025 / 2026 In Session Now</div>';
      return;
    }

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);

    const dEl = document.getElementById('cd-days');
    const hEl = document.getElementById('cd-hours');
    const mEl = document.getElementById('cd-mins');
    const sEl = document.getElementById('cd-secs');

    if (dEl) dEl.textContent = String(days).padStart(2, '0');
    if (hEl) hEl.textContent = String(hours).padStart(2, '0');
    if (mEl) mEl.textContent = String(minutes).padStart(2, '0');
    if (sEl) sEl.textContent = String(seconds).padStart(2, '0');
  }

  updateClock();
  setInterval(updateClock, 1000);
}

/* --------------------------------------------------------------------------
   Membership & Contact Form Instant Validation
   -------------------------------------------------------------------------- */
function initRegistrationForm() {
  const regForm = document.getElementById('ima-member-form');
  const alertBox = document.getElementById('form-feedback');

  if (!regForm) return;

  regForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const nameInput = regForm.querySelector('input[name="full_name"]');
    const emailInput = regForm.querySelector('input[name="email"]');

    if (!nameInput.value.trim() || !emailInput.value.trim()) {
      showFeedback('Please fill in your Full Name and Professional Email.', 'error');
      return;
    }

    const submitBtn = regForm.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerHTML;
    submitBtn.disabled = true;
    submitBtn.innerHTML = 'Submitting Certified Application...';

    setTimeout(() => {
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalText;
      regForm.reset();
      showFeedback('Thank you, Dr. ' + nameInput.value + '! Your certified membership enrolment has been submitted to the Executive Secretariat. You will receive an official confirmation via email.', 'success');
    }, 600);
  });

  function showFeedback(msg, type) {
    if (!alertBox) {
      alert(msg);
      return;
    }
    alertBox.textContent = msg;
    alertBox.className = type === 'success' ? 'p-4 rounded bg-emerald-50 text-emerald-900 border border-emerald-300 block mb-4 text-sm' : 'p-4 rounded bg-rose-50 text-rose-900 border border-rose-300 block mb-4 text-sm';
    alertBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
}

/* --------------------------------------------------------------------------
   Posters & Directory Live Search / Filter
   -------------------------------------------------------------------------- */
function initPosterFilters() {
  const filterButtons = document.querySelectorAll('.filter-btn');
  const filterItems = document.querySelectorAll('.filterable-item');

  if (!filterButtons.length) return;

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.dataset.filter;

      filterButtons.forEach(b => b.classList.remove('active', 'btn-gold'));
      btn.classList.add('active', 'btn-gold');

      filterItems.forEach(item => {
        if (filter === 'all' || item.dataset.category === filter) {
          item.style.display = '';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });
}

/* --------------------------------------------------------------------------
   Simple Lightbox for Posters & Gallery
   -------------------------------------------------------------------------- */
function initLightbox() {
  const modal = document.getElementById('lightbox-modal');
  const modalImg = document.getElementById('lightbox-img');
  const modalCaption = document.getElementById('lightbox-caption');
  const closeBtn = document.getElementById('lightbox-close');

  if (!modal || !modalImg) return;

  document.querySelectorAll('[data-lightbox]').forEach(el => {
    el.addEventListener('click', (e) => {
      e.preventDefault();
      const imgSrc = el.getAttribute('href') || el.dataset.src;
      const caption = el.dataset.caption || el.querySelector('img')?.alt || '';
      
      modalImg.src = imgSrc;
      if (modalCaption) modalCaption.textContent = caption;
      modal.classList.add('open');
    });
  });

  function closeModal() {
    modal.classList.remove('open');
  }

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('open')) closeModal();
  });
}
"""

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(prefix + dict_content + suffix)

print("SUCCESS: Embedded dictionary into main.js!")
