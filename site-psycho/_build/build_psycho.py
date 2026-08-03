# -*- coding: utf-8 -*-
"""Generator serwisu Reha Medica Psychoterapia."""
import os, json, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_psycho_data import *

OUT = "/Users/maksymzabavchuk/Desktop/rehamedica-projekt/site-psycho"
V = "2"

def rel(d):  return "../" * d
def slug_city(c): return c

# ── ikony z projektu Claude Design „Ikony Psychoterapia v4" (patrz extract_icons.py)
_IC = json.load(open(os.path.join(OUT, "assets/icons-psycho.json"), encoding="utf-8"))
ICONS, ICON_LABELS = _IC["icons"], _IC["labels"]

ICON_FOR_SERVICE = {
    "poradnia-psychologiczna":                    "p-poradnia",
    "osrodek-psychologiczno-psychoterapeutyczny": "p-osrodek",
    "konsultacje-psychologiczne":                 "p-konsultacje",
    "konsultacja-psychoterapeutyczna":            "p-psychoterapeutyczna",
    "lekarz-psychiatra":                          "p-psychiatra",
}

# sekcja „W jakich momentach psychoterapia może pomóc" — etykiety z projektu klienta,
# kierowanie do usług wyłącznie tam, gdzie uzasadnia je treść źródłowa
MOMENTS = [
    ("p-kryzys",       "poradnia-psychologiczna",         "Poradnia psychologiczna"),
    ("p-napiecie",     "konsultacje-psychologiczne",      "Konsultacje psychologiczne"),
    ("p-emocje",       "lekarz-psychiatra",               "Lekarz psychiatra"),
    ("p-relacje",      "poradnia-psychologiczna",         "Poradnia psychologiczna"),
    ("p-zrozumienie",  "konsultacja-psychoterapeutyczna", "Konsultacja psychoterapeutyczna"),
    ("p-jakosc-zycia", "poradnia-psychologiczna",         "Poradnia psychologiczna"),
]

def psymbols(ids):
    """Symbole ikon do wstrzyknięcia w <defs> sprite'a — tylko te, których strona używa."""
    out = []
    for i in ids:
        out.append(f'    <symbol id="{i}" viewBox="0 0 200 200">\n      {ICONS[i]}\n    </symbol>')
    return "\n".join(out)

def picon(icon_id, cls="picon picon--lg"):
    return (f'<svg class="{cls}" viewBox="0 0 200 200" aria-hidden="true" focusable="false">'
            f'<use href="#{icon_id}"></use></svg>')

# ─────────────────────────────────────────── sprite (1:1 z serwisu głównego)
SPRITE = """<svg class="icon-sprite" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <symbol id="i-phone" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
      <path d="M6.6 3.5h3l1.5 3.8-1.9 1.1a11 11 0 0 0 5.4 5.4l1.1-1.9 3.8 1.5v3a1.6 1.6 0 0 1-1.7 1.6A15.9 15.9 0 0 1 5 5.2 1.6 1.6 0 0 1 6.6 3.5Z"/>
    </symbol>
    <symbol id="i-pin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 21s6.5-6 6.5-11a6.5 6.5 0 1 0-13 0C5.5 15 12 21 12 21Z"/><circle cx="12" cy="10" r="2.4"/>
    </symbol>
    <symbol id="i-clock" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="8.5"/><path d="M12 7v5.2l3.2 2"/>
    </symbol>
    <symbol id="i-mail" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
      <rect x="3" y="5.5" width="18" height="13" rx="1.6"/><path d="m3.6 6.6 8.4 6 8.4-6"/>
    </symbol>
    <symbol id="i-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="m5 9 7 7 7-7"/>
    </symbol>
    <symbol id="i-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M6 6l12 12M18 6L6 18"/>
    </symbol>
    <symbol id="i-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="10.8" cy="10.8" r="6.3"/><path d="m15.4 15.4 4.1 4.1"/>
    </symbol>
    <symbol id="i-external" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M14 4.5h5.5V10M19.5 4.5 11 13"/><path d="M18 14.4v4.1a1.6 1.6 0 0 1-1.6 1.6H5.5a1.6 1.6 0 0 1-1.6-1.6V7.6A1.6 1.6 0 0 1 5.5 6h4.1"/>
    </symbol>
    <symbol id="i-nav" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
      <path d="M3.4 11.2 21 3l-8.2 17.6-2-7.4-7.4-2Z"/>
    </symbol>
    <symbol id="i-facebook" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
      <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>
    </symbol>
    <symbol id="i-instagram" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
      <rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="3.8"/><circle cx="16.9" cy="7.1" r="1.1" fill="currentColor" stroke="none"/>
    </symbol>
  </defs>
</svg>"""

def sprite(extra=()):
    """Sprite UI + tylko te ikony psychoterapeutyczne, których dana strona faktycznie używa."""
    if not extra:
        return SPRITE
    return SPRITE.replace("  </defs>", psymbols(extra) + "\n  </defs>")

A11Y_HTML = open("/Users/maksymzabavchuk/Desktop/rehamedica-projekt/site/index.html", encoding="utf-8").read()
A11Y_HTML = A11Y_HTML[A11Y_HTML.index('<button class="a11y-fab"'):A11Y_HTML.index('<script src="js/main.js')]

# ─────────────────────────────────────────── head
def head(depth, title, desc, path, img="og-psychoterapia.jpg", robots=None,
         extra_ld=None, preload_hero=False, usluga_css=True):
    r = rel(depth)
    url = BASE + "/" + path
    o = []
    o.append('<!DOCTYPE html>\n<html lang="pl">\n<head>')
    o.append('<meta charset="UTF-8">')
    o.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    o.append('')
    o.append(f'<title>{title}</title>')
    o.append(f'<meta name="description" content="{desc}">')
    if robots: o.append(f'<meta name="robots" content="{robots}">')
    o.append(f'<link rel="canonical" href="{url}">')
    o.append('')
    o.append('<meta property="og:type" content="website">')
    o.append('<meta property="og:locale" content="pl_PL">')
    o.append('<meta property="og:site_name" content="Reha Medica Psychoterapia">')
    o.append(f'<meta property="og:url" content="{url}">')
    o.append(f'<meta property="og:title" content="{title}">')
    o.append(f'<meta property="og:description" content="{desc}">')
    o.append(f'<meta property="og:image" content="{BASE}/assets/img/{img}">')
    o.append('<meta property="og:image:width" content="1200">')
    o.append('<meta property="og:image:height" content="630">')
    o.append('<meta name="twitter:card" content="summary_large_image">')
    o.append('')
    o.append('<meta name="theme-color" content="#483d32">')
    o.append(f'<link rel="icon" href="{r}assets/favicon.png">')
    o.append(f'<link rel="preload" href="{r}assets/fonts/instrumentserif-latin.woff2" as="font" type="font/woff2" crossorigin>')
    o.append(f'<link rel="preload" href="{r}assets/fonts/sourcesans3-latin.woff2" as="font" type="font/woff2" crossorigin>')
    if preload_hero:
        # pierwsze zdjęcie hero — to, które widać przed jakąkolwiek interakcją.
        # imagesrcset/imagesizes muszą powtarzać atrybuty <img>, inaczej
        # przeglądarka pobierze dwa różne pliki: jeden z preloadu, drugi z DOM.
        o.append(f'<link rel="preload" as="image" href="{r}assets/img/hw-kryzys.webp"'
                 f' imagesrcset="{r}assets/img/hw-kryzys-s.webp 960w, {r}assets/img/hw-kryzys.webp 1707w"'
                 f' imagesizes="100vw" fetchpriority="high">')
    o.append(f'<link rel="stylesheet" href="{r}css/style.css?v={V}">')
    if usluga_css:
        o.append(f'<link rel="stylesheet" href="{r}css/usluga.css?v={V}">')
    o.append(f'<link rel="stylesheet" href="{r}css/psycho.css?v={V}">')
    o.append("<script>document.documentElement.className+=' js';</script>")
    o.append('')
    o.append("<script>(function(){try{var s=JSON.parse(localStorage.getItem('rm-a11y')||'{}'),h=document.documentElement;if(s.scale&&s.scale!==100)h.style.fontSize=s.scale+'%';if(s.space)h.setAttribute('data-a11y-space',s.space);if(s.lineh)h.setAttribute('data-a11y-lineh',s.lineh);['contrast','invert','gray','underline','cursor','font','hideimg','guide','reduce'].forEach(function(k){if(s[k])h.setAttribute('data-a11y-'+k,'');});if((s.scale&&s.scale>100)||s.font)h.setAttribute('data-a11y-compact','');}catch(e){}})();</script>")
    if extra_ld:
        for block in extra_ld:
            o.append('\n<script type="application/ld+json">')
            o.append(json.dumps(block, ensure_ascii=False, indent=2))
            o.append('</script>')
    o.append('</head>')
    return "\n".join(o)

# ─────────────────────────────────────────── header
def header(depth, active=None):
    r = rel(depth)
    home = r + "index.html" if depth else "./"
    def sub_uslugi():
        li = []
        for s in SERVICE_ORDER:
            cur = ' aria-current="page"' if active == s else ''
            li.append(f'            <li><a href="{r}{s}/"{cur}>{SERVICES[s]["title"]}</a></li>')
        return "\n".join(li)
    def sub_place():
        li = []
        for c in CITIES:
            cur = ' aria-current="page"' if active == "city:" + c else ''
            li.append(f'            <li><a href="{r}{c}/"{cur}>{FAC[c]["name"]}</a></li>')
        return "\n".join(li)
    cur_kontakt = ' aria-current="page"' if active == "kontakt" else ''
    cur_akt = ' aria-current="page"' if active == "aktualnosci" else ''
    cur_faq = ' aria-current="page"' if active == "faq" else ''
    return f"""<header class="site-header" id="site-header">
  <div class="topstrip">
    <div class="wrap topstrip__inner">
      <span class="topstrip__item"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-pin"></use></svg>Opieka psychologiczna w pięciu placówkach na Pomorzu Zachodnim</span>
      <span class="topstrip__sep" aria-hidden="true"></span>
      <span class="topstrip__item"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-clock"></use></svg>pon.–pt. 8:00–19:00 · sob. 8:00–18:00</span>
    </div>
  </div>
  <div class="wrap headerbar">
    <a class="header-call" href="tel:+48943721451" aria-label="Zadzwoń: 94 372 14 51"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-phone"></use></svg></a>
    <a class="logo" href="{home}" aria-label="Reha Medica Psychoterapia — strona główna">
      <img class="logo__full" src="{r}assets/logo.svg" alt="Reha Medica Psychoterapia" width="70" height="82">
      <span class="logo__compact" aria-hidden="true">
        <img class="logo__mark" src="{r}assets/logo-mark.svg" alt="" width="30" height="27">
        <span class="logo__name">Reha<br>Medica</span>
      </span>
    </a>
    <span class="headerbar__rule" aria-hidden="true"></span>
    <nav class="nav" id="nav" aria-label="Nawigacja główna">
      <button type="button" class="nav__close" data-nav-close aria-label="Zamknij menu"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-close"></use></svg></button>
      <ul>
        <li class="nav__item nav__item--sub">
          <button type="button" class="nav__top" aria-expanded="false" aria-controls="sub-uslugi">Zakres pomocy<svg class="ico nav__chev" aria-hidden="true" focusable="false"><use href="#i-chevron"></use></svg></button>
          <ul class="nav__sub" id="sub-uslugi">
{sub_uslugi()}
          </ul>
        </li>
        <li class="nav__item nav__item--sub">
          <button type="button" class="nav__top" aria-expanded="false" aria-controls="sub-placowki">Placówki<svg class="ico nav__chev" aria-hidden="true" focusable="false"><use href="#i-chevron"></use></svg></button>
          <ul class="nav__sub" id="sub-placowki">
{sub_place()}
          </ul>
        </li>
        <li class="nav__item"><a href="{r}aktualnosci/"{cur_akt}>Aktualności</a></li>
        <li class="nav__item"><a href="{r}faq/"{cur_faq}>FAQ</a></li>
        <li class="nav__item"><a href="{r}kontakt/"{cur_kontakt}>Kontakt</a></li>
      </ul>
      <form class="nav-search" role="search" aria-label="Szukaj w serwisie">
        <svg class="ico nav-search__ico" aria-hidden="true" focusable="false"><use href="#i-search"></use></svg>
        <input type="search" id="svc-search" aria-label="Szukaj usługi" placeholder="Szukaj — np. poradnia, psychiatra, dzieci…" autocomplete="off">
        <button type="button" class="nav-search__close" data-search-close aria-label="Zamknij wyszukiwarkę"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-close"></use></svg></button>
      </form>
      <div class="nav__mobile">
        <a class="btn btn--cream" href="{home}#placowki">Wybierz placówkę <span class="btn__arrow" aria-hidden="true">→</span></a>
        <a class="phone-link" href="tel:+48943721451">Infolinia: 94 372 14 51</a>
        <a class="nav__beauty" href="{MAIN}" rel="noopener" target="_blank">Reha Medica — rehabilitacja <svg class="ico" aria-hidden="true" focusable="false"><use href="#i-external"></use></svg></a>
      </div>
    </nav>
    <div class="headerbar__cta">
      <a class="btn btn--sm btn--outline-light header-phone" href="{MAIN}" rel="noopener" target="_blank" aria-label="Reha Medica — serwis rehabilitacji i fizjoterapii (otwiera się w nowej karcie)">Rehabilitacja <svg class="ico" aria-hidden="true" focusable="false"><use href="#i-external"></use></svg></a>
      <a class="btn btn--cream btn--sm" href="{home}#placowki" data-booking>Umów wizytę <span class="btn__arrow" aria-hidden="true">→</span></a>
      <button type="button" class="icon-btn" data-search-open aria-label="Szukaj w serwisie"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-search"></use></svg></button>
    </div>
    <button class="burger" aria-label="Otwórz menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
  </div>
</header>"""

# ─────────────────────────────────────────── footer
def footer(depth):
    r = rel(depth)
    home = r + "index.html" if depth else "./"
    usl = "\n".join(f'        <li><a href="{r}{s}/">{SERVICES[s]["title"]}</a></li>' for s in SERVICE_ORDER)
    pla = "\n".join(f'        <li><a href="{r}{c}/">{FAC[c]["name"]}</a></li>' for c in CITIES)
    return f"""<footer class="site-footer" id="kontakt">
  <div class="wrap footer__top">
    <div class="footer__brand">
      <img src="{r}assets/logo.svg" alt="Reha Medica Psychoterapia" width="72" height="84">
      <p class="footer__desc">Opieka psychologiczna, psychoterapeutyczna i psychiatryczna w placówkach Reha Medica na Pomorzu Zachodnim.</p>
      <a class="footer__call" href="tel:+48943721451"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-phone"></use></svg> 94 372 14 51</a>
      <div class="footer__social"><a href="https://www.facebook.com/rehamedicaszczecinek/" target="_blank" rel="noopener" aria-label="Reha Medica na Facebooku"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-facebook"></use></svg></a><a href="https://www.instagram.com/reha.medica_szczecinek/" target="_blank" rel="noopener" aria-label="Reha Medica na Instagramie"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-instagram"></use></svg></a></div>
    </div>
    <nav class="footer__nav" aria-label="Usługi">
      <h2 class="footer__h">Usługi</h2>
      <ul>
{usl}
      </ul>
    </nav>
    <nav class="footer__nav" aria-label="Placówki">
      <h2 class="footer__h">Placówki</h2>
      <ul>
{pla}
      </ul>
    </nav>
    <nav class="footer__nav" aria-label="Kontakt i informacje">
      <h2 class="footer__h">Kontakt i informacje</h2>
      <ul>
        <li><a href="{home}#placowki">Wybierz placówkę</a></li>
        <li><a href="{r}kontakt/">Kontakt</a></li>
        <li><a href="{r}aktualnosci/">Aktualności</a></li>
        <li><a href="{r}faq/">FAQ</a></li>
        <li><a href="{r}placowki/">Wszystkie placówki</a></li>
        <li><a href="{MAIN}/ankieta-satysfakcji/" rel="noopener">Ankieta satysfakcji ↗</a></li>
        <li><a href="{MAIN}" rel="noopener" target="_blank">Reha Medica — rehabilitacja ↗</a></li>
        <li><a href="https://rehabeauty.pl" rel="noopener" target="_blank">Reha Beauty — odnowa biologiczna ↗</a></li>
      </ul>
    </nav>
  </div>

  <div class="wrap footer__bottom">
    <p class="footer__copy">© 2026 Reha Medica. Wszelkie prawa zastrzeżone.</p>
    <p class="footer__by">Realizacja: <a href="https://codingmaks.com" target="_blank" rel="noopener">codingmaks.com</a></p>
    <nav class="footer__legal" aria-label="Informacje prawne">
      <a href="{MAIN}/polityka-prywatnosci/" rel="noopener">Polityka prywatności</a>
      <a href="{MAIN}/standardy-ochrony-dzieci/" rel="noopener">Standardy ochrony małoletnich</a>
    </nav>
  </div>
</footer>"""

def tail(depth, bk_places=None, bk_service=None):
    r = rel(depth)
    bk = ""
    if bk_places is not None:
        bk = f"""
<div class="bk" id="bk" hidden data-bk-places="{bk_places}" data-bk-service="{bk_service or ''}">
  <div class="bk__veil" data-bk-close aria-hidden="true"></div>
  <div class="bk__panel" role="dialog" aria-modal="true" aria-labelledby="bk-title">
    <div class="bk__head">
      <p class="bk__title" id="bk-title">Wybierz placówkę</p>
      <button class="bk__x" type="button" data-bk-close aria-label="Zamknij">
        <svg class="ico" aria-hidden="true" focusable="false"><use href="#i-close"></use></svg>
      </button>
    </div>
    <ul class="bk__list" data-bk-list></ul>
  </div>
</div>
"""
    return f"""
<a class="dogear" href="{MAIN}/ankieta-satysfakcji/" rel="noopener" aria-label="Wypełnij ankietę satysfakcji pacjenta">
  <span class="dogear__fold" aria-hidden="true"></span>
  <span class="dogear__label">Ankieta<br>satysfakcji</span>
</a>

<a class="callfab" href="tel:+48943721451" aria-label="Zadzwoń do Reha Medica: 94 372 14 51">
  <svg class="ico" aria-hidden="true" focusable="false"><use href="#i-phone"></use></svg>
</a>
{bk}
{A11Y_HTML}<script src="{r}js/main.js?v={V}"></script>
</body>
</html>
"""

# ─────────────────────────────────────────── schema helpers
def clinic_ld(c, url, name_suffix=""):
    f = FAC[c]
    d = {
        "@type": "MedicalClinic",
        "@id": f"{BASE}/#{c}",
        "name": f"Reha Medica {f['name']}" + name_suffix,
        "url": url,
        "medicalSpecialty": "Psychiatric",
        "parentOrganization": {"@id": f"{BASE}/#organizacja"},
        "address": {
            "@type": "PostalAddress", "streetAddress": f["addr"], "postalCode": f["zip"],
            "addressLocality": f["name"], "addressRegion": "zachodniopomorskie", "addressCountry": "PL",
        },
        "telephone": f["phones"][0][1],
        "email": f["email"],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification",
             "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
             "opens": "08:00", "closes": "19:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday",
             "opens": "08:00", "closes": "18:00"},
        ],
    }
    if f["geo"]:
        d["geo"] = {"@type": "GeoCoordinates", "latitude": f["geo"][0], "longitude": f["geo"][1]}
        d["hasMap"] = f"https://www.google.com/maps/search/?api=1&query={f['geo'][0]},{f['geo'][1]}"
    return d

def breadcrumb_ld(items):
    el = []
    for i, (name, url) in enumerate(items, 1):
        d = {"@type": "ListItem", "position": i, "name": name}
        if url: d["item"] = url
        el.append(d)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": el}

# ─────────────────────────────────────────── bloki treści
def pcard(c, depth, service_label):
    f = FAC[c]
    r = rel(depth)
    phones = "".join(
        f'<a class="pcard__row" href="tel:{tel}"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-phone"></use></svg><span>{txt}</span></a>\n          '
        for txt, tel in f["phones"])
    return f"""        <article class="pcard">
          <p class="pcard__city">{f['name']}</p>
          <p class="pcard__row"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-pin"></use></svg><span>{f['addr']}, {f['zip']} {f['name']}</span></p>
          {phones}<a class="pcard__row" href="mailto:{f['email']}"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-mail"></use></svg><span>{f['email']}</span></a>
          <div class="pcard__cta"><a class="btn btn--brand" href="tel:{f['phones'][0][1]}">Umów wizytę <span class="btn__arrow" aria-hidden="true">→</span></a></div>
        </article>"""

def prose_block(cnt, img_src, img_alt, depth):
    """lintro / lpull / lparts / lcoda — układ z serwisu głównego."""
    o = []
    o.append('      <div class="lintro__open">')
    o.append('        <div class="lintro__head">')
    o.append(f'          <p class="lkick">{cnt.get("kicker","Dla kogo")}</p>')
    o.append(f'          <p class="lintro__lead">{cnt["lead"]}</p>')
    if cnt.get("_kogo"):
        # Odbiorcy jako etykiety, nie jako wyliczenie wewnątrz zdania.
        # Wzorzec „Kogo wspieramy" z Centrum Sobota: pacjent ma w sekundę
        # sprawdzić, czy jest na właściwej stronie.
        # WEWNĄTRZ .lintro__head — siatka ma obszary "lead kadr"/"body kadr",
        # więc dziecko bez przypisanego obszaru spadało pod całą prozę.
        chip = "".join(f'<li class="kogo__i">{t}</li>' for t, _ in cnt["_kogo"])
        o.append('          <ul class="kogo" aria-label="Dla kogo jest ta pomoc">' + chip + '</ul>')
    o.append('        </div>')
    if img_src:
        o.append('        <figure class="lintro__fig">')
        o.append(f'          <img width="1200" height="800" src="{img_src}" alt="{img_alt}" loading="lazy" decoding="async">')
        o.append('        </figure>')
    o.append('        <div class="lintro__body">')
    for p in cnt["body"]:
        o.append(f'          <p class="lintro__p">{p}</p>')
    o.append('        </div>')
    o.append('      </div>')
    if cnt.get("pull_q"):
        o.append('\n      <div class="lpull">')
        o.append(f'        <p class="lpull__q">{cnt["pull_q"]}</p>')
        o.append('        <div>')
        for p in cnt.get("pull_p") or []:
            o.append(f'          <p class="lpull__p">{p}</p>')
        o.append('        </div>')
        o.append('      </div>')
    if cnt.get("_ilustracja"):
        # Kotwica wizualna przy najgęstszym bloku strony. Dwie maski —
        # osobno kreska, osobno plama — więc obie warstwy biorą kolor z CSS
        # i grafika reaguje na motyw sekcji tak samo jak ikony.
        ik, alt = cnt["_ilustracja"]
        r = rel(depth)
        o.append(f'\n      <figure class="pil" role="img" aria-label="{alt}">')
        o.append(f'        <span class="pil__w" style="--plama:url({r}assets/ikony/{ik}-plama.png);'
                 f'--linie:url({r}assets/ikony/{ik}.png)"></span>')
        o.append('      </figure>')
    if cnt.get("parts_h"):
        # Akordeon zamiast gęstych akapitów klinicznych. Każdy zaczyna się od
        # <b>Nazwa</b> — nazwa zostaje widoczna i skanowalna, definicja otwiera
        # się na żądanie. Kto szuka „czy robicie diagnozę neuro", znajduje
        # odpowiedź od razu; kto chce szczegółu, klika.
        # Bez JS — <details> działa przy wyłączonym skrypcie i przy druku.
        import re as _re
        o.append('\n      <div class="lparts">')
        o.append(f'        <h2 class="lparts__h">{cnt["parts_h"]}</h2>')
        o.append('        <div class="lparts__akord">')
        for n, tekst in enumerate(cnt.get("parts") or []):
            m = _re.match(r'\s*<b>(.*?)</b>\s*(.*)$', tekst, _re.S)
            if m:
                tytul, reszta = m.group(1), m.group(2).lstrip(" —–-")
                # Tekst źródłowy jest ciągiem dalszym nazwy („Diagnoza … obejmuje
                # pełną ocenę"). Po wyniesieniu nazwy do nagłówka trzeba go
                # domknąć gramatycznie: spójka „to" traci podmiot, więc znika,
                # a zdanie zaczyna się wielką literą. Znaczenie bez zmian.
                if reszta.lower().startswith("to "):
                    reszta = reszta[3:]
                reszta = reszta[:1].upper() + reszta[1:] if reszta else reszta
            else:
                tytul, reszta = cnt["parts_h"], tekst
            o.append(f'          <details class="lpart"{" open" if n == 0 else ""}>')
            o.append(f'            <summary class="lpart__s">{tytul}</summary>')
            o.append(f'            <div class="lpart__b"><p>{reszta}</p></div>')
            o.append('          </details>')
        o.append('        </div>')
        o.append('      </div>')
    if cnt.get("coda_lead"):
        o.append('\n      <div class="lcoda">')
        o.append('        <div class="lcoda__inner">')
        o.append(f'          <p class="lcoda__lead">{cnt["coda_lead"]}</p>')
        if cnt.get("coda_p"):
            o.append(f'          <p class="lcoda__p">{cnt["coda_p"]}</p>')
        o.append('        </div>')
        o.append('      </div>')
    return "\n".join(o)

FIN_LABEL = {
    "bezpłatnie": '<span class="splate__nfz">Pomoc bezpłatna</span>',
    "komercyjnie": '<span class="splate__nfz">Wizyty komercyjne (odpłatne)</span>',
    "DO POTWIERDZENIA": '<span class="splate__nfz">Sposób finansowania — zapytaj w recepcji placówki</span>',
}

def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(content)
    return path
