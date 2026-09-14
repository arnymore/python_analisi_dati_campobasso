"""
=============================================================================
SOLUZIONE UFFICIALE: LABORATORIO 2 - PANDAS FONDAMENTI
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================
"""

import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_ROMA = os.path.join(BASE_DIR, "dataset", "raw", "roma.xlsx")

# ---------------------------------------------------------------------------
# ESERCIZIO 2.1: Importazione ed Esplorazione Iniziale
# ---------------------------------------------------------------------------
print("=== ESERCIZIO 2.1: Caricamento ed Esplorazione ===")
df_roma = pd.read_excel(FILE_ROMA, sheet_name="Dati_Vendite")

print(f"Dimensioni DataFrame (righe, colonne): {df_roma.shape}")
print("\n--- Info Colonne e Dtypes ---")
df_roma.info()

print("\n--- Prime 5 Righe ---")
print(df_roma.head())

print("\n--- Statistiche Descrittive (Numeriche) ---")
print(df_roma.describe())


# ---------------------------------------------------------------------------
# ESERCIZIO 2.2: Selezione Colonne e Indicizzazione
# ---------------------------------------------------------------------------
print("\n=== ESERCIZIO 2.2: Selezione Colonne e .loc / .iloc ===")
colonne_focus = ["ID_Transazione", "Data_Vendita", "Ragione_Sociale", "Nome_Prodotto", "Fatturato_Lordo"]
df_focus = df_roma[colonne_focus]
print("Estratto colonne principali (prime 3):\n", df_focus.head(3))

# Con .iloc: righe 10..20, prime 4 colonne
sub_iloc = df_roma.iloc[10:21, 0:4]
print("\nEstratto .iloc[10:21, 0:4]:\n", sub_iloc)

# Con .loc: righe 0..10, colonne specifiche
sub_loc = df_roma.loc[0:10, ["Ragione_Sociale", "Fatturato_Lordo"]]
print("\nEstratto .loc[0:10, ['Ragione_Sociale', 'Fatturato_Lordo']]:\n", sub_loc)


# ---------------------------------------------------------------------------
# ESERCIZIO 2.3: Filtri e Condizioni Booleane
# ---------------------------------------------------------------------------
print("\n=== ESERCIZIO 2.3: Filtri Booleani ===")

# 1. Canale E-commerce B2B
filtro_ecommerce = df_roma[df_roma["Canale_Vendita"] == "E-commerce B2B"]
print(f"Ordini E-commerce B2B: {len(filtro_ecommerce)}")

# 2. Quantita >= 10 e Sconto_Perc > 0
filtro_qta_sconto = df_roma[(df_roma["Quantita"] >= 10) & (df_roma["Sconto_Perc"] > 0)]
print(f"Ordini con Quantità >= 10 e Sconto attivo: {len(filtro_qta_sconto)}")

# 3. Categoria != Cancelleria e Fatturato_Lordo > 1500
filtro_alto_valore = df_roma[(df_roma["Categoria_Prodotto"] != "Cancelleria") & (df_roma["Fatturato_Lordo"] > 1500)]
print(f"Ordini Alto Valore (Non Cancelleria > 1500€): {len(filtro_alto_valore)}")


# ---------------------------------------------------------------------------
# ESERCIZIO 2.4: Creazione Colonne Calcolate e Ordinamento
# ---------------------------------------------------------------------------
print("\n=== ESERCIZIO 2.4: Colonne Calcolate e Top 10 Deals ===")
df_calc = df_roma.copy()

# Pulizia temporanea di Prezzo_Unitario se stringa con virgola/simboli
df_calc["Prezzo_Pulito"] = (
    df_calc["Prezzo_Unitario"]
    .astype(str)
    .str.replace("€", "", regex=False)
    .str.replace(",", ".", regex=False)
    .str.strip()
)
df_calc["Prezzo_Pulito"] = pd.to_numeric(df_calc["Prezzo_Pulito"], errors="coerce")

df_calc["Totale_Lordo_Calcolato"] = df_calc["Quantita"] * df_calc["Prezzo_Pulito"]
df_calc["Valore_Sconto"] = df_calc["Totale_Lordo_Calcolato"] * (df_calc["Sconto_Perc"] / 100.0)
df_calc["Fatturato_Netto"] = df_calc["Totale_Lordo_Calcolato"] - df_calc["Valore_Sconto"]

# Ordinamento decrescente
top_10_deals = df_calc.sort_values(by="Fatturato_Netto", ascending=False)[
    ["ID_Transazione", "Ragione_Sociale", "Nome_Prodotto", "Quantita", "Prezzo_Pulito", "Sconto_Perc", "Fatturato_Netto"]
].head(10)

print("\n--- TOP 10 TRANSAZIONI PER FATTURATO NETTO ---")
print(top_10_deals.to_string(index=False))
