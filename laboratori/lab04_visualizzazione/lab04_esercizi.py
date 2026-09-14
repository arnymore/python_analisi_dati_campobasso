"""
=============================================================================
LABORATORIO 4: VISUALIZZAZIONE DATI E REPORTING (3 Ore)
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================

OBIETTIVI:
1. Comprendere l'anatomia di un grafico con Matplotlib (Figure, Axes).
2. Realizzare grafici statistici moderni con Seaborn.
3. Rappresentare trend temporali (Line plot), confronti categorici (Bar plot) e distribuzioni (Boxplot/Scatter).
4. Creare una Heatmap di correlazione e co-occorrenza (Canale x Categoria).
5. Comporre una tavola multi-grafico (Executive Dashboard 2x2) ed esportarla in PDF/PNG ad alta risoluzione.

CASO AZIENDALE:
La direzione vuole un report visivo chiaro per il Consiglio di Amministrazione.
Dobbiamo trasformare i dati puliti delle vendite in grafici professionali ed auto-esplicativi.
=============================================================================
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FILE_ROMA = os.path.join(BASE_DIR, "dataset", "raw", "roma.xlsx")

# ---------------------------------------------------------------------------
# PREPARAZIONE DATI DI BASE
# ---------------------------------------------------------------------------
# Carica e applica la pulizia minima necessaria (drop duplicati e parsing date)
df = pd.read_excel(FILE_ROMA, sheet_name="Dati_Vendite").drop_duplicates()
df["Prezzo_Num"] = pd.to_numeric(df["Prezzo_Unitario"].astype(str).str.replace("€", "").str.replace(",", ".").str.strip(), errors="coerce")
df["Quantita"] = df["Quantita"].fillna(df["Quantita"].median())
df["Prezzo_Num"] = df["Prezzo_Num"].fillna(df["Prezzo_Num"].mean())
df["Fatturato_Netto"] = df["Quantita"] * df["Prezzo_Num"] * (1 - df["Sconto_Perc"] / 100.0)
df["Data_Vendita_dt"] = pd.to_datetime(df["Data_Vendita"], format="mixed", dayfirst=True, errors="coerce")
df["Mese"] = df["Data_Vendita_dt"].dt.month


# ---------------------------------------------------------------------------
# ESERCIZIO 4.1: Grafico a Barre Orizzontali - Top Clienti per Fatturato
# ---------------------------------------------------------------------------
# Consegna:
# 1. Raggruppa per `Ragione_Sociale` e calcola la somma del `Fatturato_Netto`.
# 2. Seleziona i primi 8 clienti.
# 3. Crea un grafico a barre orizzontali (`plt.barh` o `sns.barplot`) con etichette chiare e griglia.

# TODO: Scrivi il codice qui


# ---------------------------------------------------------------------------
# ESERCIZIO 4.2: Trend Mensile delle Vendite (Line Chart con Marker)
# ---------------------------------------------------------------------------
# Consegna:
# 1. Calcola il fatturato netto totale per ogni mese (1..12).
# 2. Crea un grafico a linee con marker sui punti, titolo esplicativo, etichette mesi (Gen..Dic)
#    e linea tratteggiata per la media mensile dell'anno.

# TODO: Scrivi il codice qui


# ---------------------------------------------------------------------------
# ESERCIZIO 4.3: Heatmap Matrice di Vendita (Canale vs Categoria)
# ---------------------------------------------------------------------------
# Consegna:
# 1. Crea una tabella pivot con `Canale_Vendita` sulle righe, `Categoria_Prodotto` sulle colonne
#    e la somma di `Fatturato_Netto` come valori.
# 2. Genera una Heatmap con `sns.heatmap` usando la palette `Blues` o `YlGnBu` e annotazioni formattate in K€.

# TODO: Scrivi il codice qui


# ---------------------------------------------------------------------------
# ESERCIZIO 4.4: Executive Dashboard 2x2 ed Esportazione
# ---------------------------------------------------------------------------
# Consegna:
# Crea una figura con griglia 2x2 (`plt.subplots(2, 2, figsize=(16, 10))`) contenente:
# - [0, 0]: Trend Mensile Fatturato (Linea)
# - [0, 1]: Fatturato per Categoria Prodotto (Barre verticali)
# - [1, 0]: Distribuzione Sconto vs Canale Vendita (Boxplot)
# - [1, 1]: Heatmap Canale x Categoria
# Salva la figura risultante in `dataset/output_pipeline/executive_report.png` a 300 DPI.

# TODO: Scrivi il codice qui


if __name__ == "__main__":
    print("Esegui il laboratorio 4!")
