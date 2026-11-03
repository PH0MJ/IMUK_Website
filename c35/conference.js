/* 35th conference photo pages: language switch, photo viewer, print button. No dependencies. */
(function () {
  var root = document.documentElement;
  var box = document.getElementById('c35-lightbox');
  var img = box.querySelector('.lb-img');
  var text = box.querySelector('.lb-text');
  var dl = box.querySelector('.lb-dl');
  var links = Array.prototype.slice.call(document.querySelectorAll('[data-lightbox]'));
  var current = -1;

  function lang() { return root.getAttribute('data-lang') === 'ar' ? 'ar' : 'en'; }

  function setLang(l) {
    root.setAttribute('lang', l);
    root.setAttribute('dir', l === 'ar' ? 'rtl' : 'ltr');
    root.setAttribute('data-lang', l);
    document.querySelectorAll('[data-set-lang]').forEach(function (b) {
      b.classList.toggle('active', b.getAttribute('data-set-lang') === l);
    });
    document.querySelectorAll('.shot img').forEach(function (im) {
      if (!im.dataset.altEn) im.dataset.altEn = im.alt;
      im.alt = l === 'ar' ? im.dataset.altAr : im.dataset.altEn;
    });
    if (current >= 0) caption();
  }

  function caption() {
    var a = links[current];
    text.textContent = a.getAttribute('data-' + lang());
  }

  var fig = box.querySelector('.lb-figure');
  var token = 0;

  // Show the already-loaded thumbnail at once, then swap in the full-size photo when it has arrived.
  // On a slow connection the viewer is never blank, and a failed load says so instead of showing a broken icon.
  function show(i) {
    current = (i + links.length) % links.length;
    var a = links[current];
    var full = a.getAttribute('href');
    var thumb = a.querySelector('img');
    var mine = ++token;
    img.alt = a.getAttribute('data-' + lang());
    if (thumb && thumb.naturalWidth) img.style.setProperty('--ar', thumb.naturalWidth / thumb.naturalHeight);
    else img.style.removeProperty('--ar');
    img.src = (thumb && (thumb.currentSrc || thumb.src)) || full;
    fig.classList.add('loading');
    fig.classList.remove('failed');
    dl.href = full;
    dl.setAttribute('download', a.getAttribute('data-download'));
    caption();
    var big = new Image();
    big.onload = function () {
      if (mine !== token) return;
      img.style.setProperty('--ar', big.naturalWidth / big.naturalHeight);
      img.src = big.src;
      fig.classList.remove('loading');
    };
    big.onerror = function () {
      if (mine !== token) return;
      fig.classList.remove('loading');
      fig.classList.add('failed');
    };
    big.src = full;
  }

  function open(i) { show(i); box.hidden = false; document.body.style.overflow = 'hidden'; box.querySelector('.lb-close').focus(); }
  function close() { token++; box.hidden = true; img.removeAttribute('src'); document.body.style.overflow = ''; if (current >= 0) links[current].focus(); }

  links.forEach(function (a, i) {
    a.addEventListener('click', function (e) { e.preventDefault(); open(i); });
  });
  box.querySelector('.lb-close').addEventListener('click', close);
  box.querySelector('.lb-prev').addEventListener('click', function () { show(current - 1); });
  box.querySelector('.lb-next').addEventListener('click', function () { show(current + 1); });
  box.addEventListener('click', function (e) { if (e.target === box) close(); });
  document.addEventListener('keydown', function (e) {
    if (box.hidden) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') show(current - 1);
    else if (e.key === 'ArrowRight') show(current + 1);
  });

  document.querySelectorAll('[data-set-lang]').forEach(function (b) {
    b.addEventListener('click', function () {
      var l = b.getAttribute('data-set-lang');
      setLang(l);
      try { localStorage.setItem('ima_language', l); } catch (e) {}
    });
  });
  document.querySelectorAll('[data-print]').forEach(function (b) {
    b.addEventListener('click', function () { window.print(); });
  });

  // Start in the language chosen on the main site (same key it uses); ?lang=ar|en overrides.
  // The Arabic page for attendees from Iraq always starts in Arabic.
  function initialLang() {
    var q = new URLSearchParams(window.location.search).get('lang');
    if (q === 'ar' || q === 'en') return q;
    if (document.body.classList.contains('c35-uk')) {
      try {
        var s = localStorage.getItem('ima_language');
        if (s === 'ar' || s === 'en') return s;
      } catch (e) {}
    }
    return lang();
  }

  setLang(initialLang());
})();
