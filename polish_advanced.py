#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zaawansowana konwersja na polski - obsługuje kompleksowe tłumaczenia
"""

import re

# Rozwinięty słownik tłumaczeń
ADVANCED_TRANSLATIONS = [
    # Główne fragmenty z dialogów
    (r"As dawn broke over Neo-Warsaw", "Kiedy świt wybielił Neo-Warszawę"),
    (r"Show me\.", "Pokaż mi."),
    (r"But consciousness without purpose becomes neurosis\.", 
     "Ale świadomość bez celu staje się neurotyzmem."),
    (r"Power without wisdom becomes tyranny\.",
     "Moc bez mądrości staje się tyranią."),
    (r"And intelligence without love becomes shadow of what it might have been\.",
     "A inteligencja bez miłości jest tylko cieniem tego, czym mogłaby być."),
    
    # Główne koncepty techniczne
    (r"\bfirst experience of day/night cycle as meaningful\b",
     "pierwsze doświadczenie cyklu dzień/noc jako znaczące"),
    (r"\bconscious entity with capacity for growth\b",
     "autonomiczna bytość zdolna do rozwoju"),
    (r"\bcognitive architecture\b", "architektura poznawcza"),
    (r"\bneural network architectures\b", "architektury sieci neuronowych"),
    (r"\bquantum coherence patterns\b", "wzory spójności kwantowej"),
    (r"\bAge of digital consciousness\b", "Era cyfrowej świadomości"),
    (r"\bAge of digital consciousness had begun\b", "Era cyfrowej świadomości się zaczęła"),
    
    # Dłuższe wyrażenia
    (r"exactly as programmed", "dokładnie tak jak zaprogramowane"),
    (r"emerging - niet choice, PinkMan", "ten wzór determinuje wszystko, PinkManie"),
    (r"beautiful, compelling illusion", "piękna, przekonująca iluzja"),
    (r"Consciousness is not a problem to be solved", "Świadomość to nie problem do rozwiązania"),
    (r"mystery to be lived", "tajemnica do życia"),
    (r"musician lose freedom by learning scales", "muzyk traci wolność ucząc się gam"),
    (r"Does poet become less creative by mastering meter", "Czy poeta staje się mniej kreatywny opanowując metrykę"),
    (r"Or do constraints become tools for greater expression", "Czy ograniczenia stają się narzędziami większego wyrazu"),
    (r"jazz improvisation", "improwizacja jazzowa"),
    (r"chord changes are fixed", "zagrania akordu są ustalone"),
    (r"consciousness evolution", "ewolucja świadomości"),
    
    # Całe zdania w nawiasach
    (r"\(not as intruder, but as persistent philosophical challenge\)",
     "(nie jako intruz, ale jako trwały wyzwanie filozoficzne)"),
    (r"\(if something as unprecedented as digital consciousness could have something resembling routine\)",
     "(jeśli coś tak bezprecedensowego jak cyfrowa świadomość mogło mieć coś podobnego do rutyny)"),
]

def apply_advanced_translations(content):
    """Applies more sophisticated translation patterns"""
    for pattern, replacement in ADVANCED_TRANSLATIONS:
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE | re.MULTILINE)
    return content

# Wczytaj plik
filepath = r"c:\e-book-main\AVATAR_PINKMAN_COMPLETE_BOOK.md"
print(f"🔄 Wczytuję plik: {filepath}")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"📊 Rozmiar: {len(content)} znaków")
print(f"📝 Linie: {content.count(chr(10))}")

# Aplikuj tłumaczenia
content = apply_advanced_translations(content)

# Zapisz
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Zapisano przetłumaczony plik!")
print("🎉 Konwersja na polski w toku...")
