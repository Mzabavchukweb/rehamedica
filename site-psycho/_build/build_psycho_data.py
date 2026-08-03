# -*- coding: utf-8 -*-
"""
Reha Medica Psychoterapia — DANE
Wszystkie fakty pochodzą z rehamedica-source-archive/. Teksty miastowe są PARAFRAZAMI
źródła (zgoda właściciela 2026-07-31, P3) — zmieniona jest wyłącznie forma, nie fakty.
"""

# PLACEHOLDER — P1 nierozstrzygnięte. Jedna stała do podmiany po podaniu domeny.
BASE = "https://psychoterapia.rehamedica.info.pl"
MAIN = "https://rehamedica.info.pl"

FAC = {
    "szczecinek": dict(
        name="Szczecinek", addr="ul. Kościuszki 57", zip="78-400",
        phones=[("94 372 14 51", "+48943721451"), ("606 965 904", "+48606965904")],
        email="szczecinek@rehamedica.info.pl",
        geo=(53.7144296471185, 16.673845677089723),
        rola="centrala",
    ),
    "szczecin": dict(
        name="Szczecin", addr="ul. Wyszyńskiego 32-34", zip="78-411",
        phones=[("530 661 982", "+48530661982")],
        email="szczecin@rehamedica.info.pl", geo=None, rola=None,
    ),
    "walcz": dict(
        name="Wałcz", addr="ul. Gen. Andersa 9", zip="78-600",
        phones=[("530 661 982", "+48530661982")],
        email="walcz@rehamedica.info.pl",
        geo=(53.26547900926746, 16.45704149395885), rola=None,
    ),
    "bialogard": dict(
        name="Białogard", addr="ul. Najświętszej Marii Panny 19", zip="78-200",
        phones=[("535 960 018", "+48535960018")],
        email="bialogard@rehamedica.info.pl", geo=None, rola=None,
    ),
    "bobolice": dict(
        name="Bobolice", addr="ul. Reymonta 2", zip="76-020",
        phones=[("530 645 059", "+48530645059")],
        email="koszalin@rehamedica.info.pl",
        geo=(53.953400029128815, 16.581402877100796), rola=None,
    ),
}
CITIES = ["szczecinek", "szczecin", "walcz", "bialogard", "bobolice"]

# Usługa -> placówki, w których źródło ją potwierdza. NIE dopisujemy miast.
SERVICES = {
    "poradnia-psychologiczna": dict(
        title="Poradnia psychologiczna",
        short="Poradnia psychologiczna",
        lead="Diagnoza i terapia dla dorosłych, młodzieży, dzieci, rodzin i par.",
        img="poradnia-hero.webp",
        band="poradnia-band.webp",
        cities=CITIES,
        fin="DO POTWIERDZENIA",
    ),
    "osrodek-psychologiczno-psychoterapeutyczny": dict(
        title="Ośrodek psychologiczno-psychoterapeutyczny",
        short="Ośrodek dla dzieci i młodzieży",
        lead="Bezpłatna pomoc psychologiczna i psychoterapeutyczna dla dzieci, młodzieży i ich rodzin.",
        img="osrodek-hero.webp",
        band="osrodek-band.webp",
        cities=CITIES,
        fin="bezpłatnie",
    ),
    "konsultacje-psychologiczne": dict(
        title="Konsultacje psychologiczne",
        short="Konsultacje psychologiczne",
        lead="Pierwsze spotkanie z psychologiem — rozeznanie sytuacji i nazwanie trudności.",
        img="konsultacja-psychologiczna.webp",
        band=None,
        cities=["szczecinek"],
        fin="DO POTWIERDZENIA",
    ),
    "konsultacja-psychoterapeutyczna": dict(
        title="Konsultacja psychoterapeutyczna",
        short="Konsultacja psychoterapeutyczna",
        lead="Rozpoznanie potrzeb, ustalenie celów terapii i sprawdzenie, czy możecie razem pracować.",
        img="konsultacja-psychoterapeutyczna.webp",
        band=None,
        cities=[],          # źródło nie wskazuje miasta — DO POTWIERDZENIA
        fin="DO POTWIERDZENIA",
    ),
    "lekarz-psychiatra": dict(
        title="Lekarz psychiatra",
        short="Lekarz psychiatra",
        lead="Diagnostyka i leczenie zaburzeń psychicznych. Pacjenci od 14. roku życia.",
        img="psychiatra.webp",
        band=None,
        cities=[],          # źródło nie wskazuje miasta — DO POTWIERDZENIA
        fin="komercyjnie",
    ),
}
SERVICE_ORDER = [
    "poradnia-psychologiczna",
    "osrodek-psychologiczno-psychoterapeutyczny",
    "konsultacje-psychologiczne",
    "konsultacja-psychoterapeutyczna",
    "lekarz-psychiatra",
]

# ══════════════════════════════════════════════════════════════════════════════
# TREŚĆ OGÓLNA USŁUG — parafraza źródła, fakty bez zmian
# ══════════════════════════════════════════════════════════════════════════════

PORADNIA_OGOLNA = dict(
    kicker="Dla kogo",
    lead="W poradni psychologicznej Reha Medica oferujemy kompleksowe wsparcie psychologiczne "
         "i psychoterapeutyczne dla osób dorosłych, młodzieży, dzieci, rodzin oraz par.",
    body=[
        "Psycholodzy i psychoterapeuci wykonują zadania diagnostyczne i terapeutyczne, kontynuują "
        "opiekę psychologiczną pacjentów po zakończonej hospitalizacji, a także otaczają nią dzieci "
        "i młodzież oraz ich rodziców.",
        "W poradni psychologicznej mają Państwo możliwość uzyskania pomocy w przypadkach kryzysu "
        "emocjonalnego spowodowanego sytuacją osobistą lub zawodową, problemami rodzinnymi czy "
        "utratą osoby bliskiej.",
        "Dodatkowo nasi terapeuci oferują wsparcie wychowawcze, a także porady psychologiczne dla "
        "rodziców dzieci sprawiających trudności wychowawcze.",
    ],
    pull_q="Zespół specjalistów pracujących w naszych poradniach to wykwalifikowani psychologowie "
           "i psychoterapeuci z dużym doświadczeniem klinicznym.",
    pull_p=[
        "W przypadkach zaburzeń zdiagnozowanych przez lekarza neurologa lub lekarza psychiatrę "
        "pacjent kierowany jest do psychologa celem przeprowadzenia całościowej diagnozy "
        "neuropsychologicznej.",
    ],
    parts_h="Diagnoza i terapia neuropsychologiczna",
    parts=[
        "<b>Diagnoza neuropsychologiczna</b> to pełna ocena sprawności poznawczej — m.in. uwagi, "
        "funkcji mnestycznych, językowych, wykonawczych i wzrokowo-przestrzennych — u pacjentów po "
        "przebytych udarach mózgu, urazach mózgowych i zabiegach neurochirurgicznych. Obejmuje "
        "również diagnozę różnicową otępienia.",
        "<b>Terapia neuropsychologiczna</b> dedykowana jest pacjentom z różnego rodzaju deficytami "
        "poznawczo-emocjonalnymi powstałymi w następstwie przebytych udarów mózgu, urazów mózgowych, "
        "po zabiegach neurochirurgicznych oraz w przebiegu chorób neurodegeneracyjnych.",
    ],
    coda_lead=None, coda_p=None,
)

OSRODEK_OGOLNY = dict(
    kicker="Dla kogo",
    lead="Ośrodek Środowiskowej Opieki Psychologicznej i Psychoterapeutycznej dla Dzieci "
         "i Młodzieży oferuje bezpłatną pomoc psychologiczną i psychoterapeutyczną.",
    body=[
        "Z pomocy ośrodka korzystają dzieci poniżej 7. roku życia, dzieci i młodzież objęte "
        "obowiązkiem szkolnym — do 21. roku życia — oraz rodziny i opiekunowie prawni.",
        "W ramach ośrodka realizowane są porady i diagnoza psychologiczna, psychoterapia "
        "indywidualna i grupowa, psychoterapia rodzinna oraz wsparcie psychospołeczne.",
    ],
    pull_q="Najmłodsi pacjenci otrzymają kompleksową opiekę wykwalifikowanej kadry: psychologa "
           "klinicznego, terapeuty środowiskowego i psychoterapeutów.",
    pull_p=[],
    parts_h=None, parts=[],
    coda_lead=None, coda_p=None,
)

KONS_PSYCHOL = dict(
    kicker="Czemu służą",
    lead="Czemu służą konsultacje psychologiczne?",
    body=[
        "Spotkania z psychologiem mają kilka celów. Pierwszym z nich jest rozeznanie Twojej obecnej "
        "sytuacji życiowej, identyfikacja problemów i ich wpływu na Twoje życie.",
        "Czasami możesz mieć problem z określeniem źródła czy natury Twoich trudności. Nie martw "
        "się — w takiej sytuacji specjalista poprzez odpowiednie pytania pomoże Ci to określić.",
    ],
    pull_q=None, pull_p=[],
    parts_h=None, parts=[],
    coda_lead=None, coda_p=None,
)

KONS_PSYCHOTER = dict(
    kicker="Czemu służą",
    lead="Celem konsultacji psychoterapeutycznej jest rozpoznanie potrzeb pacjenta i zrozumienie "
         "natury zgłaszanych problemów.",
    body=[
        "Po zebraniu wywiadu i postawieniu wstępnej diagnozy terapeuta wraz z pacjentem określają "
        "cele i oczekiwania, które mają się zrealizować dzięki podjęciu terapii. Ważne, aby cele "
        "były jasno określone oraz dotyczyły tych aspektów funkcjonowania, które mają zostać "
        "uzdrowione w procesie terapii.",
    ],
    pull_q="Oprócz zbierania informacji formalnych oraz rozeznania przeżyć wewnętrznych pacjenta, "
           "istotnym elementem konsultacji terapeutycznych jest zbadanie gotowości do podjęcia terapii.",
    pull_p=[
        "Dla pacjenta jest to temat istotny, dotyczy bowiem motywacji do rozpoczęcia terapii. "
        "Najczęściej mowa o tzw. motywacji zewnętrznej i wewnętrznej.",
        "Zewnętrzna motywacja do leczenia to sytuacja, kiedy osoba chce się go podjąć, ponieważ "
        "ktoś bliski ją do tego namawia lub decydują o tym inne czynniki zewnętrzne — np. podjęcie "
        "terapii, żeby być bardziej wydajnym w pracy.",
        "Wewnętrzna motywacja to taki rodzaj przeżycia, który wiąże się z wewnętrzną potrzebą "
        "pacjenta i jest niezależna od zmieniających się czynników zewnętrznych.",
    ],
    parts_h="Czy Klient i Terapeuta mogą ze sobą pracować",
    parts=[
        "Celem konsultacji psychoterapeutycznej jest także sprawdzenie, czy Klient i Terapeuta mogą "
        "ze sobą pracować. Psychoterapia to budowanie relacji, w której ważne jest, aby Klient czuł "
        "się bezpieczny i akceptowany.",
        "Czasem zdarza się tak, że dany Terapeuta nie pasuje Klientowi. Konsultacja "
        "psychoterapeutyczna to dobry czas na sprawdzenie tego i dokonanie zmiany.",
    ],
    coda_lead=None, coda_p=None,
)

PSYCHIATRA = dict(
    kicker="Kiedy zgłosić się",
    lead="Zaburzenia nastroju, smutek, niekontrolowane napady agresji, apatia, omamy wzrokowe "
         "i słuchowe, napady lęku — to tylko niektóre z objawów, które mogą świadczyć "
         "o rozwijających się zaburzeniach psychicznych.",
    body=[
        "Przyczyny zaburzeń psychicznych mogą być różne — zarówno biologiczne, psychologiczne, jak "
        "i środowiskowe. Niektóre z nich posiadają potencjalne podłoże genetyczne, a inne mają swoje "
        "źródła w przeżytych traumach, w braku równowagi biochemicznej w mózgu bądź nadużywaniu "
        "środków psychoaktywnych.",
    ],
    pull_q="Pierwsza wizyta u psychiatry ma charakter diagnostyczny i trwa dłużej niż późniejsze, "
           "regularne wizyty kontrolne.",
    pull_p=[
        "Najczęściej już po pierwszym spotkaniu lekarz psychiatra formułuje wstępne zalecenia "
        "i planuje przebieg leczenia.",
    ],
    parts_h="Nie lekceważ objawów",
    parts=[
        "Jeśli zauważasz u siebie lub swoich bliskich któreś z tych zachowań, nie lekceważ ich. "
        "Zadbaj o zdrowie psychiczne swoje i swoich bliskich.",
    ],
    coda_lead="W Grupie Medycznej Reha Medica do lekarza psychiatry zapraszamy pacjentów od 14. roku życia.",
    coda_p="Wsparcie lekarza psychiatry realizowane jest na zasadach komercyjnych (odpłatnie).",
)

SERVICE_CONTENT = {
    "poradnia-psychologiczna": PORADNIA_OGOLNA,
    "osrodek-psychologiczno-psychoterapeutyczny": OSRODEK_OGOLNY,
    "konsultacje-psychologiczne": KONS_PSYCHOL,
    "konsultacja-psychoterapeutyczna": KONS_PSYCHOTER,
    "lekarz-psychiatra": PSYCHIATRA,
}

# ══════════════════════════════════════════════════════════════════════════════
# TREŚĆ MIASTOWA — PARAFRAZY. Każde miasto ma własne brzmienie, te same fakty.
# Zgoda właściciela P3 (2026-07-31): wolno zmieniać formę, nie wolno dopisywać faktów.
# ══════════════════════════════════════════════════════════════════════════════

PORADNIA_MIASTA = {
"szczecinek": dict(
  lead="Poradnia psychologiczna w Szczecinku prowadzi diagnozę i terapię dla osób dorosłych, "
       "młodzieży, dzieci, a także dla rodzin i par.",
  body=[
    "Praca psychologów i psychoterapeutów obejmuje dwa nurty: zadania diagnostyczne oraz "
    "prowadzenie terapii. Pacjenci, którzy zakończyli hospitalizację, kontynuują tutaj rozpoczętą "
    "wcześniej opiekę psychologiczną.",
    "Do poradni przy ulicy Kościuszki zgłaszają się osoby przeżywające kryzys emocjonalny. Jego "
    "źródłem bywa sytuacja osobista albo zawodowa, trudności w rodzinie lub utrata kogoś bliskiego.",
    "Osobnym obszarem pracy poradni jest opieka nad dziećmi i młodzieżą — razem z ich rodzicami. "
    "Rodzice dzieci sprawiających trudności wychowawcze mogą liczyć na wsparcie wychowawcze "
    "i poradę psychologiczną.",
  ],
  pull_q="Poradnię tworzą wykwalifikowani psychologowie i psychoterapeuci z dużym doświadczeniem "
         "klinicznym.",
  pull_p=["Jeżeli zaburzenia rozpoznał wcześniej lekarz neurolog albo psychiatra, pacjent trafia do "
          "psychologa na całościową diagnozę neuropsychologiczną."],
  parts_h="Diagnoza i terapia neuropsychologiczna w Szczecinku",
  parts=[
    "<b>Diagnoza neuropsychologiczna</b> obejmuje pełną ocenę sprawności poznawczej: uwagi, funkcji "
    "mnestycznych, językowych, wykonawczych oraz wzrokowo-przestrzennych. Kierujemy ją do pacjentów "
    "po udarach mózgu, urazach mózgowych i zabiegach neurochirurgicznych. Prowadzimy również "
    "diagnozę różnicową otępienia.",
    "<b>Terapia neuropsychologiczna</b> przeznaczona jest dla osób z deficytami "
    "poznawczo-emocjonalnymi — powstałymi po udarze, urazie mózgu lub zabiegu neurochirurgicznym, "
    "a także w przebiegu chorób neurodegeneracyjnych.",
  ],
),
"szczecin": dict(
  lead="W szczecińskiej poradni psychologicznej Reha Medica pracujemy z dorosłymi, z młodzieżą "
       "i z dziećmi, a także z parami oraz całymi rodzinami.",
  body=[
    "Zakres pomocy jest szeroki. Psycholodzy i psychoterapeuci zajmują się zarówno diagnozą, jak "
    "i prowadzeniem terapii, a osoby po zakończonym pobycie w szpitalu mogą u nas kontynuować "
    "rozpoczętą opiekę psychologiczną.",
    "Znaczną część zgłoszeń stanowi kryzys emocjonalny. Wywołuje go sytuacja osobista lub zawodowa, "
    "problem w rodzinie albo odejście bliskiej osoby.",
    "Opiekujemy się też dziećmi i młodzieżą razem z ich rodzicami. Rodzicom dzieci, które sprawiają "
    "trudności wychowawcze, oferujemy poradę psychologiczną oraz wsparcie wychowawcze.",
  ],
  pull_q="W poradni przyjmują wykwalifikowani psychologowie i psychoterapeuci z dużym "
         "doświadczeniem klinicznym.",
  pull_p=["Gdy zaburzenie zdiagnozował wcześniej neurolog lub psychiatra, kolejnym krokiem jest "
          "skierowanie do psychologa na całościową diagnozę neuropsychologiczną."],
  parts_h="Neuropsychologia — diagnoza i terapia",
  parts=[
    "W ramach <b>diagnozy neuropsychologicznej</b> oceniamy całość sprawności poznawczej: uwagę, "
    "funkcje mnestyczne, językowe, wykonawcze i wzrokowo-przestrzenne. Badanie dotyczy pacjentów po "
    "przebytych udarach mózgu, urazach mózgowych oraz po zabiegach neurochirurgicznych, a także "
    "diagnozy różnicowej otępienia.",
    "<b>Terapia neuropsychologiczna</b> — prowadzimy ją u osób, u których po udarze, urazie mózgu lub "
    "zabiegu neurochirurgicznym — albo w przebiegu choroby neurodegeneracyjnej — pojawiły się "
    "deficyty poznawczo-emocjonalne.",
  ],
),
"walcz": dict(
  lead="Poradnia psychologiczna Reha Medica w Wałczu obejmuje wsparciem psychologicznym "
       "i psychoterapeutycznym osoby dorosłe, młodzież, dzieci, rodziny i pary.",
  body=[
    "Specjaliści poradni prowadzą diagnozę oraz terapię. Zapewniają również ciągłość opieki "
    "psychologicznej pacjentom, którzy zakończyli hospitalizację.",
    "Wielu pacjentów zgłasza się w kryzysie emocjonalnym — wywołanym sytuacją osobistą bądź "
    "zawodową, problemami rodzinnymi albo utratą kogoś bliskiego.",
    "Pod opieką poradni pozostają także dzieci i młodzież wraz z rodzicami. Rodzice dzieci "
    "sprawiających trudności wychowawcze otrzymują poradę psychologiczną i wsparcie wychowawcze.",
  ],
  pull_q="Zespół poradni w Wałczu to wykwalifikowani psychologowie i psychoterapeuci z dużym "
         "doświadczeniem klinicznym.",
  pull_p=["Przy zaburzeniach rozpoznanych wcześniej przez lekarza neurologa lub psychiatrę pacjent "
          "kierowany jest do psychologa na całościową diagnozę neuropsychologiczną."],
  parts_h="Diagnoza neuropsychologiczna i terapia po urazach mózgu",
  parts=[
    "<b>Diagnoza neuropsychologiczna</b> to całościowa ocena sprawności poznawczej — uwagi, funkcji "
    "mnestycznych, językowych, wykonawczych i wzrokowo-przestrzennych — u pacjentów po udarach "
    "mózgu, urazach mózgowych oraz zabiegach neurochirurgicznych. Obejmuje też diagnozę różnicową "
    "otępienia.",
    "<b>Terapia neuropsychologiczna</b> adresowana jest do pacjentów z deficytami "
    "poznawczo-emocjonalnymi, które powstały w następstwie udaru, urazu mózgu czy zabiegu "
    "neurochirurgicznego, a także w przebiegu chorób neurodegeneracyjnych.",
  ],
),
"bialogard": dict(
  lead="W Białogardzie prowadzimy poradnię psychologiczną dla pacjentów w każdym wieku — dzieci, "
       "młodzieży i dorosłych, a także dla par oraz rodzin.",
  body=[
    "Psycholodzy i psychoterapeuci pracujący w poradni prowadzą diagnostykę i terapię. Osobom po "
    "zakończonej hospitalizacji zapewniają kontynuację opieki psychologicznej.",
    "Częstym powodem zgłoszenia jest kryzys emocjonalny: trudna sytuacja osobista lub zawodowa, "
    "problemy w rodzinie, śmierć bliskiej osoby.",
    "Opieką obejmujemy również dzieci i młodzież oraz ich rodziców. Kiedy dziecko sprawia trudności "
    "wychowawcze, rodzice mogą skorzystać z porady psychologicznej i wsparcia wychowawczego.",
  ],
  pull_q="Poradnia w Białogardzie opiera się na zespole wykwalifikowanych psychologów "
         "i psychoterapeutów z dużym doświadczeniem klinicznym.",
  pull_p=["Jeśli zaburzenia zdiagnozował wcześniej neurolog albo lekarz psychiatra, pacjent zostaje "
          "skierowany do psychologa na całościową diagnozę neuropsychologiczną."],
  parts_h="Co obejmuje diagnoza i terapia neuropsychologiczna",
  parts=[
    "<b>Diagnoza neuropsychologiczna</b> polega na pełnej ocenie sprawności poznawczej: uwagi, "
    "funkcji mnestycznych, językowych, wykonawczych, wzrokowo-przestrzennych. Kierowana jest do "
    "pacjentów po przebytych udarach mózgu, urazach mózgowych i zabiegach neurochirurgicznych, "
    "a także służy diagnozie różnicowej otępienia.",
    "<b>Terapia neuropsychologiczna</b> dotyczy osób z deficytami poznawczo-emocjonalnymi po "
    "udarach, urazach mózgowych i zabiegach neurochirurgicznych oraz w przebiegu chorób "
    "neurodegeneracyjnych.",
  ],
),
"bobolice": dict(
  lead="Poradnia psychologiczna w Bobolicach zapewnia opiekę psychologiczną i psychoterapeutyczną "
       "dorosłym, młodzieży i dzieciom, a także rodzinom oraz parom.",
  body=[
    "Do zadań psychologów i psychoterapeutów należy diagnostyka oraz prowadzenie terapii. Pacjenci "
    "po zakończonej hospitalizacji kontynuują tu wcześniej rozpoczętą opiekę psychologiczną.",
    "Poradnia pomaga w kryzysie emocjonalnym, którego przyczyną bywa sytuacja osobista albo "
    "zawodowa, problemy rodzinne lub utrata bliskiej osoby.",
    "Zajmujemy się również dziećmi i młodzieżą wraz z rodzicami — w tym poradnictwem dla rodziców "
    "dzieci sprawiających trudności wychowawcze oraz wsparciem wychowawczym.",
  ],
  pull_q="W Bobolicach przyjmują wykwalifikowani psychologowie i psychoterapeuci z dużym "
         "doświadczeniem klinicznym.",
  pull_p=["Kiedy zaburzenia rozpoznał wcześniej lekarz neurolog lub psychiatra, pacjent trafia do "
          "psychologa na całościową diagnozę neuropsychologiczną."],
  parts_h="Diagnoza i terapia neuropsychologiczna",
  parts=[
    "<b>Diagnoza neuropsychologiczna</b> obejmuje ocenę całej sprawności poznawczej — m.in. uwagi "
    "oraz funkcji mnestycznych, językowych, wykonawczych i wzrokowo-przestrzennych — u pacjentów po "
    "udarach mózgu, urazach mózgowych i zabiegach neurochirurgicznych. Obejmuje również diagnozę "
    "różnicową otępienia.",
    "<b>Terapia neuropsychologiczna</b> skierowana jest do pacjentów, u których deficyty "
    "poznawczo-emocjonalne powstały po udarze, urazie mózgu lub zabiegu neurochirurgicznym, bądź "
    "rozwijają się w przebiegu chorób neurodegeneracyjnych.",
  ],
),
}

OSRODEK_MIASTA = {
"szczecinek": dict(
  lead="Ośrodek Środowiskowej Opieki Psychologicznej i Psychoterapeutycznej dla Dzieci i Młodzieży "
       "w Szczecinku prowadzi bezpłatną pomoc psychologiczną i psychoterapeutyczną.",
  body=[
    "Z opieki ośrodka korzystają dzieci przed 7. rokiem życia, dzieci i młodzież objęte obowiązkiem "
    "szkolnym — czyli do 21. roku życia — oraz rodziny i opiekunowie prawni.",
    "Zakres pomocy obejmuje porady i diagnozę psychologiczną, psychoterapię indywidualną i grupową, "
    "psychoterapię rodzinną oraz wsparcie psychospołeczne.",
  ],
  pull_q="Najmłodsi pacjenci otrzymują kompleksową opiekę wykwalifikowanej kadry: psychologa "
         "klinicznego, terapeuty środowiskowego i psychoterapeutów.",
),
"szczecin": dict(
  lead="W Szczecinie działa Ośrodek Środowiskowej Opieki Psychologicznej i Psychoterapeutycznej dla "
       "Dzieci i Młodzieży. Pomoc psychologiczna i psychoterapeutyczna jest tu bezpłatna.",
  body=[
    "Ośrodek przyjmuje dzieci poniżej 7. roku życia, dzieci i młodzież objęte obowiązkiem szkolnym "
    "do 21. roku życia, a także rodziny oraz opiekunów prawnych.",
    "W ramach ośrodka prowadzimy porady i diagnozę psychologiczną, psychoterapię indywidualną, "
    "grupową i rodzinną oraz wsparcie psychospołeczne.",
  ],
  pull_q="Opiekę nad najmłodszymi pacjentami sprawuje wykwalifikowana kadra: psycholog kliniczny, "
         "terapeuta środowiskowy i psychoterapeuci.",
),
"walcz": dict(
  lead="Ośrodek Środowiskowej Opieki Psychologicznej i Psychoterapeutycznej dla Dzieci i Młodzieży "
       "w Wałczu udziela bezpłatnej pomocy psychologicznej i psychoterapeutycznej.",
  body=[
    "Pomoc kierujemy do dzieci poniżej 7. roku życia, do dzieci i młodzieży objętych obowiązkiem "
    "szkolnym — do 21. roku życia — oraz do rodzin i opiekunów prawnych.",
    "Ośrodek realizuje porady i diagnozę psychologiczną, psychoterapię indywidualną oraz grupową, "
    "psychoterapię rodzinną i wsparcie psychospołeczne.",
  ],
  pull_q="Kadrę ośrodka tworzą psycholog kliniczny, terapeuta środowiskowy i psychoterapeuci — "
         "najmłodsi pacjenci otrzymują opiekę kompleksową.",
),
"bialogard": dict(
  lead="W Białogardzie Ośrodek Środowiskowej Opieki Psychologicznej i Psychoterapeutycznej dla "
       "Dzieci i Młodzieży zapewnia bezpłatną pomoc psychologiczną i psychoterapeutyczną.",
  body=[
    "Do ośrodka trafiają dzieci przed ukończeniem 7. roku życia, dzieci i młodzież objęte "
    "obowiązkiem szkolnym do 21. roku życia oraz rodziny i opiekunowie prawni.",
    "Prowadzimy porady i diagnozę psychologiczną, psychoterapię indywidualną, psychoterapię grupową "
    "i rodzinną, a także wsparcie psychospołeczne.",
  ],
  pull_q="Wykwalifikowana kadra — psycholog kliniczny, terapeuta środowiskowy i psychoterapeuci — "
         "otacza najmłodszych pacjentów kompleksową opieką.",
),
"bobolice": dict(
  lead="Ośrodek Środowiskowej Opieki Psychologicznej i Psychoterapeutycznej dla Dzieci i Młodzieży "
       "w Bobolicach oferuje bezpłatną pomoc psychologiczną i psychoterapeutyczną.",
  body=[
    "Z ośrodka korzystają dzieci poniżej 7. roku życia, dzieci i młodzież w wieku obowiązku "
    "szkolnego — do 21. roku życia — oraz rodziny i opiekunowie prawni.",
    "W ośrodku realizowane są porady i diagnoza psychologiczna, psychoterapia indywidualna "
    "i grupowa, psychoterapia rodzinna oraz wsparcie psychospołeczne.",
  ],
  pull_q="Najmłodsi pacjenci pozostają pod kompleksową opieką wykwalifikowanej kadry: psychologa "
         "klinicznego, terapeuty środowiskowego i psychoterapeutów.",
),
}

KONS_MIASTA = {
"szczecinek": dict(
  lead="Konsultacje psychologiczne w Szczecinku to pierwszy krok — spotkanie, na którym nazywamy "
       "problem i sprawdzamy, jakiej pomocy potrzebujesz.",
  body=[
    "Spotkania z psychologiem mają kilka celów. Pierwszym jest rozeznanie Twojej obecnej sytuacji "
    "życiowej oraz identyfikacja problemów i ich wpływu na Twoje życie.",
    "Bywa, że trudno samodzielnie wskazać źródło albo naturę własnych trudności. To normalne — "
    "specjalista pomoże Ci je określić, zadając odpowiednie pytania.",
  ],
  pull_q=None, pull_p=[], parts_h=None, parts=[],
),
}

# ══════════════════════════════════════════════════════════════════════════════
# SEKCJE „W jakich momentach psychoterapia może pomóc"
# Etykiety i ikony: projekt klienta „Ikony Psychoterapia v4".
# Opisy i wyliczenia: WYŁĄCZNIE fakty ze źródła (rehamedica-source-archive).
# Zero historii pacjentów — case studies wymagają materiału klienta i zgód (P15).
# ══════════════════════════════════════════════════════════════════════════════

MOMENT_SECTIONS = [
 dict(
  id="kryzys", icon="p-kryzys", target="poradnia-psychologiczna",
  target_label="Poradnia psychologiczna",
  h="Kryzys i trudne momenty",
  lead="Kryzys emocjonalny rzadko przychodzi zapowiedziany. Bywa wywołany sytuacją osobistą albo "
       "zawodową, problemami w rodzinie lub utratą kogoś bliskiego.",
  # Usunięte 2026-08-03 na polecenie właściciela: „W poradni psychologicznej
  # Reha Medica można uzyskać pomoc w każdej z tych sytuacji…". Obietnica pomocy
  # bez ani jednego faktu — konkret niosą znaczniki pod spodem.
  p="",
  list_h="Powody, z którymi tu przychodzą",
  items=["sytuacja osobista", "sytuacja zawodowa", "problemy rodzinne", "utrata osoby bliskiej"],
  src="Poradnia psychologiczna",
 ),
 dict(
  id="napiecie", icon="p-napiecie", target="konsultacje-psychologiczne",
  target_label="Konsultacje psychologiczne",
  h="Przeciążenie i napięcie",
  lead="Czasem wiadomo tylko tyle, że jest ciężko — a źródło i natura trudności pozostają niejasne.",
  p="Pierwsze spotkanie z psychologiem służy rozeznaniu obecnej sytuacji życiowej, nazwaniu "
    "problemów i określeniu, jak wpływają na Twoje życie.",
  list_h="Czemu służy pierwsze spotkanie",
  items=["rozeznanie sytuacji życiowej", "identyfikacja problemów", "określenie ich wpływu na życie"],
  src="Konsultacje psychologiczne",
 ),
 dict(
  id="emocje", icon="p-emocje", target="lekarz-psychiatra",
  target_label="Lekarz psychiatra",
  h="Trudne emocje",
  lead="Zaburzenia nastroju, smutek, niekontrolowane napady agresji, apatia, omamy wzrokowe "
       "i słuchowe, napady lęku — to tylko niektóre z objawów, które mogą świadczyć "
       "o rozwijających się zaburzeniach psychicznych.",
  p="Pierwsza wizyta u psychiatry ma charakter diagnostyczny i trwa dłużej niż późniejsze wizyty "
    "kontrolne. Najczęściej już po pierwszym spotkaniu lekarz formułuje wstępne zalecenia "
    "i planuje przebieg leczenia. Przyjmujemy pacjentów od 14. roku życia; wizyty są komercyjne.",
  list_h="Objawy, których nie warto lekceważyć",
  items=["zaburzenia nastroju", "napady lęku", "apatia", "napady agresji", "omamy wzrokowe i słuchowe"],
  src="Lekarz psychiatra",
 ),
 dict(
  id="relacje", icon="p-relacje", target="poradnia-psychologiczna",
  target_label="Poradnia psychologiczna",
  h="Relacje, które bolą",
  lead="Poradnia nie pracuje wyłącznie z pojedynczą osobą. Opieką obejmuje też pary i całe rodziny.",
  p="Rodzice dzieci sprawiających trudności wychowawcze mogą skorzystać ze wsparcia wychowawczego "
    "i porady psychologicznej. Dzieci i młodzież są tu przyjmowane razem z rodzicami.",
  list_h="Kogo obejmuje opieka",
  items=["pary", "rodziny", "dzieci i młodzież z rodzicami", "dorośli", "wsparcie wychowawcze"],
  src="Poradnia psychologiczna",
 ),
 dict(
  id="zrozumienie", icon="p-zrozumienie", target="konsultacja-psychoterapeutyczna",
  target_label="Konsultacja psychoterapeutyczna",
  h="Lepsze zrozumienie siebie",
  lead="Celem konsultacji psychoterapeutycznej jest rozpoznanie potrzeb pacjenta i zrozumienie "
       "natury zgłaszanych problemów.",
  p="Po zebraniu wywiadu i wstępnej diagnozie terapeuta wraz z pacjentem określają cele terapii. "
    "Konsultacja bada też gotowość i motywację do jej podjęcia — oraz to, czy Klient i Terapeuta "
    "mogą ze sobą pracować.",
  list_h="Co ustalacie na konsultacji",
  items=["rozpoznanie potrzeb", "wstępna diagnoza", "cele i oczekiwania terapii",
         "gotowość i motywacja", "dopasowanie terapeuty"],
  src="Konsultacja psychoterapeutyczna",
 ),
 dict(
  id="jakosc-zycia", icon="p-jakosc-zycia", target="poradnia-psychologiczna",
  target_label="Poradnia psychologiczna",
  h="Zmiana jakości życia",
  lead="Część pacjentów trafia do poradni po czymś, co odmieniło ich codzienne funkcjonowanie — "
       "po udarze mózgu, urazie mózgowym albo zabiegu neurochirurgicznym.",
  p="Terapia neuropsychologiczna pracuje wtedy nad deficytami poznawczo-emocjonalnymi, które "
    "powstały w następstwie tych zdarzeń oraz w przebiegu chorób neurodegeneracyjnych. Poradnia "
    "kontynuuje również opiekę psychologiczną pacjentów po zakończonej hospitalizacji.",
  list_h="Zakres pracy",
  items=["diagnoza neuropsychologiczna", "terapia neuropsychologiczna",
         "diagnoza różnicowa otępienia", "kontynuacja opieki po hospitalizacji"],
  src="Poradnia psychologiczna",
 ),
]

# ══════════════════════════════════════════════════════════════════════════════
# FAQ — cztery pytania psychologiczne zdjęte z serwisu głównego (nr 7–10).
# Źródło: raw/static-mirror/rehamedica.info.pl/faq/ — treść 1:1, bez dopisków.
# Rejestr: „4 pytania psychologiczne w FAQ (nr 7–10) zdjęte z głównego serwisu ✅"
# ══════════════════════════════════════════════════════════════════════════════
FAQ = [
 dict(q="Czym zajmuje się poradnia psychologiczna?",
      a=["Poradnia psychologiczna to miejsce przeznaczone dla osób, które pragną zatroszczyć się "
         "o swój komfort i zdrowie psychiczne.",
         "Psychoterapia to zbiór technik, których zastosowanie ma za zadanie pomóc pacjentowi "
         "zrozumieć mechanizmy czy problemy natury psychologicznej oraz naprowadzić na drogę do "
         "ich przepracowania i rozwiązania."],
      cel="poradnia-psychologiczna"),
 dict(q="Jak wygląda wizyta u psychologa?",
      a=["Konsultacja psychologiczna polega na przeprowadzeniu przez psychologa wywiadu z pacjentem. "
         "W trakcie takiej rozmowy pacjent opowiada o tym, jak się czuje oraz w jakiej sytuacji "
         "życiowej obecnie się znajduje.",
         "Im więcej psycholog usłyszy w trakcie takiego spotkania, tym łatwiej będzie wybrać "
         "odpowiednią metodę leczenia."],
      cel="konsultacje-psychologiczne"),
 dict(q="W leczeniu jakich zaburzeń może pomóc psycholog?",
      a=["Zaburzenia psychosomatyczne. Problemy z poczęciem dziecka lub jego utratą. Kryzys, "
         "trudności życiowe, aktualnie przeżywane problemy. Kryzys i trudności w związku."],
      cel="poradnia-psychologiczna"),
 dict(q="Jak wygląda konsultacja psychoterapeutyczna?",
      a=["Konsultacja psychoterapeutyczna to wstępna rozmowa, podczas której omawiany jest charakter "
         "problemu pacjenta oraz nakreślany jest plan i kształt przyszłej terapii przez psychoterapeutę.",
         "Konsultacja służy także zapoznaniu się pacjenta z psychoterapeutą i podjęciu decyzji przez "
         "pacjenta, czy chce rozpocząć psychoterapię właśnie u tego terapeuty."],
      cel="konsultacja-psychoterapeutyczna"),
]

# ══════════════════════════════════════════════════════════════════════════════
# AKTUALNOŚCI — treści historyczne dotyczące psychologii.
# Potwierdzenie klienta #2: „zostają na głównym I BĘDĄ TEŻ NA DRUGIM serwisie".
# Publikujemy z rel=canonical na serwis główny — ta sama treść na dwóch domenach
# to duplikat; canonical mówi Google, który adres jest źródłem.
# ══════════════════════════════════════════════════════════════════════════════
AKTUALNOSCI = [
 dict(slug="projekt-mindspots", kat="Projekt UE", data="2025-11-25", data_txt="25 listopada 2025",
      zrodlo="/projekty-ue/projekt-mindspots/",
      t="MINDSpots — rozwój Ośrodków Opieki Psychologicznej i Psychoterapeutycznej",
      lead="Projekt dotyczy rozwoju Ośrodków Opieki Psychologicznej i Psychoterapeutycznej "
           "w województwie zachodniopomorskim, finansowany ze środków EFS+."),
 dict(slug="zakonczenie-postepowania-ofertowego-komputery-mindspots", kat="Projekt UE",
      data="2025-12-10", data_txt="10 grudnia 2025",
      zrodlo="/projekty-ue/zakonczenie-postepowania-ofertowego-komputery-mindspots/",
      t="Zakończenie postępowania ofertowego na zakup komputerów — projekt MINDSpots",
      lead="Postępowanie zakończone bez wyboru wykonawcy — oferty przekroczyły budżet projektu."),
 dict(slug="reha-medica-dolacza-do-programu-innowacja-model-dom", kat="Aktualność",
      data="2023-07-25", data_txt="25 lipca 2023",
      zrodlo="/aktualnosci/reha-medica-dolacza-do-programu-innowacja-model-dom/",
      t="Spotkanie warsztatowe w GOPS w Szczecinku — program Innowacja „Model DOM”",
      lead="Wydarzenie zorganizował Ośrodek Środowiskowej Opieki Psychologicznej "
           "i Psychoterapeutycznej w Szczecinku."),
 dict(slug="cialo-bez-kompleksow", kat="Aktualność", data="2023-04-12", data_txt="12 kwietnia 2023",
      zrodlo="/aktualnosci/cialo-bez-kompleksow/",
      t="Ciało bez kompleksów",
      lead="Program wzmacniający rolę i umiejętności opiekunów dzieci onkologicznych, "
           "wpływające na poprawę jakości ich życia."),
]

# ─────────────────────────────────────────────────────────────────────────
# SKALA — dane OGÓLNOPOLSKIE, nie wyniki Reha Medica.
#
# Wzorzec z growtherapy.com pokazuje własne wyniki kliniczne placówki
# („75% reduced anxiety…"). Reha Medica takich pomiarów nie ma w źródłach,
# a wymyślenie ich łamie regułę o nieinwentowaniu wyników medycznych.
# Dlatego blok mówi o SKALI ZJAWISKA i o DOSTĘPIE do pomocy — to fakty
# publiczne, sprawdzalne, z podaniem wydawcy i roku.
#
# Źródło główne: CBOS, „Zdrowie psychiczne Polaków", Komunikat z badań
# nr 154/2021, grudzień 2021. Badanie na reprezentatywnej imiennej próbie
# 1100 pełnoletnich mieszkańców Polski, losowanej z rejestru PESEL,
# zrealizowane 4–14 listopada 2021 (CAPI/CATI/CAWI).
# https://www.cbos.pl/SPISKOM.POL/2021/K_154_21.PDF
#
# Liczba chorujących na depresję pochodzi z raportu NFZ z 2020 r.,
# przywołanego przez CBOS na str. 1 tego samego komunikatu.
#
# DO POTWIERDZENIA (P19): właściciel akceptuje publikację danych CBOS na
# stronie oraz brzmienie zastrzeżenia, że nie są to wyniki Reha Medica.
SKALA_ZRODLO = ("CBOS, „Zdrowie psychiczne Polaków”, komunikat z badań nr 154/2021, "
                "próba 1100 osób. Dane ogólnopolskie — nie są to wyniki Reha Medica.")
SKALA_URL = "https://www.cbos.pl/SPISKOM.POL/2021/K_154_21.PDF"
SKALA = [
    dict(v=39, jed="%", t="Polaków niepokoi się o swoje zdrowie psychiczne",
         pod="W 2012 roku było to 33%.",
         cyt="Odsetek Polaków odczuwających niepokój o stan swojego zdrowia "
             "psychicznego nieco wzrósł i obecnie wynosi 39%."),
    dict(v=71, jed="%", t="uważa, że warunki życia w Polsce szkodzą zdrowiu psychicznemu",
         pod="Tylko 17% jest przeciwnego zdania.",
         cyt="Zaniepokojenie szkodliwością dla zdrowia psychicznego warunków życia "
             "w Polsce wyraża obecnie 71% badanych."),
    dict(v=31, jed="%", t="ocenia, że trudno dostać się do psychologa lub psychoterapeuty w ramach NFZ",
         pod="Dobrze dostęp ocenia co ósmy badany.",
         cyt="Co trzeci Polak (31%) ocenia, że trudno dostać się do psychologa "
             "lub psychoterapeuty — w ramach Narodowego Funduszu Zdrowia."),
    dict(v=20, jed="%", t="ocenia swoją kondycję psychiczną jako „taką sobie”",
         pod="W 2012 roku — 14%.",
         cyt="Wzrósł odsetek osób, które oceniają swój stan psychiczny jako taki sobie "
             "(z 14% w 2012 roku do 20% w 2021 roku)."),
]

# ─────────────────────────────────────────────────────────────────────────
# FORMY POMOCY — siatka ikon zamiast akapitu wyliczającego.
# Wzorzec: centrumsobota.pl/zakres-wsparcia/strefa-adhd.
#
# Każda pozycja MUSI mieć dosłowne pokrycie w treści źródłowej — cytat jest
# w kolumnie „src”. Nie dopisujemy usług, których klient nie potwierdził.
# Ikony dostarczone przez grafika klienta 2026-08-03 (10 sztuk).
FORMY = {
 "osrodek-psychologiczno-psychoterapeutyczny": [
   ("p-fm-porada",          "Porady psychologiczne",      "„realizowane są porady i diagnoza psychologiczna”"),
   ("p-fm-diagnoza",        "Diagnoza psychologiczna",    "„…porady i diagnoza psychologiczna”"),
   ("p-fm-terapia-ind",     "Psychoterapia indywidualna", "„psychoterapia indywidualna i grupowa”"),
   ("p-fm-terapia-gr",      "Psychoterapia grupowa",      "„psychoterapia indywidualna i grupowa”"),
   ("p-fm-terapia-rodz",    "Psychoterapia rodzinna",     "„psychoterapia rodzinna”"),
   ("p-fm-psychospoleczne", "Wsparcie psychospołeczne",   "„oraz wsparcie psychospołeczne”"),
 ],
 "poradnia-psychologiczna": [
   ("p-fm-diagnoza",           "Diagnoza psychologiczna",      "„wykonują zadania diagnostyczne i terapeutyczne”"),
   ("p-fm-terapia-ind",        "Terapia psychologiczna",       "„…diagnostyczne i terapeutyczne”"),
   ("p-fm-po-hospitalizacji",  "Opieka po hospitalizacji",     "„kontynuują opiekę psychologiczną pacjentów po zakończonej hospitalizacji”"),
   ("p-fm-wychowawcze",        "Wsparcie wychowawcze",         "„oferują wsparcie wychowawcze… dla rodziców”"),
   ("p-fm-diag-neuro",         "Diagnoza neuropsychologiczna", "„pełna ocena sprawności poznawczej”"),
   ("p-fm-terapia-neuro",      "Terapia neuropsychologiczna",  "„dedykowana pacjentom z deficytami poznawczo-emocjonalnymi”"),
 ],
}

# ─────────────────────────────────────────────────────────────────────────
# DLA KOGO — etykiety zamiast wyliczenia w zdaniu.
# Wzorzec: centrumsobota.pl, siatka „Kogo wspieramy” tuż pod nagłówkiem.
# Każda pozycja to dosłowny fragment materiałów klienta, nie nasza kategoria.
DLA_KOGO = {
 "poradnia-psychologiczna": [
   ("Dorośli",  "„dla osób dorosłych”"),
   ("Młodzież", "„młodzieży”"),
   ("Dzieci",   "„dzieci”"),
   ("Rodziny",  "„rodzin”"),
   ("Pary",     "„oraz par”"),
 ],
 "osrodek-psychologiczno-psychoterapeutyczny": [
   ("Dzieci poniżej 7. roku życia",     "„dzieci poniżej 7. roku życia”"),
   ("Dzieci i młodzież do 21. roku",    "„objęte obowiązkiem szkolnym — do 21. roku życia”"),
   ("Rodziny",                          "„oraz rodziny”"),
   ("Opiekunowie prawni",               "„i opiekunowie prawni”"),
 ],
 "lekarz-psychiatra": [
   ("Pacjenci od 14. roku życia", "„Pacjenci od 14. roku życia”"),
 ],
}

# ─────────────────────────────────────────────────────────────────────────
# ILUSTRACJE KOTWICZĄCE (zestaw C z briefu) — dostarczone 2026-08-03.
# Wzorzec Centrum Sobota: duża grafika przy bloku tekstu, przy której oko
# odpoczywa. Jedna na stronę usługi; opis alt niesie treść sceny.
ILUSTRACJE = {
 "poradnia-psychologiczna":         ("p-il-poradnia",           "Dwie osoby rozmawiające w fotelach w gabinecie poradni"),
 "osrodek-psychologiczno-psychoterapeutyczny": ("p-il-osrodek", "Dziecko z opiekunem naprzeciw specjalisty"),
 "konsultacje-psychologiczne":      ("p-il-pierwsze-spotkanie", "Rozmowa, w której padają pytania"),
 "konsultacja-psychoterapeutyczna": ("p-il-dopasowanie",        "Dwie osoby składające puzzle — sprawdzenie, czy mogą pracować razem"),
 "lekarz-psychiatra":               ("p-il-motywacja",          "Osoba w ruchu, przed nią wytyczona droga"),
}

# ─────────────────────────────────────────────────────────────────────────
# NEUROPSYCHOLOGIA — pierwsza z zakładek dla form pomocy (2026-08-03).
#
# Zbudowana wg zasady uzgodnionej z właścicielem:
#   • co robi Reha Medica — WYŁĄCZNIE z materiałów klienta,
#   • czym jest metoda — z zewnętrznych, sprawdzalnych źródeł, napisane
#     własnymi słowami i podpisane, w osobnej sekcji.
# Źródło zewnętrzne przy tej stronie: Mroczkowska D., Tyras S.,
# „Zastosowanie EEG-Neurofeedback w rehabilitacji zaburzeń mowy u pacjentów
# poudarowych", Psychiatria 2018, tom 15, nr 4, s. 199–205, Via Medica.
# Cytowana stamtąd jedna liczba, z zaznaczeniem, że to dane ogólne.
SERVICES["neuropsychologia"] = dict(
    title="Diagnoza i terapia neuropsychologiczna",
    short="Neuropsychologia",
    lead="Ocena i usprawnianie funkcji poznawczych po udarze mózgu, urazie "
         "mózgowym lub zabiegu neurochirurgicznym.",
    img="poradnia-hero.webp", band=None,
    cities=["szczecinek", "szczecin", "walcz", "bialogard", "bobolice"],
    fin="DO POTWIERDZENIA",
)

SERVICE_CONTENT["neuropsychologia"] = dict(
    kicker="Dla kogo",
    lead="Diagnoza i terapia neuropsychologiczna są częścią poradni "
         "psychologicznej Reha Medica.",
    body=[
        "W przypadkach zaburzeń zdiagnozowanych przez lekarza neurologa lub "
        "lekarza psychiatrę pacjent kierowany jest do psychologa celem "
        "przeprowadzenia całościowej diagnozy neuropsychologicznej.",
        "Poradnia kontynuuje również opiekę psychologiczną pacjentów po "
        "zakończonej hospitalizacji.",
    ],
    pull_q=None, pull_p=[],
    parts_h="Co obejmuje",
    parts=[
        "<b>Diagnoza neuropsychologiczna</b> to pełna ocena sprawności "
        "poznawczej — m.in. uwagi, funkcji mnestycznych, językowych, "
        "wykonawczych i wzrokowo-przestrzennych — u pacjentów po przebytych "
        "udarach mózgu, urazach mózgowych i zabiegach neurochirurgicznych. "
        "Obejmuje również diagnozę różnicową otępienia.",
        "<b>Terapia neuropsychologiczna</b> dedykowana jest pacjentom "
        "z różnego rodzaju deficytami poznawczo-emocjonalnymi powstałymi "
        "w następstwie przebytych udarów mózgu, urazów mózgowych, po zabiegach "
        "neurochirurgicznych oraz w przebiegu chorób neurodegeneracyjnych.",
    ],
    coda_lead=None, coda_p=None,
)

# Warstwa ogólna — NIE jest to opis oferty Reha Medica, tylko kontekst
# medyczny z podanego źródła. Renderowana w osobnej, podpisanej sekcji.
KONTEKST = {
 "neuropsychologia": dict(
   naglowek="Dlaczego funkcje poznawcze bada się po udarze",
   tekst="Zaburzenia pamięci, uwagi, mowy czy planowania należą do "
         "najczęstszych następstw udaru mózgu. W polskim piśmiennictwie "
         "medycznym szacuje się, że <b>nawet połowa osób po przebytym udarze</b> "
         "może z tego powodu doświadczać niepełnosprawności. Badanie "
         "neuropsychologiczne pokazuje, które z tych funkcji ucierpiały "
         "i w jakim stopniu — a to jest punkt wyjścia do zaplanowania terapii.",
   zrodlo="Mroczkowska D., Tyras S., „Zastosowanie EEG-Neurofeedback "
          "w rehabilitacji zaburzeń mowy u pacjentów poudarowych”, "
          "Psychiatria 2018, t. 15, nr 4, s. 199–205, Via Medica.",
   url="https://journals.viamedica.pl/psychiatria/article/download/58936/46905",
 ),
}

# Zakładki budowane POZA SERVICE_ORDER — nie trafiają do menu ani do sekcji
# „Pięć form opieki", bo nie są jedną z pięciu podstawowych usług, tylko
# rozwinięciem tego, co poradnia w sobie zawiera.
DODATKOWE_ZAKLADKI = ["neuropsychologia"]

# Które pozycje siatki „Formy pomocy" mają już własną zakładkę.
# Reszta zostaje opisem — nie robimy odsyłaczy donikąd.
ZAKLADKA_FORMY = {
 "p-fm-diag-neuro":    "neuropsychologia",
 "p-fm-terapia-neuro": "neuropsychologia",
}
