"""
=============================================================================
SOLUZIONE UFFICIALE: LABORATORIO 4 - VISUALIZZAZIONE E REPORTING
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Configurazione stile globale
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
df = pd.read_excel(FILE_ROMA, sheet_name="Dati_Vendite").drop_duplicates()
df["Prezzo_Num"] = pd.to_numeric(df["Prezzo_Unitario"].astype(str).str.replace("€", "").str.replace(",", ".").str.strip(), errors="coerce")
df["Quantita"] = df["Quantita"].fillna(df["Quantita"].median())
df["Prezzo_Num"] = df["Prezzo_Num"].fillna(df["Prezzo_Num"].mean())
df["Fatturato_Netto"] = df["Quantita"] * df["Prezzo_Num"] * (1 - df["Sconto_Perc"] / 100.0)

# Categorie normalizzate
def pulisci_cat(c):
    if pd.isna(c): return "Altro"
    c = str(c).strip().lower()
    if "hard" in c or "hw" in c: return "Hardware"
    if "soft" in c or "sw" in c: return "Software"
    if "serv" in c: return "Servizi"
    if "canc" in c: return "Cancelleria"
    return "Altro"

df["Categoria"] = df["Categoria_Prodotto"].apply(pulisci_cat)

# Data parsing
df["Data_dt"] = pd.to_datetime(df["Data_Vendita"], format="mixed", dayfirst=True, errors="coerce")
df["Mese"] = df["Data_dt"].dt.month
df["Mese_Label"] = df["Data_dt"].dt.strftime("%b")

# ---------------------------------------------------------------------------
# ESERCIZIO 4.1: Top 8 Clienti per Fatturato
# ---------------------------------------------------------------------------
print("=== Generazione Grafico 4.1: Top Clienti ===")
top_clienti = (
    df.dropna(subset=["Ragione_Sociale"])
    .groupby("Ragione_Sociale")["Fatturato_Netto"]
    .sum()
    .sort_values(ascending=True)
    .tail(8)
)

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(top_clienti.index, top_clienti.values / 1000.0, color="#1f77b4", edgecolor="black", alpha=0.85)
ax.set_title("Top 8 Clienti per Fatturato Netto - Filiale Roma (2024)", fontsize=13, fontweight="bold", pad=12)
ax.set_xlabel("Fatturato Totale (Migliaia di €)", fontweight="bold")
ax.grid(axis="x", linestyle="--", alpha=0.7)

# Etichette valori sulle barre
for bar in bars:
    w = bar.get_width()
    ax.text(w + 2, bar.get_y() + bar.get_height()/2, f"{w:.1f} k€", va="center", fontsize=9, fontweight="bold")

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "ex4_1_top_clienti.png"), dpi=200)
plt.close()
print("Grafico 4.1 salvato!")


# ---------------------------------------------------------------------------
# ESERCIZIO 4.2: Trend Mensile delle Vendite
# ---------------------------------------------------------------------------
print("=== Generazione Grafico 4.2: Trend Mensile ===")
trend_mensile = df.groupby("Mese")["Fatturato_Netto"].sum() / 1000.0
mesi_nomi = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", "Lug", "Ago", "Set", "Ott", "Nov", "Dic"]
media_mensile = trend_mensile.mean()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(trend_mensile.index, trend_mensile.values, marker="o", linewidth=2.5, color="#2ca02c", label="Fatturato Mensile (k€)")
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
print("=== Generazione Grafico 4.3: Heatmap Matrice ===")
pivot_matrice = df.pivot_table(index="Canale_Vendita", columns="Categoria", values="Fatturato_Netto", aggfunc="sum") / 1000.0

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(pivot_matrice, annot=True, fmt=".1f", cmap="YlGnBu", cbar_kws={'label': 'Fatturato (k€)'}, ax=ax)
ax.set_title("Matrice Fatturato Netto (k€): Canale vs Categoria", fontsize=12, fontweight="bold", pad=12)
ax.set_xlabel("Categoria Prodotto", fontweight="bold")
ax.set_ylabel("Canale Vendita", fontweight="bold")

plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "ex4_3_heatmap_matrice.png"), dpi=200)
plt.close()
print("Grafico 4.3 salvato!")


# ---------------------------------------------------------------------------
# ESERCIZIO 4.4: Executive Dashboard 2x2
# ---------------------------------------------------------------------------
print("=== Generazione Grafico 4.4: Executive Dashboard 2x2 ===")
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("EXECUTIVE DASHBOARD VENDITE AZIENDALI - FILIALE ROMA 2024", fontsize=16, fontweight="bold", y=0.98)

# [0, 0]: Trend
axes[0, 0].plot(trend_mensile.index, trend_mensile.values, marker="o", color="#2b5c8f", linewidth=2)
axes[0, 0].axhline(media_mensile, color="crimson", linestyle="--", label=f"Media: {media_mensile:.1f}k€")
axes[0, 0].set_xticks(range(1, 13))
axes[0, 0].set_xticklabels(mesi_nomi)
axes[0, 0].set_title("1. Andamento Temporale Fatturato (k€)", fontweight="bold")
axes[0, 0].set_ylabel("Migliaia di €")
axes[0, 0].legend()
axes[0, 0].grid(True, linestyle=":", alpha=0.6)

# [0, 1]: Fatturato per Categoria
cat_fatt = (df.groupby("Categoria")["Fatturato_Netto"].sum() / 1000.0).sort_values(ascending=False)
bars = axes[0, 1].bar(cat_fatt.index, cat_fatt.values, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"], edgecolor="black", alpha=0.85)
axes[0, 1].set_title("2. Fatturato per Categoria Prodotto (k€)", fontweight="bold")
axes[0, 1].set_ylabel("Migliaia di €")
for b in bars:
    axes[0, 1].text(b.get_x() + b.get_width()/2, b.get_height() + 10, f"{b.get_height():.0f}k", ha="center", fontsize=8, fontweight="bold")

# [1, 0]: Boxplot Sconti per Canale
sns.boxplot(data=df, x="Canale_Vendita", y="Sconto_Perc", palette="Set2", ax=axes[1, 0])
axes[1, 0].set_title("3. Distribuzione Sconti Percentuali per Canale", fontweight="bold")
axes[1, 0].set_xlabel("Canale di Vendita")
axes[1, 0].set_ylabel("Sconto Applicato (%)")
axes[1, 0].tick_params(axis='x', rotation=15)

# [1, 1]: Heatmap
sns.heatmap(pivot_matrice, annot=True, fmt=".0f", cmap="Blues", ax=axes[1, 1], cbar=False)
axes[1, 1].set_title("4. Matrice Canale / Categoria (k€)", fontweight="bold")

plt.tight_layout()
dashboard_path = os.path.join(OUT_DIR, "executive_report.png")
plt.savefig(dashboard_path, dpi=300)
plt.close()
print(f"Executive Dashboard salvata con successo in: {dashboard_path}")
