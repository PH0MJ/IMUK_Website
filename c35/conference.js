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

  function show(i) {
    current = (i + links.length) % links.length;
    var a = links[current];
    img.src = a.getAttribute('href');
    img.alt = a.getAttribute('data-' + lang());
    dl.href = a.getAttribute('href');
    dl.setAttribute('download', a.getAttribute('data-download'));
    caption();
  }

  function open(i) { show(i); box.hidden = false; document.body.style.overflow = 'hidden'; box.querySelector('.lb-close').focus(); }
  function close() { box.hidden = true; img.removeAttribute('src'); document.body.style.overflow = ''; if (current >= 0) links[current].focus(); }

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
    b.addEventListener('click', function () { setLang(b.getAttribute('data-set-lang')); });
  });
  document.querySelectorAll('[data-print]').forEach(function (b) {
    b.addEventListener('click', function () { window.print(); });
  });

  setLang(lang());
})();
