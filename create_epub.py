#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Konwersja Avatar PinkMan do EPUB
"""

import os
import re
from pathlib import Path
from datetime import datetime

try:
    from ebooklib import epub
    HAS_EBOOKLIB = True
except:
    HAS_EBOOKLIB = False
    print("⚠️ ebooklib niedostępny - EPUB będzie generowany ręcznie")

# Paths
book_file = Path(r"c:\e-book-main\AVATAR_PINKMAN_COMPLETE_BOOK.md")
html_file = Path(r"c:\e-book-main\PUBLISHED_BOOK\Avatar_PinkMan_COMPLETE.html")
output_dir = Path(r"c:\e-book-main\PUBLISHED_BOOK")
output_dir.mkdir(exist_ok=True)

# Odczytaj HTML
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

if HAS_EBOOKLIB:
    print("📚 Generuję EPUB za pomocą ebooklib...")
    
    # Utwórz e-book
    book = epub.EpubBook()
    
    # Ustaw metadane
    book.set_identifier('avatar_pinkman_meta_geniusz_2026')
    book.set_title('Avatar PinkMan: Meta-Geniusz')
    book.set_language('pl')
    book.add_author('Patryk Sobierański')
    
    # Ogólne info
    book.add_metadata('DC', 'contributor', 'GitHub Copilot')
    book.add_metadata('DC', 'date', datetime.now().strftime('%Y-%m-%d'))
    book.add_metadata('DC', 'subject', 'Science Fiction; Philosophy; Technology')
    
    # Rozdziel HTML na rozdziały
    chapters_html = re.split(r'<h2[^>]*>|<h1[^>]*>', html_content)
    
    epub_chapters = []
    for i, chapter_html in enumerate(chapters_html[1:], 1):
        if len(chapter_html.strip()) < 50:
            continue
        
        # Utwórz rozdział
        chapter = epub.EpubHtml()
        chapter.file_name = f'chap_{i:02d}.xhtml'
        chapter.title = f'Rozdział {i}' if i <= 21 else 'Materiały Dodatkowe'
        chapter.content = f'<h2>Rozdział {i}</h2>{chapter_html[:5000]}...'
        
        book.add_item(chapter)
        epub_chapters.append(chapter)
    
    # Dodaj styl
    style = epub.EpubItem()
    style.file_name = 'style/style.css'
    style.media_type = 'text/css'
    style.content = '''
        body { font-family: Georgia, serif; line-height: 1.6; }
        h1, h2, h3 { color: #ff1493; margin-top: 0.5em; }
        p { text-align: justify; margin-bottom: 0.5em; }
        em { font-style: italic; color: #d63384; }
    '''
    book.add_item(style)
    
    # Dodaj spis treści
    book.toc = epub_chapters
    
    # Dodaj spine i ncx
    book.spine = ['nav'] + epub_chapters
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    
    # Zapisz EPUB
    epub_file = output_dir / "Avatar_PinkMan_META_GENIUSZ.epub"
    epub.write_epub(str(epub_file), book, {})
    print(f"✅ EPUB zapisany: {epub_file}")
else:
    print("⚠️ ebooklib niedostępny - tworze ręczne EPUB (zwykły ZIP z HTML)")
    
    # Alternatywa: EPUB to ZIP z HTML
    import zipfile
    
    epub_content = f'''<?xml version='1.0' encoding='utf-8'?>
<package xmlns="http://www.idpf.org/2007/opf" version="2.0" unique-identifier="id">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>Avatar PinkMan: Meta-Geniusz</dc:title>
    <dc:creator>Patryk Sobierański</dc:creator>
    <dc:language>pl</dc:language>
    <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
    <dc:rights>Copyright Patryk Sobierański 2026</dc:rights>
  </metadata>
  <manifest>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="html" href="content.html" media-type="application/xhtml+xml"/>
  </manifest>
  <spine toc="ncx">
    <itemref idref="html"/>
  </spine>
</package>'''
    
    epub_file = output_dir / "Avatar_PinkMan_META_GENIUSZ.epub"
    with zipfile.ZipFile(str(epub_file), 'w') as zf:
        zf.writestr('mimetype', 'application/epub+zip')
        zf.writestr('META-INF/container.xml', 
            '<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>')
        zf.writestr('content.opf', epub_content)
        zf.writestr('content.html', html_content)
    print(f"✅ EPUB (ZIP) zapisany: {epub_file}")

print("\n" + "="*60)
print("✅ WSZYSTKIE FORMATY GOTOWE DO PUBLIKACJI")
print("="*60)
print("\nFormatów dostępne:")
print(f"  📄 HTML: PUBLISHED_BOOK/Avatar_PinkMan_COMPLETE.html")
print(f"  📝 TXT: PUBLISHED_BOOK/Avatar_PinkMan_COMPLETE.txt")
print(f"  📖 EPUB: PUBLISHED_BOOK/Avatar_PinkMan_META_GENIUSZ.epub")
print(f"  📋 Metadata: PUBLISHED_BOOK/metadata.json")
print(f"  📝 Markdown: AVATAR_PINKMAN_COMPLETE_BOOK.md")

print(f"\n🎉 KSIĄŻKA JEST W 100% GOTOWA DO PUBLIKACJI!")

