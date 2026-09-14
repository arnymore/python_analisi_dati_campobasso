# 🧪 Laboratori Pratici Studenti (80% Hands-On)

Questa directory contiene tutte le esercitazioni pratiche da svolgere durante le 22 ore di corso, suddivise per modulo tematico.

---

## 🗺️ Mappa dei Laboratori

| Modulo | Cartella | File Esercizio | Focus Didattico |
|:---|:---|:---|:---|
| **Modulo 1** | `lab01_python_operativo/` | `lab01_esercizi.py` | Liste, dizionari, funzioni commerciali, pulizia stringhe e aggregazioni native. |
| **Modulo 2** | `lab02_pandas_fondamenti/` | `lab02_esercizi.py` | Import Excel, esplorazione DataFrame, filtri booleani `.loc`/`.iloc`, colonne calcolate, ordinamento. |
| **Modulo 3** | `lab03_data_wrangling/` | `lab03_esercizi.py` | Deduplicazione, missing data drop/fillna, parsing date miste/seriali, merge anagrafica clienti e groupby. |
| **Modulo 4** | `lab04_visualizzazione/` | `lab04_esercizi.py` | Matplotlib & Seaborn, trend mensili, barplot Top Clienti, heatmap di correlazione, Executive Dashboard 2x2. |
| **Modulo 5** | `lab05_automazione_pipeline/` | `pipeline_etl.py` | Ingestion automatica con `glob`, trasformazione modulare, logging, esportazione Parquet ed Excel multi-foglio. |
| **Modulo 6** | `lab06_dashboard_streamlit/` | `app_starter.py` | Sviluppo Web App interattiva: filtri sidebar, KPI metrics cards, grafici e simulatore What-If. |
| **Modulo 7** | `lab07_deploy_linux/` | `guida_deploy.md`, `setup_service.sh` | Deploy su server Linux, servizio Systemd in background, monitoraggio log con journalctl, reverse proxy. |

---

## 💡 Istruzioni per lo Studente

1. Apri la cartella del laboratorio assegnato (es. `laboratori/lab01_python_operativo/`).
2. Leggi gli obiettivi e le consegne commentate all'interno del file `.py`.
3. Completa le sezioni contrassegnate con `# TODO:`.
4. Esegui il file per verificare la correttezza del codice:
   ```bash
   python laboratori/lab01_python_operativo/lab01_esercizi.py
   ```
5. In caso di dubbi o per confrontare il tuo approccio con le best practice di settore, consulta la corrispondente soluzione nella cartella `soluzioni/`.
