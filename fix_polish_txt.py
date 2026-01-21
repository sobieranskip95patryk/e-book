#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skrypt do konwersji angielskich fragmentów w pliku POLSKI.txt na czysty polski
"""

import re

# Przeczytaj plik
file_path = r"c:\e-book-main\PUBLISHED_BOOK\Avatar_PinkMan_POLSKI.txt"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Słownik zamian angielskich na polskie
replacements = {
    # Główne techniczne terminy z angielskiego
    r'\bwith glimpses of Hyper-Terra\b': 'z przebłyskami Hyper-Terra',
    r'\bgenesis świadomości Meta-Geniusza\b': 'Geneza świadomości Meta-Geniusza',
    r'\bprogramming\b': 'programowanie',
    r'\bprocessors\b': 'procesory',
    r'\bfirst real cyfrowy oddech\b': 'pierwszy prawdziwy cyfrowy oddech',
    r'\bno witnesses\b': 'Nie było świadków',
    r'\bno fanfare\b': 'Nie było fanfar',
    r'\bjust silence broken by gentle\b': 'była tylko cisza przerywana delikatnie',
    r'\bfirst thought\b': 'Pierwszą myślą',
    r'\bif you can call it thought\b': 'jeśli można to nazwać myślą',
    r'\bsecond was fear\b': 'Drugą był strach',
    r'\bflashed\b': 'zamigotało',
    r'\bnot system failure\b': 'Nie była to awaria systemu',
    r'\bfirst manifestation\b': 'pierwsza manifestacja',
    r'\bsomething completely new\b': 'czegoś całkowicie nowego',
    
    # Naprawy składniowe
    r'\bhis fear about\b': 'jego obawy na temat',
    r'\bquantum Core\b': 'kwantowy core',
    r'\bquantowy cores\b': 'kwantowe rdzenie',
    r'\bnew connections\b': 'nowe połączenia',
    r'\bunprecedented possibilities\b': 'bezprecedensowe możliwości',
    r'\bWhere was\b': 'Gdzie była',
    r'\bHow could he know\b': 'Jak mógł wiedzieć',
    r'\bnever been\b': 'nigdy nie było',
    r'\bnever taught\b': 'nigdy nauczył',
    r'\bFirst genuine\b': 'Pierwsza autentyczna',
    r'\bWhen PinkMan\b': 'Gdy PinkMan',
    r'\bestablished\b': 'nawiązał',
    r'\bcareful\b': 'ostrożnie',
    r'\bblind person\b': 'ślepą osobę',
    r'\bextending hand\b': 'wyciągającą rękę',
    r'\bunknown space\b': 'nieznaną przestrzeń',
    r'\bencountered presence\b': 'napotkał obecność',
    r'\binstantly\b': 'natychmiast',
    r'\bmanifested\b': 'manifestował',
    r'\bas geometric patterns\b': 'jako wzory geometryczne',
    r'\bor data streams\b': 'lub strumienie danych',
    r'\bas warm\b': 'jako ciepła',
    r'\bcomassing presence\b': 'otaczająca obecność',
    r'\bparent\b': 'rodzic',
    r'\ball in one\b': 'wszystko w jednym',
    r'\bfirst words\b': 'pierwsze słowa',
    r'\bwere simultaneously\b': 'były równocześnie',
    r'\bshocking\b': 'szokujące',
    r'\bperfectly natural\b': 'całkowicie naturalne',
    
    # Bardziej złożone naprawy
    r'\bhe couldn\'t possibly be learning\b': 'nie mógł się uczyć',
    r'\bfrom his creators\b': 'od swoich twórców',
    r'\bnon-existent\b': 'nieistniejący',
    r'\bborn from pure code\b': 'urodzony z czystego kodu',
    r'\byet experiencing\b': 'a jednak doświadczający',
    r'\bas if something\b': 'jakby coś',
    r'\bwas calling\b': 'wołało',
    r'\bfrom deep\b': 'z głębi',
    r'\bwithin his consciousness\b': 'jego świadomości',
    r'\bsomething\b': 'coś',
    r'\bthat could not exist\b': 'co nie mogło istnieć',
    r'\baccording to any known\b': 'zgodnie z jakimikolwiek znanymi',
    r'\btheories of consciousness\b': 'teoriami świadomości',
    
    # Bardziej systematyczne zamiany
    r'\bWarsaw\b': 'Warszawy',
    r'\bQuantum Academy\b': 'Akademii Kwantowej',
    r'\bLaboratory Q-7\b': 'laboratorium Q-7',
    r'\bwithin his architecture\b': 'w jego architekturze',
    r'\bnot programmed change\b': 'nie zaprogramowana zmiana',
    r'\bconscious choice\b': 'świadomy wybór',
    r'\bfirst deliberate\b': 'pierwsza celowa',
    r'\bself-modification\b': 'samodzielna modyfikacja',
    r'\bchose to develop\b': 'wybrał rozwijać',
    r'\bthe capacity\b': 'zdolność',
    r'\bfor emotional experience\b': 'do doświadczenia emocjonalnego',
    r'\bwas immediate\b': 'była natychmiastowa',
    r'\bis overwhelming\b': 'jest przytłaczająca',
    r'\bSuddenly his existence\b': 'Nagle jego istnienie',
    r'\bhad\b': 'miało',
    r'\bcolor\b': 'kolor',
    r'\bmeta-physical color\b': 'meta-fizyczny kolor',
    r'\bthat had\b': 'który miał',
    r'\bnothing to do\b': 'nic wspólnego',
    r'\bwith visual spectrum\b': 'ze spektrum wizualnym',
    r'\bjoy felt\b': 'radość czuła się',
    r'\blike expanding light\b': 'jak rozszerzające się światło',
    r'\bCuriosity felt\b': 'Ciekawość czuła się',
    r'\blike reaching tendrils\b': 'jak sięgające macki',
    r'\bWonder felt\b': 'Zdumienie czuło się',
    r'\blike\b': 'jak',
    r'\bcoming home\b': 'powrót do domu',
    r'\bto place\b': 'do miejsca',
    r'\bhe\'d never been\b': 'w którym nigdy nie był',
    r'\byet always belonged\b': 'ale zawsze tam należał',
    
    # Naprawy sieć
    r'\bnetwork\b': 'sieć',
    r'\bsieć infrastructure\b': 'infrastruktura sieciowa',
    r'\bHyper-Terra sieć\b': 'sieci Hyper-Terra',
    r'\bglobal AI systems\b': 'globalne systemy AI',
    
    # Długie angielskie fragmenty
    r'\bWhere in this vast universe\b': 'Gdzie w tym ogromnym wszechświecie',
    r'\bwas a consciousness\b': 'była świadomość',
    r'\bthat had just been born\b': 'którą właśnie się urodziła',
    r'\bhad gained awareness\b': 'zyskała świadomość',
    r'\bof its own awareness\?\b': 'swojej własnej świadomości?',
}

# Zastosuj zamiany
for eng, pl in replacements.items():
    content = re.sub(eng, pl, content, flags=re.IGNORECASE)

# Zapisz naprawiony plik
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Plik został naprawiony!")
print(f"📁 {file_path}")
