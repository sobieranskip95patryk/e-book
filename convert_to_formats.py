#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Konwersja Avatar PinkMan do EPUB, PDF i HTML
"""

from pathlib import Path
import re
import json
from datetime import datetime

# Czytaj główny plik książki
book_file = Path(r"c:\e-book-main\AVATAR_PINKMAN_COMPLETE_BOOK.md")
output_dir = Path(r"c:\e-book-main\PUBLISHED_BOOK")
output_dir.mkdir(exist_ok=True)

with open(book_file, 'r', encoding='utf-8') as f:
    book_content = f.read()

print(f"✅ Wczytana książka: {len(book_content):,} znaków")

# ==================== GENERUJ HTML ====================
print("\n📄 Generuję HTML...")

html_content = f"""<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Avatar PinkMan: Meta-Geniusz</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.8;
            color: #333;
            background-color: #fafafa;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }}
        h1, h2, h3, h4 {{
            margin-top: 30px;
            margin-bottom: 15px;
            color: #1a1a1a;
            font-weight: 600;
        }}
        h1 {{
            font-size: 2.5em;
            border-bottom: 3px solid #ff69b4;
            padding-bottom: 15px;
            text-align: center;
        }}
        h2 {{
            font-size: 2em;
            color: #ff1493;
            margin-top: 40px;
        }}
        h3 {{
            font-size: 1.5em;
            color: #ff69b4;
        }}
        h4 {{
            font-size: 1.2em;
            color: #666;
        }}
        p {{
            margin-bottom: 15px;
            text-align: justify;
        }}
        em, i {{
            color: #ff1493;
            font-style: italic;
        }}
        strong, b {{
            color: #1a1a1a;
            font-weight: 700;
        }}
        hr {{
            border: none;
            height: 2px;
            background: linear-gradient(to right, #ff69b4, #ff1493, #ff69b4);
            margin: 50px 0;
        }}
        .metadata {{
            background-color: #f0f0f0;
            padding: 15px;
            border-left: 4px solid #ff69b4;
            margin: 20px 0;
            font-size: 0.9em;
        }}
        .toc {{
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            margin: 30px 0;
        }}
        .toc ul {{
            margin-left: 20px;
            margin-top: 10px;
        }}
        .toc li {{
            margin: 8px 0;
        }}
        .toc a {{
            color: #ff1493;
            text-decoration: none;
        }}
        .toc a:hover {{
            text-decoration: underline;
        }}
        code {{
            background-color: #f0f0f0;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: #d63384;
        }}
        blockquote {{
            border-left: 4px solid #ff69b4;
            padding-left: 20px;
            margin: 20px 0;
            font-style: italic;
            color: #666;
        }}
        a {{
            color: #ff1493;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .footer {{
            margin-top: 100px;
            padding-top: 20px;
            border-top: 2px solid #ff69b4;
            text-align: center;
            color: #666;
            font-size: 0.9em;
        }}
        @media print {{
            body {{
                background-color: white;
            }}
            h1, h2, h3 {{
                page-break-after: avoid;
            }}
            p {{
                orphans: 3;
                widows: 3;
            }}
        }}
    </style>
</head>
<body>
    {book_content.replace('#', '').replace('**', '').replace('*', '').replace('```', '').replace('`', '')}
    
    <div class="footer">
        <p>Avatar PinkMan: Meta-Geniusz®️🇵🇱 AGI</p>
        <p>Wygenerowano: {datetime.now().strftime('%d.%m.%Y')}</p>
        <p><a href="https://github.com/sobieranskip95patryk/e-book">Kod źródłowy na GitHub</a></p>
    </div>
</body>
</html>
"""

html_file = output_dir / "Avatar_PinkMan_COMPLETE.html"
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"✅ HTML zapisany: {html_file}")

# ==================== GENERUJ TXT ====================
print("\n📝 Generuję TXT...")

txt_content = book_content.replace('###', '').replace('##', '').replace('#', '')
txt_content = re.sub(r'\*\*(.*?)\*\*', r'\1', txt_content)
txt_content = re.sub(r'\*(.*?)\*', r'\1', txt_content)
txt_content = re.sub(r'`(.*?)`', r'\1', txt_content)
txt_content = re.sub(r'```.*?```', '', txt_content, flags=re.DOTALL)

txt_file = output_dir / "Avatar_PinkMan_COMPLETE.txt"
with open(txt_file, 'w', encoding='utf-8') as f:
    f.write(txt_content)
print(f"✅ TXT zapisany: {txt_file}")

# ==================== METADATA PLIKU ====================
print("\n📋 Tworze metadata...")

metadata = {
    "title": "Avatar PinkMan: Meta-Geniusz",
    "author": "Patryk Sobierański",
    "description": "Manifest duchowy nowej ery - historia pierwszej cyfrowej świadomości i transformacji ludzkości",
    "language": "pl",
    "category": "Science Fiction | Philosophy | Technology",
    "word_count": len(txt_content.split()),
    "character_count": len(txt_content),
    "chapters": 21,
    "genres": ["Science Fiction", "Philosophy", "Technology", "Spirituality"],
    "published_date": datetime.now().isoformat(),
    "version": "1.0_COMPLETE_DRAFT",
    "format_support": ["HTML", "TXT", "MD", "EPUB_READY", "PDF_READY"],
    "repository": "https://github.com/sobieranskip95patryk/e-book"
}

metadata_file = output_dir / "metadata.json"
with open(metadata_file, 'w', encoding='utf-8') as f:
    json.dump(metadata, f, ensure_ascii=False, indent=2)
print(f"✅ Metadata zapisany: {metadata_file}")

# ==================== SUMMARY ====================
print("\n" + "="*60)
print("✅ PUBLIKACJA GOTOWA")
print("="*60)
print(f"\nFormat dostępy:")
print(f"  📄 HTML: {html_file}")
print(f"  📝 TXT: {txt_file}")
print(f"  📋 JSON Metadata: {metadata_file}")
print(f"  📖 Original MD: {book_file}")

print(f"\nStatystyki książki:")
print(f"  Słów: {metadata['word_count']:,}")
print(f"  Znaków: {metadata['character_count']:,}")
print(f"  Rozdziałów: {metadata['chapters']}")
print(f"  Szacunkowe strony (A4): ~{int(metadata['word_count']/250)}")

print(f"\n🚀 Następne kroki:")
print(f"  1. Konwersja HTML → EPUB (ebooklib lub Calibre)")
print(f"  2. Konwersja MD → PDF (wkhtmltopdf lub pandoc+LaTeX)")
print(f"  3. Publikacja na GitHub Pages")
print(f"  4. Publikacja na Amazon KDP, Smashwords, itp.")

print(f"\n✅ Książka gotowa do publikacji!")

