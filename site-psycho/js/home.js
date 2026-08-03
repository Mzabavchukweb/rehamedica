/* Strona główna serwisu psychoterapeutycznego.
   Moduły niezależne; każdy kończy działanie, gdy nie znajdzie swojego węzła. */
(function () {
  'use strict';

  /* ── widget hero: sytuacja + miasto → dokąd zadzwonić ──────────────────
     Wzorzec Grow Therapy (stan + ubezpieczenie → „Find a provider”).
     Tutaj: sytuacja + miasto → usługa, dostępność i numer recepcji.
     ŻADNE pole nie jest wstępnie wybrane (reguła CLAUDE.md). */
  (function () {
    var box = document.querySelector('[data-szuk]');
    if (!box) return;

    var syt = box.querySelector('[data-syt]');
    var mia = box.querySelector('[data-mia]');
    var out = box.querySelector('[data-out]');
    var imgs = document.querySelectorAll('.hero3__img');
    if (!syt || !mia || !out) return;

    var REC = {
      szczecinek: ['Szczecinku',  '94 372 14 51', '+48943721451'],
      szczecin:   ['Szczecinie',  '530 661 982',  '+48530661982'],
      walcz:      ['Wałczu',      '530 661 982',  '+48530661982'],
      bialogard:  ['Białogardzie','535 960 018',  '+48535960018'],
      bobolice:   ['Bobolicach',  '530 645 059',  '+48530645059']
    };
    function esc(t) {
      return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }
    /* zdjęcie idzie za wybraną sytuacją — interakcja niesie treść, nie ozdobę */
    function foto(i) {
      for (var n = 0; n < imgs.length; n++) imgs[n].classList.toggle('is-on', n === i);
    }

    function pokaz() {
      var o = syt.selectedOptions ? syt.selectedOptions[0] : syt.options[syt.selectedIndex];
      var wSyt = syt.value, wMia = mia.value;
      if (wSyt) foto(syt.selectedIndex - 1);          // −1: pierwsza opcja to „Wybierz…”

      if (!wSyt && !wMia) {
        out.innerHTML = '<span class="szuk__brak">Wybierz oba pola — pokażemy, jaka pomoc tego dotyczy i dokąd zadzwonić.</span>';
        return;
      }
      var usluga = o && o.dataset ? (o.dataset.usluga || '') : '';
      var cel = o && o.dataset ? (o.dataset.cel || '') : '';
      var gdzie = (o && o.dataset && o.dataset.fac) ? o.dataset.fac.split(' ').filter(Boolean) : [];

      if (wSyt && !wMia) {
        out.innerHTML = '<b>' + esc(usluga) + '.</b> <span class="szuk__brak">Wskaż miasto, żeby zobaczyć dostępność i numer recepcji.</span>';
        return;
      }
      if (!wSyt && wMia) {
        out.innerHTML = '<span class="szuk__brak">Wskaż, z czym przychodzisz.</span>';
        return;
      }

      var r = REC[wMia];
      // źródło nie wskazuje miasta dla tej usługi — nie zgadujemy, że jej tam nie ma
      if (!gdzie.length) {
        out.innerHTML = '<b>' + esc(usluga) + '</b> — dostępność w ' + esc(r[0]) +
          ' potwierdza recepcja. <a class="szuk__tel" href="tel:' + r[2] + '">' + r[1] + '</a>' +
          '<br><a class="szuk__go" href="' + cel + '/">Zobacz zakres <span aria-hidden="true">&rarr;</span></a>';
        return;
      }
      // decyzja właściciela: nie ma w tej placówce = niedostępne, bez kierowania gdzie indziej
      if (gdzie.indexOf(wMia) === -1) {
        out.innerHTML = '<b>' + esc(usluga) + '</b> — <span class="szuk__brak">niedostępne w ' + esc(r[0]) + '.</span>';
        return;
      }
      out.innerHTML = '<b>' + esc(usluga) + '</b> w ' + esc(r[0]) + '. ' +
        '<a class="szuk__tel" href="tel:' + r[2] + '">' + r[1] + '</a>' +
        '<br><a class="szuk__go" href="' + cel + '/">Zobacz zakres <span aria-hidden="true">&rarr;</span></a>';
    }

    syt.addEventListener('change', pokaz);
    mia.addEventListener('change', pokaz);
    pokaz();   // stan wyjściowy: nic nie wybrane, podpowiedź co zrobić
  })();

  /* ── dostępność w sekcji „Zakres pomocy" idzie za wyborem miasta w hero ── */
  (function () {
    var mia = document.querySelector('[data-mia]');
    var poz = document.querySelectorAll('.zakres__i[data-fac]');
    if (!mia || !poz.length) return;
    mia.addEventListener('change', function () {
      var city = mia.value;
      Array.prototype.forEach.call(poz, function (el) {
        var gdzie = (el.dataset.fac || '').split(' ').filter(Boolean);
        el.setAttribute('data-avail',
          !city ? '' : (gdzie.length === 0 ? 'ask' : (gdzie.indexOf(city) > -1 ? 'yes' : 'no')));
      });
    });
  })();
})();
