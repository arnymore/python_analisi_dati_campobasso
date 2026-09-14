# 🎓 Project Work Finale (3 Ore)

Questa cartella raccoglie tutto il materiale necessario per lo svolgimento e la valutazione del **Project Work Finale** del corso.

---

## 🏢 Scenario di Business

Nel corso dell'ultimo trimestre, l'azienda ha espanso la propria rete commerciale inaugurando la nuova filiale di **Napoli**.  
I dati delle vendite del primo anno della sede di Napoli sono stati raccolti nel dataset grezzo:
`dataset/raw/napoli_project_work.xlsx`

Gli studenti, lavorando singolarmente o in piccoli team, devono:
1. Effettuare la pulizia (wrangling) del dataset di Napoli.
2. Integrare Napoli nella pipeline aziendale per ottenere un database consolidato a **4 filiali** (Roma, Milano, Torino, Napoli).
3. Rispondere ai quesiti strategici della Direzione Generale (benchmark quote, analisi canali, top categorie).
4. Produrre i grafici direzionali ad alta risoluzione ed estendere la dashboard interattiva.

---

## 📄 File Inclusi

| File | Destinatario | Descrizione |
| :--- | :--- | :--- |
| `traccia_studenti.md` | Studenti | Documento formale con la traccia, le specifiche tecniche e i requisiti di consegna. |
| `criteri_valutazione.md` | Docente / Studenti | Rubrica di valutazione analitica a 100 punti (Wrangling, Integrazione, KPI, Grafici, Qualità Codice). |
| `soluzione_project_work.py` | Docente | Codice Python completo ed eseguibile con la soluzione di riferimento e la generazione dei report grafici. |

---

## 🚀 Esecuzione Soluzione di Riferimento

```bash
python project_work/soluzione_project_work.py
```
Questo genererà il master `dataset/generated/vendite_consolidate_nazionale_4filiali.parquet` e i grafici di benchmark in `dataset/generated/`.
