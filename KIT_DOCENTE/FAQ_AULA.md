# ❓ FAQ AULA: 50+ DOMANDE FREQUENTI CON RISPOSTE DOCENTE
## Corso: Laboratorio Python + Analisi Dati (22 Ore)
### Docente: Arnaldo Morena • ITIS Campobasso

---

Questo archivio raccoglie oltre 50 domande reali poste dagli studenti durante lo svolgimento del corso, suddivise per area tematica, con le relative risposte didattiche e spiegazioni operative per il docente.

---

## 🐍 SEZIONE 1: PYTHON OPERATIVO & FONDAMENTI

### 1. Perché in Python usiamo una `List[Dict]` invece di matrici o array per rappresentare dati tabellari all'inizio?
> **Risposta Docente:** Una lista di dizionari rispecchia fedelmente la struttura di un recordset relazionale o di un payload JSON proveniente da un'API REST o da un database NoSQL. Ogni elemento della lista è una riga (record), e le chiavi del dizionario rappresentano i nomi delle colonne. È il modo più intuitivo e flessibile per comprendere il concetto di tabella prima di passare a Pandas.

### 2. Qual è la differenza tra `d['chiave']` e `d.get('chiave', default)`?
> **Risposta Docente:** L'accesso diretto `d['chiave']` genera un'eccezione irreversibile `KeyError` se la chiave non esiste nel dizionario, interrompendo lo script. Il metodo `d.get('chiave', default)` restituisce invece il valore di fallback specificato (es. `0` o `None`) senza sollevare errori, rendendo il codice robusto nella gestione di dati incompleti.

### 3. Perché non posso modificare una lista mentre la sto iterando in un ciclo `for`?
> **Risposta Docente:** Modificare la dimensione di una lista durante l'iterazione sballa i puntatori interni degli indici, provocando il salto di elementi o comportamenti indefiniti. La best practice consiste nell'iterare su una copia superficiale `for x in list(mia_lista):` oppure nell'utilizzare una list comprehension per creare una nuova lista filtrata.

### 4. Che differenza c'è tra `==` e `is` in Python?
> **Risposta Docente:** L'operatore `==` confronta l'uguaglianza dei valori contenuti negli oggetti (`val1 == val2`), mentre `is` confronta l'identità in memoria, ovvero verifica se due variabili puntano esattamente alla medesima locazione fisica di RAM (`id(a) == id(b)`).

### 5. Perché scriviamo `imponibile * (1 - sconto / 100.0)` con `.0` sul denominatore?
> **Risposta Docente:** Sebbene in Python 3 la divisione tra interi produca un float (`/`), l'uso esplicito del letterale float (`100.0`) rende chiaro al lettore del codice che l'operazione avviene nel dominio continuo dei numeri a virgola mobile e preserva la compatibilità semantica.

### 6. Come funziona l'unpacking delle tuple in un ciclo su dizionario?
> **Risposta Docente:** Il metodo `d.items()` restituisce un iteratore di tuple composte da `(chiave, valore)`. Scrivendo `for k, v in d.items():`, Python assegna automaticamente il primo elemento della tupla a `k` e il secondo a `v`.

### 7. Perché i calcoli con i numeri decimali a volte danno risultati strani come `0.30000000000000004`?
> **Risposta Docente:** Dipende dallo standard IEEE 754 per la rappresentazione in virgola mobile binaria: molte frazioni decimali (come 0.1 o 0.2) sono numeri periodici in base 2. In ambito contabile/commerciale si risolve applicando la funzione `round(valore, 2)` o utilizzando il modulo standard `decimal.Decimal`.

---

## 🐼 SEZIONE 2: PANDAS FONDAMENTALE

### 8. Perché Pandas è molto più veloce dei cicli `for` in Python?
> **Risposta Docente:** Pandas poggia su array NumPy scritti in C e C++. Quando eseguiamo operazioni tra colonne (es. `df['Qta'] * df['Prezzo']`), il calcolo avviene a livello di codice compilato a basso livello tramite operazioni vettoriali (SIMD), senza l'overhead dell'interprete Python per ogni singolo elemento.

### 9. Qual è la differenza strutturale tra una `Series` e un `DataFrame`?
> **Risposta Docente:** Una `Series` è un array monodimensionale etichettato con un solo indice. Un `DataFrame` è una tabella bidimensionale formata da più `Series` affiancate che condividono lo stesso indice di riga (`index`).

### 10. Quando devo usare `.loc[]` e quando `.iloc[]`?
> **Risposta Docente:** Usiamo `.loc[]` quando selezioniamo righe e colonne in base alle loro **etichette** (nomi di colonna ed etichette di indice). Usiamo `.iloc[]` quando vogliamo effettuare una selezione puramente **posizionale** tramite numeri interi da `0` a `N-1`.

### 11. Perché nel filtro `df[(df['A'] > 10) & (df['B'] < 5)]` servono obbligatoriamente le parentesi tonde?
> **Risposta Docente:** In Python gli operatori logici bitwise (`&`, `|`, `~`) hanno una precedenza sintattica superiore rispetto agli operatori di confronto (`>`, `<`, `==`). Senza parentesi, Python cercherebbe di calcolare `10 & df['B']`, generando un `TypeError`.

### 12. Che cos'è esattamente il `SettingWithCopyWarning` e perché si verifica?
> **Risposta Docente:** È un avviso che Pandas emette quando tentiamo di modificare un sottoinsieme di dati estratto con un filtro. Pandas non sa con certezza se quel sottoinsieme sia una **Copia** indipendente in memoria o una **Vista** collegata al DataFrame originale. Per eliminarlo ed evitare corruzioni di memoria, è necessario chiamare esplicitamente `.copy()` al momento del filtraggio.

### 13. Come fa `pd.read_excel()` a leggere i file senza avere Microsoft Excel installato sulla macchina?
> **Risposta Docente:** Pandas utilizza engine open source come `openpyxl` o `calamine`, che analizzano direttamente il formato OpenXML (che internamente è un archivio compresso di file XML) senza dipendere dal software Excel proprietario.

### 14. Perché `df.shape` non ha le parentesi tonde alla fine come `df.head()`?
> **Risposta Docente:** Perché `shape` è un **attributo** (una tupla memorizzata nell'oggetto che contiene le dimensioni correnti `(righe, colonne)`), mentre `head()` è un **metodo** (una funzione che accetta argomenti ed esegue un'elaborazione prima di restituire le prime N righe).

### 15. A cosa serve `reset_index(drop=True)`?
> **Risposta Docente:** Quando filtriamo o ordiniamo un DataFrame, i vecchi numeri di riga rimangono invariati (es. righe 3, 15, 84). `reset_index(drop=True)` rigenera un indice sequenziale continuo da `0` a `N-1`, eliminando il vecchio indice per evitare che diventi una colonna separata.

---

## 🧹 SEZIONE 3: DATA WRANGLING & QUALITÀ DATI

### 16. Perché si consiglia di fare `drop_duplicates(subset=[...])` invece che un `drop_duplicates()` generico?
> **Risposta Docente:** `drop_duplicates()` generico elimina solo le righe dove **tutte** le colonne sono identiche al 100%. Spesso due record duplicati differiscono per un timestamp di pochi secondi o una nota testuale. Specificare `subset=['ID_Transazione']` o `subset=['Data', 'Cliente', 'Prodotto']` assicura l'eliminazione della duplicazione logica del business.

### 17. Qual è la differenza tra `df.isna().sum()` e `df.isnull().sum()`?
> **Risposta Docente:** In Pandas `isna()` e `isnull()` sono esattamente la stessa identica funzione: `isnull()` è un alias storico mantenuto per analogia con il linguaggio SQL e con la libreria R.

### 18. Quando è opportuno eliminare le righe con valori nulli (`dropna()`) e quando è preferibile imputarli (`fillna()`)?
> **Risposta Docente:** Si eliminano le righe con `dropna()` solo quando la percentuale di dati mancanti è trascurabile (< 1-2%) oppure quando il campo mancante è la chiave primaria irrecuperabile (es. `ID_Transazione`). Si imputano i valori con `fillna()` (usando mediana, media o zero) quando la colonna è un attributo quantitativo secondario (es. sconti o prezzi) per non perdere il volume complessivo delle altre transazioni.

### 19. Perché le date di Excel lette come numeri interi (es. 45367) corrispondono a date reali?
> **Risposta Docente:** Microsoft Excel memorizza internamente le date come il numero di giorni trascorsi a partire dal 1° gennaio 1900 (con un noto bug storico che considera il 1900 bisestile). Per convertirle in Python basta sommare quei giorni alla data base `1899-12-30`.

### 20. Cosa significa `errors='coerce'` in `pd.to_datetime()`?
> **Risposta Docente:** Indica a Pandas che, qualora incontri una stringa di data non valida, corrotta o indecifrabile (es. `'Data_Sconosciuta'`), non deve lanciare un'eccezione che blocca lo script, ma deve convertire quel valore nel valore speciale `pd.NaT` (Not a Time), consentendo al resto della pipeline di proseguire.

### 21. Qual è la differenza tra una join `inner`, `left`, `right` e `outer`?
> **Risposta Docente:**
> - `inner`: mantiene solo i record con corrispondenza in entrambe le tabelle.
> - `left`: mantiene tutti i record della tabella sinistra e inserisce `NaN` dove non c'è corrispondenza a destra.
> - `right`: mantiene tutti i record della tabella destra.
> - `outer`: mantiene tutti i record di entrambe le tabelle, riempiendo con `NaN` le mancanze.

### 22. Che cos'è l'esplosione cartesiana in un `pd.merge()` e come si previene?
> **Risposta Docente:** Si verifica quando la tabella di destra (es. anagrafica) contiene chiavi duplicate per lo stesso codice cliente. In questo caso, ogni riga della tabella sinistra viene moltiplicata tante volte quante sono le occorrenze a destra, alterando falsamente il totale delle vendite. Si previene specificando `validate='many_to_one'` nel merge o deduplicando preventivamente la tabella anagrafica.

### 23. A cosa serve il parametro `indicator=True` in `pd.merge()`?
> **Risposta Docente:** Aggiunge una colonna speciale `_merge` con valori `'both'`, `'left_only'`, `'right_only'`, permettendo all'analista di verificare istantaneamente quali record non hanno trovato corrispondenza con la tabella anagrafica.

---

## 📈 SEZIONE 4: VISUALIZZAZIONE & REPORTING GRAFICO

### 24. Perché Matplotlib Object-Oriented (`fig, ax`) è superiore alla sintassi `plt.*`?
> **Risposta Docente:** La sintassi `plt.*` fa affidamento su un puntatore globale nascosto alla figura "corrente". Quando si creano layout complessi a griglia (es. 2x2), la sintassi OOP permette di controllare esplicitamente e simultaneamente ogni singolo asse (`ax[0, 0]`, `ax[0, 1]`, ecc.) senza rischio di sovrascritture accidentali.

### 25. Come si fa a salvare un grafico con risoluzione adatta alla stampa tipografica o a monitor 4K?
> **Risposta Docente:** Si imposta il parametro `dpi=300` (Dots Per Inch) e `bbox_inches='tight'` nel metodo `fig.savefig('report.png', dpi=300, bbox_inches='tight')`.

### 26. Qual è il significato statistico del Boxplot Seaborn?
> **Risposta Docente:** La linea spessa centrale è la **mediana** (50° percentile), i bordi della scatola sono il **primo quartile Q1** (25°) e il **terzo quartile Q3** (75°). La distanza tra Q3 e Q1 è l'intervallo interquartile (IQR). I "baffi" estendono i dati fino a 1.5 * IQR, mentre i singoli punti oltre i baffi sono considerati **outlier** statistici.

### 27. Perché nei grafici a barre Seaborn a volte vediamo una barretta nera verticale sopra le barre?
> **Risposta Docente:** È la barra di errore (intervallo di confidenza al 95%). Se vogliamo mostrare la somma totale del fatturato senza intervalli statistici, impostiamo `estimator='sum'` ed `errorbar=None`.

### 28. Perché dopo aver generato e salvato un grafico dobbiamo sempre chiamare `plt.close(fig)`?
> **Risposta Docente:** Matplotlib conserva ogni figura creata nella memoria RAM finché non viene esplicitamente chiusa. In script automatizzati o pipeline che generano decine di grafici, omettere `plt.close()` provoca un memory leak progressivo e rallentamenti di sistema.

### 29. Come si invertono gli assi in un grafico a barre orizzontali in Matplotlib?
> **Risposta Docente:** Si utilizza `ax.barh(y, width)` invece di `ax.bar(x, height)`. Per avere il cliente con il valore più alto in cima, si ordina preventivamente la serie in senso crescente (`ascending=True`).

### 30. Come formattare le etichette dell'asse Y per visualizzare migliaia di Euro (`€ 150k`)?
> **Risposta Docente:** Dividendo i valori per `1000.0` prima del plot e impostando `ax.set_ylabel('Fatturato (k€)')`, oppure utilizzando un formattatore Matplotlib: `ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f"€ {x*1e-3:.0f}k"))`.

---

## ⚙️ SEZIONE 5: AUTOMAZIONE PIPELINE & STORAGE

### 31. Perché in una pipeline batch usiamo `glob.glob()` con un filtro per `~$`?
> **Risposta Docente:** Quando un utente apre un file Excel, il sistema operativo crea nella stessa cartella un file temporaneo di lock nascosto che inizia con `~$` (es. `~$roma.xlsx`). Se lo script tenta di leggerlo con Pandas solleva un `PermissionError` o un errore di formato corrotto.

### 32. Perché il formato Parquet è preferibile a CSV ed Excel per i dati consolidati?
> **Risposta Docente:** Parquet è un formato colonnare binario compresso (algoritmo Snappy). Preserva i tipi di dato nativi (le date rimangono date, i numeri rimangono float32/int64), occupa fino all'80% di spazio in meno su disco e consente letture molto più veloci perché legge solo le colonne richieste dalla query.

### 33. Come fa `pd.ExcelWriter` a creare file con più fogli di lavoro?
> **Risposta Docente:** Invocando `pd.ExcelWriter(percorso, engine='openpyxl')` all'interno di un blocco `with`, l'oggetto `writer` mantiene aperto l'archivio Excel e consente chiamate successive a `df.to_excel(writer, sheet_name='NomeFoglio')` prima di finalizzare la scrittura alla chiusura del blocco.

### 34. A cosa serve il modulo standard `logging` al posto dei normali `print()`?
> **Risposta Docente:** `logging` aggiunge automaticamente timestamp, livello di gravità (`INFO`, `WARNING`, `ERROR`), nome del modulo, e consente di reindirizzare i messaggi simultaneamente su console e su file di log permanenti (`pipeline.log`) senza dover modificare il codice sorgente.

### 35. Perché è buona norma incapsulare il codice batch all'interno di `if __name__ == '__main__':`?
> **Risposta Docente:** Perché consente di eseguire lo script direttamente da riga di comando come programma principale, ma permette anche di importare le sue singole funzioni (es. `trasforma_dataset()`) all'interno di altri script (come la dashboard Streamlit o i test di regressione) senza eseguire l'intero ciclo batch.

### 36. Come gestire i parametri CLI con `argparse` in uno script ETL?
> **Risposta Docente:** Definendo un parser:
> ```python
> parser = argparse.ArgumentParser()
> parser.add_argument('--input-dir', default='dataset/raw')
> args = parser.parse_args()
> ```
> Questo permette di richiamare lo script da cron job o script bash con percorsi personalizzati: `python script.py --input-dir /dati/nuovi`.

---

## 🌐 SEZIONE 6: DASHBOARD STREAMLIT

### 37. Qual è il paradigma di esecuzione reattivo di Streamlit?
> **Risposta Docente:** Ogni volta che l'utente interagisce con un widget (muove uno slider, cambia un filtro), Streamlit non esegue solo un handler di evento locale, ma riesegue **l'intero script Python dall'inizio alla fine** (top-to-bottom), rigenerando l'interfaccia con i nuovi parametri.

### 38. Come funziona il decoratore `@st.cache_data` e quando si invalida la cache?
> **Risposta Docente:** `@st.cache_data` calcola l'hash dei parametri di input della funzione. Se la funzione viene richiamata con gli stessi argomenti già visti, Streamlit salta l'esecuzione del corpo della funzione e restituisce direttamente il risultato memorizzato in RAM. La cache si invalida se cambiano i parametri di input, se cambia il codice della funzione o allo scadere del parametro `ttl` (Time To Live).

### 39. Perché `st.set_page_config()` deve essere la prima istruzione Streamlit dello script?
> **Risposta Docente:** Perché Streamlit invia le direttive di layout (titolo della scheda del browser, favicon, layout wide) nell'header iniziale della sessione WebSocket; qualsiasi comando visivo eseguito prima impedisce la corretta inizializzazione del viewport.

### 40. Come si dispongono i widget o le KPI cards su più colonne in Streamlit?
> **Risposta Docente:** Si usa `col1, col2, col3 = st.columns(3)` e poi si scrive all'interno delle singole colonne tramite blocco `with col1:` oppure chiamando direttamente `col1.metric('Titolo', 'Valore')`.

### 41. Come funziona il componente `st.download_button` per esportare file CSV?
> **Risposta Docente:** Converte il DataFrame filtrato in una stringa di byte UTF-8 tramite `df.to_csv(index=False).encode('utf-8')` e fornisce al browser un pulsante standard HTML5 di download che non richiede roundtrip di salvataggio su disco sul server.

### 42. Come si realizza un simulatore economico What-If in Streamlit?
> **Risposta Docente:** Si collegano due o più slider (`st.slider`) a variabili di variazione percentuale (es. `% sconto`, `% volume`) e si applicano queste variabili a una formula vettoriale sul DataFrame filtrato, confrontando il totale ricalcolato con il totale reale tramite il parametro `delta` di `st.metric`.

### 43. Che differenza c'è tra `@st.cache_data` e `@st.cache_resource`?
> **Risposta Docente:** `@st.cache_data` si usa per oggetti serializzabili e dati tabellari (DataFrame, liste, dizionari). `@st.cache_resource` si usa per oggetti non serializzabili e connessioni globali a stato persistente (connessioni a database SQLAlchemy, modelli di Machine Learning, client HTTP).

---

## 🐧 SEZIONE 7: DEPLOY LINUX & SYSTEMD

### 44. Perché non si deve lasciare un'applicazione Streamlit in esecuzione in un terminale SSH con `nohup` o `screen` in produzione?
> **Risposta Docente:** `nohup` o `screen` non offrono gestione dei crash, non riavviano l'applicazione al boot del server, non gestiscono i log in modo centralizzato con rotazione automatica e non permettono il governo tramite strumenti standard di orchestrazione DevOps. Systemd è lo standard de facto su Linux per tutti i servizi enterprise.

### 45. Cosa significa la sezione `[Unit]` in un file `.service` di Systemd?
> **Risposta Docente:** Contiene i metadati descrittivi del servizio (`Description`) e le dipendenze di avvio (`After=network.target`), indicando a Systemd di non avviare il processo finché lo stack di rete del sistema operativo non è completamente operativo.

### 46. Perché dobbiamo specificare il percorso assoluto sia per l'eseguibile Python sia per lo script in `ExecStart`?
> **Risposta Docente:** Systemd viene eseguito in un ambiente di esecuzione minimale che non eredita il `PATH` o le variabili di sessione dell'utente interattivo. Specificare percorsi assoluti (es. `/home/ubuntu/app/.venv/bin/streamlit`) garantisce l'uso del corretto interprete virtualenv.

### 47. Qual è la differenza tra `systemctl enable` e `systemctl start`?
> **Risposta Docente:** `systemctl enable` registra il servizio nei target di avvio del sistema per farlo partire automaticamente al boot della macchina. `systemctl start` avvia immediatamente il processo nel momento presente. Il comando combinato `systemctl enable --now` esegue entrambe le operazioni contemporaneamente.

### 48. Come si controllano i log applicativi di un servizio Systemd in tempo reale?
> **Risposta Docente:** Eseguendo `sudo journalctl -u nome_servizio.service -f`. Il flag `-f` (follow) mantiene il terminale agganciato allo stream di log, stampando ogni nuova riga non appena viene generata.

### 49. A cosa serve un Reverse Proxy Nginx davanti a Streamlit?
> **Risposta Docente:** Permette di esporre l'applicazione sulle porte standard `80` (HTTP) e `443` (HTTPS) con certificati crittografici SSL/TLS (Let's Encrypt), gestire il buffering delle richieste e proteggere l'applicazione Streamlit (che risponde sulla porta interna 8501) da accessi diretti non autorizzati.

### 50. Cosa accade se si modifica il file `.service` e si prova subito a fare `systemctl restart` senza fare `daemon-reload`?
> **Risposta Docente:** Systemd ignora le modifiche apportate sul file di testo e riavvia il servizio con la vecchia configurazione presente nella cache in RAM, mostrando un messaggio di avviso *"Unit file changed on disk, run 'systemctl daemon-reload' to reload units"*.

---

## 🏆 SEZIONE 8: PROJECT WORK & INTEGRAZIONE DATI

### 51. Come deve comportarsi uno studente se durante l'integrazione di Napoli il numero totale di righe non corrisponde a 4.552?
> **Risposta Docente:** Deve verificare i due punti di perdita o moltiplicazione dati:
> 1. Verificare che siano stati eliminati esattamente i 100 record duplicati di Napoli (da 1.100 a 1.000 righe).
> 2. Verificare che nel merge con l'anagrafica non ci siano state perdite di record o duplicazioni da chiavi non univoche.

### 52. Cosa fare se il fatturato netto finale non coincide con il benchmark ufficiale di € 4.614.820,50?
> **Risposta Docente:** L'errore è quasi sempre causato dall'ordine di applicazione dello sconto (calcolare lo sconto sull'imponibile prima di sottrarlo) o da un'imputazione errata dei prezzi mancanti (es. aver imputato con la media invece che con la mediana, o non aver gestito gli sconti NaN impostandoli a zero).

---
