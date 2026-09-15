"""
=============================================================================
GENERATORE PRESENTAZIONE POWERPOINT PROFESSIONALE (75 SLIDE - 16:9 WIDESCREEN)
Corso: Laboratorio Python + Analisi Dati (22 Ore) - Docente: Arnaldo Morena
Genera: slides/Corso_Python_Campobasso_v1.pptx
=============================================================================
"""

import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLIDES_DIR = os.path.join(BASE_DIR, "slides")
ASSETS_DIR = os.path.join(SLIDES_DIR, "assets")
GEN_DIR = os.path.join(BASE_DIR, "dataset", "generated")
PPTX_OUT = os.path.join(SLIDES_DIR, "Corso_Python_Campobasso_v1.pptx")

# Palette Colori Corporate Professionale
C_NAVY = RGBColor(15, 41, 66)        # #0F2942 - Header Primario
C_BLUE = RGBColor(30, 136, 229)      # #1E88E5 - Accento Brand
C_DARK = RGBColor(30, 41, 59)        # #1E293B - Testo Principale
C_MUTED = RGBColor(100, 116, 139)    # #64748B - Sottotitoli e caption
C_BG = RGBColor(248, 250, 252)       # #F8FAFC - Sfondo Slide Chiaro
C_CARD_BG = RGBColor(255, 255, 255)  # Bianco Card
C_CARD_BORDER = RGBColor(226, 232, 240) # Grigio Bordo
C_CODE_BG = RGBColor(241, 245, 249)  # Grigio Chiaro per Codice
C_CODE_TXT = RGBColor(15, 23, 42)    # Codice Scuro
C_GREEN = RGBColor(16, 185, 129)     # Verde Successo
C_AMBER = RGBColor(245, 158, 11)     # Arancio Warning
C_PURPLE = RGBColor(139, 92, 246)    # Viola Statistica

FONT_TITLE = "Trebuchet MS"
FONT_BODY = "Arial"
FONT_CODE = "Consolas"

def init_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    return prs

def add_header(slide, title_text, category_text="LABORATORIO PYTHON + ANALISI DATI", slide_num=None):
    """Aggiunge header corporate coerente su ogni slide."""
    shapes = slide.shapes
    
    # Fascia di sfondo superiore
    top_band = shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
    top_band.fill.solid()
    top_band.fill.fore_color.rgb = C_NAVY
    top_band.line.color.rgb = C_NAVY
    
    # Linea decorativa blu
    accent = shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(1.15), Inches(13.333), Inches(0.06))
    accent.fill.solid()
    accent.fill.fore_color.rgb = C_BLUE
    accent.line.color.rgb = C_BLUE
    
    # Categoria / Modulo
    cat_box = shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(10.0), Inches(0.3))
    tf_cat = cat_box.text_frame
    tf_cat.word_wrap = True
    p_cat = tf_cat.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.name = FONT_TITLE
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = C_BLUE
    
    # Titolo Slide
    title_box = shapes.add_textbox(Inches(0.8), Inches(0.38), Inches(11.0), Inches(0.65))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = title_text
    p_t.font.name = FONT_TITLE
    p_t.font.size = Pt(22)
    p_t.font.bold = True
    p_t.font.color.rgb = RGBColor(255, 255, 255)
    
    # Footer inferiore
    foot_box = shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(10.0), Inches(0.35))
    tf_f = foot_box.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.text = "ITIS Campobasso • Docente: Arnaldo Morena • 22 Ore"
    p_f.font.name = FONT_BODY
    p_f.font.size = Pt(9)
    p_f.font.color.rgb = C_MUTED
    
    if slide_num:
        num_box = shapes.add_textbox(Inches(11.5), Inches(7.05), Inches(1.0), Inches(0.35))
        tf_n = num_box.text_frame
        p_n = tf_n.paragraphs[0]
        p_n.text = f"{slide_num} / 75"
        p_n.alignment = PP_ALIGN.RIGHT
        p_n.font.name = FONT_BODY
        p_n.font.size = Pt(9)
        p_n.font.bold = True
        p_n.font.color.rgb = C_NAVY

def add_notes(slide, explanation, time_mins, teaching_tips, questions):
    """Aggiunge note relatore formattate e dettagliate."""
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = (
        f"⏱️ TEMPO STIMATO: {time_mins} Minuti\n\n"
        f"📘 SPIEGAZIONE PER IL DOCENTE:\n{explanation}\n\n"
        f"💡 SUGGERIMENTI DI CONDUZIONE D'AULA:\n{teaching_tips}\n\n"
        f"❓ DOMANDE CHIAVE DA PORRE AGLI STUDENTI:\n{questions}"
    )

def create_card(slide, left, top, width, height, title, items=None, bg_color=C_CARD_BG, border_color=C_CARD_BORDER, title_color=C_NAVY):
    """Crea una card contenitore con stile pulito per raggruppare concetti."""
    shapes = slide.shapes
    card = shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1.2)
    
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_right = Inches(0.2)
    tf.margin_top = Inches(0.15)
    tf.margin_bottom = Inches(0.15)
    
    p0 = tf.paragraphs[0]
    p0.text = title
    p0.font.name = FONT_TITLE
    p0.font.size = Pt(15)
    p0.font.bold = True
    p0.font.color.rgb = title_color
    p0.space_after = Pt(10)
    
    if items:
        for item in items:
            p = tf.add_paragraph()
            p.text = f"• {item}"
            p.font.name = FONT_BODY
            p.font.size = Pt(12)
            p.font.color.rgb = C_DARK
            p.space_after = Pt(6)
            
    return card

def create_code_block(slide, left, top, width, height, title, code_lines):
    """Crea un blocco codice leggibile e compatto (<= 15 righe)."""
    shapes = slide.shapes
    rect = shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    rect.fill.solid()
    rect.fill.fore_color.rgb = C_CODE_BG
    rect.line.color.rgb = C_BLUE
    rect.line.width = Pt(1.5)
    
    tf = rect.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.2)
    tf.margin_right = Inches(0.2)
    tf.margin_top = Inches(0.12)
    tf.margin_bottom = Inches(0.12)
    
    p0 = tf.paragraphs[0]
    p0.text = f"💻 {title}"
    p0.font.name = FONT_TITLE
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = C_BLUE
    p0.space_after = Pt(8)
    
    for line in code_lines:
        p = tf.add_paragraph()
        p.text = line
        p.font.name = FONT_CODE
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_CODE_TXT
        p.space_after = Pt(2)
        
    return rect

# =============================================================================
# DEFINIZIONE DELLE 75 SLIDE
# =============================================================================

def build_all_slides(prs):
    blank_layout = prs.slide_layouts[6] # Blank slide
    
    # -------------------------------------------------------------------------
    # SLIDE 1: COPERTINA MASTER CORSO
    # -------------------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = C_NAVY
    bg1.line.fill.background()
    
    t_box = s1.shapes.add_textbox(Inches(1.2), Inches(1.6), Inches(11.0), Inches(2.2))
    tf1 = t_box.text_frame
    p1 = tf1.paragraphs[0]
    p1.text = "LABORATORIO PYTHON + ANALISI DATI"
    p1.font.name = FONT_TITLE
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(255, 255, 255)
    
    p1_sub = tf1.add_paragraph()
    p1_sub.text = "Dall'Elaborazione Dati con Pandas alle Dashboard Interattive in Produzione"
    p1_sub.font.name = FONT_BODY
    p1_sub.font.size = Pt(18)
    p1_sub.font.color.rgb = C_BLUE
    p1_sub.space_before = Pt(12)
    
    meta_box = s1.shapes.add_textbox(Inches(1.2), Inches(4.5), Inches(11.0), Inches(1.8))
    tf_m = meta_box.text_frame
    tf_m.paragraphs[0].text = "🏢 ITIS Campobasso • Percorso Intensivo 22 Ore (80% Laboratorio / 20% Teoria)"
    tf_m.paragraphs[0].font.size = Pt(14)
    tf_m.paragraphs[0].font.color.rgb = RGBColor(226, 232, 240)
    
    p_doc = tf_m.add_paragraph()
    p_doc.text = "👨‍🏫 Docente: Arnaldo Morena | Senior Python Developer & Data Architect"
    p_doc.font.size = Pt(14)
    p_doc.font.bold = True
    p_doc.font.color.rgb = RGBColor(255, 255, 255)
    p_doc.space_before = Pt(8)
    
    p_rep = tf_m.add_paragraph()
    p_rep.text = "🔗 Repository Ufficiale: https://github.com/arnymore/python_analisi_dati_campobasso"
    p_rep.font.size = Pt(12)
    p_rep.font.color.rgb = C_BLUE
    p_rep.space_before = Pt(8)
    
    add_notes(s1, 
        explanation="Slide di apertura del corso. Presentare gli obiettivi professionalizzanti, il valore di Python per superare i limiti di Excel e la metodologia pratica al 100%.",
        time_mins=10,
        teaching_tips="Chiedere agli studenti quali strumenti utilizzano attualmente in azienda (Excel, PowerBI, SQL, gestionali) e quali colli di bottiglia riscontrano quotidianamente.",
        questions="Qual è l'elaborazione dati più lunga o ripetitiva che svolgete settimanalmente al lavoro?"
    )

    # -------------------------------------------------------------------------
    # MODULO 1: PYTHON OPERATIVO (SLIDE 2 - 8)
    # -------------------------------------------------------------------------
    # Slide 2: Il Caso Aziendale Unico
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Il Caso Aziendale Unico: Rete Commerciale Italia", "MODULO 1: PYTHON OPERATIVO (2H)", 2)
    create_card(s2, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🏢 Scenario di Business", [
        "Azienda commerciale nazionale con 4 sedi: Roma, Milano, Torino e Napoli.",
        "Catalogo prodotti articolato: Hardware, Software, Servizi IT e Cancelleria.",
        "I gestionali regionali estraggono file Excel non standardizzati e con anomalie.",
        "Obiettivo: Costruire un sistema automatizzato end-to-end per consolidare e analizzare i KPI."
    ])
    img_arch = os.path.join(ASSETS_DIR, "diagramma_architettura_corso.png")
    if os.path.exists(img_arch):
        s2.shapes.add_picture(img_arch, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2))
    add_notes(s2, "Spiegare la continuità del caso di studio su tutto il percorso formativo.", 15, 
              "Far notare che non faremo 'esercizi giocattolo', ma lavoreremo su dati aziendali realistici.", 
              "Quali criticità nascono quando filiali diverse usano convenzioni diverse?")

    # Slide 3: Tipi Primitivi e Conversioni
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Tipi di Dato Primitivi e Casting nei Dati Aziendali", "MODULO 1: PYTHON OPERATIVO (2H)", 3)
    create_card(s3, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📌 Tipizzazione Dinamica e Pulizia", [
        "Stringhe (str): Codici cliente, nomi prodotti, date testuali.",
        "Interi (int) e Float (float): Pezzi venduti, importi monetari e sconti.",
        "Booleani (bool): Flag transazione approvata / pagamento saldato.",
        "Attenzione al 'Dirty Casting': stringhe con virgola '1250,50 €' falliscono con float() se non ripulite preventivamente."
    ])
    code_s3 = [
        "# Esempio di pulizia e cast monetario",
        "prezzo_grezzo = ' 1.850,50 € '",
        "prezzo_clean = prezzo_grezzo.replace('€', '') \\",
        "                            .replace('.', '') \\",
        "                            .replace(',', '.') \\",
        "                            .strip()",
        "prezzo_num = float(prezzo_clean)",
        "print(f'Prezzo numerico: {prezzo_num:.2f}')",
        "# Output: Prezzo numerico: 1850.50"
    ]
    create_code_block(s3, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Scripting: Sanitizzazione Stringhe Prezzo", code_s3)
    add_notes(s3, "Spiegare perché il casting fallisce sui dati reali italiani (virgola decimale vs punto).", 15,
              "Aprire il REPL Python interattivo e mostrare in diretta il ValueError lanciato da float('100,50').",
              "Perché Excel interpreta '100,50' come numero mentre Python lo vede come stringa?")

    # Slide 4: Liste, Tuple e Dizionari
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Strutture Dati Native: Liste, Tuple e Dizionari", "MODULO 1: PYTHON OPERATIVO (2H)", 4)
    create_card(s4, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🗂️ Modellare Record in Memoria", [
        "Liste []: Sequenze ordinate e modificabili (es. carrello ordini).",
        "Tuple (): Record a sola lettura immutabili (es. coordinate geografiche).",
        "Dizionari {}: Mappature chiave-valore per rappresentare righe di tabelle.",
        "Accesso sicuro con .get('chiave', default) per evitare KeyError su campi opzionali."
    ])
    code_s4 = [
        "# Modellazione di una riga transazione",
        "ordine = {",
        "    'id': 'RO-2024001',",
        "    'cliente': 'Tech Solutions Srl',",
        "    'prodotto': 'Server Rack 24U',",
        "    'qta': 2,",
        "    'prezzo': 1850.00,",
        "    'sconto': 10",
        "}",
        "print(ordine.get('note', 'Nessuna nota'))"
    ]
    create_code_block(s4, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Dizionario per Rappresentare Transazioni", code_s4)
    add_notes(s4, "Mostrare la corrispondenza 1:1 tra un record di database/Excel e un dizionario Python.", 15,
              "Far vedere la differenza tra ordine['note'] (errore) e ordine.get('note') (sicuro).",
              "Come modellereste una fattura con più articoli usando solo liste e dizionari?")

    # Slide 5: Controllo di Flusso e Iterazioni
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Logica Condizionale, Cicli ed Iterazioni", "MODULO 1: PYTHON OPERATIVO (2H)", 5)
    create_card(s5, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "⚙️ Logica Commerciale nei Cicli", [
        "Costrutti if / elif / else per applicare scaglioni di sconto e rating cliente.",
        "Ciclo for per iterare su elenchi di vendite ed accumulare totali progressivi.",
        "Funzioni enumerate() per contatori e zip() per accoppiare liste parallele.",
        "List Comprehension: trasformazioni ed estrazioni sintetiche ad alte prestazioni."
    ])
    code_s5 = [
        "ordini = [",
        "    {'prod': 'Server', 'qta': 2, 'prezzo': 1850},",
        "    {'prod': 'Mouse',  'qta': 5, 'prezzo': 25},",
        "    {'prod': 'Laptop', 'qta': 1, 'prezzo': 900}",
        "]",
        "# Filtro compatto con List Comprehension",
        "high_value = [o for o in ordini if o['prezzo'] > 500]",
        "totale = sum(o['qta'] * o['prezzo'] for o in ordini)",
        "print(f'Fatturato Lordo: {totale:.2f} €')"
    ]
    create_code_block(s5, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Elaborazione Multi-Riga con Comprehension", code_s5)
    add_notes(s5, "Evidenziare la potenza della list comprehension rispetto ai cicli for tradizionali.", 15,
              "Mostrare come calcolare somme e filtri in una sola riga leggibile ed espressiva.",
              "Qual è il vantaggio computazionale e di leggibilità di una list comprehension?")

    # Slide 6: Funzioni Commerciali Riutilizzabili
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Modularità: Funzioni per il Calcolo di KPI Commerciali", "MODULO 1: PYTHON OPERATIVO (2H)", 6)
    create_card(s6, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📐 Architettura a Funzioni", [
        "Incapsulamento della logica aziendale: mai duplicare formule contabili.",
        "Parametri posizionali e valori di default (es. aliquota_iva=0.22, sconto_perc=0).",
        "Ritorno strutturato: restituire dizionari con tutti i dettagli riga calcolati.",
        "Docstring di documentazione per rendere il codice auto-esplicativo in team."
    ])
    code_s6 = [
        "def calcola_totale_riga(qta, prezzo, sconto=0, iva=0.22):",
        "    \"\"\"Calcola imponibile, sconto, IVA e totale.\"\"\"",
        "    lordo = qta * prezzo",
        "    val_sconto = lordo * (sconto / 100.0)",
        "    netto = lordo - val_sconto",
        "    imposta = netto * iva",
        "    return {",
        "        'netto': round(netto, 2),",
        "        'iva': round(imposta, 2),",
        "        'totale': round(netto + imposta, 2)",
        "    }"
    ]
    create_code_block(s6, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Funzione di Calcolo Riga Fattura", code_s6)
    add_notes(s6, "Spiegare perché centralizzare le logiche di calcolo evita disallineamenti contabili.", 15,
              "Invitare gli studenti a scrivere funzioni pure senza effetti collaterali (side-effects).",
              "Cosa succede se l'aliquota IVA cambia dal 22% al 24% se la formula è sparpagliata in 20 punti?")

    # Slide 7: Laboratorio 1 (Traccia ed Esecuzione)
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Laboratorio 1: Calcolo KPI e Normalizzazione Anagrafiche", "MODULO 1: PYTHON OPERATIVO (2H)", 7)
    create_card(s7, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🧪 Consegne per gli Studenti", [
        "File di lavoro: laboratori/lab01_python_operativo/lab01_esercizi.py",
        "Task 1: Implementare calcola_totale_riga() con arrotondamenti a 2 decimali.",
        "Task 2: Calcolare i totali netti e IVA su un carrello ordini multi-prodotto.",
        "Task 3: Scrivere normalizza_ragione_sociale() per ripulire nomi con spazi e maiuscole.",
        "Task 4: Raggruppare le vendite per categoria con dizionario accumulatore."
    ], bg_color=RGBColor(240, 249, 255), border_color=C_BLUE)
    code_s7 = [
        "--- OUTPUT ATTESO DALL'ESECUZIONE ---",
        "Risultato riga: {'netto': 3825.0, 'iva': 841.5, ...}",
        "Fatturato Netto Ordine: 7522.50 €",
        "Totale IVA Ordine:      1654.95 €",
        "Clienti normalizzati:",
        " • '  tech solutions srl  ' -> 'Tech Solutions Srl'",
        " • '   logistica  molise   spa ' -> 'Logistica Molise SpA'",
        "Hardware: Qta 11 | Fatturato: 9070.00 €",
        "Software: Qta 13 | Fatturato: 5100.00 €"
    ]
    create_code_block(s7, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Output di Verifica (lab01_esercizi.py)", code_s7)
    add_notes(s7, "Sessione hands-on guidata di 45 minuti. Girare tra i banchi per verificare la corretta impostazione dei TODO.", 45,
              "Verificare che gli studenti abbiano attivato il virtualenv prima di lanciare lo script.",
              "Chi è riuscito a normalizzare correttamente gli acronimi 'Srl' e 'SpA'?")

    # Slide 8: Recap Modulo 1
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Recap Modulo 1: Competenze Acquisite & Prossimi Passi", "MODULO 1: PYTHON OPERATIVO (2H)", 8)
    create_card(s8, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🎯 Competenze Acquisite", [
        "Piena padronanza di liste, dizionari e strutture annidate.",
        "Capacità di scrivere funzioni modulari per il calcolo contabile.",
        "Pulizia e normalizzazione delle stringhe anagrafiche con metodi nativi.",
        "Comprensione dei limiti delle strutture native su grandi volumi di dati."
    ], bg_color=RGBColor(236, 253, 245), border_color=C_GREEN, title_color=C_GREEN)
    create_card(s8, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "🚀 Verso Pandas (Modulo 2)", [
        "I cicli for nativi diventano lenti e verbosi oltre 10.000 righe.",
        "Nel Modulo 2 scopriremo i DataFrame di Pandas per manipolare milioni di righe istantaneamente.",
        "Tutte le operazioni fatte a mano verranno vettorializzate in una sola riga di codice.",
        "Prepararsi ad aprire il dataset Excel ufficiale della filiale di Roma!"
    ], bg_color=RGBColor(254, 243, 199), border_color=C_AMBER, title_color=C_AMBER)
    add_notes(s8, "Punto di raccordo teorico-pratico: tirare le somme prima di passare alla potenza di calcolo di Pandas.", 10,
              "Sottolineare che la logica imparata con i dizionari è la base concettuale dei DataFrame.",
              "Quanto tempo impiegheremmo a pulire a mano 50.000 righe con un ciclo for rispetto a Pandas?")

    # Continuazione automatizzata delle restanti slide fino a 75...
    # Generiamo tutte le slide dei moduli 2, 3, 4, 5, 6, 7 e Project Work
    build_module_2(prs, blank_layout)
    build_module_3(prs, blank_layout)
    build_module_4(prs, blank_layout)
    build_module_5(prs, blank_layout)
    build_module_6(prs, blank_layout)
    build_module_7(prs, blank_layout)
    build_module_pw(prs, blank_layout)

def build_module_2(prs, blank_layout):
    """Modulo 2: Pandas Fondamenti (Slide 9 - 22, 14 slide)"""
    # 9. Intro Pandas
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Dal Foglio Excel al DataFrame Pandas", "MODULO 2: PANDAS FONDAMENTI (4H)", 9)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🐼 Perché Pandas per l'Analisi Dati?", [
        "Excel limita a 1M righe e si blocca sui ricalcoli pesanti.",
        "Pandas offre strutture in memoria bidimensionali (DataFrame) e monodimensionali (Series).",
        "Performance C/NumPy: calcoli vettorializzati 100x più veloci.",
        "Caricamento diretto di Excel con pd.read_excel('dataset/raw/roma.xlsx', sheet_name='Dati_Vendite')."
    ])
    code = [
        "import pandas as pd",
        "# Ingestion file Excel ufficiale filiale Roma",
        "df_roma = pd.read_excel(",
        "    'dataset/raw/roma.xlsx',",
        "    sheet_name='Dati_Vendite'",
        ")",
        "print(type(df_roma))  # <class 'pandas.core.frame.DataFrame'>",
        "print(df_roma.shape)  # (1248 righe, 13 colonne)"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Caricamento Dataset Excel", code)
    add_notes(s, "Introdurre Pandas e confrontarlo operativamente con Excel.", 15, "Far eseguire il primo import a tutti gli studenti.", "Qual è la differenza fondamentale tra una Series e un DataFrame?")

    # 10. Ispezione Metadati
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Ispezione e Diagnostica Strutturale del DataFrame", "MODULO 2: PANDAS FONDAMENTI (4H)", 10)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🔍 Metodi di Ispezione Rapida", [
        "df.info(): Visualizza colonne, conteggio non-nulli e tipi di dato (dtypes).",
        "df.describe(): Calcola statistiche descrittive istantanee (media, std, min, quartili, max).",
        "df.head(n) e df.tail(n): Campiona le prime o ultime n righe.",
        "df.columns e df.dtypes: Ispezione nomi colonne e formati memoria."
    ])
    code = [
        "# Diagnostica rapida di consistenza",
        "df_roma.info()",
        "# Statistiche descrittive su campi numerici",
        "print(df_roma[['Quantita', 'Sconto_Perc']].describe())",
        "# Prime 3 righe",
        "print(df_roma.head(3))"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Ispezione Strutturale e Metadati", code)
    add_notes(s, "Mostrare come identificare immediatamente colonne sporche o con valori nulli tramite info().", 15, "Far notare che Prezzo_Unitario è di tipo 'object' perché contiene simboli di valuta.", "Perché Prezzo_Unitario non è stato caricato come float64?")

    # 11. Selezione Colonne
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Selezione Colonne: Series (1D) vs DataFrame (2D)", "MODULO 2: PANDAS FONDAMENTI (4H)", 11)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📊 Estrazione Viste Dati", [
        "Singola colonna tra parentesi quadre df['Cliente'] ➔ Restituisce una Series monodimensionale.",
        "Lista di colonne tra doppie quadre df[['Cliente', 'Fatturato']] ➔ Restituisce un sotto-DataFrame.",
        "Creazione di viste mirate per focalizzare l'analisi solo sui dati d'interesse.",
        "Assegnazione a nuove variabili senza duplicare memoria non necessaria."
    ])
    code = [
        "# Selezione singola colonna (Series)",
        "serie_clienti = df_roma['Ragione_Sociale']",
        "",
        "# Selezione colonne multiple (DataFrame)",
        "cols = ['ID_Transazione', 'Ragione_Sociale', 'Fatturato_Lordo']",
        "df_focus = df_roma[cols]",
        "print(df_focus.head(2))"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Selezione Singola e Multi-Colonna", code)
    add_notes(s, "Chiarire la distinzione tra singola quadra e doppia quadra.", 15, "Mostrare la differenza di tipo tra Series e DataFrame.", "Cosa restituisce df[['Fatturato_Lordo']] rispetto a df['Fatturato_Lordo']?")

    # 12. Indicizzazione .iloc vs .loc
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Indicizzazione Avanzata: .iloc[] Posizionale vs .loc[] per Etichette", "MODULO 2: PANDAS FONDAMENTI (4H)", 12)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🎯 Accesso Diretto ai Dati", [
        ".iloc[righe, colonne]: Indicizzazione numerica posizionale (zero-based, estremo destro escluso).",
        ".loc[righe, colonne]: Indicizzazione per etichetta / nome colonna (estremo destro incluso).",
        ".loc accetta anche maschere booleane per filtrare righe condizionalmente.",
        "Best practice: evitare l'accesso a catena df['a']['b'] e preferire sempre .loc/.iloc."
    ])
    code = [
        "# .iloc: righe da 10 a 15, prime 4 colonne",
        "sub_pos = df_roma.iloc[10:16, 0:4]",
        "",
        "# .loc: righe con indice 0..5 e colonne specifiche",
        "sub_lbl = df_roma.loc[0:5, ['Ragione_Sociale', 'Fatturato_Lordo']]",
        "print(sub_lbl)"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Slicing con .iloc e .loc", code)
    add_notes(s, "Fissare bene la differenza tra coordinate numeriche (.iloc) e nomi colonna (.loc).", 15, "Dimostrare l'inclusione degli estremi in .loc vs esclusione in .iloc.", "In quale scenario aziendale preferireste .iloc rispetto a .loc?")

    # 13. Filtri Booleani
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Filtri Booleani e Maschere Logiche", "MODULO 2: PANDAS FONDAMENTI (4H)", 13)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🔎 Interrogare il Dataset", [
        "Creazione di una maschera booleana: df['Canale_Vendita'] == 'E-commerce B2B'.",
        "La maschera restituisce una Series di True e False con lo stesso indice.",
        "Passando la maschera a df[...] vengono estratte esclusivamente le righe True.",
        "Metodo .sum() sulla maschera per contare istantaneamente il numero di record rispondenti."
    ])
    code = [
        "# Creazione maschera booleana",
        "mask_ecom = df_roma['Canale_Vendita'] == 'E-commerce B2B'",
        "print(f'Ordini E-commerce: {mask_ecom.sum()}')",
        "",
        "# Applicazione filtro al DataFrame",
        "df_ecom = df_roma[mask_ecom]",
        "print(df_ecom[['ID_Transazione', 'Nome_Prodotto']].head(3))"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Filtro su Singola Condizione", code)
    add_notes(s, "Spiegare il concetto di maschera booleana (vettore di True/False).", 15, "Mostrare come il conteggio dei True corrisponda esattamente al numero di ordini.", "Come contereste quante transazioni hanno importo superiore a 1.000€?")

    # 14. Condizioni Multiple
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Condizioni Logiche Multiple: AND (&), OR (|), NOT (~)", "MODULO 2: PANDAS FONDAMENTI (4H)", 14)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "⚡ Regole di Sintassi Vettoriale", [
        "In Pandas NON si usano le parole chiave 'and', 'or', 'not', ma i simboli bitwise &, |, ~.",
        "IMPORTANTE: Ogni singola condizione DEVE essere racchiusa tra parentesi tonde (cond1) & (cond2).",
        "AND (&): Entrambe le condizioni devono essere vere.",
        "OR (|): Almeno una condizione deve essere vera.",
        "NOT (~): Inverte la condizione (complementare)."
    ])
    code = [
        "# Ordini con Quantita >= 10 E Sconto > 0",
        "cond_qta = (df_roma['Quantita'] >= 10)",
        "cond_sco = (df_roma['Sconto_Perc'] > 0)",
        "df_scontati = df_roma[cond_qta & cond_sco]",
        "",
        "# Ordini Alto Valore NON di Cancelleria",
        "df_target = df_roma[(df_roma['Categoria_Prodotto'] != 'Cancelleria') & \\",
        "                    (df_roma['Fatturato_Lordo'] > 1500)]"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Filtri Booleani Composti", code)
    add_notes(s, "Insistere sull'errore più comune dei principianti: dimenticare le parentesi tonde.", 15, "Spiegare la precedenza degli operatori in Python.", "Perché (df['qta'] > 5) & (df['sconto'] > 0) richiede le parentesi?")

    # 15. Filtri Avanzati isin e str.contains
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Filtri Avanzati: .isin() e Ricerca Testuale con .str.contains()", "MODULO 2: PANDAS FONDAMENTI (4H)", 15)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🔍 Pattern Matching su Dati", [
        ".isin([valori]): Filtra righe il cui valore appartiene a un elenco predefinito.",
        ".str.contains('keyword', case=False, na=False): Ricerca testuale parziale (case-insensitive).",
        "na=False evita errori quando la colonna contiene valori nulli (NaN).",
        "Utilissimo per individuare famiglie di prodotti (es. 'Server', 'Licenza', 'Laptop')."
    ])
    code = [
        "# Filtro su elenco canali autorizzati",
        "canali = ['E-commerce B2B', 'Partner Commerciale']",
        "df_canali = df_roma[df_roma['Canale_Vendita'].isin(canali)]",
        "",
        "# Ricerca per parola chiave 'Server' nel prodotto",
        "df_server = df_roma[df_roma['Nome_Prodotto'].str.contains(",
        "    'Server', case=False, na=False",
        ")]"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Ricerche Testuali e Liste di Valori", code)
    add_notes(s, "Mostrare l'efficacia di .isin() rispetto a concatenazioni infinite di OR (|).", 15, "Far provare la ricerca su nomi prodotto diversi.", "Cosa succede con .str.contains se una cella contiene NaN e non si imposta na=False?")

    # 16. Vettorializzazione
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Vettorializzazione e Colonne Calcolate", "MODULO 2: PANDAS FONDAMENTI (4H)", 16)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "⚡ Calcoli Aritmetici Istantanei", [
        "In Pandas non si itera riga per riga: le operazioni tra colonne sono vettoriali.",
        "df['Lordo'] = df['Quantita'] * df['Prezzo_Unitario'] viene calcolato istantaneamente su tutte le righe.",
        "Creazione di nuove metriche derivate in una sola riga di codice.",
        "Prestazioni ottimali garantite dall'esecuzione in linguaggio C sottostante."
    ])
    code = [
        "# Operazione vettoriale diretta",
        "df_calc = df_roma.copy()",
        "df_calc['Lordo_Calcolato'] = (",
        "    df_calc['Quantita'] * 850.0  # Moltiplicazione scalare/vettoriale",
        ")",
        "print(df_calc[['Quantita', 'Lordo_Calcolato']].head(3))"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Calcolo Vettorializzato", code)
    add_notes(s, "Spiegare perché i cicli for in Pandas sono un anti-pattern da evitare.", 15, "Confrontare i millisecondi di un'operazione vettoriale vs iterrows().", "Perché la vettorializzazione è 100 volte più veloce di un ciclo for?")

    # 17. Cast Numerico Sicuro
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Cast Numerico Sicuro con pd.to_numeric(errors='coerce')", "MODULO 2: PANDAS FONDAMENTI (4H)", 17)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🛡️ Gestione Errori di Conversione", [
        "Quando i dati contengono sporcature o refusi, float() lancia un'eccezione bloccante.",
        "pd.to_numeric(..., errors='coerce') converte i valori validi e trasforma i refusi in NaN senza interrompere l'esecuzione.",
        "Pulizia preventiva con .str.replace('€', '').str.replace(',', '.').",
        "Permette di isolare e diagnosticare rapidamente i record anomali."
    ])
    code = [
        "# Pulizia stringa e conversione sicura",
        "p_clean = (",
        "    df_roma['Prezzo_Unitario']",
        "    .astype(str)",
        "    .str.replace('€', '', regex=False)",
        "    .str.replace(',', '.', regex=False)",
        "    .str.strip()",
        ")",
        "df_roma['Prezzo_Num'] = pd.to_numeric(p_clean, errors='coerce')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Conversione con Coerce a NaN", code)
    add_notes(s, "Spiegare il parametro errors='coerce' come salvavita contro crash improvvisi di pipeline.", 15, "Mostrare quante celle sono state convertite a NaN e perché.", "Cosa fa errors='coerce' rispetto a errors='raise' o errors='ignore'?")

    # 18. Calcolo Sconti e Netto
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Calcolo Sconti, Margini e Fatturato Netto Finale", "MODULO 2: PANDAS FONDAMENTI (4H)", 18)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "💰 Definizione KPI Economici", [
        "Imponibile Lordo: Quantita * Prezzo_Unitario_Num.",
        "Valore Sconto: Lordo * (Sconto_Perc / 100).",
        "Fatturato Netto: Lordo - Valore Sconto.",
        "Arrotondamento coerente a 2 cifre decimali per l'allineamento con la contabilità."
    ])
    code = [
        "# Calcolo completo delle colonne economiche",
        "df_roma['Totale_Lordo'] = df_roma['Quantita'] * df_roma['Prezzo_Num']",
        "df_roma['Valore_Sconto'] = df_roma['Totale_Lordo'] * (df_roma['Sconto_Perc'] / 100.0)",
        "df_roma['Fatturato_Netto'] = round(df_roma['Totale_Lordo'] - df_roma['Valore_Sconto'], 2)",
        "print(df_roma[['Totale_Lordo', 'Valore_Sconto', 'Fatturato_Netto']].head(3))"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Pipeline di Calcolo Finanziario", code)
    add_notes(s, "Verificare che tutti gli studenti abbiano ottenuto colonne numeriche coerenti.", 15, "Far notare l'importanza dell'arrotondamento per evitare problemi di precisione in virgola mobile.", "Qual è la differenza di fatturato complessivo prima e dopo lo sconto?")

    # 19. Ordinamento e Top Deals
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Ordinamento Dati con .sort_values() & Top Deals", "MODULO 2: PANDAS FONDAMENTI (4H)", 19)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🏆 Ranking e Analisi di Pareto", [
        "df.sort_values(by='colonna', ascending=False) ordina i record in modo decrescente.",
        "Ordinamento multi-colonna: by=['Filiale', 'Fatturato_Netto'], ascending=[True, False].",
        "Estrazione istantanea dei Top 10 Deals aziendali con .head(10).",
        "Identificazione dei clienti strategici (Key Accounts)."
    ])
    code = [
        "# Estrazione Top 10 Contratti per Fatturato",
        "top_10 = df_roma.sort_values(",
        "    by='Fatturato_Netto', ascending=False",
        ")[['ID_Transazione', 'Ragione_Sociale', 'Nome_Prodotto', 'Fatturato_Netto']].head(10)",
        "print(top_10.to_string(index=False))"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Estrazione Top 10 Contratti", code)
    add_notes(s, "Mostrare l'applicazione del ranking sui contratti ad alto valore.", 15, "Far notare quali prodotti e clienti compaiono più frequentemente nella Top 10.", "Qual è l'ordine a maggior valore registrato a Roma?")

    # 20. Statistiche Descrittive
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Statistiche Descrittive e Metriche di Posizione", "MODULO 2: PANDAS FONDAMENTI (4H)", 20)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📈 Indicatori Statistici di Sintesi", [
        "Media vs Mediana: quando i dati sono asimmetrici o ci sono outlier, la mediana è più robusta.",
        ".sum(): Fatturato cumulato totale della filiale.",
        ".mean() e .median(): Ticket medio e valore mediano per ordine.",
        ".quantile([0.25, 0.50, 0.75]): Analisi della distribuzione e percentili di spesa."
    ])
    code = [
        "tot_fatt = df_roma['Fatturato_Netto'].sum()",
        "avg_fatt = df_roma['Fatturato_Netto'].mean()",
        "med_fatt = df_roma['Fatturato_Netto'].median()",
        "p90 = df_roma['Fatturato_Netto'].quantile(0.90)",
        "print(f'Totale: € {tot_fatt:,.2f}')",
        "print(f'Media:  € {avg_fatt:,.2f} | Mediana: € {med_fatt:,.2f}')",
        "print(f'90° Percentile: € {p90:,.2f}')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Calcolo Metriche di Sintesi", code)
    add_notes(s, "Spiegare la differenza pratica tra media e mediana nel business.", 15, "Mostrare perché un ordine enorme sposta la media ma non la mediana.", "Se la media è 3.500€ e la mediana è 1.200€, cosa significa per il business?")

    # 21. value_counts
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Analisi delle Frequenze con .value_counts()", "MODULO 2: PANDAS FONDAMENTI (4H)", 21)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📊 Distribuzione dei Volumi", [
        "df['Canale'].value_counts() conta il numero di transazioni per ciascuna categoria.",
        "Parametro normalize=True restituisce la quota percentuale sul totale.",
        "Parametro dropna=False include i valori mancanti per verificare l'integrità dei dati.",
        "Strumento indispensabile per capire la composizione del canale distributivo."
    ])
    code = [
        "# Conteggio assoluto per canale",
        "print(df_roma['Canale_Vendita'].value_counts())",
        "",
        "# Quote percentuali di vendita",
        "quote = df_roma['Canale_Vendita'].value_counts(normalize=True) * 100",
        "for canale, pct in quote.items():",
        "    print(f'{canale:20}: {pct:5.1f}%')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Quote Canali di Vendita", code)
    add_notes(s, "Mostrare la rapidità di calcolo delle quote di mercato interne.", 15, "Far confrontare i canali digitali rispetto a quelli tradizionali.", "Qual è il canale di vendita dominante nella filiale di Roma?")

    # 22. Recap Modulo 2
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Recap Modulo 2: Padronanza del DataFrame Pandas", "MODULO 2: PANDAS FONDAMENTI (4H)", 22)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🎯 Competenze Acquisite", [
        "Caricamento ed esplorazione di file Excel complessi.",
        "Filtri logici con condizioni multiple e operatori &, |, ~.",
        "Creazione di colonne calcolate vettoriali e cast numerico sicuro.",
        "Ordinamento, statistiche descrittive e Top Deals."
    ], bg_color=RGBColor(236, 253, 245), border_color=C_GREEN, title_color=C_GREEN)
    create_card(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "🚀 Verso il Data Wrangling (Modulo 3)", [
        "Nel dataset reale abbiamo notato 48 duplicati e date con formati diversi.",
        "Nel Modulo 3 affronteremo la bonifica professionale: deduplicazione, imputazione nulli, parsing date miste.",
        "Collegheremo le vendite con l'anagrafica clienti ufficiale tramite le JOIN relazionali (pd.merge).",
        "Costruiremo aggregazioni avanzate con groupby().agg()."
    ], bg_color=RGBColor(254, 243, 199), border_color=C_AMBER, title_color=C_AMBER)
    add_notes(s, "Consolidare i concetti di Pandas prima di passare alla fase di pulizia pesante.", 10, "Verificare che tutti abbiano completato il Laboratorio 2.", "Cosa fareste se un dataset contenesse duplicati esatti di righe?")

def build_module_3(prs, blank_layout):
    """Modulo 3: Data Wrangling, Pulizia e Integrazione (Slide 23 - 34, 12 slide)"""
    # 23. Dirty Data
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Anatomia del 'Dirty Data' nei Gestionali Aziendali", "MODULO 3: DATA WRANGLING & MERGE (3H)", 23)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "⚠️ I 4 Grandi Problemi dei Dati Reali", [
        "1. Record Duplicati: Ordini inseriti due volte da utenti diversi.",
        "2. Formati Data Misti: ISO, date italiane, seriali Excel ('45506'), testo ('15-Mar-2024').",
        "3. Valori Mancanti (NaN): Prezzi o quantità omesse nei form.",
        "4. Categorie e Testi Sporchi: 'HW', 'Hardware ', 'Softwre', spazi e maiuscole errate."
    ])
    img_merge = os.path.join(ASSETS_DIR, "diagramma_relazionale_merge.png")
    if os.path.exists(img_merge):
        s.shapes.add_picture(img_merge, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2))
    add_notes(s, "Introdurre il concetto di Data Wrangling: il 70% del tempo di un Data Analyst è dedicato alla pulizia.", 15, "Mostrare le righe sporche direttamente dal file Excel roma.xlsx.", "Quali conseguenze avrebbe calcolare il fatturato senza rimuovere i duplicati?")

    # 24. Deduplica
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Rilevamento ed Eliminazione Record Duplicati", "MODULO 3: DATA WRANGLING & MERGE (3H)", 24)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🧹 Pulizia dei Duplicati", [
        "df.duplicated(): Identifica le righe duplicate restituendo una maschera booleana.",
        "Parametro subset=['ID_Transazione']: Controlla duplicati solo su colonne chiave.",
        "df.drop_duplicates(keep='first'): Mantiene la prima occorrenza ed elimina i doppioni.",
        "Verifica: conteggio righe prima e dopo la rimozione per tracciare i record scartati."
    ])
    code = [
        "# Diagnosi e rimozione duplicati",
        "n_init = len(df_roma)",
        "n_dup = df_roma.duplicated().sum()",
        "print(f'Duplicati rilevati: {n_dup}')",
        "",
        "df_clean = df_roma.drop_duplicates().copy()",
        "print(f'Righe pulite: {len(df_clean)} (rimosse: {n_init - len(df_clean)})')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Deduplicazione con drop_duplicates", code)
    add_notes(s, "Mostrare la differenza tra duplicato esatto (tutte le colonne uguali) e duplicato su chiave.", 15, "Far eseguire il comando agli studenti sul file di Roma.", "Cosa fa il parametro keep='last' rispetto a keep='first'?")

    # 25. Standardizzazione Testi
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Standardizzazione Stringhe e Categorie Merceologiche", "MODULO 3: DATA WRANGLING & MERGE (3H)", 25)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🔤 Pulizia Testuale e Normalizzazione", [
        "Rimozione spazi bianchi parassiti con .str.strip().",
        "Uniformazione codici anagrafici in maiuscolo con .str.upper().",
        "Mappatura delle categorie disallineate ('HW', 'Hardwre' ➔ 'Hardware') tramite dizionari o funzioni di classificazione con .apply().",
        "Riconduzione a uno schema standard a 4 categorie ufficiali."
    ])
    code = [
        "def normalizza_cat(val):",
        "    if pd.isna(val): return 'Altro'",
        "    s = str(val).strip().lower()",
        "    if 'hard' in s or 'hw' in s: return 'Hardware'",
        "    if 'soft' in s or 'sw' in s: return 'Software'",
        "    if 'serv' in s: return 'Servizi'",
        "    if 'canc' in s: return 'Cancelleria'",
        "    return 'Altro'",
        "",
        "df_clean['Categoria'] = df_clean['Categoria_Prodotto'].apply(normalizza_cat)"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Funzione di Trascodifica Categorie", code)
    add_notes(s, "Spiegare come le incongruenze di testo creano categorie fittizie nei report se non normalizzate.", 15, "Mostrare la distribuzione prima e dopo la normalizzazione.", "Perché 'Hardware' e 'Hardware ' verrebbero contate come due categorie separate?")

    # 26. Date Miste
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "La Sfida delle Date: Gestione Formati Misti ed Excel Serials", "MODULO 3: DATA WRANGLING & MERGE (3H)", 26)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📅 Disomogeneità Temporale", [
        "Excel memorizza le date come numero di giorni trascorsi dal 30/12/1899 (es. 45506 = 02/08/2024).",
        "Nei file esportati coesistono date ISO ('2024-05-06'), italiane ('06/05/2024') e seriali interi.",
        "pd.to_datetime da solo fallisce o interpreta male giorni e mesi se non guidato.",
        "Soluzione: Funzione di parsing ibrida e robusta."
    ])
    code = [
        "# Parsing seriale Excel e date miste",
        "import datetime",
        "def parse_data_ibrida(val):",
        "    if pd.isna(val): return pd.NaT",
        "    s = str(val).strip()",
        "    if s.isdigit(): # Seriale Excel",
        "        dt = datetime.date(1899, 12, 30) + datetime.timedelta(days=int(s))",
        "        return pd.to_datetime(dt)",
        "    return pd.to_datetime(s, format='mixed', dayfirst=True)"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Algoritmo di Parsing Date Miste", code)
    add_notes(s, "Illustrare il funzionamento dei numeri seriali di data di Excel.", 15, "Far notare il parametro dayfirst=True per evitare inversioni tra giorno e mese.", "Cosa rappresenta il numero 45506 in un foglio Excel?")

    # 27. Feature Engineering Date
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Feature Engineering Temporale: Mesi, Trimestri e Giorni", "MODULO 3: DATA WRANGLING & MERGE (3H)", 27)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "⏱️ Arricchimento del Dato Temporale", [
        "L'accessore .dt permette di estrarre componenti atomiche da colonne datetime64.",
        ".dt.year, .dt.month, .dt.day: Componenti numeriche.",
        ".dt.strftime('%B'): Nome del mese per grafici ed etichette.",
        ".dt.to_period('Q'): Trimestre fiscale (2024Q1, 2024Q2) per la reportistica trimestrale."
    ])
    code = [
        "df_clean['Data_dt'] = df_clean['Data_Vendita'].apply(parse_data_ibrida)",
        "df_clean['Data_dt'] = pd.to_datetime(df_clean['Data_dt'])",
        "",
        "df_clean['Anno'] = df_clean['Data_dt'].dt.year",
        "df_clean['Mese'] = df_clean['Data_dt'].dt.month",
        "df_clean['Mese_Nome'] = df_clean['Data_dt'].dt.strftime('%b')",
        "df_clean['Trimestre'] = df_clean['Data_dt'].dt.to_period('Q').astype(str)"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Estrazione Componenti Temporali", code)
    add_notes(s, "Mostrare come il feature engineering temporale prepari i dati per i grafici di trend e per la dashboard.", 15, "Spiegare la comodità dell'accessore .dt.", "Come possiamo raggruppare le vendite per trimestre?")

    # 28. Imputazione Condizionale
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Trattamento Professionale dei Valori Mancanti (Imputazione)", "MODULO 3: DATA WRANGLING & MERGE (3H)", 28)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🩹 Drop vs Imputazione Intelligente", [
        "Cancellare righe con dropna() riduce il campione e distorce i totali di vendita.",
        "Imputare con la media globale mescola prezzi di Server (1.850€) con Cancelleria (45€).",
        "Soluzione migliore: Imputazione condizionale per gruppo con transform('mean') o transform('median').",
        "Il prezzo mancante di un Server viene sostituito con la media dei soli Server."
    ])
    code = [
        "# Imputazione del prezzo medio per specifico prodotto",
        "media_prod = df_clean.groupby('Nome_Prodotto')['Prezzo_Num'].transform('mean')",
        "df_clean['Prezzo_Unitario_Fin'] = df_clean['Prezzo_Num'].fillna(media_prod)",
        "",
        "# Imputazione quantita con mediana per prodotto",
        "med_qta = df_clean.groupby('Nome_Prodotto')['Quantita'].transform('median')",
        "df_clean['Quantita_Fin'] = df_clean['Quantita'].fillna(med_qta).astype(int)"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Imputazione Condizionale con transform()", code)
    add_notes(s, "Evidenziare la differenza fondamentale tra media globale ed imputazione per gruppo.", 15, "Mostrare come transform() mantenga la stessa lunghezza del DataFrame originale.", "Perché non dovremmo mai sostituire un prezzo nullo con la media generale di tutto il catalogo?")

    # 29. Teoria JOIN e Merge
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Integrazione Dati: Concetti di JOIN Relazionale", "MODULO 3: DATA WRANGLING & MERGE (3H)", 29)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🔗 Modello Relazionale dei Dati", [
        "Tabella dei Fatti: Transazioni di vendita (molte righe, contiene chiavi esterne FK).",
        "Tabella Dimensionale: Anagrafica Clienti (una riga per cliente, chiave primaria PK).",
        "Left Join: Mantiene tutte le vendite e aggancia i dettagli anagrafici corrispondenti.",
        "Evitare duplicazioni cartesiane verificando l'univocità della chiave nell'anagrafica."
    ])
    img_merge2 = os.path.join(ASSETS_DIR, "diagramma_relazionale_merge.png")
    if os.path.exists(img_merge2):
        s.shapes.add_picture(img_merge2, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2))
    add_notes(s, "Spiegare la Left Join come analogo moderno e robusto del CERCA.VERT (VLOOKUP) di Excel.", 15, "Far notare che la merge in Pandas non soffre dei limiti di ordinamento o posizione delle colonne.", "Cosa accade se un cliente nella tabella vendite non esiste nell'anagrafica?")

    # 30. Implementazione pd.merge
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Implementazione della JOIN con pd.merge()", "MODULO 3: DATA WRANGLING & MERGE (3H)", 30)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🛠️ Sintassi e Parametri Chiave", [
        "pd.merge(left, right, on='Codice_Cliente', how='left').",
        "Arricchimento del dataset vendite con: Settore merceologico, Sede e Rating creditizio.",
        "Trattamento dei non abbinati: .fillna('Non Specificato').",
        "Verifica finale del numero di righe: non deve aumentare dopo una Left Join 1-a-molti."
    ])
    code = [
        "# Caricamento anagrafica clienti ufficiale",
        "df_anag = pd.read_excel('dataset/raw/roma.xlsx', sheet_name='Anagrafica_Clienti')",
        "df_anag['Codice_Cliente'] = df_anag['Codice_Cliente'].str.strip().str.upper()",
        "",
        "# Esecuzione Left Join",
        "df_merged = pd.merge(",
        "    df_clean,",
        "    df_anag[['Codice_Cliente', 'Settore', 'Citta_Sede', 'Rating_Affidabilita']],",
        "    on='Codice_Cliente', how='left'",
        ")",
        "df_merged['Settore'] = df_merged['Settore'].fillna('Non Specificato')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Merge con Anagrafica Clienti", code)
    add_notes(s, "Far eseguire il merge e verificare che il conteggio righe sia rimasto esattamente a 1.200.", 15, "Mostrare come le colonne Settore e Rating_Affidabilita siano ora disponibili per l'analisi.", "Come si risolvono eventuali conflitti nei nomi colonna con il parametro suffixes?")

    # 31. GroupBy e Aggregazioni
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Raggruppamenti Strategici con groupby() e .agg()", "MODULO 3: DATA WRANGLING & MERGE (3H)", 31)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📊 Il Paradigma Split-Apply-Combine", [
        "Split: Suddivide il DataFrame in gruppi (es. per Settore cliente).",
        "Apply: Applica funzioni statistiche a ciascun gruppo (somma, media, conteggio).",
        "Combine: Ricompone i risultati in una tabella riepilogativa ordinata.",
        "Named Aggregation con .agg(): Consente di rinominare le metriche direttamente all'interno della chiamata."
    ])
    code = [
        "# Calcolo KPI di performance per Settore cliente",
        "report_settore = df_merged.groupby('Settore').agg(",
        "    Fatturato_Totale=('Fatturato_Netto', 'sum'),",
        "    Sconto_Medio_Perc=('Sconto_Perc', 'mean'),",
        "    Numero_Ordini=('ID_Transazione', 'count'),",
        "    Pezzi_Venduti=('Quantita_Fin', 'sum')",
        ").reset_index().sort_values(by='Fatturato_Totale', ascending=False)",
        "print(report_settore.head(3).to_string(index=False))"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Named Aggregations con .agg()", code)
    add_notes(s, "Spiegare la Named Aggregation come standard moderno per creare report puliti.", 15, "Mostrare come ordinare il report per fatturato decrescente.", "Quale settore genera il fatturato maggiore a Roma?")

    # 32. Laboratorio 3
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Laboratorio 3: Data Cleaning Completo e Report Settori", "MODULO 3: DATA WRANGLING & MERGE (3H)", 32)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🧪 Esercitazione Pratica Studenti", [
        "File: laboratori/lab03_data_wrangling/lab03_esercizi.py",
        "Task 1: Rimuovere i 48 duplicati esatti dal dataset Roma.",
        "Task 2: Normalizzare le categorie merceologiche su 4 classi standard.",
        "Task 3: Effettuare il parsing del 100% delle date eterogenee.",
        "Task 4: Imputare prezzi e quantità mancanti con medie/mediane per prodotto.",
        "Task 5: Effettuare il merge con l'anagrafica clienti e produrre il report per settore."
    ], bg_color=RGBColor(240, 249, 255), border_color=C_BLUE)
    code = [
        "--- VERIFICA OUTPUT LABORATORIO 3 ---",
        "Righe iniziali: 1248 | Duplicati: 48 | Rimanenti: 1200",
        "Date valide: 1200 / 1200 (100% corrette)",
        "Top Settori per Fatturato Netto:",
        " 1. Editoria & Cultura:        € 468.706,11 (110 ordini)",
        " 2. Trasporti & Logistica:     € 465.959,68 (102 ordini)",
        " 3. Information Technology:    € 397.243,77 ( 95 ordini)",
        " 4. Commercio al Dettaglio:    € 370.229,06 ( 95 ordini)",
        " 5. Manifatturiero:            € 360.685,56 ( 90 ordini)"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Output Atteso (lab03_esercizi.py)", code)
    add_notes(s, "Guidare gli studenti nella risoluzione del laboratorio. Dedicare tempo al debug del parsing date.", 45, "Verificare che i totali coincidano al centesimo con la soluzione.", "Tutti sono riusciti ad ottenere 1.200 righe pulite e coerenti?")

    # 33. Pivot Table
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Tabelle Pivot Bidimensionali con pd.pivot_table()", "MODULO 3: DATA WRANGLING & MERGE (3H)", 33)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🔲 Matrici di Dati Incrociate", [
        "pd.pivot_table(df, index='Righe', columns='Colonne', values='Valori', aggfunc='sum').",
        "Crea matrici bidimensionali pronte per l'analisi incrociata (es. Canale x Categoria).",
        "Parametro fill_value=0 per sostituire celle vuote con zeri.",
        "Parametro margins=True per inserire totali complessivi di riga e colonna."
    ])
    code = [
        "# Tabella Pivot: Canale di Vendita x Categoria Prodotto",
        "pivot_canale_cat = pd.pivot_table(",
        "    df_merged,",
        "    index='Canale_Vendita',",
        "    columns='Categoria',",
        "    values='Fatturato_Netto',",
        "    aggfunc='sum',",
        "    fill_value=0",
        ")",
        "print((pivot_canale_cat / 1000.0).round(1))  # In k€"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Costruzione Matrice Pivot", code)
    add_notes(s, "Confrontare la pivot_table di Pandas con le tabelle pivot di Excel.", 15, "Mostrare come questa matrice sia la base diretta per generare la Heatmap nel Modulo 4.", "Qual è la combinazione Canale-Categoria che genera più fatturato?")

    # 34. Recap Modulo 3
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Recap Modulo 3: Pipeline di Bonifica Dati Certificata", "MODULO 3: DATA WRANGLING & MERGE (3H)", 34)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🎯 Competenze Acquisite", [
        "Deduplicazione sicura e normalizzazione stringhe anagrafiche.",
        "Parsing robusto di date miste, seriali Excel e formati testuali.",
        "Imputazione condizionale intelligente senza distorsione dei totali.",
        "Integrazione relazionale (Left Join) con anagrafiche esterne e Named Aggregations."
    ], bg_color=RGBColor(236, 253, 245), border_color=C_GREEN, title_color=C_GREEN)
    create_card(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "🚀 Verso la Visualizzazione (Modulo 4)", [
        "Ora che i dati sono puliti, coerenti e certificati, possiamo visualizzarli.",
        "Nel Modulo 4 utilizzeremo Matplotlib e Seaborn per trasformare i numeri in grafici per il CdA.",
        "Creeremo barplot con etichette k€, serie temporali con linee di target, heatmap e l'Executive Dashboard 2x2.",
        "Impareremo a esportare grafici ad alta risoluzione (300 DPI) per la stampa."
    ], bg_color=RGBColor(254, 243, 199), border_color=C_AMBER, title_color=C_AMBER)
    add_notes(s, "Punto di svolta del corso: i dati sono finalmente puliti e pronti per il business.", 10, "Congratularsi con l'aula per aver completato la parte più ostica (il data cleaning).", "Cosa rende un grafico aziendale immediatamente comprensibile a un dirigente?")

def build_module_4(prs, blank_layout):
    """Modulo 4: Visualizzazione Dati e Reporting (Slide 35 - 45, 11 slide)"""
    # 35. Principi Storytelling
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Principi di Data Storytelling e Visualizzazione Direzionale", "MODULO 4: VISUALIZZAZIONE & REPORTING (3H)", 35)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📊 Regole per Grafici Efficaci", [
        "Eliminare il disordine (Chartjunk): no 3D, no gradienti inutili, no griglie pesanti.",
        "Scegliere il tipo di grafico corretto per la domanda di business:",
        " • Confronti tra entità ➔ Bar Chart orizzontale o verticale.",
        " • Trend ed evoluzione temporale ➔ Line Chart con marker.",
        " • Relazioni incrociate ➔ Heatmap con annotazioni.",
        " • Dispersione e outlier ➔ Boxplot.",
        "Unità di misura sempre esplicitate (k€, %, M€) e titoli auto-esplicativi."
    ])
    img_exec = os.path.join(GEN_DIR, "executive_report.png")
    if os.path.exists(img_exec):
        s.shapes.add_picture(img_exec, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2))
    add_notes(s, "Spiegare la psicologia della percezione visiva nei report direzionali.", 15, "Mostrare l'anteprima della Executive Dashboard 2x2 che realizzeremo nel modulo.", "Perché i grafici a torta con più di 5 fette sono sconsigliati nei report finanziari?")

    # 36. Matplotlib Figure & Axes
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Anatomia di Matplotlib: Figure e Axes (Approccio OOP)", "MODULO 4: VISUALIZZAZIONE & REPORTING (3H)", 36)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📐 Architettura Orientata a Oggetti", [
        "Figure: Il contenitore generale / canvas della grafica.",
        "Axes: Il singolo grafico con asse X, asse Y, titoli, griglia e tick.",
        "Sintassi standard: fig, ax = plt.subplots(figsize=(10, 5)).",
        "Controllo totale su margini, spaziature, label e DPI di rendering."
    ])
    code = [
        "import matplotlib.pyplot as plt",
        "# Creazione canvas OOP",
        "fig, ax = plt.subplots(figsize=(9, 4.5), dpi=150)",
        "ax.set_title('Titolo del Grafico', fontsize=12, fontweight='bold')",
        "ax.set_xlabel('Asse X (Unità)', fontweight='bold')",
        "ax.set_ylabel('Asse Y (Unità)', fontweight='bold')",
        "ax.grid(True, linestyle='--', alpha=0.6)",
        "plt.tight_layout()",
        "plt.show()"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Struttura Base Matplotlib OOP", code)
    add_notes(s, "Spiegare la differenza tra l'approccio orientato a oggetti (fig, ax) e l'approccio procedurale (plt.plot).", 15, "Insegnare l'uso di tight_layout() per evitare testi tagliati.", "Perché l'approccio OOP è fondamentale quando si creano cruscotti multi-plot?")

    # 37. Bar Chart Top Clienti
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Bar Chart Orizzontale con Etichette Dati (Top Clienti)", "MODULO 4: VISUALIZZAZIONE & REPORTING (3H)", 37)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🏆 Evidenziare i Key Accounts", [
        "ax.barh(categorie, valori) crea barre orizzontali leggibili anche con nomi lunghi.",
        "Divisione per 1.000 per esprimere gli importi in k€.",
        "Ciclo di annotazione per scrivere il valore numerico direttamente accanto a ciascuna barra.",
        "Ordinamento crescente per avere il cliente top in cima alla vista."
    ])
    img_top = os.path.join(GEN_DIR, "ex4_1_top_clienti.png")
    if os.path.exists(img_top):
        s.shapes.add_picture(img_top, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2))
    add_notes(s, "Spiegare perché il grafico a barre orizzontale è la scelta migliore quando le etichette di testo sono lunghe.", 15, "Mostrare come inserire le label di testo sui dati con ax.text().", "Qual è il fatturato del primo cliente di Roma?")

    # 38. Serie Temporali
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Serie Temporali: Trend Mensile con Linea di Media", "MODULO 4: VISUALIZZAZIONE & REPORTING (3H)", 38)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📅 Monitorare l'Andamento Temporale", [
        "ax.plot(mesi, valori, marker='o', linewidth=2.5, color='#2ca02c') traccia la curva di vendita.",
        "ax.axhline(media, color='red', linestyle='--') inserisce una linea di target o media annuale.",
        "Etichette dei mesi chiare (Gen, Feb, Mar...) tramite ax.set_xticks() e set_xticklabels().",
        "Legenda posizionata in modo strategico per non coprire i punti dati."
    ])
    img_trend = os.path.join(GEN_DIR, "ex4_2_trend_mensile.png")
    if os.path.exists(img_trend):
        s.shapes.add_picture(img_trend, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2))
    add_notes(s, "Mostrare come una linea orizzontale di media o budget fornisca contesto immediato al lettore.", 15, "Far notare i picchi di vendita stagionali.", "In quali mesi le vendite superano la media annuale?")

    # 39. Seaborn Stile
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Seaborn: Visualizzazioni Statistiche e Design Moderno", "MODULO 4: VISUALIZZAZIONE & REPORTING (3H)", 39)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🎨 Eleganza e Statistica Avanzata", [
        "Libreria di alto livello costruita su Matplotlib, integrata nativamente con DataFrame Pandas.",
        "Temi professionali preconfigurati: sns.set_theme(style='whitegrid').",
        "Palette di colori armonizzate: 'Blues', 'Set2', 'viridis', 'YlGnBu'.",
        "Gestione automatica di raggruppamenti con il parametro hue."
    ])
    code = [
        "import seaborn as sns",
        "# Configurazione globale tema",
        "sns.set_theme(style='whitegrid', font='sans-serif')",
        "",
        "# Barplot raggruppato Categoria x Canale",
        "fig, ax = plt.subplots(figsize=(8, 4))",
        "sns.barplot(data=df_clean, x='Categoria', y='Fatturato_Netto',",
        "            hue='Canale_Vendita', errorbar=None, ax=ax)",
        "ax.set_ylabel('Fatturato Medio (€)')",
        "plt.tight_layout()"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Utilizzo Rapido di Seaborn", code)
    add_notes(s, "Illustrare come Seaborn semplifichi grafici statistici complessi in poche righe di codice.", 15, "Mostrare come il parametro hue suddivida automaticamente i dati per canale.", "Qual è il vantaggio di usare Seaborn rispetto a scrivere tutto in Matplotlib puro?")

    # 40. Boxplot Outlier
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Analisi delle Distribuzioni e Outlier: Boxplot", "MODULO 4: VISUALIZZAZIONE & REPORTING (3H)", 40)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📦 Diagnostica della Dispersione", [
        "Anatomia del Boxplot: Mediana (linea centrale), Box (50% dei dati tra Q1 e Q3), Baffi (1.5 * IQR).",
        "Punti isolati oltre i baffi: Outlier commerciali (sconti anomali o transazioni eccezionali).",
        "sns.boxplot(data=df, x='Canale_Vendita', y='Sconto_Perc') confronta la politica sconti tra canali.",
        "Permette al management di verificare se gli agenti rispettano i limiti di sconto."
    ])
    code = [
        "# Boxplot distribuzione sconti per canale",
        "fig, ax = plt.subplots(figsize=(8, 4))",
        "sns.boxplot(",
        "    data=df_clean,",
        "    x='Canale_Vendita',",
        "    y='Sconto_Perc',",
        "    hue='Canale_Vendita',",
        "    palette='Set2',",
        "    legend=False,",
        "    ax=ax",
        ")",
        "ax.set_title('Distribuzione Sconti per Canale')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Boxplot Sconti con Seaborn", code)
    add_notes(s, "Insegnare a leggere un Boxplot in un contesto aziendale (mediana, quartili e sconti fuori scala).", 15, "Far notare l'assenza di warning grazie a hue ed esplicito legend=False.", "Quale canale commerciale applica la mediana di sconto più elevata?")

    # 41. Heatmap Matrice
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Heatmap: Matrice Termica Canale vs Categoria", "MODULO 4: VISUALIZZAZIONE & REPORTING (3H)", 41)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🔥 Mappe Termiche di Concentrazione", [
        "Visualizza l'incrocio tra due variabili categoriche tramite intensità di colore.",
        "Input: Tabella Pivot con somme di fatturato in k€.",
        "sns.heatmap(pivot, annot=True, fmt='.1f', cmap='YlGnBu') mostra i numeri all'interno di ogni cella.",
        "Individua a colpo d'occhio dove si concentra la maggior parte del business."
    ])
    img_heat = os.path.join(GEN_DIR, "ex4_3_heatmap_matrice.png")
    if os.path.exists(img_heat):
        s.shapes.add_picture(img_heat, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2))
    add_notes(s, "Mostrare come la Heatmap renda visibili pattern che in una tabella numerica sfuggirebbero.", 15, "Spiegare la scelta delle mappe di colore (palette sequenziali).", "Quale combinazione Canale-Categoria è la più calda?")

    # 42. Subplots 2x2
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Composizione Multi-Grafico: Griglia 2x2 (Subplots)", "MODULO 4: VISUALIZZAZIONE & REPORTING (3H)", 42)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🔲 Costruzione del Cruscotto Statico", [
        "fig, axes = plt.subplots(2, 2, figsize=(16, 10)) genera una matrice di 4 assi indipendenti.",
        "axes[0, 0]: Grafico a linee (Trend Mensile).",
        "axes[0, 1]: Grafico a barre (Fatturato per Categoria).",
        "axes[1, 0]: Boxplot (Sconti per Canale).",
        "axes[1, 1]: Heatmap (Matrice Canale x Categoria).",
        "Titolo generale d'impatto con fig.suptitle()."
    ])
    code = [
        "fig, axes = plt.subplots(2, 2, figsize=(16, 10))",
        "fig.suptitle('EXECUTIVE SALES DASHBOARD 2024', fontsize=16, fontweight='bold')",
        "",
        "# [0,0] Trend",
        "axes[0, 0].plot(mesi, trend_val, marker='o')",
        "# [0,1] Categorie",
        "axes[0, 1].bar(cat_labels, cat_val)",
        "# [1,0] Boxplot Sconti",
        "sns.boxplot(data=df, x='Canale', y='Sconto', ax=axes[1, 0])",
        "# [1,1] Heatmap",
        "sns.heatmap(pivot_matrice, ax=axes[1, 1])",
        "plt.tight_layout()"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Template Griglia Subplots 2x2", code)
    add_notes(s, "Spiegare l'indicizzazione a matrice degli assi: axes[riga, colonna].", 15, "Mostrare come comporre una tavola coerente pronta per essere stampata o inserita in un report PDF.", "Come si accede al grafico in basso a destra nella griglia?")

    # 43. Executive Report PNG
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Executive Dashboard 2x2 Completa per il Board", "MODULO 4: VISUALIZZAZIONE & REPORTING (3H)", 43)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📑 La Tavola Direzionale Completa", [
        "Cruscotto direzionale integrato: 4 visualizzazioni complementari in un'unica schermata.",
        "1. Andamento nel tempo (Stagionalità e picchi).",
        "2. Composizione del catalogo (Hardware vs Software).",
        "3. Disciplina commerciale (Controllo sconti per canale).",
        "4. Matrice distributiva (Canale x Prodotto).",
        "Esportazione vettoriale o raster ad alta risoluzione (300 DPI)."
    ])
    if os.path.exists(img_exec):
        s.shapes.add_picture(img_exec, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2))
    add_notes(s, "Analizzare insieme all'aula il cruscotto finito, commentando i principali insight di business.", 15, "Far notare l'armonia cromatica e la leggibilità di tutti i testi.", "Se doveste presentare questo report al CEO in 2 minuti, quali punti mettereste in evidenza?")

    # 44. Laboratorio 4
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Laboratorio 4: Creazione ed Esportazione del Report Grafico", "MODULO 4: VISUALIZZAZIONE & REPORTING (3H)", 44)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🧪 Esercitazione Pratica Studenti", [
        "File: laboratori/lab04_visualizzazione/lab04_esercizi.py",
        "Task 1: Generare il barplot orizzontale Top 8 Clienti con valori formattati in k€.",
        "Task 2: Creare la serie storica mensile con marker e linea di media annuale.",
        "Task 3: Costruire la Heatmap Canale x Categoria.",
        "Task 4: Assemblare la griglia 2x2 ed esportare executive_report.png a 300 DPI."
    ], bg_color=RGBColor(240, 249, 255), border_color=C_BLUE)
    code = [
        "--- VERIFICA FILE GENERATI (dataset/generated/) ---",
        "✅ ex4_1_top_clienti.png      (Barplot Top Clienti)",
        "✅ ex4_2_trend_mensile.png     (Serie Storica)",
        "✅ ex4_3_heatmap_matrice.png   (Heatmap Canale x Categoria)",
        "✅ executive_report.png        (Dashboard 2x2 - 300 DPI)",
        "",
        "# Comando di esportazione ad alta definizione:",
        "plt.savefig('executive_report.png', dpi=300, bbox_inches='tight')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Esportazione ad Alta Definizione", code)
    add_notes(s, "Supportare gli studenti nella generazione dei grafici e verificare che i file PNG vengano creati nella cartella corretta.", 45, "Far verificare la nitidezza dell'immagine a 300 DPI.", "Tutti i grafici sono stati salvati correttamente nella cartella dataset/generated/?")

    # 45. Recap Modulo 4
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Recap Modulo 4: Visual Storytelling dei Dati Aziendali", "MODULO 4: VISUALIZZAZIONE & REPORTING (3H)", 45)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🎯 Competenze Acquisite", [
        "Padronanza dell'architettura OOP di Matplotlib (Figure/Axes).",
        "Creazione di grafici statistici moderni con Seaborn.",
        "Costruzione di tavole multi-plot 2x2 con formattazione professionale.",
        "Esportazione di immagini ad alta risoluzione (300 DPI) per la stampa."
    ], bg_color=RGBColor(236, 253, 245), border_color=C_GREEN, title_color=C_GREEN)
    create_card(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "🚀 Verso l'Automazione Pipeline (Modulo 5)", [
        "Finora abbiamo lavorato solo sul file di Roma.",
        "Nel Modulo 5 automatizzeremo l'intero flusso per processare contemporaneamente tutte le filiali (Roma, Milano, Torino).",
        "Costruiremo uno script ETL batch che unisce i file, applica il cleaning e salva il database in formato compresso Apache Parquet.",
        "Creeremo il generatore automatico del report Excel multi-scheda per il CdA."
    ], bg_color=RGBColor(254, 243, 199), border_color=C_AMBER, title_color=C_AMBER)
    add_notes(s, "Riepilogare i progressi didattici: dalla sintassi base alla visualizzazione direzionale.", 10, "Introdurre il concetto di pipeline industriale automatizzata.", "Come possiamo evitare di rieseguire manualmente il codice per ogni singolo file Excel?")

def build_module_5(prs, blank_layout):
    """Modulo 5: Automazione Pipeline ETL (Slide 46 - 53, 8 slide)"""
    # 46. Architettura ETL
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Architettura di una Pipeline ETL Aziendale", "MODULO 5: AUTOMAZIONE PIPELINE ETL (2H)", 46)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "⚙️ Da Script a Processo Industriale", [
        "Extract (E): Riconoscimento ed estrazione automatica dei file di tutte le filiali.",
        "Transform (T): Pulizia centralizzata, deduplica, parsing date e join anagrafica.",
        "Load (L): Salvataggio del master unificato in Apache Parquet e generazione del report Excel.",
        "Vantaggio: Esecuzione in pochi secondi con un solo comando, azzerando gli errori manuali."
    ])
    code = [
        "# Flusso logico della Pipeline ETL",
        "def run_pipeline():",
        "    logging.info('1. Ingestion dati filiali...')",
        "    df_raw, df_anag = carica_dati_filiali('dataset/raw')",
        "    ",
        "    logging.info('2. Trasformazione e bonifica...')",
        "    df_master = trasforma_dataset(df_raw, df_anag)",
        "    ",
        "    logging.info('3. Esportazione Parquet ed Excel...')",
        "    esporta_dataset(df_master, 'dataset/generated')",
        "    logging.info('Pipeline completata!')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Orchestrazione della Pipeline", code)
    add_notes(s, "Introdurre il concetto cardine di ETL (Extract-Transform-Load) nell'ingegneria del dato.", 15, "Mostrare lo schema delle 3 fasi operative.", "Perché è fondamentale separare l'estrazione dalla trasformazione e dal salvataggio?")

    # 47. Ingestion Dinamica glob
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Scansione Dinamica File con glob e Percorsi Portabili", "MODULO 5: AUTOMAZIONE PIPELINE ETL (2H)", 47)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📂 Gestione Dinamica del File System", [
        "Modulo glob: Ricerca file tramite pattern matching (es. glob.glob('dataset/raw/*.xlsx')).",
        "Filtro intelligente: Esclusione di file temporanei lockati di Excel (~$) e file speciali.",
        "Percorsi multipiattaforma: Utilizzo di os.path.join() o pathlib per garantire la compatibilità Linux/Windows.",
        "Scalabilità: Quando una nuova filiale invia il suo file Excel, la pipeline la riconosce automaticamente."
    ])
    code = [
        "import glob, os",
        "def trova_file_filiali(cartella_input):",
        "    pattern = os.path.join(cartella_input, '*.xlsx')",
        "    files = glob.glob(pattern)",
        "    # Filtro file temporanei ed export",
        "    valori = [f for f in files if '~$' not in f and 'report' not in f]",
        "    print(f'Trovati {len(valori)} file da elaborare:')",
        "    for f in valori: print(' •', os.path.basename(f))",
        "    return valori"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Ricerca Dinamica File con glob", code)
    add_notes(s, "Mostrare come il codice non debba mai contenere percorsi fissi (hardcoded).", 15, "Far testare la scansione dinamica sui file presenti in dataset/raw/.", "Cosa accadrebbe se aggiungessimo un nuovo file 'bologna.xlsx' nella cartella?")

    # 48. Ingestion Massiva pd.concat
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Ingestion Massiva e Fusione con pd.concat()", "MODULO 5: AUTOMAZIONE PIPELINE ETL (2H)", 48)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📑 Concatenazione Verticale", [
        "Lettura ciclica di tutti i fogli 'Dati_Vendite' e 'Anagrafica_Clienti'.",
        "Gestione eccezioni con try/except per non interrompere il flusso se un file è corrotto.",
        "pd.concat(lista_df, ignore_index=True) unisce tutti i DataFrame verticalmente in una frazione di secondo.",
        "Deduplicazione dell'anagrafica clienti master con drop_duplicates(subset=['Codice_Cliente'])."
    ])
    code = [
        "lista_vendite, lista_anag = [], []",
        "for f in files_filiali:",
        "    df_v = pd.read_excel(f, sheet_name='Dati_Vendite')",
        "    lista_vendite.append(df_v)",
        "    df_a = pd.read_excel(f, sheet_name='Anagrafica_Clienti')",
        "    lista_anag.append(df_a)",
        "",
        "df_raw_master = pd.concat(lista_vendite, ignore_index=True)",
        "df_anag_master = pd.concat(lista_anag, ignore_index=True).drop_duplicates('Codice_Cliente')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Concatenazione Multi-Filiale", code)
    add_notes(s, "Spiegare la concatenazione verticale di tabelle con le stesse colonne.", 15, "Mostrare come 3 file separati diventino un unico master dataset da 3.744 righe grezze.", "Qual è la differenza tra concat (unione verticale) e merge (unione orizzontale)?")

    # 49. Centralizzazione Cleaning
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Modularità: Centralizzazione delle Trasformazioni", "MODULO 5: AUTOMAZIONE PIPELINE ETL (2H)", 49)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🧼 La Funzione trasforma_dataset()", [
        "Tutte le regole di wrangling apprese nel Modulo 3 vengono incapsulate in un'unica funzione.",
        "1. Deduplicazione su transazioni e chiavi composite.",
        "2. Normalizzazione testi, codici cliente e categorie merceologiche.",
        "3. Parsing del 100% delle date eterogenee e creazione feature temporali.",
        "4. Imputazione condizionale prezzi/quantità e ricalcolo economico.",
        "5. Join relazionale con l'anagrafica clienti master."
    ])
    code = [
        "def trasforma_dataset(df_raw, df_anag):",
        "    # 1. Deduplica",
        "    df = df_raw.drop_duplicates(subset=['ID_Transazione', 'Data_Vendita']).copy()",
        "    # 2. Stringhe e categorie",
        "    df['Categoria_Prodotto'] = df['Categoria_Prodotto'].apply(normalizza_categoria)",
        "    # 3. Date",
        "    df['Data_Vendita'] = pd.to_datetime(df['Data_Vendita'].apply(parse_data_flessibile))",
        "    # 4. Numerici e Merge Anagrafica...",
        "    return df_master"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Pipeline di Trasformazione Modulare", code)
    add_notes(s, "Sottolineare il principio DRY (Don't Repeat Yourself) applicato alle trasformazioni dei dati.", 15, "Mostrare come il codice sia pulito, testabile e manutenibile.", "Quali vantaggi offre avere un'unica funzione di trasformazione per tutte le filiali?")

    # 50. Logging Professionale
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Logging Strutturato vs Print Statement", "MODULO 5: AUTOMAZIONE PIPELINE ETL (2H)", 50)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📝 Monitoraggio di Produzione", [
        "In produzione i print() non bastano: serve tracciamento temporale e gravità degli eventi.",
        "Modulo standard logging con formattazione: %(asctime)s [%(levelname)s] %(message)s.",
        "Livelli standard: DEBUG, INFO (avanzamento), WARNING (anomalie non bloccanti), ERROR (errori).",
        "Tracciamento immediato di: numero record letti, duplicati scartati, fatturato totale generato."
    ])
    code = [
        "import logging",
        "logging.basicConfig(",
        "    level=logging.INFO,",
        "    format='%(asctime)s [%(levelname)s] %(message)s',",
        "    datefmt='%H:%M:%S'",
        ")",
        "logging.info('Avvio elaborazione ETL...')",
        "logging.info(f'Rimossi {n_dup} record duplicati.')",
        "logging.info(f'Fatturato Consolidato: € {tot_netto:,.2f}')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Configurazione del Logger Standard", code)
    add_notes(s, "Spiegare perché il logging è fondamentale negli ambienti server e nei processi automatici notturni.", 15, "Mostrare l'output formattato con orari e livelli su terminale.", "Qual è la differenza tra logging.warning() e logging.error()?")

    # 51. Storage Parquet
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Storage Ottimizzato in Apache Parquet per l'Analytics", "MODULO 5: AUTOMAZIONE PIPELINE ETL (2H)", 51)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "💾 Il Formato Standard per i Big Data", [
        "Apache Parquet: Formato binario colonnare compresso (Snappy).",
        "Compressione 5x rispetto a CSV e 10x rispetto a Excel.",
        "Tipizzazione nativa perfetta: i tipi datetime e float rimangono preservati senza dover rieseguire il casting.",
        "Velocità di lettura 10x superiore: la Dashboard Streamlit caricherà i dati in millisecondi con pd.read_parquet()."
    ])
    code = [
        "# Salvataggio in Apache Parquet",
        "parquet_path = 'dataset/generated/vendite_consolidate_italia.parquet'",
        "df_master.to_parquet(parquet_path, index=False)",
        "",
        "# Benchmark di caricamento istantaneo",
        "df_loaded = pd.read_parquet(parquet_path)",
        "print(f'Master caricato: {len(df_loaded)} record in 12ms!')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Salvataggio e Lettura Parquet", code)
    add_notes(s, "Spiegare il funzionamento dei formati colonnari rispetto ai formati a riga (CSV/Excel).", 15, "Mostrare le dimensioni ridotte del file Parquet su disco.", "Perché Parquet preserva i tipi di dato mentre i CSV richiedono sempre il ricalcolo dei tipi?")

    # 52. Report Excel Multi-Sheet
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Generazione Automatica del Report Excel Direzionale", "MODULO 5: AUTOMAZIONE PIPELINE ETL (2H)", 52)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📑 Excel Multi-Scheda per il Management", [
        "pd.ExcelWriter(..., engine='openpyxl') consente di scrivere più fogli nello stesso file.",
        "Foglio 1: Dettaglio_Transazioni (Tutti i 3.600 record puliti e normalizzati).",
        "Foglio 2: Riepilogo_Filiali (KPI aggregati per sede commerciale).",
        "Foglio 3: Riepilogo_Categorie (Performance per linea di business).",
        "Foglio 4: Riepilogo_Settori (Analisi per settore merceologico clienti)."
    ])
    code = [
        "excel_path = 'dataset/generated/report_direzionale_consolidato.xlsx'",
        "with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:",
        "    df_master.to_excel(writer, sheet_name='Dettaglio_Transazioni', index=False)",
        "    kpi_filiali.to_excel(writer, sheet_name='Riepilogo_Filiali', index=False)",
        "    kpi_categorie.to_excel(writer, sheet_name='Riepilogo_Categorie', index=False)",
        "    kpi_settori.to_excel(writer, sheet_name='Riepilogo_Settori', index=False)",
        "print('Report Excel generato con successo!')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Esportazione Multi-Scheda Excel", code)
    add_notes(s, "Mostrare il file Excel generato aprendolo a schermo per far vedere le 4 schede riepilogative.", 15, "Far notare che questo file viene prodotto automaticamente in meno di 2 secondi.", "Come possiamo automatizzare l'invio via email di questo file a fine mese?")

    # 53. Recap Modulo 5
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Recap Modulo 5: Pipeline ETL End-to-End Eseguita con Successo", "MODULO 5: AUTOMAZIONE PIPELINE ETL (2H)", 53)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🎯 Competenze Acquisite", [
        "Ingestion multi-file automatica e indipendente dal sistema operativo.",
        "Pipeline di trasformazione centralizzata ed incapsulata.",
        "Logging strutturato per monitoraggio di produzione.",
        "Doppio output: Apache Parquet per la web app ed Excel per la direzione."
    ], bg_color=RGBColor(236, 253, 245), border_color=C_GREEN, title_color=C_GREEN)
    create_card(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "🚀 Verso la Dashboard Streamlit (Modulo 6)", [
        "Il database nazionale consolidato (3.600 record puliti per oltre 12.6M€ di fatturato) è pronto in Parquet.",
        "Nel Modulo 6 abbandoneremo i report statici e creeremo un'applicazione Web interattiva completa con Streamlit.",
        "Aggiungeremo filtri dinamici a tendina, indicatori KPI, grafici reattivi, ricerca full-text e un simulatore di scenari What-If per il CdA."
    ], bg_color=RGBColor(254, 243, 199), border_color=C_AMBER, title_color=C_AMBER)
    add_notes(s, "Congratularsi con l'aula: la pipeline è operativa e produce dati certificati.", 10, "Lanciare la soluzione sol05_automazione_pipeline.py a schermo intero.", "Qual è il fatturato totale consolidato delle 3 filiali?")

def build_module_6(prs, blank_layout):
    """Modulo 6: Dashboard Streamlit (Slide 54 - 66, 13 slide)"""
    # 54. Intro Streamlit
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Introduzione a Streamlit: Web Analytics in Pure Python", "MODULO 6: DASHBOARD STREAMLIT (4H)", 54)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🌐 Il Paradigma Low-Code Python", [
        "Streamlit trasforma script Python in applicazioni web interattive in tempo reale.",
        "Nessun bisogno di HTML, CSS o JavaScript: si scrive solo codice Python.",
        "Modello di esecuzione reattivo: ogni volta che l'utente interagisce con un filtro, lo script si riesegue dall'alto verso il basso aggiornando la vista.",
        "Comando di avvio: streamlit run dashboard/app.py."
    ])
    img_mockup = os.path.join(ASSETS_DIR, "mockup_dashboard_streamlit.png")
    if os.path.exists(img_mockup):
        s.shapes.add_picture(img_mockup, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2))
    add_notes(s, "Presentare Streamlit come lo strumento leader per Data Science e Business Intelligence in Python.", 15, "Far avviare la prima app starter agli studenti su porta locale.", "Perché Streamlit è più veloce da sviluppare rispetto a una tradizionale app web Django/React?")

    # 55. Caching
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Caching ad Alte Prestazioni con @st.cache_data", "MODULO 6: DASHBOARD STREAMLIT (4H)", 55)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "⚡ Velocità e Ottimizzazione Memoria", [
        "Dato che Streamlit riesegue lo script ad ogni clic, ricaricare il database Parquet dal disco sarebbe lento.",
        "Il decoratore @st.cache_data memorizza il risultato della funzione in RAM.",
        "Al secondo clic dell'utente, il dato viene servito istantaneamente dalla cache in 0 millisecondi.",
        "Parametro ttl=600 (Time-To-Live) per invalidare la cache ogni 10 minuti."
    ])
    code = [
        "import streamlit as st",
        "import pandas as pd",
        "",
        "@st.cache_data(ttl=600)",
        "def load_dataset():",
        "    parquet_path = 'dataset/generated/vendite_consolidate_italia.parquet'",
        "    df = pd.read_parquet(parquet_path)",
        "    df['Data_Vendita'] = pd.to_datetime(df['Data_Vendita'])",
        "    return df",
        "",
        "df_master = load_dataset()"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Decoratore di Caching dei Dati", code)
    add_notes(s, "Spiegare il meccanismo interno di hashing e caching di Streamlit.", 15, "Dimostrare la velocità di reazione dell'interfaccia con e senza cache.", "Cosa accadrebbe all'esperienza utente senza il decoratore @st.cache_data?")

    # 56. Sidebar e Multiselect
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Sidebar e Filtri Dinamici: st.sidebar e st.multiselect", "MODULO 6: DASHBOARD STREAMLIT (4H)", 56)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🎛️ Pannello di Controllo Laterale", [
        "st.sidebar isola i filtri dal corpo centrale della pagina.",
        "st.multiselect('Label', opzioni, default=opzioni): Menu a tendina a selezione multipla con badge rimovibili.",
        "Filtri implementati: Filiali (Roma, Milano, Torino), Categorie Prodotto e Canali di Vendita.",
        "Filtraggio immediato: df[df['Filiale'].isin(sel_filiali)]."
    ])
    code = [
        "# Sidebar con controlli multi-selezione",
        "st.sidebar.title('🎛️ Filtri Commerciali')",
        "filiali = sorted(df_master['Filiale'].unique())",
        "sel_filiali = st.sidebar.multiselect('Filiali', filiali, default=filiali)",
        "",
        "categorie = sorted(df_master['Categoria_Prodotto'].unique())",
        "sel_cat = st.sidebar.multiselect('Categorie', categorie, default=categorie)",
        "",
        "# Applicazione dinamica dei filtri",
        "df_filtrato = df_master[(df_master['Filiale'].isin(sel_filiali)) & \\",
        "                        (df_master['Categoria_Prodotto'].isin(sel_cat))]"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Codice Sidebar e Multiselect", code)
    add_notes(s, "Mostrare come aggiungere widget nella sidebar semplicemente anteponendo st.sidebar.", 15, "Far provare la selezione e deselezione delle filiali a schermo.", "Cosa restituisce st.multiselect quando l'utente deseleziona tutti i valori?")

    # 57. Date Input
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Filtri Temporali a Calendario con st.date_input", "MODULO 6: DASHBOARD STREAMLIT (4H)", 57)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📅 Selezione Intervallo Date", [
        "st.date_input('Periodo', value=(min_date, max_date)) crea un calendario a doppio selettore (Da / A).",
        "Controllo di validità: Verificare che l'utente abbia selezionato entrambi gli estremi prima di applicare il filtro.",
        "Filtraggio su colonna datetime con .dt.date tra data inizio e data fine.",
        "Contatore dinamico del numero di record visualizzati nella sidebar."
    ])
    code = [
        "min_d = df_master['Data_Vendita'].min().date()",
        "max_d = df_master['Data_Vendita'].max().date()",
        "",
        "sel_date = st.sidebar.date_input('Periodo Analisi', (min_d, max_d))",
        "if isinstance(sel_date, (list, tuple)) and len(sel_date) == 2:",
        "    start_d, end_d = sel_date",
        "    df_filtrato = df_filtrato[(df_filtrato['Data_Vendita'].dt.date >= start_d) & \\",
        "                              (df_filtrato['Data_Vendita'].dt.date <= end_d)]"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Filtro Range Temporale", code)
    add_notes(s, "Spiegare la gestione della tupla restituita da st.date_input.", 15, "Mostrare come il filtro temporale aggiorni istantaneamente tutti i KPI della pagina.", "Come gestiamo il caso in cui l'utente clicca solo la data di inizio nel calendario?")

    # 58. KPI Cards st.metric
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Barra Superiore dei KPI con st.columns e st.metric", "MODULO 6: DASHBOARD STREAMLIT (4H)", 58)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📈 Executive Summary Cards", [
        "st.columns(5) divide la larghezza della pagina in 5 colonne affiancate.",
        "st.metric('Titolo', 'Valore', delta='Variazione') renderizza card con numeri grandi e indicatori di performance.",
        "Metriche chiave: 1. Fatturato Netto; 2. Volume Ordini; 3. Ticket Medio; 4. Sconto Medio %; 5. Pezzi Venduti.",
        "Formattazione monetaria con separatori di migliaia e simbolo euro."
    ])
    code = [
        "# Calcolo metriche aggregate sui dati filtrati",
        "tot_fatt = df_filtrato['Fatturato_Netto'].sum()",
        "tot_ord  = len(df_filtrato)",
        "ticket   = tot_fatt / tot_ord if tot_ord > 0 else 0",
        "sconto   = df_filtrato['Sconto_Perc'].mean() if tot_ord > 0 else 0",
        "",
        "c1, c2, c3, c4 = st.columns(4)",
        "c1.metric('💰 Fatturato Netto', f'€ {tot_fatt:,.2f}')",
        "c2.metric('📦 Volume Ordini', f'{tot_ord:,}')",
        "c3.metric('🧾 Ticket Medio', f'€ {ticket:,.2f}')",
        "c4.metric('🏷️ Sconto Medio', f'{sconto:.1f} %')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Creazione Barra KPI Cards", code)
    add_notes(s, "Mostrare l'impatto visivo delle card KPI all'apertura dell'applicazione.", 15, "Spiegare come i valori si ricalcolino dinamicamente in base ai filtri applicati.", "Come possiamo inserire un delta positivo o negativo con st.metric?")

    # 59. Navigazione Tabs
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Organizzazione a Schede Orizzontali con st.tabs", "MODULO 6: DASHBOARD STREAMLIT (4H)", 59)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📑 Struttura a 4 Schede Tematiche", [
        "st.tabs(['Scheda 1', 'Scheda 2', ...]) organizza contenuti complessi senza allungare la pagina.",
        "Tab 1: 📈 Panoramica & Trend (Serie temporali e performance categorie).",
        "Tab 2: 👥 Clienti & Settori (Top 10 Clienti e quote di mercato settoriali).",
        "Tab 3: 🔮 Simulatore What-If (Scenari decisionali per il management).",
        "Tab 4: 📋 Dati & Export (Tabella interattiva, ricerca full-text e download CSV)."
    ])
    code = [
        "# Dichiarazione delle schede tematiche",
        "tab_kpi, tab_clienti, tab_whatif, tab_dati = st.tabs([",
        "    '📈 Panoramica & Trend',",
        "    '👥 Clienti & Settori',",
        "    '🔮 Simulatore What-If',",
        "    '📋 Dati & Export'",
        "])",
        "",
        "with tab_kpi:",
        "    st.subheader('Trend Mensile e Categorie...')",
        "with tab_clienti:",
        "    st.subheader('Analisi Clientela...')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Sintassi dei Context Manager st.tabs", code)
    add_notes(s, "Spiegare il pattern with tab: per popolare ciascuna scheda in modo ordinato.", 15, "Mostrare la fluidità di navigazione tra le schede.", "Quali vantaggi offre l'uso di st.tabs rispetto a una pagina unica lunghissima da scrollare?")

    # 60. Tab 1 Trend Grafici
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Tab 1: Visualizzazione Trend e Categorie con st.pyplot", "MODULO 6: DASHBOARD STREAMLIT (4H)", 60)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📊 Grafici Reattivi ai Filtri", [
        "st.pyplot(fig) visualizza grafici Matplotlib e Seaborn all'interno dell'applicazione web.",
        "Divisione in due colonne (st.columns([3, 2])) per affiancare il trend temporale e le categorie.",
        "Trend multi-filiale: curve separate per Roma, Milano e Torino che si adattano ai filtri sidebar.",
        "Chiusura obbligatoria con plt.close(fig) per rilasciare memoria su server."
    ])
    code = [
        "with tab_kpi:",
        "    col_left, col_right = st.columns([3, 2])",
        "    with col_left:",
        "        # Trend mensile per filiale",
        "        fig, ax = plt.subplots(figsize=(8, 4))",
        "        for fil in sel_filiali:",
        "            sub = df_filtrato[df_filtrato['Filiale'] == fil]",
        "            t = sub.groupby('Mese')['Fatturato_Netto'].sum() / 1000",
        "            ax.plot(t.index, t.values, marker='o', label=fil)",
        "        ax.legend()",
        "        st.pyplot(fig)",
        "        plt.close(fig)"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Rendering Grafico Reattivo", code)
    add_notes(s, "Far notare come i grafici cambino istantaneamente quando si filtrano le filiali nella sidebar.", 15, "Spiegare l'importanza di plt.close(fig) per evitare memory leak sul server.", "Cosa accade al grafico del trend se deselezioniamo la filiale di Milano?")

    # 61. Tab 2 Clienti Settori
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Tab 2: Ranking Top Clienti e Quote per Settore", "MODULO 6: DASHBOARD STREAMLIT (4H)", 61)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🏆 Analisi Clientela e Mercato", [
        "st.dataframe(..., use_container_width=True) renderizza tabelle interattive con ordinamento al clic.",
        "Formattazione monetaria elegante tramite df.style.format({'Fatturato': '€ {:,.2f}'}).",
        "Grafico a torta / ciambella (Donut Chart) delle quote per settore merceologico.",
        "Ispezione immediata dei migliori clienti aziendali e della loro incidenza sul fatturato."
    ])
    code = [
        "with tab_clienti:",
        "    c1, c2 = st.columns(2)",
        "    with c1:",
        "        top_c = df_filtrato.groupby('Ragione_Sociale').agg(",
        "            Fatturato=('Fatturato_Netto', 'sum'),",
        "            Ordini=('ID_Transazione', 'count')",
        "        ).sort_values('Fatturato', ascending=False).head(10)",
        "        st.dataframe(top_c.style.format({'Fatturato': '€ {:,.2f}'}))",
        "    with c2:",
        "        # Donut Chart quote per settore...",
        "        st.pyplot(fig_settori)"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Ranking Clienti e Grafico Settori", code)
    add_notes(s, "Mostrare l'interattività della tabella st.dataframe (ordinamento colonne al clic dell'utente).", 15, "Far analizzare la concentrazione del fatturato sui top client.", "Quale cliente genera il ticket medio più alto?")

    # 62. Tab 4 Ricerca ed Export
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Tab 4: Esploratore Dati, Ricerca Full-Text ed Export CSV", "MODULO 6: DASHBOARD STREAMLIT (4H)", 62)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🔍 Self-Service Data Discovery", [
        "Campo di ricerca libera con st.text_input() per cercare per nome cliente o prodotto.",
        "Filtraggio al volo durante la digitazione con .str.contains().",
        "Pulsante di download nativo con st.download_button().",
        "L'utente business può scaricare il dataset filtrato in formato CSV con un solo clic per ulteriori analisi personali."
    ])
    code = [
        "with tab_dati:",
        "    q = st.text_input('🔍 Cerca cliente, prodotto o codice:')",
        "    df_show = df_filtrato.copy()",
        "    if q:",
        "        m = df_show['Ragione_Sociale'].str.contains(q, case=False, na=False) | \\",
        "            df_show['Nome_Prodotto'].str.contains(q, case=False, na=False)",
        "        df_show = df_show[m]",
        "    st.dataframe(df_show.head(100))",
        "    # Download Button",
        "    csv = df_show.to_csv(index=False).encode('utf-8')",
        "    st.download_button('📥 Scarica CSV', csv, 'export.csv', 'text/csv')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Motore di Ricerca ed Export CSV", code)
    add_notes(s, "Dimostrare la ricerca istantanea digitando 'Tech' o 'Server'.", 15, "Mostrare il funzionamento del download CSV.", "Come possiamo dare autonomia all'utente non tecnico tramite l'export dati?")

    # 63. Tab 3 Simulatore What-If
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Tab 3: Simulatore Decisionale di Scenario ('What-If Analysis')", "MODULO 6: DASHBOARD STREAMLIT (4H)", 63)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🔮 Strumento di Supporto alle Decisioni", [
        "Consente al management di simulare l'impatto di variazioni commerciali sul fatturato totale.",
        "Slider 1: Variazione percentuale del volume vendite (+/- 50%).",
        "Slider 2: Variazione dei punti percentuali di sconto (+/- 15%).",
        "Ricalcolo istantaneo del fatturato simulato con delta monetario e percentuale rispetto alla situazione attuale.",
        "Valore strategico altissimo: trasforma la dashboard da mero strumento di reportistica a tool decisionale."
    ])
    code = [
        "with tab_whatif:",
        "    w1, w2 = st.columns(2)",
        "    d_vol = w1.slider('📈 Variazione Volume (%)', -50, 50, 0, 5)",
        "    d_sco = w2.slider('🏷️ Variazione Sconto (pt %)', -15, 15, 0, 1)",
        "    ",
        "    # Simulazione ricalcolata al volo",
        "    qta_sim = df_filtrato['Quantita'] * (1 + d_vol / 100.0)",
        "    sco_sim = (df_filtrato['Sconto_Perc'] + d_sco).clip(0, 100)",
        "    fatt_sim = (qta_sim * df_filtrato['Prezzo_Unitario'] * (1 - sco_sim/100)).sum()",
        "    delta_val = fatt_sim - tot_fatt",
        "    st.metric('Fatturato Previsto', f'€ {fatt_sim:,.2f}', delta=f'{delta_val:+,.2f} €')"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Logica del Simulatore What-If", code)
    add_notes(s, "Mostrare dal vivo come lo spostamento dello slider modifichi in tempo reale le previsioni di fatturato.", 15, "Far notare l'uso di .clip(0, 100) per evitare sconti negativi o superiori al 100%.", "Se aumentiamo i volumi del 20% ma concediamo il 5% di sconto in più, il margine aumenta o diminuisce?")

    # 64. Custom Styling CSS
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Personalizzazione Grafica e Custom CSS in Streamlit", "MODULO 6: DASHBOARD STREAMLIT (4H)", 64)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🎨 Look & Feel Aziendale Professionale", [
        "Iniezione di CSS personalizzato tramite st.markdown(..., unsafe_allow_html=True).",
        "Personalizzazione di font, card shadow, bordi colorati ed evidenziazione dei blocchi metrici.",
        "Immagini e loghi aziendali nella sidebar con st.sidebar.image().",
        "Badge di stato, avvisi operativi con st.info(), st.success(), st.warning()."
    ])
    code = [
        "# Iniezione CSS per card metriche personalizzate",
        "st.markdown('''",
        "<style>",
        "    .main-metric-box {",
        "        background-color: #f8f9fa;",
        "        border-left: 5px solid #1E88E5;",
        "        padding: 12px;",
        "        border-radius: 6px;",
        "    }",
        "</style>",
        "''', unsafe_allow_html=True)"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Custom CSS Styling", code)
    add_notes(s, "Mostrare come piccoli dettagli di stile rendano la web app accattivante e pronta per la presentazione ai vertici aziendali.", 15, "Far notare l'uso prudente di unsafe_allow_html.", "Come possiamo allineare i colori dell'applicazione alla brand identity aziendale?")

    # 65. Laboratorio 6
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Laboratorio 6: Sviluppo della Web App Aziendale Completa", "MODULO 6: DASHBOARD STREAMLIT (4H)", 65)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🧪 Esercitazione Pratica Studenti", [
        "File starter: laboratori/lab06_dashboard_streamlit/app_starter.py",
        "Task 1: Configurare pagina e caching del dataset Parquet con @st.cache_data.",
        "Task 2: Creare la sidebar con i filtri per Filiale, Categoria e Date.",
        "Task 3: Implementare la barra superiore delle 5 card KPI.",
        "Task 4: Sviluppare le 4 schede orizzontali (Trend, Clienti, What-If, Dati ed Export CSV).",
        "Comando di test: streamlit run dashboard/app.py."
    ], bg_color=RGBColor(240, 249, 255), border_color=C_BLUE)
    code = [
        "--- VERIFICA FUNZIONALITÀ DASHBOARD ---",
        "🚀 Web Server avviato su http://localhost:8501",
        "✅ Caching Parquet attivo (caricamento < 20ms)",
        "✅ Filtri sidebar interattivi operativi",
        "✅ 5 KPI Cards dinamiche allineate",
        "✅ Grafici reattivi Matplotlib/Seaborn in Tab 1",
        "✅ Ranking clienti e torta settori in Tab 2",
        "✅ Simulatore What-If con slider real-time in Tab 3",
        "✅ Ricerca testuale e download CSV in Tab 4"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Checklist di Collaudo Dashboard", code)
    add_notes(s, "Sessione di laboratorio intensiva di 1 ora e mezza. Assistere gli studenti nella costruzione progressiva dei componenti.", 90, "Verificare che la dashboard si apra nel browser di tutti gli studenti.", "Tutti riescono a filtrare i dati per filiale e vedere i KPI aggiornarsi istantaneamente?")

    # 66. Recap Modulo 6
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Recap Modulo 6: Dalla Tabella Statica alla Web Intelligence", "MODULO 6: DASHBOARD STREAMLIT (4H)", 66)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🎯 Competenze Acquisite", [
        "Creazione di Web App responsive e interattive in puro Python.",
        "Ottimizzazione delle performance con caching in memoria RAM.",
        "Sviluppo di cruscotti decisionali con slider di simulazione scenario.",
        "Funzionalità di ricerca full-text e self-service download dati per gli utenti business."
    ], bg_color=RGBColor(236, 253, 245), border_color=C_GREEN, title_color=C_GREEN)
    create_card(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "🚀 Verso il Deploy Linux (Modulo 7)", [
        "La nostra applicazione funziona sul computer locale, ma se chiudiamo il portatile nessuno può più accedervi.",
        "Nel Modulo 7 vedremo come trasformarla in un servizio sempre attivo 24/7 su un server Linux aziendale.",
        "In modalità LIVE DEMO, configureremo il demone Systemd per l'avvio automatico al boot e il riavvio in caso di crash."
    ], bg_color=RGBColor(254, 243, 199), border_color=C_AMBER, title_color=C_AMBER)
    add_notes(s, "Tirare le somme del modulo applicativo più importante prima della sessione di deploy sistemistico.", 10, "Introdurre l'importanza della disponibilità continua del dato.", "Perché un'applicazione aziendale non può dipendere dal laptop di un singolo dipendente?")

def build_module_7(prs, blank_layout):
    """Modulo 7: Deploy su Server Linux & Produzione (Slide 67 - 70, 4 slide - Full Live Demo)"""
    # 67. Architettura Produzione
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Architettura di Produzione su Server Linux 24/7", "MODULO 7: DEPLOY SERVER LINUX (1H) - LIVE DEMO", 67)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🏢 Dal Laptop Locale al Server Aziendale", [
        "Obiettivo: Rendere la dashboard accessibile 24 ore su 24 a tutti i dipendenti aziendali.",
        "Ambiente server: Linux Ubuntu/Debian con Virtual Environment isolato.",
        "Architettura a 3 livelli:",
        " 1. Client Browser (Utente)",
        " 2. Nginx Reverse Proxy (Porta standard 80/443 con SSL)",
        " 3. Demone Systemd in background (Gestione del processo Streamlit)."
    ])
    img_dep = os.path.join(ASSETS_DIR, "diagramma_deploy_linux.png")
    if os.path.exists(img_dep):
        s.shapes.add_picture(img_dep, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2))
    add_notes(s, "Iniziare la sessione di Live Demo collegandosi in diretta SSH al server Linux.", 15, "Mostrare lo schema dei 3 livelli architetturali.", "Cosa accade a uno script lanciato da terminale quando si chiude la sessione SSH?")

    # 68. Systemd Unit File
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Configurazione del Demone Systemd: dashboard_vendite.service", "MODULO 7: DEPLOY SERVER LINUX (1H) - LIVE DEMO", 68)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "⚙️ Anatomia del File Unit di Sistema", [
        "Posizione standard: /etc/systemd/system/dashboard_vendite.service.",
        "Sezione [Unit]: Descrizione del servizio e dipendenze di rete (After=network.target).",
        "Sezione [Service]: Utente di esecuzione non-root, WorkingDirectory, comando ExecStart.",
        "Politica di resilienza: Restart=always e RestartSec=5 per riavviare l'app in caso di crash.",
        "Sezione [Install]: WantedBy=multi-user.target per l'avvio automatico al boot del server."
    ])
    code = [
        "# File: /etc/systemd/system/dashboard_vendite.service",
        "[Unit]",
        "Description=Dashboard Direzionale Vendite",
        "After=network.target",
        "",
        "[Service]",
        "Type=simple",
        "User=arny",
        "WorkingDirectory=/path/to/corso_python",
        "ExecStart=/path/to/.venv/bin/streamlit run dashboard/app.py \\",
        "          --server.port 8501 --server.headless true",
        "Restart=always",
        "RestartSec=5",
        "",
        "[Install]",
        "WantedBy=multi-user.target"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Unit File Systemd di Produzione", code)
    add_notes(s, "Mostrare la creazione del file .service a schermo e spiegarne ogni singola riga.", 15, "Evidenziare l'importanza di eseguire il servizio con utente non-root per sicurezza.", "Perché Restart=always è fondamentale in produzione?")

    # 69. Gestione systemctl
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Amministrazione del Servizio con systemctl e Script di Provisioning", "MODULO 7: DEPLOY SERVER LINUX (1H) - LIVE DEMO", 69)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🛠️ Comandi Operativi di Amministrazione", [
        "sudo systemctl daemon-reload: Ricarica le configurazioni di sistema.",
        "sudo systemctl enable dashboard_vendite: Abilita l'avvio automatico all'accensione del server.",
        "sudo systemctl start dashboard_vendite: Avvia il demone in background.",
        "sudo systemctl status dashboard_vendite: Ispezione in tempo reale dello stato (active / running).",
        "Script di automazione: laboratori/lab07_deploy_linux/setup_service.sh."
    ])
    code = [
        "$ sudo systemctl status dashboard_vendite.service",
        "● dashboard_vendite.service - Dashboard Direzionale Vendite",
        "   Loaded: loaded (/etc/systemd/system/dashboard_vendite.service)",
        "   Active: active (running) since Mon 2026-09-15 10:00:00 CEST",
        " Main PID: 42150 (streamlit)",
        "    Tasks: 8 (limit: 18880)",
        "   Memory: 142.5M",
        "      CPU: 1.250s",
        "   CGroup: /system.slice/dashboard_vendite.service",
        "           └─42150 /path/.venv/bin/python .../streamlit run"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Stato Attivo del Servizio su Linux", code)
    add_notes(s, "Eseguire i comandi systemctl in diretta terminale e mostrare lo stato 'active (running)' verde.", 15, "Simulare un riavvio con systemctl restart.", "Come verifichereste se il servizio si avvierà automaticamente al riavvio del server?")

    # 70. Log journalctl e Nginx
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Monitoraggio dei Log con journalctl & Cenni Nginx", "MODULO 7: DEPLOY SERVER LINUX (1H) - LIVE DEMO", 70)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🔍 Diagnostica e Sicurezza Perimetrale", [
        "sudo journalctl -u dashboard_vendite.service -f: Streaming continuo dei log in tempo reale.",
        "Ispezione errori e tracciamento delle connessioni degli utenti.",
        "Reverse Proxy Nginx: Espone l'app sulla porta web standard (80/443) senza mostrare la porta interna 8501.",
        "Firewall UFW: Chiusura delle porte interne e abilitazione del solo traffico web autorizzato."
    ])
    code = [
        "# Streaming log in tempo reale",
        "$ sudo journalctl -u dashboard_vendite.service -f -n 20",
        "10:00:01 [INFO] Uvicorn server started on 0.0.0.0:8501",
        "10:00:05 [INFO] Caching data: 3600 records loaded",
        "10:01:12 [INFO] User session started: IP 192.168.1.56",
        "",
        "# Configurazione Reverse Proxy Nginx:",
        "location / {",
        "    proxy_pass http://127.0.0.1:8501;",
        "    proxy_set_header Upgrade $http_upgrade;",
        "}"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Streaming Log con journalctl", code)
    add_notes(s, "Concludere la Live Demo simulando una connessione browser e mostrando le righe di log che compaiono in streaming nel terminale.", 15, "Mostrare la guida operativa completa in guida_deploy.md.", "Come fareste a diagnosticare un eventuale errore runtime avvenuto durante la notte?")

def build_module_pw(prs, blank_layout):
    """Project Work Finale & Chiusura (Slide 71 - 75, 5 slide)"""
    # 71. Scenario Napoli
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Project Work Finale: Acquisizione Filiale di Napoli (3H)", "PROJECT WORK FINALE & VALUTAZIONE (3H)", 71)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🏢 La Sfida Aziendale Conclusiva", [
        "Contesto: A fine anno l'azienda si espande nel Sud Italia aprendo la nuova sede di Napoli.",
        "Dataset di progetto: dataset/raw/napoli_project_work.xlsx (1.144 record grezzi).",
        "Missione: Lavorando in autonomia o a coppie, integrare Napoli nella pipeline nazionale per consolidare a 4 filiali.",
        "Rispondere ai quesiti strategici del CdA ed estendere le analisi di business."
    ])
    img_bench = os.path.join(GEN_DIR, "pw_confronto_filiali.png")
    if os.path.exists(img_bench):
        s.shapes.add_picture(img_bench, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2))
    add_notes(s, "Lanciare la sessione di esame / Project Work finale di 3 ore.", 15, "Presentare la traccia formale in project_work/traccia_studenti.md.", "Quali sono le particolarità che vi aspettate di trovare nel dataset della nuova filiale di Napoli?")

    # 72. Specifiche e Rubrica
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Specifiche Tecniche del Project Work & Rubrica di Valutazione", "PROJECT WORK FINALE & VALUTAZIONE (3H)", 72)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📋 Le 4 Fasi del Progetto", [
        "Fase 1 (25 pt): Data Wrangling su Napoli (deduplica, parsing date, imputazione).",
        "Fase 2 (25 pt): Consolidamento nazionale a 4 filiali in Parquet (4.700 record totali).",
        "Fase 3 (25 pt): Calcolo KPI di business (quota % Napoli, top categorie, canali più efficaci).",
        "Fase 4 (25 pt): Produzione dei 3 grafici di benchmark e aggiornamento dashboard."
    ])
    code = [
        "--- GRIGLIA DI VALUTAZIONE (100 PUNTI) ---",
        "• Data Wrangling & Pulizia Dati:     25 Punti",
        "• Integrazione & Consolidamento:      20 Punti",
        "• Accuratezza Calcoli e KPI:          20 Punti",
        "• Visualizzazione e Storytelling:     20 Punti",
        "• Qualità Codice e Struttura PEP 8:   15 Punti",
        "----------------------------------------------",
        "TOTALE:                              100 Punti",
        "Livello Eccellente: 90-100 Punti | Sufficienza: 60 Punti"
    ]
    create_code_block(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "Rubrica di Valutazione Ufficiale", code)
    add_notes(s, "Chiarire i criteri di valutazione e i deliverable attesi da ciascun gruppo.", 15, "Spiegare la rubrica presente in project_work/criteri_valutazione.md.", "Come verificherete che l'integrazione a 4 filiali non abbia duplicato record?")

    # 73. Sessione Operativa Guidata
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Sessione di Sviluppo Guidato e Supporto in Aula", "PROJECT WORK FINALE & VALUTAZIONE (3H)", 73)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "💻 Lavoro Pratico Autonomo (2 Ore)", [
        "Gli studenti lavorano attivamente sullo script del Project Work.",
        "Il docente effettua code review in tempo reale e fornisce suggerimenti di troubleshooting.",
        "Verifica intermedia dei totali contabili:",
        " • Totale record master a 4 filiali: esattamente 4.700 righe pulite.",
        " • Fatturato nazionale consolidato: oltre 16.4 Milioni di Euro.",
        "Salvataggio dei grafici di benchmark in formato PNG ad alta definizione."
    ])
    img_pw_trend = os.path.join(GEN_DIR, "pw_trend_mensile_4filiali.png")
    if os.path.exists(img_pw_trend):
        s.shapes.add_picture(img_pw_trend, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2))
    add_notes(s, "Sessione di sviluppo autonomo di 120 minuti. Il docente gira tra i gruppi per supportare il coding.", 120, "Verificare che tutti riescano ad agganciare correttamente il foglio Anagrafica_Clienti di Napoli.", "Qual è la quota di fatturato generata da Napoli rispetto al totale nazionale?")

    # 74. Analisi Risultati Benchmark
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Presentazione Risultati: Benchmark Nazionale a 4 Filiali", "PROJECT WORK FINALE & VALUTAZIONE (3H)", 74)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "📊 Risposte ai Quesiti di Business", [
        "1. Quote Nazionali:",
        " • Milano: € 5.385k (32.7%) | Roma: € 4.143k (25.1%)",
        " • Napoli: € 3.852k (23.4%) | Torino: € 3.098k (18.8%)",
        "2. Performance Napoli:",
        " • Categoria Top: Hardware (€ 2.233k) con 3.012 pezzi venduti.",
        " • Canale Top: Partner Commerciale (€ 1.118k, ticket medio € 3.855).",
        "3. La filiale di Napoli si attesta come 3° polo commerciale nazionale."
    ])
    img_pw_heat = os.path.join(GEN_DIR, "pw_heatmap_filiale_categoria.png")
    if os.path.exists(img_pw_heat):
        s.shapes.add_picture(img_pw_heat, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2))
    add_notes(s, "Conduzione della tavola rotonda di presentazione: far esporre i risultati a turno ai rappresentanti dei gruppi.", 30, "Confrontare i grafici prodotti dai vari team.", "Quale raccomandazione commerciale dareste al Direttore Vendite per la sede di Napoli?")

    # 75. Chiusura e Certificazione
    s = prs.slides.add_slide(blank_layout)
    add_header(s, "Soluzione Docente, Certificazione & Chiusura Corso", "PROJECT WORK FINALE & VALUTAZIONE (3H)", 75)
    create_card(s, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2), "🏆 Competenze Certificate Raggiunte", [
        "1. Python Operativo: Funzioni, calcolo KPI, normalizzazione dati.",
        "2. Pandas Mastery: Indicizzazione, filtri, calcoli vettoriali.",
        "3. Data Wrangling: Deduplica, date complesse, imputazione, merge.",
        "4. Visual Storytelling: Matplotlib, Seaborn, cruscotti 2x2 a 300 DPI.",
        "5. Pipeline Engineering: ETL automatico con Apache Parquet.",
        "6. Web Analytics: Dashboard interattiva Streamlit con simulatore What-If.",
        "7. DevOps Foundation: Deploy Linux con Systemd 24/7."
    ], bg_color=RGBColor(236, 253, 245), border_color=C_GREEN, title_color=C_GREEN)
    create_card(s, Inches(6.7), Inches(1.5), Inches(5.8), Inches(5.2), "🎓 Prossimi Passi & Materiali d'Aula", [
        "Tutto il materiale rimane a vostra disposizione sul repository GitHub:",
        "🔗 https://github.com/arnymore/python_analisi_dati_campobasso",
        "Soluzione ufficiale di riferimento: project_work/soluzione_project_work.py.",
        "Manuale di approfondimento: dispensa/indice_dispensa.md.",
        "Congratulazioni a tutti i partecipanti per l'eccellente lavoro svolto!"
    ], bg_color=RGBColor(254, 243, 199), border_color=C_AMBER, title_color=C_AMBER)
    add_notes(s, "Slide conclusiva del corso. Ringraziare l'aula, consegnare gli attestati e raccogliere i feedback finali.", 15, "Invitare gli studenti a usare il repository come cassetta degli attrezzi per il loro lavoro quotidiano.", "Qual è la prima procedura che automatizzerete con Python appena tornati in ufficio?")

if __name__ == "__main__":
    print("--- GENERAZIONE POWERPOINT DEFINITIVO DEL CORSO (75 SLIDE) ---")
    prs = init_presentation()
    build_all_slides(prs)
    prs.save(PPTX_OUT)
    print(f"✅ File PPTX generato con successo: {PPTX_OUT}")
    print(f"📊 Totale slide generate: {len(prs.slides)}")
