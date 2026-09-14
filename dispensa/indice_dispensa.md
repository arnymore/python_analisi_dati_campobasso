# 📖 INDICE DETTAGLIATO DELLA DISPENSA PER LO STUDENTE
## Manuale Operativo: Python per l'Analisi Dati Aziendale
**Docente: Arnaldo Morena** | ITIS Campobasso | Corso di 22 Ore

---

### PRESENTAZIONE DEL MANUALE
* **Prefazione del Docente**: Perché Python è lo standard de facto per l'automazione aziendale e l'analisi dati.
* **Metodologia del Corso**: Approccio hands-on (80% pratica di laboratorio, 20% concetti teorici essenziali).
* **Guida all'Ambiente di Lavoro**: Installazione di Python, configurazione di VS Code / Jupyter, gestione dei Virtual Environment.
* **Il Caso Aziendale Unico**: Introduzione alla società commerciale di distribuzione IT e presentazione della struttura dati delle filiali.

---

### CAPITOLO 1: PYTHON OPERATIVO PER IL BUSINESS & AUTOMAZIONE
* **1.1 Fondamenti del Linguaggio e Tipi di Dato Primitivi**
  * 1.1.1 Variabili, costanti e convenzioni di denominazione PEP8.
  * 1.1.2 Stringhe, numeri interi, numeri in virgola mobile (float) e booleani.
  * 1.1.3 Casting esplicito e gestione dei problemi di conversione nei dati aziendali (virgole, simboli di valuta).
* **1.2 Collezioni Dati Native: Strutturare Informazioni Complesse**
  * 1.2.1 Liste: indicizzazione, slicing, mutabilità e metodi essenziali (`append`, `extend`, `insert`, `pop`).
  * 1.2.2 Tuple: collezioni immutabili e utilizzo nei record a sola lettura.
  * 1.2.3 Dizionari: mappatura chiave-valore, accesso sicuro con `.get()`, dizionari annidati per modellare tabelle.
  * 1.2.4 Set: gestione di insiemi unici ed eliminazione rapida di valori duplicati.
* **1.3 Controllo di Flusso e Logica Commerciale**
  * 1.3.1 Condizionali `if`, `elif`, `else` ed espressioni booleane composte (`and`, `or`, `not`).
  * 1.3.2 Cicli `for` e `while`: iterare su liste di transazioni e cataloghi.
  * 1.3.3 Funzioni di supporto all'iterazione: `range()`, `enumerate()`, `zip()`.
  * 1.3.4 List Comprehension e Dictionary Comprehension per trasformazioni compatte e ad alte prestazioni.
* **1.4 Modularità con le Funzioni**
  * 1.4.1 Definizione di funzioni con `def`, parametri posizionali, parametri con valori di default e keyword arguments.
  * 1.4.2 Valori di ritorno singoli e multipli (tuple return).
  * 1.4.3 Ambito delle variabili (scope locale vs globale) e docstring di documentazione.
  * 1.4.4 Creazione di funzioni di calcolo commerciale riutilizzabili (Sconto, IVA, Scorporo, Ricarico, Margine).
* **1.5 Manipolazione Avanzata delle Stringhe per la Pulizia Anagrafica**
  * 1.5.1 Metodi di stringa: `.strip()`, `.lower()`, `.upper()`, `.title()`, `.replace()`, `.split()`, `.join()`.
  * 1.5.2 Formattazione moderna con f-strings per reportistica testuale.
  * 1.5.3 Introduzione alle Espressioni Regolari (Regex con modulo `re`) per validazione codici fiscali, P.IVA ed email.
* **1.6 Laboratorio 1 Guidato: Esercizi ed Esempi Risolti**

---

### CAPITOLO 2: PANDAS - ANALISI E MANIPOLAZIONE DATAFRAME
* **2.1 Introduzione all'Architettura di Pandas**
  * 2.1.1 Dal foglio Excel al DataFrame: perché Pandas rivoluziona la produttività in azienda.
  * 2.1.2 Le due strutture portanti: Series (monodimensionale) e DataFrame (bidimensionale).
* **2.2 Ingestion Dati: Importare Fonti Eterogenee**
  * 2.2.1 Lettura file Excel con `pd.read_excel()`: gestione schede multiple, intestazioni complesse e range di celle.
  * 2.2.2 Lettura file CSV e delimitati con `pd.read_csv()`: separatori, decimali e codifica caratteri (UTF-8, Latin1).
* **2.3 Diagnostica, Ispezione e Metadati**
  * 2.3.1 Esplorare forma e tipologie: `df.shape`, `df.columns`, `df.dtypes`, `df.info()`.
  * 2.3.2 Visualizzare campioni: `df.head()`, `df.tail()`, `df.sample()`.
  * 2.3.3 Statistiche descrittive sintetiche: `df.describe()` su colonne numeriche e categoriche.
* **2.4 Indicizzazione, Selezione e Filtri di Dati**
  * 2.4.1 Selezione di singole e multiple colonne: Series vs DataFrame.
  * 2.4.2 Indicizzazione numerica per posizione: `.iloc[]`.
  * 2.4.3 Indicizzazione basata su etichette e booleana: `.loc[]`.
  * 2.4.4 Filtri logici avanzati con operatori vettorializzati (`&`, `|`, `~`).
  * 2.4.5 Metodi di selezione avanzata: `.isin()`, `.between()`, `.str.contains()`.
* **2.5 Vettorializzazione e Creazione di Nuove Colonne Calcolate**
  * 2.5.1 Operazioni aritmetiche vettoriali tra colonne (prezzo per quantità).
  * 2.5.2 Funzioni matematiche e arrotondamenti con Pandas e NumPy.
  * 2.5.3 Creazione di colonne categoriche condizionali (`np.where()`, `pd.cut()`).
* **2.6 Ordinamento, Ranking e Statistiche per Colonna**
  * 2.6.1 Ordinamento a singola e multipla chiave con `df.sort_values()`.
  * 2.6.2 Calcolo di percentili, quartili e misure di dispersione (varianza, deviazione standard).
  * 2.6.3 Conteggi di frequenza e distribuzioni relative con `df.value_counts()`.
* **2.7 Laboratorio 2 Guidato: Esercizi ed Esempi Risolti**

---

### CAPITOLO 3: DATA WRANGLING, PULIZIA E INTEGRAZIONE DATI
* **3.1 La Teoria del Data Cleaning: Affrontare il Dato Sporco Aziendale**
  * 3.1.1 Cause comuni di degrado della qualità dati nei gestionali aziendali.
  * 3.1.2 Tassonomia degli errori: duplicazioni, missing values, disallineamenti di formattazione, incoerenze logiche.
* **3.2 Gestione dei Record Duplicati**
  * 3.2.1 Identificazione duplicati con `df.duplicated()` su sottoinsiemi di colonne chiave.
  * 3.2.2 Rimozione sicura dei duplicati con `df.drop_duplicates()`.
* **3.3 Trattamento Professionale dei Valori Mancanti (Null/NaN)**
  * 3.3.1 Rilevazione e quantificazione: `isna()`, `notna()`, matrici di completezza.
  * 3.3.2 Strategie di cancellazione: quando è opportuno usare `dropna()`.
  * 3.3.3 Strategie di imputazione: sostituzione con costanti, media, mediana, o imputazione condizionale per gruppo.
* **3.4 Normalizzazione dei Campi Testuali e Categorie Merceologiche**
  * 3.4.1 Standardizzazione di codici identificativi e ragioni sociali.
  * 3.4.2 Mappatura di categorie disomogenee e correzione dei refusi con dizionari di trascodifica.
* **3.5 Il Problema delle Date: Da Formati Misti a Oggetti Datetime**
  * 3.5.1 Conversione con `pd.to_datetime()` e formati personalizzati (`strftime`/`strptime`).
  * 3.5.2 Gestione dei numeri seriali di data tipici di Microsoft Excel.
  * 3.5.3 Feature Engineering temporale: estrazione di Anno, Mese, Giorno della Settimana, Trimestre, Settimana dell'anno.
* **3.6 Integrazione Dati: Join e Merge tra Tabelle**
  * 3.6.1 Modello relazionale: tabelle dei fatti (vendite) e tabelle dimensionali (anagrafica clienti).
  * 3.6.2 Esecuzione di Left, Right, Inner e Outer Join con `pd.merge()`.
  * 3.6.3 Risoluzione dei conflitti sui nomi delle colonne (`suffixes`) e controllo di cardinalità.
* **3.7 Aggregazioni e Raggruppamenti con `groupby()`**
  * 3.7.1 Il paradigma Split-Apply-Combine.
  * 3.7.2 Aggregazioni singole e multiple con la funzione `.agg()`.
  * 3.7.3 Costruzione di Tabelle Pivot bidimensionali con `pd.pivot_table()`.
* **3.8 Laboratorio 3 Guidato: Esercizi ed Esempi Risolti**

---

### CAPITOLO 4: VISUALIZZAZIONE DATI E REPORTING DIREZIONALE
* **4.1 Principi di Data Storytelling ed Efficacia Visiva**
  * 4.1.1 Eliminare il disordine visivo (Chartjunk) e massimizzare il Data-to-Ink ratio.
  * 4.1.2 Scegliere il grafico corretto per ogni domanda di business.
* **4.2 Matplotlib: Il Motore Grafico di Base**
  * 4.2.1 Architettura orientata a oggetti: `Figure` e `Axes`.
  * 4.2.2 Grafici a barre verticali e orizzontali per confronti categorici (`ax.bar`, `ax.barh`).
  * 4.2.3 Grafici a linee per serie storiche e trend temporali (`ax.plot`).
  * 4.2.4 Personalizzazione di titoli, etichette degli assi, limiti, tick e griglie.
  * 4.2.5 Aggiunta di linee di riferimento (target di vendita, medie) e annotazioni puntuali.
* **4.3 Seaborn: Visualizzazioni Statistiche e Palette Moderne**
  * 4.3.1 Vantaggi di Seaborn nell'integrazione diretta con i DataFrame Pandas.
  * 4.3.2 Grafici a barre raggruppati con suddivisione per categoria (`hue`).
  * 4.3.3 Analisi delle distribuzioni e della dispersione: Istogrammi, KDE e Boxplot.
  * 4.3.4 Grafici a dispersione (Scatter Plot) per analisi delle correlazioni.
  * 4.3.5 Matrici di calore (Heatmap) con annotazioni per l'analisi incrociata Canale / Categoria.
* **4.4 Creazione di Layout Multi-Grafico (Executive Dashboards)**
  * 4.4.1 Costruzione di griglie 2x2 con `plt.subplots()`.
  * 4.4.2 Allineamento degli spazi e gestione del titolo generale (`suptitle`).
* **4.5 Esportazione Professionale**
  * 4.5.1 Salvataggio ad alta risoluzione (300 DPI) con `plt.savefig()`.
  * 4.5.2 Formati vettoriali (PDF, SVG) vs raster (PNG, JPEG).
* **4.6 Laboratorio 4 Guidato: Esercizi ed Esempi Risolti**

---

### CAPITOLO 5: AUTOMAZIONE DELLA PIPELINE ETL AZIENDALE
* **5.1 Progettare una Pipeline di Elaborazione Dati Industriale**
  * 5.1.1 Dal notebook interattivo al modulo Python eseguibile (.py).
  * 5.1.2 Modularità, robustezza e gestione degli imprevisti.
* **5.2 Interazione con il File System e Riconoscimento Automatico dei File**
  * 5.2.1 Percorsi portabili con i moduli `os` e `pathlib`.
  * 5.2.2 Scansione automatica di cartelle con pattern matching (`glob.glob`).
  * 5.2.3 Riconoscimento dinamico di nuovi file di filiale in arrivo.
* **5.3 Ingestion Massiva e Fusione di Dati Eterogenei**
  * 5.3.1 Lettura a blocchi e gestione controllata delle eccezioni `try/except`.
  * 5.3.2 Concatenazione verticale ed orizzontale con `pd.concat()`.
* **5.4 Implementazione del Data Quality Audit e Checksum**
  * 5.4.1 Tracciamento automatico dei record scartati, duplicati o corretti.
  * 5.4.2 Riconciliazione contabile dei totali prima e dopo la pulizia.
* **5.5 Logging Professionale vs Print Statement**
  * 5.5.1 Configurazione del modulo `logging` di Python.
  * 5.5.2 Scrittura simultanea dei log su console e file storico su disco.
* **5.6 Ottimizzazione del Formato di Output: Parquet ed Excel Multi-Scheda**
  * 5.6.1 Il formato Apache Parquet: struttura a colonne, compressione Snappy e velocità I/O.
  * 5.6.2 Generazione di report Excel multi-foglio arricchiti con formule e fogli pivot.
* **5.7 Esecuzione Batch e Parametrizzazione da Terminale (CLI con `argparse`)**
* **5.8 Laboratorio 5 Guidato: Script Completo `pipeline_etl.py`**

---

### CAPITOLO 6: DASHBOARD WEB INTERATTIVE CON STREAMLIT
* **6.1 Introduzione a Streamlit e Paradigma Low-Code Python**
  * 6.1.1 Come funziona Streamlit: ciclo di vita dell'applicazione ed esecuzione reattiva.
  * 6.1.2 Confronto tra Streamlit, PowerBI, Tableau e dashboard web tradizionali.
* **6.2 Struttura della Pagina e Componenti Grafici**
  * 6.2.1 Configurazione pagina (`st.set_page_config`) e layout responsive.
  * 6.2.2 Testi, titoli, markdown, badge informativi e immagini aziendali.
* **6.3 Caching dei Dati per Massimizzare le Prestazioni**
  * 6.3.1 Il decoratore `@st.cache_data`: memorizzare in RAM dataset pesanti ed evitare ricaricamenti continui.
* **6.4 Widget Interattivi e Pannello di Controllo (Sidebar)**
  * 6.4.1 Creazione della barra laterale (`st.sidebar`).
  * 6.4.2 Filtri a discesa singoli (`selectbox`) e multipli (`multiselect`).
  * 6.4.3 Selettore di date a calendario (`date_input`) e cursori numerici (`slider`).
  * 6.4.4 Logica di filtraggio dinamico del DataFrame Pandas in base all'input utente.
* **6.5 Layout Moderno: Colonne, Metriche e Schede Tematiche**
  * 6.5.1 Creazione di schede KPI con `st.columns()` e `st.metric()` (con indicatori di delta).
  * 6.5.2 Navigazione a schede orizzontali con `st.tabs()`.
  * 6.5.3 Pannelli richiudibili con `st.expander()`.
* **6.6 Visualizzazione Dati Dinamica nella Dashboard**
  * 6.6.1 Rendering di grafici Matplotlib/Seaborn con `st.pyplot()`.
  * 6.6.2 Tabelle interattive ricercabili e ordinabili con `st.dataframe()` e formattazione monetaria.
* **6.7 Funzionalità Avanzate: Ricerca Testuale, Export CSV e Simulatore What-If**
  * 6.7.1 Casella di ricerca full-text integrata.
  * 6.7.2 Creazione del pulsante di download dati con `st.download_button()`.
  * 6.7.3 Costruzione di un simulatore interattivo di scenario commerciale con calcolo in tempo reale di variazioni di margine e volume.
* **6.8 Laboratorio 6 Guidato: Sviluppo della Web App Aziendale**

---

### CAPITOLO 7: DEPLOY E MESSA IN PRODUZIONE SU SERVER LINUX
* **7.1 Dal Laptop al Server Aziendale**
  * 7.1.1 Concetti di server Linux, connessione remota SSH e gestione utenti sicuri.
  * 7.1.2 Differenze tra esecuzione manuale in terminale ed esecuzione come servizio di sistema continuo.
* **7.2 Preparazione dell'Ambiente di Esecuzione**
  * 7.2.1 Creazione del Virtual Environment dedicato sul server.
  * 7.2.2 Installazione controllata delle dipendenze con `pip install -r requirements.txt`.
* **7.3 Configurazione di Systemd come Gestore di Servizi**
  * 7.3.1 Anatomia di un Unit File di Systemd (`.service`): sezioni `[Unit]`, `[Service]`, `[Install]`.
  * 7.3.2 Configurazione dell'avvio automatico di Streamlit all'accensione del server (Boot).
  * 7.3.3 Politiche di riavvio automatico in caso di crash improvviso (`Restart=always`).
* **7.4 Comandi Operativi di Amministrazione con `systemctl`**
  * 7.4.1 Avvio, arresto, riavvio e controllo dello stato operativo del servizio.
* **7.5 Diagnostica e Consultazione dei Log con `journalctl`**
  * 7.5.1 Visualizzazione dei log storici e monitoraggio dei log in tempo reale (`journalctl -f`).
* **7.6 Cenni di Messa in Sicurezza e Reverse Proxy**
  * 7.6.1 Esporre l'applicazione su porta standard 80/443 con Nginx Reverse Proxy.
  * 7.6.2 Configurazione di base del firewall Linux (UFW).
* **7.7 Laboratorio 7 Guidato: Deploy Completo del Servizio Linux**

---

### CAPITOLO 8: PROJECT WORK FINALE & CASO AZIENDALE COMPLETO
* **8.1 La Sfida Finale: Espansione Commerciale con la Filiale di Napoli**
* **8.2 Traccia di Lavoro e Specifiche Tecniche per lo Studente**
* **8.3 Guida all'Integrazione Nazionale a 4 Filiali**
* **8.4 Guida all'Analisi di Business e alla Redazione del Report Strategico**
* **8.5 Criteri e Griglia di Valutazione Ufficiale**
* **8.6 Codice di Riferimento e Commento ai Risultati**

---

### APPENDICI
* **Appendice A**: Tabella di Equivalenza Operativa tra Funzioni Excel e Metodi Pandas.
* **Appendice B**: Cheat-Sheet di Sintassi Rapida (Python, Pandas, Seaborn, Streamlit, Linux).
* **Appendice C**: Glossario dei Termini di Data Engineering e Business Analytics.
