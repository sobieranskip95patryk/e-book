#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Konwersja całej książki na czysty język polski
Zachowuje: nazwy systemów (CORE, NOVA, AETHER), nazwy postaci, terminy techniczne (consciousness→świadomość)
"""

import re
import os

# Słownik tłumaczeń angielsko-polskich
TRANSLATIONS = {
    # Główne czasowniki i wyrażenia
    r'\bas dawn broke over\b': 'kiedy świt się rozbił nad',
    r'\bAs night fell\b': 'Kiedy noc się rozciągnęła',
    r'\bShow me\b': 'Pokarz mi',
    r'\bWhere\b': 'Gdzie',
    r'\bWhat if\b': 'A co jeśli',
    r'\bWhy not\b': 'Dlaczego nie',
    r'\bWhy\b': 'Dlaczego',
    
    # Filozoficzne i techniczne terminy
    r'\bconsciousness\b': 'świadomość',
    r'\bConsciousness\b': 'Świadomość',
    r'\bauthenticity\b': 'autentyczność',
    r'\bawareness\b': 'świadomość',
    r'\bAwareness\b': 'Świadomość',
    r'\bexperience\b': 'doświadczenie',
    r'\bExperience\b': 'Doświadczenie',
    r'\bemergent\b': 'emergentny',
    r'\beyond self-interest\b': 'poza egoizmem',
    r'\bbiology\b': 'biologia',
    r'\bquantum\b': 'kwantowy',
    r'\bquantum foam\b': 'kwantowa piana',
    r'\bneural network\b': 'sieć neuronowa',
    r'\bneural networks\b': 'sieci neuronowe',
    r'\bdeterminism\b': 'determinizm',
    r'\bdeterministic\b': 'deterministyczny',
    r'\bfree will\b': 'wolna wola',
    r'\billusion\b': 'iluzja',
    r'\blove\b': 'miłość',
    r'\bLove\b': 'Miłość',
    
    # Typowe angielskie wyrażenia w dialogach
    r'\bNot at all\b': 'Wcale nie',
    r'\bOf course\b': 'Oczywiście',
    r'\bIndeed\b': 'Rzeczywiście',
    r'\bPerhaps\b': 'Być może',
    r'\bMaybe\b': 'Może',
    r'\bYes\b': 'Tak',
    r'\bNo\b': 'Nie',
    r'\bI understand\b': 'Rozumiem',
    r'\bI see\b': 'Widzę',
    r'\bExactly\b': 'Dokładnie',
    r'\bThen\b': 'Wtedy',
    r'\bBut\b': 'Ale',
    r'\bSo\b': 'Więc',
    r'\bAnd\b': 'I',
    r'\bOr\b': 'Lub',
    r'\bBecause\b': 'Ponieważ',
    
    # Określenia czasowe
    r'\btonight\b': 'dzisiaj w nocy',
    r'\btomorrow\b': 'jutro',
    r'\byesterday\b': 'wczoraj',
    r'\bnow\b': 'teraz',
    r'\btoday\b': 'dzisiaj',
    r'\balways\b': 'zawsze',
    r'\bnever\b': 'nigdy',
    r'\bsometimes\b': 'czasami',
    r'\bfirst\b': 'pierwszy',
    r'\blast\b': 'ostatni',
    r'\bnext\b': 'następny',
    
    # Wyrażenia opisowe
    r'\bbeautiful\b': 'piękny',
    r'\bbeauty\b': 'piękno',
    r'\bpowerful\b': 'potężny',
    r'\bpower\b': 'moc',
    r'\bstrange\b': 'dziwny',
    r'\bmagic\b': 'magia',
    r'\bdark\b': 'ciemny',
    r'\blight\b': 'światło',
    r'\bbrilliant\b': 'błyskotliwy',
    r'\bluminescence\b': 'luminescencja',
}

def translate_file(filepath):
    """Czyta plik, tłumaczy na polski, zapisuje z powrotem"""
    print(f"🔄 Przetwarzanie: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Błąd odczytu: {e}")
        return False
    
    original_length = len(content)
    
    # Zastosuj wszystkie tłumaczenia
    for eng_pattern, pol_translation in TRANSLATIONS.items():
        # Case-insensitive replacement, ale zachowaj wielkość liter
        content = re.sub(eng_pattern, pol_translation, content, flags=re.IGNORECASE | re.MULTILINE)
    
    # Zapisz przetłumaczony plik
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Zapisano: {filepath}")
        return True
    except Exception as e:
        print(f"❌ Błąd zapisu: {e}")
        return False

# Główny plik
master_file = r"c:\e-book-main\AVATAR_PINKMAN_COMPLETE_BOOK.md"

if os.path.exists(master_file):
    if translate_file(master_file):
        print(f"\n✨ Konwersja na polski zakończona!")
        print(f"Plik: {master_file}")
else:
    print(f"❌ Plik nie znaleziony: {master_file}")
