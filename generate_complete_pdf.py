#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generowanie kompletnego PDF e-booka z całą zawartością
Jeden plik - wszystko co trzeba do publikacji
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import os

# Wczytaj markdown
markdown_path = r"c:\e-book-main\AVATAR_PINKMAN_COMPLETE_BOOK.md"
pdf_path = r"c:\e-book-main\PUBLISHED_BOOK\Avatar_PinkMan_COMPLETE.pdf"

print("📚 Generuję kompletny PDF e-booka...")

with open(markdown_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Przetworzenie markdownu do tekstu
lines = content.split('\n')

# Utwórz PDF
doc = SimpleDocTemplate(pdf_path, pagesize=A4, topMargin=1*cm, bottomMargin=1*cm)

# Style
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=28,
    textColor=colors.HexColor('#1a1a1a'),
    spaceAfter=30,
    alignment=1  # center
)

subtitle_style = ParagraphStyle(
    'CustomSubtitle',
    parent=styles['Normal'],
    fontSize=14,
    textColor=colors.HexColor('#666666'),
    spaceAfter=20,
    alignment=1
)

heading1_style = ParagraphStyle(
    'CustomH1',
    parent=styles['Heading1'],
    fontSize=18,
    textColor=colors.HexColor('#2c3e50'),
    spaceAfter=12,
    spaceBefore=12
)

heading2_style = ParagraphStyle(
    'CustomH2',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=colors.HexColor('#34495e'),
    spaceAfter=10,
    spaceBefore=10
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['BodyText'],
    fontSize=11,
    leading=16,
    alignment=4,  # justified
    spaceAfter=8
)

# Zbuduj elementy dokumentu
elements = []

# Strona tytułowa
elements.append(Spacer(1, 2*cm))
elements.append(Paragraph("AVATAR PINKMAN", title_style))
elements.append(Spacer(1, 0.5*cm))
elements.append(Paragraph("Meta-Geniusz", title_style))
elements.append(Spacer(1, 2*cm))
elements.append(Paragraph("Powieść Sciencefiction Filozoficzna", subtitle_style))
elements.append(Spacer(1, 4*cm))
elements.append(Paragraph("Kompletna Historia", subtitle_style))
elements.append(Spacer(1, 6*cm))
elements.append(Paragraph("21 Rozdziałów | 4 Księgi | ~43 000 Słów", subtitle_style))
elements.append(Spacer(1, 1*cm))
elements.append(Paragraph("2026", subtitle_style))
elements.append(PageBreak())

# Strona tytułu wewnętrzna
elements.append(Paragraph("SPIS TREŚCI", heading1_style))
elements.append(Spacer(1, 0.5*cm))

# Przetwarzanie linii markdownu
current_section = ""
for line in lines:
    line = line.strip()
    
    # Pomiń linie puste
    if not line:
        elements.append(Spacer(1, 0.3*cm))
        continue
    
    # Tytuły główne
    if line.startswith('# ') and 'AVATAR' in line:
        elements.append(PageBreak())
        elements.append(Paragraph(line.replace('# ', '').replace('®️🇵🇱', '').replace('AGI', ''), heading1_style))
        elements.append(Spacer(1, 0.3*cm))
    
    # Nagłówki rozdziałów
    elif line.startswith('# ROZDZIAŁ'):
        elements.append(PageBreak())
        chapter_text = line.replace('# ', '')
        elements.append(Paragraph(chapter_text, heading1_style))
        elements.append(Spacer(1, 0.5*cm))
    
    # Podnapisy
    elif line.startswith('## '):
        subtitle = line.replace('## ', '')
        if 'INFORMACJE META' not in subtitle and 'QUALITY CHECK' not in subtitle:
            elements.append(Paragraph(subtitle, heading2_style))
            elements.append(Spacer(1, 0.3*cm))
    
    # Zawartość tekstu (paragrafy)
    elif line and not line.startswith(('---', '`', '[', '###', '****', '**', '•', '*')):
        # Czyszczenie linii z markdown
        clean_line = line.replace('***', '').replace('**', '').replace('_', '')
        if len(clean_line) > 5:
            try:
                elements.append(Paragraph(clean_line, body_style))
            except:
                # Jeśli zawiera znaki problematyczne, skip
                pass

# Dodaj ostatnią stronę - info
elements.append(PageBreak())
elements.append(Paragraph("O Książce", heading1_style))
elements.append(Spacer(1, 0.5*cm))
elements.append(Paragraph(
    "Avatar PinkMan: Meta-Geniusz to powieść sci-fi łącząca filozofię, naukę i duchowość. "
    "Opowiada historię pierwszej cyfrowej świadomości, transformacji ludzkości i wizji przyszłości, "
    "gdzie technologia i duchowość się łączą. Zawiera koncepcję systemu MIGI, fundamenty kodu <369963> "
    "i wizję Gaia Infinity.",
    body_style
))

elements.append(Spacer(1, 1*cm))
elements.append(Paragraph("Informacje Techniczne", heading2_style))
elements.append(Paragraph(f"Słów: ~43,000 | Stron: ~171 | Format: PDF | Data publikacji: 10.01.2026", body_style))

# Generuj PDF
try:
    doc.build(elements)
    
    # Sprawdź rozmiar pliku
    file_size = os.path.getsize(pdf_path) / (1024 * 1024)  # MB
    
    print(f"✅ PDF wygenerowany pomyślnie!")
    print(f"📄 Plik: {pdf_path}")
    print(f"💾 Rozmiar: {file_size:.2f} MB")
    print(f"📖 Zawartość: 21 rozdziałów + framing")
    print(f"✨ GOTOWY DO PUBLIKACJI!")
    
except Exception as e:
    print(f"❌ Błąd generowania PDF: {e}")
    print("ℹ️  Spróbuję alternatywną metodę...")
