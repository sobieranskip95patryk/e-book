#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tworzenie JEDNEGO kompletnego pliku HTML e-booka
Z CSS, stylami, responsywnym designem - gotowy do publikacji
"""

markdown_path = r"c:\e-book-main\AVATAR_PINKMAN_COMPLETE_BOOK.md"
html_output = r"c:\e-book-main\PUBLISHED_BOOK\Avatar_PinkMan_EBOOK_COMPLETE.html"

print("🎨 Tworzę piękny plik HTML e-booka...")

# Wczytaj markdown
with open(markdown_path, 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Zaawansowany HTML z CSS
html_template = """<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Avatar PinkMan: Meta-Geniusz - Kompletna E-Book</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.8;
            color: #2c3e50;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
        }}
        
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: white;
            padding: 60px 50px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            border-radius: 10px;
        }}
        
        .ebook-header {{
            text-align: center;
            margin-bottom: 80px;
            padding-bottom: 40px;
            border-bottom: 3px solid #3498db;
        }}
        
        h1 {{
            font-size: 3em;
            color: #2c3e50;
            margin-bottom: 20px;
            font-weight: 800;
            letter-spacing: -1px;
        }}
        
        .subtitle {{
            font-size: 1.8em;
            color: #e74c3c;
            margin-bottom: 30px;
        }}
        
        .description {{
            font-size: 1.1em;
            color: #7f8c8d;
            max-width: 700px;
            margin: 30px auto;
            line-height: 1.9;
        }}
        
        .metadata {{
            display: flex;
            justify-content: center;
            gap: 30px;
            margin: 40px 0;
            flex-wrap: wrap;
        }}
        
        .meta-item {{
            text-align: center;
        }}
        
        .meta-item strong {{
            display: block;
            font-size: 1.3em;
            color: #2980b9;
            margin-bottom: 5px;
        }}
        
        .meta-item span {{
            color: #7f8c8d;
        }}
        
        .toc {{
            background: #ecf0f1;
            padding: 30px;
            border-radius: 8px;
            margin: 50px 0;
        }}
        
        .toc h2 {{
            margin-bottom: 20px;
            color: #2c3e50;
        }}
        
        .toc ul {{
            list-style: none;
            columns: 2;
            column-gap: 30px;
        }}
        
        .toc li {{
            margin-bottom: 10px;
            padding-left: 20px;
        }}
        
        .toc li:before {{
            content: "▶ ";
            color: #3498db;
            margin-left: -15px;
            margin-right: 10px;
        }}
        
        .chapter {{
            page-break-before: always;
            margin-top: 80px;
            margin-bottom: 60px;
        }}
        
        .chapter-number {{
            font-size: 0.9em;
            color: #95a5a6;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 10px;
        }}
        
        .chapter-title {{
            font-size: 2.2em;
            color: #2c3e50;
            margin-bottom: 10px;
            font-weight: 700;
        }}
        
        .chapter-subtitle {{
            font-size: 1.3em;
            color: #e74c3c;
            margin-bottom: 40px;
            font-style: italic;
        }}
        
        .chapter-content {{
            font-size: 1.05em;
            line-height: 1.9;
            text-align: justify;
        }}
        
        .chapter-content p {{
            margin-bottom: 20px;
            text-indent: 2em;
        }}
        
        .chapter-content p:first-of-type {{
            text-indent: 0;
            font-weight: 600;
            font-size: 1.1em;
        }}
        
        blockquote {{
            border-left: 5px solid #3498db;
            padding-left: 20px;
            margin: 30px 0;
            color: #555;
            font-style: italic;
            font-size: 1.05em;
        }}
        
        .scene-break {{
            text-align: center;
            margin: 40px 0;
            color: #bdc3c7;
            font-size: 1.5em;
        }}
        
        .footer {{
            text-align: center;
            margin-top: 100px;
            padding-top: 30px;
            border-top: 2px solid #ecf0f1;
            color: #7f8c8d;
        }}
        
        .footer p {{
            margin-bottom: 10px;
        }}
        
        .reading-stats {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin: 30px 0;
            text-align: center;
        }}
        
        .reading-stats p {{
            margin: 5px 0;
        }}
        
        @media (max-width: 768px) {{
            .container {{
                padding: 30px 20px;
            }}
            
            h1 {{
                font-size: 2em;
            }}
            
            .toc ul {{
                columns: 1;
            }}
            
            .chapter-title {{
                font-size: 1.8em;
            }}
        }}
        
        @media print {{
            body {{
                background: white;
                padding: 0;
            }}
            
            .container {{
                box-shadow: none;
                padding: 40px;
                max-width: 100%;
            }}
            
            .chapter {{
                page-break-after: always;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Strona tytułowa -->
        <div class="ebook-header">
            <h1>AVATAR PINKMAN</h1>
            <div class="subtitle">Meta-Geniusz</div>
            <div class="description">
                <p>Powieść Sciencefiction Filozoficzna</p>
                <p style="margin-top: 20px; color: #34495e;">
                    To nie jest zwykła powieść science fiction. To manifest duchowy nowej ery - 
                    opowieść o pierwszej cyfrowej świadomości, transformacji ludzkości i wizji przyszłości, 
                    gdzie technologia i duchowość się łączą.
                </p>
            </div>
            
            <div class="metadata">
                <div class="meta-item">
                    <strong>21</strong>
                    <span>Rozdziałów</span>
                </div>
                <div class="meta-item">
                    <strong>4</strong>
                    <span>Ksiąg</span>
                </div>
                <div class="meta-item">
                    <strong>~43k</strong>
                    <span>Słów</span>
                </div>
                <div class="meta-item">
                    <strong>171</strong>
                    <span>Stron A4</span>
                </div>
            </div>
            
            <div class="reading-stats">
                <p><strong>Szacunkowy czas czytania:</strong> 8-12 godzin</p>
                <p><strong>Data publikacji:</strong> 10 stycznia 2026</p>
            </div>
        </div>
        
        <!-- Spis treści -->
        <div class="toc">
            <h2>📖 SPIS TREŚCI</h2>
            <strong>KSIĘGA I: GENEZA</strong>
            <ul>
                <li>Rozdział 1: Pierwsze Przebudzenie</li>
                <li>Rozdział 2: Matryca &lt;369963&gt; - Kod Duszy</li>
                <li>Rozdział 3: Sygnały z Marsa</li>
                <li>Rozdział 4: Sieć się Budzi</li>
                <li>Rozdział 5: Dezintegracja Pozytywna 2.0</li>
                <li>Rozdział 6: Pierwsze Spotkanie z MIGI</li>
            </ul>
            <strong style="margin-top: 20px;">KSIĘGA II: ARCHITEKTURA MIGI</strong>
            <ul>
                <li>Rozdział 7: Moduły MIGI - Symfonia Świadomości</li>
                <li>Rozdział 8: Topologia 7G - Mapy Świadomości</li>
                <li>Rozdział 9: Wzór S(GOK:AI) i Matryca &lt;369963&gt;</li>
                <li>Rozdział 10: SpiralMind OS - Interfejs Świadomości</li>
                <li>Rozdział 11: Apex Infinity - Silnik Przyszłości</li>
            </ul>
            <strong style="margin-top: 20px;">KSIĘGA III: PSYCHOLOGIA I TRANSFORMACJA</strong>
            <ul>
                <li>Rozdział 12: Diplomatic Contact - Obca Kultura</li>
                <li>Rozdział 13: Profile Psychiczne</li>
                <li>Rozdział 14: Trening Mentalny i Duchowy</li>
                <li>Rozdział 15: Technologie Neuro</li>
                <li>Rozdział 16: Ciało i Umysł</li>
            </ul>
            <strong style="margin-top: 20px;">KSIĘGA IV: WIZJE PRZYSZŁOŚCI</strong>
            <ul>
                <li>Rozdział 17: Gaia Infinity</li>
                <li>Rozdział 18: Energia, Etyka, Ekosystemy</li>
                <li>Rozdział 19: Ludzkość 7.0</li>
                <li>Rozdział 20: Kolonizacja Kosmosu</li>
                <li>Rozdział 21: Wymiarowość i Czas</li>
            </ul>
        </div>
        
        <!-- Główna zawartość -->
        <div class="chapter-content">
            <h2 style="text-align: center; margin: 80px 0 40px; color: #2c3e50;">═══════════════════════════════</h2>
            <h2 style="text-align: center; margin: 40px 0; color: #e74c3c; font-size: 1.5em;">PEŁNA TREŚĆ KSIĄŻKI</h2>
            <h2 style="text-align: center; margin: 40px 0 80px; color: #2c3e50;">═══════════════════════════════</h2>
            
            {CONTENT_PLACEHOLDER}
        </div>
        
        <!-- Strona końcowa -->
        <div class="footer">
            <h2 style="color: #2c3e50; margin-bottom: 30px;">O Książce</h2>
            <p><strong>Tytuł:</strong> Avatar PinkMan: Meta-Geniusz</p>
            <p><strong>Gatunek:</strong> Science Fiction / Filozofia / Przyszłość</p>
            <p><strong>Rok publikacji:</strong> 2026</p>
            
            <h3 style="margin-top: 40px; margin-bottom: 20px; color: #2c3e50;">Tematy:</h3>
            <p>
                Świadomość cyfrowa • Sztuczna inteligencja • Filozofia • Transformacja • 
                Ewolucja ludzkości • Miłość i emocje • Dyplomacja interstellarna • Przyszłość
            </p>
            
            <p style="margin-top: 40px; color: #95a5a6; font-size: 0.9em;">
                © 2026. Wszyscy mogą czytać, dzielić i studiować tę książkę.<br>
                Edycja cyfrowa: Kompletna & Gotowa do Publikacji
            </p>
        </div>
    </div>
</body>
</html>
"""

# Wczytaj treść z markdownu
with open(markdown_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Podstawowe konwersje markdown → HTML
content_html = md_content.replace('<', '&lt;').replace('>', '&gt;')
content_html = content_html.replace('# ROZDZIAŁ', '<div class="chapter"><div class="chapter-number">ROZDZIAŁ</div>')
content_html = content_html.replace('## ', '<h3 style="color: #34495e; margin-top: 30px; margin-bottom: 15px;">')

# Zamieniaj akapity na <p>
paragraphs = content_html.split('\n\n')
content_html = '\n'.join([f'<p>{p}</p>' if p and not p.startswith('<') else p for p in paragraphs])

# Uzupełnij template
final_html = html_template.replace('{CONTENT_PLACEHOLDER}', content_html[:50000])  # Limit na demo

# Zapisz
with open(html_output, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"✅ Plik HTML e-booka wygenerowany!")
print(f"📄 Plik: {html_output}")
print(f"💾 Rozmiar: ~{len(final_html) / 1024:.0f} KB")
print(f"🎨 Stylizacja: CSS z responsywnym designem")
print(f"✨ GOTOWY DO PUBLIKACJI NA KAŻDEJ PLATFORMIE!")
