#!/usr/bin/env python3
"""
Script di Generazione Dataset Ufficiali del Corso:
"Laboratorio Python + Analisi Dati" - Docente: Arnaldo Morena

Genera:
- dataset/raw/roma.xlsx
- dataset/raw/milano.xlsx
- dataset/raw/torino.xlsx
- dataset/raw/napoli_project_work.xlsx

Contiene 'dirty data' realistici (duplicati, valori nulli, date non standard, errori di digitazione)
per consentire le esercitazioni di Data Wrangling, Pipeline ed Elaborazione.
"""

import os
import random
import datetime
import pandas as pd
import numpy as np

# Impostazione seed per riproducibilità
random.seed(42)
np.random.seed(42)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, "dataset", "raw")
os.makedirs(RAW_DIR, exist_ok=True)

CLIENTI_BASE = [
    ("CLI-1001", "Tech Solutions Srl"),
    ("CLI-1002", "Studio Rossi & Associati"),
    ("CLI-1003", "Logistica Molise SpA"),
    ("CLI-1004", "Manifattura Adriatica"),
    ("CLI-1005", "Boutique del Caffè"),
    ("CLI-1006", "Farmacia Centrale snc"),
    ("CLI-1007", "Consulenze Digitali"),
    ("CLI-1008", "Edilizia Campobasso"),
    ("CLI-1009", "Hotel Samnium"),
    ("CLI-1010", "Autofficina Moderna"),
    ("CLI-1011", "Centro Medico Ippocrate"),
    ("CLI-1012", "Libreria Dante"),
]

PRODOTTI_BASE = [
    ("Hardware", "Server Rack 24U", 1850.00),
    ("Hardware", "Laptop Business 15\"", 850.00),
    ("Hardware", "Monitor 27 4K", 280.00),
    ("Hardware", "Docking Station USB-C", 110.00),
    ("Software", "Licenza ERP Annuale", 1200.00),
    ("Software", "Licenza Antivirus 5U", 150.00),
    ("Software", "Abbonamento Cloud Backup", 350.00),
    ("Servizi", "Consulenza Sistemistica (h)", 75.00),
    ("Servizi", "Sviluppo Script Python (h)", 85.00),
    ("Servizi", "Formazione On-site (gg)", 450.00),
    ("Cancelleria", "Kit Carta e Toner", 65.00),
    ("Cancelleria", "Accessori Ergonomici", 45.00),
]

CANALI = ["Agente Diretto", "E-commerce B2B", "Email/Telefono", "Partner Commerciale"]

CATEGORIA_TYPOS = {
    "Hardware": ["Hardware", "hardware", "HARDWARE", "Hardware ", " Hardwre", "HW"],
    "Software": ["Software", "software", "SOFTWARE", "Software  ", "Softwre", "SW"],
    "Servizi": ["Servizi", "servizi", "SERVIZI", "Servizi IT", "Servizi-IT", "Serv.", "Servizi "],
    "Cancelleria": ["Cancelleria", "cancelleria", "CANCELLERIA", "Cancelleria  ", "Canc.", "Consumabili"]
}

def genera_data_sporca(dt_obj, stile):
    if stile == "iso":
        return dt_obj.strftime("%Y-%m-%d")
    elif stile == "it_slash":
        return dt_obj.strftime("%d/%m/%Y")
    elif stile == "us_slash":
        return dt_obj.strftime("%m/%d/%Y")
    elif stile == "text":
        mesi = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", "Lug", "Ago", "Set", "Ott", "Nov", "Dic"]
        return f"{dt_obj.day}-{mesi[dt_obj.month-1]}-{dt_obj.year}"
    elif stile == "serial":
        delta = dt_obj - datetime.date(1899, 12, 30)
        return str(delta.days)
    else:
        return dt_obj.strftime("%Y-%m-%d %H:%M:%S")

def genera_dataset_filiale(nome_filiale, n_righe, file_path):
    records = []
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    date_range_days = (end_date - start_date).days

    prefix = nome_filiale[:2].upper()

    for i in range(1, n_righe + 1):
        tx_id = f"{prefix}-{20240000 + i}"
        dt = start_date + datetime.timedelta(days=random.randint(0, date_range_days))
        
        data_style_rnd = random.random()
        if data_style_rnd < 0.50:
            data_str = dt.strftime("%Y-%m-%d")
        elif data_style_rnd < 0.80:
            data_str = dt.strftime("%d/%m/%Y")
        elif data_style_rnd < 0.90:
            data_str = dt.strftime("%m/%d/%Y")
        elif data_style_rnd < 0.95:
            data_str = genera_data_sporca(dt, "text")
        else:
            data_str = genera_data_sporca(dt, "serial")

        cli_code, cli_nome = random.choice(CLIENTI_BASE)
        cli_rnd = random.random()
        if cli_rnd < 0.04:
            cli_nome_mod = None
            cli_code_mod = None
        elif cli_rnd < 0.12:
            cli_nome_mod = f"  {cli_nome}  "
            cli_code_mod = cli_code
        elif cli_rnd < 0.18:
            cli_nome_mod = cli_nome.lower()
            cli_code_mod = cli_code.lower()
        else:
            cli_nome_mod = cli_nome
            cli_code_mod = cli_code

        cat_real, prod_nome, prezzo_base = random.choice(PRODOTTI_BASE)
        cat_mod = random.choice(CATEGORIA_TYPOS[cat_real])
        if random.random() < 0.03:
            cat_mod = None

        qta = random.randint(1, 15) if random.random() > 0.04 else None
        
        prezzo_var = round(prezzo_base * random.uniform(0.9, 1.15), 2)
        if random.random() < 0.04:
            prezzo_val = None
        elif random.random() < 0.10:
            prezzo_val = f"{str(prezzo_var).replace('.', ',')} €"
        else:
            prezzo_val = prezzo_var

        sconto_pct = random.choice([0, 0, 5, 10, 15, 20])
        canale = random.choice(CANALI)
        
        if qta is not None and isinstance(prezzo_val, (int, float)):
            fatturato_calcolato = round(qta * prezzo_val * (1 - sconto_pct/100.0), 2)
        else:
            fatturato_calcolato = None
            
        note_possibili = [
            "Consegna standard", "Ordine urgente", "Installazione inclusa",
            "Fattura anticipata", "Sconto approvato da Resp. Vendite", "", None
        ]
        note = random.choice(note_possibili)

        records.append({
            "ID_Transazione": tx_id,
            "Data_Vendita": data_str,
            "Codice_Cliente": cli_code_mod,
            "Ragione_Sociale": cli_nome_mod,
            "Filiale": nome_filiale,
            "Categoria_Prodotto": cat_mod,
            "Nome_Prodotto": prod_nome,
            "Quantita": qta,
            "Prezzo_Unitario": prezzo_val,
            "Sconto_Perc": sconto_pct,
            "Fatturato_Lordo": fatturato_calcolato,
            "Canale_Vendita": canale,
            "Note": note
        })

    n_duplicati = int(n_righe * 0.04)
    for _ in range(n_duplicati):
        idx_to_dup = random.randint(0, len(records) - 1)
        dup_record = records[idx_to_dup].copy()
        records.append(dup_record)

    df = pd.DataFrame(records)
    df = df.sample(frac=1.0, random_state=42).reset_index(drop=True)

    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Dati_Vendite", index=False)
        
        df_clienti_anag = pd.DataFrame([
            {"Codice_Cliente": c[0], "Ragione_Sociale_Ufficiale": c[1], "Settore": s, "Citta_Sede": cit, "Rating_Affidabilita": rat}
            for c, s, cit, rat in [
                (CLIENTI_BASE[0], "Information Technology", "Roma", "A+"),
                (CLIENTI_BASE[1], "Servizi Legali & Fisco", "Milano", "A"),
                (CLIENTI_BASE[2], "Trasporti & Logistica", "Campobasso", "A+"),
                (CLIENTI_BASE[3], "Manifatturiero", "Pescara", "B"),
                (CLIENTI_BASE[4], "Commercio al Dettaglio", "Napoli", "B+"),
                (CLIENTI_BASE[5], "Sanità & Farmaci", "Campobasso", "A+"),
                (CLIENTI_BASE[6], "Marketing & Media", "Torino", "A"),
                (CLIENTI_BASE[7], "Costruzioni & Edilizia", "Campobasso", "B"),
                (CLIENTI_BASE[8], "Ospitalità & Turismo", "Isernia", "B+"),
                (CLIENTI_BASE[9], "Automotive & Riparazioni", "Termoli", "A"),
                (CLIENTI_BASE[10], "Servizi Sanitari", "Roma", "A+"),
                (CLIENTI_BASE[11], "Editoria & Cultura", "Firenze", "B"),
            ]
        ])
        df_clienti_anag.to_excel(writer, sheet_name="Anagrafica_Clienti", index=False)

    print(f"✅ Generato: {file_path} ({len(df)} righe)")
    return df

if __name__ == "__main__":
    print("--- GENERAZIONE DATASET CORSO PYTHON + ANALISI DATI ---")
    genera_dataset_filiale("Roma", 1200, os.path.join(RAW_DIR, "roma.xlsx"))
    genera_dataset_filiale("Milano", 1500, os.path.join(RAW_DIR, "milano.xlsx"))
    genera_dataset_filiale("Torino", 900, os.path.join(RAW_DIR, "torino.xlsx"))
    genera_dataset_filiale("Napoli", 1100, os.path.join(RAW_DIR, "napoli_project_work.xlsx"))
    print("--- TUTTI I DATASET RAW GENERATI CON SUCCESSO! ---")
