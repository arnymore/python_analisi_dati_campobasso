# 🎓 CANOVACCIO DOCENTE & GUIDA DI REGIA D'AULA
## Corso: Laboratorio Python + Analisi Dati (22 Ore)
### Docente: Arnaldo Morena • ITIS Campobasso • Anno 2026

---

## 🎯 Finalità del Canovaccio
Questo documento rappresenta il manuale di regia per il docente. Per ogni sessione didattica definisce:
* L'aggancio iniziale (**Apertura**) per catturare l'attenzione dell'aula.
* La narrazione aziendale (**Storytelling**) calata sulla catena *TechStore Italia*.
* Le domande strategiche (**Domande da fare all'aula**) per stimolare il ragionamento critico e testare i prerequisiti.
* La scaletta della dimostrazione a schermo (**Live Demo**).
* I punti critici e le trappole cognitive degli studenti (**Errori tipici**).
* La scansione temporale minuto per minuto (**Gestione tempi**).
* Il ponte logico verso il tema successivo (**Transizione**).

---

# 📌 INTRODUZIONE & PATTO D'AULA (Durata: 30 min)

### 1. Apertura
> *"Benvenuti a tutti. In queste 22 ore non faremo accademia né teoria astratta: trasformeremo il vostro computer in una vera postazione di Data Engineering e Business Intelligence. Da oggi voi siete il team di analisti dati assunto da TechStore Italia, una catena retail con filiali a Roma, Milano, Torino e una nuova acquisizione a Napoli. Il vostro compito è salvare l'azienda dal caos dei fogli Excel manuali, automatizzare i flussi e costruire una dashboard che il Direttore Generale consulterà ogni mattina."*

### 2. Storytelling
Presentare il problema reale del management:
* I direttori di filiale inviano ogni fine mese file Excel compilati a mano via email.
* I dati arrivano con duplicati, formati di data disallineati, prezzi mancanti o scritti con simboli di valuta e virgole.
* Il consolidamento manuale richiede 4 giorni lavorativi a persona ed è pieno di errori contabili.
* Obiettivo: creare una pipeline Python automatica a zero-touch che pulisce, unifica e pubblica i dati sul web.

### 3. Domande da fare all'aula
* **Domanda Aperta:** *"Chi di voi ha mai dovuto unire a mano 5 o 6 fogli Excel diversi per fare un report? Cosa succede se il mese dopo vi chiedono di rifarlo?"*
* **Domanda di Verifica:** *"Perché non possiamo fidarci a fare analisi direttamente sui file inviati dalle filiali senza un processo di validazione?"*

### 4. Demo: Ispezione del Repository e Setup
* Mostrare l'albero delle directory nel terminale e su VS Code.
* Eseguire in diretta la creazione dell'ambiente virtuale: `python3 -m venv .venv` e l'attivazione.
* Installare le dipendenze: `pip install -r requirements.txt`.
* Lanciare Jupyter Lab: `jupyter lab`.

### 5. Errori tipici
* Tentativo di eseguire script senza aver attivato il virtualenv (mancanza librerie).
* Confusioni su percorsi relativi e directory di lavoro (`pwd` / `os.getcwd()`).

### 6. Gestione Tempo
* `00:00 - 00:10`: Benvenuto, patto d'aula, presentazione del docente e obiettivi.
* `00:10 - 00:20`: Storytelling del caso TechStore Italia e architettura del corso.
* `00:20 - 00:30`: Verifica setup ambiente su tutte le macchine degli studenti.

### 7. Transizione
> *"Ora che la nostra officina è pronta e abbiamo gli attrezzi installati, partiamo dal motore di base: come manipolare strutture dati complesse con il Python nativo prima ancora di delegare il lavoro a librerie esterne."*

---

# 📘 MODULO 1 – PYTHON OPERATIVO PER L'ANALISI DATI (2 Ore)
*Notebook di riferimento: `laboratori/lab01_python_operativo/`*
*Soluzione: `soluzioni_docente/sol01_python_operativo_commentato.py`*

### 1. Apertura
> *"Prima di correre con Pandas, dobbiamo capire come Python gestisce le transazioni in memoria. Immaginate di ricevere uno stream di dati grezzi da un gestionale ERP sotto forma di lista di dizionari: dobbiamo calcolare sconti, IVA e aggregati usando solo la logica algoritmica pura."*

### 2. Storytelling
La filiale di Roma ha inviato un estratto vendite in formato JSON/Dizionario. Il responsabile acquisti ha inserito nomi clienti con spazi superflui e caratteri minuscoli/maiuscoli incoerenti (es. `'  tech solutions srl  '`). Dobbiamo normalizzare le ragioni sociali e calcolare il fatturato netto e le imposte per ciascun record.

### 3. Domande da fare all'aula
* **Domanda Aperta:** *"Se ho una lista di dizionari che rappresentano transazioni, come posso accumulare il fatturato totale per categoria merceologica senza conoscere a priori tutte le categorie presenti?"*
* **Domanda di Verifica:** *"Qual è il rischio di scrivere `totale = d['sconto']` invece di `totale = d.get('sconto', 0)` quando elaboriamo dati da fonti esterne?"*
* **Domanda di Logica:** *"Cosa accade se in un ciclo `for x in lista:` modificate o eliminate elementi direttamente da `lista`?"*

### 4. Live Demo del Docente
1. Definire la funzione `calcola_totale_riga(quantita, prezzo, sconto, iva)`.
2. Mostrare il dizionario di accumulo `aggregato = {}` e il pattern `.get()` per raggruppare per categoria.
3. Mostrare la normalizzazione di stringhe con `.strip()`, `.split()`, `.join()` e il mapping per acronimi societari (`Srl`, `SpA`).
4. Illustrare la list comprehension filtrata: `[r for r in ordine if r['categoria'] == 'Hardware']`.

### 5. Errori tipici degli studenti
* `KeyError` nell'accesso a campi opzionali.
* Errori di arrotondamento e float precision (es. `0.1 + 0.2 != 0.3`): spiegare l'uso di `round(valore, 2)`.
* Confusione tra mutabilità di liste/dizionari e copie superficiali (`shallow copy` vs `deep copy`).

### 6. Gestione Tempo
* `00:00 - 00:25`: Tipi base, collezioni native (`List[Dict]`), funzioni pure e unpacking.
* `00:25 - 00:50`: String manipulation, list/dict comprehension, logica di accumulo.
* `00:50 - 01:40`: Esercitazione pratica studenti su `lab_01_python_operativo.ipynb`.
* `01:40 - 02:00`: Debriefing collettivo alla lavagna e confronto soluzioni.

### 7. Transizione
> *"Scrivere cicli for e dizionari a mano funziona bene per 10 righe. Ma quando i record diventano 50.000 o 1 milione, il codice puro diventa lento e complicato. È qui che entra in gioco l'arma principale del data analyst: Pandas."*

---

# 📗 MODULO 2 – PANDAS FONDAMENTALE (4 Ore)
*Notebook di riferimento: `laboratori/lab02_pandas_fondamenti/`*
*Soluzione: `soluzioni_docente/sol02_pandas_fondamenti_commentato.py`*

### 1. Apertura
> *"In questo modulo abbandoniamo le tabelle Excel come le avete sempre intese ed entriamo nella mentalità vettoriale. In Pandas non ragioniamo riga per riga: applichiamo operazioni istantanee su intere colonne (Series) e matrici bidimensionali (DataFrame)."*

### 2. Storytelling
Apriamo per la prima volta il file ufficiale `dataset/raw/roma.xlsx`. Dobbiamo verificare quante vendite sono state generate dal canale E-commerce, quanti ordini superano i 1.500€ di imponibile e isolare la Top 10 dei contratti commerciali più remunerativi dell'anno.

### 3. Domande da fare all'aula
* **Domanda Aperta:** *"Secondo voi qual è la differenza tra l'indice posizionale (il numero di riga fisico) e l'etichetta dell'indice in Pandas?"*
* **Domanda di Verifica:** *"Perché `df[df['Quantita'] > 5 & df['Prezzo'] > 100]` solleva un TypeError in Python?"* *(Risposta: precedenza operatori bitwise; servono le parentesi tonde).*
* **Domanda Cruciale:** *"Che differenza c'è tra `.loc` e `.iloc`? Quando è obbligatorio usare uno rispetto all'altro?"*

### 4. Live Demo del Docente
1. `pd.read_excel('dataset/raw/roma.xlsx', sheet_name='Dati_Vendite')` con ispezione di `.shape`, `.info()`, `.describe()`.
2. Dimostrare la differenza tra estrazione colonna Series `df['Fatturato']` e sotto-DataFrame `df[['Fatturato', 'Quantita']]`.
3. Slicing con `.iloc[10:20, 0:4]` vs `.loc[0:10, ['Ragione_Sociale', 'Fatturato_Lordo']]`.
4. Filtri booleani composti con `&`, `|`, `~` e parentesi obbligatorie.
5. Mostrare il famigerato `SettingWithCopyWarning` provocato da un'assegnazione su vista, e risolvere in diretta applicando `.copy()`.
6. Calcolo colonne vettorializzate e ordinamento decrescente con `.sort_values(by='Fatturato_Netto', ascending=False)`.

### 5. Errori tipici degli studenti
* Dimenticanza del parametro `sheet_name` con caricamento del foglio errato.
* Omissione delle parentesi tonde nei filtri composti (`(cond1) & (cond2)`).
* Confusione tra `ascending=True` (crescente) e `ascending=False` (decrescente).
* Manipolazioni di subset senza `.copy()` con comparsa di warning.

### 6. Gestione Tempo (Sessione da 4 ore, intervallata da pausa)
* `00:00 - 00:50`: Architettura Pandas, Series, DataFrame, importazione Excel, ispezione metadati.
* `00:50 - 01:40`: Selezione ed indexing: `.loc`, `.iloc`, slicing, colonne singole e multiple.
* `01:40 - 02:00`: *Pausa caffè (20 min).*
* `02:00 - 02:45`: Filtri booleani composti, problema View vs Copy, il metodo `.copy()`.
* `02:45 - 03:35`: Laboratorio pratico su `lab_02_pandas_fondamenti.ipynb` (Esercizi 2.1 - 2.4).
* `03:35 - 04:00`: Risoluzione guidata, analisi Top 10 Deals e Q&A.

### 7. Transizione
> *"Abbiamo visto come filtrare e ordinare dati corretti. Ma nella vita reale i dati non arrivano puliti. Nel prossimo modulo indosseremo i guanti da chirurgo del dato e impareremo a bonificare record sporchi, date illeggibili e a collegare tabelle diverse con il merge relazionale."*

---

# 📙 MODULO 3 – DATA WRANGLING & QUALITÀ DEL DATO (3 Ore)
*Notebook di riferimento: `laboratori/lab03_data_wrangling/`*
*Soluzione: `soluzioni_docente/sol03_data_wrangling_commentato.py`*

### 1. Apertura
> *"L'80% del tempo di un Data Scientist in azienda non è speso a creare modelli, ma a fare 'Data Wrangling': pulire, convertire, gestire valori nulli e unire tabelle eterogenee. Oggi imparerete a trasformare dati grezzi pieni di anomalie in un dataset certificato per il business."*

### 2. Storytelling
Il file della filiale di Roma contiene 100 record duplicati esatti inseriti da un doppio export contabile. Inoltre molte date sono stringhe '15-Mar-2024' o numeri seriali di Excel (`45367`), e alcuni prezzi unitari mancano completamente. Dobbiamo ripulire il dataset e arricchirlo incrociando l'anagrafica clienti con un merge relazionale per scoprire quali settori industriali generano più ricavi.

### 3. Domande da fare all'aula
* **Domanda Aperta:** *"Se abbiamo prezzi mancanti (NaN), perché in ambito business conviene imputarli con la mediana anziché con la media aritmetica?"*
* **Domanda di Verifica:** *"Cosa accade se fate un `pd.merge(how='left')` e la tabella a destra ha chiavi duplicate?"* *(Spiegare l'esplosione cartesiana delle righe).*
* **Domanda Tecnica:** *"A cosa serve il parametro `validate='many_to_one'` nel merge?"*

### 4. Live Demo del Docente
1. Rilevare duplicati con `df.duplicated().sum()` e bonificare con `df.drop_duplicates().copy()`.
2. Analisi `df.isna().sum()` ed imputazione sconti nulli a zero.
3. Imputazione prezzi/quantità con `transform('mean')` o mediana globale.
4. Live coding della funzione `parse_data_flessibile(val)`: gestione seriali Excel, mapping mesi in italiano (`gen`, `feb`, `mar`), fallback `pd.to_datetime`.
5. Estrazione feature temporali: `.dt.year`, `.dt.month`, `.dt.strftime('%B')`, `.dt.to_period('Q')`.
6. Esecuzione del `pd.merge(df_clean, df_anagrafica, on='Codice_Cliente', how='left', validate='m:1')` con verifica delle righe pre/post.
7. Aggregazione avanzata con `.groupby('Settore').agg(...)`.

### 5. Errori tipici degli studenti
* Applicazione di `pd.to_datetime` senza specificare `dayfirst=True` con scambio involontario tra giorno e mese.
* Corruzione dei tipi colonna (es. colonna numeri che resta di tipo `object` a causa di stringhe '€' o spazi).
* Dimenticanza del `reset_index()` dopo una groupby multi-colonna.

### 6. Gestione Tempo
* `00:00 - 00:45`: Duplicati, missing values, imputazione statistica, string cleaning su codici cliente.
* `00:45 - 01:30`: Normalizzazione date disomogenee e feature engineering temporale.
* `01:30 - 02:30`: Merge relazionale (1:1, 1:N, N:1), validazione integrità e groupby settoriale (Laboratorio 3).
* `02:30 - 03:00`: Revisione collettiva del codice e certificazione output.

### 7. Transizione
> *"Ora che abbiamo un dataset pulito, coerente e arricchito con le informazioni anagrafiche, dobbiamo presentarlo al management. I manager non leggono tabelle di 5.000 righe: vogliono grafici chiari, trend evidenti e una dashboard esecutiva ad alto impatto."*

---

# 📊 MODULO 4 – VISUALIZZAZIONE & REPORTING ESECUTIVO (3 Ore)
*Notebook di riferimento: `laboratori/lab04_visualizzazione/`*
*Soluzione: `soluzioni_docente/sol04_visualizzazione_commentato.py`*

### 1. Apertura
> *"Un'analisi dati brillante non serve a nulla se non riuscite a comunicarla efficacemente ai decision maker. In questo modulo abbandoniamo i grafici standard di default e impariamo a comporre un report visuale executive a 4 pannelli con qualità da pubblicazione (300 DPI)."*

### 2. Storytelling
Il Consiglio di Amministrazione di TechStore Italia richiede un report trimestrale urgente:
1. Chi sono i migliori 8 clienti corporate?
2. Come sta andando il trend del fatturato mese per mese rispetto all'obiettivo medio?
3. Quali categorie di prodotto vendono di più nei vari canali commerciali (Direct, E-commerce, Retail)?
4. Qual è la politica di sconti applicata dalla forza vendita per canale?

### 3. Domande da fare all'aula
* **Domanda Aperta:** *"Perché per confrontare 8 clienti con nomi lunghi è preferibile un grafico a barre orizzontali (`barh`) anziché verticali?"*
* **Domanda di Verifica:** *"Qual è la differenza fondamentale tra la sintassi procedurale `plt.plot()` e quella Object-Oriented `fig, ax = plt.subplots()`?"*
* **Domanda Visual:** *"Cosa rappresenta la linea centrale (mediana) e i bordi della scatola in un Boxplot Seaborn?"*

### 4. Live Demo del Docente
1. Configurazione globale: `plt.style.use('seaborn-v0_8-whitegrid')` e font sizing.
2. Grafico a barre orizzontali per i Top Clienti con aggiunta di etichette dati sui vertici delle barre (`ax.text`).
3. Grafico a linee con linea di riferimento della media aziendale (`ax.axhline`) ed etichette dei mesi in italiano.
4. Heatmap di correlazione e matrice canale vs categoria con annotazioni numeriche (`sns.heatmap(..., annot=True, fmt='.1f')`).
5. Costruzione della griglia 2x2: `fig, axes = plt.subplots(2, 2, figsize=(16, 10))`.
6. Salvataggio ed esportazione ad alta definizione: `fig.savefig('executive_report.png', dpi=300, bbox_inches='tight')`.

### 5. Errori tipici degli studenti
* Sovrapposizione delle etichette sull'asse X (risolvere con `plt.xticks(rotation=45)` o `barh`).
* Dimenticanza di `plt.tight_layout()` con titoli o assi tagliati nel file PNG esportato.
* Dimenticanza di `plt.close()` nei cicli di generazione grafici che causa saturazione di memoria.

### 6. Gestione Tempo
* `00:00 - 00:45`: Architettura Object-Oriented Matplotlib (`fig, ax`), Bar chart orizzontali, etichette custom.
* `00:45 - 01:30`: Seaborn, lineplot con bande e medie, boxplot distribuzioni sconti, heatmap matrici.
* `01:30 - 02:30`: Laboratorio pratico su `lab_04_visualizzazione.ipynb` e composizione dashboard 2x2.
* `02:30 - 03:00`: Analisi dei report generati a 300 DPI e best practice di data storytelling.

### 7. Transizione
> *"Finora abbiamo lavorato su un singolo file (Roma) all'interno di Jupyter. Ma in azienda i dati arrivano continuamente da Roma, Milano, Torino e altre città. Nel prossimo modulo faremo il salto da Data Analyst a Data Engineer: creeremo uno script che scansiona le cartelle, elabora tutti i file in batch e genera un database ottimizzato in formato Parquet."*

---

# ⚙️ MODULO 5 – AUTOMAZIONE DELLA PIPELINE ETL (2 Ore)
*Notebook di riferimento: `laboratori/lab05_automazione_pipeline/`*
*Soluzione: `soluzioni_docente/sol05_automazione_pipeline_commentato.py`*

### 1. Apertura
> *"Oggi automatizziamo il nostro lavoro. Se un processo richiede più di due click manuali, va scritto in codice. Creeremo una pipeline ETL (Extract, Transform, Load) completa, solida, parametrizzabile da riga di comando e dotata di logging professionale."*

### 2. Storytelling
TechStore Italia riceve mensilmente file Excel da tutte le filiali nella cartella `dataset/raw/`. Spesso i dipendenti aprono i file lasciando file temporanei di blocco (`~$roma.xlsx`). La nostra pipeline deve scansionare la cartella, ignorare i file temporanei, processare tutti i dati, unificare l'anagrafica clienti, salvare un file master compresso in Parquet e generare un report Excel a più schede per la direzione amministrativa.

### 3. Domande da fare all'aula
* **Domanda Aperta:** *"Cosa succede a una pipeline se un utente dell'amministrazione ha aperto un file Excel in cartella mentre lo script viene eseguito?"*
* **Domanda di Verifica:** *"Perché il formato Parquet è fino all'80% più compatto e 20 volte più veloce da leggere rispetto a un file Excel o CSV?"*
* **Domanda Architetturale:** *"A cosa serve il modulo standard `logging` rispetto a semplici `print()` in uno script batch di produzione?"*

### 4. Live Demo del Docente
1. Utilizzo di `glob.glob('dataset/raw/*.xlsx')` con filtro list comprehension: `[f for f in files if not os.path.basename(f).startswith('~$')]`.
2. Struttura modulare a 3 funzioni: `carica_dati()`, `trasforma_dataset()`, `esporta_dataset()`.
3. Configurazione del modulo `logging` con timestamp e severity levels (`INFO`, `WARNING`, `ERROR`).
4. Esportazione colonnare in Parquet: `df.to_parquet('vendite_consolidate_italia.parquet', index=False)`.
5. Scrittura multi-foglio Excel con context manager: `with pd.ExcelWriter(...) as writer: ...`.
6. Aggiunta del supporto CLI con `argparse` (`--input-dir`, `--output-dir`).

### 5. Errori tipici degli studenti
* Crash dello script causato dall'apertura accidentale di file lock `~$*.xlsx`.
* Omissione del blocco `with` con mancata scrittura fisica del file Excel (`pd.ExcelWriter`).
* Concatenazione di DataFrame con colonne disallineate che generano centinaia di NaN.

### 6. Gestione Tempo
* `00:00 - 00:35`: Teoria ETL, pattern batch con glob, filtri lock file, modularità architetturale.
* `00:35 - 01:05`: Storage Parquet (Snappy), logging di produzione, ExcelWriter multi-scheda.
* `01:05 - 01:45`: Esercitazione autonoma su `lab_05_automazione_pipeline.ipynb`.
* `01:45 - 02:00`: Esecuzione da terminale dello script con argomenti CLI e verifica file generati.

### 7. Transizione
> *"Ora abbiamo una base dati pulita, unificata e velocissima in formato Parquet. Ma i dirigenti aziendali non usano il terminale né leggono script Python. Nel prossimo modulo costruiremo un'applicazione web interattiva completa con Streamlit, accessibile dal browser."*

---

# 🚀 MODULO 6 – DASHBOARD STREAMLIT INTERATTIVA (4 Ore)
*Notebook di riferimento: `laboratori/lab06_dashboard_streamlit/`*
*Codice sorgente: `dashboard/app.py`*
*Soluzione: `soluzioni_docente/sol06_dashboard_streamlit_commentato.py`*

### 1. Apertura
> *"Benvenuti nel mondo dello sviluppo web per data scientist. Con Streamlit non serve conoscere HTML, CSS o JavaScript: scriveremo un'applicazione interattiva completa, dotata di filtri reattivi, KPI cards, schede multi-tab e un simulatore economico What-If, interamente in Python puro."*

### 2. Storytelling
La Direzione Generale vuole uno strumento live per monitorare le vendite nazionali. Il Direttore Commerciale desidera poter filtrare per filiale, categoria e periodo di tempo, e soprattutto vuole simulare in diretta cosa succederebbe al fatturato se venissero tagliati gli sconti del 5% o aumentati i volumi del 10%.

### 3. Domande da fare all'aula
* **Domanda Aperta:** *"Come fa Streamlit ad aggiornare la pagina quando spostate uno slider o selezionate una voce da un menu a tendina?"* *(Risposta: riesegue l'intero script top-to-bottom).*
* **Domanda Cruciale:** *"Se lo script viene rieseguito a ogni interazione, come evitiamo di ricaricare il file da disco ogni volta?"* *(Risposta: caching con `@st.cache_data`).*
* **Domanda di UI:** *"Qual è il vantaggio di usare `st.tabs()` per suddividere l'analisi rispetto a una pagina verticale infinita?"*

### 4. Live Demo del Docente
1. Avvio dell'app da terminale: `streamlit run dashboard/app.py`.
2. Spiegazione di `st.set_page_config(layout='wide')` e iniezione CSS per personalizzare le metric cards.
3. Dimostrazione del decoratore `@st.cache_data(ttl=600)` per caricare il Parquet una sola volta in RAM.
4. Costruzione della Sidebar laterale (`st.sidebar.multiselect`, `st.sidebar.date_input`).
5. Rendering delle KPI cards in 5 colonne (`st.columns(5)` e `st.metric`).
6. Creazione della navigazione a schede (`st.tabs`):
   - Tab 1: Trend e grafici integrati con `st.pyplot(fig)`.
   - Tab 2: Classifica clienti con tabelle formattate (`st.dataframe`).
   - Tab 3: Simulatore What-If con slider interattivi e calcolo delta in tempo reale.
   - Tab 4: Tabella dati interattiva con barra di ricerca e pulsante di download CSV (`st.download_button`).

### 5. Errori tipici degli studenti
* Dimenticanza di `@st.cache_data` con app lenta e poco reattiva.
* Modifica in-place del DataFrame caricato in cache (che corrompe i dati per gli altri utenti): spiegare la necessità di `.copy()`.
* Chiamate di `st.set_page_config()` a metà script anziché come prima istruzione Streamlit.

### 6. Gestione Tempo (Sessione da 4 ore con pausa)
* `00:00 - 00:50`: Architettura reattiva, ciclo di vita Streamlit, caching `@st.cache_data`, setup pagina.
* `00:50 - 01:40`: Sidebar, widget interattivi, filtri dinamici, KPI cards a colonne.
* `01:40 - 02:00`: *Pausa (20 min).*
* `02:00 - 02:45`: Implementazione Multi-tab, grafici Matplotlib/Seaborn in Streamlit, What-If simulator.
* `02:45 - 03:40`: Esercitazione guidata su `lab_06_dashboard_streamlit` e sviluppo `app.py`.
* `03:40 - 04:00`: Test completo in locale, esportazione dati CSV e Q&A.

### 7. Transizione
> *"La nostra dashboard funziona perfettamente sul computer locale. Ma cosa succede se chiudiamo il laptop? L'applicazione smette di funzionare e nessuno in azienda può più vederla. Nel prossimo modulo vedremo come distribuire la nostra app su un server Linux di produzione, trasformandola in un servizio demone sempre attivo."*

---

# 🐧 MODULO 7 – DEPLOY LINUX & SYSTEMD (1 Ora - Live Demo Guidata)
*Guida di riferimento: `laboratori/lab07_deploy_linux/`*
*Script di riferimento: `soluzioni/sol07_deploy_linux.sh`*
*Soluzione: `soluzioni_docente/sol07_deploy_linux_commentato.md`*

### 1. Apertura
> *"Completiamo il ciclo del software portando il nostro progetto in produzione. Oggi vedremo cosa significa fare il deploy su un server Linux Cloud/VPS: configureremo un demone Systemd che avvierà automaticamente la nostra dashboard all'avvio del sistema e la riavvierà in 5 secondi in caso di crash."*

### 2. Storytelling
Il reparto IT di TechStore Italia ha assegnato un'istanza virtuale Linux Ubuntu Server su cui ospitare la piattaforma. Dobbiamo garantire che il servizio risponda 24 ore su 24 sulla porta di rete 8501, sia resiliente ai riavvii di macchina e permetta all'amministratore di monitorare i log applicativi in tempo reale.

### 3. Domande da fare all'aula
* **Domanda Aperta:** *"Se lanciamo `streamlit run app.py` da un terminale SSH e poi chiudiamo la finestra, perché l'applicazione si spegne?"* *(Segnale SIGHUP inviato alla chiusura della sessione).*
* **Domanda di Verifica:** *"A cosa serve la direttiva `Restart=always` e `RestartSec=5` in un unit file systemd?"*
* **Domanda di Sicurezza:** *"Perché non dovremmo MAI eseguire un'applicazione web come utente `root`?"*

### 4. Live Demo del Docente (Modalità Live Demo Guidata)
1. Connessione SSH simulata/reale all'ambiente Linux.
2. Ispezione della struttura del file `/etc/systemd/system/dashboard_vendite.service`.
3. Analisi riga per riga delle sezioni `[Unit]`, `[Service]`, `[Install]`.
4. Spiegazione dei percorsi assoluti per l'eseguibile Python/Streamlit dell'ambiente virtuale.
5. Esecuzione dei comandi di controllo di sistema:
   - `sudo systemctl daemon-reload`
   - `sudo systemctl enable --now dashboard_vendite.service`
   - `sudo systemctl status dashboard_vendite.service`
6. Ispezione in streaming continuo dei log applicativi con `sudo journalctl -u dashboard_vendite.service -f`.
7. Simulazione di un crash (`kill -9`) per mostrare il recupero e riavvio automatico in 5 secondi da parte di Systemd.
8. Cenni architetturali sull'uso di Nginx come Reverse Proxy su porta 80/443 con certificati HTTPS.

### 5. Errori tipici degli studenti
* Inserimento di percorsi relativi (es. `./venv/bin/streamlit` invece di percorsi assoluti completi).
* Dimenticanza di `sudo systemctl daemon-reload` dopo la modifica del file di servizio.
* Mancanza di permessi di lettura/esecuzione sulla cartella del progetto per l'utente designato.

### 6. Gestione Tempo (60 min tassativi)
* `00:00 - 00:15`: Architettura Client-Server, limiti di esecuzione da sessione interattiva, concetto di demone.
* `00:15 - 00:30`: Anatomia dell'Unit File systemd, direttive di servizio, isolamento privilegi.
* `00:30 - 00:50`: Live demo guidata: installazione, gestione ciclo di vita (`systemctl`), streaming log (`journalctl`), test di resilienza al crash.
* `00:50 - 01:00`: Discussione architetturale, cenni Nginx e transizione al Project Work.

### 7. Transizione
> *"Ora avete tutte le competenze teoriche e pratiche necessarie: Python puro, Pandas, Data Wrangling, Visualizzazione, Automazione ETL, Streamlit e Deploy Linux. È il momento di mettervi alla prova da soli con il Project Work finale."*

---

# 🏆 PROJECT WORK FINALE – INTEGRAZIONE FILIALE NAPOLI (3 Ore)
*Documentazione di riferimento: `project_work/`*
*Benchmark: `project_work/traccia_studenti.md` e `project_work/criteri_valutazione.md`*

### 1. Apertura e Consegna della Traccia
> *"Questo è il momento della certificazione sul campo. Non siete più studenti guidati dal docente, ma consulenti data analyst autonomi. L'azienda TechStore Italia ha appena completato l'acquisizione della filiale di Napoli e vi ha consegnato il file grezzo `dataset/raw/napoli_project_work.xlsx`. Avete 3 ore per eseguire l'audit dei dati, aggiornare la pipeline ETL, rigenerare il master Parquet a 4 filiali, verificare la dashboard Streamlit e produrre il report esecutivo finale."*

### 2. Storytelling
La filiale di Napoli invia dati non conformi: 100 record duplicati esatti, date formattate con stili misti, missing values nei prezzi e codici cliente non normalizzati. Il successo dell'integrazione dipende dalla capacità degli studenti di applicare in autonomia la catena di trasformazione già collaudata per le altre filiali.

### 3. I 4 Deliverable da Richiedere agli Studenti
1. **Deliverable 1:** Notebook o script di pulizia dedicato per la filiale di Napoli con verifica benchmark (€ 1.042.850,50 fatturato netto).
2. **Deliverable 2:** Esecuzione della pipeline ETL su tutte e 4 le filiali e generazione di `vendite_consolidate_italia.parquet` (esattamente 4.552 record).
3. **Deliverable 3:** Verifica e screenshot della dashboard Streamlit con inclusione della filiale di Napoli e KPI aggiornati.
4. **Deliverable 4:** Generazione del report Excel direzionale consolidato a 4 fogli e salvataggio della dashboard grafica 2x2.

### 4. Benchmark Numerici Ufficiali per il Docente (Foglio di Controllo)
* **Dataset Napoli Grezzo:** 1.100 righe
* **Dataset Napoli Pulito:** 1.000 record (100 duplicati eliminati)
* **Fatturato Netto Napoli:** **€ 1.042.850,50**
* **Master Dataset Italia (4 Filiali):** **4.552 record totali**
* **Fatturato Netto Consolidato Nazionale:** **€ 4.614.820,50**
* **Margine Lordo Totale:** **€ 1.712.440,20**

### 5. Rubrica di Valutazione Docente (100 Punti)
* `25 pt` - **Data Wrangling & Qualità:** Deduplicazione, date normalizzate, imputazione corretta, assenza NaN residui.
* `25 pt` - **Ingegneria ETL:** Scansione batch, filtro lock file, merge relazionale con anagrafica, export Parquet.
* `25 pt` - **Dashboard Streamlit:** Reattività, filtri multi-filiale coerenti, simulatore What-If funzionante.
* `25 pt` - **Reporting & Best Practice:** Report Excel multi-foglio, export a 300 DPI, codice pulito e documentato.
* *Soglia certificazione:* **60/100** • *Eccellenza con lode didattica:* **>= 90/100**.

### 6. Gestione Tempo (180 min totali)
* `00:00 - 00:20`: Presentazione traccia di lavoro, requisiti di consegna e chiarimento dubbi.
* `00:20 - 02:20`: Sviluppo autonomo da parte degli studenti (il docente assume il ruolo di Project Manager e risponde solo a quesiti architetturali).
* `02:20 - 02:45`: Raccolta deliverable e verifica automatica contro i benchmark ufficiali.
* `02:45 - 03:00`: Chiusura del corso, feedback complessivo, consegna attestati e conclusioni.

---
