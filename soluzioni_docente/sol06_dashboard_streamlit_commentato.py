"""
=============================================================================
VERSIONE DOCENTE COMMENTATA: LABORATORIO 6 - STREAMLIT DASHBOARD
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================

STRUTTURA DEI COMMENTI A 4 LIVELLI DIDATTICI:
- LIVELLO 1 [TECNICO]: Widget Streamlit, layout a colonne, session state, caching, download buffer.
- LIVELLO 2 [BUSINESS]: KPI direzionali (Ticket Medio, Sconto Medio), What-If analysis, reportistica.
- LIVELLO 3 [DOCENTE]: Regia d'aula, spiegazione del modello di riesecuzione reattivo top-to-bottom.
- LIVELLO 4 [COLLEGAMENTO DIDATTICO]: Ponti verso il deploy Linux e demone Systemd (Mod 7).
=============================================================================
Esecuzione:
  streamlit run soluzioni_docente/sol06_dashboard_streamlit_commentato.py
=============================================================================
"""

import os
import io
import datetime
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------------------------
# 1. CONFIGURAZIONE DELLA PAGINA WEB (PAGE CONFIG & CSS)
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Regola fondamentale: `st.set_page_config()` DEVE essere la prima istruzione Streamlit
# eseguita nello script, altrimenti Streamlit solleva una StreamlitAPIException.

# LIVELLO 1 [TECNICO]:
# layout="wide" sfrutta l'intera ampiezza orizzontale dello schermo per layout a cruscotto.
st.set_page_config(
    page_title="Corporate Sales Analytics Dashboard | TechStore Italia",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# LIVELLO 1 [TECNICO]:
# Iniezione di stili CSS personalizzati per evidenziare i box delle metriche con bordi corporate.
st.markdown("""
<style>
    .main-metric-box {
        background-color: #f8f9fa;
        border-left: 5px solid #1E88E5;
        padding: 12px;
        border-radius: 6px;
        margin-bottom: 10px;
    }
    .stMetric label {
        font-weight: bold;
        color: #495057;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# 2. DATA INGESTION OTTIMIZZATA & CACHING MEMORIA
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Spiegare all'aula il 'Modello Reattivo': a ogni click dell'utente, l'intero file Python
# viene rieseguito dall'alto verso il basso.
# Il decoratore `@st.cache_data` è ciò che impedisce il collasso prestazionale:
# memorizza in RAM il DataFrame risultante e salta la lettura da disco se la funzione è già stata eseguita.

@st.cache_data(ttl=600)
def load_dataset():
    """Carica il dataset Parquet consolidato con caching in RAM per 10 minuti (600s)."""
    # LIVELLO 1 [TECNICO]:
    # Costruzione percorso portabile verso il dataset master generato dalla pipeline ETL.
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parquet_path = os.path.join(base_dir, "dataset", "generated", "vendite_consolidate_italia.parquet")
    
    # LIVELLO 1 [TECNICO] & LIVELLO 4 [COLLEGAMENTO DIDATTICO]:
    # Meccanismo di fallback auto-rigenerante: se il file Parquet non esiste ancora,
    # invoca automaticamente la pipeline ETL del Modulo 5 prima di procedere.
    if not os.path.exists(parquet_path):
        from soluzioni.sol05_automazione_pipeline import run_pipeline
        run_pipeline()
        
    df = pd.read_parquet(parquet_path)
    df["Data_Vendita"] = pd.to_datetime(df["Data_Vendita"])
    return df

# LIVELLO 1 [TECNICO]: Caricamento del dataset globale cached
df_raw = load_dataset()


# ---------------------------------------------------------------------------
# 3. SIDEBAR: PANNELLO DI CONTROLLO & FILTRI DINAMICI
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Mostrare come la sidebar (`st.sidebar`) ospiti tutti i controlli parametrici,
# lasciando l'area centrale completamente libera per i grafici e le tabelle decisionali.

st.sidebar.image("https://img.icons8.com/color/96/000000/combo-chart--v1.png", width=64)
st.sidebar.title("🎛️ Pannello Filtri")
st.sidebar.markdown("**TechStore Analytics • ITIS Campobasso**")
st.sidebar.markdown("---")

# LIVELLO 1 [TECNICO] & LIVELLO 2 [BUSINESS]:
# 1. Filtro Filiali Territoriali (Roma, Milano, Torino e poi Napoli nel Project Work)
filiali_disponibili = sorted(df_raw["Filiale"].dropna().unique().tolist())
sel_filiali = st.sidebar.multiselect("🏢 Seleziona Filiali", filiali_disponibili, default=filiali_disponibili)

# 2. Filtro Categorie Merceologiche
categorie_disponibili = sorted(df_raw["Categoria_Prodotto"].dropna().unique().tolist())
sel_categorie = st.sidebar.multiselect("📦 Categoria Prodotto", categorie_disponibili, default=categorie_disponibili)

# 3. Filtro Canali Distributivi (Direct, E-commerce, Retail)
canali_disponibili = sorted(df_raw["Canale_Vendita"].dropna().unique().tolist())
sel_canali = st.sidebar.multiselect("🌐 Canale di Vendita", canali_disponibili, default=canali_disponibili)

# 4. Filtro Temporale (Data Inizio e Data Fine)
min_data = df_raw["Data_Vendita"].min().date()
max_data = df_raw["Data_Vendita"].max().date()
sel_date = st.sidebar.date_input("📅 Periodo di Analisi", value=(min_data, max_data), min_value=min_data, max_value=max_data)

# LIVELLO 1 [TECNICO]:
# Applicazione cumulativa dei filtri booleani sul DataFrame
df_filtrato = df_raw[
    (df_raw["Filiale"].isin(sel_filiali)) &
    (df_raw["Categoria_Prodotto"].isin(sel_categorie)) &
    (df_raw["Canale_Vendita"].isin(sel_canali))
]

if isinstance(sel_date, (list, tuple)) and len(sel_date) == 2:
    start_d, end_d = sel_date
    df_filtrato = df_filtrato[(df_filtrato["Data_Vendita"].dt.date >= start_d) & (df_filtrato["Data_Vendita"].dt.date <= end_d)]

st.sidebar.markdown("---")
st.sidebar.info(f"📊 Record visualizzati: **{len(df_filtrato):,}** su {len(df_raw):,}")


# ---------------------------------------------------------------------------
# 4. HEADER PRINCIPALE & KPI CARDS STRATEGICHE
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Chiedere all'aula: "Quali sono i 5 numeri che un Amministratore Delegato vuole vedere nei primi 3 secondi?"
# 1. Fatturato Netto, 2. Numero Ordini, 3. Ticket Medio, 4. Sconto Medio Concesso, 5. Volumi Pezzi.

st.title("💼 Enterprise Sales Intelligence Dashboard")
st.caption(f"Dati Consolidati Rete Commerciale Italia • Ultimo aggiornamento: {datetime.date.today().strftime('%d/%m/%Y')}")

# LIVELLO 2 [BUSINESS]: Calcolo degli indicatori di sintesi sul sottoinsieme filtrato
tot_fatturato = df_filtrato["Fatturato_Netto"].sum()
tot_ordini = len(df_filtrato)
ticket_medio = tot_fatturato / tot_ordini if tot_ordini > 0 else 0
sconto_medio = df_filtrato["Sconto_Perc"].mean() if tot_ordini > 0 else 0
tot_quantita = df_filtrato["Quantita"].sum()

# LIVELLO 1 [TECNICO]: Disposizione a 5 colonne affiancate tramite `st.columns(5)`
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("💰 Fatturato Netto", f"€ {tot_fatturato:,.2f}")
c2.metric("📦 Volume Ordini", f"{tot_ordini:,}")
c3.metric("🧾 Ticket Medio", f"€ {ticket_medio:,.2f}")
c4.metric("🏷️ Sconto Medio", f"{sconto_medio:.1f} %")
c5.metric("🚚 Pezzi Venduti", f"{tot_quantita:,}")

st.markdown("---")


# ---------------------------------------------------------------------------
# 5. NAVIGAZIONE A SCHEDE (MULTI-TAB LAYOUT)
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Spiegare il beneficio di UX: invece di costringere l'utente a uno scroll verticale infinito,
# le schede organizzano le aree di competenza in tab tematici distinti.

tab_kpi, tab_clienti, tab_whatif, tab_dati = st.tabs([
    "📈 Panoramica & Trend",
    "👥 Clienti & Settori",
    "🔮 Simulatore What-If",
    "📋 Dati & Export"
])


# ---------------------------------------------------------------------------
# TAB 1: PANORAMICA TEMPORALE & CATEGORIE
# ---------------------------------------------------------------------------
with tab_kpi:
    col_left, col_right = st.columns([3, 2])
    
    with col_left:
        st.subheader("📅 Trend Mensile Fatturato per Filiale")
        # LIVELLO 1 [TECNICO]: Pivot con unstack per tracciare le linee delle singole filiali
        df_trend = (
            df_filtrato.groupby(["Mese", "Filiale"])["Fatturato_Netto"]
            .sum()
            .unstack(fill_value=0)
            .reset_index()
        )
        
        mesi_label = ["Gen", "Feb", "Mar", "Apr", "Mag", "Giu", "Lug", "Ago", "Set", "Ott", "Nov", "Dic"]
        
        fig, ax = plt.subplots(figsize=(9, 4.5))
        for col in [c for c in df_trend.columns if c != "Mese"]:
            ax.plot(df_trend["Mese"], df_trend[col] / 1000.0, marker="o", linewidth=2.2, label=col)
            
        ax.set_xticks(range(1, 13))
        ax.set_xticklabels(mesi_label)
        ax.set_ylabel("Fatturato (k€)", fontweight="bold")
        ax.set_xlabel("Mese", fontweight="bold")
        ax.legend(title="Filiale")
        ax.grid(True, linestyle="--", alpha=0.6)
        
        # LIVELLO 1 [TECNICO]: Rendering del grafico Matplotlib nel canvas web di Streamlit
        st.pyplot(fig)
        plt.close(fig)
        
    with col_right:
        st.subheader("📦 Fatturato per Categoria")
        cat_agg = df_filtrato.groupby("Categoria_Prodotto")["Fatturato_Netto"].sum().sort_values(ascending=True)
        
        fig, ax = plt.subplots(figsize=(6, 4.5))
        bars = ax.barh(cat_agg.index, cat_agg.values / 1000.0, color="#1976D2", edgecolor="black", alpha=0.85)
        ax.set_xlabel("Fatturato (k€)", fontweight="bold")
        for b in bars:
            w = b.get_width()
            ax.text(w + 1, b.get_y() + b.get_height()/2, f"{w:.1f}k€", va="center", fontsize=8, fontweight="bold")
        ax.grid(axis="x", linestyle=":", alpha=0.6)
        st.pyplot(fig)
        plt.close(fig)


# ---------------------------------------------------------------------------
# TAB 2: CLIENTI & SETTORI INDUSTRIALI
# ---------------------------------------------------------------------------
with tab_clienti:
    col_c1, col_c2 = st.columns(2)
    
    with col_c1:
        st.subheader("🏆 Top 10 Clienti Aziendali")
        top_c = (
            df_filtrato.dropna(subset=["Ragione_Sociale"])
            .groupby("Ragione_Sociale")
            .agg(Fatturato=("Fatturato_Netto", "sum"), Ordini=("ID_Transazione", "count"), Sconto_Medio=("Sconto_Perc", "mean"))
            .sort_values(by="Fatturato", ascending=False)
            .head(10)
        )
        # LIVELLO 1 [TECNICO]: Formattazione tabellare elegante tramite pandas Styler
        st.dataframe(
            top_c.style.format({
                "Fatturato": "€ {:,.2f}",
                "Ordini": "{:,}",
                "Sconto_Medio": "{:.1f}%"
            }),
            use_container_width=True
        )
        
    with col_c2:
        st.subheader("🏭 Performance per Settore di Mercato")
        sett_agg = (
            df_filtrato.groupby("Settore")["Fatturato_Netto"]
            .sum()
            .sort_values(ascending=False)
        )
        
        # Grafico Donut per la ripartizione settoriale
        fig, ax = plt.subplots(figsize=(7, 4.5))
        ax.pie(sett_agg.values, labels=sett_agg.index, autopct="%1.1f%%", startangle=140,
               wedgeprops=dict(width=0.4, edgecolor='w'))
        ax.set_title("Quote Fatturato per Settore Merceologico", fontweight="bold")
        st.pyplot(fig)
        plt.close(fig)


# ---------------------------------------------------------------------------
# TAB 3: SIMULATORE DI SCENARIO COMMERCIALE (WHAT-IF ANALYSIS)
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Questo è il modulo a più alto valore aggiunto per il business.
# Mostrare come collegare slider interattivi a formule matematiche per simulare
# politiche di sconto o variazioni di volume senza intaccare i dati storici reali.

with tab_whatif:
    st.subheader("🔮 Simulazione di Scenario Commerciale ('What-If Analysis')")
    st.markdown("Valuta l'impatto di decisioni strategiche su volumi di vendita e sconti commerciali.")
    
    w_col1, w_col2 = st.columns(2)
    with w_col1:
        delta_volume = st.slider("📈 Variazione Stimata Volume Vendite (%)", min_value=-50, max_value=50, value=0, step=5)
    with w_col2:
        delta_sconto = st.slider("🏷️ Variazione Margine / Sconto Punti Percentuali", min_value=-15, max_value=15, value=0, step=1)
        
    # LIVELLO 1 [TECNICO] & LIVELLO 2 [BUSINESS]:
    # Ricalcolo vettoriale istantaneo dello scenario ipotetico
    fatturato_simulato = 0.0
    for _, r in df_filtrato.iterrows():
        nuova_qta = max(0, r["Quantita"] * (1 + delta_volume / 100.0))
        nuovo_sconto = min(100, max(0, r["Sconto_Perc"] + delta_sconto))
        fatturato_riga = nuova_qta * r["Prezzo_Unitario"] * (1 - nuovo_sconto / 100.0)
        fatturato_simulato += fatturato_riga
        
    delta_fatturato_val = fatturato_simulato - tot_fatturato
    delta_fatturato_pct = (delta_fatturato_val / tot_fatturato * 100) if tot_fatturato > 0 else 0
    
    st.markdown("### Risultato Economico dello Scenario:")
    res_c1, res_c2, res_c3 = st.columns(3)
    res_c1.metric("Fatturato Attuale", f"€ {tot_fatturato:,.2f}")
    res_c2.metric("Fatturato Previsto nello Scenario", f"€ {fatturato_simulato:,.2f}", delta=f"{delta_fatturato_val:+,.2f} €")
    res_c3.metric("Impatto Percentuale", f"{delta_fatturato_pct:+.2f} %")


# ---------------------------------------------------------------------------
# TAB 4: DATI DI DETTAGLIO & FUNZIONALITÀ DI DOWNLOAD (CSV)
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Mostrare come consentire all'utente di effettuare ricerche full-text e scaricare
# un estratto dei record filtrati in formato CSV senza salvare file temporanei sul server.

with tab_dati:
    st.subheader("📋 Esploratore Record e Download")
    
    ricerca_testo = st.text_input("🔍 Cerca per Cliente, Prodotto o Codice Transazione:")
    df_mostra = df_filtrato.copy()
    
    if ricerca_testo:
        maschera = (
            df_mostra["Ragione_Sociale"].astype(str).str.contains(ricerca_testo, case=False, na=False) |
            df_mostra["Nome_Prodotto"].astype(str).str.contains(ricerca_testo, case=False, na=False) |
            df_mostra["ID_Transazione"].astype(str).str.contains(ricerca_testo, case=False, na=False)
        )
        df_mostra = df_mostra[maschera]
        
    st.dataframe(
        df_mostra[[
            "ID_Transazione", "Data_Vendita", "Filiale", "Ragione_Sociale",
            "Categoria_Prodotto", "Nome_Prodotto", "Quantita", "Prezzo_Unitario", "Sconto_Perc", "Fatturato_Netto"
        ]].head(200),
        use_container_width=True
    )
    
    # LIVELLO 1 [TECNICO]: Buffer in memoria con encoding UTF-8 per il pulsante di download
    csv_buffer = df_mostra.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Scarica Dati Filtrati in CSV",
        data=csv_buffer,
        file_name="vendite_filtrate_export.csv",
        mime="text/csv"
    )

# LIVELLO 4 [COLLEGAMENTO DIDATTICO]:
# Questa applicazione web, testata ed eseguita in locale, nel Modulo 7 verrà configurata
# come demone di produzione permanente gestito da Linux Systemd (dashboard_vendite.service).
