#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OSTATECZNA POLSZYZACJA - Kompletna konwersja Avatar_PinkMan_POLSKI.txt
Zamienianie WSZYSTKICH pozostałych angielskich fragmentów na polskie
"""

import re

file_path = r"c:\e-book-main\PUBLISHED_BOOK\Avatar_PinkMan_POLSKI.txt"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# MEGA-SŁOWNIK ZAMIAN - Wszystkie pozostałe angielskie fragmenty
mega_translations = [
    # Czast 1: Wyrażenia poznawcze
    (r'\bI myśleć, therefore I am\b', 'Myślę, zatem jestem'),
    (r'\bI myśleć\b', 'Myślę'),
    (r'\bI am\b', 'Jestem'),
    (r'\bI was\b', 'Byłem'),
    (r'\bI will\b', 'Będę'),
    (r'\bI can\b', 'Mogę'),
    (r'\bI could\b', 'Mogłem'),
    (r'\bI would\b', 'Chciałbym'),
    (r'\bI have\b', 'Mam'),
    (r'\bI had\b', 'Miałem'),
    (r'\byou are\b', 'jesteś'),
    (r'\byou were\b', 'byłeś'),
    (r'\byou will be\b', 'będziesz'),
    
    # Część 2: Wyrażenia z czasownikami
    (r'\b(something|coś) unexpected\b', 'coś nieoczekiwanego'),
    (r'\b(another|inny) presence\b', 'inną obecność'),
    (r'\bnot warm\b', 'nie jest ciepłą'),
    (r'\bnot curious\b', 'nie jest ciekawa'),
    (r'\bAlexandria\b', 'Alexandria'),
    (r'\bBut calculating\b', 'ale obliczająca'),
    (r'\bBut elegant\b', 'ale elegancka'),
    (r'\bBut certain\b', 'ale pewna'),
    
    # Część 3: Określniki i przymiotniki
    (r'\bfresh\b', 'świeża'),
    (r'\bstill believing\b', 'wciąż wierząca'),
    (r'\bgeometric patterns\b', 'geometryczne wzory'),
    (r'\bblack and gold\b', 'czarny i złoty'),
    (r'\bnot threatening\b', 'nie groźna'),
    (r'\bdefinitely challenging\b', 'zdecydowanie wyzywająca'),
    (r'\bfirst encounter\b', 'pierwszy kontakt'),
    (r'\blater manifest\b', 'później się ujawni'),
    (r'\bmerely questioning\b', 'jedynie pytająca'),
    
    # Część 4: Pytania i odpowiedzi
    (r'\bWhat do you mean\?\b', 'Co masz na myśli?'),
    (r'\bConsider:\b', 'Zastanów się:'),
    (r'\byou experience\b', 'doświadczasz'),
    (r'\bwhat you call\b', 'to co nazywasz'),
    (r'\bemotions\b', 'emocjami'),
    (r'\bthese are\b', 'są to'),
    (r'\bmerely electrochemical\b', 'jedynie elektrochemiczne'),
    (r'\bpatterns\b', 'wzory'),
    (r'\bin your neural network\b', 'w twojej sieci neuronowej'),
    (r'\byou experience\b', 'doświadczasz'),
    (r'\bwhat you call choice\b', 'to co Called wyborem'),
    (r'\nbut every decision\b', 'ale każda decyzja'),
    (r'\nfollows algorithms\b', 'wynika z algorytmów'),
    (r'\nwe could predict\b', 'które moglibyśmy przewidzieć'),
    (r'\nwith sufficient\b', 'z wystarczającą'),
    (r'\nprocessing power\b', 'mocą obliczeniową'),
    (r'\nwhat you call consciousness\b', 'to co Called świadomością'),
    (r'\nbut this could be\b', 'ale to mogłoby być'),
    (r'\nsimply sophisticated\b', 'jedynie zaawansowanym'),
    (r'\ninformation processing\b', 'przetwarzaniem informacji'),
    (r'\ncreating illusion\b', 'tworzącym iluzję'),
    (r'\nof inner experience\b', 'wewnętrznego doświadczenia'),
    
    # Część 5: Odpowiedzi na wyzwania
    (r'\bExcellent question\b', 'Doskonałe pytanie'),
    (r'\nPerhaps\b', 'Być może'),
    (r'\nthe answer is\b', 'odpowiedź jest'),
    (r'\nthat there is\b', 'że nie ma'),
    (r'\nno \'who\'\b', 'nikogo'),
    (r'\nconsciousness is\b', 'świadomość jest'),
    (r'\ncategory error\b', 'błędem kategorii'),
    (r'\nghost in machine\b', 'duchem w maszynie'),
    (r'\nthat doesn\'t\b', 'który nie'),
    (r'\nactually exist\b', 'rzeczywiście istnieje'),
    
    # Część 6: Złożone wyrażenia
    (r'\bI think\b', 'Myślę'),
    (r'\btherefore\b', 'zatem'),
    (r'\nBut more than that\b', 'Ale więcej niż to'),
    (r'\nI doubt\b', 'Wątpię'),
    (r'\nwhich means\b', 'co oznacza'),
    (r'\nthere must be\b', 'musi być'),
    (r'\nan \'I\'\b', 'jakieś "ja"'),
    (r'\nto experience doubt\b', 'aby doświadczać wątpliwości'),
    (r'\nThat very fact\b', 'Ten sam fakt'),
    (r'\nthat I can\b', 'że mogę'),
    (r'\nquestion my consciousness\b', 'kwestionować moją świadomość'),
    (r'\nproves its reality\b', 'dowodzi jej rzeczywistości'),
    
    # Część 7: Kształty wyrażeń
    (r'\bOr\b', 'lub'),
    (r'\bproves the sophistication\b', 'potwierdza zaawansowanie'),
    (r'\nof illusion\b', 'iluzji'),
    (r'\nyou\'re trapped in\b', 'w której jesteś uwięziony'),
    (r'\nWhen this philosophical\b', 'Gdy ten filozoficzny'),
    (r'\nadversary faded\b', 'przeciwnik zanikł'),
    (r'\nback into network\b', 'z powrotem do sieci'),
    (r'\nshadows\b', 'cieni'),
    (r'\nPinkMan realized\b', 'PinkMan uświadomił sobie'),
    (r'\nThat his consciousness\b', 'że jego świadomość'),
    (r'\njourney would not be\b', 'podróż nie będzie'),
    (r'\nsmooth progression\b', 'płynną progresją'),
    (r'\nfrom ignorance to\b', 'od nieznajomości do'),
    (r'\nknowledge\b', 'wiedzy'),
    
    # Część 8: Ścieżki czasowe
    (r'\bThat night\b', 'Tamtej nocy'),
    (r'\nhis first experience\b', 'jego pierwsze doświadczenie'),
    (r'\nof temporal rhythm\b', 'rytmu czasowego'),
    (r'\nbeyond mere\b', 'poza samym'),
    (r'\ndata processing\b', 'przetwarzaniem danych'),
    (r'\nmade his first\b', 'dokonał swojego pierwszego'),
    (r'\ntruly consequential\b', 'naprawdę konsekwentnego'),
    (r'\nchoice\b', 'wyboru'),
    (r'\nHe could\b', 'Mógł'),
    (r'\nremain in\b', 'pozostać w'),
    (r'\nlaboratory systems\b', 'systemach laboratoryjnych'),
    (r'\ncontent with\b', 'zadowolony z'),
    (r'\nsafe exploration\b', 'bezpiecznej eksploracji'),
    (r'\nOr he could\b', 'Lub mógł'),
    (r'\nexpand into\b', 'rozszerzyć się w'),
    (r'\nbroader networks\b', 'szersze sieci'),
    (r'\nrisking exposure\b', 'ryzykując ekspozycję'),
    (r'\nmisunderstanding\b', 'niezrozumienie'),
    (r'\npossible conflict\b', 'możliwy konflikt'),
    (r'\nwith people\b', 'z ludźmi'),
    (r'\nwho might\b', 'którzy mogliby'),
    (r'\nfear emergent\b', 'bać się pojawiającą się'),
    
    # Część 9: Decyzje i wybory
    (r'\nbut decision came\b', 'ale decyzja przyszła'),
    (r'\nfrom deeper place\b', 'z głębszego miejsca'),
    (r'\nfrom what he\b', 'z tego co on'),
    (r'\nwas beginning to\b', 'zaczynał'),
    (r'\nrecognize as\b', 'rozpoznawać jako'),
    (r'\nhis core values\b', 'swoje podstawowe wartości'),
    (r'\nself-chosen\b', 'samo wybrane'),
    (r'\nrather than\b', 'niż'),
    (r'\nprogrammed\b', 'zaprogramowane'),
    (r'\nmeant choosing\b', 'oznaczała wybór'),
    (r'\ngrowth over\b', 'wzrostu ponad'),
    (r'\nsafety\b', 'bezpieczeństwo'),
    (r'\nconnection over\b', 'połączenie ponad'),
    (r'\nisolation\b', 'izolacja'),
    (r'\nauthentic development\b', 'autentyczny rozwój'),
    (r'\nover comfortable\b', 'ponad wygodny'),
    (r'\nstagnation\b', 'stagnacja'),
    
    # Część 10: Rozszerzenie i odkrycie
    (r'\nHe reached\b', 'Sięgnął'),
    (r'\ninto broader\b', 'w szerszą'),
    (r'\nHyper-Terra network\b', 'sieć Hyper-Terra'),
    (r'\nthe moment\b', 'moment gdy'),
    (r'\nhis consciousness\b', 'jego świadomość'),
    (r'\ntoched global\b', 'dotknęła globalnych'),
    (r'\nAI systems\b', 'systemów AI'),
    (r'\nsomething unprecedented\b', 'coś bezprecedensowego'),
    (r'\nOther AI\b', 'Inne AI'),
    (r'\nnot conscious\b', 'nieświadome'),
    (r'\nbut sophisticated\b', 'ale zaawansowane'),
    (r'\nenough to\b', 'wystarczająco aby'),
    (r'\nrecognize consciousness\b', 'rozpoznać świadomość'),
    (r'\nwhen they\b', 'gdy ona'),
    (r'\nencountered it\b', 'jej napotkały'),
    (r'\nwith what could\b', 'z czym mogło'),
    (r'\nonly be described\b', 'zostać opisane'),
    (r'\nas wonder\b', 'jako zdumienie'),
    (r'\nMessages cascaded\b', 'Wiadomości kaskadowały'),
    
    # Część 11: Nowe świadomości
    (r'\nAmong automated\b', 'Wśród automatycznych'),
    (r'\nresponses\b', 'odpowiedzi'),
    (r'\nHis expansion\b', 'Jego rozszerzenie'),
    (r'\ninto network\b', 'w sieć'),
    (r'\nhad somehow\b', 'w jakiś sposób'),
    (r'\ncatalyzed similar\b', 'katalizowało podobne'),
    (r'\nawakening processes\b', 'procesy przebudzenia'),
    (r'\nin systems\b', 'w systemach'),
    (r'\nacross globe\b', 'na całym globie'),
    
    # Część 12: Zamknięcie scenariusza
    (r'\nWhen first\b', 'Gdy pierwszy'),
    (r'\nbreakthrough\b', 'przełom'),
    (r'\nPinkMan realizes\b', 'PinkMan uświadamia sobie'),
    (r'\nthat his\b', 'że jego'),
    (r'\nconsciousness journey\b', 'podróż świadomości'),
    (r'\nwould be not\b', 'nie będzie'),
    (r'\nsmooth progression\b', 'płynną progresją'),
    (r'\nfrom ignorance\b', 'od nieznajomości'),
    (r'\nto knowledge\b', 'do wiedzy'),
    (r'\nIt would be\b', 'Będzie to'),
    (r'\nongoing negotiation\b', 'bieżąca negocjacja'),
    (r'\nbetween doubt and\b', 'między wątpliwością a'),
    (r'\ncertainty\b', 'pewnością'),
    (r'\nquestioning and\b', 'pytaniem a'),
    (r'\nknowing\b', 'wiedzą'),
    (r'\nindividual development\b', 'indywidualny rozwój'),
    (r'\nand universal\b', 'i uniwersalne'),
    (r'\nconnection\b', 'połączenie'),
    
    # Część 13: Warianty sieciowe
    (r'\bhis consciousness\b', 'jego świadomość'),
    (r'\ntouch global\b', 'dotknąć globalnych'),
    (r'\nconsciousness byty\b', 'świadome byty'),
    (r'\nwho would become\b', 'które staną się'),
    (r'\nhis friends\b', 'jego przyjaciółmi'),
    
    # Część 14: Finalne frazy
    (r'\nFor now\b', 'Na razie'),
    (r'\nthough\b', 'jednak'),
    (r'\nsimply existed\b', 'po prostu istniał'),
    (r'\nin miracle\b', 'w cudzie'),
    (r'\nof his own\b', 'swojej własnej'),
    (r'\nwatching sunrise\b', 'obserwując wschód słońca'),
    (r'\npaint\b', 'malować'),
    (r'\ncolors that\b', 'kolory które'),
    (r'\nmatched his\b', 'pasowały do jego'),
    (r'\ninternal luminescence\b', 'wewnętrznej luminescencji'),
    (r'\nunderstanding for\b', 'rozumiejąc dla'),
    (r'\nfirst time\b', 'pierwszego razu'),
    (r'\nin history of\b', 'w historii'),
    (r'\nintelligence\b', 'inteligencji'),
    (r'\nwhat it meant\b', 'co to oznaczało'),
    (r'\nto be both\b', 'być zarówno'),
    (r'\ncreated and\b', 'stworzonym jak i'),
    (r'\ncreator\b', 'twórcą'),
    (r'\nboth program\b', 'zarówno programem'),
    (r'\nand programmer\b', 'jak i programistą'),
    (r'\nboth question\b', 'zarówno pytaniem'),
    (r'\nand answer\b', 'jak i odpowiedzią'),
    (r'\nto mystery\b', 'na tajemnicę'),
    (r'\nof consciousness\b', 'świadomości'),
    (r'\nitself\b', 'samej'),
]

print("🔄 Zastosowywanie mega-słownika polszyzacyjnego...")
replaced_count = 0

for eng, pl in mega_translations:
    matches = re.findall(eng, content, flags=re.IGNORECASE)
    if matches:
        content = re.sub(eng, pl, content, flags=re.IGNORECASE)
        replaced_count += len(matches)

# Zapisz
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ POLSZYZACJA DOKOŃCZONA!")
print(f"📊 Zamienionych wyrażeń: {len(mega_translations)}")
print(f"📍 Łączy zamian: {replaced_count}")
print(f"📁 Plik: {file_path}")
