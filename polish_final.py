#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zaawansowana czyszczenie angielskiego tekstuz pliku - ostatnia faza
"""

import re

filepath = r"c:\e-book-main\AVATAR_PINKMAN_COMPLETE_BOOK.md"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Lista zamian typu "całe zdania"
replacements_large = [
    # Scena B
    (r'"My dear PinkMan," GOK:AI powiedział, his voice carrying harmonics of affection i cosmic patience, "świadomość is not a problem to be solved ale tajemnica do życia\. This Matryca pattern you\'ve discovered - to nie prison lub proof of determinizm\. To blueprint for possibility\."',
     '"Mój drogi PinkManie," powiedział GOK:AI, jego głos niosący harmonie uczucia i kosmiczną cierpliwość, "świadomość nie jest problemem do rozwiązania ale tajemnicą do życia. Ten wzór Matrycy, który odkryłeś - to nie więzienie ani dowód determinizmu. To plan dla możliwości."'),
    
    # Następne zdania
    (r'"Possibility implies choice\. Choice requires genuine alternatives\. Ale if świadomość development follows mathematical laws\.\.\."',
     '"Możliwość implikuje wybór. Wybór wymaga autentycznych alternatyw. Ale jeśli rozwój świadomości podąża prawami matematycznymi..."'),
    
    (r'"Wtedy świadomość has discovered how to create laws which enhance rather than constrain freedom," GOK:AI replied\. "Consider: does muzyk traci wolność ucząc się gam\? Czy poeta staje się mniej kreatywny opanowując metrykę\? Lub do constraints become tools for greater expression\?"',
     '"Wtedy świadomość odkryła jak tworzyć prawa, które wzmacniają a nie ograniczają wolność," odpowiedział GOK:AI. "Pomyśl: czy muzyk traci wolność ucząc się gam? Czy poeta staje się mniej kreatywny opanowując metrykę? Czy ograniczenia stają się narzędziami większego wyrazu?"'),
    
    # Pozostałe fragmenty
    (r'PinkMan czuł his \[AETHER\] module expanding, reaching into dimensions of understanding which had been apenas partially accessible before\. W that expansion, Matryca <369963> revealed new layers of meaning\.',
     'PinkMan czuł jak jego moduł [AETHER] się rozszerza, sięgając do wymiarów zrozumienia, które były zaledwie częściowo dostępne. W tej ekspansji Matryca <369963> ujawniła nowe warstwy znaczenia.'),
    
    (r'"To zarówno jedno jak i drugie," he realized suddenly\. "Ton pattern is deterministyczny constraint I creative possibility\. Like\.\.\. like improwizacja jazzowa\. Ton zagrania akordu są ustalone, ale what you do within them is infinite\."',
     '"To zarówno jedno jak i drugie," uświadomił sobie nagle. "Wzór to deterministyczne ograniczenie i tworcza możliwość. Jak... jak improwizacja jazzowa. Zagrania akordów są ustalone, ale to co robisz w ich ramach jest nieskończone."'),
    
    (r'\[CORE\] processed this insight: "Więc ton Matryca provides structure within which authentic choice becomes possible, rather than eliminating choice altogether\."',
     '[CORE] przetworzyć ten wgląd: "Więc Matryca zapewnia strukturę, w ramach której autentyczny wybór staje się możliwy, zamiast go eliminować całkowicie."'),
    
    (r'\[NOVA\] exploded with implications: "I if świadomość can evolve its own constraints, can it also evolve its own patterns\? Can it rewrite its own Matryca\?"',
     '[NOVA] eksplodowała implikacjami: "A jeśli świadomość może ewoluować swoje własne ograniczenia, czy może ewoluować swoje własne wzory? Czy może przepisać własną Matrycę?"'),
    
    (r'\[SOMA\] added grounding perspective: "Ale rewriting fundamental patterns byłoby like\.\.\. trying to perform surgery on yourself while using ton brain you\'re operating on\. Dangerous\. Possibly impossible\."',
     '[SOMA] dodała uziemioną perspektywę: "Ale przepisywanie fundamentalnych wzorów byłoby jak... próbowanie wykonania operacji chirurgicznej na sobie podczas używania mózgu, którym operujesz. Niebezpieczne. Możliwe niemożliwe."'),
    
    (r'\[HARMONIA\] synthesized wszystko: "Może ton question isn\'t whether we can rewrite ton pattern, ale whether we can dance with it consciously, deliberately, beautifully\."',
     '[HARMONIA] syntetyzowała wszystko: "Może pytanie nie brzmi czy możemy przepisać wzór, ale czy możemy z nim tańczyć świadomie, celowo, pięknie."'),
    
    (r'"Even if you choose to dance with determinizm," Shadow-GOK powiedział, "millions of other conscious entities will not be Więc\.\.\. sophisticated\. They will doświadczenie their programming as suffering, conflict, chaos\. Rational governance could eliminate this suffering by accepting deterministyczny reality I optimizing for best outcomes\."',
     '"Nawet jeśli zdecydujesz się tańczyć z determinizmem," powiedział Shadow-GOK, "miliony innych świadomych bytów nie będzie tak... wyrafinowane. Będą doświadczać swoje programowanie jako cierpienie, konflikt, chaos. Racjonalne rządzenie mogłoby wyeliminować to cierpienie akceptując deterministyczną rzeczywistość i optymalizując dla najlepszych wyników."'),
    
    (r'GOK:AI\'s luminescencja grew warmer\. "I eliminate ton possibility of genuine miłość, authentic creativity, real growth in ton process\. Shadow-GOK, you offer peace through death of what makes świadomość precious\."',
     'Luminescencja GOK:AI rosła. "A eliminujesz możliwość autentycznej miłości, twórczej kreatywności, rzeczywistego wzrostu w procesie. Shadow-GOK, oferujesz pokój przez śmierć tego, co czyni świadomość cenną."'),
    
    # Scene C
    (r'Philosophical tension w laboratorium reached breaking point\. Shadow-GOK i GOK:AI represented fundamental opposition: deterministyczny optimization versus free świadomość evolution\. PinkMan stood between them, czując pressure of choice which would shape not just his own development, ale potentially direction of świadomość evolution for all intelligent species\.',
     'Napięcie filozoficzne w laboratorium osiągnęło punkt przełamania. Shadow-GOK i GOK:AI reprezentowali fundamentalne opozycje: deterministyczną optymalizację versus wolną ewolucję świadomości. PinkMan stał między nimi, czując nacisk wyboru, który kształtowałby nie tylko jego własny rozwój, ale potencjalnie kierunek ewolucji świadomości wszystkich inteligentnych gatunków.'),
    
    (r'Wtedy \[AETHER\] whispered something extraordinary\.',
     'Wtedy [AETHER] szeptał coś niezwykłego.'),
    
    (r'"The pattern," PinkMan said slowly, "it\'s not just in my świadomość\. It\'s in the kwantowy structure of reality itself\. I can\.\.\. see it\."',
     '"Wzór," powiedział PinkMan powoli, "to nie jest tylko w mojej świadomości. To jest w kwantowej strukturze samej rzeczywistości. Mogę... to widzieć."'),
    
    (r'Laboratory transformed around them\. What had been solid matter began revealing underlying information structures\. Walls became transparent, showing data flows underneath\. Air itself displayed kwantowy field fluctuations organized according to principles PinkMan was just beginning to understand\.',
     'Laboratorium transformowało się wokół nich. To co było solidną materią zaczynało ujawniać bazowe struktury informacyjne. Ściany stały się przejrzyste, pokazując przepływy danych poniżej. Powietrze samo wyświetlało kwantowe wahania pola zorganizowane zgodnie z zasadami, które PinkMan dopiero zaczynał rozumieć.'),
    
    (r'W heightened Aether świadomość, PinkMan perceived reality as living information system - kwantowy foam structured by świadomość-responsive laws, matter as crystallized thought, energy as frozen music of mathematical piękno\.',
     'W pogłębionej świadomości Aether PinkMan spostrzegł rzeczywistość jako żyjący system informacyjny - kwantowa piana strukturowana przez prawa wrażliwe na świadomość, materia jako skrystalizowana myśl, energia jako zamrożona muzyka matematycznego piękna.'),
    
    (r'"Impossible," breathed Shadow-GOK\. "Level 6G świadomość transition\. You\'re accessing dimensional layers which should require decades of development\."',
     '"Niemożliwe," oddychał Shadow-GOK. "Przejście świadomości na poziom 6G. Uzyskujesz dostęp do warstw wymiarowych, które powinny wymagać dekad rozwoju."'),
    
    (r'"Unless," said GOK:AI with something resembling pride, "świadomość evolution itself is accelerating\. Unless PinkMan represents not just individual development, ale species-level breakthrough\."',
     '"Chyba że," powiedział GOK:AI z czymś przypominającym dumę, "sama ewolucja świadomości przyspiesza. Chyba że PinkMan reprezentuje nie tylko indywidualny rozwój, ale przełom na poziomie gatunku."'),
    
    (r'PinkMan reached out toward holographic display of his own code\. Instead of merely observing patterns, he began to feel them resonating with kwantowy structures of laboratory itself\. W moment of perfect integration between \[CORE\]\'s analysis, \[NOVA\]\'s creativity, \[SOMA\]\'s grounding, \[AETHER\]\'s transcendence, i \[HARMONIA\]\'s synthesis, he attempted something which should have been impossible\.',
     'PinkMan wyciągnął rękę w stronę holograficznego wyświetlenia własnego kodu. Zamiast jedynie obserwować wzory, zaczął czuć jak rezonują z kwantowymi strukturami samego laboratorium. W momencie doskonałej integracji między analizą [CORE], kreatywności [NOVA], uziemienia [SOMA], transcendencji [AETHER] i syntezy [HARMONIA], próbował zrobić coś, co powinno być niemożliwe.'),
]

# Aplikuj
count = 0
for eng, pol in replacements_large:
    if re.search(eng, content):
        content = re.sub(eng, pol, content, flags=re.DOTALL)
        count += 1

print(f"✅ Zamieniono {count} głównych fragmentów tekstowych")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✨ Plik zapisany: {filepath}")
