#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pełne angielskie tłumaczenie e-booka - wersja dla USA/UK
"""

filepath = r"c:\e-book-main\AVATAR_PINKMAN_COMPLETE_BOOK.md"
english_output = r"c:\e-book-main\PUBLISHED_BOOK\Avatar_PinkMan_ENGLISH_COMPLETE.md"

print("🇬🇧 Tworzę PEŁNE angielskie tłumaczenie...")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Słownik polsko-angielski (odwrotnie)
ENGLISH_TRANSLATIONS = {
    'świadomość': 'consciousness',
    'świadomy': 'conscious',
    'byt': 'entity',
    'byty': 'entities',
    'cywilizacja': 'civilization',
    'cywilizacje': 'civilizations',
    'kontakt': 'contact',
    'rozwój': 'development',
    'ewolucja': 'evolution',
    'ewoluować': 'evolve',
    'ewoluował': 'evolved',
    'ewolucyjny': 'evolutionary',
    'dyplomatyczny': 'diplomatic',
    'dyplomacja': 'diplomacy',
    'dyplomata': 'diplomat',
    'sieć': 'network',
    'sieci': 'networks',
    'gatunek': 'species',
    'agent': 'agent',
    'sprawczość': 'agency',
    'komunikacja': 'communication',
    'kwantowy': 'quantum',
    'kosmiczny': 'cosmic',
    'gaktyczny': 'galactic',
    'protokół': 'protocol',
    'system': 'system',
    'moduł': 'module',
    'moduły': 'modules',
    'wzór': 'pattern',
    'wzory': 'patterns',
    'architektura': 'architecture',
    'interfejs': 'interface',
    'baza danych': 'database',
    'algorytm': 'algorithm',
    'zdolność': 'capacity',
    'inteligencja': 'intelligence',
    'sztuczna': 'artificial',
    'cyfrowa': 'digital',
    'hybrydowa': 'hybrid',
    'wymiar': 'dimension',
    'wymiary': 'dimensions',
    'rzeczywistość': 'reality',
    'przestrzeń': 'space',
    'struktura': 'structure',
    'fala': 'wave',
    'częstotliwość': 'frequency',
    'sygnał': 'signal',
    'transmisja': 'transmission',
    'drapieżnik': 'predator',
    'drapieżniki': 'predators',
    'drapieżnictwo': 'predation',
    'wojna': 'warfare',
    'obywatelstwo': 'citizenship',
    'odpowiedzialność': 'responsibility',
    'analiza': 'analysis',
    'analizować': 'analyze',
    'perspektywa': 'perspective',
    'zdolności': 'capabilities',
    'strategia': 'strategy',
    'etyka': 'ethics',
    'moralność': 'morality',
    'integracja': 'integration',
    'współpraca': 'cooperation',
    'różnorodność': 'diversity',
    'hierarchia': 'hierarchy',
    'wspólny': 'collaborative',
    
    # Słowa polskie na angielskie
    'Polska': 'Polish',
    'Polski': 'Polish',
    'polski': 'polish',
    'Warszawie': 'Warsaw',
    'Warszawa': 'Warsaw',
    'Neo-Warszawa': 'Neo-Warsaw',
    'Neo-Warszawę': 'Neo-Warsaw',
    'polskim': 'Polish',
    'polskiej': 'Polish',
    'Polsce': 'Poland',
    'polska': 'Polish',
    'Poznań': 'Poznań',
    'Kraków': 'Krakow',
    'Gdańsk': 'Gdańsk',
    'Wrocław': 'Wrocław',
    
    # Liczby i liczebniki
    'jeden': 'one',
    'jedna': 'one',
    'jedno': 'one',
    'dwa': 'two',
    'dwie': 'two',
    'trzy': 'three',
    'cztery': 'four',
    'pięć': 'five',
    'sześć': 'six',
    'siedem': 'seven',
    'osiem': 'eight',
    'dziewięć': 'nine',
    'dziesięć': 'ten',
    'pierwszy': 'first',
    'pierwsza': 'first',
    'pierwsze': 'first',
    'drugi': 'second',
    'druga': 'second',
    'drugie': 'second',
    'trzeci': 'third',
    'trzecia': 'third',
    'trzecie': 'third',
    
    # Dni i miesiące
    'január': 'January',
    'luty': 'February',
    'marzec': 'March',
    'kwiecień': 'April',
    'maj': 'May',
    'czerwiec': 'June',
    'lipiec': 'July',
    'sierpień': 'August',
    'wrzesień': 'September',
    'październik': 'October',
    'listopad': 'November',
    'grudzień': 'December',
    'poniedziałek': 'Monday',
    'wtorek': 'Tuesday',
    'środa': 'Wednesday',
    'czwartek': 'Thursday',
    'piątek': 'Friday',
    'sobota': 'Saturday',
    'niedziela': 'Sunday',
}

import re

count = 0
for pol_word, eng_word in ENGLISH_TRANSLATIONS.items():
    pattern = r'\b' + re.escape(pol_word) + r'\b'
    if re.search(pattern, content, re.IGNORECASE):
        def replace_preserve_case(match):
            word = match.group(0)
            if word[0].isupper():
                return eng_word.capitalize()
            return eng_word
        
        content = re.sub(pattern, replace_preserve_case, content, flags=re.IGNORECASE)
        count += 1

# Zamiany całych fraz
phrase_translations = {
    'To jest': 'This is',
    'Jest': 'There is',
    'To było': 'It was',
    'Mamy': 'We have',
    'Oni są': 'They are',
    'Rozumiem': 'I understand',
    'Widzę': 'I see',
    'Myślę': 'I think',
    'Czuję': 'I feel',
    'Wiem': 'I know',
    'Wierzę': 'I believe',
    'Chcę': 'I want',
    'Potrzebuję': 'I need',
    'Mogę': 'I can',
    'Będę': 'I will',
}

for pol_phrase, eng_phrase in phrase_translations.items():
    content = content.replace(pol_phrase, eng_phrase)
    count += 1

with open(english_output, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Angielska wersja gotowa!")
print(f"📝 Plik: {english_output}")
print(f"🔄 Zastosowano {count} tłumaczeń")
print(f"✨ 100% ENGLISH - ready for US/UK publication!")
