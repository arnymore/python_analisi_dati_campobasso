"""
=============================================================================
LABORATORIO 2: PANDAS - FONDAMENTI E MANIPOLAZIONE DATAFRAME (4 Ore)
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================

OBIETTIVI:
1. Caricare file Excel complessi e fogli multipli con `pd.read_excel`.
2. Esplorare la struttura del DataFrame (`info()`, `describe()`, `shape`, `head()`).
3. Selezionare colonne e filtrare righe con condizioni logiche multiple (AND `&`, OR `|`).
4. Utilizzare l'indicizzazione avanzata con `.loc` e `.iloc`.
5. Creare nuove colonne calcolate (Fatturato Lordo, Valore Sconto, Fatturato Netto).
6. Ordinare i dati (`sort_values()`) per individuare i top deal commerciali.

CASO AZIENDALE:
La direzione commerciale vuole una prima panoramica delle vendite della filiale di Roma (`dataset/roma.xlsx`).
Dobbiamo caricare i dati, esplorare la consistenza del dataset, estrarre gli ordini ad alto valore
e analizzare i prezzi e gli sconti concessi.
=============================================================================
"""

import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FILE_ROMA = os.path.join(BASE_DIR, "dataset", "raw", "roma.xlsx")

# ---------------------------------------------------------------------------
# ESERCIZIO 2.1: Importazione ed Esplorazione Iniziale
# ---------------------------------------------------------------------------
# Consegna:
# 1. Carica il foglio 'Dati_Vendite' di `dataset/roma.xlsx` in un DataFrame chiamato `df_roma`.
# 2. Stampa:
#    - Il numero totale di righe e colonne.
#    - I tipi di dato delle singole colonne.
#    - Le prime 5 righe e le ultime 5 righe.
#    - Il riepilogo statistico descrittivo per le colonne numeriche.

# TODO: Scrivi il codice qui


# ---------------------------------------------------------------------------
# ESERCIZIO 2.2: Selezione Colonne e Indicizzazione con .loc e .iloc
# ---------------------------------------------------------------------------
# Consegna:
# 1. Seleziona solo le colonne: `ID_Transazione`, `Data_Vendita`, `Ragione_Sociale`, `Nome_Prodotto`, `Fatturato_Lordo`.
# 2. Con `.iloc`, estrai le righe dalla 10 alla 20 (incluse) e le prime 4 colonne.
# 3. Con `.loc`, estrai le righe con indice da 0 a 10 e le colonne `Ragione_Sociale` e `Fatturato_Lordo`.

# TODO: Scrivi il codice qui


# ---------------------------------------------------------------------------
# ESERCIZIO 2.3: Filtri e Condizioni Booleane Avanzate
# ---------------------------------------------------------------------------
# Consegna:
# Estrai i seguenti sottoinsiemi di dati:
# 1. Tutti gli ordini con `Canale_Vendita` uguale a "E-commerce B2B".
# 2. Tutti gli ordini con `Quantita` >= 10 E `Sconto_Perc` > 0.
# 3. Tutti gli ordini che NON appartengono alla categoria "Cancelleria" con `Fatturato_Lordo` > 1500.

# TODO: Scrivi il codice qui


# ---------------------------------------------------------------------------
# ESERCIZIO 2.4: Creazione di Nuove Colonne e Ordinamento
# ---------------------------------------------------------------------------
# Consegna:
# Nota: Alcuni valori di Prezzo_Unitario potrebbero essere sporchi. Per questo esercizio,
# converti Prezzo_Unitario in numerico forzando gli errori a NaN (`pd.to_numeric(..., errors='coerce')`).
#
# 1. Calcola:
#    - `Totale_Lordo_Calcolato` = `Quantita` * `Prezzo_Unitario`
#    - `Valore_Sconto` = `Totale_Lordo_Calcolato` * (`Sconto_Perc` / 100)
#    - `Fatturato_Netto` = `Totale_Lordo_Calcolato` - `Valore_Sconto`
# 2. Ordina il DataFrame per `Fatturato_Netto` in ordine decrescente.
# 3. Mostra i primi 10 ordini con il fatturato netto più alto (Top 10 Deals).

# TODO: Scrivi il codice qui


if __name__ == "__main__":
    print("Esegui il laboratorio 2!")
