"""
=============================================================================
VERSIONE DOCENTE COMMENTATA: LABORATORIO 2 - PANDAS FONDAMENTI
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================

STRUTTURA DEI COMMENTI A 4 LIVELLI DIDATTICI:
- LIVELLO 1 [TECNICO]: Sintassi, metodi Pandas, indexing, gestione copie in memoria.
- LIVELLO 2 [BUSINESS]: Canali distributivi (B2B, Retail), marginalità, Top Deals.
- LIVELLO 3 [DOCENTE]: Regia didattica, trappole comuni (parentesi booleane, View vs Copy).
- LIVELLO 4 [COLLEGAMENTO DIDATTICO]: Ponti verso Data Wrangling (Mod 3) e Dashboard (Mod 6).
=============================================================================
"""

import os
import pandas as pd

# LIVELLO 1 [TECNICO]:
# Costruzione del percorso assoluto portabile indipendente dal sistema operativo ospitante (Linux/Windows/macOS).
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_ROMA = os.path.join(BASE_DIR, "dataset", "raw", "roma.xlsx")

# ---------------------------------------------------------------------------
# ESERCIZIO 2.1: Importazione ed Esplorazione Iniziale
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Chiedere all'aula: "Cosa succede se omettiamo il parametro sheet_name in un file Excel multi-foglio?"
# Mostrare come pd.read_excel carica di default il primo foglio, ma per sicurezza enterprise
# è fondamentale specificare esplicitamente sheet_name="Dati_Vendite".

print("=== ESERCIZIO 2.1: Caricamento ed Esplorazione ===")
# LIVELLO 1 [TECNICO]:
# Caricamento del dataset vendite da Excel in un DataFrame bidimensionale.
df_roma = pd.read_excel(FILE_ROMA, sheet_name="Dati_Vendite")

# LIVELLO 1 [TECNICO]:
# .shape restituisce la tupla (righe, colonne).
print(f"Dimensioni DataFrame (righe, colonne): {df_roma.shape}")

# LIVELLO 3 [DOCENTE]:
# Fermarsi sull'output di `.info()` e far notare i tipi di dato (dtypes):
# Identificare quali colonne sono numeriche (int64, float64) e quali sono testuali/miste (object).
print("\n--- Info Colonne e Dtypes ---")
df_roma.info()

print("\n--- Prime 5 Righe ---")
print(df_roma.head())

# LIVELLO 2 [BUSINESS]:
# `.describe()` fornisce una fotografia immediata della distribuzione statistica:
# Valori minimi, massimi, quartili e medie di prezzi e quantità per individuare possibili anomalie macroscopiche.
print("\n--- Statistiche Descrittive (Numeriche) ---")
print(df_roma.describe())


# ---------------------------------------------------------------------------
# ESERCIZIO 2.2: Selezione Colonne e Indicizzazione (.loc vs .iloc)
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Chiedere: "Qual è la differenza tra df['Colonna'] e df[['Colonna']]?"
# Spiegare che la singola parentesi restituisce una Series monodimensionale, mentre la doppia
# parentesi quadra restituisce un DataFrame bidimensionale.

print("\n=== ESERCIZIO 2.2: Selezione Colonne e .loc / .iloc ===")
colonne_focus = ["ID_Transazione", "Data_Vendita", "Ragione_Sociale", "Nome_Prodotto", "Fatturato_Lordo"]
df_focus = df_roma[colonne_focus]
print("Estratto colonne principali (prime 3):\n", df_focus.head(3))

# LIVELLO 1 [TECNICO]:
# `.iloc[start:stop, start:stop]` -> Indicizzazione puramente POSIZIONALE (interi 0-indexed).
# Notare che lo slicing 10:21 include le righe dall'indice 10 al 20 compreso (esclude il 21).
sub_iloc = df_roma.iloc[10:21, 0:4]
print("\nEstratto .iloc[10:21, 0:4]:\n", sub_iloc)

# LIVELLO 1 [TECNICO]:
# `.loc[label_start:label_stop, [nomi_colonne]]` -> Indicizzazione basata su ETICHETTE.
# Notare che .loc include sia l'etichetta iniziale che quella finale (0:10 include anche l'etichetta 10).
sub_loc = df_roma.loc[0:10, ["Ragione_Sociale", "Fatturato_Lordo"]]
print("\nEstratto .loc[0:10, ['Ragione_Sociale', 'Fatturato_Lordo']]:\n", sub_loc)


# ---------------------------------------------------------------------------
# ESERCIZIO 2.3: Filtri e Condizioni Booleane
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Trappola d'aula classica: gli studenti dimenticano le parentesi tonde tra le condizioni logiche.
# Ricordare: `(df['A'] > 5) & (df['B'] < 10)` è obbligatorio a causa della precedenza dell'operatore `&`.

print("\n=== ESERCIZIO 2.3: Filtri Booleani ===")

# LIVELLO 2 [BUSINESS]:
# Filtro 1: Canale distributivo E-commerce B2B (vendite digitali alle aziende).
filtro_ecommerce = df_roma[df_roma["Canale_Vendita"] == "E-commerce B2B"]
print(f"Ordini E-commerce B2B: {len(filtro_ecommerce)}")

# LIVELLO 2 [BUSINESS]:
# Filtro 2: Ordini di volume consistente (Quantita >= 10) in cui il commerciale ha concesso uno sconto.
filtro_qta_sconto = df_roma[(df_roma["Quantita"] >= 10) & (df_roma["Sconto_Perc"] > 0)]
print(f"Ordini con Quantità >= 10 e Sconto attivo: {len(filtro_qta_sconto)}")

# LIVELLO 2 [BUSINESS]:
# Filtro 3: Contratti ad alto valore economico (> 1500€) escludendo la cancelleria a basso margine.
filtro_alto_valore = df_roma[(df_roma["Categoria_Prodotto"] != "Cancelleria") & (df_roma["Fatturato_Lordo"] > 1500)]
print(f"Ordini Alto Valore (Non Cancelleria > 1500€): {len(filtro_alto_valore)}")


# ---------------------------------------------------------------------------
# ESERCIZIO 2.4: Creazione Colonne Calcolate e Ordinamento (Top 10 Deals)
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Spiegare perché usiamo `.copy()`: senza `.copy()`, operare su df_calc potrebbe sollevare
# il `SettingWithCopyWarning` se derivato da uno slice.

print("\n=== ESERCIZIO 2.4: Colonne Calcolate e Top 10 Deals ===")
df_calc = df_roma.copy()

# LIVELLO 1 [TECNICO]:
# Pulizia preventiva del testo: rimuove simboli di valuta '€' e converte la virgola europea in punto decimale.
# `pd.to_numeric(..., errors='coerce')` converte in float64 trasformando valori non validi in NaN.
df_calc["Prezzo_Pulito"] = (
    df_calc["Prezzo_Unitario"]
    .astype(str)
    .str.replace("€", "", regex=False)
    .str.replace(",", ".", regex=False)
    .str.strip()
)
df_calc["Prezzo_Pulito"] = pd.to_numeric(df_calc["Prezzo_Pulito"], errors="coerce")

# LIVELLO 1 [TECNICO] & LIVELLO 2 [BUSINESS]:
# Operazioni vettorializzate ad altissima velocità tra colonne:
# Totale Lordo = Quantita * Prezzo_Unitario
df_calc["Totale_Lordo_Calcolato"] = df_calc["Quantita"] * df_calc["Prezzo_Pulito"]
# Valore Sconto = Totale Lordo * (Sconto_Perc / 100)
df_calc["Valore_Sconto"] = df_calc["Totale_Lordo_Calcolato"] * (df_calc["Sconto_Perc"] / 100.0)
# Fatturato Netto = Totale Lordo - Valore Sconto (ricavo netto effettivo)
df_calc["Fatturato_Netto"] = df_calc["Totale_Lordo_Calcolato"] - df_calc["Valore_Sconto"]

# LIVELLO 4 [COLLEGAMENTO DIDATTICO]:
# L'estrazione della Top 10 con `.sort_values(ascending=False).head(10)` anticipa
# il grafico a barre orizzontali dei Top Clienti che realizzeremo nel Modulo 4 e nella dashboard del Modulo 6.
top_10_deals = df_calc.sort_values(by="Fatturato_Netto", ascending=False)[
    ["ID_Transazione", "Ragione_Sociale", "Nome_Prodotto", "Quantita", "Prezzo_Pulito", "Sconto_Perc", "Fatturato_Netto"]
].head(10)

print("\n--- TOP 10 TRANSAZIONI PER FATTURATO NETTO ---")
print(top_10_deals.to_string(index=False))
