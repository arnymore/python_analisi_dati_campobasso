# ⏱️ PIANO DI GESTIONE DEI TEMPI & SCANSIONE ORARIA (22 ORE)
## Corso: Laboratorio Python + Analisi Dati
### Docente: Arnaldo Morena • ITIS Campobasso

---

## 🎯 Panoramica della Distribuzione Didattica
Il corso ha una durata complessiva certificata di **22 Ore** (1.320 minuti netti). La metodologia adottata è un modello **Hands-On (40% Spiegazione / Live Demo - 60% Laboratorio Attivo)**.

```text
┌────────────────────────────────────────────────────────────┐
│                    DISTRIBUZIONE 22 ORE                   │
├──────────────────────────┬───────┬────────────┬────────────┤
│ Modulo                   │ Ore   │ Teoria/Demo│ Laboratorio│
├──────────────────────────┼───────┼────────────┼────────────┤
│ Modulo 1 - Python Operat.│ 2h    │ 45 min     │ 75 min     │
│ Modulo 2 - Pandas Fondam.│ 4h    │ 90 min     │ 150 min    │
│ Modulo 3 - Data Wrangling│ 3h    │ 65 min     │ 115 min    │
│ Modulo 4 - Visualizzaz.  │ 3h    │ 65 min     │ 115 min    │
│ Modulo 5 - Automazione   │ 2h    │ 40 min     │ 80 min     │
│ Modulo 6 - Streamlit     │ 4h    │ 85 min     │ 155 min    │
│ Modulo 7 - Deploy Linux  │ 1h    │ 45 min     │ 15 min     │
│ Project Work Finale      │ 3h    │ 20 min     │ 160 min    │
├──────────────────────────┼───────┼────────────┼────────────┤
│ TOTALE                   │ 22h   │ ~ 7.5h     │ ~ 14.5h    │
└──────────────────────────┴───────┴────────────┴────────────┘
```

---

# 📅 CRONOPROGRAMMA DETTAGLIATO MODULO PER MODULO

## 🔵 MODULO 1: Python Operativo (2 Ore • 120 min)
| Minuti | Attività Didattica | Tipologia | Obiettivo Operativo |
| :---: | :--- | :---: | :--- |
| `00 - 15` | Accoglienza, patto d'aula, introduzione TechStore Italia | Lezione | Allineamento aspettative e obiettivi |
| `15 - 35` | Tipi nativi, collezioni `List[Dict]`, funzioni e calcolo KPI | Live Demo | Implementazione `calcola_totale_riga()` |
| `35 - 50` | String manipulation, acronimi societari, list comprehension | Live Demo | Pulizia ragioni sociali e filtri |
| `50 - 95` | **Laboratorio 1:** Esercizi 1.1, 1.2, 1.3, 1.4 | Hands-On | Autonomia su accumulo dizionari |
| `95 - 110` | Correzione collettiva e debriefing errori comuni | Revisione | Fissaggio concetti e best practice |
| `110 - 120` | **Buffer & Q&A:** Consolidamento e ponte a Pandas | Buffer | Risoluzione dubbi e transizione |

---

## 🟢 MODULO 2: Pandas Fondamentale (4 Ore • 240 min)
| Minuti | Attività Didattica | Tipologia | Obiettivo Operativo |
| :---: | :--- | :--- :---: | :--- |
| `00 - 40` | Architettura Series vs DataFrame, importazione da Excel | Lezione/Demo | `pd.read_excel`, `.shape`, `.info()` |
| `40 - 75` | Indicizzazione ed estrazione: `.loc` vs `.iloc`, slicing | Live Demo | Selezione mirata di righe e colonne |
| `75 - 115` | **Laboratorio 2 (Parte 1):** Esercizi 2.1 e 2.2 | Hands-On | Ispezione e selezioni posizionali |
| `115 - 130` | *Pausa Caffè Rigenerativa* | Pausa | Recupero energie |
| `130 - 165` | Filtri booleani composti (`&`, `|`), View vs Copy e `.copy()` | Live Demo | Eliminare `SettingWithCopyWarning` |
| `165 - 205` | **Laboratorio 2 (Parte 2):** Esercizi 2.3 e 2.4 (Top Deals) | Hands-On | Colonne calcolate e ordinamenti |
| `205 - 225` | Discussione Top 10 Deals ed estrazione insight | Revisione | Interpretazione di business del dato |
| `225 - 240` | **Buffer & Q&A:** Verifica setup su tutte le postazioni | Buffer | Recupero studenti in ritardo |

---

## 🟠 MODULO 3: Data Wrangling & Qualità del Dato (3 Ore • 180 min)
| Minuti | Attività Didattica | Tipologia | Obiettivo Operativo |
| :---: | :--- | :--- :---: | :--- |
| `00 - 35` | Deduplicazione, analisi missing values, imputazione con mediana | Live Demo | `drop_duplicates()`, `fillna()` |
| `35 - 65` | Parsing date disomogenee (`parse_data_flessibile`) e feature tempo | Live Demo | Gestione seriali Excel e stringhe italiane |
| `65 - 100` | **Laboratorio 3 (Parte 1):** Pulizia, date e imputazione prezzi | Hands-On | Bonifica completa dataset Roma |
| `100 - 130` | Merge relazionale con anagrafica, validazione `many_to_one` | Live Demo | Prevenire esplosione cartesiana |
| `130 - 165` | **Laboratorio 3 (Parte 2):** Merge e GroupBy settoriale | Hands-On | Aggregazioni aggregate con `.agg()` |
| `165 - 180` | **Buffer & Validazione:** Verifica coerenza record | Buffer | Controllo asserzioni numeriche |

---

## 🟣 MODULO 4: Visualizzazione & Reporting Esecutivo (3 Ore • 180 min)
| Minuti | Attività Didattica | Tipologia | Obiettivo Operativo |
| :---: | :--- | :--- :---: | :--- |
| `00 - 35` | Architettura OOP Matplotlib (`fig, ax`), Barh per Top Clienti | Live Demo | Etichette sui vertici, layout pulito |
| `35 - 65` | Seaborn: lineplot con medie, boxplot sconti, heatmap matrici | Live Demo | Grafici statistici avanzati |
| `65 - 105` | **Laboratorio 4 (Parte 1):** Grafici 4.1, 4.2 e 4.3 | Hands-On | Generazione singoli grafici su file |
| `105 - 135` | Composizione dell'Executive Dashboard 2x2 ed export 300 DPI | Live Demo | Layout a 4 pannelli coordinati |
| `135 - 165` | **Laboratorio 4 (Parte 2):** Assemblaggio dashboard 2x2 | Hands-On | Finalizzazione file `executive_report.png` |
| `165 - 180` | **Buffer & Feedback:** Revisione grafica dei report | Buffer | Allineamento estetico e leggibilità |

---

## 🔴 MODULO 5: Automazione della Pipeline ETL (2 Ore • 120 min)
| Minuti | Attività Didattica | Tipologia | Obiettivo Operativo |
| :---: | :--- | :--- :---: | :--- |
| `00 - 25` | Pattern di scansione batch con `glob`, filtro lock file (`~$`) | Live Demo | Ingestione multi-file automatizzata |
| `25 - 45` | Storage Parquet compresso (Snappy) vs Excel, logging di produzione | Live Demo | `.to_parquet()`, modulo `logging` |
| `45 - 90` | **Laboratorio 5:** Scrittura ed esecuzione script ETL completo | Hands-On | Generazione master Parquet e report Excel |
| `90 - 110` | Test da riga di comando con argomenti CLI (`argparse`) | Live Demo/Lab | Esecuzione parametrica da terminale |
| `110 - 120` | **Buffer:** Controllo dimensioni file e tempi di lettura | Buffer | Verifica performance Parquet |

---

## 🟡 MODULO 6: Dashboard Interattiva Streamlit (4 Ore • 240 min)
| Minuti | Attività Didattica | Tipologia | Obiettivo Operativo |
| :---: | :--- | :--- :---: | :--- |
| `00 - 45` | Modello reattivo Streamlit, ciclo di vita, caching `@st.cache_data` | Live Demo | Setup pagina wide e lettura cached |
| `45 - 80` | Sidebar, selettori multi-filiale, filtri data, KPI cards in colonne | Live Demo | `st.sidebar`, `st.columns`, `st.metric` |
| `80 - 120` | **Laboratorio 6 (Parte 1):** Costruzione struttura e filtri | Hands-On | Interfaccia base reattiva funzionante |
| `120 - 135` | *Pausa Rigenerativa* | Pausa | Recupero concentrazione |
| `135 - 165` | Navigazione Multi-Tab, grafici dinamici, What-If simulator, export | Live Demo | `st.tabs`, simulatore di scenario, download |
| `165 - 215` | **Laboratorio 6 (Parte 2):** Implementazione What-If ed export | Hands-On | Completamento applicazione `app.py` |
| `215 - 240` | **Buffer & Demo:** Presentazione incrociata delle dashboard | Buffer | Test utente interattivo |

---

## 🟤 MODULO 7: Deploy Linux & Systemd (1 Ora • 60 min)
*Modalità: Live Demo Guidata dal Docente*
| Minuti | Attività Didattica | Tipologia | Obiettivo Operativo |
| :---: | :--- | :--- :---: | :--- |
| `00 - 15` | Architettura Cloud/Server, limiti sessioni SSH, concetto di demone | Lezione | Comprensione del ciclo di vita in produzione |
| `15 - 30` | Creazione dell'unit file `/etc/systemd/system/dashboard_vendite.service` | Live Demo | Sintassi Unit File, policy `Restart=always` |
| `30 - 45` | Attivazione servizio (`systemctl enable --now`) e streaming log (`journalctl -f`)| Live Demo | Controllo operativo demone in tempo reale |
| `45 - 55` | Test di resilienza: uccisione forzata del processo e riavvio automatico | Live Demo | Dimostrazione della robustezza Systemd |
| `55 - 60` | Cenni su Nginx Reverse Proxy (porte 80/443 SSL) e Q&A | Discussione | Quadro architetturale enterprise completo |

---

## 🏁 PROJECT WORK FINALE: Filiale Napoli (3 Ore • 180 min)
| Minuti | Attività Didattica | Tipologia | Obiettivo Operativo |
| :---: | :--- | :--- :---: | :--- |
| `00 - 20` | Consegna della traccia, spiegazione dei 4 deliverable e benchmark | Presentazione | Comprensione dei requisiti aziendali |
| `20 - 75` | **Fase 1:** Audit e pulizia dati filiale Napoli (1.000 record netti) | Lavoro Autonomo | Bonifica anomalie e verifica € 1.042.850,50 |
| `75 - 125` | **Fase 2:** Esecuzione ETL a 4 filiali, generazione Parquet (4.552 righe) | Lavoro Autonomo | Consolidamento master e report Excel |
| `125 - 155` | **Fase 3:** Aggiornamento dashboard Streamlit e verifica grafici | Lavoro Autonomo | Test interattivo con filtro Napoli attivo |
| `155 - 170` | Valutazione e confronto con benchmark del docente (100 pt) | Valutazione | Certificazione competenze acquisite |
| `170 - 180` | Conclusioni finali del corso, feedback e rilascio attestati | Chiusura | Termine del percorso formativo |

---

# 🛡️ STRATEGIE DI RECUPERO RITARDI & ACCELERATORI D'AULA

### Scenario A: L'aula è in ritardo sulla tabella di marcia (-30 min)
1. **Modulo 2:** Ridurre l'esercitazione sui filtri concentrandosi solo sull'Esercizio 2.3 e 2.4 (i più qualificanti).
2. **Modulo 3:** Fornire la funzione `parse_data_flessibile()` pre-scritta nel notebook invece di farla digitare da zero, concentrando l'attenzione sul merge relazionale.
3. **Modulo 4:** Limitare la dashboard 2x2 a 2 grafici essenziali (Trend + Boxplot) rimandando i restanti alla consultazione della soluzione.

### Scenario B: L'aula è particolarmente avanzata (+30 min di anticipo)
1. **Approfondimento Modulo 3:** Introdurre l'imputazione contestuale per categoria tramite `df.groupby('Categoria')['Prezzo'].transform('median')`.
2. **Approfondimento Modulo 4:** Mostrare come salvare il grafico in formato vettoriale PDF/SVG per stampe ad altissima fedeltà.
3. **Approfondimento Modulo 6:** Aggiungere un grafico a barre interattivo Plotly in Streamlit (`st.plotly_chart`).
4. **Approfondimento Modulo 7:** Mostrare la configurazione di un virtual host di base in Nginx (`/etc/nginx/sites-available/streamlit`).

---
