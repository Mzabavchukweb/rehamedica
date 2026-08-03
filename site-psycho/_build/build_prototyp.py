# -*- coding: utf-8 -*-
"""
PROTOTYP — DO WYRZUCENIA. Nie jest częścią serwisu.

Odpowiada na jedno pytanie: który kierunek pierwszego ekranu wybieramy?
Trzy radykalnie różne warianty na jednej trasie, przełączane `?v=1|2|3`
paskiem na dole. Wybierasz jeden (albo kawałki z każdego), reszta idzie do kosza.

Ustalenia z przesłuchania 2026-08-01/02, wiążące dla wszystkich trzech:
  1. zostają tylko logo i kolory — reszta zaprojektowana od nowa
  2. głos: TY, w całym serwisie
  3. pierwszy ekran: zdanie + wybór sytuacji, bez banera ze zdjęciem
  4. stały pasek miasta, pusty na starcie, filtruje serwis
  5. sygnatura: zdania jako interfejs
  6. treść zdań ściśle ze źródła; cieplejsze propozycje osobno, DO POTWIERDZENIA
  7. ruch: jeden moment — wejście strony
  + numeracja 01–06 zdjęta: sześć sytuacji to nie sekwencja
"""
import json, os

OUT = "/Users/maksymzabavchuk/Desktop/rehamedica-projekt/site-psycho"
IC = json.load(open(os.path.join(OUT, "assets/icons-psycho.json"), encoding="utf-8"))["icons"]

# ── ZDANIA — każde z przypisem, z czego w źródle wynika ────────────────────
# Parafraza formy w ramach zgody P3. Żaden fakt nie dołożony.
SYT = [
 dict(ic="p-kryzys", cel="poradnia-psychologiczna", usluga="Poradnia psychologiczna",
      zdanie="Masz za sobą trudną sytuację — w domu, w pracy, albo straciłeś kogoś bliskiego.",
      proza="masz za sobą trudną sytuację w domu albo w pracy, albo straciłeś kogoś bliskiego",
      zrodlo="Poradnia: „kryzysu emocjonalnego spowodowanego sytuacją osobistą lub zawodową, "
             "problemami rodzinnymi czy utratą osoby bliskiej”"),
 dict(ic="p-napiecie", cel="konsultacje-psychologiczne", usluga="Konsultacje psychologiczne",
      zdanie="Czasem trudno powiedzieć, skąd biorą się Twoje trudności.",
      proza="trudno powiedzieć, skąd biorą się Twoje trudności",
      zrodlo="Konsultacje: „Czasami możesz mieć problem z określeniem źródła czy natury "
             "Twoich trudności” — niemal dosłownie, źródło już mówi na Ty"),
 dict(ic="p-emocje", cel="lekarz-psychiatra", usluga="Lekarz psychiatra",
      zdanie="Nastrój, lęk, apatia albo złość, nad którą nie panujesz.",
      proza="dokucza nastrój, lęk, apatia albo złość, nad którą nie panujesz",
      zrodlo="Psychiatra: „Zaburzenia nastroju, smutek, niekontrolowane napady agresji, "
             "apatia […] napady lęku”"),
 dict(ic="p-relacje", cel="poradnia-psychologiczna", usluga="Poradnia psychologiczna",
      zdanie="Coś nie działa w Twojej rodzinie, w związku albo z dzieckiem.",
      proza="coś nie działa w Twojej rodzinie, w związku albo z dzieckiem",
      zrodlo="Poradnia: „dla osób dorosłych, młodzieży, dzieci, rodzin oraz par” + "
             "„porady […] dla rodziców dzieci sprawiających trudności wychowawcze”"),
 dict(ic="p-zrozumienie", cel="konsultacja-psychoterapeutyczna", usluga="Konsultacja psychoterapeutyczna",
      zdanie="Chcesz zrozumieć, co się z Tobą dzieje, i coś z tym zrobić.",
      proza="chcesz zrozumieć, co się z Tobą dzieje, i coś z tym zrobić",
      zrodlo="Konsultacja psychoter.: „rozpoznanie potrzeb pacjenta i zrozumienie natury "
             "zgłaszanych problemów” + „określają cele i oczekiwania”"),
 dict(ic="p-jakosc-zycia", cel="poradnia-psychologiczna", usluga="Poradnia psychologiczna",
      zdanie="Po udarze albo urazie mózgu trudniej Ci się skupić i zapamiętać.",
      proza="po udarze albo urazie mózgu trudniej Ci się skupić i zapamiętać",
      zrodlo="Poradnia: „deficytami poznawczo-emocjonalnymi powstałymi w następstwie "
             "przebytych udarów mózgu, urazów mózgowych” + „funkcji mnestycznych”"),
]

# ── TEZA ───────────────────────────────────────────────────────────────────
# Wierne streszczenie: źródło mówi, że możesz nie umieć nazwać trudności,
# i że to nie problem — specjalista pomoże Ci to określić.
TEZA_1 = "Nie musisz wiedzieć, od czego zacząć."
TEZA_2 = "Powiedz, co się dzieje. Resztę ustalimy razem."

MIASTA = [("szczecinek","Szczecinek"),("szczecin","Szczecin"),("walcz","Wałcz"),
          ("bialogard","Białogard"),("bobolice","Bobolice")]

# usługa → miasta potwierdzone w źródle (matryca z Etapu 3)
DOSTEPNOSC = {
 "poradnia-psychologiczna":        ["szczecinek","szczecin","walcz","bialogard","bobolice"],
 "konsultacje-psychologiczne":     ["szczecinek"],
 "lekarz-psychiatra":              [],   # źródło nie wskazuje miasta
 "konsultacja-psychoterapeutyczna":[],   # źródło nie wskazuje miasta
}

def sym(ids):
    return "\n".join(f'<symbol id="{i}" viewBox="0 0 200 200">{IC[i]}</symbol>' for i in ids)

def ico(i, cls="pico"):
    return f'<svg class="{cls}" viewBox="0 0 200 200" aria-hidden="true"><use href="#{i}"></use></svg>'

def poz(s, wariant):
    """Jedna sytuacja. Markup różni się między wariantami — to jest sedno testu."""
    miasta = " ".join(DOSTEPNOSC[s["cel"]])
    common = f'href="../{s["cel"]}/" data-fac="{miasta}" title="{s["zrodlo"]}"'
    if wariant == 1:
        return f'''<a class="v1__row" {common}>
          {ico(s["ic"], "pico v1__ico")}
          <span class="v1__zd">{s["zdanie"]}</span>
          <span class="v1__do">{s["usluga"]}</span>
          <span class="v1__arw" aria-hidden="true">&rarr;</span>
        </a>'''
    if wariant == 2:
        return f'''<a class="v2__row" {common}>
          <span class="v2__mark" aria-hidden="true"></span>
          <span class="v2__zd">{s["zdanie"]}</span>
          <span class="v2__do">{s["usluga"]}</span>
        </a>'''
    return f'<a class="v3__zd" {common}>{s["proza"]}</a>'

MIASTA_HTML = "\n".join(
    f'<button type="button" class="cb__opt" data-city="{k}" aria-pressed="false">{n}</button>'
    for k, n in MIASTA)

def wariant(n):
    if n == 1:
        return f'''<section class="v1" aria-labelledby="teza">
  <div class="pwrap">
    <h1 class="teza" id="teza"><span class="teza__a">{TEZA_1}</span><span class="teza__b">{TEZA_2}</span></h1>
    <div class="v1__list">
      {"".join(poz(s,1) for s in SYT)}
    </div>
    <p class="pomoc">Albo od razu <a href="../kontakt/">zadzwoń do recepcji</a> — nie trzeba wiedzieć, o co poprosić.</p>
  </div>
</section>'''
    if n == 2:
        return f'''<section class="v2" aria-labelledby="teza">
  <div class="pwrap v2__grid">
    <div class="v2__col">
      <h1 class="teza" id="teza"><span class="teza__a">{TEZA_1}</span><span class="teza__b">{TEZA_2}</span></h1>
      <div class="v2__list">
        {"".join(poz(s,2) for s in SYT)}
      </div>
      <p class="pomoc">Albo od razu <a href="../kontakt/">zadzwoń do recepcji</a>.</p>
    </div>
  </div>
</section>'''
    return f'''<section class="v3" aria-labelledby="teza">
  <div class="pwrap">
    <h1 class="teza teza--v3" id="teza"><span class="teza__a">{TEZA_1}</span></h1>
    <p class="v3__proza">
      {TEZA_2} Przychodzisz, kiedy {poz(SYT[0],3)}.
      Kiedy {poz(SYT[1],3)}.
      Kiedy {poz(SYT[2],3)}.
      Kiedy {poz(SYT[3],3)}.
      Kiedy {poz(SYT[4],3)}.
      Albo kiedy {poz(SYT[5],3)}.
    </p>
    <p class="pomoc">Kliknij to zdanie, które jest prawdziwe. Albo <a href="../kontakt/">zadzwoń</a>.</p>
  </div>
</section>'''

CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "prototyp.css"), encoding="utf-8").read()

html = f'''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PROTOTYP — kierunek strony głównej · Reha Medica Psychoterapia</title>
<meta name="robots" content="noindex,nofollow">
<link rel="icon" href="../assets/favicon.png">
<link rel="preload" href="../assets/fonts/literata-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="../assets/fonts/worksans-latin.woff2" as="font" type="font/woff2" crossorigin>
<!-- style.css TYLKO dla @font-face i tokenów :root — zero klas układu -->
<link rel="stylesheet" href="../css/style.css?v=2">
<style>{CSS}</style>
</head>
<body>
<svg class="sprite" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"><defs>
{sym([s["ic"] for s in SYT])}
</defs></svg>

<a class="skip" href="#main">Przejdź do treści</a>

<div class="chrome">
<header class="ph">
  <a class="ph__logo" href="../"><img src="../assets/logo-brand.svg" alt="Reha Medica Psychoterapia" width="58" height="68"></a>
  <nav class="ph__nav" aria-label="Nawigacja">
    <a href="../poradnia-psychologiczna/">Zakres pomocy</a>
    <a href="../placowki/">Placówki</a>
    <a href="../kontakt/">Kontakt</a>
  </nav>
</header>

<div class="cb" role="group" aria-label="Wybierz miasto">
  <span class="cb__q">Gdzie szukasz pomocy?</span>
  <div class="cb__opts">{MIASTA_HTML}</div>
  <button type="button" class="cb__clear" hidden>zmień</button>
  <span class="cb__tel"><small data-tel-label>Centrala</small><a href="tel:+48943721451" data-tel>94 372 14 51</a></span>
</div>
</div>

<main id="main">
__WARIANT__
</main>

<footer class="pf">
  <p>Reha Medica — opieka psychologiczna, psychoterapeutyczna i psychiatryczna.</p>
  <p class="pf__proto">PROTOTYP · do wyrzucenia po wyborze kierunku</p>
</footer>

<nav class="switch" aria-label="Przełącz wariant">
  <span class="switch__l">Wariant</span>
  <a href="?v=1" data-v="1"><b>1</b> Lista</a>
  <a href="?v=2" data-v="2"><b>2</b> Rozmowa</a>
  <a href="?v=3" data-v="3"><b>3</b> Proza</a>
</nav>

<script>
(function(){{
  var v = new URLSearchParams(location.search).get('v') || '1';
  if (!['1','2','3'].includes(v)) v = '1';
  document.body.setAttribute('data-v', v);
  document.querySelectorAll('.switch a').forEach(function(a){{
    if (a.dataset.v === v) a.setAttribute('aria-current','true');
  }});

  // wejście strony — jedyny ruch na stronie (ustalenie 7)
  if (!matchMedia('(prefers-reduced-motion: reduce)').matches)
    requestAnimationFrame(function(){{ document.body.classList.add('in'); }});
  else document.body.classList.add('in');

  // pasek miasta: nic nie jest zaznaczone na starcie (reguła CLAUDE.md)
  var TEL = {{szczecinek:['94 372 14 51','+48943721451'], szczecin:['530 661 982','+48530661982'],
              walcz:['530 661 982','+48530661982'], bialogard:['535 960 018','+48535960018'],
              bobolice:['530 645 059','+48530645059']}};
  var opts = document.querySelectorAll('.cb__opt'), clear = document.querySelector('.cb__clear');
  function apply(city){{
    document.body.setAttribute('data-city', city || '');
    opts.forEach(function(o){{ o.setAttribute('aria-pressed', String(o.dataset.city === city)); }});
    clear.hidden = !city;
    var t = document.querySelector('[data-tel]');
    var lab = document.querySelector('[data-tel-label]');
    var NAZWA = {{szczecinek:'Szczecinek',szczecin:'Szczecin',walcz:'Wałcz',bialogard:'Białogard',bobolice:'Bobolice'}};
    if (city && TEL[city]) {{ t.textContent = TEL[city][0]; t.href = 'tel:' + TEL[city][1]; lab.textContent = 'Recepcja ' + NAZWA[city]; }}
    else {{ t.textContent = '94 372 14 51'; t.href = 'tel:+48943721451'; lab.textContent = 'Centrala'; }}
    document.querySelectorAll('[data-fac]').forEach(function(el){{
      var lista = el.dataset.fac.split(' ').filter(Boolean);
      // brak potwierdzonego miasta = nie ukrywamy, ale oznaczamy „zapytaj recepcję”
      var stan = !city ? '' : (lista.length === 0 ? 'ask' : (lista.includes(city) ? 'yes' : 'no'));
      el.setAttribute('data-avail', stan);
    }});
  }}
  opts.forEach(function(o){{ o.addEventListener('click', function(){{
    apply(o.getAttribute('aria-pressed') === 'true' ? '' : o.dataset.city); }}); }});
  clear.addEventListener('click', function(){{ apply(''); }});
}})();
</script>
</body>
</html>
'''

os.makedirs(os.path.join(OUT, "prototyp"), exist_ok=True)
strona = html.replace("__WARIANT__", "\n".join(wariant(n) for n in (1, 2, 3)))
open(os.path.join(OUT, "prototyp/index.html"), "w", encoding="utf-8").write(strona)
print("prototyp/index.html — 3 warianty, przełącznik ?v=1|2|3")
print(f"  zdań: {len(SYT)} · każde z przypisem źródłowym w atrybucie title")
