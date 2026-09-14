"""
=============================================================================
LABORATORIO 6: DASHBOARD INTERATTIVA CON STREAMLIT (4 Ore)
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================

OBIETTIVI:
1. Comprendere l'architettura reattiva di Streamlit.
2. Costruire una UI professionale con layout responsive (sidebar, colonne, tabs, metric cards).
3. Integrare filtri interattivi dinamici (multiselect filiali, date_range, slider sconti).
4. Visualizzare grafici interattivi e tabelle dati formattate.
5. Aggiungere funzionalità di download dati (CSV/Excel) e un simulatore di scenari ("What-If").

CASO AZIENDALE:
La direzione vuole abbandonare i fogli Excel statici e accedere a una dashboard web
interattiva per monitorare le vendite di tutte le filiali in tempo reale.
=============================================================================
"""

import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# CONFIGURAZIONE PAGINA
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Executive Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Executive Dashboard Vendite Italia")
st.markdown("Monitoraggio KPI Commerciali e Performance Filiali (Roma, Milano, Torino)")

# ---------------------------------------------------------------------------
# CARICAMENTO DATI CON CACHING
# ---------------------------------------------------------------------------
@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    parquet_path = os.path.join(base_dir, "dataset", "generated", "vendite_consolidate_italia.parquet")
    df = pd.read_parquet(parquet_path)
    df["Data_Vendita"] = pd.to_datetime(df["Data_Vendita"])
    return df

df_master = load_data()

# ---------------------------------------------------------------------------
# ESERCIZIO 6.1: Sidebar e Filtri Interattivi
# ---------------------------------------------------------------------------
# TODO:
# 1. Crea un filtro multiselect nella sidebar per `Filiale` (default tutte).
# 2. Crea un filtro multiselect per `Categoria_Prodotto`.
# 3. Crea un date_input per filtrare l'intervallo date.
# 4. Applica i filtri al DataFrame principale.

st.sidebar.header("🎯 Filtri di Ricerca")
# Scrivi qui i filtri sidebar...


# ---------------------------------------------------------------------------
# ESERCIZIO 6.2: Metriche KPI (st.columns e st.metric)
# ---------------------------------------------------------------------------
# TODO:
# Crea 4 colonne (`st.columns(4)`) e mostra:
# - Fatturato Netto Totale (€)
# - Numero Ordini Totali
# - Ticket Medio per Ordine (€)
# - Sconto Medio Applicato (%)


# ---------------------------------------------------------------------------
# ESERCIZIO 6.3: Tab con Grafici e Tabelle
# ---------------------------------------------------------------------------
# TODO:
# Crea due schede: `tab1, tab2 = st.tabs(["Trend & Categorie", "Dati Dettagliati"])`
# In tab1: Grafico trend mensile e grafico a barre per categoria.
# In tab2: Tabella dati interattiva e pulsante di download CSV.
