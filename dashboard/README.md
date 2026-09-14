# 📊 Dashboard Streamlit Direzionale

Questa cartella contiene l'applicazione web interattiva completa utilizzata per il monitoraggio analitico delle vendite aziendali.

---

## 🎯 Funzionalità dell'Applicazione (`app.py`)

* **Pannello Filtri Sidebar Dinamico:**
  * Selezione multi-filiale (`Roma`, `Milano`, `Torino`).
  * Selezione multi-categoria merceologica (`Hardware`, `Software`, `Servizi`, `Cancelleria`).
  * Selezione per canale distributivo (`Agente Diretto`, `E-commerce B2B`, `Email/Telefono`, `Partner Commerciale`).
  * Selettore di intervallo date (`st.date_input`).
* **KPI Metrics Cards Superiori:**
  * Fatturato Netto Totale (€)
  * Volume Totale Ordini
  * Ticket Medio per Transazione (€)
  * Sconto Medio Concesso (%)
  * Pezzi Totali Venduti
* **Scheda 1: Panoramica & Trend:**
  * Grafico a linee multi-filiale del trend mensile di fatturato.
  * Grafico a barre orizzontali del fatturato per categoria prodotto.
* **Scheda 2: Clienti & Settori:**
  * Tabella dinamica dei Top 10 Clienti formattata con valuta euro e percentuali.
  * Grafico a torta/ciambella della quota di fatturato per settore merceologico.
* **Scheda 3: Simulatore What-If:**
  * Cursori interattivi per simulare variazioni di volume vendite (+/- 50%) e scostamenti di sconto (+/- 15%).
  * Ricalcolo in tempo reale del fatturato previsionale con delta assoluto e percentuale.
* **Scheda 4: Dati & Export:**
  * Visualizzazione tabellare dinamica con ordinamento e filtro di ricerca full-text.
  * Pulsante per il download istantaneo del dataset filtrato in formato CSV.

---

## 🚀 Come Avviare la Dashboard

```bash
# Assicurarsi che l'ambiente virtuale sia attivo
source .venv/bin/activate

# Avvio applicazione Streamlit
streamlit run dashboard/app.py
```
L'applicazione risponderà all'indirizzo locale: `http://localhost:8501`.
