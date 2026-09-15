# 🛠️ TROUBLESHOOTING D'AULA: GUIDA ALLA RISOLUZIONE DEI PROBLEMI
## Corso: Laboratorio Python + Analisi Dati (22 Ore)
### Docente: Arnaldo Morena • ITIS Campobasso

---

Questa guida è uno strumento di pronto intervento rapido per il docente e per gli assistenti d'aula. Per ogni problema frequente viene descritto il **Sintomo riscontrato**, la **Causa radice** e la **Soluzione immediata (Quick Fix)**.

---

# 1. 🐍 PROBLEMI PYTHON, AMBIENTI VIRTUALI & DEPENDENCIES

### 1.1 `ModuleNotFoundError: No module named 'pandas'` (o 'streamlit', 'seaborn')
* **Sintomo:** Lo script o il notebook fallisce subito alla prima riga di `import`.
* **Causa Radice:** L'ambiente virtuale `.venv` non è stato attivato nel terminale, oppure Jupyter Lab sta eseguendo un kernel Python globale di sistema invece del kernel virtualenv.
* **Quick Fix:**
  1. Da terminale: `source .venv/bin/activate` (Linux/Mac) o `.venv\Scripts\activate` (Windows).
  2. In Jupyter Lab: verificare in alto a destra che il kernel selezionato sia `.venv (Python 3.x)`. Se non compare:
     ```bash
     .venv/bin/python -m ipykernel install --user --name=corso_python --display-name="Python (Corso ITIS)"
     ```

### 1.2 `SyntaxError: invalid syntax` su operatore di tipo o f-string
* **Sintomo:** Python segnala errore di sintassi su `list[dict]` o su formattazioni con f-string.
* **Causa Radice:** Lo studente sta usando una versione obsoleta di Python (es. Python 3.7 o 3.8).
* **Quick Fix:**
  Verificare la versione: `python3 --version`. Se inferiore a 3.10, installare Python 3.10+ o usare la sintassi compatibile `typing.List` e `typing.Dict`.

### 1.3 `PermissionError: [Errno 13] Permission denied` su file Excel
* **Sintomo:** Impossibile leggere o sovrascrivere un file `.xlsx` durante l'esecuzione di uno script.
* **Causa Radice:** Il file Excel è aperto in un'altra finestra con Microsoft Excel o LibreOffice Calc, che ha posto un lock esclusivo sul file.
* **Quick Fix:**
  Chiudere l'applicazione Excel/Calc e rieseguire lo script.

---

# 2. 🐼 PROBLEMI PANDAS & DATA WRANGLING

### 2.1 `SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame`
* **Sintomo:** Compare un rettangolo rosso con warning durante l'assegnazione di una colonna (`df_sub['nuova_col'] = ...`).
* **Causa Radice:** `df_sub` è stato creato tramite un filtro senza aver invocato il metodo `.copy()`, lasciando Pandas nell'incertezza tra copia e vista.
* **Quick Fix:**
  Aggiungere esplicitamente `.copy()` al momento del filtraggio:
  ```python
  # CORRETTO:
  df_sub = df.loc[df['Quantita'] > 5].copy()
  df_sub['Fatturato_Netto'] = df_sub['Quantita'] * df_sub['Prezzo_Unitario']
  ```

### 2.2 `MergeError: Merge keys have non-unique values in right frame; cannot validate many-to-one`
* **Sintomo:** Il merge relazionale si blocca con eccezione `MergeError`.
* **Causa Radice:** La tabella anagrafica contiene chiavi duplicate (es. due clienti con lo stesso `Codice_Cliente`), violando la regola di integrità `validate='many_to_one'`.
* **Quick Fix:**
  Deduplicare la tabella di destra sulla chiave primaria prima del merge:
  ```python
  df_anagrafica_clean = df_anagrafica.drop_duplicates(subset=['Codice_Cliente']).copy()
  df_merged = pd.merge(df_clean, df_anagrafica_clean, on='Codice_Cliente', how='left', validate='m:1')
  ```

### 2.3 Date invertite o non riconosciute (giorno e mese scambiati)
* **Sintomo:** Una data come `05/06/2024` (5 Giugno) viene parsata come `2024-05-06` (6 Maggio).
* **Causa Radice:** `pd.to_datetime()` di default utilizza il formato anglosassone mese-prima (`monthfirst=True`).
* **Quick Fix:**
  Specificare `dayfirst=True` o definire il formato esplicito:
  ```python
  df['Data_dt'] = pd.to_datetime(df['Data_Vendita'], format='mixed', dayfirst=True)
  ```

### 2.4 Numeri letti come stringhe (tipo `object`) con `€` o virgole
* **Sintomo:** Le operazioni matematiche falliscono con `TypeError: can't multiply sequence by non-int of type 'float'`.
* **Causa Radice:** I prezzi importati contengono caratteri non numerici (spazi, simboli di valuta `€`, virgole per i decimali).
* **Quick Fix:**
  Applicare una pipeline di normalizzazione testuale prima della conversione numerica:
  ```python
  df['Prezzo_Pulito'] = (
      df['Prezzo_Unitario'].astype(str)
      .str.replace('€', '', regex=False)
      .str.replace(',', '.', regex=False)
      .str.strip()
  )
  df['Prezzo_Pulito'] = pd.to_numeric(df['Prezzo_Pulito'], errors='coerce')
  ```

---

# 3. 📊 PROBLEMI VISUALIZZAZIONE (MATPLOTLIB & SEABORN)

### 3.1 Etichette dell'asse X sovrapposte e illeggibili
* **Sintomo:** Le ragioni sociali dei clienti o i nomi dei mesi si sovrappongono formando una striscia nera illeggibile.
* **Causa Radice:** Mancanza di rotazione o troppi elementi sull'asse orizzontale.
* **Quick Fix:**
  1. Ruotare le etichette: `ax.tick_params(axis='x', rotation=45)` o `plt.xticks(rotation=45)`.
  2. Per molti elementi con testi lunghi, passare a un grafico a barre orizzontali: `ax.barh(...)`.

### 3.2 Grafico tagliato ai bordi nel file PNG salvato su disco
* **Sintomo:** Il titolo superiore o i valori dell'asse Y non compaiono nell'immagine esportata.
* **Causa Radice:** I margini della figura non sono stati ricalcolati automaticamente prima del salvataggio.
* **Quick Fix:**
  Invocare `plt.tight_layout()` e specificare `bbox_inches='tight'` in `savefig`:
  ```python
  plt.tight_layout()
  fig.savefig('report.png', dpi=300, bbox_inches='tight')
  ```

### 3.3 Warning `UserWarning: The figure layout has changed to tight`
* **Sintomo:** Compare un avviso durante l'esecuzione di più chiamate a `tight_layout()`.
* **Causa Radice:** Chiamata ridondante di `tight_layout()` dopo che il motore grafico ha già finalizzato la geometria.
* **Quick Fix:**
  Chiamare `plt.tight_layout()` una sola volta subito prima di `plt.show()` o `fig.savefig()`.

---

# 4. 🌐 PROBLEMI STREAMLIT & WEB DASHBOARD

### 4.1 `StreamlitAPIException: set_page_config() can only be called once per app page, and must be the first Streamlit command used`
* **Sintomo:** L'applicazione Streamlit si blocca con schermata di errore rossa.
* **Causa Radice:** È stato inserito un comando come `st.title()` o `st.write()` prima di `st.set_page_config()`.
* **Quick Fix:**
  Spostare `st.set_page_config(...)` in cima allo script come prima istruzione Streamlit in assoluto.

### 4.2 L'applicazione web è lenta e si ricarica faticosamente a ogni click
* **Sintomo:** Ogni volta che l'utente muove uno slider o seleziona un filtro, compare il logo 'Running' per diversi secondi.
* **Causa Radice:** La funzione di caricamento del dataset (`load_dataset()`) o le elaborazioni pesanti non sono decorate con `@st.cache_data`.
* **Quick Fix:**
  Aggiungere il decoratore di caching:
  ```python
  @st.cache_data(ttl=600)
  def load_dataset():
      return pd.read_parquet('dataset/generated/vendite_consolidate_italia.parquet')
  ```

### 4.3 `OSError: [Errno 98] Address already in use` (Porta 8501 occupata)
* **Sintomo:** Il comando `streamlit run app.py` fallisce indicando che la porta di rete è già utilizzata.
* **Causa Radice:** Un'altra istanza di Streamlit è già in esecuzione in background sulla porta di default 8501.
* **Quick Fix:**
  1. Specificare una porta alternativa: `streamlit run app.py --server.port 8502`.
  2. Oppure terminare il processo precedente:
     ```bash
     fuser -k 8501/tcp   # Su Linux
     killall streamlit   # Termina tutti i processi Streamlit attivi
     ```

### 4.4 I grafici Matplotlib mostrano warning o layout rimpiccioliti nella dashboard
* **Sintomo:** Compare `PyplotGlobalUseWarning` nella console.
* **Causa Radice:** Utilizzo di `st.pyplot()` senza passare esplicitamente l'oggetto `fig`.
* **Quick Fix:**
  Creare sempre esplicitamente la figura e passarla al widget:
  ```python
  fig, ax = plt.subplots(figsize=(10, 5))
  # ... codice di plotting ...
  st.pyplot(fig)
  plt.close(fig)
  ```

---

# 5. 🐧 PROBLEMI LINUX, SSH & SYSTEMD DEPLOY

### 5.1 `Failed to start service: Unit ... not found`
* **Sintomo:** Il comando `sudo systemctl start dashboard_vendite.service` fallisce.
* **Causa Radice:** Il file `.service` non è stato copiato in `/etc/systemd/system/` oppure non è stato eseguito `daemon-reload`.
* **Quick Fix:**
  ```bash
  sudo cp /tmp/dashboard_vendite.service /etc/systemd/system/
  sudo systemctl daemon-reload
  sudo systemctl start dashboard_vendite.service
  ```

### 5.2 Lo stato del servizio è `failed (Result: exit-code)`
* **Sintomo:** `sudo systemctl status dashboard_vendite.service` mostra lo stato in rosso con errore di terminazione.
* **Causa Radice:** Percorso errato dell'interprete virtualenv in `ExecStart` o permessi non concessi all'utente specificato in `User=`.
* **Quick Fix:**
  Ispezionare i log dettagliati dell'errore:
  ```bash
  sudo journalctl -u dashboard_vendite.service -e --no-pager
  ```
  Verificare che il percorso in `ExecStart` sia assoluto e che il file Python esista realmente in quel percorso.

### 5.3 L'applicazione funziona localmente ma non è raggiungibile dall'esterno (browser degli altri PC)
* **Sintomo:** Il browser restituisce *"Impossibile raggiungere il sito"* collegandosi all'IP del server (`http://<IP_SERVER>:8501`).
* **Causa Radice:**
  1. Streamlit è stato avviato in ascolto solo su `localhost` (127.0.0.1) anziché su tutte le interfacce di rete (`0.0.0.0`).
  2. Il firewall di Linux (`ufw`) blocca la porta TCP 8501.
* **Quick Fix:**
  1. Assicurarsi che nel comando o file di configurazione sia presente `--server.address 0.0.0.0`.
  2. Aprire la porta nel firewall:
     ```bash
     sudo ufw allow 8501/tcp
     sudo ufw reload
     ```

---
