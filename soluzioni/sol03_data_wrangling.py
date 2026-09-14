"""
=============================================================================
SOLUZIONE UFFICIALE: LABORATORIO 3 - DATA WRANGLING & MERGE
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================
"""

import os
import datetime
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_ROMA = os.path.join(BASE_DIR, "dataset", "raw", "roma.xlsx")

# ---------------------------------------------------------------------------
# ESERCIZIO 3.1: Rimozione Duplicati
# ---------------------------------------------------------------------------
print("=== ESERCIZIO 3.1: Rimozione Duplicati ===")
df_raw = pd.read_excel(FILE_ROMA, sheet_name="Dati_Vendite")
n_init = len(df_raw)
n_dup = df_raw.duplicated().sum()
print(f"Righe totali iniziali: {n_init} | Duplicati esatti rilevati: {n_dup}")

df_clean = df_raw.drop_duplicates().copy()
print(f"Righe dopo rimozione duplicati: {len(df_clean)}")


# ---------------------------------------------------------------------------
# ESERCIZIO 3.2: Pulizia Stringhe e Normalizzazione Categorie
# ---------------------------------------------------------------------------
print("\n=== ESERCIZIO 3.2: Normalizzazione Categorie e Stringhe ===")

# Pulizia Codice e Ragione Sociale
df_clean["Codice_Cliente"] = df_clean["Codice_Cliente"].astype(str).str.strip().str.upper()
df_clean["Codice_Cliente"] = df_clean["Codice_Cliente"].replace("NAN", np.nan).replace("NONE", np.nan)

df_clean["Ragione_Sociale"] = df_clean["Ragione_Sociale"].astype(str).str.strip()
df_clean["Ragione_Sociale"] = df_clean["Ragione_Sociale"].replace("nan", np.nan).replace("None", np.nan)

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

df_clean["Categoria_Prodotto"] = df_clean["Categoria_Prodotto"].apply(normalizza_categoria)
print("Distribuzione categorie normalizzate:\n", df_clean["Categoria_Prodotto"].value_counts())


# ---------------------------------------------------------------------------
# ESERCIZIO 3.3: Parsing e Normalizzazione Date
# ---------------------------------------------------------------------------
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
    
    # Se numerico (seriale Excel)
    if s.isdigit():
        try:
            # Excel base date
            dt = datetime.date(1899, 12, 30) + datetime.timedelta(days=int(s))
            return pd.to_datetime(dt)
        except Exception:
            pass

    # Se formato con nome mese (es. 15-Mar-2024)
    for m_nome, m_num in MESI_MAP.items():
        if m_nome in s.lower():
            parti = s.split("-")
            if len(parti) == 3:
                giorno = parti[0].zfill(2)
                anno = parti[2]
                s = f"{anno}-{m_num}-{giorno}"
                break

    # Tentativi standard con pd.to_datetime
    try:
        return pd.to_datetime(s, format="mixed", dayfirst=True)
    except Exception:
        return pd.NaT

df_clean["Data_Vendita_dt"] = df_clean["Data_Vendita"].apply(parse_data_flessibile)
df_clean["Data_Vendita_dt"] = pd.to_datetime(df_clean["Data_Vendita_dt"])

df_clean["Anno"] = df_clean["Data_Vendita_dt"].dt.year
df_clean["Mese"] = df_clean["Data_Vendita_dt"].dt.month
df_clean["Mese_Nome"] = df_clean["Data_Vendita_dt"].dt.strftime("%B")
df_clean["Trimestre"] = df_clean["Data_Vendita_dt"].dt.to_period("Q").astype(str)

print("Controllo date parsate (non-nulli):", df_clean["Data_Vendita_dt"].notna().sum(), "/", len(df_clean))


# ---------------------------------------------------------------------------
# ESERCIZIO 3.4: Pulizia Prezzi, Quantità e Ricalcolo
# ---------------------------------------------------------------------------
print("\n=== ESERCIZIO 3.4: Imputazione e Ricalcolo Fatturato ===")

# Pulizia prezzo
df_clean["Prezzo_Unitario_Num"] = (
    df_clean["Prezzo_Unitario"]
    .astype(str)
    .str.replace("€", "", regex=False)
    .str.replace(",", ".", regex=False)
    .str.strip()
)
df_clean["Prezzo_Unitario_Num"] = pd.to_numeric(df_clean["Prezzo_Unitario_Num"], errors="coerce")

# Imputazione prezzo con media per prodotto
media_prezzo_prod = df_clean.groupby("Nome_Prodotto")["Prezzo_Unitario_Num"].transform("mean")
df_clean["Prezzo_Unitario_Num"] = df_clean["Prezzo_Unitario_Num"].fillna(media_prezzo_prod)

# Imputazione quantita con mediana per prodotto
mediana_qta_prod = df_clean.groupby("Nome_Prodotto")["Quantita"].transform("median")
df_clean["Quantita"] = df_clean["Quantita"].fillna(mediana_qta_prod).fillna(1).astype(int)

# Ricalcolo colonne economiche coerenti
df_clean["Fatturato_Lordo_Ricalcolato"] = round(df_clean["Quantita"] * df_clean["Prezzo_Unitario_Num"], 2)
df_clean["Sconto_Valore"] = round(df_clean["Fatturato_Lordo_Ricalcolato"] * (df_clean["Sconto_Perc"] / 100.0), 2)
df_clean["Fatturato_Netto"] = round(df_clean["Fatturato_Lordo_Ricalcolato"] - df_clean["Sconto_Valore"], 2)


# ---------------------------------------------------------------------------
# ESERCIZIO 3.5: Merge con Anagrafica Clienti e GroupBy
# ---------------------------------------------------------------------------
print("\n=== ESERCIZIO 3.5: Merge con Anagrafica e GroupBy ===")
df_anagrafica = pd.read_excel(FILE_ROMA, sheet_name="Anagrafica_Clienti")
df_anagrafica["Codice_Cliente"] = df_anagrafica["Codice_Cliente"].str.strip().str.upper()

df_merged = pd.merge(
    df_clean,
    df_anagrafica[["Codice_Cliente", "Settore", "Citta_Sede", "Rating_Affidabilita"]],
    on="Codice_Cliente",
    how="left"
)
df_merged["Settore"] = df_merged["Settore"].fillna("Non Specificato")

report_settore = df_merged.groupby("Settore").agg(
    Fatturato_Totale=("Fatturato_Netto", "sum"),
    Sconto_Medio_Perc=("Sconto_Perc", "mean"),
    Numero_Ordini=("ID_Transazione", "count"),
    Quantita_Totale=("Quantita", "sum")
).reset_index().sort_values(by="Fatturato_Totale", ascending=False)

print("\n--- PERFORMANCE COMMERCIALI PER SETTORE CLIENTE ---")
print(report_settore.to_string(index=False))
