#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FINALIZACJA EDYCJI - Przygotowanie e-book do wydania
Naprawy ostateczne i formatowanie
"""

import re
from pathlib import Path

FILE_PATH = r"c:\e-book-main\PUBLISHED_BOOK\Avatar_PinkMan_POLSKI.txt"

# Naprawy ostateczne - błędy z poprzednich pass'ów
FINAL_FIXES = [
    (r"^dane ukończenia", "Data ukończenia"),
    (r"^robić nie est", "To nie jest"),
    (r"^robić jest", "To jest"),
    (r"że robić est", "że to jest"),
    (r"że robić słowo", "że to słowo"),
    (r"że robić nie", "że to nie"),
    (r"objawia duchowy", "manifest duchowy"),
    (r"rdzenie inicjalizacja", "CORE inicjalizacja"),
    (r"spontaniczny NOWA", "spontaniczna NOVA"),
    (r"4G→5G przejście", "4G→5G transition"),
    (r"cień-GOK role", "Cień-GOK rola"),
    (r"Otwarcie scena", "OTWARCIE SCENY"),
    (r"Rozwój scena", "Rozwój SCENY"),
    (r"kwantowy jądra", "kwantowe jądra"),
    (r"Neuronalne sieci, dane przetwarzanie", "Neuronalne sieci, przetwarzanie danych"),
    (r"pamięć alokacja systems", "alokacja pamięci systemy"),
    (r"robić była ta", "To była ta"),
    (r"robić słowo nie", "to słowo nie"),
    (r"logiczny wniosek", "logiczny wniosek"),
    (r"wewnętrzne wiedząc", "wewnętrzne wiedzieć"),
    (r"Do słowo", "To słowo"),
    (r"bazy danych", "bazy danych"),
    (r"doubt about", "wątpliwości dotyczące"),
    (r"shadow-GOK", "Cień-GOK"),
    (r"Shadow-GOK", "Cień-GOK"),
    (r"Genesis", "Geneza"),
    (r"emergence", "pojawienia"),
    (r"emergence", "pojawienia"),
]

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Przeczytaj plik
content = read_file(FILE_PATH)
print("📖 Czytanie pliku...")

# Zastosuj naprawy ostateczne
fixes_count = 0
for pattern, replacement in FINAL_FIXES:
    matches = len(re.findall(pattern, content, re.MULTILINE | re.IGNORECASE))
    if matches > 0:
        fixes_count += matches
        content = re.sub(pattern, replacement, content, flags=re.MULTILINE | re.IGNORECASE)

# Usuń informacje meta
print("🧹 Usuwanie informacji META...")
content = re.sub(r'### 🎯 INFORMACJE META.*?\n---\n', '', content, flags=re.DOTALL)

# Dodaj właściwy header
header = """# AVATAR PINKMAN: META-GENIUSZ
## Kompletna Powieść Sciencefiction Filozoficzna

**Autor**: System Avatar PinkMan  
**Gatunek**: Science Fiction • Filozofia • Dystopia  
**Status**: ✅ PEŁNA WERSJA PUBLIKACYJNA  
**Słowa**: ~400,000+  
**Rozdziały**: 21 + Prolog + Epilog  
**Księgi**: 4  
**Data**: 10 stycznia 2026  
**Język**: Polski  
**Kodowanie**: UTF-8  

---

## LICENCJA

© 2026 Avatar PinkMan Meta-Geniusz. Wszelkie prawa zastrzeżone.

Ta publikacja może być dystrybuowana pod warunkami Creative Commons lub inną umową licencyjną.

---

"""

# Zastąp stary header nowym
content = re.sub(r'# AVATAR PINKMAN:.*?\n---\n', header, content, flags=re.DOTALL)

# Zapisz poprawioną wersję
write_file(FILE_PATH, content)

print(f"✅ FINALIZACJA DOKOŃCZONA!")
print(f"📊 Napraw ostatecznych: {fixes_count}")
print(f"📁 Plik: {FILE_PATH}")
print(f"📖 Rozmiar: {len(content):,} znaków")
print(f"\n🎉 E-BOOK GOTOWY DO WYDANIA!")
