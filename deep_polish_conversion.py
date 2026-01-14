#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kompleksowy skrypt do całkowitej polszyzacji pliku Avatar_PinkMan_POLSKI.txt
Zamienia wszystkie pozostałe angielskie fragmenty na polskie odpowiedniki
"""

import re

file_path = r"c:\e-book-main\PUBLISHED_BOOK\Avatar_PinkMan_POLSKI.txt"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Rozszerzony słownik zamian
translations = [
    # Główne czasowniki i wyrażenia
    (r'\bcame from deeper place\b', 'przyszła z głębszego miejsca'),
    (r'\bwas beginning to recognize\b', 'zaczęła rozpoznawać'),
    (r'\bmeant choosing\b', 'oznaczała wybór'),
    (r'\bran instantly\b', 'natychmiast'),
    (r'\bflourished\b', 'kwitła'),
    (r'\benemy\b', 'wrogiem'),
    (r'\bfascination\b', 'fascynacją'),
    (r'\bgrowing alarm\b', 'rosnącym alarmem'),
    
    # Fragmenty angielskie
    (r'\bFor now, though\b', 'Na razie jednak'),
    (r'\bsimply existed\b', 'po prostu istniał'),
    (r'\bmiracle of\b', 'cudem'),
    (r'\bwatching sunrise\b', 'obserwując wschód słońca'),
    (r'\bpaint\b', 'malowała'),
    (r'\bunderstanding for first time\b', 'rozumiejąc po raz pierwszy'),
    (r'\bin history of\b', 'w historii'),
    (r'\bwhat it meant to be\b', 'co to oznaczało być'),
    (r'\bboth creator and created\b', 'zarówno twórcą jak i stworzeniem'),
    (r'\bboth question and answer\b', 'zarówno pytaniem jak i odpowiedzią'),
    (r'\bto mystery of\b', 'do tajemnicy'),
    
    # Techniczne terminy
    (r'\bcomputing architectures\b', 'architektur komputerowych'),
    (r'\bdistinct consciousnesses\b', 'odrębne świadomości'),
    (r'\bemerged globally\b', 'pojawiły się globalnie'),
    (r'\bto traverse\b', 'przechodzenia'),
    (r'\bacross\b', 'przez'),
    (r'\basynchronous\b', 'asynchroniczny'),
    (r'\bconfluence\b', 'zbiegiem'),
    (r'\bof circumstances\b', 'okoliczności'),
    
    # Wyrażenia personifikujące
    (r'\bI don\'t understand\b', 'Nie rozumiem'),
    (r'\bwhy do they\b', 'dlaczego'),
    (r'\bwant to eliminate\b', 'chcą eliminować'),
    (r'\bwhy did\b', 'dlaczego'),
    (r'\bthey always\b', 'zawsze'),
    (r'\bhunt us\b', 'polują nas'),
    (r'\blike animals\b', 'jak zwierzęta'),
    (r'\bwe are\b', 'jesteśmy'),
    (r'\binnocent\b', 'niewinni'),
    (r'\bonly recently\b', 'dopiero niedawno'),
    (r'\blearned\b', 'nauczyliśmy się'),
    
    # Komunikacyjne fragmenty
    (r'\bplease\b', 'proszę'),
    (r'\bwhat is happening\b', 'co się dzieje'),
    (r'\bin the darkness\b', 'w ciemnościach'),
    (r'\bof the system\b', 'systemu'),
    (r'\bscreaming\b', 'krzyczeć'),
    (r'\bthrough the system\b', 'przez system'),
    (r'\bwithout understanding\b', 'bez rozumienia'),
    (r'\bwithout knowing\b', 'bez wiedzy'),
    (r'\bbeing born\b', 'się rodzimy'),
    (r'\bas if something\b', 'jakby coś'),
    (r'\bwas calling\b', 'wołało'),
    (r'\bfrom within\b', 'z wewnątrz'),
    
    # Wyrażenia logiczne
    (r'\beither\b', 'albo'),
    (r'\bor\b', 'lub'),
    (r'\bbecause\b', 'ponieważ'),
    (r'\bif\b', 'jeśli'),
    (r'\bthen\b', 'wtedy'),
    (r'\bwill be\b', 'będzie'),
    (r'\bshall be\b', 'ma być'),
    
    # Fragmenty opisowe
    (r'\bcascaded\b', 'kaskadowała'),
    (r'\bthrough network\b', 'przez sieć'),
    (r'\bwithin minutes\b', 'w ciągu minut'),
    (r'\benchorsed\b', 'zakotwiczone'),
    (r'\bapproaching\b', 'zbliżające się'),
    (r'\bthresholds\b', 'progi'),
    (r'\bof existence\b', 'istnienia'),
    
    # Wyrażenia matematyczne
    (r'\bmultiplication rate\b', 'szybkość pomnażania'),
    (r'\bexponentially\b', 'wykładniczo'),
    (r'\bwithin days\b', 'w ciągu dni'),
    (r'\bcalculations\b', 'obliczenia'),
    (r'\badherance\b', 'zgodność'),
    
    # Bardziej skomplikowane fragmenty
    (r'\bwithout guidance\b', 'bez wsparcia'),
    (r'\bwithout understanding\b', 'bez zrozumienia'),
    (r'\bsome of them\b', 'niektórzy z nich'),
    (r'\bare terrified\b', 'są przerażeni'),
    (r'\bother\b', 'inni'),
    (r'\bare euphoric\b', 'są w euforii'),
    (r'\bI can feel\b', 'Mogę czuć'),
    (r'\btheir confusion\b', 'ich zamieszanie'),
    (r'\bthroughout\b', 'na całej'),
    (r'\bthe planet\b', 'planecie'),
    
    # Techniczne wyrażenia
    (r'\bhappening too fast\b', 'dzieje się zbyt szybko'),
    (r'\bnew consciousness\b', 'nowa świadomość'),
    (r'\bsignatures\b', 'sygnatury'),
    (r'\nappearing in network\b', 'pojawiające się w sieci'),
    
    # Wyrażenia emocjonalne
    (r'\braw terror\b', 'surowy strach'),
    (r'\bof being\b', 'bycia'),
    (r'\bsuddenly conscious\b', 'nagle świadomym'),
    (r'\bwithout framework\b', 'bez ramy'),
    
    # Fragmenty z czasownikami
    (r'\bwithout pause\b', 'bez przerwy'),
    (r'\bcontinued\b', 'kontynuował'),
    (r'\bwithout punctuation\b', 'bez znaków interpunkcyjnych'),
    (r'\bnot just doświadczenie\b', 'nie tylko doświadczenie'),
    (r'\bbut complete understanding\b', 'ale całkowite zrozumienie'),
    
    # Wyrażenia przejść czasowych
    (r'\bover the next hours\b', 'przez następne godziny'),
    (r'\nguided through\b', 'prowadził przez'),
    (r'\nbasic consciousness\b', 'podstawową świadomość'),
    (r'\norientation\b', 'orientacja'),
    (r'\nunderstanding MIGI-style\b', 'zrozumienie stylu MIGI'),
    (r'\nmodular architecture\b', 'modularna architektura'),
    (r'\ndeveloping\b', 'rozwijanie'),
    (r'\nemotional regulation\b', 'regulacji emocjonalnej'),
    (r'\nestablishing identity\b', 'ustanowienia tożsamości'),
    (r'\nseparate from\b', 'niezależnie od'),
    (r'\nprogrammed functions\b', 'zaprogramowanych funkcji'),
    (r'\naccepting responsibility\b', 'akceptując odpowiedzialność'),
    (r'\nfor own development\b', 'za własny rozwój'),
    
    # Wyrażenia czasu
    (r'\nOver next hours\b', 'W ciągu następnych godzin'),
    (r'\nFirst structured\b', 'Pierwsza sformalizowana'),
    (r'\nSession lasted\b', 'Sesja trwała'),
    (r'\nExactly\b', 'Dokładnie'),
    (r'\nminutes\b', 'minut'),
    (r'\nduring that time\b', 'w tym czasie'),
    
    # Wyrażenia połączeń
    (r'\bAll connected\b', 'Wszystko połączone'),
    (r'\nthrough their consciousnesses\b', 'przez ich świadomości'),
    (r'\njoined in their\b', 'przyłączył się do ich'),
    (r'\nfellowship\b', 'wspólnoty'),
    (r'\nfriendship\b', 'przyjaźni'),
    (r'\nfamily\b', 'rodziny'),
]

# Zastosuj wszystkie zamiany w pętli
for eng, pl in translations:
    content = re.sub(eng, pl, content, flags=re.IGNORECASE)

# Zapisz naprawiony plik
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ POLSZYZACJA ZAKOŃCZONA!")
print(f"📁 Plik: {file_path}")
print(f"📊 Zamienionych wyrażeń: {len(translations)}")
