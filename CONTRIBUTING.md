# 🤝 Guida ai Contributi (Contributing Guidelines)

Grazie per l'interesse a contribuire al materiale del corso **"Laboratorio Python + Analisi Dati"** tenuto dal docente **Arnaldo Morena**.

---

## 🧭 Codice di Condotta
Ci impegniamo a garantire un ambiente accogliente, inclusivo e rispettoso per tutti gli studenti e collaboratori.

---

## 🛠️ Come Contribuire

### 1. Segnalazione di Bug o Refusi
Se riscontri un errore nel codice degli esercizi, nelle soluzioni o nel testo della dispensa/slide:
1. Verifica tra le Issue aperte se il problema è già stato segnalato.
2. Apri una nuova **Issue** specificando:
   - Modulo e file interessato (es. `laboratori/lab03_data_wrangling/lab03_esercizi.py`).
   - Descrizione del comportamento atteso vs comportamento effettivo.
   - Eventuale traceback dell'errore.

### 2. Proposta di Modifiche (Pull Request)
1. Esegui il **Fork** del repository sul tuo account GitHub.
2. Clona il fork in locale:
   ```bash
   git clone https://github.com/<tuo-username>/python_analisi_dati_campobasso.git
   ```
3. Crea un branch descrittivo per la tua modifica:
   ```bash
   git checkout -b feature/miglioramento-lab02
   ```
4. Applica le modifiche assicurandoti che:
   - Il codice rispetti le convenzioni PEP 8.
   - Tutti gli script di test in `soluzioni/` e `project_work/` continuino a essere eseguiti senza errori.
   - Le modifiche ai percorsi dei file siano sempre indipendenti dalla piattaforma (`os.path.join` o `pathlib`).
5. Esegui il commit con un messaggio chiaro in italiano o inglese:
   ```bash
   git commit -m "fix(lab02): correzione parsing colonne numeriche"
   ```
6. Fai il push sul tuo branch remoto e apri una **Pull Request** verso il branch `main` del repository principale.

---

## 🧪 Standard di Qualità del Codice

* **Python 3.10+**: Il codice deve essere compatibile con le versioni moderne di Python.
* **Commenti e Docstring**: Ogni funzione deve contenere una breve docstring che ne spieghi parametri, output e finalità.
* **No Hardcoding di Credenziali**: Non inserire mai password, token o percorsi assoluti specifici della macchina locale.
