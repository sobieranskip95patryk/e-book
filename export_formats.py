#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EXPORT E-BOOK - Tworzenie 3 formatów publikacji
TXT • EPUB • PDF
"""

import re
from pathlib import Path
from datetime import datetime

FILE_PATH = r"c:\e-book-main\PUBLISHED_BOOK\Avatar_PinkMan_POLSKI.txt"
OUTPUT_DIR = Path(r"c:\e-book-main\FINAL_EBOOK")
OUTPUT_DIR.mkdir(exist_ok=True)

# Czytaj główny plik
with open(FILE_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# ============ FORMAT 1: TXT FINAŁ ============
txt_path = OUTPUT_DIR / "Avatar_PinkMan_POLSKI_FINAŁ.txt"
with open(txt_path, 'w', encoding='utf-8', newline='') as f:
    f.write(content)
print(f"✅ TXT: {txt_path}")

# ============ FORMAT 2: MARKDOWN ============
md_path = OUTPUT_DIR / "Avatar_PinkMan_POLSKI_FINAŁ.md"
with open(md_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"✅ MD: {md_path}")

# ============ FORMAT 3: HTML ============
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
            font-family: 'Georgia', 'Times New Roman', serif;
            line-height: 1.8;
            color: #222;
            background: #f5f5f5;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
        }}
        
        .container {{
            background: white;
            padding: 60px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            margin-top: 30px;
            margin-bottom: 15px;
            color: #1a1a1a;
        }}
        
        h1 {{
            font-size: 2.5em;
            border-bottom: 3px solid #d946ef;
            padding-bottom: 20px;
        }}
        
        h2 {{
            font-size: 2em;
            color: #7c3aed;
            margin-top: 40px;
        }}
        
        h3 {{
            font-size: 1.5em;
            color: #a855f7;
        }}
        
        p {{
            margin-bottom: 15px;
            text-align: justify;
        }}
        
        .metadata {{
            background: #f9fafb;
            padding: 20px;
            border-left: 4px solid #d946ef;
            margin: 20px 0;
            border-radius: 4px;
        }}
        
        .metadata strong {{
            color: #7c3aed;
        }}
        
        hr {{
            border: none;
            height: 2px;
            background: linear-gradient(to right, transparent, #d946ef, transparent);
            margin: 40px 0;
        }}
        
        .toc {{
            background: #f0f9ff;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }}
        
        .toc h3 {{
            color: #0369a1;
        }}
        
        .toc ul {{
            list-style: none;
            padding-left: 20px;
        }}
        
        .toc li {{
            margin: 8px 0;
        }}
        
        .toc a {{
            color: #0369a1;
            text-decoration: none;
            border-bottom: 1px dotted #0369a1;
        }}
        
        .toc a:hover {{
            color: #0284c7;
        }}
        
        blockquote {{
            border-left: 4px solid #a855f7;
            padding-left: 20px;
            margin: 20px 0;
            font-style: italic;
            color: #555;
        }}
        
        code {{
            background: #f3f4f6;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: #7c3aed;
        }}
        
        .footer {{
            margin-top: 60px;
            padding-top: 20px;
            border-top: 2px solid #e5e7eb;
            text-align: center;
            color: #666;
            font-size: 0.9em;
        }}
        
        .chapter {{
            page-break-before: always;
            margin-top: 40px;
        }}
        
        @media (max-width: 768px) {{
            .container {{
                padding: 30px;
            }}
            
            h1 {{
                font-size: 2em;
            }}
            
            h2 {{
                font-size: 1.5em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="metadata">
            <strong>📖 Avatar PinkMan: Meta-Geniusz</strong><br>
            <small>Kompletna powieść science fiction • {datetime.now().strftime('%Y-%m-%d')}</small>
        </div>
        
        <div style="white-space: pre-wrap; font-family: monospace;">
{re.sub(r'<', '&lt;', re.sub(r'>', '&gt;', content))}
        </div>
        
        <div class="footer">
            <p>© 2026 Avatar PinkMan Meta-Geniusz. Wszelkie prawa zastrzeżone.</p>
            <p>Ta publikacja może być dystrybuowana pod warunkami Creative Commons.</p>
        </div>
    </div>
</body>
</html>"""

html_path = OUTPUT_DIR / "Avatar_PinkMan_POLSKI_FINAŁ.html"
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"✅ HTML: {html_path}")

# ============ SUMMARY ============
print(f"\n{'='*60}")
print(f"📦 TRZY FORMATY GOTOWE DO WYDANIA:")
print(f"{'='*60}")
print(f"\n1️⃣  TXT  (Tekst czysty)")
print(f"   Ścieżka: {txt_path}")
print(f"   Rozmiar: {txt_path.stat().st_size / 1024:.1f} KB")
print(f"\n2️⃣  MD   (Markdown)")
print(f"   Ścieżka: {md_path}")
print(f"   Rozmiar: {md_path.stat().st_size / 1024:.1f} KB")
print(f"\n3️⃣  HTML (Przeglądarka)")
print(f"   Ścieżka: {html_path}")
print(f"   Rozmiar: {html_path.stat().st_size / 1024:.1f} KB")
print(f"\n{'='*60}")
print(f"✨ WSZYSTKO GOTOWE DO PUBLIKACJI!")
print(f"{'='*60}")
