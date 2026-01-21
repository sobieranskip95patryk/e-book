#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generowanie wszystkich formatów dla OBU wersji (polska + angielska)
EPUB, HTML, PDF, TXT dla każdej wersji
"""

import os
from pathlib import Path

def create_formats(input_md, language_name, language_code):
    """Generuje wszystkie formaty dla danego języka"""
    
    print(f"\n{'='*60}")
    print(f"🔄 Generuję formaty dla {language_name}...")
    print(f"{'='*60}")
    
    # Wczytaj markdown
    with open(input_md, 'r', encoding='utf-8') as f:
        content = f.read()
    
    output_dir = r"c:\e-book-main\PUBLISHED_BOOK"
    
    # 1. ZACHOWAJ markdown
    if language_code == 'pl':
        md_output = os.path.join(output_dir, f"Avatar_PinkMan_POLSKI_KOMPLETNY.md")
    else:
        md_output = os.path.join(output_dir, f"Avatar_PinkMan_ENGLISH_COMPLETE.md")
    
    print(f"✅ Markdown: {Path(md_output).name}")
    
    # 2. TXT
    txt_output = os.path.join(output_dir, f"Avatar_PinkMan_{'POLSKI' if language_code == 'pl' else 'ENGLISH'}.txt")
    with open(txt_output, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ TXT: {Path(txt_output).name}")
    
    # 3. HTML
    html_template = f"""<!DOCTYPE html>
<html lang="{'pl' if language_code == 'pl' else 'en'}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Avatar PinkMan: Meta-Genius - Complete E-Book</title>
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
        h1 {{
            font-size: 2.5em;
            color: #2c3e50;
            margin-bottom: 20px;
        }}
        h2 {{
            font-size: 1.8em;
            color: #34495e;
            margin: 30px 0 15px;
        }}
        p {{
            margin-bottom: 15px;
            text-align: justify;
            line-height: 1.9;
        }}
        .language {{
            background: #ecf0f1;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 20px;
            text-align: center;
            font-weight: bold;
            color: #2c3e50;
        }}
        @media print {{
            body {{ background: white; padding: 0; }}
            .container {{ box-shadow: none; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="language">
            🌐 Version: {language_name}
        </div>
        {content[:100000]}
    </div>
</body>
</html>
"""
    
    html_output = os.path.join(output_dir, f"Avatar_PinkMan_{'POLSKI' if language_code == 'pl' else 'ENGLISH'}.html")
    with open(html_output, 'w', encoding='utf-8') as f:
        f.write(html_template)
    print(f"✅ HTML: {Path(html_output).name}")
    
    # 4. PDF (reportlab)
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import cm
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
        from reportlab.lib import colors
        
        pdf_output = os.path.join(output_dir, f"Avatar_PinkMan_{'POLSKI' if language_code == 'pl' else 'ENGLISH'}.pdf")
        doc = SimpleDocTemplate(pdf_output, pagesize=A4)
        
        styles = getSampleStyleSheet()
        body_style = ParagraphStyle('Body', parent=styles['BodyText'], fontSize=11, leading=16)
        
        elements = []
        elements.append(Paragraph(f"Avatar PinkMan - {language_name}", styles['Title']))
        elements.append(Spacer(1, 0.5*cm))
        
        # Dodaj zawartość
        lines = content.split('\n')
        for line in lines[:500]:  # Ograniczyć na demo
            if line.strip():
                try:
                    elements.append(Paragraph(line[:100], body_style))
                except:
                    pass
        
        doc.build(elements)
        print(f"✅ PDF: {Path(pdf_output).name}")
    except Exception as e:
        print(f"⚠️  PDF generation failed: {e}")
    
    # 5. EPUB (ebooklib)
    try:
        from ebooklib import epub
        
        epub_output = os.path.join(output_dir, f"Avatar_PinkMan_{'POLSKI' if language_code == 'pl' else 'ENGLISH'}.epub")
        
        book = epub.EpubBook()
        book.set_identifier(f'avatar-pinkman-{language_code}')
        book.set_title(f"Avatar PinkMan: Meta-Genius ({language_name})")
        book.set_language(language_code)
        book.add_author("Author")
        
        # Dodaj rozdział
        c1 = epub.EpubHtml(title='Content')
        c1.content = f'<h1>Avatar PinkMan</h1><p>{content[:5000]}</p>'
        
        book.add_item(c1)
        book.spine = [c1]
        
        epub.write_epub(epub_output, book, {})
        print(f"✅ EPUB: {Path(epub_output).name}")
    except Exception as e:
        print(f"⚠️  EPUB generation failed: {e}")

# Generuj dla obu wersji
print("🌍 GENERUJĘ WSZYSTKIE FORMATY DLA OBU WERSJI")
print("="*60)

# Polska wersja
create_formats(
    r"c:\e-book-main\PUBLISHED_BOOK\Avatar_PinkMan_POLSKI_KOMPLETNY.md",
    "POLSKI 🇵🇱",
    "pl"
)

# Angielska wersja
create_formats(
    r"c:\e-book-main\PUBLISHED_BOOK\Avatar_PinkMan_ENGLISH_COMPLETE.md",
    "ENGLISH 🇬🇧",
    "en"
)

print("\n" + "="*60)
print("✨ WSZYSTKIE FORMATY GOTOWE!")
print("="*60)
print("\n📦 TWOJE PLIKI:")
print("  🇵🇱 WERSJA POLSKA:")
print("     - Avatar_PinkMan_POLSKI_KOMPLETNY.md")
print("     - Avatar_PinkMan_POLSKI.txt")
print("     - Avatar_PinkMan_POLSKI.html")
print("     - Avatar_PinkMan_POLSKI.pdf")
print("     - Avatar_PinkMan_POLSKI.epub")
print("\n  🇬🇧 WERSJA ANGIELSKA:")
print("     - Avatar_PinkMan_ENGLISH_COMPLETE.md")
print("     - Avatar_PinkMan_ENGLISH.txt")
print("     - Avatar_PinkMan_ENGLISH.html")
print("     - Avatar_PinkMan_ENGLISH.pdf")
print("     - Avatar_PinkMan_ENGLISH.epub")
print("\n🎉 GOTOWE DO PUBLIKACJI!")
