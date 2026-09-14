# 🎬 PIANO SLIDE & STORYBOARD COMPLETO (100 SLIDE)
## Corso: Laboratorio Python + Analisi Dati (22 Ore)
**Docente: Arnaldo Morena** | ITIS Campobasso

---

### STRUTTURA DEL CORSO & RIPARTIZIONE SLIDE
* **Modulo 1 – Python Operativo per l'Analisi Dati** (2h) ➔ Slide 1 – 12 (12 slide)
* **Modulo 2 – Pandas: Fondamenti e Manipolazione Dati** (4h) ➔ Slide 13 – 30 (18 slide)
* **Modulo 3 – Data Wrangling, Pulizia e Integrazione** (3h) ➔ Slide 31 – 46 (16 slide)
* **Modulo 4 – Visualizzazione Dati e Reporting** (3h) ➔ Slide 47 – 60 (14 slide)
* **Modulo 5 – Automazione Pipeline ETL** (2h) ➔ Slide 61 – 70 (10 slide)
* **Modulo 6 – Dashboard Interattive con Streamlit** (4h) ➔ Slide 71 – 86 (16 slide)
* **Modulo 7 – Deploy su Server Linux & Produzione** (1h) ➔ Slide 87 – 94 (8 slide)
* **Project Work Finale & Chiusura Corso** (3h) ➔ Slide 95 – 100 (6 slide)

---

## 📘 MODULO 1: PYTHON OPERATIVO PER L'ANALISI DATI (2 Ore)

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **1** | Benvenuti al Laboratorio Python + Analisi Dati | Obiettivi del corso, metodologia pratica 80/20, presentazione docente Arnaldo Morena, regole d'aula e repository. | Tour del repository GitHub/locale. | Setup ambiente locale e test Python. |
| **2** | Il Caso Aziendale Unico | Presentazione della rete commerciale (filiali Roma, Milano, Torino, Napoli), problemi aziendali reali (fogli Excel disomogenei, perdite di tempo). | Apertura dei file Excel grezzi. | Ispezione visiva di `roma.xlsx`. |
| **3** | Variabili e Tipi di Dato per il Business | Stringhe, interi, float, booleani; conversione di tipi (`int()`, `float()`, `str()`), gestione errori di cast. | REPL Python: cast di prezzi con virgole e simboli. | Conversione tipi su variabili singole. |
| **4** | Liste e Tuple: Gestire Vettori di Dati | Indicizzazione da 0, slicing `[start:end]`, metodi `.append()`, `.extend()`, `.pop()`, immutabilità delle tuple. | Creazione dinamica di una lista transazioni. | Manipolazione lista prezzi. |
| **5** | Dizionari: La Struttura Chiave-Valore | Coppie chiave-valore, accesso `.get()`, aggiunta e aggiornamento chiavi, annidamento dati (tabelle in memoria). | Rappresentare una riga d'ordine come dizionario. | Creazione schema anagrafico cliente. |
| **6** | Controllo di Flusso: Logica Condizionale | Costrutti `if`, `elif`, `else`, operatori relazionali (`==`, `!=`, `>`, `<`), operatori logici (`and`, `or`, `not`). | Assegnazione fascia cliente (Gold, Silver, Bronze). | Calcolo scaglioni sconto per volume. |
| **7** | Cicli `for` e `while` per Iterare sui Dati | Ciclo su liste e dizionari, funzioni `enumerate()` e `zip()`, accumulo totali e somme progressive. | Calcolo fatturato totale da un carrello ordini. | Iterazione su lista ordini mensili. |
| **8** | List Comprehension: Eleganza ed Efficienza | Sintassi compatta `[f(x) for x in lista if condizione]`, confronto prestazionale vs ciclo for classico. | Filtrare ordini Hardware in una riga di codice. | Trasformazione lista imponibili netti. |
| **9** | Funzioni: Modularità e Riutilizzo | Definizione con `def`, parametri posizionali e di default, valore di ritorno `return`, docstring esplicative. | Scrittura della funzione `calcola_totale_riga()`. | **Lab 1 - Es. 1.1**: Funzione calcolo riga. |
| **10** | Elaborazione Liste di Dizionari | Modellazione tabellare: `List[Dict]`, iterazione multi-chiave, calcolo imponibile, sconto e IVA. | Calcolo subtotali su ordine multi-riga. | **Lab 1 - Es. 1.2**: Totali ordine carrello. |
| **11** | Manipolazione Stringhe & Regex Base | Metodi `.strip()`, `.lower()`, `.upper()`, `.title()`, `.replace()`, `.split()`, introduzione al modulo `re`. | Pulizia di ragioni sociali con spazi e typo. | **Lab 1 - Es. 1.3**: Normalizzazione anagrafica. |
| **12** | Aggregazioni Native Senza Librerie | Raggruppamento con dizionari accumulatore, calcolo conteggi, somme e medie manuali. | Aggregazione vendite per categoria con dizionario. | **Lab 1 - Es. 1.4**: Aggregatore categorie. |

---

## 📗 MODULO 2: PANDAS - FONDAMENTI E MANIPOLAZIONE DATAFRAME (4 Ore)

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **13** | Introduzione all'Ecosistema Pandas | Perché Pandas per l'analisi dati, confronto operativo Excel vs Pandas, Series e DataFrame a confronto. | Creazione del primo DataFrame manuale. | Creazione DataFrame da dizionario. |
| **14** | Ingestion Dati: Leggere File Excel e CSV | `pd.read_excel()`, selezione fogli `sheet_name`, parametri `header`, `skiprows`, `usecols`, introduzione a `pd.read_csv()`. | Caricamento di `roma.xlsx` (foglio Dati e Clienti). | **Lab 2 - Es. 2.1**: Caricamento dataset Roma. |
| **15** | Ispezione e Metadati del DataFrame | `.info()`, `.describe()`, `.shape`, `.columns`, `.dtypes`, `.head()`, `.tail()`, memoria occupata. | Diagnostica rapida di consistenza colonne. | Calcolo statistiche descrittive Roma. |
| **16** | Selezione Colonne e Serie Pandas | Notazione a parentesi quadre `df['col']` vs `df[['col1', 'col2']]`, differenze tra Series e DataFrame. | Estrazione colonna fatturato e clienti. | Selezione colonne target di analisi. |
| **17** | Indicizzazione Posizionale: `.iloc[]` | Accesso tramite indici numerici di riga e colonna `df.iloc[righe, colonne]`, slicing posizionale. | Estrazione blocchi di righe e prime N colonne. | **Lab 2 - Es. 2.2**: Estrazione slice `.iloc`. |
| **18** | Indicizzazione per Etichetta: `.loc[]` | Accesso per etichette di riga/colonna, slicing inclusivo degli estremi, selezione mirata. | Filtro combinato per indici e nomi colonna. | Estrazione sottoinsiemi con `.loc`. |
| **19** | Filtri Booleani Semplici | Maschere booleane (`df['col'] == valore`), estrazione righe corrispondenti, conteggio righe filtrate. | Filtro su vendite canale "E-commerce B2B". | **Lab 2 - Es. 2.3 (Parte 1)**: Filtro canale. |
| **20** | Condizioni Logiche Multiple: AND, OR, NOT | Uso obbligatorio di `&` (AND), `\|` (OR), `~` (NOT), importanza delle parentesi tonde `(cond1) & (cond2)`. | Filtro ordini > 10 pezzi con sconto attivo. | **Lab 2 - Es. 2.3 (Parte 2)**: Condizioni doppie. |
| **21** | Metodi di Filtro Avanzati: `.isin()`, `.between()` | Filtrare liste di valori con `.isin(['Roma', 'Milano'])`, range numerici con `.between(100, 500)`. | Estrazione transazioni di fascia media. | Applicazione filtri complessi multi-valore. |
| **22** | Ricerca Testuale con `.str.contains()` | Filtro su stringhe, parametro `case=False`, gestione valori nulli con `na=False`. | Trovare tutti gli ordini contenenti "Server". | Ricerca per parole chiave prodotto. |
| **23** | Creazione e Modifica di Colonne Calcolate | Operazioni vettorializzate colonna per colonna, calcolo `Fatturato_Lordo` = `Quantita * Prezzo`. | Calcolo colonne economiche senza cicli for. | **Lab 2 - Es. 2.4 (Parte 1)**: Calcolo imponibili. |
| **24** | Gestione Tipi Numerici con `pd.to_numeric` | Conversione forzata con `errors='coerce'`, individuazione valori non numerici generati come NaN. | Conversione colonne prezzo con sporcature. | Pulizia preliminare colonna prezzi. |
| **25** | Calcolo Sconti e Incidenza Economica | Calcolo valore sconto in euro, fatturato netto, applicazione aliquote IVA vettoriali. | Calcolo margine e netto finale riga per riga. | Calcolo `Fatturato_Netto` su tutto il dataset. |
| **26** | Ordinamento Dati con `.sort_values()` | Ordinamento singolo e multi-colonna (`ascending=[True, False]`), gestione valori nulli con `na_position`. | Trovare i 10 ordini a maggior fatturato. | **Lab 2 - Es. 2.4 (Parte 2)**: Top 10 Deals. |
| **27** | Statistiche Descrittive per Colonna | `.sum()`, `.mean()`, `.median()`, `.min()`, `.max()`, `.quantile()`, `.std()`, parametri `skipna=True`. | Calcolo KPI generali filiale Roma. | Calcolo mediane e percentili vendita. |
| **28** | Conteggi di Frequenza con `.value_counts()` | Analisi distribuzione frequenze, percentuali con `normalize=True`, conteggio categorie e canali. | Quote percentuali per canale di vendita. | Calcolo share per canale commerciale. |
| **29** | Esportazione Dati con Pandas | `.to_excel()`, `.to_csv()`, `.to_parquet()`, gestione parametri `index=False` ed encoding UTF-8. | Salvataggio del primo export filtrato. | Export dati ripuliti in formato CSV ed Excel. |
| **30** | Recap e Best Practice Modulo 2 | Vettorializzazione vs cicli lenti, gestione memoria, riepilogo comandi essenziali. | Q&A interattivo su casi limite in aula. | Test di autovalutazione rapido su Pandas. |

---

## 📙 MODULO 3: DATA WRANGLING, PULIZIA E INTEGRAZIONE (3 Ore)

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **31** | Il Concetto di Tidy Data & Dirty Data | I 5 problemi classici dei dati reali: duplicati, nulli, tipi errati, formati incoerenti, strutture non tabulari. | Mostrare le anomalie reali in `roma.xlsx`. | Identificazione anomalie con codice. |
| **32** | Individuazione e Rimozione Duplicati | `df.duplicated(subset=...)`, conteggio duplicati, rimozione con `.drop_duplicates(keep='first'/'last')`. | Eliminazione vendite registrate due volte. | **Lab 3 - Es. 3.1**: Deduplica del dataset Roma. |
| **33** | Diagnosi dei Valori Mancanti (Missing Values) | `.isna()`, `.isnull()`, `.notna()`, conteggio e percentuali di missing value per colonna. | Matrice riassuntiva dei dati mancanti. | Ispezione valori nulli su tutte le colonne. |
| **34** | Strategie di Trattamento Nulli: Drop vs Impute | Quando usare `.dropna()` (righe/colonne) e quando usare `.fillna()`, rischi di distorsione del dato. | Confronto tra cancellazione e imputazione. | Scelta strategia per quantità e prezzi. |
| **35** | Imputazione Numerica Avanzata | Imputazione con media e mediana condizionale per gruppo (`transform('mean')` / `transform('median')`). | Imputare il prezzo mancante con la media prodotto. | **Lab 3 - Es. 3.4**: Imputazione prezzi e qta. |
| **36** | Normalizzazione Testi con Accessori `.str` | `.str.strip()`, `.str.lower()`, `.str.title()`, rimozione caratteri speciali e doppi spazi. | Pulizia della colonna `Ragione_Sociale`. | **Lab 3 - Es. 3.2 (Parte 1)**: Pulizia anagrafiche. |
| **37** | Pulizia e Normalizzazione Categorie | Mappatura con `.map()`, `.replace()`, funzioni custom con `.apply()` e dizionari di riconduzione standard. | Riconduzione da 'HW', 'Hardware ' a 'Hardware'. | **Lab 3 - Es. 3.2 (Parte 2)**: Normalizzazione categorie. |
| **38** | La Sfida delle Date: Formati Eterogenei | Date ISO (`2024-01-30`), formati italiani (`30/01/2024`), formati US (`01/30/2024`), testo (`30-Gen-2024`). | Analisi dei formati disallineati nel file Excel. | Ispezione valori colonna `Data_Vendita`. |
| **39** | Date Seriali Excel e Parsing Robusto | Come Excel memorizza le date (giorni dal 1899-12-30), conversione seriali in datetime, `pd.to_datetime()`. | Scrittura della funzione `parse_data_flessibile()`. | **Lab 3 - Es. 3.3 (Parte 1)**: Parsing date miste. |
| **40** | Feature Engineering Temporale | Estrazione componenti `.dt.year`, `.dt.month`, `.dt.day`, `.dt.day_name()`, `.dt.quarter`, periodi trimestrali. | Creazione colonna Mese, Nome Mese e Trimestre. | **Lab 3 - Es. 3.3 (Parte 2)**: Nuove feature temporali. |
| **41** | Integrazione Dati: Concetti di JOIN / Merge | Teoria delle JOIN: Inner Join, Left Join, Right Join, Outer Join; chiavi primarie e chiavi esterne. | Diagramma di Venn ed esempi visivi JOIN. | Comprensione relazioni tra tabelle. |
| **42** | Implementazione con `pd.merge()` | Sintassi `pd.merge(df1, df2, on='ID', how='left')`, gestione colonne con nomi diversi (`left_on`, `right_on`). | Unire le vendite con l'anagrafica clienti ufficiale. | **Lab 3 - Es. 3.5 (Parte 1)**: Merge anagrafica clienti. |
| **43** | Aggregazioni e Tabelle Pivot con `groupby()` | Sintassi `df.groupby('Col')['Val'].sum()`, raggruppamenti multi-colonna (`Filiale`, `Categoria`). | Raggruppamento fatturato per settore cliente. | Calcolo aggregati per categoria e filiale. |
| **44** | Aggregazioni Multiple Avanzate: `.agg()` | Uso di `.agg()` con dizionari e tuple nominate (`sum`, `mean`, `count`, `std`), ridenominazione colonne KPI. | Creazione del report per settore con 4 metriche. | **Lab 3 - Es. 3.5 (Parte 2)**: Report avanzato `.agg`. |
| **45** | Tabelle Pivot con `pd.pivot_table()` | Creazione matrici bidimensionali (Righe x Colonne), valori aggregati, margini e totali complessivi (`margins=True`). | Matrice Canale di Vendita x Categoria Prodotto. | Costruzione tabella pivot canali/prodotti. |
| **46** | Validazione e Data Quality Check | Tecniche di assert, verifica di consistenza tra lordo, sconti e netto, controllo duplicazioni post-merge. | Script di validazione consistenza dati. | Verifica finale della qualità del dataset pulito. |

---

## 📊 MODULO 4: VISUALIZZAZIONE DATI E REPORTING (3 Ore)

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **47** | I Principi della Data Visualization Efficace | Scelta del grafico corretto (Trend ➔ Linee, Confronto ➔ Barre, Distribuzione ➔ Boxplot, Relazione ➔ Scatter). | Esempi di grafici efficaci vs grafici fuorvianti. | Analisi critica di visualizzazioni aziendali. |
| **48** | Anatomia di Matplotlib: Figure e Axes | Gerarchia di Matplotlib: `fig, ax = plt.subplots()`, canvas, assi, titoli, tick, label e legende. | Creazione del primo Canvas Matplotlib orientato a oggetti. | Inizializzazione struttura Figure/Axes. |
| **49** | Grafici a Barre Verticali e Orizzontali | `ax.bar()` e `ax.barh()`, formattazione colori, bordi, etichette dei valori sopra/accanto alle barre. | Grafico Top 8 Clienti per fatturato netto. | **Lab 4 - Es. 4.1**: Bar chart orizzontale Top Clienti. |
| **50** | Serie Temporali e Trend Lineari | `ax.plot()`, stili di linea (`linestyle`), marker, spessore (`linewidth`), formattazione asse temporale. | Andamento mensile delle vendite con marker. | **Lab 4 - Es. 4.2 (Parte 1)**: Line chart trend mensile. |
| **51** | Aggiunta di Linee Guida e Annotazioni | `ax.axhline()`, `ax.axvline()`, `ax.annotate()`, evidenziare target di budget e medie annuali. | Inserimento linea di media annuale con etichetta. | **Lab 4 - Es. 4.2 (Parte 2)**: Aggiunta target di vendita. |
| **52** | Seaborn: Statistica e Design Moderno | Perché Seaborn, temi integrati (`set_theme()`, palette cromatiche `Blues`, `viridis`, `Set2`), integrazione nativa Pandas. | Confronto immediato stile Matplotlib vs Seaborn. | Configurazione palette e stili Seaborn. |
| **53** | Grafici a Barre con Seaborn: `sns.barplot` | Aggregazione automatica, barre di errore/intervalli di confidenza, parametro `hue` per sottogruppi. | Vendite per Categoria suddivise per Canale. | Creazione barplot con suddivisione `hue`. |
| **54** | Analisi delle Distribuzioni: Istogrammi e KDE | `sns.histplot()`, curve di densità di probabilità (KDE), binning ottimale per prezzi e sconti. | Distribuzione degli sconti percentuali applicati. | Istogramma sconti e ticket medi. |
| **55** | Boxplot per l'Individuazione di Outlier | Anatomia del Boxplot (mediana, quartili Q1/Q3, IQR, baffi, valori anomali), `sns.boxplot()`. | Analisi sconti concessi per canale di vendita. | Identificazione outlier commerciali con boxplot. |
| **56** | Grafici a Dispersione: Relazioni e Correlazioni | `sns.scatterplot()`, dimensione bolle (`size`), colore (`hue`), individuazione cluster commerciali. | Relazione tra Quantità ordinata e Sconto concesso. | Scatter plot correlazione quantità vs prezzo. |
| **57** | Heatmap e Matrici di Correlazione | `sns.heatmap()`, pivot table come input, parametri `annot=True`, formattazione numerica `fmt='.1f'`. | Matrice di calore Fatturato per Canale x Categoria. | **Lab 4 - Es. 4.3**: Creazione Heatmap vendite. |
| **58** | Layout Multi-Plot Avanzato: Subplots | `plt.subplots(nrows, ncols, figsize=(w, h))`, gestione assi condivisi, titoli individuali e super-title `suptitle`. | Costruzione griglia 2x2 multi-grafico. | **Lab 4 - Es. 4.4 (Parte 1)**: Composizione griglia 2x2. |
| **59** | Executive Dashboard 2x2 Completa | Assemblaggio dei 4 grafici direzionali in una tavola unica per il CdA. | Rifinitura estetica, allineamento e spaziature. | **Lab 4 - Es. 4.4 (Parte 2)**: Executive Dashboard finale. |
| **60** | Esportazione Grafici per Presentazioni e Stampa | `plt.savefig()` a 300 DPI, formati PNG, PDF vettoriale, SVG, parametro `bbox_inches='tight'`. | Esportazione automatizzata in file ad alta risoluzione. | Salvataggio report grafico in cartella output. |

---

## ⚙️ MODULO 5: AUTOMAZIONE PIPELINE ETL (2 Ore)

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **61** | Architettura di una Pipeline ETL Aziendale | Concetto di Extract (E), Transform (T), Load (L); passaggio da script 'one-shot' a processi automatizzati e stabili. | Schema architetturale della pipeline vendite. | Progettazione del flusso dati modulare. |
| **62** | Gestione File System e Modulo `pathlib` / `os` | Percorsi relativi e assoluti, `os.path.join()`, creazione cartelle dinamiche `os.makedirs(..., exist_ok=True)`. | Scrittura di percorsi multipiattaforma (Linux/Windows). | Configurazione percorsi I/O dinamici. |
| **63** | Scansione Dinamica dei File con `glob` | Ricerca automatica di tutti i file regionali `glob.glob('dataset/*.xlsx')`, filtraggio file temporanei `~$`. | Rilevamento automatico di Roma, Milano, Torino. | **Lab 5 - Fase 1**: Ingestion automatica file. |
| **64** | Ingestion e Concatenazione Massiva | Lettura ciclica con gestione eccezioni `try/except`, unione verticale di DataFrame con `pd.concat()`. | Caricamento e fusione dei file di tutte le filiali. | Concatenazione dati vendite e anagrafiche. |
| **65** | Modularizzazione della Trasformazione Dati | Raggruppamento delle funzioni di cleaning in un modulo pulito, applicazione uniforme su tutte le filiali. | Esecuzione della pipeline di trasformazione. | **Lab 5 - Fase 2**: Funzione `trasforma_dataset()`. |
| **66** | Data Quality Audit e Report di Validazione | Generazione metriche di controllo qualità: duplicati rimossi, righe con anomalie, totali di controllo (Checksum). | Stampa del report di integrità a schermo. | Calcolo metriche di coerenza contabile. |
| **67** | Logging Professionale con il Modulo `logging` | Perché evitare `print()`, livelli di log (DEBUG, INFO, WARNING, ERROR, CRITICAL), formattazione timestamp. | Configurazione del logger standard su console e file. | Aggiunta log strutturati alla pipeline. |
| **68** | Esportazione Parquet: Prestazioni e Compressione | Perché Parquet rispetto a CSV/Excel: compressione a colonna, tipizzazione nativa, velocità 10x in lettura. | Confronto dimensioni file e tempi di caricamento. | **Lab 5 - Fase 3 (Parte 1)**: Salvataggio Parquet. |
| **69** | Generazione Report Excel Multi-Foglio | Scrittura avanzata con `pd.ExcelWriter(..., engine='openpyxl')`, creazione fogli riepilogativi aggregati. | Generazione di `report_direzionale_consolidato.xlsx`. | **Lab 5 - Fase 3 (Parte 2)**: Report Excel multi-scheda. |
| **70** | Esecuzione da Linea di Comando (CLI & Argparse) | Modulo `argparse`, parametri `--input-dir` e `--output-dir`, esecuzione batch della pipeline. | Esecuzione dello script da terminale con flag custom. | Esecuzione pipeline completa end-to-end. |

---

## 💻 MODULO 6: DASHBOARD INTERATTIVE CON STREAMLIT (4 Ore)

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **71** | Introduzione a Streamlit e Architettura Reattiva | Cos'è Streamlit, filosofia "Pure Python", modello di esecuzione reattivo (script re-run ad ogni interazione). | Creazione app "Hello World" e avvio server locale. | Avvio del primo script Streamlit. |
| **72** | Configurazione Pagina e Titoli | `st.set_page_config()`, layout wide, favicon, `st.title()`, `st.header()`, `st.caption()`, formattazione Markdown. | Impostazione del layout aziendale della dashboard. | Personalizzazione intestazione applicazione. |
| **73** | Caching per Alte Prestazioni: `@st.cache_data` | Perché il caching è vitale, come evitare di ricaricare file Parquet ad ogni clic dell'utente, TTL e invalidazione. | Dimostrazione velocità di caricamento con/senza cache. | Applicazione decorator `@st.cache_data`. |
| **74** | Controlli Utente: Sidebar e Widget Interattivi | `st.sidebar`, caselle a discesa `st.selectbox()`, selezione multipla `st.multiselect()`, valori di default. | Creazione filtri interattivi Filiale e Categoria. | **Lab 6 - Es. 6.1 (Parte 1)**: Sidebar con filtri. |
| **75** | Filtri Temporali e Slider | `st.date_input()` con range di selezione date, `st.slider()` per intervalli numerici e soglie. | Filtraggio dinamico del DataFrame per periodo. | **Lab 6 - Es. 6.1 (Parte 2)**: Filtro per range date. |
| **76** | Schede di Riepilogo: `st.columns` e `st.metric` | Suddivisione della pagina in colonne `st.columns(5)`, visualizzazione KPI cards con valori e delta. | Costruzione della barra KPI superiore (Fatturato, Ordini). | **Lab 6 - Es. 6.2**: Creazione 5 KPI metric cards. |
| **77** | Organizzazione Contenuti: `st.tabs` e `st.expander` | Creazione schede di navigazione `st.tabs()`, pannelli collassabili `st.expander()`, layout ordinato e moderno. | Creazione delle 4 schede tematiche dell'applicazione. | Strutturazione interfaccia in schede tematiche. |
| **78** | Integrazione Grafici Matplotlib e Seaborn | `st.pyplot(fig)`, gestione rendering vettoriale, dimensionamento ottimale all'interno delle colonne. | Inserimento trend mensile interattivo nella scheda 1. | Rendering grafici analitici in Streamlit. |
| **79** | Grafici Nativi Streamlit & Altair | `st.line_chart()`, `st.bar_chart()`, `st.altair_chart()`, interattività nativa con tooltip al passaggio del mouse. | Creazione grafico a barre interattivo per categoria. | Costruzione grafici nativi interattivi. |
| **80** | Visualizzazione Tabelle Dati: `st.dataframe` | `st.dataframe()` vs `st.table()`, ordinamento colonne interattivo, ricerca rapida, formattazione con `.style.format()`. | Tabella Top 10 Clienti formattata con valuta euro. | Visualizzazione tabelle ranking con stili. |
| **81** | Filtro di Ricerca Testuale Dinamico | `st.text_input()`, filtraggio in tempo reale su ragione sociale o codice prodotto durante la digitazione. | Ricerca rapida cliente nel database master. | Implementazione motore di ricerca interno. |
| **82** | Esportazione Dati per l'Utente: `st.download_button` | Creazione buffer in memoria (`io.BytesIO` / `.to_csv()`), download immediato del dataset filtrato in CSV/Excel. | Download dei record visualizzati con un solo clic. | **Lab 6 - Es. 6.3**: Pulsante download CSV. |
| **83** | Simulatore di Scenari di Business ("What-If") | Come costruire un simulatore decisionale: slider per variazione volumi (+/-%) e sconti, ricalcolo in tempo reale. | Dimostrazione simulazione impatto margini in aula. | Creazione scheda Simulatore What-If. |
| **84** | Messaggi Informativi e Feedback Visivo | `st.success()`, `st.info()`, `st.warning()`, `st.error()`, indicatori di caricamento con `st.spinner()`. | Aggiunta banner di stato e notifiche operative. | Inserimento notifiche di stato nell'app. |
| **85** | Rifinitura UI e Custom Styling con CSS | Iniezione di CSS personalizzato con `st.markdown(..., unsafe_allow_html=True)`, colori aziendali e card shadow. | Personalizzazione estetica professionale del cruscotto. | Applicazione stili CSS al cruscotto. |
| **86** | Revisione e Test End-to-End della Dashboard | Navigazione completa, test di tutti i filtri, verifica reattività e assenza di bug. | Demo completa dell'applicazione funzionante. | Collaudo finale della dashboard da parte degli studenti. |

---

## 🚀 MODULO 7: DEPLOY SU SERVER LINUX & PRODUZIONE (1 Ora)

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **87** | Dal Laptop al Server Aziendale | Perché il deploy su server: accessibilità continua 24/7, sicurezza, centralizzazione dei dati, differenze dev vs prod. | Connessione SSH al server aziendale Linux. | Accesso al terminale Linux. |
| **88** | Architettura di Produzione su Linux | Schema a 3 livelli: Streamlit Daemon ➔ Gestore di Servizi Systemd ➔ Reverse Proxy Nginx (Porta 80/443). | Illustrazione architettura di produzione. | Comprensione del flusso di rete su server. |
| **89** | Preparazione Ambiente e Virtual Environment | Configurazione permessi utente non-root, creazione cartella applicazione, creazione virtualenv isolato `.venv`. | Creazione `.venv` e installazione dipendenze da `requirements.txt`. | Setup del virtual environment su Linux. |
| **90** | Demoni e Servizi in Background: Systemd | Perché non usare `nohup` o `screen`, vantaggi di Systemd (avvio automatico al boot, riavvio in caso di crash). | Spiegazione della struttura di un file unit Systemd. | Lettura del file `dashboard_vendite.service`. |
| **91** | Scrittura del File `.service` | Definizione sezioni `[Unit]`, `[Service]` (User, WorkingDirectory, ExecStart, Restart), `[Install]`. | Creazione del file `/etc/systemd/system/dashboard_vendite.service`. | **Lab 7**: Configurazione file service. |
| **92** | Gestione del Servizio con `systemctl` | Comandi operativi: `systemctl daemon-reload`, `enable`, `start`, `stop`, `restart`, `status`. | Avvio e verifica dello stato del demone Streamlit. | Avvio del servizio e verifica stato attivo. |
| **93** | Ispezione dei Log con `journalctl` | Monitoraggio log in tempo reale con `journalctl -u dashboard_vendite.service -f`, debug degli errori di produzione. | Simulazione di errore e lettura log in diretta. | Debugging e consultazione log di sistema. |
| **94** | Cenni di Reverse Proxy (Nginx) & Firewall (UFW) | Concetto di Reverse Proxy, configurazione blocco Nginx per porta 8501, regole firewall di sicurezza con UFW. | Mostrare Nginx proxy pass funzionante. | Checklist di sicurezza e messa in sicurezza server. |

---

## 🏆 PROJECT WORK FINALE & CHIUSURA CORSO (3 Ore)

| N. | Titolo Slide | Contenuto Chiave (Bullet Points) | Demo Live Docente | Esercitazione Laboratorio |
|:---|:---|:---|:---|:---|
| **95** | Presentazione del Project Work Finale | Scenario: Acquisizione nuova filiale di Napoli (`napoli_project_work.xlsx`), obiettivi di business e requisiti di consegna. | Presentazione traccia ufficiale e dataset Napoli. | Download e apertura dataset Napoli. |
| **96** | Fasi Operative del Project Work | Guida alle 4 fasi: 1. Cleaning Napoli; 2. Integrazione Nazionale; 3. Analisi di Business; 4. Estensione Dashboard. | Chiarimento dubbi metodologici e tecnici. | Avvio lavoro autonomo / a coppie. |
| **97** | Sessione di Laboratorio Guidato (Hands-On) | Gli studenti sviluppano la pipeline completa e rispondono ai quesiti di business, supporto personalizzato docente. | Affiancamento, troubleshooting e code review in aula. | Sviluppo attivo script e grafici. |
| **98** | Presentazione dei Risultati degli Studenti | Esposizione sintetica dei risultati da parte dei partecipanti, confronto metriche e insight scoperti sui dati. | Conduzione tavola rotonda e confronto soluzioni. | Presentazione grafici e insight di business. |
| **99** | Analisi della Soluzione Docente di Riferimento | Presentazione della soluzione ufficiale commentata, best practice architetturali, benchmark prestazioni. | Esecuzione live di `soluzione_project_work.py`. | Confronto codice docente vs codice studente. |
| **100** | Conclusioni, Certificazione e Prossimi Passi | Riepilogo competenze acquisite (Python, Pandas, Wrangling, Seaborn, ETL, Streamlit, Deploy), consegna attestati. | Risorse per continuare ad approfondire Python & Data. | Consegna materiali completi del corso. |
