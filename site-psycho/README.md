# Reha Medica Psychoterapia — serwis

Osobna witryna dla psychologii, psychoterapii i psychiatrii, wydzielona z serwisu głównego
zgodnie z regułą wykluczenia w `CLAUDE.md` i potwierdzeniami klienta z 2026-07-14 i 2026-07-19.

Statyczny HTML/CSS/JS, bez frameworka i bez builda — tak jak serwis główny.

## Uruchomienie lokalne

```
python3 -m http.server 8932 --directory site-psycho
```
Serwis: http://localhost:8932/

## Generatory

Serwis jest generowany — źródła w `_build/`:
`build_psycho_data.py` (dane + teksty) · `build_psycho_pages.py` (strony) · `patch_js.py` (JS).
Przebudowa: `python3 _build/build_psycho_pages.py && python3 _build/patch_js.py`
(przed `patch_js.py` skopiuj świeży `site/js/main.js` — patch jest jednorazowy).

## Struktura

```
/                                                  strona główna
/poradnia-psychologiczna/                          usługa (ogólna)
/osrodek-psychologiczno-psychoterapeutyczny/       usługa (ogólna)
/konsultacje-psychologiczne/                       usługa (ogólna)
/konsultacja-psychoterapeutyczna/                  usługa (ogólna)
/lekarz-psychiatra/                                usługa (ogólna)
/<miasto>/                                         hub placówki
/<miasto>/poradnia-psychologiczna/                 miasto × usługa
/<miasto>/osrodek-psychologiczno-psychoterapeutyczny/
/szczecinek/konsultacje-psychologiczne/
/placowki/  /kontakt/  /404.html
```

Miasta: `szczecinek` · `szczecin` · `walcz` · `bialogard` · `bobolice`.

**URL-e nie są dowolne.** Wynikają wprost z `working-docs/stage-5-redirects.csv` — mapa 26 przekierowań
301 z serwisu głównego już na nie wskazuje. Zmiana adresu = zerwane przekierowanie.

## Ikony

11 ikon pochodzi z projektu Claude Design **„Ikony Psychoterapia v4"**
(`claude.ai/design/p/fe0f3c94-9ed4-404d-8fb8-23ffcad46caf`), materiał klienta.

- `_build/icons-source.html` — kopia robocza ze źródła (nie edytować ręcznie),
- `_build/extract_icons.py` — wyciąga i przemapowuje kolory,
- `assets/icons-psycho.json` — wynik: 11 symboli + etykiety,
- `css/psycho.css` — warstwa prezentacji.

Kolory oryginału zamieniono na tokeny, więc ikona dziedziczy paletę serwisu:
`stroke/fill #3B4133 → currentColor` · `blob #EBE8DC → var(--ico-blob)`.
Konstrukcje edytora (`<sc-if>`, `{{ }}`) usunięte.

Symbole są **wstrzykiwane per strona** — każda dostaje tylko te, których używa
(strona główna 11, strona usługi 1, hub miasta 5). Zero dodatkowych żądań.

| Ikona | Gdzie |
|---|---|
| 5 ikon usług | indeks „Formy opieki", nagłówek dostępności na stronie usługi, listy usług w hubach miast |
| 6 ikon „momentów" | sekcja „W jakich momentach psychoterapia może pomóc" na stronie głównej |

Sekcja „momentów" jest **statyczna — bez efektów najechania** (decyzja właściciela 2026-07-31).
Zostaje wyłącznie wskaźnik fokusu z globalnej reguły `a:focus-visible`, wymagany przez WCAG 2.2 AA.
Nazwa usługi docelowej siedzi w `.visually-hidden` — czytnik ekranu ją ogłasza, wizualnie jej nie ma.

## Typografia — jedyne rozejście z serwisem głównym

| | serwis główny | tutaj |
|---|---|---|
| display | Instrument Serif 400 | **EB Garamond** 400–600 (zmienny) |
| tekst | Source Sans 3 | **Karla** 400–700 (zmienny) |

Kroje z projektu klienta „Ikony Psychoterapia v4", pobrane z Google Fonts (OFL), self-hostowane
i zsubsetowane `pyftsubset` do łaciny + polskich diakrytyków (`_build/` zawiera zakresy).
Razem 76 KB. **Kolorystyka jest identyczna z serwisem głównym** — decyzja właściciela
2026-08-01: „fonty mogą być inne, kolorystyka ta sama".

## Fundamenty wizualne

Przeniesione 1:1 z serwisu głównego: `css/style.css`, `css/usluga.css`, fonty self-hosted
(Instrument Serif + Source Sans 3, zsubsetowane pod polskie diakrytyki), logotyp, paleta
ciepłego brązu, siatka 1180 px, menu dostępności WCAG.

Odstępstwa od serwisu głównego (świadome):
- `.hcard__foot[hidden]{display:none}` — dodana reguła; karta placówek startuje bez CTA.
- mobilny obrazek hero w media query → `hero-0-wsparcie-m.webp`.

## Różnice w `js/main.js` względem serwisu głównego

Plik jest kopią `site/js/main.js` z czterema zmianami (skrypt: ``_build/patch_js.py``):

1. `window.RM_SEARCH` — indeks wyszukiwarki wygenerowany z 24 stron tego serwisu.
2. Link „Przejdź do placówki" buduje `/<miasto>/`, nie `/placowki/<miasto>/`.
3. **Brak preselekcji placówki.** Karta startuje pusta, stopka z CTA ukryta do wyboru miasta.
   Serwis główny ma tu świadome nadpisanie właściciela (2026-07-27) — tutaj go nie ma,
   więc obowiązuje reguła `CLAUDE.md` „No facility may be preselected".
4. Rotator usług zasilony 5 usługami psychologicznymi; martwy rotator konsultacji usunięty.

Moduły nieużywane w tym serwisie (newsletter, opinie Google, ankieta) same się wyłączają —
każdy kończy działanie, gdy nie znajdzie swojego węzła w DOM.

## ⚠ PLACEHOLDERY — do podmiany przed publikacją

| Co | Gdzie | Blokada |
|---|---|---|
| **Domena** `https://psychoterapia.rehamedica.info.pl` | canonical, OG, `sitemap.xml`, `robots.txt`, schema | **P1** — klient nie podał domeny. Jedna stała `BASE` w `_build/build_psycho_data.py`. |
| **Polityka prywatności / standardy ochrony małoletnich** | stopka — linki prowadzą na serwis główny | **P10/P11** — nierozstrzygnięty podmiot prawny. |

## Czego tu celowo NIE MA

Nie zbudowano, bo brak źródła lub decyzji — nie wolno zmyślać:

- **cennik** — źródło nie zawiera żadnych kwot,
- **sylwetki specjalistów** — źródło nie zawiera nazwisk; brak schema `Physician`,
- **opinie pacjentów** — brak źródła dla tego serwisu,
- **aktualności / newsletter** — decyzja klienta otwarta (P9),
- **godziny przyjęć poradni** — w źródle są tylko godziny globalne 8–19 / sob. 8–18 (P6),
- **NFZ per usługa** — źródło potwierdza wyłącznie: Ośrodek = bezpłatny, psychiatra = komercyjnie.
