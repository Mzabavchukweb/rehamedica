# -*- coding: utf-8 -*-
"""
Wyciąga 11 ikon z projektu Claude Design „Ikony Psychoterapia v4.dc.html"
i zapisuje je jako symbole SVG w palecie serwisu.

Źródło: claude.ai/design/p/fe0f3c94-9ed4-404d-8fb8-23ffcad46caf
Kolory oryginału → tokeny serwisu:
  stroke #3B4133  → currentColor        (dziedziczy --color-brand #483d32)
  fill   #3B4133  → currentColor
  blob   #EBE8DC  → var(--ico-blob)     (domyślnie --color-bg-beige-2 #ece4d7)
Konstrukcje narzędzia (<sc-if>, {{ }}) usunięte — blob renderowany zawsze (default true).
"""
import re, json, os

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons-source.html")
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "icons-psycho.json")

# etykieta z projektu -> id symbolu w serwisie
IDS = {
    "Kryzys i trudne momenty":        "p-kryzys",
    "Przeciążenie i napięcie":        "p-napiecie",
    "Trudne emocje":                  "p-emocje",
    "Relacje, które bolą":            "p-relacje",
    "Lepsze zrozumienie siebie":      "p-zrozumienie",
    "Zmiana jakości życia":           "p-jakosc-zycia",
    "Ośrodek dla Dzieci i Młodzieży": "p-osrodek",
    "Poradnia psychologiczna":        "p-poradnia",
    "Konsultacja psychoterapeutyczna":"p-psychoterapeutyczna",
    "Konsultacje psychologiczne":     "p-konsultacje",
    "Lekarz psychiatra":              "p-psychiatra",
}

src = open(SRC, encoding="utf-8").read()

# każda kafelka: <svg …>…</svg> … <p …>ETYKIETA</p>
pat = re.compile(r'(<svg viewBox="0 0 200 200".*?</svg>).*?<p style="[^"]*">([^<]+)</p>', re.S)
found = pat.findall(src)
assert len(found) == 11, f"oczekiwano 11 ikon, znaleziono {len(found)}"

def clean(svg):
    # zdejmij powłokę <svg> — zostaje sama zawartość do <symbol>
    body = re.sub(r'^<svg[^>]*>', '', svg).replace('</svg>', '')
    # <sc-if> to konstrukcja edytora; default true → zostawiamy zawartość
    body = re.sub(r'<sc-if[^>]*>', '', body)
    body = body.replace('</sc-if>', '')
    # paleta → tokeny
    body = body.replace('fill:#EBE8DC', 'fill:var(--ico-blob,#ece4d7)')
    body = body.replace('stroke:#3B4133', 'stroke:currentColor')
    body = body.replace('fill:#3B4133', 'fill:currentColor')
    assert '#3B4133' not in body and '#EBE8DC' not in body, "został niezmapowany kolor"
    assert '{{' not in body, "został placeholder szablonu"
    return re.sub(r'\n\s*', '\n      ', body).strip()

icons, labels = {}, {}
for svg, label in found:
    label = label.strip()
    assert label in IDS, f"nieznana etykieta: {label}"
    icons[IDS[label]] = clean(svg)
    labels[IDS[label]] = label

assert len(icons) == 11, "duplikat etykiety"
json.dump({"icons": icons, "labels": labels}, open(OUT, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(f"wyciagnieto {len(icons)} ikon -> {OUT}")
for k, v in labels.items():
    print(f"  {k:24s} {v}")
