# 📊 Dataset Generated (Output delle Pipeline e Report)

Questa cartella raccoglie tutti i file prodotti automaticamente dalle pipeline di elaborazione ETL, dagli script di visualizzazione e dalle sessioni di laboratorio.

---

## 📁 File Generati

| File | Tipologia | Descrizione |
| :--- | :--- | :--- |
| `vendite_consolidate_italia.parquet` | Apache Parquet | Database unificato e ottimizzato delle 3 filiali storiche (Roma, Milano, Torino). Usato dalla Dashboard Streamlit. |
| `vendite_consolidate_nazionale_4filiali.parquet` | Apache Parquet | Database consolidato nazionale a 4 filiali (inclusa Napoli) generato dal Project Work. |
| `report_direzionale_consolidato.xlsx` | Microsoft Excel | Report multi-scheda per il CdA (`Dettaglio_Transazioni`, `Riepilogo_Filiali`, `Riepilogo_Categorie`, `Riepilogo_Settori`). |
| `executive_report.png` | Immagine PNG (300 DPI) | Executive Dashboard 2x2 multi-plot generata dal Laboratorio 4. |
| `ex4_1_top_clienti.png` | Immagine PNG | Grafico a barre orizzontali dei Top Clienti per fatturato. |
| `ex4_2_trend_mensile.png` | Immagine PNG | Serie storica mensile con linea di media annuale. |
| `ex4_3_heatmap_matrice.png` | Immagine PNG | Matrice di calore Canale di Vendita vs Categoria Prodotto. |
| `pw_confronto_filiali.png` | Immagine PNG | Benchmark quote fatturato delle 4 filiali (Project Work). |
| `pw_trend_mensile_4filiali.png` | Immagine PNG | Confronto trend mensile multi-linea tra le 4 filiali (Project Work). |
| `pw_heatmap_filiale_categoria.png` | Immagine PNG | Heatmap di correlazione Filiale x Categoria Prodotto (Project Work). |

---

## 🔄 Come Rigenerare gli Output

Per rigenerare tutti i file da riga di comando:

```bash
# 1. Rigenerare i file consolidati standard (3 filiali) ed Excel direzionale:
python soluzioni/sol05_automazione_pipeline.py

# 2. Rigenerare i grafici di reporting Modulo 4:
python soluzioni/sol04_visualizzazione.py

# 3. Rigenerare il master consolidato a 4 filiali e i grafici di benchmark:
python project_work/soluzione_project_work.py
```
