"""
=============================================================================
VERSIONE DOCENTE COMMENTATA: LABORATORIO 4 - VISUALIZZAZIONE & REPORTING
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================

STRUTTURA DEI COMMENTI A 4 LIVELLI DIDATTICI:
- LIVELLO 1 [TECNICO]: Matplotlib Object-Oriented (`fig, ax`), Seaborn, parametri grafici, 300 DPI.
- LIVELLO 2 [BUSINESS]: Indicatori di performance commerciale, trend temporale, politiche di sconto.
- LIVELLO 3 [DOCENTE]: Regia visiva, scelta dei grafici migliori, evitare sovrapposizioni e memory leak.
- LIVELLO 4 [COLLEGAMENTO DIDATTICO]: Ponti verso la dashboard Streamlit interattiva (Mod 6).
=============================================================================
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# LIVELLO 1 [TECNICO]:
# Configurazione globale dello stile grafico per uniformità visiva corporate.
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.size"] = 10

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_ROMA = os.path.join(BASE_DIR, "dataset", "raw", "roma.xlsx")
OUT_DIR = os.path.join(BASE_DIR, "dataset", "generated")
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# CARICAMENTO E PREPARAZIONE DATI
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Ricordare come la preparazione rapida dei dati sintetizzi i passi appresi nel Modulo 2 e 3.
df = pd.read_excel(FILE_ROMA, sheet_name="Dati_Vendite").drop_duplicates()
df["Prezzo_Num"] = pd.to_numeric(df["Prezzo_Unitario"].astype(str).str.replace("€", "").str.replace(",", ".").str.strip(), errors="coerce")
df["Quantita"] = df["Quantita"].fillna(df["Quantita"].median())
df["Prezzo_Num"] = df["Prezzo_Num"].fillna(df["Prezzo_Num"].mean())
df["Fatturato_Netto"] = df["Quantita"] * df["Prezzo_Num"] * (1 - df["Sconto_Perc"] / 100.0)

def pulisci_cat(c):
    if pd.isna(c): return "Altro"
    c = str(c).strip().lower()
    if "hard" in c or "hw" in c: return "Hardware"
    if "soft" in c or "sw" in c: return "Software"
    if "serv" in c: return "Servizi"
    if "canc" in c: return "Cancelleria"
    return "Altro"

df["Categoria"] = df["Categoria_Prodotto"].apply(pulisci_cat)
df["Data_dt"] = pd.to_datetime(df["Data_Vendita"], format="mixed", dayfirst=True, errors="coerce")
df["Mese"] = df["Data_dt"].dt.month
df["Mese_Label"] = df["Data_dt"].dt.strftime("%b")

# ---------------------------------------------------------------------------
# ESERCIZIO 4.1: Top 8 Clienti per Fatturato (Grafico a Barre Orizzontali)
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Chiedere: "Perché usiamo ax.barh() invece di ax.bar()?"
# Spiegare: i nomi delle aziende sono lunghi; le barre orizzontali permettono una lettura naturale
# da sinistra a destra senza dover inclinare o tagliare i testi sull'asse.

print("=== Generazione Grafico 4.1: Top Clienti ===")
# LIVELLO 2 [BUSINESS]:
# Identificazione dei "Key Accounts" (i clienti strategici che generano la quota di maggioranza del fatturato).
top_clienti = (
    df.dropna(subset=["Ragione_Sociale"])
    .groupby("Ragione_Sociale")["Fatturato_Netto"]
    .sum()
    .sort_values(ascending=True)
    .tail(8)
)

# LIVELLO 1 [TECNICO]:
# Istanziazione esplicita di Figure e Axes (Paradigma Object-Oriented).
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(top_clienti.index, top_clienti.values / 1000.0, color="#1f77b4", edgecolor="black", alpha=0.85)
ax.set_title("Top 8 Clienti per Fatturato Netto - Filiale Roma (2024)", fontsize=13, fontweight="bold", pad=12)
ax.set_xlabel("Fatturato Totale (Migliaia di €)", fontweight="bold")
ax.grid(axis="x", linestyle="--", alpha=0.7)

# LIVELLO 1 [TECNICO] & LIVELLO 3 [DOCENTE]:
# Aggiunta di data label numerici all'estremità di ogni barra per immediata leggibilità esecutiva.
for bar in bars:
    w = bar.get_width()
    ax.text(w + 2, bar.get_y() + bar.get_height()/2, f"{w:.1f} k€", va="center", fontsize=9, fontweight="bold")

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "ex4_1_top_clienti.png"), dpi=200)
# LIVELLO 1 [TECNICO]: Liberazione immediata della memoria RAM con plt.close().
plt.close()
print("Grafico 4.1 salvato!")


# ---------------------------------------------------------------------------
# ESERCIZIO 4.2: Trend Mensile delle Vendite con Linea di Benchmark
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Mostrare come una linea orizzontale di benchmark (ax.axhline) consenta di capire a colpo d'occhio
# quali mesi hanno performato sopra o sotto la media aziendale annua.

print("=== Generazione Grafico 4.2: Trend Mensile ===")
trend_mensile = df.groupby("Mese")["Fatturato_Netto"].sum() / 1000.0
mesi_nomi = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", "Lug", "Ago", "Set", "Ott", "Nov", "Dic"]
media_mensile = trend_mensile.mean()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(trend_mensile.index, trend_mensile.values, marker="o", linewidth=2.5, color="#2ca02c", label="Fatturato Mensile (k€)")
# LIVELLO 2 [BUSINESS]: Target/Media mensile come linea di riferimento strategica.
ax.axhline(media_mensile, color="red", linestyle="--", alpha=0.75, label=f"Media Mensile ({media_mensile:.1f} k€)")
ax.set_title("Andamento Mensile del Fatturato Netto (2024)", fontsize=13, fontweight="bold", pad=12)
ax.set_xticks(range(1, 13))
ax.set_xticklabels(mesi_nomi)
ax.set_ylabel("Fatturato (k€)", fontweight="bold")
ax.set_xlabel("Mese", fontweight="bold")
ax.legend(loc="upper left")
ax.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "ex4_2_trend_mensile.png"), dpi=200)
plt.close()
print("Grafico 4.2 salvato!")


# ---------------------------------------------------------------------------
# ESERCIZIO 4.3: Heatmap Matrice Canale vs Categoria
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Spiegare la funzione `pivot_table`: trasforma una tabella piatta in una matrice a due dimensioni
# (Canale sulle righe, Categoria sulle colonne) ideale per la visualizzazione tramite mappa termica (Heatmap).

print("=== Generazione Grafico 4.3: Heatmap Matrice ===")
pivot_matrice = df.pivot_table(index="Canale_Vendita", columns="Categoria", values="Fatturato_Netto", aggfunc="sum") / 1000.0

fig, ax = plt.subplots(figsize=(8, 5))
# LIVELLO 1 [TECNICO]:
# annot=True inserisce i valori numerici all'interno delle celle, fmt='.1f' formatta con 1 cifra decimale.
sns.heatmap(pivot_matrice, annot=True, fmt=".1f", cmap="YlGnBu", cbar_kws={'label': 'Fatturato (k€)'}, ax=ax)
ax.set_title("Matrice Fatturato Netto (k€): Canale vs Categoria", fontsize=12, fontweight="bold", pad=12)
ax.set_xlabel("Categoria Prodotto", fontweight="bold")
ax.set_ylabel("Canale Vendita", fontweight="bold")

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "ex4_3_heatmap_matrice.png"), dpi=200)
plt.close()
print("Grafico 4.3 salvato!")


# ---------------------------------------------------------------------------
# ESERCIZIO 4.4: Executive Dashboard 2x2 ed Export a 300 DPI
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Questo è l'apice del modulo di visualizzazione: comporre un layout 2x2 a 4 pannelli sinottici
# e salvare il file a 300 DPI per la direzione aziendale.

print("=== Generazione Grafico 4.4: Executive Dashboard 2x2 ===")
# LIVELLO 1 [TECNICO]:
# Creazione della griglia a 2 righe e 2 colonne: axes è un array NumPy 2x2 di oggetti Axes.
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("EXECUTIVE DASHBOARD VENDITE AZIENDALI - FILIALE ROMA 2024", fontsize=16, fontweight="bold", y=0.98)

# Panel [0, 0]: Trend Mensile
axes[0, 0].plot(trend_mensile.index, trend_mensile.values, marker="o", color="#2b5c8f", linewidth=2)
axes[0, 0].axhline(media_mensile, color="crimson", linestyle="--", label=f"Media: {media_mensile:.1f}k€")
axes[0, 0].set_xticks(range(1, 13))
axes[0, 0].set_xticklabels(mesi_nomi)
axes[0, 0].set_title("1. Andamento Temporale Fatturato (k€)", fontweight="bold")
axes[0, 0].set_ylabel("Migliaia di €")
axes[0, 0].legend()
axes[0, 0].grid(True, linestyle=":", alpha=0.6)

# Panel [0, 1]: Fatturato per Categoria
cat_fatt = (df.groupby("Categoria")["Fatturato_Netto"].sum() / 1000.0).sort_values(ascending=False)
bars = axes[0, 1].bar(cat_fatt.index, cat_fatt.values, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"], edgecolor="black", alpha=0.85)
axes[0, 1].set_title("2. Fatturato per Categoria Prodotto (k€)", fontweight="bold")
axes[0, 1].set_ylabel("Migliaia di €")
for b in bars:
    axes[0, 1].text(b.get_x() + b.get_width()/2, b.get_height() + 10, f"{b.get_height():.0f}k", ha="center", fontsize=8, fontweight="bold")

# Panel [1, 0]: Boxplot Distribuzione Sconti per Canale
# LIVELLO 2 [BUSINESS]:
# Verifica se la rete di vendita sta concedendo sconti eccessivi sul canale Direct rispetto all'E-commerce.
sns.boxplot(data=df, x="Canale_Vendita", y="Sconto_Perc", hue="Canale_Vendita", palette="Set2", legend=False, ax=axes[1, 0])
axes[1, 0].set_title("3. Distribuzione Sconti Percentuali per Canale", fontweight="bold")
axes[1, 0].set_xlabel("Canale di Vendita")
axes[1, 0].set_ylabel("Sconto Applicato (%)")
axes[1, 0].tick_params(axis='x', rotation=15)

# Panel [1, 1]: Heatmap Canale / Categoria
sns.heatmap(pivot_matrice, annot=True, fmt=".0f", cmap="Blues", ax=axes[1, 1], cbar=False)
axes[1, 1].set_title("4. Matrice Canale / Categoria (k€)", fontweight="bold")

# LIVELLO 1 [TECNICO] & LIVELLO 4 [COLLEGAMENTO DIDATTICO]:
# Salvataggio ad alta risoluzione (dpi=300). Questa struttura visiva sarà ripresa e resa
# completamente interattiva e filtrabile via web nella dashboard Streamlit del Modulo 6.
plt.tight_layout()
dashboard_path = os.path.join(OUT_DIR, "executive_report.png")
plt.savefig(dashboard_path, dpi=300)
plt.close()
print(f"Executive Dashboard salvata con successo in: {dashboard_path}")
