# 🎓 PROJECT WORK FINALE (3 Ore)
## Corso: Laboratorio Python + Analisi Dati
**Docente: Arnaldo Morena** | ITIS Campobasso

---

## 🏢 Scenario Aziendale
A fine 2024, la nostra azienda commerciale ha completato l'espansione nel Sud Italia aprendo la nuova filiale commerciale di **Napoli**. 
I dati del primo anno di attività della filiale di Napoli sono stati raccolti nel file:
`dataset/napoli_project_work.xlsx`

La Direzione Generale richiede un lavoro completo di **integrazione, analisi strategica e presentazione**:
Non basta analizzare Napoli a parte: occorre includerla nella pipeline aziendale automatizzata, confrontare le sue performance con Roma, Milano e Torino, ed evidenziare i principali trend commerciali.

---

## 📋 Consegne Richieste agli Studenti

### 1. Ingestion e Data Quality Audit (Peso: 25%)
- Caricare il dataset `dataset/napoli_project_work.xlsx`.
- Ispezionare la qualità dei dati (conteggio record iniziali, identificazione di righe duplicate, valori mancanti su quantità e prezzi, disallineamenti di formato data).
- Applicare la pipeline di pulizia:
  - Deduplicazione.
  - Normalizzazione delle categorie prodotto e delle ragioni sociali.
  - Parsing corretto delle date.
  - Imputazione dei valori mancanti con strategie coerenti (medie/mediane per prodotto).
  - Ricalcolo accurato di Sconti, Fatturato Lordo e Fatturato Netto.

### 2. Integrazione con l'Anagrafica e Consolidamento Nazionale (Peso: 25%)
- Effettuare la JOIN (merge) con il foglio `Anagrafica_Clienti` per arricchire i dati con Settore, Sede e Rating di affidabilità.
- Integrare Napoli nel dataset nazionale consolidato (unendo Roma, Milano, Torino e Napoli).
- Salvare il nuovo master consolidato in `dataset/output_pipeline/vendite_consolidate_nazionale_4filiali.parquet`.

### 3. Analisi Dati e Statistiche Comparative (Peso: 25%)
Rispondere ai seguenti quesiti di business tramite script Python:
1. **Benchmark Filiali**: Qual è la quota percentuale di fatturato generata da Napoli rispetto al totale nazionale?
2. **Top Prodotti e Categorie a Napoli**: Quali sono le 3 categorie merceologiche più vendute a Napoli e qual è lo sconto medio applicato?
3. **Analisi Canali**: Qual è il canale di vendita più efficace a Napoli in termini di fatturato e ticket medio?
4. **Comportamento Clienti per Rating**: I clienti con rating "A+" acquistano proporzionalmente più servizi o hardware?

### 4. Visualizzazione e Dashboard Reporting (Peso: 25%)
- Produrre almeno 3 grafici significativi ad alta risoluzione:
  - Grafico 1: Confronto Fatturato Netto tra le 4 filiali (Bar plot con valori percentuali).
  - Grafico 2: Trend mensile comparativo delle 4 filiali (Multi-line chart).
  - Grafico 3: Mappa di correlazione o Heatmap Categoria x Filiale.
- Integrare Napoli nella dashboard interattiva Streamlit (`dashboard/app.py`).

---

## 📦 Modalità di Consegna
Ogni gruppo o studente dovrà consegnare:
1. Lo script Python eseguibile del project work (`project_work_<cognome>.py`).
2. I grafici salvati in formato PNG.
3. Una breve presentazione/report di sintesi (1-2 pagine o slide) con i commenti ai dati e le raccomandazioni commerciali per la direzione.
