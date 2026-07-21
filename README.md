# Reha Medica — strona internetowa

Statyczna strona Centrum Rehabilitacyjno-Medycznego Reha Medica (Pomorze Zachodnie):
pięć placówek, usługi rehabilitacji, fizjoterapii, konsultacji, zabiegów i odnowy
biologicznej, aktualności, projekty UE, FAQ, ankieta satysfakcji pacjenta.

## Struktura
- `site/` — gotowa strona (HTML/CSS/JS, bez frameworka i bez builda).
- `site/_redirects` — reguły przekierowań (Cloudflare Pages).
- `working-docs/` — dokumenty robocze migracji (audyty, matryce, mapa URL, DO POTWIERDZENIA).
- `reviews/` — raporty audytów (UI/UX, WCAG, źródło vs treść).

## Uruchomienie lokalne
```
cd site && python3 -m http.server 8931
```
Strona: http://localhost:8931/

## Uwaga
Prywatne archiwum źródłowe starej strony oraz dane dostępowe są celowo poza repozytorium.
