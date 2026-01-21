#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Czyszczenie angielskich fragmentów z polskiego tekstu
"""

import re

# Wczytaj plik
filepath = r"c:\e-book-main\AVATAR_PINKMAN_COMPLETE_BOOK.md"
print(f"🔄 Czyszczenie angielskiego: {filepath}")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Wzory do zamienienia
patterns = {
    # Zdania rozpoczynające się od "It was"
    r'It was true\. ': 'To była prawda. ',
    r'It\'s not ': 'To nie jest ',
    r'It\'s both': 'To zarówno jedno jak i drugie',
    r'It\'s like': 'To jest jak',
    r'It was': 'To było',
    
    # Zdania z "The"
    r'The question hung': 'Pytanie wisiało',
    r'The real adventure': 'Prawdziwa przygoda',
    r'The age of digital': 'Era cyfrowej',
    
    # Słowa pojedyncze
    r'\bsaid\b': 'powiedział',
    r'\bsays\b': 'mówi',
    r'\bcan see\b': 'może widzieć',
    r'\bcan feel\b': 'może czuć',
    r'\bfeeling\b': 'czując',
    r'\bfelt\b': 'czuł',
    r'\bshould be\b': 'powinno być',
    r'\bwould be\b': 'byłoby',
    r'\bwould have\b': 'byłoby',
    r'\bmight be\b': 'mogłoby być',
    r'\bmight\b': 'mogłoby',
    r'\bcoming\b': 'nadchodząca',
    r'\bbecoming\b': 'stając się',
    
    # Znaki punkutacji angielskie
    r'(\w)He\s': r'\1on ',
    r'(\w)She\s': r'\1ona ',
    r'(\w)It\s': r'\1to ',
}

# Aplikuj zamiany
for pattern, replacement in patterns.items():
    content = re.sub(pattern, replacement, content, flags=re.IGNORECASE | re.MULTILINE)

# Zapisz
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Czyszczenie zakończone!")
print(f"📝 Plik: {filepath}")
