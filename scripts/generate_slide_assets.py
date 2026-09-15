"""
Script per la generazione di asset grafici ad alta risoluzione da includere nelle slide PPTX/PDF.
Crea diagrammi architetturali, visualizzazioni della dashboard Streamlit, workflow e schemi didattici.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "slides", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# Stile grafico coerente e pulito
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]
plt.rcParams["font.family"] = "sans-serif"

def crea_diagramma_architettura_corso():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    
    # Box stile flowchart
    def add_box(x, y, w, h, title, subtitle, color, text_color="white"):
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", 
                                      ec="#2b2b2b", fc=color, lw=1.5)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h*0.62, title, ha="center", va="center", 
                fontsize=11, fontweight="bold", color=text_color)
        ax.text(x + w/2, y + h*0.30, subtitle, ha="center", va="center", 
                fontsize=8.5, color=text_color)

    # Nodi
    add_box(0.5, 3.2, 2.5, 1.3, "1. Dati Grezzi (Excel)", "Roma, Milano, Torino\nDuplicati, Formati Misti", "#455A64")
    add_box(3.7, 3.2, 2.6, 1.3, "2. Wrangling & ETL", "Python + Pandas\nParsing, Deduplica, Merge", "#1976D2")
    add_box(7.0, 3.2, 2.5, 1.3, "3. Storage Parquet", "Compressione Snappy\nTipizzazione nativa", "#388E3C")
    
    add_box(2.0, 0.8, 2.8, 1.4, "4. Analytics & Seaborn", "Executive Report 2x2\nHeatmap, Trend, Outlier", "#7B1FA2")
    add_box(5.5, 0.8, 3.8, 1.4, "5. Web App Streamlit & Deploy", "Dashboard Reattiva + What-If\nDemone Systemd Linux su Server", "#E64A19")

    # Frecce di connessione
    arrow_kw = dict(arrowstyle="->", lw=2.2, color="#37474F", mutation_scale=15)
    ax.annotate("", xy=(3.6, 3.85), xytext=(3.1, 3.85), arrowprops=arrow_kw)
    ax.annotate("", xy=(6.9, 3.85), xytext=(6.4, 3.85), arrowprops=arrow_kw)
    ax.annotate("", xy=(3.4, 2.3), xytext=(7.8, 3.1), arrowprops=arrow_kw)
    ax.annotate("", xy=(5.4, 1.5), xytext=(4.9, 1.5), arrowprops=arrow_kw)

    plt.tight_layout()
    plt.savefig(os.path.join(ASSETS_DIR, "diagramma_architettura_corso.png"), bbox_inches="tight")
    plt.close()

def crea_mockup_dashboard_streamlit():
    """Genera una simulazione visiva realistica della Dashboard Streamlit con KPI e grafici."""
    fig = plt.figure(figsize=(12, 6.5), dpi=220)
    fig.patch.set_facecolor("#F8F9FA")
    
    # Layout con griglia
    gs = fig.add_gridspec(3, 3, height_ratios=[0.8, 2.2, 2.2], hspace=0.35, wspace=0.25)
    
    # Header e KPI
    ax_header = fig.add_subplot(gs[0, :])
    ax_header.axis("off")
    
    # 4 KPI Cards
    kpis = [
        ("💰 FATTURATO NETTO", "€ 12.615.973,71", "+14.2% vs budget", "#1E88E5"),
        ("📦 ORDINI TOTALI", "3.600", "4 filiali nazionali", "#43A047"),
        ("🧾 TICKET MEDIO", "€ 3.504,44", "+5.1% YoY", "#FB8C00"),
        ("🏷️ SCONTO MEDIO", "8.7%", "Target max 10%", "#8E24AA")
    ]
    
    for i, (title, val, delta, col) in enumerate(kpis):
        x = i * 0.25 + 0.01
        rect = patches.FancyBboxPatch((x, 0.05), 0.23, 0.85, boxstyle="round,pad=0.03",
                                      ec="#CFD8DC", fc="white", lw=1.2)
        ax_header.add_patch(rect)
        ax_header.text(x + 0.115, 0.68, title, ha="center", fontsize=8.5, fontweight="bold", color="#546E7A")
        ax_header.text(x + 0.115, 0.38, val, ha="center", fontsize=12, fontweight="bold", color="#263238")
        ax_header.text(x + 0.115, 0.16, delta, ha="center", fontsize=7.5, color=col, fontweight="semibold")

    # Grafico 1: Trend Mensile
    ax1 = fig.add_subplot(gs[1, :2])
    mesi = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", "Lug", "Ago", "Set", "Ott", "Nov", "Dic"]
    milano = np.array([420, 390, 460, 480, 510, 470, 430, 380, 490, 520, 540, 560])
    roma = np.array([320, 310, 350, 370, 390, 360, 330, 300, 380, 400, 410, 430])
    torino = np.array([240, 230, 260, 270, 280, 260, 240, 210, 270, 290, 300, 320])
    
    ax1.plot(mesi, milano, marker="o", color="#1E88E5", label="Milano", lw=2)
    ax1.plot(mesi, roma, marker="s", color="#43A047", label="Roma", lw=2)
    ax1.plot(mesi, torino, marker="^", color="#FB8C00", label="Torino", lw=2)
    ax1.set_title("Trend Mensile Fatturato Netto per Filiale (k€)", fontsize=10, fontweight="bold", pad=8)
    ax1.set_ylabel("Fatturato (k€)", fontsize=8.5)
    ax1.legend(loc="upper left", fontsize=8)
    ax1.tick_params(labelsize=8)

    # Grafico 2: Quota Categorie
    ax2 = fig.add_subplot(gs[1, 2])
    cat_labels = ["Hardware", "Software", "Servizi", "Cancelleria"]
    cat_vals = [55, 25, 15, 5]
    colors = ["#1976D2", "#388E3C", "#F57C00", "#7B1FA2"]
    ax2.pie(cat_vals, labels=cat_labels, autopct="%1.0f%%", startangle=140, colors=colors, textprops={'fontsize': 8})
    ax2.set_title("Fatturato per Categoria", fontsize=10, fontweight="bold")

    # Grafico 3: Simulatore What-If
    ax3 = fig.add_subplot(gs[2, :])
    ax3.axis("off")
    rect_whatif = patches.FancyBboxPatch((0.02, 0.05), 0.96, 0.88, boxstyle="round,pad=0.04",
                                         ec="#00897B", fc="#E0F2F1", lw=1.5)
    ax3.add_patch(rect_whatif)
    ax3.text(0.05, 0.72, "🔮 SIMULATORE DI SCENARIO COMMERCIALE (WHAT-IF ANALYSIS)", 
             fontsize=10, fontweight="bold", color="#004D40")
    ax3.text(0.05, 0.45, "Slider Volume Vendite: [+15%]  |  Slider Variazione Sconto: [-2.0%]", 
             fontsize=9, color="#00695C")
    ax3.text(0.05, 0.20, "Risultato Simulazione: Fatturato Previsto € 14.780.000,00 (+17.15% con Extra-Margine di € 2.164.026,29)", 
             fontsize=9.5, fontweight="bold", color="#004D40")

    plt.savefig(os.path.join(ASSETS_DIR, "mockup_dashboard_streamlit.png"), bbox_inches="tight")
    plt.close()

def crea_diagramma_deploy_linux():
    """Genera schema visivo dell'architettura di deploy Linux."""
    fig, ax = plt.subplots(figsize=(9, 4.2), dpi=200)
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 4)
    ax.axis("off")
    
    def add_node(x, y, w, h, t1, t2, col):
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", ec="#263238", fc=col, lw=1.3)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h*0.62, t1, ha="center", va="center", fontsize=9.5, fontweight="bold", color="white")
        ax.text(x + w/2, y + h*0.30, t2, ha="center", va="center", fontsize=8, color="white")

    add_node(0.4, 1.4, 2.2, 1.2, "1. Client Browser", "Utente Aziendale\nHTTP / HTTPS", "#455A64")
    add_node(3.4, 1.4, 2.4, 1.2, "2. Nginx Proxy", "Reverse Proxy (Port 80)\nSSL / Security Firewall", "#00897B")
    add_node(6.4, 1.4, 2.2, 1.2, "3. Systemd Demone", "Streamlit Server (8501)\nAuto-Restart on Crash", "#D81B60")

    arrow_kw = dict(arrowstyle="->", lw=2, color="#263238", mutation_scale=15)
    ax.annotate("", xy=(3.3, 2.0), xytext=(2.7, 2.0), arrowprops=arrow_kw)
    ax.annotate("", xy=(6.3, 2.0), xytext=(5.9, 2.0), arrowprops=arrow_kw)
    
    ax.text(4.5, 0.4, "⚙️ Gestione con systemctl (start/stop/status) e log con journalctl -f", 
            ha="center", fontsize=9, fontweight="bold", color="#37474F")

    plt.tight_layout()
    plt.savefig(os.path.join(ASSETS_DIR, "diagramma_deploy_linux.png"), bbox_inches="tight")
    plt.close()

def crea_diagramma_relazionale_merge():
    """Genera schema visivo della Left Join Vendite + Anagrafica Clienti."""
    fig, ax = plt.subplots(figsize=(9, 4), dpi=200)
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 4)
    ax.axis("off")
    
    # Tabella Vendite
    rect1 = patches.FancyBboxPatch((0.5, 0.6), 3.2, 2.8, boxstyle="round,pad=0.08", ec="#1565C0", fc="#E3F2FD", lw=1.5)
    ax.add_patch(rect1)
    ax.text(2.1, 3.1, "TABELLA DEI FATTI (Vendite)", ha="center", fontsize=9.5, fontweight="bold", color="#0D47A1")
    ax.text(0.7, 2.5, "• ID_Transazione (PK)", fontsize=8, color="#1565C0")
    ax.text(0.7, 2.1, "• Data_Vendita", fontsize=8, color="#1565C0")
    ax.text(0.7, 1.7, "• Codice_Cliente (FK)", fontsize=8, fontweight="bold", color="#B71C1C")
    ax.text(0.7, 1.3, "• Quantita, Prezzo, Sconto", fontsize=8, color="#1565C0")
    ax.text(0.7, 0.9, "• Fatturato_Netto", fontsize=8, color="#1565C0")
    
    # Tabella Clienti
    rect2 = patches.FancyBboxPatch((5.3, 0.6), 3.2, 2.8, boxstyle="round,pad=0.08", ec="#2E7D32", fc="#E8F5E9", lw=1.5)
    ax.add_patch(rect2)
    ax.text(6.9, 3.1, "DIMENSIONE (Anagrafica)", ha="center", fontsize=9.5, fontweight="bold", color="#1B5E20")
    ax.text(5.5, 2.5, "• Codice_Cliente (PK)", fontsize=8, fontweight="bold", color="#B71C1C")
    ax.text(5.5, 2.1, "• Ragione_Sociale_Ufficiale", fontsize=8, color="#2E7D32")
    ax.text(5.5, 1.7, "• Settore Merceologico", fontsize=8, color="#2E7D32")
    ax.text(5.5, 1.3, "• Citta_Sede", fontsize=8, color="#2E7D32")
    ax.text(5.5, 0.9, "• Rating_Affidabilita (A+, A)", fontsize=8, color="#2E7D32")

    # Freccia Merge
    ax.annotate("pd.merge(..., on='Codice_Cliente', how='left')", 
                xy=(5.2, 1.7), xytext=(3.8, 1.7),
                arrowprops=dict(arrowstyle="<->", lw=2, color="#B71C1C", mutation_scale=15),
                ha="center", va="bottom", fontsize=8, fontweight="bold", color="#B71C1C")

    plt.tight_layout()
    plt.savefig(os.path.join(ASSETS_DIR, "diagramma_relazionale_merge.png"), bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    print("--- GENERAZIONE ASSET GRAFICI PER LE SLIDE ---")
    crea_diagramma_architettura_corso()
    crea_mockup_dashboard_streamlit()
    crea_diagramma_deploy_linux()
    crea_diagramma_relazionale_merge()
    print("✅ Tutti gli asset grafici generati con successo in:", ASSETS_DIR)
