# -*- coding: utf-8 -*-
"""Dostrojenie js/main.js do serwisu psychoterapeutycznego."""
import os, re, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_psycho_data import SERVICES, SERVICE_ORDER, CITIES, FAC

OUT = "/Users/maksymzabavchuk/Desktop/rehamedica-projekt/site-psycho"
JS = os.path.join(OUT, "js/main.js")
src = open(JS, encoding="utf-8").read()

# ── 1. indeks wyszukiwarki: zbudowany z realnych stron tego serwisu
def meta(path, name):
    h = open(os.path.join(OUT, path), encoding="utf-8").read()
    t = re.search(r"<title>(.*?)</title>", h, re.S).group(1).strip()
    d = re.search(r'<meta name="description" content="(.*?)">', h, re.S)
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', h, re.S)
    h1 = re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else ""
    return {"u": name, "t": h1 or t.split("—")[0].strip(), "c": CAT.get(name, "Serwis"),
            "k": (t + " " + (d.group(1) if d else "")).strip()}

CAT = {"": "Strona główna", "placowki/": "Placówki", "kontakt/": "Kontakt"}
for s in SERVICE_ORDER: CAT[s + "/"] = "Usługi"
for c in CITIES:
    CAT[c + "/"] = "Placówki"
    for s in SERVICE_ORDER:
        CAT[f"{c}/{s}/"] = FAC[c]["name"]

entries = [meta("index.html", "")]
for s in SERVICE_ORDER: entries.append(meta(f"{s}/index.html", s + "/"))
entries.append(meta("placowki/index.html", "placowki/"))
entries.append(meta("kontakt/index.html", "kontakt/"))
for c in CITIES:
    entries.append(meta(f"{c}/index.html", c + "/"))
    for s in SERVICE_ORDER:
        p = f"{c}/{s}/index.html"
        if os.path.exists(os.path.join(OUT, p)):
            entries.append(meta(p, f"{c}/{s}/"))

new_idx = "window.RM_SEARCH=" + json.dumps(entries, ensure_ascii=False, separators=(",", ":")) + ";"
src, n = re.subn(r"window\.RM_SEARCH=\[.*?\];", lambda m: new_idx, src, count=1, flags=re.S)
assert n == 1, "nie podmieniono indeksu wyszukiwarki"

# ── 2. link „Przejdź do placówki": serwis psycho ma /<miasto>/, nie /placowki/<miasto>/
old_link = "see.setAttribute('href', linkPrefix + 'placowki/' + slugMiasta + '/');"
assert old_link in src, "nie znaleziono budowania linku placówki"
src = src.replace(old_link, "see.setAttribute('href', linkPrefix + slugMiasta + '/');")
src = src.replace(
    "      // Szczecinek = centrala: /placowki/szczecinek/ jest przekierowaniem 301 na stronę główną.\n",
    "      // Serwis psychoterapeutyczny: strona placówki leży pod /<miasto>/ (zgodnie z mapą 301).\n")

# ── 3. ZERO preselekcji placówki (reguła CLAUDE.md; brak nadpisania właściciela dla tego serwisu)
old_def = "var domyslna = card.getAttribute('data-fac-default') || 'szczecinek';"
assert old_def in src, "nie znaleziono domyślnej placówki"
src = src.replace(old_def,
    "// Serwis psychoterapeutyczny: ŻADNA placówka nie jest preselektowana (reguła CLAUDE.md).\n"
    "  // Karta startuje w stanie pustym — pacjent musi świadomie wskazać miasto.\n"
    "  var domyslna = card.getAttribute('data-fac-default');")
old_init = "var initial = tabs.filter(function (t) { return t.dataset.fac === domyslna; })[0] || tabs[0];"
assert old_init in src
src = src.replace(old_init,
    "var initial = domyslna ? tabs.filter(function (t) { return t.dataset.fac === domyslna; })[0] : null;")

# ── 4. rotator usług: dane serwisu psychoterapeutycznego
svc_data = ",\n".join(
    "      { t: %s, d: %s, h: %s }" % (json.dumps(SERVICES[s]["title"], ensure_ascii=False),
                                      json.dumps(SERVICES[s]["lead"], ensure_ascii=False),
                                      json.dumps(s + "/", ensure_ascii=False))
    for s in SERVICE_ORDER)
src, n = re.subn(
    r"(item: '\.svc__item'.*?data: \[)(.*?)(\n    \]\n  \}\);)",
    lambda m: m.group(1) + "\n" + svc_data + m.group(3), src, count=1, flags=re.S)
assert n == 1, "nie podmieniono danych rotatora usług"

# ── 5. rotator konsultacji nie istnieje w tym serwisie — usuwamy martwe dane
src, n = re.subn(r"\n  rotator\(\{\n    item: '\.kons__row'.*?\n    \]\n  \}\);\n", "\n", src, count=1, flags=re.S)
print("rotator konsultacji usunięty:", bool(n))

# ── 6. karuzela opinii Google: brak źródła dla serwisu psycho — moduł wyłączony
src = src.replace("fetch('data/reviews.json')", "fetch('data/reviews.json'/* brak danych dla serwisu psycho */)")

open(JS, "w", encoding="utf-8").write(src)
print(f"main.js: {len(entries)} pozycji w indeksie wyszukiwarki, {len(src.splitlines())} linii")

# ── 7. pusty stan karty: bez preselekcji CTA „Umów wizytę" prowadziłoby do href="#".
#      Stopkę karty odsłaniamy dopiero po wskazaniu miasta.
src = open(JS, encoding="utf-8").read()
old = "    if (empty) empty.hidden = true;\n    detail.hidden = false;"
assert old in src, "nie znaleziono odsloniecia detalu"
src = src.replace(old, old + "\n    var foot = card.querySelector('.hcard__foot');\n    if (foot) foot.hidden = false;")
old2 = "  var initial = domyslna ? tabs.filter(function (t) { return t.dataset.fac === domyslna; })[0] : null;"
assert old2 in src
src = src.replace(old2,
  "  var foot0 = card.querySelector('.hcard__foot');\n"
  "  if (foot0) foot0.hidden = true;   // dopóki nie wybrano miasta — brak przycisku donikąd\n"
  + old2)
open(JS, "w", encoding="utf-8").write(src)
print("karta placówek: stopka ukryta w stanie pustym")
