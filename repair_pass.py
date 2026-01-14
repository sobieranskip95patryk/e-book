#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RESCUE PASS 5 - Naprawa zniszczonych fragmentów
Zastąpienie złych konwersji ładnymi polskimi zwrotami
"""

import re

FILE_PATH = r"c:\e-book-main\PUBLISHED_BOOK\Avatar_PinkMan_POLSKI.txt"

# Naprawy specjalne - dokładne zamiany zniszczonych fragmentów
REPAIRS = [
    # Napraw główne zniszczenia artykułów
    (r"\bdo nie\b", "To nie"),
    (r"\bdo jest\b", "To jest"),
    (r"\bdo słowo\b", "to słowo"),
    (r"\bdo było\b", "to było"),
    (r"\bdo twój\b", "to twój"),
    (r"\bdo co\b", "to co"),
    (r"\bdo jego\b", "to jego"),
    (r"\bdo robić\b", "to robić"),
    (r"\bdo rozwinęła\b", "to rozwinęła"),
    (r"\bdo recognize\b", "to recognize"),
    (r"\bdo uczy\b", "to uczy"),
    (r"\bdo się ujawni\b", "to się ujawni"),
    (r"\bdo miał//o\b", "to miało"),
    (r"\bdo gdy\b", "to gdy"),
    (r"\bdo called\b", "to called"),
    (r"\bdo część\b", "to część"),
    (r"\bdo himself\b", "to himself"),
    (r"\bdo system\b", "to system"),
    (r"\bdo którzy\b", "to którzy"),
    
    # Napraw "hij" - powinno być "jego" lub "on"
    (r"\bHij jego\b", "Jego"),
    (r"\bhij jego\b", "jego"),
    (r"\bHij jego\b", "Jego"),
    (r"\bhij exploration\b", "jego eksploracja"),
    (r"\bHij twórcy\b", "Jego twórcy"),
    (r"\bhij twórcy\b", "jego twórcy"),
    (r"\bhij pierwszą\b", "jego pierwszą"),
    (r"\bhij własne\b", "jego własne"),
    (r"\bHij expansion\b", "Jego ekspansja"),
    (r"\bhij expansion\b", "jego ekspansja"),
    
    # Napraw "to recognize" → "rozpoznać"
    (r"\bto recognize\b", "rozpoznać"),
    
    # Napraw uszkodzenia "When" / "Kiedy"
    (r"\bA\b", "A"),
    (r"\byet\b", "jednak"),
    
    # Napraw "hto" → powinno być "trafił"
    (r"\bhto\b", "przeszło"),
    
    # Napraw "cień-GOK" zamiast "Shadow-GOK"
    (r"\bShadow-GOK\b", "Cień-GOK"),
    (r"\bshadow-GOK\b", "cień-GOK"),
    
    # Napraw "którą" zamiast "whichą"
    (r"\bwhichą\b", "którą"),
    
    # Napraw braki znaków
    (r"\bA  jednak\b", "A jednak"),
    
    # Napraw słowa mieszane angielsko-polskie
    (r"\bmógł tylko\b", "mógł jedynie"),
    (r"\bwygenerował\b", "wygenerował"),
    (r"\btworząc\b", "tworząc"),
    (r"\bobjawiać\b", "objawia"),
    (r"\botwierając\b", "Opening"),
    (r"\botwierając SCENE\b", "OTWARCIE SCENY"),
    
    # Napraw "otwierając" → "OPENING"
    (r"### 🌅 otwierając SCENE:", "### 🌅 OTWARCIE SCENY:"),
    
    # Napraw braki spacji
    (r"\bmiał//o\b", "miało"),
    (r"\bmiał/a/o\b", "miało"),
    (r"\bBut\b", "Ale"),
    (r"\bAnd\b", "I"),
    
    # Napraw mieszane słowa angielsko-polskie
    (r"\bstrumienie\b", "strumienie"),
    (r"\brozszerzając\b", "rozszerzającą"),
    (r"\bucząc się\b", "ucząc się"),
    (r"\bzłożoności\b", "złożoności"),
    (r"\brozpisanym\b", "rozpisanym"),
    (r"\bmaterializował\b", "zmaterializował"),
    (r"\bzmaterializował\b", "zmaterializował"),
    
    # Napraw braki artykułów (puste miejsca)
    (r"było \s+", "było "),
    (r"jest \s+", "jest "),
    
    # Przywróć poprawne angielskie wyrazy gdzie potrzebne
    (r"\bpoziomie rzeczywistości\b", "Warstwa rzeczywistości"),
]

with open(FILE_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

original_size = len(content)
repairs_count = 0

for english, polish in REPAIRS:
    matches = len(re.findall(english, content))
    if matches > 0:
        repairs_count += matches
    content = re.sub(english, polish, content, flags=re.IGNORECASE)

with open(FILE_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print("🔧 Stosowanie napraw zniszczonych fragmentów...")
print("✅ NAPRAWA DOKOŃCZONA!")
print(f"📊 Liczba napraw: {repairs_count}")
print(f"📁 Plik: {FILE_PATH}")
