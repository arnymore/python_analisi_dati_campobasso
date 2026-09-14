# Laboratorio 5: Automazione Pipeline ETL (2 Ore)

## 🎯 Obiettivi
* Progettare un'architettura modulare di elaborazione dati Extract-Transform-Load.
* Automatizzare l'ingestion multi-file dinamica con il modulo `glob`.
* Centralizzare le trasformazioni di pulizia e normalizzazione.
* Implementare il tracciamento dei log di processo con il modulo `logging`.
* Esportare i dati consolidati in formato Apache Parquet compresso e report Excel multi-scheda.

## 📄 File di Lavoro
* `pipeline_etl.py`: Scheletro della pipeline modulare da implementare.
* Input: Tutti i file `.xlsx` in `dataset/raw/`.
* Output: `dataset/generated/vendite_consolidate_italia.parquet` e `report_direzionale_consolidato.xlsx`.

## 🚀 Esecuzione
```bash
python laboratori/lab05_automazione_pipeline/pipeline_etl.py
```
Soluzione di riferimento: `soluzioni/sol05_automazione_pipeline.py`.
