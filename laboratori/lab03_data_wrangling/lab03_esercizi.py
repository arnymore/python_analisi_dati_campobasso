"""
=============================================================================
LABORATORIO 3: DATA WRANGLING, PULIZIA E INTEGRAZIONE (3 Ore)
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================

OBIETTIVI:
1. Rilevare ed eliminare i record duplicati (`drop_duplicates`).
2. Gestire valori nulli/mancanti (`isna()`, `fillna()`, `dropna()`) con strategie mirate.
3. Risolvere date eterogenee (ISO, formati IT, date seriali Excel) in oggetti datetime uniformi.
4. Normalizzare stringhe e categorie usando dizionari di mappatura e regex.
5. Integrare i dati di vendita con l'anagrafica clienti ufficiale tramite `pd.merge()`.
6. Eseguire aggregazioni avanzate con `groupby()` e `agg()`.

CASO AZIENDALE:
I dati grezzi di `dataset/roma.xlsx` contengono incongruenze (nomi clienti sporchi,
date con formati diversi, valori mancanti e duplicati).
Dobbiamo ripulire completamente il dataset, agganciare le informazioni sui clienti (Settore, Rating)
e calcolare i KPI di vendita affidabili.
=============================================================================
"""

import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FILE_ROMA = os.path.join(BASE_DIR, "dataset", "raw", "roma.xlsx")

# ---------------------------------------------------------------------------
# ESERCIZIO 3.1: Individuazione e Rimozione Duplicati
# ---------------------------------------------------------------------------
# Consegna:
# 1. Carica il foglio 'Dati_Vendite' di `dataset/roma.xlsx`.
# 2. Conta quanti duplicati esatti sono presenti nel DataFrame.
# 3. Rimuovi i duplicati mantenendo la prima occorrenza (`keep='first'`).

# TODO: Scrivi il codice qui


# ---------------------------------------------------------------------------
# ESERCIZIO 3.2: Pulizia Stringhe e Normalizzazione Categorie
# ---------------------------------------------------------------------------
# Consegna:
# 1. Rimuovi gli spazi iniziali e finali dai campi `Codice_Cliente` e `Ragione_Sociale`.
# 2. Porta `Codice_Cliente` in maiuscolo.
# 3. Normalizza `Categoria_Prodotto` riconducendo le varianti (es. 'HW', 'Softwre', 'Servizi IT')
#    alle 4 categorie standard: 'Hardware', 'Software', 'Servizi', 'Cancelleria'.

# TODO: Scrivi il codice qui


# ---------------------------------------------------------------------------
# ESERCIZIO 3.3: Parsing e Normalizzazione Date Disomogenee
# ---------------------------------------------------------------------------
# Consegna:
# Il campo `Data_Vendita` contiene stringhe ISO ('2024-03-15'), formati italiani ('15/03/2024'),
# mesi testuali ('15-Mar-2024') e numeri seriali Excel (es. '45365').
#
# Scrivi una funzione di parsing e converti l'intera colonna in `datetime64[ns]`.
# Estrai le colonne: `Anno`, `Mese`, `Mese_Nome`, `Trimestre`.

# TODO: Scrivi il codice qui


# ---------------------------------------------------------------------------
# ESERCIZIO 3.4: Gestione Valori Mancanti e Ricalcolo Fatturato
# ---------------------------------------------------------------------------
# Consegna:
# 1. Analizza i valori mancanti per ogni colonna.
# 2. Per `Quantita`: se mancante, imputa il valore mediano per prodotto.
# 3. Per `Prezzo_Unitario`: pulisci eventuali simboli '€' e virgole, converti in float,
#    e imputa i valori mancanti con la media di prezzo di quel prodotto.
# 4. Ricalcola `Fatturato_Netto` = `Quantita` * `Prezzo_Unitario` * (1 - `Sconto_Perc`/100).

# TODO: Scrivi il codice qui


# ---------------------------------------------------------------------------
# ESERCIZIO 3.5: Merge con Anagrafica Clienti e GroupBy
# ---------------------------------------------------------------------------
# Consegna:
# 1. Carica il foglio 'Anagrafica_Clienti' da `dataset/roma.xlsx`.
# 2. Esegui una `merge` (left join) tra il DataFrame vendite pulito e l'anagrafica
#    utilizzando la chiave `Codice_Cliente`.
# 3. Esegui una `groupby()` per `Settore` e calcola:
#    - Somma del Fatturato Netto
#    - Media dello Sconto Percentuale
#    - Conteggio Transazioni
# 4. Ordina per fatturato decrescente.

# TODO: Scrivi il codice qui


if __name__ == "__main__":
    print("Esegui il laboratorio 3!")
