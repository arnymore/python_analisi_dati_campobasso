"""
=============================================================================
SOLUZIONE UFFICIALE: PROJECT WORK FINALE
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================
"""

import os
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_DIR = os.path.join(BASE_DIR, "dataset", "raw")
OUT_DIR = os.path.join(BASE_DIR, "dataset", "generated")
os.makedirs(OUT_DIR, exist_ok=True)

MESI_MAP = {
    "gen": "01", "feb": "02", "mar": "03", "apr": "04",
    "mag": "05", "giu": "06", "lug": "07", "ago": "08",
    "set": "09", "ott": "10", "nov": "11", "dic": "12"
}

def parse_data(val):
    if pd.isna(val): return pd.NaT
    s = str(val).strip()
    if s.isdigit():
        try:
            return pd.to_datetime(datetime.date(1899, 12, 30) + datetime.timedelta(days=int(s)))
        except Exception:
            pass
    for m_k, m_v in MESI_MAP.items():
        if m_k in s.lower():
            p = s.split("-")
            if len(p) == 3:
                s = f"{p[2]}-{m_v}-{p[0].zfill(2)}"
                break
    try:
        return pd.to_datetime(s, format="mixed", dayfirst=True)
    except Exception:
        return pd.NaT

def normalizza_cat(c):
    if pd.isna(c): return "Altro"
    c = str(c).strip().lower()
    if "hard" in c or "hw" in c: return "Hardware"
    if "soft" in c or "sw" in c: return "Software"
    if "serv" in c: return "Servizi"
    if "canc" in c or "consum" in c: return "Cancelleria"
    return "Altro"

def clean_dataframe(df_raw, df_anag):
    # 1. Deduplica
    df = df_raw.drop_duplicates(subset=["ID_Transazione", "Data_Vendita", "Nome_Prodotto"]).copy()
    
    # 2. Stringhe
    df["Codice_Cliente"] = df["Codice_Cliente"].astype(str).str.strip().str.upper().replace(["NAN", "NONE"], np.nan)
    df["Ragione_Sociale"] = df["Ragione_Sociale"].astype(str).str.strip().replace(["nan", "None"], np.nan)
    df["Categoria_Prodotto"] = df["Categoria_Prodotto"].apply(normalizza_cat)
    
    # 3. Date
    df["Data_Vendita"] = df["Data_Vendita"].apply(parse_data)
    df["Data_Vendita"] = pd.to_datetime(df["Data_Vendita"])
    df["Mese"] = df["Data_Vendita"].dt.month
    df["Trimestre"] = df["Data_Vendita"].dt.to_period("Q").astype(str)
    
    # 4. Numerici
    df["Prezzo_Num"] = (
        df["Prezzo_Unitario"].astype(str)
        .str.replace("€", "", regex=False)
        .str.replace(",", ".", regex=False)
        .str.strip()
    )
    df["Prezzo_Num"] = pd.to_numeric(df["Prezzo_Num"], errors="coerce")
    media_prezzi = df.groupby("Nome_Prodotto")["Prezzo_Num"].transform("mean")
    df["Prezzo_Unitario_Fin"] = df["Prezzo_Num"].fillna(media_prezzi).round(2)
    
    mediana_qta = df.groupby("Nome_Prodotto")["Quantita"].transform("median")
    df["Quantita_Fin"] = df["Quantita"].fillna(mediana_qta).fillna(1).astype(int)
    
    df["Sconto_Perc"] = df["Sconto_Perc"].fillna(0).astype(float)
    df["Fatturato_Lordo"] = round(df["Quantita_Fin"] * df["Prezzo_Unitario_Fin"], 2)
    df["Valore_Sconto"] = round(df["Fatturato_Lordo"] * (df["Sconto_Perc"] / 100.0), 2)
    df["Fatturato_Netto"] = round(df["Fatturato_Lordo"] - df["Valore_Sconto"], 2)
    
    # 5. Merge Anagrafica
    df_a = df_anag.copy()
    df_a["Codice_Cliente"] = df_a["Codice_Cliente"].astype(str).str.strip().str.upper()
    df_m = pd.merge(
        df,
        df_a[["Codice_Cliente", "Settore", "Citta_Sede", "Rating_Affidabilita"]],
        on="Codice_Cliente",
        how="left"
    )
    df_m["Settore"] = df_m["Settore"].fillna("Non Specificato")
    df_m["Citta_Sede"] = df_m["Citta_Sede"].fillna("Non Specificata")
    df_m["Rating_Affidabilita"] = df_m["Rating_Affidabilita"].fillna("N.D.")
    
    colonne_finali = [
        "ID_Transazione", "Data_Vendita", "Mese", "Trimestre",
        "Filiale", "Codice_Cliente", "Ragione_Sociale", "Settore", "Citta_Sede", "Rating_Affidabilita",
        "Categoria_Prodotto", "Nome_Prodotto", "Quantita_Fin", "Prezzo_Unitario_Fin",
        "Sconto_Perc", "Fatturato_Lordo", "Valore_Sconto", "Fatturato_Netto", "Canale_Vendita", "Note"
    ]
    df_result = df_m[colonne_finali].rename(columns={
        "Quantita_Fin": "Quantita",
        "Prezzo_Unitario_Fin": "Prezzo_Unitario"
    })
    return df_result

def run_project_work():
    print("==================================================================")
    print("      ESECUZIONE SOLUZIONE PROJECT WORK (4 FILIALI)              ")
    print("==================================================================")
    
    # Caricamento di tutti i 4 file (incluso Napoli)
    files = ["roma.xlsx", "milano.xlsx", "torino.xlsx", "napoli_project_work.xlsx"]
    lista_df_v = []
    lista_df_a = []
    
    for f_name in files:
        p = os.path.join(DATASET_DIR, f_name)
        df_v = pd.read_excel(p, sheet_name="Dati_Vendite")
        lista_df_v.append(df_v)
        df_a = pd.read_excel(p, sheet_name="Anagrafica_Clienti")
        lista_df_a.append(df_a)
        
    df_raw_tot = pd.concat(lista_df_v, ignore_index=True)
    df_anag_tot = pd.concat(lista_df_a, ignore_index=True).drop_duplicates(subset=["Codice_Cliente"])
    
    df_master_4 = clean_dataframe(df_raw_tot, df_anag_tot)
    
    # Salvataggio parquet consolidato a 4 filiali
    out_parquet = os.path.join(OUT_DIR, "vendite_consolidate_nazionale_4filiali.parquet")
    df_master_4.to_parquet(out_parquet, index=False)
    print(f"✅ Salvato Master 4 Filiali: {out_parquet} ({len(df_master_4)} record)")
    
    # --- RISPOSTE AI QUESITI DI BUSINESS ---
    print("\n--- 1. BENCHMARK QUOTE FILIALI ---")
    kpi_fil = df_master_4.groupby("Filiale").agg(
        Fatturato_Netto=("Fatturato_Netto", "sum"),
        Ordini=("ID_Transazione", "count")
    )
    kpi_fil["Quota_Perc"] = (kpi_fil["Fatturato_Netto"] / kpi_fil["Fatturato_Netto"].sum() * 100).round(2)
    print(kpi_fil.sort_values(by="Fatturato_Netto", ascending=False).to_string())
    
    print("\n--- 2. PERFORMANCE FILIALE NAPOLI PER CATEGORIA ---")
    df_napoli = df_master_4[df_master_4["Filiale"] == "Napoli"]
    kpi_nap_cat = df_napoli.groupby("Categoria_Prodotto").agg(
        Fatturato_Netto=("Fatturato_Netto", "sum"),
        Pezzi_Venduti=("Quantita", "sum"),
        Sconto_Medio=("Sconto_Perc", "mean")
    ).sort_values(by="Fatturato_Netto", ascending=False)
    print(kpi_nap_cat.to_string())
    
    print("\n--- 3. CANALI DI VENDITA A NAPOLI ---")
    kpi_nap_can = df_napoli.groupby("Canale_Vendita").agg(
        Fatturato_Netto=("Fatturato_Netto", "sum"),
        Numero_Ordini=("ID_Transazione", "count"),
        Ticket_Medio=("Fatturato_Netto", "mean")
    ).sort_values(by="Fatturato_Netto", ascending=False)
    print(kpi_nap_can.to_string())
    
    # --- GENERAZIONE GRAFICI DI REPORTISTICA ---
    print("\n--- 4. GENERAZIONE GRAFICI COMPARATIVI NAZIONALI ---")
    
    # Grafico 1: Quota e Fatturato Filiali
    fig, ax = plt.subplots(figsize=(8, 5))
    bar_data = kpi_fil.sort_values(by="Fatturato_Netto", ascending=False)
    bars = ax.bar(bar_data.index, bar_data["Fatturato_Netto"] / 1000.0, color=["#1E88E5", "#43A047", "#FB8C00", "#E53935"], edgecolor="black")
    ax.set_title("Confronto Fatturato Netto per Filiale Commerciale (k€)", fontsize=13, fontweight="bold", pad=12)
    ax.set_ylabel("Fatturato (k€)", fontweight="bold")
    for b in bars:
        h = b.get_height()
        ax.text(b.get_x() + b.get_width()/2, h + 20, f"{h:.0f}k€", ha="center", fontsize=9, fontweight="bold")
    plt.tight_layout()
    g1_path = os.path.join(OUT_DIR, "pw_confronto_filiali.png")
    plt.savefig(g1_path, dpi=200)
    plt.close()
    
    # Grafico 2: Trend Mensile Comparativo 4 Filiali
    fig, ax = plt.subplots(figsize=(10, 5))
    trend_4 = df_master_4.groupby(["Mese", "Filiale"])["Fatturato_Netto"].sum().unstack() / 1000.0
    mesi_label = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", "Lug", "Ago", "Set", "Ott", "Nov", "Dic"]
    for col in trend_4.columns:
        ax.plot(trend_4.index, trend_4[col], marker="o", linewidth=2, label=col)
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(mesi_label)
    ax.set_title("Trend Mensile Vendite 2024: Benchmark tra le 4 Filiali", fontsize=13, fontweight="bold", pad=12)
    ax.set_ylabel("Fatturato Mensile (k€)", fontweight="bold")
    ax.legend(title="Filiale")
    ax.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    g2_path = os.path.join(OUT_DIR, "pw_trend_mensile_4filiali.png")
    plt.savefig(g2_path, dpi=200)
    plt.close()
    
    # Grafico 3: Heatmap Categoria x Filiale
    fig, ax = plt.subplots(figsize=(8, 5))
    pivot_fil_cat = df_master_4.pivot_table(index="Filiale", columns="Categoria_Prodotto", values="Fatturato_Netto", aggfunc="sum") / 1000.0
    sns.heatmap(pivot_fil_cat, annot=True, fmt=".1f", cmap="YlOrRd", cbar_kws={'label': 'Fatturato (k€)'}, ax=ax)
    ax.set_title("Matrice Fatturato Netto: Filiale x Categoria Prodotto (k€)", fontsize=12, fontweight="bold", pad=12)
    plt.tight_layout()
    g3_path = os.path.join(OUT_DIR, "pw_heatmap_filiale_categoria.png")
    plt.savefig(g3_path, dpi=200)
    plt.close()
    
    print(f"✅ Grafici salvati con successo in: {OUT_DIR}")
    print("==================================================================")

if __name__ == "__main__":
    run_project_work()
