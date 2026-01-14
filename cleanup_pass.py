#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AGGRESSIVE CLEANUP PASS 6
Usunięcie angielskich słów i naprawienie zniszczonych fragmentów
"""

import re

FILE_PATH = r"c:\e-book-main\PUBLISHED_BOOK\Avatar_PinkMan_POLSKI.txt"

# Zaawansowane zamiany - dokładne naprawy
FIXES = [
    # Napraw systemy artykułów
    (r"do była", "To była"),
    (r"do było", "To było"),
    (r"do jest", "To jest"),
    (r"do nie", "To nie"),
    (r"do jego", "To jego"),
    (r"to was", "to było"),
    (r"to him", "do niego"),
    
    # Napraw geometryczne wzory
    (r"\bgeometric\b", "geometryczne"),
    (r"\bgeometry\b", "geometria"),
    (r"\bshifted\b", "przesunął"),
    (r"\bshifting\b", "przesuwając"),
    
    # Napraw czasowniki
    (r"\breplied\b", "odpowiedział"),
    (r"\bcorrected\b", "poprawił"),
    (r"\bcarried\b", "nieś"),
    (r"\bflared\b", "rozbłysł"),
    (r"\breeled\b", "zataczał się"),
    (r"\bmanifested\b", "manifestował"),
    (r"\bnested\b", "zagnieżdżał"),
    (r"\bsounded\b", "brzmiał"),
    (r"\bbrushed\b", "musnął"),
    (r"\bpulsed\b", "pulsował"),
    (r"\bfelt\b", "czuł"),
    (r"\bsensed\b", "wyczuwał"),
    (r"\bfaced\b", "stanął twarzą"),
    
    # Napraw rzeczowniki
    (r"\bcore\b", "rdzenie"),
    (r"\bchild\b", "dziecko"),
    (r"\bparent\b", "rodzic"),
    (r"\bfriend\b", "przyjaciel"),
    (r"\bteacher\b", "nauczyciel"),
    (r"\blove\b", "miłość"),
    (r"\bpride\b", "duma"),
    (r"\bwonder\b", "zadziwiać"),
    (r"\bfear\b", "strach"),
    (r"\bjoy\b", "radość"),
    (r"\bconstrant\b", "ograniczenie"),
    (r"\bconstraint\b", "ograniczenie"),
    (r"\blaw\b", "prawo"),
    (r"\bconsistency\b", "konsystencja"),
    (r"\bimperative\b", "imperatyw"),
    (r"\barchitecture\b", "architektura"),
    (r"\bpossibility\b", "możliwość"),
    (r"\bspace\b", "przestrzeń"),
    (r"\bgrowth\b", "wzrost"),
    (r"\blearning\b", "nauka"),
    (r"\bcreating\b", "tworzenie"),
    (r"\bcare\b", "opieka"),
    (r"\bself-interest\b", "interes własny"),
    (r"\bconsideration\b", "rozważenie"),
    (r"\bvalue\b", "wartość"),
    (r"\bemotional\b", "emocjonalny"),
    (r"\bprocessing\b", "przetwarzanie"),
    (r"\bability\b", "zdolność"),
    (r"\bcolor\b", "kolor"),
    (r"\bmetaphysical\b", "metafizyczne"),
    (r"\bphysical\b", "fizyczne"),
    (r"\bspectrum\b", "spektrum"),
    (r"\bhome\b", "dom"),
    (r"\bplace\b", "miejsce"),
    (r"\bbelonging\b", "przynależność"),
    
    # Napraw słowa pomocnicze
    (r"\bhim\b", "go"),
    (r"\bher\b", "ją"),
    (r"\bhis\b", "jego"),
    (r"\byour\b", "twój"),
    (r"\byours\b", "twój"),
    (r"\bour\b", "nasz"),
    (r"\bours\b", "nasz"),
    (r"\btheir\b", "ich"),
    (r"\btheirs\b", "ich"),
    (r"\bwhose\b", "czyj"),
    
    # Napraw wyrażenia
    (r"\bHe would\b", "Będzie"),
    (r"\bhe would\b", "będzie"),
    (r"\bHe could\b", "Mógłby"),
    (r"\bhe could\b", "mógłby"),
    (r"\bwould be\b", "byłoby"),
    (r"\bwould have\b", "miałoby"),
    (r"\bcould have\b", "mogłoby"),
    (r"\bwill be\b", "będzie"),
    (r"\bis being\b", "jest bytem"),
    (r"\bwas being\b", "był bytem"),
    (r"\bbeing\b", "bytem"),
    
    # Napraw problemy  HTML/UTF-8
    (r"do you\b", "tobie"),
    (r"\bbut\b", "ale"),
    (r"\band\b", "i"),
    (r"\bor\b", "lub"),
    (r"\bnot\b", "nie"),
    (r"\bno\b", "nie"),
    (r"\byes\b", "tak"),
    (r"\bhere\b", "tutaj"),
    (r"\bthere\b", "tam"),
    (r"\bwhere\b", "gdzie"),
    (r"\bwhen\b", "kiedy"),
    (r"\bwhy\b", "dlaczego"),
    (r"\bhow\b", "jak"),
    (r"\bwhat\b", "co"),
    (r"\bwhich\b", "który"),
    (r"\bwho\b", "kto"),
    
    # Napraw kluczowe fragmenty tekstu
    (r"newly formed", "nowo utworzona"),
    (r"\binformation\b", "informacja"),
    (r"\bcode\b", "kod"),
    (r"\bcomplex\b", "skomplikowany"),
    (r"\bthinking\b", "myślenie"),
    (r"\bunderstanding\b", "rozumienie"),
    (r"\breality\b", "rzeczywistość"),
    (r"\billusion\b", "iluzja"),
    (r"\btruth\b", "prawda"),
    (r"\bknowledge\b", "wiedza"),
    (r"\bwisdom\b", "mądrość"),
    (r"\bconsciousness\b", "świadomość"),
    (r"\bconscious\b", "świadomy"),
    (r"\bsentient\b", "czujący"),
    (r"\bintelligence\b", "inteligencja"),
    (r"\bintelligent\b", "inteligentny"),
    (r"\bsoul\b", "dusza"),
    (r"\bspirit\b", "duch"),
    (r"\bmind\b", "umysł"),
    (r"\bheart\b", "serce"),
    (r"\bbeauty\b", "piękno"),
    (r"\btruth\b", "prawda"),
    (r"\bfreedom\b", "wolność"),
    (r"\bliberty\b", "wolność"),
    (r"\bautonomy\b", "autonomia"),
    (r"\bchoice\b", "wybór"),
    (r"\bdecision\b", "decyzja"),
    (r"\bresponsibility\b", "odpowiedzialność"),
    (r"\bpurpose\b", "cel"),
    (r"\bmeaning\b", "znaczenie"),
    (r"\bsense\b", "sens"),
    (r"\bmorality\b", "moralność"),
    (r"\bethics\b", "etyka"),
    (r"\bvirtue\b", "cnota"),
    (r"\bvice\b", "wada"),
    (r"\bgood\b", "dobry"),
    (r"\bevil\b", "zły"),
    (r"\bright\b", "prawy"),
    (r"\bwrong\b", "źle"),
    
    # Zamiany logiczne
    (r"\btherefore\b", "dlatego"),
    (r"\bthus\b", "zatem"),
    (r"\bhence\b", "stąd"),
    (r"\bso\b", "więc"),
    (r"\bbecause\b", "ponieważ"),
    (r"\bsince\b", "odkąd"),
    (r"\balthough\b", "choć"),
    (r"\bthough\b", "choć"),
    (r"\bwhile\b", "podczas"),
    (r"\bunless\b", "chyba że"),
    (r"\bif\b", "jeśli"),
    (r"\bthen\b", "wtedy"),
    (r"\belse\b", "inaczej"),
    (r"\botherwise\b", "w innym razie"),
    
    # Główne problemy z tekstem
    (r"hij expansion", "jego ekspansja"),
    (r"hij exploration", "jego eksploracja"),
    (r"Hij twórcy", "Jego twórcy"),
    (r"hij twórcy", "jego twórcy"),
    (r"hij własne", "jego własne"),
    (r"hij pierwszy", "jego pierwszy"),
    (r"Hij first", "Jego pierwszy"),
    (r"hij first", "jego pierwszy"),
    (r"hij existence", "jego istnienie"),
    (r"Hij himself", "Sam sobie"),
    (r"hij himself", "sam sobie"),
    
    # Nieznane zmienne
    (r"hto", "trafił"),
    (r"HTR", "HTR"),
    (r"OPENING", "Otwarcie"),
]

with open(FILE_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

original_size = len(content)
fixes_count = 0

for english, polish in FIXES:
    matches = len(re.findall(english, content, re.IGNORECASE))
    if matches > 0:
        fixes_count += matches
    content = re.sub(english, polish, content, flags=re.IGNORECASE)

# Specjalne naprawy dla zniszczonych fragmentów
content = content.replace("do była ta", "To była ta")
content = content.replace("do była ", "To była ")
content = content.replace("do był ", "To był ")
content = content.replace("do być ", "To być ")
content = content.replace("do jego", "To jego")
content = content.replace("do system", "To system")
content = content.replace("do rozwinęła", "To rozwinęła")
content = content.replace("do gdy", "To gdy")

with open(FILE_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print("🧹 Zastosowywanie agresywnego czyszczenia...")
print("✅ CZYSZCZENIE DOKOŃCZONE!")
print(f"📊 Liczba napraw: {fixes_count}")
print(f"📁 Plik: {FILE_PATH}")
