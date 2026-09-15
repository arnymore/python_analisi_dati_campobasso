# 🔍 QA REPORT FINALE: AUDIT TECNICO E REVISIONE DIDATTICA
## Corso: Laboratorio Python + Analisi Dati (22 Ore)
### Lead QA Engineer & Lead Instructional Designer: Arnaldo Morena • ITIS Campobasso • Anno 2026

---

## 📋 Executive Summary
Il presente report documenta l'audit tecnico, didattico e architetturale completo condotto sull'intero ecosistema del repository.
L'obiettivo primario dell'audit è stato **certificare la perfetta coerenza trasversale** tra tutti i materiali:
1. **Canovaccio Docente & Guide di Regia** (`KIT_DOCENTE/`)
2. **Storyboard & Slide Deck 75 slide** (`slides/`)
3. **Dispensa Ufficiale Studenti DOCX + PDF** (`dispensa/`)
4. **Laboratori Guidati & Esercizi** (`laboratori/`)
5. **Project Work Finale & Benchmark** (`project_work/`)
6. **Soluzioni Ufficiali & Versione Docente a 4 Livelli** (`soluzioni/`, `soluzioni_docente/`)
7. **Applicazione Web Reattiva** (`dashboard/app.py`)

---

# 🔎 FASE 1: AUDIT COMPLETO & ANALISI DELLE INCOERENZE

### 1.1 Incoerenze Rilevate e Risolte
* **Integrità del Merge Relazionale:** Nelle prime versioni di alcuni script di laboratorio, `pd.merge()` non includeva esplicitamente il parametro `validate="many_to_one"`. È stato allineato in tutto il repository, aggiungendo asserzioni di forma (`assert len(df_merged) == len(df_clean)`) per impedire moltiplicazioni di record.
* **Gestione Imputazione Avanzata vs Standard (`transform`):** È stato verificato che il percorso principale del Modulo 3 utilizzi `fillna()` con mediana o media globale, confinando `groupby().transform()` all'approfondimento facoltativo per evitare salti cognitivi prematuri.
* **Filtro Lock File Excel (`~$`):** Verificato che in tutti i punti di scansione batch (`glob`) sia presente il filtro di esclusione per i file temporanei `~$*.xlsx`.

### 1.2 Analisi di Concetti: Introdotti vs Spiegati vs Utilizzati
| Categoria di Controllo | Esito Audit | Note Didattiche & Azioni Intraprese |
| :--- | :---: | :--- |
| **Concetti introdotti troppo presto** | **RISOLTO** | `groupby().transform()` è stato spostato come approfondimento del Modulo 3, partendo prima da `fillna()` semplice. |
| **Concetti spiegati ma non utilizzati** | **RISOLTO** | Tutte le strutture native introdotte nel Modulo 1 (`List[Dict]`, `.get()`, list comprehension) trovano esatto riscontro ed evoluzione nei metodi di Pandas. |
| **Concetti utilizzati ma non spiegati** | **RISOLTO** | Il decoratore `@st.cache_data` e il modello di riesecuzione top-to-bottom di Streamlit sono ora spiegati dettagliatamente sia nelle slide sia nella dispensa sia nel canovaccio. |

### 1.3 Matrice di Coerenza: Storyboard vs Codice vs Dispensa vs Canovaccio
* **Slide Storyboard (75 slide):** Rispettano al 100% la ripartizione oraria certificata (Mod 1: 8 slide; Mod 2: 14 slide; Mod 3: 12 slide; Mod 4: 11 slide; Mod 5: 8 slide; Mod 6: 13 slide; Mod 7: 4 slide; PW: 5 slide).
* **Dispensa Studenti (25 pag. DOCX/PDF):** Contiene tutti gli 8 capitoli operativi, il glossario, le tabelle di benchmark e le domande di autovalutazione allineate agli esercizi.
* **Canovaccio Docente (`CANOVACCIO_DOCENTE.md`):** Fornisce per ogni modulo l'Apertura, lo Storytelling TechStore, le domande interattive, la scaletta di Live Demo, gli errori tipici e il timing minuto per minuto.

---

# 🪜 FASE 2: VERIFICA DELLA PROGRESSIONE DIDATTICA

L'architettura formativa segue una traiettoria rigorosamente progressiva a zero salti cognitivi:

```text
[Modulo 1: Python Operativo] (2h)
  └─► Fornisce la logica algoritmica, l'accumulo con dizionari e le strutture List[Dict].
        │
        ▼
[Modulo 2: Pandas Fondamentale] (4h)
  └─► Converte List[Dict] in DataFrame; insegna .loc/.iloc, filtri booleani e la regola aurea di .copy().
        │
        ▼
[Modulo 3: Data Wrangling & Merge] (3h)
  └─► Risolve anomalie reali: duplicati, missing values, date disomogenee e join relazionali con validazione 1:N.
        │
        ▼
[Modulo 4: Visualizzazione & Reporting] (3h)
  └─► Traduce i dati puliti in grafici professionali (Matplotlib OOP, Seaborn, Dashboard 2x2 a 300 DPI).
        │
        ▼
[Modulo 5: Automazione Pipeline ETL] (2h)
  └─► Incapsula pulizia e merge in un flusso batch (glob, filtro ~$, storage Parquet compresso, report Excel multi-scheda).
        │
        ▼
[Modulo 6: Dashboard Streamlit] (4h)
  └─► Alimenta l'applicazione web reattiva leggendo il Parquet con @st.cache_data, filtri dinamici e What-If simulator.
        │
        ▼
[Modulo 7: Deploy Linux & Systemd] (1h Live Demo)
  └─► Trasforma l'app locale in un servizio demone Linux persistente 24/7 (Restart=always, journalctl -f).
        │
        ▼
[Project Work Finale: Filiale Napoli] (3h)
  └─► Integrazione autonoma end-to-end della 4ª filiale contro i benchmark ufficiali (4.552 record, € 4.614.820,50).
```

---

# 💻 FASE 3: REVISIONE DEL CODICE SORGENTE

Tutti gli script in `soluzioni/` e `soluzioni_docente/` sono stati revisionati e certificati:
1. **`sol01_python_operativo`:** Funzioni pure, gestione arrotondamenti finanziari con `round(..., 2)`, list comprehension pulite.
2. **`sol02_pandas_fondamenti`:** Utilizzo rigoroso di `.copy()` dopo i filtri per prevenire `SettingWithCopyWarning`, naming coerente delle colonne.
3. **`sol03_data_wrangling`:** Funzione `parse_data_flessibile()` robusta su seriali Excel e mesi italiani, merge validato `many_to_one` con asserzione di integrità.
4. **`sol04_visualizzazione`:** Paradigma Matplotlib OOP (`fig, ax`), gestione dei DPI (300), rilascio esplicito della memoria con `plt.close()`.
5. **`sol05_automazione_pipeline`:** Logging con timestamp, filtro file lock `~$`, storage Parquet compresso, context manager per `ExcelWriter`.
6. **`sol06_dashboard_streamlit`:** `st.set_page_config()` come prima istruzione, `@st.cache_data` con TTL, layout multi-tab coordinato.
7. **`sol07_deploy_linux`:** Unit file Systemd con percorsi assoluti, isolamento privilegi (`User=arny`), gestione streaming log.

---

# 🎯 FASE 4: CONTROLLI OBBLIGATORI CERTIFICATI

| Controllo Obbligatorio | File Coinvolti | Stato | Dettagli di Conformità |
| :--- | :--- | :---: | :--- |
| **1. transform()** | `sol03`, `sol05`, Dispensa, Slide | ✅ CONFORME | Percorso base con `fillna()` e mediane; `transform()` spiegato come approfondimento contestuale. |
| **2. copy() & Warning** | `sol02`, `sol03`, `sol05`, `app.py` | ✅ CONFORME | `SettingWithCopyWarning` spiegato in teoria; `.copy()` applicato sistematicamente a ogni estrazione di subset. |
| **3. Merge Relazionale** | `sol03`, `sol05`, `sol_PW`, Dispensa | ✅ CONFORME | `validate="many_to_one"` attivo, deduplicazione preventiva anagrafica, asserzioni di cardinalità verificate. |
| **4. Pipeline ETL & Lock** | `sol05`, `sol05_commentato`, Lab 5 | ✅ CONFORME | Filtro `not os.path.basename(f).startswith('~$')` attivo in tutte le scansioni `glob`. |
| **5. Streamlit Reactive** | `dashboard/app.py`, `sol06`, Lab 6 | ✅ CONFORME | Riesecuzione top-to-bottom gestita con caching `@st.cache_data(ttl=600)`, nessun memory leak. |
| **6. Deploy Linux Systemd** | `sol07.sh`, `sol07.md`, Lab 7 | ✅ CONFORME | Percorsi assoluti, direttiva `Restart=always`, `RestartSec=5s`, monitoraggio `journalctl -u ... -f`. |

---

# 🧪 FASE 5: ESITI DEI TEST TECNICI ESEMPIO

1. **Test Esecuzione Script Moduli 1..5:** ✅ **PASSED** (Tutti gli script terminano con exit code 0).
2. **Test Ingestione Dataset Raw:** ✅ **PASSED** (Roma, Milano, Torino e Napoli caricati e validati).
3. **Test Generazione Master Parquet:** ✅ **PASSED** (File `vendite_consolidate_italia.parquet` generato correttamente).
4. **Test Modulo Dashboard Streamlit:** ✅ **PASSED** (Modulo importato e validato senza errori di sintassi o dipendenze).
5. **Test Soluzione Project Work (4 Filiali):** ✅ **PASSED** (Benchmark 4.700/4.552 record e quote fatturato verificate al centesimo).

---
