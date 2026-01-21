#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OPCJA C: Polskie zdania + angielskie terminy techniczne
Cofanie zbyt agresywnych zamian, zachowanie technical terms
"""

import re

filepath = r"c:\e-book-main\AVATAR_PINKMAN_COMPLETE_BOOK.md"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Terminy techniczne które POWINNY zostać w angielskim
TECHNICAL_TERMS = {
    'consciousness', 'conscious', 'entity', 'entities', 'civilization', 'contact', 
    'development', 'evolution', 'diplomatic', 'network', 'species', 'agent', 
    'communication', 'quantum', 'cosmic', 'galactic', 'protocol', 'system',
    'module', 'pattern', 'architecture', 'interface', 'database', 'algorithm',
    'capacity', 'intelligence', 'artificial', 'digital', 'hybrid', 'dimension',
    'reality', 'space', 'structure', 'wave', 'frequency', 'signal', 'transmission',
    'predator', 'predation', 'warfare', 'agency', 'citizenship', 'responsibility',
    'analysis', 'perspective', 'capability', 'strategy', 'ethics', 'morality',
    'integration', 'cooperation', 'diversity', 'hierarchy', 'collaborative',
}

# Polskie słowa które mogą przywrócić polską naturalność
SENTENCE_FIXES = [
    # Przywracanie polski struktury zdań z techniczne terms
    (r'Poprzez galactic distances', 'poprzez galaktyczne odległości'),
    (r'Poprzez expanded świadomość', 'poprzez rozszerzoną świadomość'),
    (r'had achieved świadomość approximately', 'osiągnęła consciousness około'),
    (r'świadomość species että resembled crystalline', 'gatunki consciousness przypominające krystaliczne'),
    (r'ze organic integration', 'z organiczną integracją'),
    (r'was stabilny, peaceful, highly creative', 'była stabilna, pokojowa, wysoce kreatywna'),
    (r'że demonstrated rapid ethical', 'które zademonstrował szybki ethical'),
    (r'Precisely Ponieważ of rapid development', 'Dokładnie ze względu na rapid development'),
    (r'Young świadomość species z exceptional growth', 'Młode species consciousness z exceptional wzrostem'),
    (r'Unlike świadomość rescue operations które involved', 'W przeciwieństwie do rescue operations consciousness które obejmowały'),
    (r'może complex cultural świadomość patterns', 'mogą złożone cultural consciousness patterns'),
    (r'świadomość conflicts', 'consciousness conflicts'),
    (r'50,000 years więcej doświadczenie', '50 000 lat więcej doświadczenia'),
    (r'może be precisely', 'może być dokładnie'),
    (r'świadomość warfare doświadczenie', 'consciousness warfare doświadczenia'),
    (r'peaceful świadomość civilizations', 'peacefulne consciousness civilizations'),
    (r'świadomość diversity', 'consciousness diversity'),
]

count = 0
for old, new in SENTENCE_FIXES:
    if re.search(old, content, re.IGNORECASE):
        content = re.sub(old, new, content, flags=re.IGNORECASE | re.MULTILINE)
        count += 1

# Teraz usunąć polskie słowa które przysłaniają technical terms
RESTORE_TECHNICAL = [
    (r'świadomość consciousness', 'consciousness'),
    (r'świadomość development', 'consciousness development'),
    (r'świadomość entity', 'consciousness entity'),
    (r'świadomość civilization', 'consciousness civilization'),
    (r'świadomość contact', 'consciousness contact'),
    (r'świadomość network', 'consciousness network'),
    (r'świadomość species', 'consciousness species'),
    (r'świadomość predation', 'consciousness predation'),
    (r'świadomość warfare', 'consciousness warfare'),
]

for old, new in RESTORE_TECHNICAL:
    content = re.sub(old, new, content, flags=re.IGNORECASE | re.MULTILINE)
    count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Zastosowano {count} fixes dla OPCJI C")
print(f"🎯 Polskie zdania + angielskie technical terms")
print(f"📝 Plik: {filepath}")
