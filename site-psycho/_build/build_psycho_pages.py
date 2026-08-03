# -*- coding: utf-8 -*-
"""Reha Medica Psychoterapia — budowa stron."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_psycho import *

BUILT = []

# zdjęcie reagujące na wskazane zdanie. 4 sceny stockowe + 2 autentyczne wnętrza —
# brakuje dwóch kadrów dla dorosłych, to jest luka do sesji zdjęciowej (P17).
FOTO = {
 "p-kryzys":       ("sy-kryzys.webp",      "Rozmowa w poradni psychologicznej"),
 "p-napiecie":     ("sy-napiecie.webp",    "Pierwsze spotkanie — nazywanie trudności"),
 "p-emocje":       ("sy-emocje.webp",      "Recepcja Reha Medica"),
 "p-relacje":      ("sy-relacje.webp",     "Konsultacja dla pary"),
 "p-zrozumienie":  ("sy-zrozumienie.webp", "Wsparcie grupowe"),
 "p-jakosc-zycia": ("sy-jakosc.webp",      "Wnętrze placówki Reha Medica"),
}
DOSTEPNOSC = {
 "poradnia-psychologiczna":        "szczecinek szczecin walcz bialogard bobolice",
 "konsultacje-psychologiczne":     "szczecinek",
 "lekarz-psychiatra":              "",
 "konsultacja-psychoterapeutyczna":"",
 "osrodek-psychologiczno-psychoterapeutyczny": "szczecinek szczecin walcz bialogard bobolice",
}
ZDANIA = {
 "kryzys":      "Masz za sobą trudną sytuację — w domu, w pracy, albo straciłeś kogoś bliskiego.",
 "napiecie":    "Czasem trudno powiedzieć, skąd biorą się Twoje trudności.",
 "emocje":      "Nastrój, lęk, apatia albo złość, nad którą nie panujesz.",
 "relacje":     "Coś nie działa w Twojej rodzinie, w związku albo z dzieckiem.",
 "zrozumienie": "Chcesz zrozumieć, co się z Tobą dzieje, i coś z tym zrobić.",
 "jakosc-zycia":"Po udarze albo urazie mózgu trudniej Ci się skupić i zapamiętać.",
}


# ══════════════════════════════════════════════ STRONA GŁÓWNA
def build_home():
    org = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "MedicalOrganization",
                "@id": f"{BASE}/#organizacja",
                "name": "Reha Medica Psychoterapia",
                "alternateName": "Reha Medica — opieka psychologiczna i psychoterapeutyczna",
                "url": BASE + "/",
                "logo": f"{BASE}/assets/logo.svg",
                "image": f"{BASE}/assets/img/og-psychoterapia.jpg",
                "description": "Opieka psychologiczna, psychoterapeutyczna i psychiatryczna Reha Medica w pięciu placówkach na Pomorzu Zachodnim.",
                "medicalSpecialty": "Psychiatric",
                "telephone": "+48943721451",
                "email": "szczecinek@rehamedica.info.pl",
                "parentOrganization": {"@type": "MedicalOrganization", "name": "Reha Medica", "url": MAIN + "/"},
                "department": [{"@id": f"{BASE}/#{c}"} for c in CITIES],
                "address": {"@type": "PostalAddress", "streetAddress": "ul. Kościuszki 57",
                            "postalCode": "78-400", "addressLocality": "Szczecinek",
                            "addressRegion": "zachodniopomorskie", "addressCountry": "PL"},
            }
        ] + [clinic_ld(c, f"{BASE}/{c}/") for c in CITIES],
    }

    tabs = "\n".join(
        f'          <button role="tab" type="button" data-fac="{c}" aria-selected="false" aria-controls="hcard-panel">{FAC[c]["name"]}</button>'
        for c in CITIES)


    # hero: sześć zdań jako router + zdjęcie, które na nie odpowiada
    citybar_opts = "\n".join(
        f'      <button type="button" class="citybar__opt" data-city="{c}" aria-pressed="false">{FAC[c]["name"]}</button>'
        for c in CITIES)
    hero_rows = "\n".join(
        f'        <li class="hero2__row" data-fac="{DOSTEPNOSC[MOMENT_SECTIONS[i]["target"]]}"'
        f' data-svc="{MOMENT_SECTIONS[i]["target_label"]}">'
        f'{picon(MOMENT_SECTIONS[i]["icon"], "picon hero2__ico")}'
        f'<span class="hero2__body">'
        f'<a class="hero2__zd" href="#{cid}">{ZDANIA[cid]}</a>'
        f'<span class="hero2__act" data-act aria-live="polite"></span>'
        f'</span>'
        f'<span class="hero2__arw" aria-hidden="true">&rarr;</span></li>'
        for i, cid in enumerate(c["id"] for c in MOMENT_SECTIONS))
    # siódma pozycja: kto się nie rozpozna w sześciu zdaniach, też musi mieć dokąd pójść
    hero_rows += (
        '\n        <li class="hero2__row hero2__row--else">'
        '<span class="hero2__ico" aria-hidden="true"></span>'
        '<span class="hero2__body">'
        '<a class="hero2__zd" href="kontakt/">Nic z tego nie pasuje.</a>'
        '<span class="hero2__act" data-act aria-live="polite"></span>'
        '</span>'
        '<span class="hero2__arw" aria-hidden="true">&rarr;</span></li>')
    hero_imgs = "\n".join(
        f'        <img class="hero2__img{" is-on" if i == 0 else ""}" src="assets/img/{FOTO[c["icon"]][0]}"'
        f' alt="" data-cap="{FOTO[c["icon"]][1]}" width="880" height="1100"'
        f' loading="{"eager" if i == 0 else "lazy"}" decoding="async">'
        for i, c in enumerate(MOMENT_SECTIONS))


    zakres_html = "\n".join(
        f'      <li class="zakres__i" data-fac="{DOSTEPNOSC.get(k,"")}">'
        f'<a class="zakres__a" href="{k}/">'
        f'{picon(ICON_FOR_SERVICE[k], "picon zakres__ico")}'
        f'<span class="zakres__b"><span class="zakres__t">{SERVICES[k]["title"]}</span>'
        f'<span class="zakres__d">{SERVICES[k]["lead"]}</span></span>'
        f'<span class="zakres__arw" aria-hidden="true">&rarr;</span></a></li>'
        for k in SERVICE_ORDER)
    faq_html = "\n".join(
        f"""      <details class="qa"{' open' if n == 0 else ''}>
        <summary class="qa__q">{f['q']}</summary>
        <div class="qa__a"><p>{f['a'][0]}</p></div>
      </details>""" for n, f in enumerate(FAQ))
    akt_html = "\n".join(
        f'      <li class="akt__i"><a class="akt__a" href="aktualnosci/{a["slug"]}/">'
        f'<span class="akt__meta">{a["kat"]} · <time datetime="{a["data"]}">{a["data_txt"]}</time></span>'
        f'<span class="akt__t">{a["t"]}</span></a></li>'
        for a in AKTUALNOSCI[:3])


    # hero pełnoekranowe: zdjęcia jako tło + dwa pola wyboru
    # Wymiary czytane z pliku — kadry mają różne rozdzielczości, bo każdy jest
    # cięty z natywnego oryginału i NIC nie jest powiększane. Sztywne
    # width/height 1900×1070 podawało przeglądarce nieprawdę i psuło proporcję.
    def _wym(p):
        import struct
        with open(p, "rb") as f:
            b = f.read(30)
        assert b[:4] == b"RIFF" and b[8:12] == b"WEBP", p
        if b[12:16] == b"VP8X":
            return (int.from_bytes(b[24:27], "little") + 1,
                    int.from_bytes(b[27:30], "little") + 1)
        if b[12:16] == b"VP8L":
            v = struct.unpack("<I", b[21:25])[0]
            return ((v & 0x3FFF) + 1, ((v >> 14) & 0x3FFF) + 1)
        return struct.unpack("<HH", b[26:30])          # VP8 (stratny)

    hero_imgs = []
    for n, c in enumerate(MOMENT_SECTIONS):
        w, h = _wym(f"{OUT}/assets/img/hw-{c['id']}.webp")
        hero_imgs.append(
            f'    <img class="hero3__img{" is-on" if n == 0 else ""}"'
            f' src="assets/img/hw-{c["id"]}.webp"'
            f' srcset="assets/img/hw-{c["id"]}-s.webp 960w, assets/img/hw-{c["id"]}.webp {w}w"'
            f' sizes="100vw" alt="" width="{w}" height="{h}"'
            f' loading="{"eager" if n == 0 else "lazy"}"'
            f' fetchpriority="{"high" if n == 0 else "auto"}" decoding="async">')
    hero_imgs = "\n".join(hero_imgs)
    # skala zjawiska — słupek rysowany jest CSS-em z --v, więc liczba i długość
    # kreski nie mogą się rozjechać: obie biorą się z tej samej wartości
    skala_html = "\n".join(
        f'      <li class="skala__i" style="--v:{d["v"]}" data-animate>\n'
        f'        <p class="skala__v"><b>{d["v"]}</b><span class="skala__jed">{d["jed"]}</span></p>\n'
        f'        <p class="skala__t">{d["t"]}</p>\n'
        f'        <span class="skala__bar" aria-hidden="true"><i></i></span>\n'
        f'        <p class="skala__pod">{d["pod"]}</p>\n'
        f'      </li>'
        for d in SKALA)
    szuk_syt = "\n".join(
        f'            <option value="{c["id"]}" data-cel="{c["target"]}" data-usluga="{c["target_label"]}"'
        f' data-fac="{DOSTEPNOSC[c["target"]]}">{ZDANIA[c["id"]].rstrip(".")}</option>'
        for c in MOMENT_SECTIONS)
    szuk_mia = "\n".join(
        f'            <option value="{c}">{FAC[c]["name"]}</option>' for c in CITIES)

    # 6 osobnych sytuacji — opisy wyłącznie z faktów źródłowych, ikony z projektu klienta
    # Sytuacja jako komórka siatki, nie artykuł na całą szerokość.
    # Było: 6 bloków jeden pod drugim, tekst na 40% szerokości, reszta pusta —
    # 2969 px, czyli 34% całej strony. Dwie kolumny zdejmują z tego połowę.
    # Zdanie „Wolisz porozmawiać?…" powtarzało się w KAŻDYM z sześciu bloków
    # i odsyłało do „paska powyżej", którego już nie ma. Zostaje raz, na końcu.
    def case_block(i, c):
        items = "\n".join(f'        <li>{it}</li>' for it in c["items"])
        # część sytuacji nie ma drugiego akapitu — pusty <p> zostawiałby dziurę
        # Drugi akapit zdjęty z KAŻDEJ sytuacji (2026-08-03). Na stronie głównej
        # sytuacja ma rozpoznać pacjenta i skierować go dalej — opisy kliniczne
        # żyją na stronach usług, do których prowadzi odsyłacz pod spodem.
        akapit = ""
        return f"""      <article class="case" id="{c['id']}">
        <p class="case__top">
          <span class="case__num">{i+1:02d}</span>
          {picon(c['icon'], 'picon case__ico')}
        </p>
        <h3 class="case__h">{c['h']}</h3>
        <p class="case__lead">{c['lead']}</p>
{akapit}        <ul class="case__list">
{items}
        </ul>
        <a class="case__cta" href="{c['target']}/">{c['target_label']} <span aria-hidden="true">&rarr;</span></a>
      </article>"""
    cases_html = "\n".join(case_block(i, c) for i, c in enumerate(MOMENT_SECTIONS))

    svc_imgs = "\n".join(
        f'        <div class="svc__img{" is-active" if i == 0 else ""}" data-bg="assets/img/{SERVICES[s]["img"]}"></div>'
        for i, s in enumerate(SERVICE_ORDER))
    svc_index = "\n".join(
        f'      <a class="svc__item" href="{s}/" data-svc="{i}"><span class="svc__inum">0{i+1}</span>'
        f'{picon(ICON_FOR_SERVICE[s], "picon svc__iico")}'
        f'<span class="svc__iname">{SERVICES[s]["title"]}</span>'
        f'<span class="svc__iarrow" aria-hidden="true">→</span><span class="svc__iline" aria-hidden="true"></span></a>'
        for i, s in enumerate(SERVICE_ORDER))

    html_out = head(
        0,
        "Reha Medica Psychoterapia — opieka psychologiczna i psychoterapeutyczna",
        "Poradnia psychologiczna, ośrodek dla dzieci i młodzieży, konsultacje psychologiczne i psychoterapeutyczne oraz lekarz psychiatra w placówkach Reha Medica na Pomorzu Zachodnim.",
        "", preload_hero=True, extra_ld=[org], usluga_css=True,
    ) + f"""
<body class="is-home">

<a class="skip-link" href="#main">Przejdź do treści</a>

{sprite(list(ICONS))}

{header(0)}

<main id="main">

<!-- HERO PEŁNOEKRANOWE — wzorzec Grow Therapy: zdjęcie na całą szerokość
     i wysokość, nagłówek na nim, a w środku widget z dwoma polami wyboru.
     Tam są „stan" i „ubezpieczenie"; tutaj MIASTO i SYTUACJA — dokładne
     odpowiedniki, bo to one decydują, dokąd pacjent ma zadzwonić.
     Wybór sytuacji podmienia zdjęcie: interakcja niesie treść, nie ozdobę. -->
<section class="hero3" id="hero" aria-labelledby="teza">
  <div class="hero3__media" aria-hidden="true">
{hero_imgs}
    <span class="hero3__scrim"></span>
  </div>
  <div class="hero3__in hero3__grid">
   <div class="hero3__col">
    <h1 class="hero3__h" id="teza">
      <span class="hero3__a">Nie musisz wiedzieć, od czego zacząć.</span>
      <span class="hero3__b">Powiedz, co się dzieje. Resztę ustalimy razem.</span>
    </h1>
    <!-- Po lewej NIE MA przycisku. Rehabilitacja ma tu dwa („Umów wizytę",
         „Znajdź usługę") i konkurują z kartą po prawej. Tutaj jedyną akcją
         samoobsługową jest wybierak w karcie; po lewej stoi telefon, czyli
         INNA droga, a nie ta sama w drugim opakowaniu. -->
    <p class="hero3__tel">
      <span class="hero3__tel-l">Wolisz od razu porozmawiać?</span>
      <a class="hero3__tel-n" href="tel:+48943721451">94&nbsp;372&nbsp;14&nbsp;51</a>
      <span class="hero3__tel-g">pon.–pt. 8:00–19:00 · sob. 8:00–18:00</span>
    </p>
   </div>

    <!-- Karta pionowa po prawej, jak w rehabilitacji: hasło nad polami,
         oba pola obok siebie, wynik pod spodem. -->
    <div class="szuk" id="placowki" data-szuk>
      <p class="szuk__h">Zacznijmy od dwóch pytań.</p>
      <div class="szuk__row">
        <p class="szuk__f">
          <label class="szuk__l" for="sz-syt">Z czym przychodzisz?</label>
          <select class="szuk__s" id="sz-syt" data-syt>
            <option value="">Wybierz…</option>
{szuk_syt}
          </select>
        </p>
        <p class="szuk__f">
          <label class="szuk__l" for="sz-mia">Gdzie szukasz pomocy?</label>
          <select class="szuk__s" id="sz-mia" data-mia>
            <option value="">Wybierz…</option>
{szuk_mia}
          </select>
        </p>
      </div>
      <div class="szuk__out" data-out aria-live="polite"></div>
    </div>
  </div>
</section>

<!-- Alma trzyma koszt w hero, nie w połowie strony. Najmocniejszy
     potwierdzony fakt cenowy wychodzi tuż pod pierwszy ekran. -->
<aside class="darmo">
  <div class="wrap darmo__in">
    <span class="darmo__tag">Bezpłatnie</span>
    <p class="darmo__t">Dzieci i młodzież do 21. roku życia oraz ich rodziny — <a href="osrodek-psychologiczno-psychoterapeutyczny/">Ośrodek Środowiskowej Opieki Psychologicznej i Psychoterapeutycznej</a>.</p>
  </div>
</aside>

<!-- Skala zjawiska. Wzorzec: pasek wyników z growtherapy.com. Tam są to
     WŁASNE wyniki kliniczne placówki; Reha Medica takich pomiarów nie ma
     w źródłach, a wymyślenie ich łamie regułę o nieinwentowaniu wyników.
     Dlatego liczby mówią o skali zjawiska i o dostępie do pomocy — dane
     CBOS, z podaniem komunikatu, próby i odsyłacza do PDF-a.
     Zastrzeżenie „nie są to wyniki Reha Medica" jest w sekcji, nie w stopce. -->
<section class="sec skala" id="skala" aria-labelledby="skala-h">
  <div class="wrap">
    <header class="skala__head" data-animate>
      <p class="kicker">To częstsze, niż się wydaje</p>
      <h2 class="sec__h" id="skala-h">Tak to wygląda w Polsce</h2>
    </header>
    <ol class="skala__lista">
{skala_html}
    </ol>
    <p class="skala__zrodlo">
      Źródło: <a href="{SKALA_URL}" rel="noopener nofollow" target="_blank">{SKALA_ZRODLO}</a>
    </p>
  </div>
</section>

<section class="cases" id="pomoc" aria-labelledby="cases-h">
  <header class="cases__head" data-animate>
    <p class="kicker">Sytuacje</p>
    <h2 class="cases__h" id="cases-h">W jakich momentach psychoterapia może pomóc</h2>
    <p class="cases__intro">Sześć sytuacji opisanych w materiałach poradni. Każda prowadzi do konkretnej formy pomocy.</p>
  </header>
  <div class="cases__list">
{cases_html}
  </div>
  <p class="cases__stopka">Nie rozpoznajesz się w żadnej z tych sytuacji? To nie przeszkoda —
    <a href="kontakt/">zadzwoń do recepcji</a> albo <a href="#pierwsza-wizyta">zobacz, jak wygląda pierwsza wizyta</a>.</p>
</section>

<section class="sec zakres" id="uslugi" aria-labelledby="zakres-h">
  <div class="wrap">
    <header class="sec__head">
      <p class="kicker">Zakres pomocy</p>
      <h2 class="sec__h" id="zakres-h">Pięć form opieki</h2>
      <p class="sec__lead">Od pierwszej konsultacji, przez psychoterapię, po diagnozę neuropsychologiczną i leczenie psychiatryczne.</p>
    </header>
    <ul class="zakres__list">
{zakres_html}
    </ul>
  </div>
</section>

<section class="sec sec--beige koszt" id="finansowanie" aria-labelledby="koszt-h">
  <div class="wrap koszt__grid">
    <header class="sec__head">
      <p class="kicker">Finansowanie</p>
      <h2 class="sec__h" id="koszt-h">Ile to kosztuje</h2>
      <p class="sec__lead">Mówimy tylko to, co potwierdzone. Resztę ustala recepcja placówki — i lepiej zapytać, niż zgadywać.</p>
    </header>
    <dl class="koszt__list">
      <div class="koszt__i koszt__i--free">
        <dt>Ośrodek dla Dzieci i Młodzieży</dt>
        <dd><b>Bezpłatnie.</b> Dzieci do 7. roku życia, dzieci i młodzież objęte obowiązkiem szkolnym do 21. roku życia oraz ich rodziny i opiekunowie prawni.</dd>
      </div>
      <div class="koszt__i">
        <dt>Lekarz psychiatra</dt>
        <dd><b>Komercyjnie, odpłatnie.</b> Pacjenci od 14. roku życia.</dd>
      </div>
      <div class="koszt__i">
        <dt>Poradnia i konsultacje</dt>
        <dd>Sposób finansowania potwierdza recepcja wybranej placówki.</dd>
      </div>
    </dl>
  </div>
</section>

<!-- Pierwsza wizyta. Wzorzec z rynku: to pytanie zatrzymuje przed telefonem
     częściej niż cena. Zamiast trzech kart — sekwencja z ciągłą linią, bo to
     jest droga, nie zestaw. Kadra wyciągnięta na wierzch: badania rynku PL
     mówią wprost, że zaufanie buduje informacja o tym, KTO przyjmie. -->
<section class="sec wiz" id="pierwsza-wizyta" aria-labelledby="wiz-h">
  <div class="wrap wiz__grid">
    <div class="wiz__intro">
      <p class="kicker">Zanim zadzwonisz</p>
      <h2 class="sec__h" id="wiz-h">Jak wygląda pierwsza wizyta</h2>
      <p class="sec__lead">Nie musisz umieć nazwać tego, co się dzieje. Pierwsze spotkanie służy właśnie temu, żeby to określić.</p>
      <div class="wiz__kto">
        <p class="wiz__kto-l">Kto Cię przyjmie</p>
        <p class="wiz__kto-t">Wykwalifikowani <b>psychologowie i psychoterapeuci z dużym doświadczeniem klinicznym</b>. W Ośrodku dla Dzieci i Młodzieży — psycholog kliniczny, terapeuta środowiskowy i psychoterapeuci.</p>
      </div>
      <!-- Autentyczne wejście Reha Medica. Sekcja odpowiada na pytanie „co się
           wydarzy", a zdjęcie odpowiada na jego cichą część: „jak tam będzie".
           Stało tu wcześniej ok. 150 px pustki pod tekstem. -->
      <figure class="wiz__foto">
        <img src="assets/img/recepcja-konsultacje.webp" alt="Wejście i poczekalnia w placówce Reha Medica"
             width="1200" height="800" loading="lazy" decoding="async">
        <figcaption>Wejście do placówki w Szczecinku</figcaption>
      </figure>
    </div>

    <ol class="wiz__kroki">
      <li class="wiz__k">
        <h3 class="wiz__kh">Mówisz, co się dzieje</h3>
        <p class="wiz__kp">Opowiadasz o tym, jak się czujesz i w jakiej sytuacji życiowej teraz jesteś.</p>
      </li>
      <li class="wiz__k">
        <h3 class="wiz__kh">Specjalista pyta i słucha</h3>
        <p class="wiz__kp">Jeśli sam nie potrafisz nazwać trudności, pomoże Ci to określić odpowiednimi pytaniami. Im więcej usłyszy, tym łatwiej dobrać właściwą pomoc.</p>
      </li>
      <li class="wiz__k">
        <h3 class="wiz__kh">Ustalacie, co dalej</h3>
        <p class="wiz__kp">Razem określacie cele i oczekiwania, które mają się zrealizować dzięki terapii. Rozmowa obejmuje też gotowość i motywację do jej podjęcia.</p>
      </li>
    </ol>

    <p class="wiz__ulga"><b>Terapeuta też jest do sprawdzenia.</b> Czasem zdarza się, że dany terapeuta nie pasuje pacjentowi. Konsultacja jest dobrym czasem, żeby to sprawdzić i dokonać zmiany.</p>
    <p class="wiz__uwaga">Pierwsza wizyta u lekarza psychiatry ma charakter diagnostyczny i trwa dłużej niż późniejsze wizyty kontrolne.</p>
  </div>
</section>

<!-- OPINIE. Uwaga treściowa: żadna z 14 opinii nie dotyczy psychoterapii —
     wszystkie mówią o rehabilitacji, zabiegach i recepcji. Sekcja mówi to
     wprost, bo inaczej sugerowałaby opinie o opiece psychologicznej, których
     nie ma. Dane: site-psycho/data/reviews.json, weryfikacja ręczna. -->
<section class="reviews" id="opinie" aria-labelledby="rv-h">
  <h2 class="visually-hidden" id="rv-h">Opinie pacjentów o Reha Medica</h2>
  <div class="reviews__inner">
    <div class="rv-summary" data-animate>
      <p class="kicker rv-summary__eyebrow">Opinie pacjentów</p>
      <p class="rv-summary__label" data-rv-label>DOSKONAŁA</p>
      <div class="rv-summary__stars" data-rv-stars aria-hidden="true">★★★★★</div>
      <p class="rv-summary__score"><span data-rv-rating>4,8</span><span class="rv-summary__of">/5</span></p>
      <p class="rv-summary__count">Na podstawie <span data-rv-count>58</span> opinii</p>
      <p class="rv-summary__brand"><img src="assets/img/google-g-mono.svg" alt="Google" width="18" height="18"><span>Opinie zweryfikowane w Google</span></p>
      <p class="rv-summary__zakres">Oceny dotyczą centrum Reha Medica w Szczecinku — rehabilitacji, zabiegów i obsługi recepcji. <b>Nie są to opinie o opiece psychologicznej.</b></p>
      <a class="rv-summary__cta" data-rv-more href="https://share.google/ACPY9joNkVJVdrKvZ" target="_blank" rel="noopener">Zobacz wszystkie opinie w Google <span class="rv-summary__arw" aria-hidden="true">&rarr;</span></a>
    </div>
    <div class="rv-slider">
      <ul class="rv-track" id="rv-track" data-rv-track role="list" tabindex="0" aria-label="Opinie pacjentów Reha Medica — karuzela">
        <li class="rv-card rv-card--empty" aria-hidden="true"></li>
      </ul>
      <button class="rv-arrow rv-arrow--prev" data-rv-prev type="button" aria-label="Poprzednie opinie" aria-controls="rv-track">
        <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M15 5l-7 7 7 7" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <button class="rv-arrow rv-arrow--next" data-rv-next type="button" aria-label="Następne opinie" aria-controls="rv-track">
        <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M9 5l7 7-7 7" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
    </div>
  </div>
</section>

<section class="sec sec--beige pyt" id="faq" aria-labelledby="pyt-h">
  <div class="wrap pyt__grid">
    <div class="pyt__intro">
      <header class="sec__head">
        <p class="kicker">Wątpliwości</p>
        <h2 class="sec__h" id="pyt-h">Najczęstsze pytania</h2>
      </header>
      <p class="pyt__lead">Jeśli Twojego pytania tu nie ma, recepcja odpowie przez telefon.</p>
      <a class="sec__more" href="faq/">Wszystkie pytania <span aria-hidden="true">&rarr;</span></a>
    </div>
    <div class="pyt__list">
{faq_html}
    </div>
  </div>
</section>


<!-- Newsletter — ten sam punkt końcowy co serwis główny, więc zapisy trafiają
     do istniejącego panelu. Telefon opcjonalny, zgoda SMS pojawia się dopiero
     po wpisaniu numeru (obsługa w main.js). -->
<section class="section newsletter" id="newsletter" aria-labelledby="nl-h">
  <div class="wrap newsletter__inner" data-animate>
    <div class="newsletter__text">
      <p class="kicker">Newsletter</p>
      <h2 class="section__title" id="nl-h">Informacje z placówek prosto na Twój e-mail</h2>
      <p class="newsletter__lead">Nowe terminy, zmiany w placówkach i projekty, w których bierzemy udział. Podaj telefon, jeśli chcesz dostawać powiadomienia także SMS-em.</p>
    </div>
    <form class="newsletter__form" id="newsletter-form" novalidate data-endpoint="https://rehamedica.info.pl/panel/api/subscribe.php">
      <div class="field field--nl">
        <label for="nl-email">Adres e-mail</label>
        <input id="nl-email" name="email" type="email" placeholder="Twój adres e-mail" autocomplete="email" required>
      </div>
      <div class="field field--nl">
        <label for="nl-tel">Telefon <span class="field__opt">— opcjonalnie</span></label>
        <input id="nl-tel" name="tel" type="tel" inputmode="tel" placeholder="np. 600 100 200" autocomplete="tel" aria-describedby="nl-tel-hint">
        <p class="field__hint" id="nl-tel-hint">Tylko jeśli chcesz otrzymywać powiadomienia SMS. Bez numeru zapiszesz się na sam e-mail.</p>
      </div>
      <label class="consent consent--nl">
        <input type="checkbox" name="consent" required>
        <span>Wyrażam zgodę na otrzymywanie newslettera Reha Medica na podany adres e-mail. Szczegóły dotyczące przetwarzania danych znajdują się w <a href="{MAIN}/polityka-prywatnosci/" rel="noopener">polityce prywatności</a>.</span>
      </label>
      <label class="consent consent--nl" data-sms-consent hidden>
        <input type="checkbox" name="consent-sms">
        <span>Wyrażam zgodę na otrzymywanie powiadomień SMS na podany numer telefonu.</span>
      </label>
      <button class="btn btn--brand newsletter__submit" type="submit">Zapisuję się</button>
      <p class="newsletter__note" data-nl-note hidden></p>
    </form>
  </div>
</section>

</main>

{footer(0)}
{tail(0)}""".replace('</body>', '<script src="js/home.js?v=2"></script>\n</body>')
    BUILT.append(write("index.html", html_out))


# ══════════════════════════════════════════════ STRONA USŁUGI (ogólna)
def build_service(sk):
    s = SERVICES[sk]
    cnt = SERVICE_CONTENT[sk]
    depth = 1
    r = rel(depth)
    url = f"{BASE}/{sk}/"

    # Siatka form pomocy zamiast akapitu wyliczającego (wzorzec Centrum Sobota).
    # Renderuje się WYŁĄCZNIE dla usług obecnych w FORMY, czyli tam, gdzie
    # materiały klienta faktycznie wymieniają poszczególne formy.
    formy_sekcja = ""
    if sk in FORMY:
        kafle = "\n".join(
            f'        <li class="formy__i">'
            f'<span class="formy__ico" style="--ik:url({r}assets/ikony/{ik}.png)" aria-hidden="true"></span>'
            f'<span class="formy__t">{txt}</span></li>'
            for ik, txt, _ in FORMY[sk])
        formy_sekcja = f"""
  <section class="lsec lsec--beige formy" aria-labelledby="formy-h">
    <div class="wrap">
      <h2 class="formy__h" id="formy-h">Formy pomocy</h2>
      <ul class="formy__list">
{kafle}
      </ul>
    </div>
  </section>
"""

    if s["cities"]:
        cards = "\n".join(pcard(c, depth, s["title"]) for c in s["cities"])
        label = "Dostępne w placówkach" if len(s["cities"]) > 1 else "Dostępne w placówce"
        city_links = "\n".join(
            f'        <li><a class="needs__item" href="{r}{c}/{sk}/"><span class="needs__txt">'
            f'<span class="needs__name">{s["title"]} — {FAC[c]["name"]}</span>'
            f'<span class="needs__to">{FAC[c]["addr"]}, {FAC[c]["zip"]} {FAC[c]["name"]}</span></span>'
            f'<span class="needs__arrow" aria-hidden="true">→</span></a></li>'
            for c in s["cities"])
        miasta_sekcja = f"""
  <section class="lsec lsec--beige">
    <div class="wrap">
      <header class="section__head">
        <p class="kicker">Placówki</p>
        <h2 class="section__title">{s['title']} w Twoim mieście</h2>
      </header>
      <ul class="needs__list cornerframe">
{city_links}
      </ul>
    </div>
  </section>
"""
        splate = f"""<section class="splate">
  <div class="wrap splate__inner">
    <div class="splate__head">
      {picon(ICON_FOR_SERVICE[sk], "picon splate__ico")}<span class="splate__label">{label}</span>
      {FIN_LABEL[s['fin']]}
    </div>
    <div class="splate__grid">
      <div class="splate__cards">
{cards}
      </div>
    </div>
  </div>
</section>"""
        bk_places = " ".join(s["cities"])
    else:
        miasta_sekcja = ""
        splate = f"""<section class="splate">
  <div class="wrap splate__inner">
    <div class="splate__head">
      {picon(ICON_FOR_SERVICE[sk], "picon splate__ico")}<span class="splate__label">Dostępność</span>
      {FIN_LABEL[s['fin']]}
    </div>
    <div class="splate__grid">
      <div class="splate__cards">
        <article class="pcard">
          <p class="pcard__city">Zapytaj o termin</p>
          <p class="pcard__row"><span>Skontaktuj się z recepcją wybranej placówki Reha Medica, aby potwierdzić dostępność tej formy pomocy i umówić termin.</span></p>
          <div class="pcard__cta"><a class="btn btn--brand" href="{r}placowki/">Wybierz placówkę <span class="btn__arrow" aria-hidden="true">→</span></a></div>
        </article>
      </div>
    </div>
  </div>
</section>"""
        bk_places = " ".join(CITIES)

    ld = [breadcrumb_ld([("Strona główna", BASE + "/"), (s["title"], None)])]
    html_out = head(depth, f"{s['title']} — Reha Medica Psychoterapia", s["lead"], f"{sk}/",
                    img=s["img"] if s["img"].endswith(".jpg") else "og-psychoterapia.jpg",
                    extra_ld=ld) + f"""
<body class="no-hero">

<a class="skip-link" href="#main">Przejdź do treści</a>

{sprite([ICON_FOR_SERVICE[sk]])}

{header(depth, active=sk)}

<main id="main">

<section class="shero">
  <div class="shero__media" aria-hidden="true">
    <div class="shero__img" style="background-image:url('{r}assets/img/{s['img']}')"></div>
    <div class="shero__scrim"></div>
  </div>
  <div class="wrap shero__inner">
    <nav class="ubread" aria-label="Ścieżka nawigacji">
      <ol class="ubread__list">
        <li><a href="{r}index.html">Strona główna</a></li>
        <li><span aria-current="page">{s['title']}</span></li>
      </ol>
    </nav>
    <h1 class="shero__title">{s['title']}</h1>
  </div>
</section>

{splate}

<article class="usluga">
{formy_sekcja}
  <section class="lsec lsec--ivory">
    <div class="wrap lintro lintro--rytm">

{prose_block(cnt, f"{r}assets/img/{s['band'] or s['img']}", s['title'] + " — Reha Medica", depth)}

    </div>
  </section>
{miasta_sekcja}
  <section class="uend">
    <div class="wrap uend__inner">
      <a class="btn btn--brand uend__btn" href="{r}index.html#placowki" data-booking>Umów wizytę <span class="btn__arrow" aria-hidden="true">→</span></a>
      <a class="uend__back" href="{r}index.html"><span aria-hidden="true">←</span> Wróć do strony głównej</a>
    </div>
  </section>

</article>

</main>

{footer(depth)}
{tail(depth, bk_places=bk_places, bk_service=s['title'])}"""
    BUILT.append(write(f"{sk}/index.html", html_out))


# ══════════════════════════════════════════════ STRONA MIASTO × USŁUGA
def build_city_service(city, sk):
    s = SERVICES[sk]
    f = FAC[city]
    depth = 2
    r = rel(depth)
    if sk == "poradnia-psychologiczna":
        cnt = dict(PORADNIA_MIASTA[city]); cnt["kicker"] = "Dla kogo"
    elif sk == "osrodek-psychologiczno-psychoterapeutyczny":
        cnt = dict(OSRODEK_MIASTA[city]); cnt["kicker"] = "Dla kogo"
        cnt.setdefault("pull_p", []); cnt.setdefault("parts_h", None); cnt.setdefault("parts", [])
    else:
        cnt = dict(KONS_MIASTA[city]); cnt["kicker"] = "Czemu służą"
    cnt.setdefault("coda_lead", None); cnt.setdefault("coda_p", None)

    title = f"{s['title']} — {f['name']}"
    url = f"{BASE}/{city}/{sk}/"
    ld = [
        clinic_ld(city, url, name_suffix=""),
        breadcrumb_ld([("Strona główna", BASE + "/"),
                       (f["name"], f"{BASE}/{city}/"),
                       (s["title"], None)]),
    ]
    ld[0] = {"@context": "https://schema.org", **ld[0]}

    html_out = head(depth, f"{title} | Reha Medica Psychoterapia",
                    f"{s['title']} w {f['name']}: {f['addr']}. Telefon, e-mail i godziny recepcji. {s['lead']}",
                    f"{city}/{sk}/", extra_ld=ld) + f"""
<body class="no-hero">

<a class="skip-link" href="#main">Przejdź do treści</a>

{sprite([ICON_FOR_SERVICE[sk]])}

{header(depth, active="city:" + city)}

<main id="main">

<section class="shero">
  <div class="shero__media" aria-hidden="true">
    <div class="shero__img" style="background-image:url('{r}assets/img/{s['img']}')"></div>
    <div class="shero__scrim"></div>
  </div>
  <div class="wrap shero__inner">
    <nav class="ubread" aria-label="Ścieżka nawigacji">
      <ol class="ubread__list">
        <li><a href="{r}index.html">Strona główna</a></li>
        <li><a href="{r}{city}/">{f['name']}</a></li>
        <li><span aria-current="page">{s['title']}</span></li>
      </ol>
    </nav>
    <h1 class="shero__title">{s['title']} — {f['name']}</h1>
  </div>
</section>

<section class="splate">
  <div class="wrap splate__inner">
    <div class="splate__head">
      {picon(ICON_FOR_SERVICE[sk], "picon splate__ico")}<span class="splate__label">Placówka</span>
      {FIN_LABEL[s['fin']]}
    </div>
    <div class="splate__grid">
      <div class="splate__cards">
{pcard(city, depth, s['title'])}
      </div>
    </div>
  </div>
</section>

<article class="usluga">

  <section class="lsec lsec--ivory">
    <div class="wrap lintro lintro--rytm">

{prose_block(cnt, f"{r}assets/img/{s['band'] or s['img']}", f"{s['title']} — Reha Medica {f['name']}", depth)}

    </div>
  </section>

  <section class="lsec lsec--beige">
    <div class="wrap">
      <header class="section__head">
        <p class="kicker">{f['name']}</p>
        <h2 class="section__title">Dojazd i kontakt</h2>
      </header>
      <ul class="needs__list cornerframe">
        <li><a class="needs__item" href="{r}{city}/"><span class="needs__txt"><span class="needs__name">Placówka Reha Medica {f['name']}</span><span class="needs__to">Adres, telefon, godziny i pełna oferta psychologiczna</span></span><span class="needs__arrow" aria-hidden="true">→</span></a></li>
        <li><a class="needs__item" href="{r}{sk}/"><span class="needs__txt"><span class="needs__name">{s['title']} — pełny opis</span><span class="needs__to">Zakres, przebieg i dla kogo</span></span><span class="needs__arrow" aria-hidden="true">→</span></a></li>
      </ul>
    </div>
  </section>

  <section class="uend">
    <div class="wrap uend__inner">
      <a class="btn btn--brand uend__btn" href="tel:{f['phones'][0][1]}">Zadzwoń: {f['phones'][0][0]} <span class="btn__arrow" aria-hidden="true">→</span></a>
      <a class="uend__back" href="{r}{city}/"><span aria-hidden="true">←</span> Wróć do placówki {f['name']}</a>
    </div>
  </section>

</article>

</main>

{footer(depth)}
{tail(depth)}"""
    BUILT.append(write(f"{city}/{sk}/index.html", html_out))


# ══════════════════════════════════════════════ HUB MIASTA
def build_city(city):
    f = FAC[city]
    depth = 1
    r = rel(depth)
    services_here = [s for s in SERVICE_ORDER if city in SERVICES[s]["cities"]]
    url = f"{BASE}/{city}/"

    items = "\n".join(
        f'        <li><a class="needs__item needs__item--ico" href="{r}{city}/{s}/">'
        f'{picon(ICON_FOR_SERVICE[s], "picon needs__ico")}<span class="needs__txt">'
        f'<span class="needs__name">{SERVICES[s]["title"]}</span>'
        f'<span class="needs__to">{SERVICES[s]["lead"]}</span></span>'
        f'<span class="needs__arrow" aria-hidden="true">→</span></a></li>'
        for s in services_here)

    inne = "\n".join(
        f'        <li><a class="needs__item needs__item--ico" href="{r}{s}/">'
        f'{picon(ICON_FOR_SERVICE[s], "picon needs__ico")}<span class="needs__txt">'
        f'<span class="needs__name">{SERVICES[s]["title"]}</span>'
        f'<span class="needs__to">Dostępność potwierdza recepcja</span></span>'
        f'<span class="needs__arrow" aria-hidden="true">→</span></a></li>'
        for s in SERVICE_ORDER if s not in services_here)

    ld = [{"@context": "https://schema.org", **clinic_ld(city, url)},
          breadcrumb_ld([("Strona główna", BASE + "/"), ("Placówki", f"{BASE}/placowki/"), (f["name"], None)])]

    lista_uslug = ", ".join(SERVICES[s]["title"].lower() for s in services_here)
    html_out = head(depth, f"Reha Medica {f['name']} — opieka psychologiczna",
                    f"Opieka psychologiczna Reha Medica w {f['name']}: {lista_uslug}. {f['addr']}, telefon i e-mail do recepcji.",
                    f"{city}/", extra_ld=ld) + f"""
<body class="no-hero">

<a class="skip-link" href="#main">Przejdź do treści</a>

{sprite([ICON_FOR_SERVICE[s] for s in SERVICE_ORDER])}

{header(depth, active="city:" + city)}

<main id="main">

<section class="shero">
  <div class="shero__media" aria-hidden="true">
    <div class="shero__img" style="background-image:url('{r}assets/img/budynek-rehamedica.webp')"></div>
    <div class="shero__scrim"></div>
  </div>
  <div class="wrap shero__inner">
    <nav class="ubread" aria-label="Ścieżka nawigacji">
      <ol class="ubread__list">
        <li><a href="{r}index.html">Strona główna</a></li>
        <li><a href="{r}placowki/">Placówki</a></li>
        <li><span aria-current="page">{f['name']}</span></li>
      </ol>
    </nav>
    <h1 class="shero__title">Reha Medica {f['name']} — opieka psychologiczna</h1>
  </div>
</section>

<section class="splate">
  <div class="wrap splate__inner">
    <div class="splate__head">
      <span class="splate__label">Kontakt do recepcji</span>
      <span class="splate__nfz">Pon.–pt. 8:00–19:00 · sob. 8:00–18:00</span>
    </div>
    <div class="splate__grid">
      <div class="splate__cards">
{pcard(city, depth, "Wizyta")}
      </div>
    </div>
  </div>
</section>

<article class="usluga">

  <section class="lsec lsec--ivory">
    <div class="wrap">
      <header class="section__head">
        <p class="kicker">Zakres pomocy w {f['name']}</p>
        <h2 class="section__title">Co prowadzimy w tej placówce</h2>
      </header>
      <ul class="needs__list cornerframe">
{items}
      </ul>
    </div>
  </section>

  <section class="lsec lsec--beige">
    <div class="wrap">
      <header class="section__head">
        <p class="kicker">Pozostałe formy pomocy</p>
        <h2 class="section__title">Dostępność potwierdza recepcja</h2>
      </header>
      <ul class="needs__list cornerframe">
{inne}
      </ul>
      <p class="needs__note">Nie zakładamy, że każda placówka prowadzi każdą formę pomocy. Przed wizytą potwierdź dostępność telefonicznie.</p>
    </div>
  </section>

  <section class="uend">
    <div class="wrap uend__inner">
      <a class="btn btn--brand uend__btn" href="tel:{f['phones'][0][1]}">Zadzwoń: {f['phones'][0][0]} <span class="btn__arrow" aria-hidden="true">→</span></a>
      <a class="uend__back" href="{r}placowki/"><span aria-hidden="true">←</span> Wszystkie placówki</a>
    </div>
  </section>

</article>

</main>

{footer(depth)}
{tail(depth)}"""
    BUILT.append(write(f"{city}/index.html", html_out))


# ══════════════════════════════════════════════ HUB PLACÓWEK + KONTAKT + 404
def build_placowki():
    depth = 1
    r = rel(depth)
    cards = "\n".join(f"""        <article class="pcard">
          <p class="pcard__city"><a href="{r}{c}/">{FAC[c]['name']}</a></p>
          <p class="pcard__row"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-pin"></use></svg><span>{FAC[c]['addr']}, {FAC[c]['zip']} {FAC[c]['name']}</span></p>
""" + "".join(f'          <a class="pcard__row" href="tel:{tel}"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-phone"></use></svg><span>{txt}</span></a>\n' for txt, tel in FAC[c]['phones']) + f"""          <a class="pcard__row" href="mailto:{FAC[c]['email']}"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-mail"></use></svg><span>{FAC[c]['email']}</span></a>
          <div class="pcard__cta"><a class="btn btn--brand" href="{r}{c}/">Zobacz placówkę <span class="btn__arrow" aria-hidden="true">→</span></a></div>
        </article>""" for c in CITIES)

    ld = [breadcrumb_ld([("Strona główna", BASE + "/"), ("Placówki", None)])]
    html_out = head(depth, "Placówki — Reha Medica Psychoterapia",
                    "Adresy, telefony i e-maile placówek Reha Medica prowadzących opiekę psychologiczną: Szczecinek, Szczecin, Wałcz, Białogard, Bobolice.",
                    "placowki/", extra_ld=ld) + f"""
<body class="no-hero">

<a class="skip-link" href="#main">Przejdź do treści</a>

{SPRITE}

{header(depth)}

<main id="main">

<section class="shero">
  <div class="shero__media" aria-hidden="true">
    <div class="shero__img" style="background-image:url('{r}assets/img/wnetrze-rehamedica.webp')"></div>
    <div class="shero__scrim"></div>
  </div>
  <div class="wrap shero__inner">
    <nav class="ubread" aria-label="Ścieżka nawigacji">
      <ol class="ubread__list">
        <li><a href="{r}index.html">Strona główna</a></li>
        <li><span aria-current="page">Placówki</span></li>
      </ol>
    </nav>
    <h1 class="shero__title">Placówki</h1>
  </div>
</section>

<section class="splate">
  <div class="wrap splate__inner">
    <div class="splate__head">
      <span class="splate__label">Pięć placówek na Pomorzu Zachodnim</span>
      <span class="splate__nfz">Pon.–pt. 8:00–19:00 · sob. 8:00–18:00</span>
    </div>
    <div class="splate__grid">
      <div class="splate__cards">
{cards}
      </div>
    </div>
  </div>
</section>

<article class="usluga">
  <section class="uend">
    <div class="wrap uend__inner">
      <a class="btn btn--brand uend__btn" href="{r}index.html#placowki" data-booking>Umów wizytę <span class="btn__arrow" aria-hidden="true">→</span></a>
      <a class="uend__back" href="{r}index.html"><span aria-hidden="true">←</span> Wróć do strony głównej</a>
    </div>
  </section>
</article>

</main>

{footer(depth)}
{tail(depth, bk_places=" ".join(CITIES), bk_service="Wizyta")}"""
    BUILT.append(write("placowki/index.html", html_out))


def build_kontakt():
    depth = 1
    r = rel(depth)
    rows = "\n".join(f"""        <article class="pcard">
          <p class="pcard__city"><a href="{r}{c}/">{FAC[c]['name']}</a></p>
          <p class="pcard__row"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-pin"></use></svg><span>{FAC[c]['addr']}, {FAC[c]['zip']} {FAC[c]['name']}</span></p>
""" + "".join(f'          <a class="pcard__row" href="tel:{tel}"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-phone"></use></svg><span>{txt}</span></a>\n' for txt, tel in FAC[c]['phones']) + f"""          <a class="pcard__row" href="mailto:{FAC[c]['email']}"><svg class="ico" aria-hidden="true" focusable="false"><use href="#i-mail"></use></svg><span>{FAC[c]['email']}</span></a>
        </article>""" for c in CITIES)

    ld = [breadcrumb_ld([("Strona główna", BASE + "/"), ("Kontakt", None)])]
    html_out = head(depth, "Kontakt — Reha Medica Psychoterapia",
                    "Telefony i adresy e-mail do recepcji placówek Reha Medica prowadzących opiekę psychologiczną i psychoterapeutyczną.",
                    "kontakt/", extra_ld=ld) + f"""
<body class="no-hero">

<a class="skip-link" href="#main">Przejdź do treści</a>

{SPRITE}

{header(depth, active="kontakt")}

<main id="main">

<section class="shero">
  <div class="shero__media" aria-hidden="true">
    <div class="shero__img" style="background-image:url('{r}assets/img/recepcja-hero.webp')"></div>
    <div class="shero__scrim"></div>
  </div>
  <div class="wrap shero__inner">
    <nav class="ubread" aria-label="Ścieżka nawigacji">
      <ol class="ubread__list">
        <li><a href="{r}index.html">Strona główna</a></li>
        <li><span aria-current="page">Kontakt</span></li>
      </ol>
    </nav>
    <h1 class="shero__title">Kontakt</h1>
  </div>
</section>

<article class="usluga">

  <section class="lsec lsec--ivory">
    <div class="wrap lintro">
      <div class="lintro__open">
        <div class="lintro__head">
          <p class="lkick">Jak umówić wizytę</p>
          <p class="lintro__lead">Wizytę umawiasz bezpośrednio w recepcji wybranej placówki — telefonicznie lub e-mailem.</p>
        </div>
        <div class="lintro__body">
          <p class="lintro__p">Wybierz miasto, w którym chcesz się leczyć, i skontaktuj się z jego recepcją. Recepcja potwierdzi dostępność danej formy pomocy w tej placówce oraz zaproponuje termin.</p>
          <p class="lintro__p">Zgłoszenie telefoniczne lub e-mailowe nie jest jeszcze potwierdzoną wizytą — termin potwierdza recepcja placówki.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="splate">
    <div class="wrap splate__inner">
      <div class="splate__head">
        <span class="splate__label">Recepcje placówek</span>
        <span class="splate__nfz">Pon.–pt. 8:00–19:00 · sob. 8:00–18:00</span>
      </div>
      <div class="splate__grid">
        <div class="splate__cards">
{rows}
        </div>
      </div>
    </div>
  </section>

  <section class="uend">
    <div class="wrap uend__inner">
      <a class="btn btn--brand uend__btn" href="{r}placowki/">Wszystkie placówki <span class="btn__arrow" aria-hidden="true">→</span></a>
      <a class="uend__back" href="{r}index.html"><span aria-hidden="true">←</span> Wróć do strony głównej</a>
    </div>
  </section>

</article>

</main>

{footer(depth)}
{tail(depth)}"""
    BUILT.append(write("kontakt/index.html", html_out))


def build_404():
    depth = 0
    html_out = head(0, "Nie znaleziono strony — Reha Medica Psychoterapia",
                    "Strona o podanym adresie nie istnieje.", "404.html",
                    robots="noindex,follow") + f"""
<body class="no-hero">

<a class="skip-link" href="#main">Przejdź do treści</a>

{SPRITE}

{header(0)}

<main id="main">
<section class="facmove">
  <div class="wrap facmove__wrap">
    <p class="facmove__kicker">Błąd 404</p>
    <h1 class="facmove__h">Nie znaleźliśmy tej strony</h1>
    <p class="facmove__lead">Strona o podanym adresie nie istnieje lub została przeniesiona. Skorzystaj z menu albo przejdź do listy placówek.</p>
    <a class="btn btn--brand" href="./">Strona główna <span class="btn__arrow" aria-hidden="true">→</span></a>
  </div>
</section>
</main>

{footer(0)}
{tail(0)}"""
    BUILT.append(write("404.html", html_out))


# ══════════════════════════════════════════════ RUN
build_home()
for sk in SERVICE_ORDER:
    build_service(sk)
for c in CITIES:
    build_city(c)
    for sk in SERVICE_ORDER:
        if c in SERVICES[sk]["cities"]:
            build_city_service(c, sk)
build_placowki()
build_kontakt()
build_404()

# sitemap + robots
urls = [""] + [f"{s}/" for s in SERVICE_ORDER] + ["placowki/", "kontakt/"]
for c in CITIES:
    urls.append(f"{c}/")
    for sk in SERVICE_ORDER:
        if c in SERVICES[sk]["cities"]:
            urls.append(f"{c}/{sk}/")
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemap.org/schemas/sitemap/0.9">'.replace("sitemap.org", "sitemaps.org")]
for u in urls:
    sm.append(f"  <url><loc>{BASE}/{u}</loc></url>")
sm.append("</urlset>")
BUILT.append(write("sitemap.xml", "\n".join(sm) + "\n"))
BUILT.append(write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n"))

print(f"Zbudowano {len(BUILT)} plików:")
for b in sorted(BUILT):
    print("  " + b)


# ══════════════════════════════════════════════ FAQ
def build_faq():
    depth = 1; r = rel(depth)
    poz = "\n".join(f"""        <details class="qa"{' open' if i == 0 else ''}>
          <summary class="qa__q">{f['q']}</summary>
          <div class="qa__a">
{chr(10).join(f'            <p>{x}</p>' for x in f['a'])}
            <a class="qa__more" href="{r}{f['cel']}/">{SERVICES[f['cel']]['title']} <span aria-hidden="true">&rarr;</span></a>
          </div>
        </details>""" for i, f in enumerate(FAQ))
    ld = [
      {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":f["q"],
         "acceptedAnswer":{"@type":"Answer","text":" ".join(f["a"])}} for f in FAQ]},
      breadcrumb_ld([("Strona główna", BASE + "/"), ("FAQ", None)]),
    ]
    html_out = head(depth, "Najczęstsze pytania — Reha Medica Psychoterapia",
        "Odpowiedzi na pytania o poradnię psychologiczną, przebieg wizyty u psychologa "
        "i konsultację psychoterapeutyczną w Reha Medica.", "faq/", extra_ld=ld) + f"""
<body class="no-hero">
<a class="skip-link" href="#main">Przejdź do treści</a>
{sprite()}
{header(depth, active="faq")}
<main id="main">
<section class="plain">
  <div class="wrap plain__head">
    <nav class="ubread" aria-label="Ścieżka nawigacji"><ol class="ubread__list">
      <li><a href="{r}index.html">Strona główna</a></li><li><span aria-current="page">FAQ</span></li>
    </ol></nav>
    <h1 class="plain__h">Najczęstsze pytania</h1>
    <p class="plain__lead">Cztery pytania, które pacjenci zadają najczęściej, zanim umówią pierwszą wizytę.</p>
  </div>
  <div class="wrap qa__list">
{poz}
  </div>
  <p class="wrap plain__note">Nie znalazłeś odpowiedzi? <a href="{r}kontakt/">Zadzwoń do recepcji</a> — nie trzeba wiedzieć, o co zapytać.</p>
</section>
</main>
{footer(depth)}
{tail(depth)}"""
    BUILT.append(write("faq/index.html", html_out))


# ══════════════════════════════════════════════ AKTUALNOŚCI
def build_aktualnosci():
    depth = 1; r = rel(depth)
    poz = "\n".join(f"""        <article class="post">
          <p class="post__meta"><span class="post__cat">{a['kat']}</span>
            <time datetime="{a['data']}">{a['data_txt']}</time></p>
          <h2 class="post__t"><a href="{r}aktualnosci/{a['slug']}/">{a['t']}</a></h2>
          <p class="post__lead">{a['lead']}</p>
        </article>""" for a in AKTUALNOSCI)
    ld = [breadcrumb_ld([("Strona główna", BASE + "/"), ("Aktualności", None)])]
    html_out = head(depth, "Aktualności — Reha Medica Psychoterapia",
        "Projekty i wydarzenia dotyczące opieki psychologicznej i psychoterapeutycznej "
        "Reha Medica, w tym projekt MINDSpots.", "aktualnosci/", extra_ld=ld) + f"""
<body class="no-hero">
<a class="skip-link" href="#main">Przejdź do treści</a>
{sprite()}
{header(depth, active="aktualnosci")}
<main id="main">
<section class="plain">
  <div class="wrap plain__head">
    <nav class="ubread" aria-label="Ścieżka nawigacji"><ol class="ubread__list">
      <li><a href="{r}index.html">Strona główna</a></li><li><span aria-current="page">Aktualności</span></li>
    </ol></nav>
    <h1 class="plain__h">Aktualności</h1>
    <p class="plain__lead">Projekty i wydarzenia dotyczące opieki psychologicznej w Reha Medica.</p>
  </div>
  <div class="wrap post__list">
{poz}
  </div>
</section>
</main>
{footer(depth)}
{tail(depth)}"""
    BUILT.append(write("aktualnosci/index.html", html_out))


def build_wpis(a):
    depth = 2; r = rel(depth)
    kanoniczny = MAIN + a["zrodlo"]
    ld = [breadcrumb_ld([("Strona główna", BASE + "/"),
                         ("Aktualności", f"{BASE}/aktualnosci/"), (a["t"], None)])]
    o = head(depth, f"{a['t']} — Reha Medica Psychoterapia", a["lead"],
             f"aktualnosci/{a['slug']}/", extra_ld=ld)
    # ta sama treść żyje na obu domenach (potw. klienta #2) — canonical wskazuje źródło
    o = o.replace(f'<link rel="canonical" href="{BASE}/aktualnosci/{a["slug"]}/">',
                  f'<link rel="canonical" href="{kanoniczny}">')
    html_out = o + f"""
<body class="no-hero">
<a class="skip-link" href="#main">Przejdź do treści</a>
{sprite()}
{header(depth, active="aktualnosci")}
<main id="main">
<section class="plain">
  <div class="wrap plain__head">
    <nav class="ubread" aria-label="Ścieżka nawigacji"><ol class="ubread__list">
      <li><a href="{r}index.html">Strona główna</a></li>
      <li><a href="{r}aktualnosci/">Aktualności</a></li>
      <li><span aria-current="page">{a['t'][:40]}…</span></li>
    </ol></nav>
    <p class="post__meta"><span class="post__cat">{a['kat']}</span>
      <time datetime="{a['data']}">{a['data_txt']}</time></p>
    <h1 class="plain__h">{a['t']}</h1>
    <p class="plain__lead">{a['lead']}</p>
  </div>
  <div class="wrap plain__body">
    <p>Pełna treść tego wpisu prowadzona jest w serwisie Reha Medica — ta sama treść na dwóch
    domenach byłaby duplikatem, dlatego adres kanoniczny wskazuje serwis główny.</p>
    <a class="btn btn--brand" href="{kanoniczny}" rel="noopener">Czytaj w serwisie Reha Medica
      <span class="btn__arrow" aria-hidden="true">&rarr;</span></a>
  </div>
  <p class="wrap plain__note"><a href="{r}aktualnosci/">&larr; Wszystkie aktualności</a></p>
</section>
</main>
{footer(depth)}
{tail(depth)}"""
    BUILT.append(write(f"aktualnosci/{a['slug']}/index.html", html_out))


build_faq()
build_aktualnosci()
for _a in AKTUALNOSCI:
    build_wpis(_a)
