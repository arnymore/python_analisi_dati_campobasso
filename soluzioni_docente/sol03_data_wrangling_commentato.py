"""
=============================================================================
VERSIONE DOCENTE COMMENTATA: LABORATORIO 3 - DATA WRANGLING & MERGE
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================

STRUTTURA DEI COMMENTI A 4 LIVELLI DIDATTICI:
- LIVELLO 1 [TECNICO]: Deduplicazione, missing values, normalizzazione date, merge relazionale.
- LIVELLO 2 [BUSINESS]: Integrità anagrafiche, settori merceologici, rating solvibilità.
- LIVELLO 3 [DOCENTE]: Regia d'aula, spiegazione esplosione cartesiana, controllo righe pre/post.
- LIVELLO 4 [COLLEGAMENTO DIDATTICO]: Ponti verso la pipeline ETL batch (Mod 5) e la visualizzazione (Mod 4).
=============================================================================
"""

import os
import datetime
import pandas as pd
import numpy as np

# LIVELLO 1 [TECNICO]:
# Definizione percorsi assoluti
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_ROMA = os.path.join(BASE_DIR, "dataset", "raw", "roma.xlsx")

# ---------------------------------------------------------------------------
# ESERCIZIO 3.1: Rimozione Duplicati
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Chiedere: "Come possiamo quantificare quanti record duplicati sono presenti prima di cancellarli?"
# Spiegare che `df.duplicated().sum()` calcola il conteggio dei booleani True.

print("=== ESERCIZIO 3.1: Rimozione Duplicati ===")
df_raw = pd.read_excel(FILE_ROMA, sheet_name="Dati_Vendite")
n_init = len(df_raw)
n_dup = df_raw.duplicated().sum()
print(f"Righe totali iniziali: {n_init} | Duplicati esatti rilevati: {n_dup}")

# LIVELLO 1 [TECNICO] & LIVELLO 2 [BUSINESS]:
# `drop_duplicates().copy()` rimuove i duplicati identici generati da doppi export contabili.
# L'uso di `.copy()` crea una nuova allocazione di memoria garantendo integrità per i passi successivi.
df_clean = df_raw.drop_duplicates().copy()
print(f"Righe dopo rimozione duplicati: {len(df_clean)}")


# ---------------------------------------------------------------------------
# ESERCIZIO 3.2: Pulizia Stringhe e Normalizzazione Categorie
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Mostrare il valore sporco di alcune categorie (es. 'hw', 'Hardware ', 'SOFT').
# Spiegare perché è indispensabile raggrupparle in categorie canoniche pulite.

print("\n=== ESERCIZIO 3.2: Normalizzazione Categorie e Stringhe ===")

# LIVELLO 1 [TECNICO]:
# Normalizzazione e standardizzazione in maiuscolo dei codici identificativi cliente.
# Sostituzione di stringhe anomale 'NAN' o 'NONE' con l'oggetto NaN nativo di NumPy.
df_clean["Codice_Cliente"] = df_clean["Codice_Cliente"].astype(str).str.strip().str.upper()
df_clean["Codice_Cliente"] = df_clean["Codice_Cliente"].replace(["NAN", "NONE", ""], np.nan)

df_clean["Ragione_Sociale"] = df_clean["Ragione_Sociale"].astype(str).str.strip()
df_clean["Ragione_Sociale"] = df_clean["Ragione_Sociale"].replace(["nan", "None", ""], np.nan)

# LIVELLO 1 [TECNICO] & LIVELLO 2 [BUSINESS]:
# Funzione di mapping a regole di business per categorizzare i prodotti a listino.
def normalizza_categoria(cat):
    if pd.isna(cat) or not str(cat).strip():
        return "Altro"
    c = str(cat).strip().lower()
    if "hard" in c or "hw" in c:
        return "Hardware"
    elif "soft" in c or "sw" in c:
        return "Software"
    elif "serv" in c:
        return "Servizi"
    elif "canc" in c or "consum" in c:
        return "Cancelleria"
    return "Altro"

# LIVELLO 1 [TECNICO]:
# Applicazione funzionale riga per riga con `.apply()`.
df_clean["Categoria_Prodotto"] = df_clean["Categoria_Prodotto"].apply(normalizza_categoria)
print("Distribuzione categorie normalizzate:\n", df_clean["Categoria_Prodotto"].value_counts())


# ---------------------------------------------------------------------------
# ESERCIZIO 3.3: Parsing e Normalizzazione Date Disomogenee
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Questo è uno dei passaggi più critici in azienda.
# Spiegare le 3 casistiche gestite:
# 1. Numeri seriali interi di Excel (es. 45367).
# 2. Stringhe con nome del mese in italiano (es. '15-Mar-2024').
# 3. Stringhe standard ISO o europee con fallback robusto.

print("\n=== ESERCIZIO 3.3: Parsing Date Eterogenee ===")

MESI_MAP = {
    "gen": "01", "feb": "02", "mar": "03", "apr": "04",
    "mag": "05", "giu": "06", "lug": "07", "ago": "08",
    "set": "09", "ott": "10", "nov": "11", "dic": "12"
}

def parse_data_flessibile(val):
    if pd.isna(val):
        return pd.NaT
    s = str(val).strip()
    
    # LIVELLO 1 [TECNICO]:
    # Caso 1: Seriali Excel (giorni trascorsi dal 30/12/1899).
    if s.isdigit():
        try:
            dt = datetime.date(1899, 12, 30) + datetime.timedelta(days=int(s))
            return pd.to_datetime(dt)
        except Exception:
            pass

    # LIVELLO 1 [TECNICO]:
    # Caso 2: Formati con abbreviazioni di mesi in italiano.
    for m_nome, m_num in MESI_MAP.items():
        if m_nome in s.lower():
            parti = s.split("-")
            if len(parti) == 3:
                giorno = parti[0].zfill(2)
                anno = parti[2]
                s = f"{anno}-{m_num}-{giorno}"
                break

    # LIVELLO 1 [TECNICO]:
    # Caso 3: Parsing automatico Pandas con formati misti e dayfirst=True per lo standard europeo.
    try:
        return pd.to_datetime(s, format="mixed", dayfirst=True)
    except Exception:
        return pd.NaT

df_clean["Data_Vendita_dt"] = df_clean["Data_Vendita"].apply(parse_data_flessibile)
df_clean["Data_Vendita_dt"] = pd.to_datetime(df_clean["Data_Vendita_dt"])

# LIVELLO 4 [COLLEGAMENTO DIDATTICO]:
# L'estrazione delle componenti temporali (.dt.year, .dt.month, .dt.to_period('Q'))
# fornirà le dimensioni di aggregazione per l'analisi dei trend mensili e trimestrali
# nei grafici del Modulo 4 e nei filtri temporali di Streamlit (Modulo 6).
df_clean["Anno"] = df_clean["Data_Vendita_dt"].dt.year
df_clean["Mese"] = df_clean["Data_Vendita_dt"].dt.month
df_clean["Mese_Nome"] = df_clean["Data_Vendita_dt"].dt.strftime("%B")
df_clean["Trimestre"] = df_clean["Data_Vendita_dt"].dt.to_period("Q").astype(str)

print("Controllo date parsate (non-nulli):", df_clean["Data_Vendita_dt"].notna().sum(), "/", len(df_clean))


# ---------------------------------------------------------------------------
# ESERCIZIO 3.4: Pulizia Prezzi, Quantità e Ricalcolo Economico
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Chiedere all'aula: "Perché usiamo transform('mean') anziché una semplice media globale?"
# Spiegare: l'imputazione contestuale per prodotto assegna a un 'Server' il prezzo medio dei server,
# e a un 'Mouse' il prezzo medio dei mouse, evitando distorsioni macroscopiche.

print("\n=== ESERCIZIO 3.4: Imputazione e Ricalcolo Fatturato ===")

# LIVELLO 1 [TECNICO]:
# Conversione prezzo da stringa a float pulito
df_clean["Prezzo_Unitario_Num"] = (
    df_clean["Prezzo_Unitario"]
    .astype(str)
    .str.replace("€", "", regex=False)
    .str.replace(",", ".", regex=False)
    .str.strip()
)
df_clean["Prezzo_Unitario_Num"] = pd.to_numeric(df_clean["Prezzo_Unitario_Num"], errors="coerce")

# LIVELLO 1 [TECNICO]:
# Imputazione avanzata: calcola la media raggruppata per singolo prodotto e propaga il valore sulle righe NaN.
media_prezzo_prod = df_clean.groupby("Nome_Prodotto")["Prezzo_Unitario_Num"].transform("mean")
df_clean["Prezzo_Unitario_Num"] = df_clean["Prezzo_Unitario_Num"].fillna(media_prezzo_prod)

# Imputazione quantità mancanti con la mediana di quel prodotto (o 1 se non calcolabile)
mediana_qta_prod = df_clean.groupby("Nome_Prodotto")["Quantita"].transform("median")
df_clean["Quantita"] = df_clean["Quantita"].fillna(mediana_qta_prod).fillna(1).astype(int)

# LIVELLO 2 [BUSINESS]:
# Ricalcolo contabile certificato delle grandezze economiche:
df_clean["Fatturato_Lordo_Ricalcolato"] = round(df_clean["Quantita"] * df_clean["Prezzo_Unitario_Num"], 2)
df_clean["Sconto_Valore"] = round(df_clean["Fatturato_Lordo_Ricalcolato"] * (df_clean["Sconto_Perc"] / 100.0), 2)
df_clean["Fatturato_Netto"] = round(df_clean["Fatturato_Lordo_Ricalcolato"] - df_clean["Sconto_Valore"], 2)


# ---------------------------------------------------------------------------
# ESERCIZIO 3.5: Merge con Anagrafica Clienti e GroupBy Settoriale
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Eseguire il merge e spiegare la cardinalità: le transazioni sono 'Many' (N), i clienti in anagrafica sono 'One' (1).
# Mostrare come arricchire il dataset con Settore merceologico e Rating di affidabilità creditizia.

print("\n=== ESERCIZIO 3.5: Merge con Anagrafica e GroupBy ===")
df_anagrafica = pd.read_excel(FILE_ROMA, sheet_name="Anagrafica_Clienti")
df_anagrafica["Codice_Cliente"] = df_anagrafica["Codice_Cliente"].astype(str).str.strip().str.upper()

# LIVELLO 1 [TECNICO] & LIVELLO 2 [BUSINESS]:
# Left Join tra le transazioni (tabella primaria) e l'anagrafica clienti (tabella lookup dimensionale).
df_merged = pd.merge(
    df_clean,
    df_anagrafica[["Codice_Cliente", "Settore", "Citta_Sede", "Rating_Affidabilita"]],
    on="Codice_Cliente",
    how="left"
)
df_merged["Settore"] = df_merged["Settore"].fillna("Non Specificato")

# LIVELLO 4 [COLLEGAMENTO DIDATTICO]:
# L'aggregazione multi-metrica `.agg(...)` produce la tabella di sintesi che alimenterà
# i grafici a torta e i riepiloghi direzionali del Modulo 4 e 5.
report_settore = df_merged.groupby("Settore").agg(
    Fatturato_Totale=("Fatturato_Netto", "sum"),
    Sconto_Medio_Perc=("Sconto_Perc", "mean"),
    Numero_Ordini=("ID_Transazione", "count"),
    Quantita_Totale=("Quantita", "sum")
).reset_index().sort_values(by="Fatturato_Totale", ascending=False)

print("\n--- PERFORMANCE COMMERCIALI PER SETTORE CLIENTE ---")
print(report_settore.to_string(index=False))
