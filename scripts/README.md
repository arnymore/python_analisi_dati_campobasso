# 🛠️ Scripts di Utilità e Setup

Questa cartella contiene gli script ausiliari per la preparazione e gestione dell'ambiente di corso.

---

## 📄 Script Disponibili

### `generate_datasets.py`
Script Python deterministico (seed impostato a `42`) per generare i dataset di partenza in formato Excel (`.xlsx`) all'interno di `dataset/raw/`:
* `roma.xlsx` (1.248 record)
* `milano.xlsx` (1.560 record)
* `torino.xlsx` (936 record)
* `napoli_project_work.xlsx` (1.144 record)

Ciascun file include dati di vendita con difetti controllati (duplicati, formati data misti, anomalie di stringa, valori nulli) e un foglio anagrafica clienti per le operazioni di `merge`.

#### Come Eseguire:
```bash
python scripts/generate_datasets.py
```
