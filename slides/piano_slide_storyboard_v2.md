# 🎬 PIANO SLIDE & STORYBOARD V2 (75 SLIDE OTTIMIZZATE)
## Corso: Laboratorio Python + Analisi Dati (22 Ore)
**Docente: Arnaldo Morena** | ITIS Campobasso  
**Revisione Didattica:** Versione 2.0 (Ottimizzazione densità, +30% tempo dedicato ai laboratori, Modulo 7 in Live Demo)

---

## 📊 RIEPILOGO STRUTTURA & RIPARTIZIONE SLIDE

| Modulo Didattico | Durata | N. Slide V1 | N. Slide V2 | Range Slide V2 | Modalità Didattica & Focus Pedagogico |
|:---|:---:|:---:|:---:|:---:|:---|
| **Modulo 1 – Python Operativo** | 2h | 12 | **8** | Slide 1 – 8 | Laboratorio hands-on: tipi, strutture native, funzioni commerciali e normalizzazione stringhe. |
| **Modulo 2 – Pandas Fondamenti** | 4h | 18 | **14** | Slide 9 – 22 | Laboratorio hands-on: vettorializzazione, `.copy()`, indexing `.loc`/`.iloc`, filtri booleani, Top Deals. |
| **Modulo 3 – Data Wrangling** | 3h | 16 | **12** | Slide 23 – 34 | Laboratorio hands-on: deduplica, date miste, imputazione semplice (`fillna`), merge e validazione integrità. |
| **Modulo 4 – Visualizzazione & Report**| 3h | 14 | **11** | Slide 35 – 45 | Laboratorio hands-on: Matplotlib + Seaborn, trend mensile, boxplot sconti, heatmap e dashboard 2x2. |
| **Modulo 5 – Automazione Pipeline** | 2h | 10 | **8** | Slide 46 – 53 | Laboratorio hands-on: scansione `glob` con filtro `~$`, trasformazione modulare, Parquet ed Excel multi-sheet. |
| **Modulo 6 – Dashboard Streamlit** | 4h | 16 | **13** | Slide 54 – 66 | Laboratorio hands-on: flusso reattivo, sidebar filtri, metric cards, download CSV e simulatore What-If. |
| **Modulo 7 – Deploy Server Linux** | 1h | 8 | **4** | Slide 67 – 70 | **Live Demo guidata (Show-and-Tell)**: Systemd service, auto-restart, journalctl e Nginx. |
| **Project Work Finale & Chiusura** | 3h | 6 | **5** | Slide 71 – 75 | Project Work autonomo/guidato: filiale Napoli, pipeline consolidata, benchmark e debriefing. |
| **TOTALE** | **22h** | **100** | **75** | **Slide 1 – 75** | **80% Laboratorio Hands-on / 20% Teoria Operativa** |

---

## 🗓️ NUOVA AGENDA DOCENTE (TIMELINE 22 ORE COMPLESSIVE)

* **Sessione 1 (Ore 1 – 4, 4h):**
  * *Ore 1-2:* Modulo 1 – Python Operativo (Slide 1 – 8 ➔ **Lab 1**: calcolo KPI e pulizia stringhe).
  * *Ore 3-4:* Modulo 2 – Pandas Parte 1: Ingestion, `.copy()` e Indicizzazione (Slide 9 – 15 ➔ **Lab 2.1 & 2.2**).
* **Sessione 2 (Ore 5 – 8, 4h):**
  * *Ore 5-6:* Modulo 2 – Pandas Parte 2: Filtri, Calcoli e Ordinamento (Slide 16 – 22 ➔ **Lab 2.3 & 2.4**).
  * *Ore 7-8:* Modulo 3 – Data Wrangling Parte 1: Deduplica, Date e Stringhe (Slide 23 – 28 ➔ **Lab 3.1, 3.2, 3.3**).
* **Sessione 3 (Ore 9 – 12, 4h):**
  * *Ore 9:* Modulo 3 – Data Wrangling Parte 2: Imputazione `fillna()` e Merge con Controllo Integrità (Slide 29 – 34 ➔ **Lab 3.4 & 3.5**).
  * *Ore 10-12:* Modulo 4 – Visualizzazione Dati e Dashboard 2x2 (Slide 35 – 45 ➔ **Lab 4 completo**).
* **Sessione 4 (Ore 13 – 16, 4h):**
  * *Ore 13-14:* Modulo 5 – Automazione Pipeline ETL, Filtro `~$` e Storage Parquet (Slide 46 – 53 ➔ **Lab 5 batch**).
  * *Ore 15-16:* Modulo 6 – Streamlit Parte 1: Flusso Reattivo, Caching e KPI Cards (Slide 54 – 60 ➔ **Lab 6 starter**).
* **Sessione 5 (Ore 17 – 20, 4h):**
  * *Ore 17-18:* Modulo 6 – Streamlit Parte 2: Tabs, Simulatore What-If ed Export (Slide 61 – 66 ➔ **Lab 6 completo**).
  * *Ore 19:* Modulo 7 – Deploy Linux in **Live Demo guidata** (Slide 67 – 70 ➔ Configurazione Systemd a schermo).
  * *Ore 20:* Project Work – Lancio Traccia e Ingestion Filiale Napoli (Slide 71 – 72 ➔ **Avvio Project Work**).
* **Sessione 6 (Ore 21 – 22, 2h):**
  * *Ore 21-22:* Project Work – Consolidamento Nazionale, Benchmark, Soluzione Docente e Chiusura (Slide 73 – 75).

---

## 📘 MODULO 1: PYTHON OPERATIVO PER IL BUSINESS (2 Ore) – [Slide 1 – 8]

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **1** | Benvenuti & Il Caso Aziendale Unico | Obiettivi del corso 80/20, presentazione rete commerciale nazionale (Roma, Milano, Torino, Napoli), problemi dei fogli Excel disallineati. | Esplorazione cartella dati e file grezzo `roma.xlsx`. | Setup ambiente locale e verifica Python 3.12. |
| **2** | Tipi Primitivi e Conversioni di Business | Numeri, stringhe, booleani; conversione di tipi (`float()`, `int()`, `str()`), rimozione simboli valuta e virgole decimali. | Cast e pulizia rapida di stringhe prezzo in Python. | Normalizzazione tipi variabili isolate. |
| **3** | Collezioni Native: Liste e Dizionari | Liste indicizzate, tuple immutabili, dizionari chiave-valore `.get()`, rappresentazione di righe tabellari in memoria. | Costruzione del dizionario di una transazione commerciale. | Creazione schemi anagrafici con dizionari. |
| **4** | Controllo di Flusso e Iterazioni | Costrutti `if/elif/else`, cicli `for` su elenchi di vendite, accumulo progressivo di totali e medie. | Calcolo fatturato totale carrello con ciclo `for`. | Iterazione su lista transazioni d'ordine. |
| **5** | List Comprehension Operativa | Sintassi compatta ed efficiente `[f(x) for x in lista if cond]`, trasformazioni e filtri istantanei. | Estrazione degli ordini con importo > 1000€. | Trasformazione lista imponibili netti. |
| **6** | Funzioni Commerciali Riutilizzabili | Definizione `def`, parametri posizionali e di default, ritorno strutturato in dizionario (`imponibile`, `sconto`, `iva`, `totale`). | Scrittura e test della funzione `calcola_totale_riga()`. | **Lab 1 - Es. 1.1**: Funzione calcolo riga ordine. |
| **7** | Pulizia e Normalizzazione Testi | Metodi `.strip()`, `.lower()`, `.title()`, `.replace()`, `.split()`, correzione spazi multipli e acronimi societari (Srl, SpA). | Pulizia dinamica di ragioni sociali grezze. | **Lab 1 - Es. 1.3**: Normalizzazione nomi clienti. |
| **8** | Aggregazioni Native Senza Librerie | Raggruppamento con dizionari accumulatore per categoria, calcolo quantità e volumi di vendita complessivi. | Aggregatore vendite per categoria prodotto. | **Lab 1 - Es. 1.4**: Aggregazione nativa carrello. |

---

## 📗 MODULO 2: PANDAS - FONDAMENTI E MANIPOLAZIONE DATAFRAME (4 Ore) – [Slide 9 – 22]

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **9** | Dal Foglio Excel al DataFrame Pandas | Perché Pandas, architettura tabellare (Series 1D vs DataFrame 2D), caricamento Excel con `pd.read_excel()` e selezione fogli. | Caricamento live di `dataset/raw/roma.xlsx`. | **Lab 2 - Es. 2.1 (Parte 1)**: Ingestion dati Roma. |
| **10** | Ispezione e Diagnostica Strutturale | `.info()`, `.describe()`, `.shape`, `.columns`, `.dtypes`, `.head()`, identificazione tipi errati e consistenza dati. | Diagnostica rapida DataFrame e statistiche di base. | **Lab 2 - Es. 2.1 (Parte 2)**: Diagnostica colonne. |
| **11** | Selezione Colonne, Viste e Copie (`.copy()`) | Selezione `df['col']` vs `df[['c1', 'c2']]`; View vs Copy in Pandas, uso esplicito di `.copy()` e prevenzione del `SettingWithCopyWarning`. | Dimostrazione pratica dell'avviso `SettingWithCopyWarning` e risoluzione con `.copy()`. | Estrazione sottoinsiemi sicuri con `.copy()`. |
| **12** | Indicizzazione: `.iloc[]` vs `.loc[]` | `.iloc` (posizionale per numeri di riga/colonna) vs `.loc` (basato su etichette e condizioni logiche). | Estrazione blocchi di dati con slicing comparato. | **Lab 2 - Es. 2.2**: Estrazione slice `.iloc` e `.loc`. |
| **13** | Filtri Booleani e Maschere Logiche | Maschere logiche (`df['Canale'] == 'E-commerce'`), conteggio occorrenze, estrazione record filtrati. | Filtro vendite canale digitale. | **Lab 2 - Es. 2.3 (Parte 1)**: Filtro canale vendita. |
| **14** | Condizioni Multiple: AND (`&`), OR (`\|`), NOT (`~`) | Obbligatorietà delle parentesi tonde `(cond1) & (cond2)`, filtro congiunto su volumi e sconti applicati. | Estrazione ordini con Quantità >= 10 e Sconto > 0. | **Lab 2 - Es. 2.3 (Parte 2)**: Filtri booleani combinati. |
| **15** | Filtri Avanzati: `.isin()` e `.str.contains()` | Selezione di elenchi con `.isin(['Roma', 'Milano'])`, ricerca testuale flessibile con `.str.contains(..., case=False)`. | Ricerca articoli contenenti "Server" o "Laptop". | Filtri su elenchi prodotti e categorie. |
| **16** | Vettorializzazione e Colonne Calcolate | Calcolo senza cicli for: `Fatturato_Lordo = Quantita * Prezzo_Unitario`, efficienza vettoriale di Pandas. | Calcolo immediato dell'imponibile su 1.200 righe. | **Lab 2 - Es. 2.4 (Parte 1)**: Calcolo lordo vettoriale. |
| **17** | Cast Numerico Sicuro con `pd.to_numeric` | Gestione di valori sporchi con `errors='coerce'`, conversione automatica di stringhe anomale in `NaN`. | Pulizia vettoriale prezzi contenenti caratteri spuri. | Bonifica preliminare colonna prezzi. |
| **18** | Calcolo Sconti, Margini e Fatturato Netto | Calcolo valore sconto in euro, applicazione aliquote IVA, determinazione del `Fatturato_Netto` finale su DataFrame espliciti. | Calcolo colonne economiche complete. | Completamento colonne economiche riga. |
| **19** | Ordinamento Dati con `.sort_values()` | Ordinamento per singola e multipla colonna (`ascending=[True, False]`), identificazione Top Deals commerciali. | Estrazione dei 10 ordini con maggior fatturato netto. | **Lab 2 - Es. 2.4 (Parte 2)**: Top 10 Deals Roma. |
| **20** | Statistiche Descrittive e Percentili | `.sum()`, `.mean()`, `.median()`, `.quantile()`, misure di dispersione e analisi ticket medio. | Calcolo KPI generali di filiale. | Calcolo mediane e metriche di vendita. |
| **21** | Analisi Frequenze con `.value_counts()` | Distribuzione ordini per canale e categoria, frequenze relative percentuali (`normalize=True`). | Calcolo quote percentuali per canale commerciale. | Calcolo market share interno per prodotto. |
| **22** | Esportazione Dati Puliti | `.to_excel()`, `.to_parquet()`, salvataggio formati standard senza indice superfluo (`index=False`). | Export del dataset filtrato in formato Excel e Parquet. | Salvataggio output elaborazione Modulo 2. |

---

## 📙 MODULO 3: DATA WRANGLING, PULIZIA E INTEGRAZIONE (3 Ore) – [Slide 23 – 34]

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **23** | Anatomia del 'Dirty Data' Aziendale | Cause reali dei dati sporchi, i 4 pilastri del wrangling: duplicati, formati data, valori nulli, anomalie stringa. | Ispezione anomalie reali su `roma.xlsx`. | Identificazione anomalie nel dataset. |
| **24** | Rilevamento ed Eliminazione Duplicati | `df.duplicated(subset=...)`, verifica duplicati esatti vs duplicati su chiave, rimozione con `.drop_duplicates()`. | Eliminazione di 48 transazioni duplicate. | **Lab 3 - Es. 3.1**: Deduplica del dataset Roma. |
| **25** | Standardizzazione Testi e Categorie | Rimozione spazi parassiti `.str.strip()`, maiuscole `.str.upper()`, dizionari di trascodifica categorie (`HW` ➔ `Hardware`). | Normalizzazione ragioni sociali e categorie. | **Lab 3 - Es. 3.2**: Pulizia codici e categorie. |
| **26** | Il Rompicapo delle Date Eterogenee | Date ISO (`2024-03-15`), formati IT (`15/03/2024`), date testuali (`15-Mar-2024`) e seriali Excel (`45506`). | Analisi dei formati disallineati nel foglio Excel. | Ispezione colonna `Data_Vendita`. |
| **27** | Parsing Robusto con `pd.to_datetime` | Funzione custom di parsing flessibile, conversione seriali Excel (base 1899-12-30) a oggetti `datetime64`. | Esecuzione parsing date miste (100% successo). | **Lab 3 - Es. 3.3 (Parte 1)**: Parsing date eterogenee. |
| **28** | Feature Engineering Temporale | Estrazione componenti temporali: `.dt.year`, `.dt.month`, `.dt.strftime('%B')`, `.dt.to_period('Q')` per i trimestri. | Creazione colonne Mese, Nome Mese e Trimestre. | **Lab 3 - Es. 3.3 (Parte 2)**: Creazione feature date. |
| **29** | Diagnosi dei Valori Mancanti (`NaN`) | Rilevazione nulli con `.isna().sum()`, quantificazione percentuale per colonna, impatto sui calcoli economici. | Mappa riassuntiva dei valori mancanti. | Ispezione valori nulli su tutte le colonne. |
| **30** | Trattamento Nulli: Imputazione Semplice con `fillna()` | **Percorso Principale:** Imputazione robusta con mediana o media globale (`df['Prezzo'].fillna(df['Prezzo'].median())`); *Nota Extra Didattica:* accenno all'imputazione condizionale per gruppo con `transform()` disponibile nella dispensa di approfondimento. | Applicazione `fillna()` con mediana e confronto impatto. | **Lab 3 - Es. 3.4**: Imputazione e ricalcolo netto. |
| **31** | Integrazione Relazionale: Concetti di Merge | Modello Fatti-Dimensioni, tipi di Join (Left, Inner, Outer), chiave primaria e chiave esterna (`Codice_Cliente`). | Diagramma relazionale Vendite ➔ Anagrafica Clienti. | Comprensione relazioni tra tabelle. |
| **32** | Esecuzione Merge & Controllo Integrità | Sintassi `pd.merge(how='left')`, validazione unicità con `validate='many_to_one'`, diagnostica join con `indicator=True`, controllo `df.shape` pre/post join per prevenire duplicazioni. | Esecuzione merge anagrafica e verifica conteggio righe. | **Lab 3 - Es. 3.5 (Parte 1)**: Merge anagrafica clienti con verifica integrità. |
| **33** | Aggregazioni Strategiche con `groupby()` | Paradigma Split-Apply-Combine, raggruppamento multi-livello per Settore cliente e Categoria prodotto. | Calcolo fatturato e sconti per settore merceologico. | Raggruppamento per settore e canale. |
| **34** | Metriche Multiple Avanzate con `.agg()` | Costruzione del report direzionale con `.agg(Fatturato=('Netto', 'sum'), Ordini=('ID', 'count'), Sconto=('Sconto', 'mean'))`. | Creazione del report per settore ordinato per fatturato. | **Lab 3 - Es. 3.5 (Parte 2)**: Report avanzato `.agg`. |

---

## 📊 MODULO 4: VISUALIZZAZIONE DATI E REPORTING DIREZIONALE (3 Ore) – [Slide 35 – 45]

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **35** | Principi di Data Storytelling Aziendale | Scelta della visualizzazione corretta, rimozione del disordine (chartjunk), focus sui KPI direzionali. | Confronto tra grafici poco chiari e visualizzazioni efficaci. | Analisi critica visualizzazioni. |
| **36** | Anatomia di Matplotlib: Figure e Axes | Architettura orientata a oggetti `fig, ax = plt.subplots()`, canvas, assi, etichette e griglie. | Creazione del canvas Matplotlib con layout pulito. | Inizializzazione struttura Figure/Axes. |
| **37** | Bar Chart Orizzontale con Valori sui Dati | Grafico a barre orizzontali `ax.barh()`, formattazione k€, inserimento etichette valori direttamente sulle barre. | Grafico Top 8 Clienti per fatturato netto. | **Lab 4 - Es. 4.1**: Bar chart orizzontale Top Clienti. |
| **38** | Serie Temporali: Trend Mensile e Target | Grafico a linee con marker `ax.plot()`, aggiunta linea di media annuale con `ax.axhline()`, etichette mesi (Gen..Dic). | Andamento mensile delle vendite con target budget. | **Lab 4 - Es. 4.2**: Line chart trend vendite mensili. |
| **39** | Seaborn: Statistica e Design Professionale | Integrazione con DataFrame Pandas, impostazione stili (`whitegrid`) e palette cromatiche aziendali. | Confronto rapido Matplotlib puro vs stile Seaborn. | Configurazione palette Seaborn. |
| **40** | Analisi Distribuzioni e Outlier: Boxplot | Anatomia del Boxplot (mediana, quartili, IQR, outlier), analisi sconti applicati per canale di vendita con `sns.boxplot`. | Individuazione canali con eccessiva dispersione di sconti. | Boxplot distribuzione sconti per canale. |
| **41** | Heatmap Matrice Canale vs Categoria | Tabella pivot bidimensionale trasformata in matrice di calore con `sns.heatmap()`, annotazioni numeriche formattate. | Mappa termica Fatturato per Canale x Categoria. | **Lab 4 - Es. 4.3**: Costruzione Heatmap vendite. |
| **42** | Layout Multi-Plot Avanzato (Subplots) | Costruzione di griglie 2x2 con `plt.subplots(2, 2, figsize=(16, 10))`, gestione spazi e assi individuali. | Composizione della griglia multi-grafico. | **Lab 4 - Es. 4.4 (Parte 1)**: Griglia multi-plot 2x2. |
| **43** | Executive Dashboard 2x2 per il CdA | Assemblaggio completo dei 4 grafici direzionali (Trend, Categorie, Sconti, Heatmap) con `suptitle`. | Generazione della dashboard unificata per la direzione. | **Lab 4 - Es. 4.4 (Parte 2)**: Assemblaggio Executive Report. |
| **44** | Esportazione ad Alta Risoluzione | Salvataggio con `plt.savefig()` a 300 DPI in formato PNG/PDF per stampa e presentazioni direzionali. | Export automatico del file `executive_report.png`. | Salvataggio grafici in `dataset/generated/`. |
| **45** | Recap & Best Practice Visualizzazione | Checklist di qualità: titoli auto-esplicativi, unità di misura, contrasto cromatico, formati vettoriali. | Code review e discussione sui grafici prodotti. | Rifinitura estetica dei grafici studenti. |

---

## ⚙️ MODULO 5: AUTOMAZIONE PIPELINE ETL (2 Ore) – [Slide 46 – 53]

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **46** | Architettura della Pipeline ETL Aziendale | Flusso Extract-Transform-Load, passaggio da script interattivo a modulo batch automatico e robusto. | Diagramma di flusso della pipeline di filiale. | Progettazione flusso ETL modulare. |
| **47** | Scansione Dinamica & Filtro File Temporanei | Ricerca file regionali `glob.glob('dataset/raw/*.xlsx')`, gestione percorsi con `os.path`, filtro ed esclusione attiva dei file lock/temporanei di Excel (`~$*.xlsx`). | Riconoscimento dinamico ed esclusione file lock temporanei. | **Lab 5 - Fase 1**: Ingestion automatica multi-file. |
| **48** | Ingestion Massiva e Concatenazione | Lettura ciclica con gestione eccezioni `try/except`, unione verticale con `pd.concat()` per vendite e anagrafiche. | Fusione automatica di 3 filiali in un unico DataFrame. | Concatenazione master dataset. |
| **49** | Centralizzazione della Trasformazione | Incapsulamento delle regole di wrangling in `trasforma_dataset()`, deduplica, parsing date e imputazioni automatiche. | Esecuzione del cleaning centralizzato su tutto il master. | **Lab 5 - Fase 2**: Funzione di trasformazione. |
| **50** | Logging Strutturato vs Print Statement | Configurazione del modulo standard `logging`, livelli (INFO, WARNING, ERROR), timestamp e monitoraggio esecuzione. | Tracciamento eventi e metriche della pipeline su console. | Aggiunta log strutturati alla pipeline. |
| **51** | Storage Ottimizzato in Apache Parquet | Perché Parquet per l'analytics: archiviazione a colonna, compressione Snappy, velocità di caricamento 10x per Streamlit. | Confronto peso file e benchmark lettura Parquet vs CSV. | **Lab 5 - Fase 3 (Parte 1)**: Export Parquet compresso. |
| **52** | Generazione Report Excel Multi-Foglio | Creazione automatica di `report_direzionale_consolidato.xlsx` con fogli di dettaglio e schede KPI per filiale e settore. | Generazione e apertura del report Excel multi-scheda. | **Lab 5 - Fase 3 (Parte 2)**: Export Excel direzionale. |
| **53** | Esecuzione Batch da Terminale (CLI) | Integrazione con `argparse`, parametri `--input-dir` e `--output-dir`, esecuzione end-to-end con un solo comando. | Esecuzione da terminale della pipeline completa. | Esecuzione autonoma della pipeline ETL. |

---

## 💻 MODULO 6: DASHBOARD INTERATTIVE CON STREAMLIT (4 Ore) – [Slide 54 – 66]

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **54** | Architettura Reattiva di Streamlit & Pure Python | Paradigma reattivo: esecuzione top-to-bottom ad ogni interazione dell'utente con i widget; vantaggi vs BI tradizionali, setup layout wide. | Avvio della prima applicazione Streamlit locale e test reattività. | Configurazione iniziale Web App. |
| **55** | Caching ad Alte Prestazioni con `@st.cache_data` | Memorizzazione in RAM del dataset Parquet, prevenzione dei ricaricamenti inutili, invalidazione e TTL. | Benchmark prestazioni con/senza decoratore di cache. | Applicazione caching su caricamento Parquet. |
| **56** | Sidebar & Controlli Utente Dinamici | Barra laterale `st.sidebar`, filtri multi-selezione `st.multiselect()` per filiali, categorie e canali distributivi. | Creazione del pannello filtri interattivo. | **Lab 6 - Es. 6.1 (Parte 1)**: Costruzione sidebar filtri. |
| **57** | Filtri Temporali con `st.date_input` | Selettore a calendario con range date (min/max), filtraggio dinamico del DataFrame per periodo di vendita. | Filtraggio temporale dinamico dei dati. | **Lab 6 - Es. 6.1 (Parte 2)**: Filtro per intervallo date. |
| **58** | Barra Superiore dei KPI con `st.metric` | Suddivisione layout con `st.columns(5)`, card di riepilogo: Fatturato Netto, Ordini, Ticket Medio, Sconto Medio, Pezzi. | Costruzione della barra KPI con formattazione euro. | **Lab 6 - Es. 6.2**: Creazione 5 metric cards. |
| **59** | Organizzazione a Schede con `st.tabs` | Creazione di 4 schede tematiche (Trend, Clienti, What-If, Dati), layout pulito e navigazione moderna. | Strutturazione dell'interfaccia in schede orizzontali. | Implementazione schede con `st.tabs`. |
| **60** | Tab 1: Trend Temporale & Performance Categorie | Rendering di grafici Matplotlib/Seaborn con `st.pyplot()`, trend mensile multi-filiale e vendite per categoria. | Visualizzazione grafici analitici reattivi ai filtri. | Rendering grafici analitici in Tab 1. |
| **61** | Tab 2: Ranking Top Clienti & Settori | Tabelle formattate con `st.dataframe()` e `style.format()`, grafico a torta/ciambella quote di mercato settoriali. | Tabella Top 10 Clienti con ordinamento interattivo. | Visualizzazione ranking e quote in Tab 2. |
| **62** | Motore di Ricerca Full-Text Interno | Campo `st.text_input()` con ricerca istantanea multi-campo su clienti, prodotti e ID transazione. | Ricerca cliente in tempo reale nel database master. | Implementazione casella di ricerca. |
| **63** | Esportazione Dati per l'Utente: `st.download_button` | Creazione buffer CSV in memoria (`.to_csv().encode('utf-8')`), download immediato dei record filtrati. | Download istantaneo del report CSV filtrato. | **Lab 6 - Es. 6.3**: Pulsante download CSV. |
| **64** | Tab 3: Simulatore di Scenari ("What-If Analysis") | Modello decisionale interattivo: slider per variazione volumi (+/- 50%) e sconti (+/- 15%), ricalcolo del margine. | Simulazione live dell'impatto di una politica sconti. | Costruzione del simulatore commerciale. |
| **65** | Indicatori Visivi e CSS Personalizzato | Iniezione CSS personalizzato con `st.markdown()`, box informativi `st.info()`, `st.success()`, badge di stato. | Personalizzazione grafica professionale dell'applicazione. | Rifinitura estetica e layout della dashboard. |
| **66** | Collaudo End-to-End della Dashboard | Test incrociato filtri, reattività, assenza di errori runtime, verifica coerenza contabile dei totali. | Dimostrazione dell'applicazione completa in esecuzione. | Collaudo finale da parte degli studenti. |

---

## 🚀 MODULO 7: DEPLOY SU SERVER LINUX & PRODUZIONE (1 Ora) – [Slide 67 – 70]
> **MODALITÀ DIDATTICA ESCLUSIVA: LIVE DEMO GUIDATA (SHOW-AND-TELL 100% PRATICO)**

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **67** | Dal Laptop alla Produzione 24/7 | Perché il deploy su server: centralizzazione dati, disponibilità continua, sicurezza; architettura Demone ➔ Systemd ➔ Nginx. | Connessione SSH al server Linux e panoramica ambiente. | **Live Demo guidata**: Osservazione e consultazione `guida_deploy.md`. |
| **68** | Creazione del Servizio Demone con Systemd | Struttura del file unit `/etc/systemd/system/dashboard_vendite.service`, sezioni `[Unit]`, `[Service]` (User, ExecStart, Restart=always). | Creazione a schermo del file `.service` con `setup_service.sh`. | **Live Demo guidata**: Provisioning file systemd service. |
| **69** | Amministrazione del Servizio con `systemctl` | Comandi essenziali: `systemctl daemon-reload`, `enable` (boot automatico), `start`, `status`, `restart`, `stop`. | Avvio e verifica stato attivo (`running`) del servizio. | **Live Demo guidata**: Gestione ciclo di vita servizio. |
| **70** | Monitoraggio Log con `journalctl` & Cenni Nginx | Diagnostica log in tempo reale `journalctl -u dashboard_vendite.service -f`, reverse proxy Nginx su porta 80, firewall UFW. | Simulazione riavvio per crash e ispezione log in diretta. | **Live Demo guidata**: Consultazione log di produzione. |

---

## 🏆 PROJECT WORK FINALE & CHIUSURA CORSO (3 Ore) – [Slide 71 – 75]

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **71** | Business Case Finale: Espansione Filiale Napoli | Scenario: Ingestion della nuova sede di Napoli (`napoli_project_work.xlsx`), obiettivi di consolidamento a 4 filiali e quesiti di business. | Presentazione dataset Napoli e traccia ufficiale d'esame. | **Project Work**: Ingestion dataset Napoli. |
| **72** | Specifiche Tecniche & Rubrica di Valutazione | I 4 deliverable: 1. Cleaning; 2. Merge e Consolidamento Parquet; 3. Risposta KPI; 4. Grafici di Benchmark; criteri di voto (100pt). | Chiarimento requisiti e standard di consegna. | **Project Work**: Sviluppo pipeline a 4 filiali. |
| **73** | Sessione Operativa Guidata (Hands-On) | Lavoro autonomo / a coppie degli studenti sullo script finale, supporto personalizzato del docente e troubleshooting. | Affiancamento e revisione codice in tempo reale. | **Project Work**: Sviluppo script e grafici PNG. |
| **74** | Presentazione Risultati & Analisi Benchmark | Esposizione dei team: quote filiali (Milano 32.7%, Roma 25.1%, Napoli 23.4%, Torino 18.8%), insight commerciali su Napoli. | Conduzione tavola rotonda e confronto insight. | Presentazione report e metriche scoperte. |
| **75** | Soluzione Ufficiale Docente & Conclusioni | Presentazione codice di riferimento `soluzione_project_work.py`, recap competenze acquisite, consegna attestati e prossimi passi. | Esecuzione live soluzione docente e chiusura corso. | Consegna kit didattico completo del corso. |
