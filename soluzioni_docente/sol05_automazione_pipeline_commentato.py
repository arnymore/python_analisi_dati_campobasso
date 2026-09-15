"""
=============================================================================
VERSIONE DOCENTE COMMENTATA: LABORATORIO 5 - PIPELINE ETL AUTOMATIZZATA
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================

STRUTTURA DEI COMMENTI A 4 LIVELLI DIDATTICI:
- LIVELLO 1 [TECNICO]: Scansione `glob`, filtri lock file, modularità ETL, Parquet, `logging`, `argparse`.
- LIVELLO 2 [BUSINESS]: Consolidamento vendite multi-filiale (Roma, Milano, Torino), reporting direzionale.
- LIVELLO 3 [DOCENTE]: Regia architetturale, transizione da notebook a script batch, gestione eccezioni.
- LIVELLO 4 [COLLEGAMENTO DIDATTICO]: Ponti verso la dashboard Streamlit (Mod 6) e il deploy server (Mod 7).
=============================================================================
"""

import os
import glob
import datetime
import logging
import argparse
import pandas as pd
import numpy as np

# LIVELLO 1 [TECNICO]:
# Configurazione standard del modulo logging: livello INFO, formato con timestamp e severity.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)

MESI_MAP = {
    "gen": "01", "feb": "02", "mar": "03", "apr": "04",
    "mag": "05", "giu": "06", "lug": "07", "ago": "08",
    "set": "09", "ott": "10", "nov": "11", "dic": "12"
}

# LIVELLO 1 [TECNICO]:
# Funzione pura di parsing data flessibile collaudata nel Modulo 3.
def parse_data_flessibile(val):
    if pd.isna(val):
        return pd.NaT
    s = str(val).strip()
    if s.isdigit():
        try:
            dt = datetime.date(1899, 12, 30) + datetime.timedelta(days=int(s))
            return pd.to_datetime(dt)
        except Exception:
            pass
    for m_nome, m_num in MESI_MAP.items():
        if m_nome in s.lower():
            parti = s.split("-")
            if len(parti) == 3:
                giorno = parti[0].zfill(2)
                anno = parti[2]
                s = f"{anno}-{m_num}-{giorno}"
                break
    try:
        return pd.to_datetime(s, format="mixed", dayfirst=True)
    except Exception:
        return pd.NaT

def normalizza_categoria(cat):
    if pd.isna(cat) or not str(cat).strip():
        return "Altro"
    c = str(cat).strip().lower()
    if "hard" in c or "hw" in c: return "Hardware"
    if "soft" in c or "sw" in c: return "Software"
    if "serv" in c: return "Servizi"
    if "canc" in c or "consum" in c: return "Cancelleria"
    return "Altro"


# ---------------------------------------------------------------------------
# FASE 1: EXTRACT (Estrazione e Ingestione Multi-File)
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Spiegare all'aula: "Cosa succede se un dipendente in ufficio sta modificando roma.xlsx?"
# Excel crea il lock temporaneo `~$roma.xlsx`. Senza il filtro `not startswith('~$')`, lo script fallirebbe!

def carica_dati_filiali(cartella_input):
    """Estrae i dati da tutti i file filiale standard (esclusi lock temporanei ed export)."""
    # LIVELLO 1 [TECNICO]:
    # Scansione tramite pattern matching con glob.
    pattern = os.path.join(cartella_input, "*.xlsx")
    files = glob.glob(pattern)
    
    # LIVELLO 1 [TECNICO] & LIVELLO 2 [BUSINESS]:
    # Filtro di esclusione: scarta file di lock `~$`, il file del Project Work (Napoli) e report già generati.
    files_filiali = [f for f in files if "project_work" not in f and "~$" not in f and "report" not in f]
    
    logging.info(f"Trovati {len(files_filiali)} file da processare: {[os.path.basename(f) for f in files_filiali]}")
    
    lista_df_vendite = []
    lista_df_anagrafica = []
    
    for f in files_filiali:
        try:
            df_v = pd.read_excel(f, sheet_name="Dati_Vendite")
            lista_df_vendite.append(df_v)
            df_a = pd.read_excel(f, sheet_name="Anagrafica_Clienti")
            lista_df_anagrafica.append(df_a)
            logging.info(f" -> Letto {os.path.basename(f)}: {len(df_v)} righe vendite, {len(df_a)} record clienti")
        except Exception as e:
            logging.error(f"Errore lettura file {f}: {e}")
            
    if not lista_df_vendite:
        raise FileNotFoundError("Nessun file valido trovato nella cartella specificata.")
        
    # LIVELLO 1 [TECNICO]:
    # Concatenazione verticale di tutti i DataFrame parziali delle filiali in un unico master grezzo.
    df_raw_master = pd.concat(lista_df_vendite, ignore_index=True)
    df_anag_master = pd.concat(lista_df_anagrafica, ignore_index=True).drop_duplicates(subset=["Codice_Cliente"])
    
    return df_raw_master, df_anag_master


# ---------------------------------------------------------------------------
# FASE 2: TRANSFORM (Data Cleaning, Imputazione, Feature Engineering e Merge)
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Mostrare come questa funzione incapsuli tutte le regole di business e trasformazione
# validate sperimentalmente nei laboratori precedenti (Modulo 2 e 3).

def trasforma_dataset(df_raw, df_anagrafica):
    """Applica la pipeline di data cleaning e data enrichment."""
    logging.info(f"Inizio trasformazione: {len(df_raw)} record iniziali.")
    
    # 1. Deduplicazione logica di business
    n_pre_dup = len(df_raw)
    df = df_raw.drop_duplicates(subset=["ID_Transazione", "Data_Vendita", "Codice_Cliente", "Nome_Prodotto"]).copy()
    logging.info(f"Rimossi {n_pre_dup - len(df)} duplicati. Record rimanenti: {len(df)}")
    
    # 2. Normalizzazione codici e testi
    df["Codice_Cliente"] = df["Codice_Cliente"].astype(str).str.strip().str.upper()
    df["Codice_Cliente"] = df["Codice_Cliente"].replace(["NAN", "NONE", ""], np.nan)
    df["Ragione_Sociale"] = df["Ragione_Sociale"].astype(str).str.strip()
    df["Ragione_Sociale"] = df["Ragione_Sociale"].replace(["nan", "None", ""], np.nan)
    df["Categoria_Prodotto"] = df["Categoria_Prodotto"].apply(normalizza_categoria)
    
    # 3. Parsing Date e creazione gerarchie temporali
    df["Data_Vendita"] = df["Data_Vendita"].apply(parse_data_flessibile)
    df["Data_Vendita"] = pd.to_datetime(df["Data_Vendita"])
    df["Anno"] = df["Data_Vendita"].dt.year
    df["Mese"] = df["Data_Vendita"].dt.month
    df["Mese_Nome"] = df["Data_Vendita"].dt.strftime("%B")
    df["Trimestre"] = df["Data_Vendita"].dt.to_period("Q").astype(str)
    
    # 4. Bonifica numerici e imputazione statistica
    df["Prezzo_Pulito"] = (
        df["Prezzo_Unitario"]
        .astype(str)
        .str.replace("€", "", regex=False)
        .str.replace(",", ".", regex=False)
        .str.strip()
    )
    df["Prezzo_Pulito"] = pd.to_numeric(df["Prezzo_Pulito"], errors="coerce")
    
    media_prezzi = df.groupby("Nome_Prodotto")["Prezzo_Pulito"].transform("mean")
    df["Prezzo_Unitario_Finale"] = df["Prezzo_Pulito"].fillna(media_prezzi).round(2)
    
    mediana_qta = df.groupby("Nome_Prodotto")["Quantita"].transform("median")
    df["Quantita_Finale"] = df["Quantita"].fillna(mediana_qta).fillna(1).astype(int)
    
    df["Sconto_Perc"] = df["Sconto_Perc"].fillna(0).astype(float)
    
    # LIVELLO 2 [BUSINESS]: Ricalcolo metriche economiche certificate
    df["Fatturato_Lordo"] = round(df["Quantita_Finale"] * df["Prezzo_Unitario_Finale"], 2)
    df["Valore_Sconto"] = round(df["Fatturato_Lordo"] * (df["Sconto_Perc"] / 100.0), 2)
    df["Fatturato_Netto"] = round(df["Fatturato_Lordo"] - df["Valore_Sconto"], 2)
    
    # 5. Join relazionale con Anagrafica Clienti (con validazione m:1)
    df_anag = df_anagrafica.copy()
    df_anag["Codice_Cliente"] = df_anag["Codice_Cliente"].astype(str).str.strip().str.upper()
    df_anag = df_anag.drop_duplicates(subset=["Codice_Cliente"]).copy()
    
    n_righe_prev = len(df)
    df_master = pd.merge(
        df,
        df_anag[["Codice_Cliente", "Settore", "Citta_Sede", "Rating_Affidabilita"]],
        on="Codice_Cliente",
        how="left",
        validate="many_to_one"
    )
    assert len(df_master) == n_righe_prev, f"ERRORE CRITICO: Moltiplicazione righe nel merge ETL ({len(df_master)} != {n_righe_prev})!"
    
    df_master["Settore"] = df_master["Settore"].fillna("Non Specificato")
    df_master["Citta_Sede"] = df_master["Citta_Sede"].fillna("Non Specificata")
    df_master["Rating_Affidabilita"] = df_master["Rating_Affidabilita"].fillna("N.D.")
    
    # Riordino finale e rinomina standard delle colonne
    colonne_finali = [
        "ID_Transazione", "Data_Vendita", "Anno", "Mese", "Mese_Nome", "Trimestre",
        "Filiale", "Codice_Cliente", "Ragione_Sociale", "Settore", "Citta_Sede", "Rating_Affidabilita",
        "Categoria_Prodotto", "Nome_Prodotto", "Quantita_Finale", "Prezzo_Unitario_Finale",
        "Sconto_Perc", "Fatturato_Lordo", "Valore_Sconto", "Fatturato_Netto", "Canale_Vendita", "Note"
    ]
    df_master = df_master[colonne_finali].rename(columns={
        "Quantita_Finale": "Quantita",
        "Prezzo_Unitario_Finale": "Prezzo_Unitario"
    })
    
    logging.info("Trasformazione e pulizia completata con successo.")
    return df_master


# ---------------------------------------------------------------------------
# FASE 3: LOAD (Storage Parquet ad Alte Prestazioni & Report Multi-Foglio)
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Evidenziare il doppio canale di output:
# 1. Canale Machine/Analytics: file Parquet compresso ad altissima efficienza per Streamlit.
# 2. Canale Human/Management: cartella di lavoro Excel multi-scheda per l'amministrazione.

def esporta_dataset(df_master, cartella_output):
    """Esporta in Parquet e genera un report Excel strutturato multi-scheda."""
    os.makedirs(cartella_output, exist_ok=True)
    
    # LIVELLO 1 [TECNICO] & LIVELLO 4 [COLLEGAMENTO DIDATTICO]:
    # Salvataggio nel formato colonnare Parquet (richiede PyArrow).
    # Questo file sarà la sorgente istantanea letta da Streamlit nel Modulo 6.
    parquet_path = os.path.join(cartella_output, "vendite_consolidate_italia.parquet")
    df_master.to_parquet(parquet_path, index=False)
    logging.info(f"Salvato Parquet ottimizzato: {parquet_path}")
    
    # LIVELLO 2 [BUSINESS]:
    # Creazione delle tabelle aggregate per la Direzione Commerciale e Finanziaria
    kpi_filiale = df_master.groupby("Filiale").agg(
        Fatturato_Totale=("Fatturato_Netto", "sum"),
        Quantita_Totale=("Quantita", "sum"),
        Numero_Ordini=("ID_Transazione", "count"),
        Sconto_Medio_Perc=("Sconto_Perc", "mean"),
        Fatturato_Medio_Ordine=("Fatturato_Netto", "mean")
    ).reset_index().sort_values(by="Fatturato_Totale", ascending=False)
    
    kpi_categoria = df_master.groupby("Categoria_Prodotto").agg(
        Fatturato_Totale=("Fatturato_Netto", "sum"),
        Quantita_Totale=("Quantita", "sum"),
        Numero_Ordini=("ID_Transazione", "count"),
        Sconto_Medio_Perc=("Sconto_Perc", "mean")
    ).reset_index().sort_values(by="Fatturato_Totale", ascending=False)
    
    kpi_settore = df_master.groupby("Settore").agg(
        Fatturato_Totale=("Fatturato_Netto", "sum"),
        Numero_Ordini=("ID_Transazione", "count"),
        Fatturato_Medio_Ordine=("Fatturato_Netto", "mean")
    ).reset_index().sort_values(by="Fatturato_Totale", ascending=False)
    
    # LIVELLO 1 [TECNICO]:
    # Scrittura multi-foglio tramite openpyxl context manager
    excel_path = os.path.join(cartella_output, "report_direzionale_consolidato.xlsx")
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        df_master.to_excel(writer, sheet_name="Dettaglio_Transazioni", index=False)
        kpi_filiale.to_excel(writer, sheet_name="Riepilogo_Filiali", index=False)
        kpi_categoria.to_excel(writer, sheet_name="Riepilogo_Categorie", index=False)
        kpi_settore.to_excel(writer, sheet_name="Riepilogo_Settori", index=False)
        
    logging.info(f"Salvato Report Excel Direzionale: {excel_path}")


# ---------------------------------------------------------------------------
# ORCHESTRATORE PIPELINE & INTERFACCIA CLI (argparse)
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Mostrare come la funzione orchestratrice colleghi in sequenza ordinata le tre fasi ETL:
# carica_dati -> trasforma_dataset -> esporta_dataset.

def run_pipeline(input_dir=None, output_dir=None):
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    inp = input_dir or os.path.join(base, "dataset", "raw")
    out = output_dir or os.path.join(base, "dataset", "generated")
    
    logging.info("==================================================")
    logging.info("       AVVIO PIPELINE ETL AZIENDALE               ")
    logging.info("==================================================")
    
    df_raw, df_anag = carica_dati_filiali(inp)
    df_clean = trasforma_dataset(df_raw, df_anag)
    esporta_dataset(df_clean, out)
    
    tot_fatturato = df_clean["Fatturato_Netto"].sum()
    logging.info(f"PIPELINE TERMINATA! Totale Record Master: {len(df_clean)} | Fatturato Consolidato: {tot_fatturato:,.2f} €")
    logging.info("==================================================")


# LIVELLO 1 [TECNICO] & LIVELLO 4 [COLLEGAMENTO DIDATTICO]:
# Interfaccia CLI con argparse: permette a cron job e script di automazione su server Linux (Modulo 7)
# di eseguire la pipeline specificando cartelle personalizzate da riga di comando.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pipeline ETL Vendite Aziendali TechStore")
    parser.add_argument("--input-dir", type=str, default=None, help="Cartella con i file Excel regionali")
    parser.add_argument("--output-dir", type=str, default=None, help="Cartella di destinazione output")
    args = parser.parse_args()
    
    run_pipeline(args.input_dir, args.output_dir)
