# 🎓 Laboratorio Python + Analisi Dati
### Corso Formativo e Professionalizzante (22 Ore)

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.2%2B-150458.svg)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Format: Hands--On](https://img.shields.io/badge/Formato-80%25%20Laboratorio%20%7C%2020%25%20Teoria-success.svg)](#metodologia)

**Docente:** Arnaldo Morena  
**Sede / Ente:** ITIS Campobasso  
**Repository Ufficiale:** [https://github.com/arnymore/python_analisi_dati_campobasso](https://github.com/arnymore/python_analisi_dati_campobasso)

---

## 🏢 Il Caso Aziendale Unico

Il corso accompagna i partecipanti lungo l'intero ciclo di vita del dato attraverso un **unico caso aziendale concreto**: l'analisi commerciale, il consolidamento dati e il monitoraggio delle performance di vendita di una società di distribuzione IT e servizi con filiali operative a **Roma**, **Milano**, **Torino** e la recente espansione a **Napoli**.

Partendo da fogli Excel grezzi ed eterogenei ("dirty data"), gli studenti impareranno a:
1. Automatizzare le elaborazioni con **Python puro**.
2. Manipolare e pulire tabelle complesse con **Pandas**.
3. Gestire duplicati, valori mancanti, formati data misti e join anagrafiche (**Data Wrangling**).
4. Costruire grafici ad alto impatto con **Matplotlib** e **Seaborn**.
5. Costruire una **Pipeline ETL automatizzata** con output compresso in **Apache Parquet**.
6. Realizzare e pubblicare una **Dashboard Web interattiva** con **Streamlit**.
7. Configurare il **Deploy continuo su Server Linux** con gestione tramite **Systemd**.

---

## 🗂️ Struttura Dettagliata del Repository

```text
python_analisi_dati_campobasso/
├── README.md                            # Guida principale del corso
├── requirements.txt                     # Dipendenze e librerie Python
├── CONTRIBUTING.md                      # Linee guida per contribuzioni e PR
├── LICENSE                              # Licenza open-source MIT
├── .gitignore                           # Configurazione esclusioni Git
│
├── dataset/                             # Dati del corso (Raw e Generati)
│   ├── raw/                             # Dataset Excel grezzi di input
│   │   ├── README.md                    # Descrizione colonne e difetti controllati
│   │   ├── roma.xlsx                    # Transazioni e anagrafica filiale Roma (~1.200 record)
│   │   ├── milano.xlsx                  # Transazioni e anagrafica filiale Milano (~1.500 record)
│   │   ├── torino.xlsx                  # Transazioni e anagrafica filiale Torino (~900 record)
│   │   └── napoli_project_work.xlsx     # Dataset per il Project Work finale (~1.100 record)
│   └── generated/                       # Output prodotti da pipeline e script
│       ├── README.md                    # Dettaglio degli artefatti generati
│       ├── vendite_consolidate_italia.parquet
│       ├── vendite_consolidate_nazionale_4filiali.parquet
│       ├── report_direzionale_consolidato.xlsx
│       └── *.png                        # Grafici e dashboard 2x2 ad alta risoluzione
│
├── scripts/                             # Script di supporto
│   ├── README.md                        # Guida all'uso degli script
│   └── generate_datasets.py             # Generatore deterministico dei dataset Excel sporchi
│
├── laboratori/                          # Esercitazioni pratiche per gli studenti
│   ├── README.md                        # Mappa dei laboratori e istruzioni
│   ├── lab01_python_operativo/          # Modulo 1 (2h): Strutture dati, funzioni e stringhe
│   ├── lab02_pandas_fondamenti/         # Modulo 2 (4h): Dataframe, filtri .loc/.iloc, ordinamenti
│   ├── lab03_data_wrangling/            # Modulo 3 (3h): Deduplica, missing values, date, merge
│   ├── lab04_visualizzazione/           # Modulo 4 (3h): Matplotlib, Seaborn, Heatmap, Subplots 2x2
│   ├── lab05_automazione_pipeline/      # Modulo 5 (2h): Pipeline ETL batch, glob, logging, Parquet
│   ├── lab06_dashboard_streamlit/       # Modulo 6 (4h): Web app, filtri sidebar, KPI, What-If
│   └── lab07_deploy_linux/              # Modulo 7 (1h): Daemon Systemd, systemctl, journalctl
│
├── soluzioni/                           # Codice di riferimento per il docente
│   ├── README.md                        # Indice delle soluzioni e comandi di test
│   ├── sol01_python_operativo.py
│   ├── sol02_pandas_fondamenti.py
│   ├── sol03_data_wrangling.py
│   ├── sol04_visualizzazione.py
│   ├── sol05_automazione_pipeline.py
│   ├── sol06_dashboard_streamlit.py
│   └── sol07_deploy_linux.sh
│
├── dashboard/                           # Applicazione Web interattiva Streamlit
│   ├── README.md                        # Guida e funzionalità della dashboard
│   └── app.py                           # Codice completo dell'app (Filtri, KPI, Tabs, Export)
│
├── project_work/                        # Materiale per il Project Work finale (3 Ore)
│   ├── README.md                        # Panoramica del Project Work
│   ├── traccia_studenti.md              # Traccia e requisiti per i partecipanti
│   ├── criteri_valutazione.md           # Rubrica analitica di valutazione (100 punti)
│   └── soluzione_project_work.py        # Soluzione eseguibile con analisi e grafici
│
├── slides/                              # Piano e storyboard didattico
│   ├── README.md                        # Mappa della presentazione
│   └── piano_slide_storyboard.md        # Storyboard dettagliato di 100 Slide
│
└── dispensa/                            # Documentazione teorico-pratica di riferimento
    ├── README.md                        # Struttura del manuale operativo
    └── indice_dispensa.md               # Indice dettagliato capitolo per capitolo
```

---

## ⏱️ Programma Orario & Articolazione Didattica (22 Ore)

| Modulo | Titolo | Durata | Metodologia | Obiettivo Chiave |
|:---|:---|:---:|:---:|:---|
| **Modulo 1** | Python Operativo per l'Analisi Dati | **2 ore** | 20% T / 80% L | Tipi nativi, liste, dizionari, funzioni di calcolo commerciale e pulizia stringhe. |
| **Modulo 2** | Pandas: Fondamenti e Manipolazione | **4 ore** | 20% T / 80% L | Ingestion Excel, filtri booleani `.loc`/`.iloc`, colonne calcolate, ordinamento. |
| **Modulo 3** | Data Wrangling, Pulizia e Integrazione | **3 ore** | 20% T / 80% L | Deduplica, imputazione nulli, parsing date miste/seriali, merge anagrafiche. |
| **Modulo 4** | Visualizzazione Dati e Reporting | **3 ore** | 20% T / 80% L | Matplotlib & Seaborn, trend mensili, barplot, heatmap e Executive Dashboard 2x2. |
| **Modulo 5** | Automazione Pipeline ETL | **2 ore** | 20% T / 80% L | Ingestion multi-file con `glob`, trasformazione massiva, Parquet ed Excel multi-scheda. |
| **Modulo 6** | Dashboard Interattive con Streamlit | **4 ore** | 20% T / 80% L | Web app interattiva, sidebar filtri, KPI cards, grafici dinamici, download e simulatore What-If. |
| **Modulo 7** | Deploy su Server Linux & Produzione | **1 ora** | 20% T / 80% L | Servizio Systemd continuo, auto-restart, gestione demone, journalctl e reverse proxy. |
| **Project Work**| Project Work Finale & Presentazione | **3 ore** | 100% Lab | Ingestion filiale Napoli, consolidamento nazionale a 4 filiali, analisi business e report. |
| **TOTALE** | | **22 ore** | **80% Lab / 20% Teoria** | **Autonomia operativa completa** |

---

## 🚀 Guida Rapida all'Installazione e Setup

### 1. Prerequisiti
* Python 3.10 o superiore installato sul sistema.
* Git installato e configurato.

### 2. Installazione dell'Ambiente
```bash
# 1. Clonazione del repository
git clone https://github.com/arnymore/python_analisi_dati_campobasso.git
cd python_analisi_dati_campobasso

# 2. Creazione dell'ambiente virtuale isolato
python3 -m venv .venv

# 3. Attivazione dell'ambiente virtuale
source .venv/bin/activate       # Su Linux/macOS
# oppure .venv\Scripts\activate  # Su Windows

# 4. Installazione delle dipendenze
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🖥️ Comandi Operativi per Docente e Studenti

```bash
# Rigenerare i dataset raw da zero (opzionale):
python scripts/generate_datasets.py

# Eseguire la Pipeline ETL automatizzata:
python soluzioni/sol05_automazione_pipeline.py

# Avviare la Dashboard Streamlit nel browser (http://localhost:8501):
streamlit run dashboard/app.py

# Eseguire la soluzione del Project Work Finale:
python project_work/soluzione_project_work.py
```

---

## 📄 Licenza

Questo progetto è distribuito sotto licenza **MIT** - consulta il file [LICENSE](LICENSE) per i dettagli completi.
