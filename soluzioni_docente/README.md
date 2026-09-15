# 👨‍🏫 SOLUZIONI COMMENTATE - VERSIONE DOCENTE
## Corso: Laboratorio Python + Analisi Dati (22 Ore)
### Docente: Arnaldo Morena • ITIS Campobasso • Anno 2026

---

## 🎯 Finalità di questa Cartella
Questa directory contiene la **versione formativa completa e commentata a 4 livelli didattici** di tutte le soluzioni ufficiali dei laboratori del corso.

A differenza delle soluzioni standard presenti in `soluzioni/` (che contengono solo il codice risolutivo), questi script sono veri e propri **copioni didattici operativi** pensati per supportare il docente durante la spiegazione, la conduzione del live coding e la gestione dei dubbi degli studenti.

---

## 📚 Lo Standard dei 4 Livelli Didattici di Commento

Ogni file di questa cartella adotta sistematicamente la seguente architettura di annotazione:

```python
# ---------------------------------------------------------------------------
# 1. LIVELLO 1 - COMMENTI TECNICI [TECNICO]
# Spiegazione approfondita della sintassi Python, metodi Pandas, tipi colonna,
# slicing, decoratori di caching e parametri funzionali.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 2. LIVELLO 2 - COMMENTI DI BUSINESS [BUSINESS]
# Contestualizzazione aziendale: logiche contabili ERP, ricavo netto vs lordo,
# marginalità commerciale, segmentazione clienti e canali distributivi.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 3. LIVELLO 3 - NOTE DI REGIA DOCENTE [DOCENTE]
# Suggerimenti per il docente: pause strategiche, domande da rivolgere all'aula,
# trappole cognitive tipiche dove gli studenti si bloccano e test interattivi.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 4. LIVELLO 4 - COLLEGAMENTI DIDATTICI [COLLEGAMENTO DIDATTICO]
# Ponti concettuali che collegano l'esercizio corrente ai moduli precedenti
# o ne evidenziano l'anticipazione rispetto ai moduli successivi e al Project Work.
# ---------------------------------------------------------------------------
```

---

## 📁 Mappa dei File Disponibili

| File Soluzione Commentata | Modulo di Riferimento | Descrizione Contenuto & Focus Didattico |
| :--- | :--- | :--- |
| [`sol01_python_operativo_commentato.py`](sol01_python_operativo_commentato.py) | **Modulo 1 (2h)** | Tipi primitivi, `List[Dict]`, funzioni pure, calcolo IVA/sconti, normalizzazione stringhe e accumulo nativo. |
| [`sol02_pandas_fondamenti_commentato.py`](sol02_pandas_fondamenti_commentato.py) | **Modulo 2 (4h)** | `Series`, `DataFrame`, importazione Excel, filtri booleani composti con `.loc`/`.iloc`, View vs Copy e `.copy()`. |
| [`sol03_data_wrangling_commentato.py`](sol03_data_wrangling_commentato.py) | **Modulo 3 (3h)** | Deduplicazione, missing values, parsing date robuste (`parse_data_flessibile`), merge validato `many_to_one`. |
| [`sol04_visualizzazione_commentato.py`](sol04_visualizzazione_commentato.py) | **Modulo 4 (3h)** | Matplotlib Object-Oriented (`fig, ax`), Barh con etichette, trend con media, boxplot sconti, heatmap e dashboard 2x2 (300 DPI). |
| [`sol05_automazione_pipeline_commentato.py`](sol05_automazione_pipeline_commentato.py) | **Modulo 5 (2h)** | Pipeline ETL batch, scansione `glob` con filtro `~$`, storage Parquet Snappy, report Excel multi-foglio e logging. |
| [`sol06_dashboard_streamlit_commentato.py`](sol06_dashboard_streamlit_commentato.py) | **Modulo 6 (4h)** | Web application reattiva completa: caching `@st.cache_data`, sidebar, metric cards `st.metric`, multi-tab, What-If simulator ed export CSV. |
| [`sol07_deploy_linux_commentato.md`](sol07_deploy_linux_commentato.md) | **Modulo 7 (1h)** | Guida al deploy su server Linux: analisi dell'unit file Systemd, permessi, comandi `systemctl`, log streaming con `journalctl -f`. |

---

## 🚀 Come Eseguire le Soluzioni

Tutti gli script Python sono **perfettamente eseguibili** e testati nell'ambiente virtuale del corso:

```bash
# Attivare l'ambiente virtuale
source .venv/bin/activate

# Esecuzione script Moduli 1..5
python soluzioni_docente/sol01_python_operativo_commentato.py
python soluzioni_docente/sol02_pandas_fondamenti_commentato.py
python soluzioni_docente/sol03_data_wrangling_commentato.py
python soluzioni_docente/sol04_visualizzazione_commentato.py
python soluzioni_docente/sol05_automazione_pipeline_commentato.py

# Avvio della Dashboard Streamlit (Modulo 6)
streamlit run soluzioni_docente/sol06_dashboard_streamlit_commentato.py
```

---
