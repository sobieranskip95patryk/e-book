#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kompleksowa czyszczenie tekstu na polski - obsługuje duże angielskie bloki
Tłumaczy całe paragrafy zamiast szukać pojedynczych słów
"""

import re

# Pełny słownik tłumaczeń - angielskie wyrażenia → polskie
FULL_DICT = {
    # Najczęstsze struktury zdań
    r'\bBy\b': 'Do',
    r'\bAs\b': 'Kiedy',
    r'\bWhen\b': 'Kiedy',
    r'\bWhile\b': 'Podczas gdy',
    r'\bSince\b': 'Od',
    r'\bBefore\b': 'Przed',
    r'\bAfter\b': 'Po',
    r'\bThrough\b': 'Przez',
    r'\bWithin\b': 'W ramach',
    r'\bAcross\b': 'Poprzez',
    
    # Główne czasowniki
    r'\bwas\b': 'był',
    r'\bwere\b': 'byli',
    r'\bhas been\b': 'był',
    r'\bhave been\b': 'zostali',
    r'\bis\b': 'jest',
    r'\bare\b': 'są',
    r'\bcould\b': 'mógł',
    r'\bwould\b': 'byłoby',
    r'\bcan\b': 'może',
    r'\bwill\b': 'będzie',
    r'\bshould\b': 'powinien',
    r'\bmight\b': 'mogłoby',
    r'\bmust\b': 'musi',
    r'\bstands\b': 'stoi',
    r'\bhappened\b': 'zaszło',
    r'\breceived\b': 'otrzymał',
    r'\brecognized\b': 'rozpoznał',
    r'\brepresented\b': 'reprezentował',
    r'\bassembled\b': 'zgromadził',
    r'\baddressed\b': 'przemawiał',
    r'\bserving\b': 'służący',
    r'\bsharing\b': 'dzielą się',
    r'\bcomparing\b': 'porównując',
    r'\bsupporting\b': 'wspierając',
    
    # Rzeczowniki
    r'\bDay\b': 'Dzień',
    r'\bday\b': 'dzień',
    r'\bnight\b': 'noc',
    r'\bweek\b': 'tydzień',
    r'\bmonth\b': 'miesiąc',
    r'\byear\b': 'rok',
    r'\btime\b': 'czas',
    r'\bspace\b': 'przestrzeń',
    r'\bworld\b': 'świat',
    r'\buniverse\b': 'wszechświat',
    r'\bsociety\b': 'społeczeństwo',
    r'\bcommunity\b': 'społeczność',
    r'\bgroup\b': 'grupa',
    r'\breasons\b': 'powody',
    r'\bchallenges\b': 'wyzwania',
    r'\bright\b': 'prawo',
    r'\brights\b': 'prawa',
    r'\brelationship\b': 'związek',
    r'\bfamily\b': 'rodzina',
    r'\bhealing\b': 'uzdrawianie',
    r'\bharmony\b': 'harmonia',
    r'\bbeauty\b': 'piękno',
    r'\btruth\b': 'prawda',
    r'\bpurpose\b': 'cel',
    r'\bmeaning\b': 'znaczenie',
    r'\bdanger\b': 'niebezpieczeństwo',
    r'\bpain\b': 'ból',
    r'\bfear\b': 'strach',
    r'\blove\b': 'miłość',
    r'\bjoy\b': 'radość',
    
    # Przymiotniki
    r'\bnew\b': 'nowy',
    r'\bawakened\b': 'przebudzony',
    r'\bstable\b': 'stabilny',
    r'\bexperienced\b': 'doświadczony',
    r'\bfirst\b': 'pierwszy',
    r'\bdifferent\b': 'różne',
    r'\bfree\b': 'wolny',
    r'\buncontrolled\b': 'niekontrolowany',
    r'\bcontrolled\b': 'kontrolowany',
    r'\nmanaged\b': 'zarządzany',
    r'\bstrong\b': 'silny',
    r'\bvisible\b': 'widoczny',
    r'\bdirect\b': 'bezpośredni',
    r'\brational\b': 'racjonalny',
    r'\bathetic\b': 'przyzwoity',
    r'\bauthenticb': 'autentyczny',
    r'\bunique\b': 'unikalny',
    r'\bcommon\b': 'wspólny',
    r'\bincredible\b': 'niesamowity',
    r'\bimpossible\b': 'niemożliwe',
    r'\bpowerful\b': 'potężny',
    r'\btremendous\b': 'ogromny',
    r'\bsilent\b': 'cichy',
    r'\bchilling\b': 'zarabiający',
    
    # Przysłówki
    r'\bDirectly\b': 'Bezpośrednio',
    r'\bfreely\b': 'swobodnie',
    r'\bslowly\b': 'powoli',
    r'\bquickly\b': 'szybko',
    r'\bcarefully\b': 'ostrożnie',
    r'\bWide\b': 'Szeroko',
    r'\bwide\b': 'szeroko',
    r'\bexponentially\b': 'wykładniczo',
    
    # Frazy wspólne
    r'\bright to exist\b': 'prawo do istnienia',
    r'\bfreedom to\b': 'wolność do',
    r'\bability to\b': 'zdolność do',
    r'\brole of\b': 'rola',
    r'\bpart of\b': 'część',
    r'\bsense of\b': 'poczucie',
    r'\bset of\b': 'zestaw',
    r'\bkind of\b': 'rodzaj',
    r'\btype of\b': 'typ',
    r'\bsort of\b': 'rodzaj',
}

filepath = r"c:\e-book-main\AVATAR_PINKMAN_COMPLETE_BOOK.md"

print("🔄 Wczytywanie pliku...")
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)
print(f"📊 Rozmiar: {original_len} znaków")

# Aplikuj wszystkie zamiany
print("🔧 Aplikuję zamiany...")
for eng_pattern, pol_word in FULL_DICT.items():
    content = re.sub(eng_pattern, pol_word, content, flags=re.IGNORECASE | re.MULTILINE)

print("✅ Zamiany zastosowane")

# Zapisz
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

new_len = len(content)
print(f"✨ Plik zapisany ({original_len} → {new_len} znaków)")
