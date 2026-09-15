# -*- coding: utf-8 -*-
"""
=============================================================================
GENERATORE DISPENSA UFFICIALE DEL CORSO (DOCX + PDF)
Corso: Laboratorio Python + Analisi Dati (22 Ore)
Docente: Arnaldo Morena - ITIS Campobasso
Genera:
  - dispensa/Dispensa_Studenti_v1.docx
  - dispensa/Dispensa_Studenti_v1.pdf
=============================================================================
"""

import os
import sys
import html

# DOCX Imports
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

# PDF Imports
import reportlab
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, Image, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

# Import data
from dispensa_data import (
    COURSE_TITLE, COURSE_SUBTITLE, COURSE_HOURS, COURSE_INSTRUCTOR,
    COURSE_INSTITUTION, COURSE_YEAR, INTRO_DATA, CHAPTERS_DATA, APPENDICE_DATA
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DISPENSA_DIR = os.path.join(BASE_DIR, "dispensa")
SLIDES_ASSETS = os.path.join(BASE_DIR, "slides", "assets")

DOCX_OUT = os.path.join(DISPENSA_DIR, "Dispensa_Studenti_v1.docx")
PDF_OUT = os.path.join(DISPENSA_DIR, "Dispensa_Studenti_v1.pdf")

# Palette Colori Corporate
C_NAVY_HEX = "#0F2942"
C_BLUE_HEX = "#1E88E5"
C_DARK_HEX = "#1E293B"
C_MUTED_HEX = "#64748B"
C_BG_HEX = "#F8FAFC"
C_CODE_BG_HEX = "#F1F5F9"
C_GREEN_HEX = "#10B981"
C_AMBER_HEX = "#F59E0B"

C_NAVY_RGB = RGBColor(15, 41, 66)
C_BLUE_RGB = RGBColor(30, 136, 229)
C_DARK_RGB = RGBColor(30, 41, 59)
C_MUTED_RGB = RGBColor(100, 116, 139)

# -----------------------------------------------------------------------------
# NUMBERED CANVAS PATTERN FOR REPORTLAB
# -----------------------------------------------------------------------------
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_header_footer(num_pages)
            super().showPage()
        super().save()

    def draw_header_footer(self, page_count):
        if self._pageNumber == 1:
            return  # Skip copertina
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(HexColor(C_MUTED_HEX))
        
        # Header superiore
        self.drawString(45, 800, "LABORATORIO PYTHON + ANALISI DATI • ITIS CAMPOBASSO")
        self.drawRightString(550, 800, "DOCENTE: ARNALDO MORENA")
        self.setStrokeColor(HexColor("#E2E8F0"))
        self.setLineWidth(0.6)
        self.line(45, 794, 550, 794)
        
        # Footer inferiore
        self.line(45, 45, 550, 45)
        self.drawString(45, 32, "Manuale Operativo dello Studente • 22 Ore")
        self.drawRightString(550, 32, f"Pagina {self._pageNumber} di {page_count}")
        self.restoreState()


# -----------------------------------------------------------------------------
# DOCX BUILDER HELPERS
# -----------------------------------------------------------------------------
def docx_set_cell_shading(cell, color_hex):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def docx_set_cell_left_border(cell, color_hex, size="24"):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="{size}" w:space="0" w:color="{color_hex}"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    tcPr.append(borders)

def docx_add_heading_1(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(20)
    h.paragraph_format.space_after = Pt(8)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(18)
    run.font.bold = True
    run.font.color.rgb = C_NAVY_RGB
    return h

def docx_add_heading_2(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(6)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = C_BLUE_RGB
    return h

def docx_add_heading_3(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(10)
    h.paragraph_format.space_after = Pt(4)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = C_DARK_RGB
    return h

def docx_add_p(doc, text, bold_prefix=None, italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_b = p.add_run(bold_prefix + " ")
        r_b.font.name = "Calibri"
        r_b.font.size = Pt(10.5)
        r_b.font.bold = True
        r_b.font.color.rgb = C_DARK_RGB
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.italic = italic
    r.font.color.rgb = C_DARK_RGB
    return p

def docx_add_bullet(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_b = p.add_run(bold_prefix + ": ")
        r_b.font.name = "Calibri"
        r_b.font.size = Pt(10.5)
        r_b.font.bold = True
        r_b.font.color.rgb = C_DARK_RGB
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.color.rgb = C_DARK_RGB
    return p

def docx_add_code_block(doc, title, code_lines):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    docx_set_cell_shading(cell, "F1F5F9")
    docx_set_cell_left_border(cell, "1E88E5", size="24")
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(4)
    r_t = p.add_run(f"💻 {title}")
    r_t.font.name = "Calibri"
    r_t.font.size = Pt(10)
    r_t.font.bold = True
    r_t.font.color.rgb = C_BLUE_RGB
    
    for line in code_lines:
        p_c = cell.add_paragraph()
        p_c.paragraph_format.space_after = Pt(1.5)
        p_c.paragraph_format.line_spacing = 1.0
        r_c = p_c.add_run(line)
        r_c.font.name = "Consolas"
        r_c.font.size = Pt(9)
        r_c.font.color.rgb = RGBColor(15, 23, 42)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def docx_add_callout(doc, text, title="NOTA OPERATIVA", box_type="info"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    
    if box_type == "warning":
        shd_col = "FEF3C7"
        border_col = "F59E0B"
        icon = "⚠️"
        t_col = RGBColor(180, 83, 9)
    elif box_type == "success":
        shd_col = "ECFDF5"
        border_col = "10B981"
        icon = "✅"
        t_col = RGBColor(4, 120, 87)
    elif box_type == "tip":
        shd_col = "F0FDF4"
        border_col = "22C55E"
        icon = "💡"
        t_col = RGBColor(21, 128, 61)
    else:
        shd_col = "EFF6FF"
        border_col = "1E88E5"
        icon = "ℹ️"
        t_col = C_BLUE_RGB
        
    docx_set_cell_shading(cell, shd_col)
    docx_set_cell_left_border(cell, border_col, size="30")
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(3)
    r_t = p.add_run(f"{icon} {title}")
    r_t.font.name = "Calibri"
    r_t.font.size = Pt(10.5)
    r_t.font.bold = True
    r_t.font.color.rgb = t_col
    
    p_b = cell.add_paragraph()
    p_b.paragraph_format.space_after = Pt(2)
    p_b.paragraph_format.line_spacing = 1.15
    r_b = p_b.add_run(text)
    r_b.font.name = "Calibri"
    r_b.font.size = Pt(10)
    r_b.font.color.rgb = C_DARK_RGB
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def docx_add_image_safe(doc, img_name, caption=""):
    img_path = os.path.join(SLIDES_ASSETS, img_name)
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(2)
        p_img.add_run().add_picture(img_path, width=Inches(5.8))
        if caption:
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(8)
            r_c = p_cap.add_run(f"Figura: {caption}")
            r_c.font.name = "Calibri"
            r_c.font.size = Pt(9)
            r_c.font.italic = True
            r_c.font.color.rgb = C_MUTED_RGB

def docx_add_table(doc, headers, rows):
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    
    # Header Row
    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        docx_set_cell_shading(hdr_cells[i], "0F2942")
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for r in p.runs:
            r.font.name = "Calibri"
            r.font.size = Pt(9.5)
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)
            
    # Data Rows
    for r_idx, row in enumerate(rows):
        row_cells = table.rows[r_idx + 1].cells
        bg_col = "FFFFFF" if r_idx % 2 == 0 else "F8FAFC"
        for c_idx, val in enumerate(row):
            row_cells[c_idx].text = str(val)
            docx_set_cell_shading(row_cells[c_idx], bg_col)
            p = row_cells[c_idx].paragraphs[0]
            for r in p.runs:
                r.font.name = "Calibri"
                r.font.size = Pt(9)
                r.font.color.rgb = C_DARK_RGB
    doc.add_paragraph().paragraph_format.space_after = Pt(6)


# -----------------------------------------------------------------------------
# BUILD DOCX FILE
# -----------------------------------------------------------------------------
def generate_docx():
    print(f"[*] Inizio generazione DOCX: {DOCX_OUT}")
    doc = Document()
    
    # Impostazione margini A4
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
    # --- COPERTINA ---
    p_top = doc.add_paragraph()
    p_top.paragraph_format.space_before = Pt(30)
    p_top.paragraph_format.space_after = Pt(10)
    r_inst = p_top.add_run(f"{COURSE_INSTITUTION.upper()} • ANNO ACCADEMICO {COURSE_YEAR}")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(11)
    r_inst.font.bold = True
    r_inst.font.color.rgb = C_MUTED_RGB
    
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_after = Pt(6)
    r_title = p_title.add_run(COURSE_TITLE)
    r_title.font.name = "Calibri"
    r_title.font.size = Pt(28)
    r_title.font.bold = True
    r_title.font.color.rgb = C_NAVY_RGB
    
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(25)
    r_sub = p_sub.add_run(COURSE_SUBTITLE)
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(15)
    r_sub.font.color.rgb = C_BLUE_RGB
    
    docx_add_callout(
        doc,
        f"Manuale ufficiale dello studente per il corso intensivo di {COURSE_HOURS}.\n"
        f"Docente: {COURSE_INSTRUCTOR}\n"
        "Comprende: Teoria, Casi d'Uso Aziendali, Esempi di Codice, Best Practice, Errori Comuni, Domande di Autovalutazione e Specifiche del Project Work.",
        title="METADATI DEL CORSO",
        box_type="info"
    )
    
    doc.add_page_break()
    
    # --- INTRODUZIONE ---
    docx_add_heading_1(doc, INTRO_DATA["title"])
    for sec in INTRO_DATA["sections"]:
        docx_add_heading_2(doc, sec["title"])
        for p_text in sec.get("paragraphs", []):
            docx_add_p(doc, p_text)
        if "bullets" in sec:
            for b_pref, b_text in sec["bullets"]:
                docx_add_bullet(doc, b_text, bold_prefix=b_pref)
        if "image" in sec:
            img_n, img_c = sec["image"]
            docx_add_image_safe(doc, img_n, caption=img_c)
        if "table" in sec:
            docx_add_table(doc, sec["table"]["headers"], sec["table"]["rows"])
        if "code_blocks" in sec:
            for cb in sec["code_blocks"]:
                docx_add_code_block(doc, cb["title"], cb["code"])
        if "callouts" in sec:
            for co in sec["callouts"]:
                docx_add_callout(doc, co["text"], title=co["title"], box_type=co.get("type", "info"))
                
    doc.add_page_break()
    
    # --- CAPITOLI 1-8 ---
    for ch in CHAPTERS_DATA:
        ch_num = ch["number"]
        ch_title = f"Capitolo {ch_num} - {ch['title']}"
        docx_add_heading_1(doc, ch_title)
        
        docx_add_callout(
            doc,
            f"Durata modulo: {ch['duration']} | Laboratorio di riferimento: {ch['lab_ref']}\n"
            f"Sintesi: {ch['subtitle']}",
            title="SCHEDA DEL MODULO DIDATTICO",
            box_type="info"
        )
        
        for sec in ch["sections"]:
            docx_add_heading_2(doc, sec["title"])
            for p_text in sec.get("paragraphs", []):
                docx_add_p(doc, p_text)
            if "bullets" in sec:
                for b_pref, b_text in sec["bullets"]:
                    docx_add_bullet(doc, b_text, bold_prefix=b_pref)
            if "image" in sec:
                img_n, img_c = sec["image"]
                docx_add_image_safe(doc, img_n, caption=img_c)
            if "table" in sec:
                docx_add_table(doc, sec["table"]["headers"], sec["table"]["rows"])
            if "code_blocks" in sec:
                for cb in sec["code_blocks"]:
                    docx_add_code_block(doc, cb["title"], cb["code"])
            if "callouts" in sec:
                for co in sec["callouts"]:
                    docx_add_callout(doc, co["text"], title=co["title"], box_type=co.get("type", "info"))
            if "qa_list" in sec:
                for q_idx, (q_text, a_text) in enumerate(sec["qa_list"], start=1):
                    docx_add_p(doc, f"Domanda {q_idx}: {q_text}", bold_prefix="❓", italic=False)
                    docx_add_p(doc, f"Risposta: {a_text}", bold_prefix="💡", italic=True)
                    
        doc.add_page_break()
        
    # --- APPENDICE ---
    docx_add_heading_1(doc, APPENDICE_DATA["title"])
    for sec in APPENDICE_DATA["sections"]:
        docx_add_heading_2(doc, sec["title"])
        if "table" in sec:
            docx_add_table(doc, sec["table"]["headers"], sec["table"]["rows"])
            
    doc.save(DOCX_OUT)
    print(f"[✓] DOCX generato con successo: {DOCX_OUT} ({os.path.getsize(DOCX_OUT) / 1024:.1f} KB)")


# -----------------------------------------------------------------------------
# REPORTLAB PDF BUILDER
# -----------------------------------------------------------------------------
def generate_pdf():
    print(f"[*] Inizio generazione PDF: {PDF_OUT}")
    
    doc = SimpleDocTemplate(
        PDF_OUT,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=48,
        bottomMargin=48
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    style_cover_inst = ParagraphStyle(
        'CoverInst',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=HexColor(C_MUTED_HEX),
        spaceAfter=15
    )
    style_cover_title = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=HexColor(C_NAVY_HEX),
        spaceAfter=10
    )
    style_cover_sub = ParagraphStyle(
        'CoverSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=13,
        leading=17,
        textColor=HexColor(C_BLUE_HEX),
        spaceAfter=25
    )
    
    style_h1 = ParagraphStyle(
        'DispensaH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=19,
        textColor=HexColor(C_NAVY_HEX),
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )
    style_h2 = ParagraphStyle(
        'DispensaH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=HexColor(C_BLUE_HEX),
        spaceBefore=10,
        spaceAfter=5,
        keepWithNext=True
    )
    style_h3 = ParagraphStyle(
        'DispensaH3',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=HexColor(C_DARK_HEX),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    style_body = ParagraphStyle(
        'DispensaBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=HexColor(C_DARK_HEX),
        spaceAfter=5
    )
    style_bullet = ParagraphStyle(
        'DispensaBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=HexColor(C_DARK_HEX),
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=3
    )
    style_code_title = ParagraphStyle(
        'CodeTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=HexColor(C_BLUE_HEX),
        spaceAfter=3
    )
    style_code_body = ParagraphStyle(
        'CodeBody',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.8,
        leading=9.8,
        textColor=HexColor("#0F172A")
    )
    style_callout_title = ParagraphStyle(
        'CalloutTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=HexColor(C_BLUE_HEX),
        spaceAfter=2
    )
    style_callout_body = ParagraphStyle(
        'CalloutBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.8,
        leading=11.8,
        textColor=HexColor(C_DARK_HEX)
    )
    style_tbl_hdr = ParagraphStyle(
        'TableHdr',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.2,
        leading=10.5,
        textColor=colors.white
    )
    style_tbl_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.0,
        leading=10.2,
        textColor=HexColor(C_DARK_HEX)
    )
    style_caption = ParagraphStyle(
        'CaptionStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=10,
        textColor=HexColor(C_MUTED_HEX),
        alignment=1,
        spaceBefore=3,
        spaceAfter=6
    )
    style_qa_q = ParagraphStyle(
        'QAQuestion',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.2,
        leading=12.5,
        textColor=HexColor(C_NAVY_HEX),
        spaceBefore=4,
        spaceAfter=2,
        keepWithNext=True
    )
    style_qa_a = ParagraphStyle(
        'QAAnswer',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.8,
        leading=12.0,
        textColor=HexColor(C_DARK_HEX),
        leftIndent=12,
        spaceAfter=6
    )

    story = []
    
    def pdf_make_code_block(title, lines):
        code_html = "<br/>".join([html.escape(l).replace(" ", "&nbsp;") for l in lines])
        p_title = Paragraph(f"<b>💻 {html.escape(title)}</b>", style_code_title)
        p_code = Paragraph(code_html, style_code_body)
        
        t = Table([[p_title], [p_code]], colWidths=[515])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), HexColor(C_CODE_BG_HEX)),
            ('BOX', (0,0), (-1,-1), 0.5, HexColor("#CBD5E1")),
            ('LINELEFT', (0,0), (0,-1), 3.0, HexColor(C_BLUE_HEX)),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        return KeepTogether([t, Spacer(1, 4)])

    def pdf_make_callout(text, title="NOTA OPERATIVA", box_type="info"):
        if box_type == "warning":
            bg_col = "#FEF3C7"
            brd_col = C_AMBER_HEX
            t_col = "#B45309"
            icon = "⚠️"
        elif box_type == "success":
            bg_col = "#ECFDF5"
            brd_col = C_GREEN_HEX
            t_col = "#047857"
            icon = "✅"
        elif box_type == "tip":
            bg_col = "#F0FDF4"
            brd_col = "#22C55E"
            t_col = "#15803D"
            icon = "💡"
        else:
            bg_col = "#EFF6FF"
            brd_col = C_BLUE_HEX
            t_col = C_BLUE_HEX
            icon = "ℹ️"
            
        c_style_title = ParagraphStyle('CTitle', parent=style_callout_title, textColor=HexColor(t_col))
        p_title = Paragraph(f"<b>{icon} {html.escape(title)}</b>", c_style_title)
        p_body = Paragraph(html.escape(text).replace("\n", "<br/>"), style_callout_body)
        
        t = Table([[p_title], [p_body]], colWidths=[515])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), HexColor(bg_col)),
            ('LINELEFT', (0,0), (0,-1), 3.5, HexColor(brd_col)),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        return KeepTogether([t, Spacer(1, 4)])

    def pdf_make_table(headers, rows):
        hdr_p = [Paragraph(f"<b>{html.escape(h)}</b>", style_tbl_hdr) for h in headers]
        data = [hdr_p]
        for r in rows:
            data.append([Paragraph(html.escape(str(c)), style_tbl_cell) for c in r])
        
        num_cols = len(headers)
        col_w = 515 / num_cols
        t = Table(data, colWidths=[col_w]*num_cols)
        
        t_styles = [
            ('BACKGROUND', (0,0), (-1,0), HexColor(C_NAVY_HEX)),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 5),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
            ('GRID', (0,0), (-1,-1), 0.4, HexColor("#CBD5E1")),
        ]
        for i in range(1, len(data)):
            bg = HexColor("#FFFFFF") if i % 2 != 0 else HexColor(C_BG_HEX)
            t_styles.append(('BACKGROUND', (0, i), (-1, i), bg))
            
        t.setStyle(TableStyle(t_styles))
        return KeepTogether([t, Spacer(1, 6)])

    # --- COPERTINA ---
    story.append(Spacer(1, 40))
    story.append(Paragraph(f"{COURSE_INSTITUTION.upper()} • ANNO ACCADEMICO {COURSE_YEAR}", style_cover_inst))
    story.append(Paragraph(COURSE_TITLE, style_cover_title))
    story.append(Paragraph(COURSE_SUBTITLE, style_cover_sub))
    story.append(HRFlowable(width="100%", thickness=1.5, color=HexColor(C_BLUE_HEX), spaceBefore=5, spaceAfter=20))
    
    meta_text = (
        f"<b>Corso:</b> {COURSE_TITLE} ({COURSE_HOURS})<br/>"
        f"<b>Docente:</b> {COURSE_INSTRUCTOR}<br/>"
        f"<b>Istituzione:</b> {COURSE_INSTITUTION}<br/>"
        f"<b>Tipologia:</b> Manuale Didattico Operativo & Guida ai Laboratori<br/>"
        f"<b>Prerequisiti:</b> Fondamenti minimi di logica e utilizzo base del PC<br/>"
        f"<b>Struttura:</b> 8 Capitoli Operativi + Project Work Finale + Appendice di Riferimento"
    )
    story.append(pdf_make_callout(meta_text, title="INFORMAZIONI GENERALI SUL CORSO", box_type="info"))
    story.append(Spacer(1, 20))
    story.append(Paragraph(
        "Questa dispensa fornisce il percorso completo ed autosufficiente per consentire a ogni studente "
        "di seguire le lezioni in aula, riprodurre autonomamente tutti i laboratori pratici, comprendere "
        "i costrutti architetturali e completare con successo il Project Work finale.",
        style_body
    ))
    story.append(PageBreak())

    # --- INTRODUZIONE ---
    story.append(Paragraph(INTRO_DATA["title"], style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=HexColor(C_BLUE_HEX), spaceBefore=2, spaceAfter=8))
    
    for sec in INTRO_DATA["sections"]:
        story.append(Paragraph(sec["title"], style_h2))
        for p_text in sec.get("paragraphs", []):
            story.append(Paragraph(p_text, style_body))
        if "bullets" in sec:
            for b_pref, b_text in sec["bullets"]:
                story.append(Paragraph(f"• <b>{b_pref}:</b> {b_text}", style_bullet))
        if "image" in sec:
            img_n, img_c = sec["image"]
            img_p = os.path.join(SLIDES_ASSETS, img_n)
            if os.path.exists(img_p):
                story.append(Spacer(1, 4))
                story.append(Image(img_p, width=470, height=200))
                story.append(Paragraph(f"Figura: {img_c}", style_caption))
                story.append(Spacer(1, 4))
        if "table" in sec:
            story.append(pdf_make_table(sec["table"]["headers"], sec["table"]["rows"]))
        if "code_blocks" in sec:
            for cb in sec["code_blocks"]:
                story.append(pdf_make_code_block(cb["title"], cb["code"]))
        if "callouts" in sec:
            for co in sec["callouts"]:
                story.append(pdf_make_callout(co["text"], title=co["title"], box_type=co.get("type", "info")))
        story.append(Spacer(1, 6))

    story.append(PageBreak())

    # --- CAPITOLI 1-8 ---
    for ch in CHAPTERS_DATA:
        ch_num = ch["number"]
        ch_title = f"Capitolo {ch_num} - {ch['title']}"
        story.append(Paragraph(ch_title, style_h1))
        story.append(HRFlowable(width="100%", thickness=1, color=HexColor(C_BLUE_HEX), spaceBefore=2, spaceAfter=8))
        
        ch_meta = (
            f"<b>Durata del Modulo:</b> {ch['duration']} &nbsp;|&nbsp; <b>Laboratorio:</b> {ch['lab_ref']}<br/>"
            f"<b>Obiettivo Didattico:</b> {ch['subtitle']}"
        )
        story.append(pdf_make_callout(ch_meta, title="SCHEDA MODULO DIDATTICO", box_type="info"))
        story.append(Spacer(1, 6))
        
        for sec in ch["sections"]:
            story.append(Paragraph(sec["title"], style_h2))
            for p_text in sec.get("paragraphs", []):
                story.append(Paragraph(p_text, style_body))
            if "bullets" in sec:
                for b_pref, b_text in sec["bullets"]:
                    story.append(Paragraph(f"• <b>{b_pref}:</b> {b_text}", style_bullet))
            if "image" in sec:
                img_n, img_c = sec["image"]
                img_p = os.path.join(SLIDES_ASSETS, img_n)
                if os.path.exists(img_p):
                    story.append(Spacer(1, 4))
                    story.append(Image(img_p, width=470, height=200))
                    story.append(Paragraph(f"Figura: {img_c}", style_caption))
                    story.append(Spacer(1, 4))
            if "table" in sec:
                story.append(pdf_make_table(sec["table"]["headers"], sec["table"]["rows"]))
            if "code_blocks" in sec:
                for cb in sec["code_blocks"]:
                    story.append(pdf_make_code_block(cb["title"], cb["code"]))
            if "callouts" in sec:
                for co in sec["callouts"]:
                    story.append(pdf_make_callout(co["text"], title=co["title"], box_type=co.get("type", "info")))
            if "qa_list" in sec:
                for q_idx, (q_text, a_text) in enumerate(sec["qa_list"], start=1):
                    story.append(Paragraph(f"❓ <b>Domanda {q_idx}:</b> {q_text}", style_qa_q))
                    story.append(Paragraph(f"💡 <b>Risposta:</b> {a_text}", style_qa_a))
            story.append(Spacer(1, 4))
            
        story.append(PageBreak())

    # --- APPENDICE ---
    story.append(Paragraph(APPENDICE_DATA["title"], style_h1))
    story.append(HRFlowable(width="100%", thickness=1, color=HexColor(C_BLUE_HEX), spaceBefore=2, spaceAfter=8))
    for sec in APPENDICE_DATA["sections"]:
        story.append(Paragraph(sec["title"], style_h2))
        if "table" in sec:
            story.append(pdf_make_table(sec["table"]["headers"], sec["table"]["rows"]))
        story.append(Spacer(1, 6))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[✓] PDF generato con successo: {PDF_OUT} ({os.path.getsize(PDF_OUT) / 1024:.1f} KB)")


# -----------------------------------------------------------------------------
# MAIN ENTRYPOINT
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("BUILD DISPENSA UFFICIALE: DOCX + PDF")
    print("=" * 70)
    generate_docx()
    generate_pdf()
    print("=" * 70)
    print("BUILD COMPLETATA CON SUCCESSO!")
    print("=" * 70)
