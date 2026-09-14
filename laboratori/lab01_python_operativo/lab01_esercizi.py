"""
=============================================================================
LABORATORIO 1: PYTHON OPERATIVO PER L'ANALISI DATI (2 Ore)
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================

OBIETTIVI:
1. Padroneggiare le strutture dati native fondamentali: liste, dizionari, tuple.
2. Applicare cicli (for/while), condizioni logiche e list comprehension per trasformare dati.
3. Creare funzioni riutilizzabili per il calcolo di KPI commerciali (Sconti, IVA, Margini).
4. Manipolare stringhe per normalizzare dati anagrafici sporchi.

CASO AZIENDALE:
La nostra azienda commerciale distribuisce prodotti IT e servizi in tutta Italia.
Prima di passare a Pandas, dobbiamo automatizzare alcune logiche di calcolo e
ripulire piccoli elenchi di dati commerciali grezzi estratti dal gestionale.
=============================================================================
"""

# ---------------------------------------------------------------------------
# ESERCIZIO 1.1: Calcolo KPI Commerciali e Funzioni
# ---------------------------------------------------------------------------
# Consegna:
# Scrivi una funzione `calcola_totale_riga(quantita, prezzo_unitario, sconto_perc=0, aliquota_iva=0.22)`
# che:
# 1. Calcoli l'imponibile lordo (quantità * prezzo).
# 2. Applichi lo sconto percentuale se presente.
# 3. Calcoli l'IVA sull'importo scontato.
# 4. Restituisca un dizionario con le seguenti chiavi:
#    - 'imponibile_lordo'
#    - 'importo_sconto'
#    - 'imponibile_netto'
#    - 'iva'
#    - 'totale_fattura'
# Arrotonda tutti i valori a 2 cifre decimali.

def calcola_totale_riga(quantita, prezzo_unitario, sconto_perc=0, aliquota_iva=0.22):
    # TODO: Implementare il calcolo
    pass


# ---------------------------------------------------------------------------
# ESERCIZIO 1.2: Elaborazione di un Ordine Multi-Riga (Liste di Dizionari)
# ---------------------------------------------------------------------------
# Consegna:
# Dato il seguente carrello di vendita grezzo, calcola:
# 1. Il fatturato totale netto dell'ordine.
# 2. Il totale IVA.
# 3. Il totale complessivo fattura.
# 4. Crea una nuova lista con i soli articoli appartenenti alla categoria 'Hardware'.

ordine_grezzo = [
    {"prodotto": "Server Rack 24U", "categoria": "Hardware", "qta": 2, "prezzo": 1850.00, "sconto": 10},
    {"prodotto": "Licenza ERP Annuale", "categoria": "Software", "qta": 1, "prezzo": 1200.00, "sconto": 0},
    {"prodotto": "Consulenza Sistemistica", "categoria": "Servizi", "qta": 8, "prezzo": 75.00, "sconto": 5},
    {"prodotto": "Laptop Business 15\"", "categoria": "Hardware", "qta": 3, "prezzo": 850.00, "sconto": 5},
]

# TODO: Calcolare i totali iterando sull'elenco o usando comprehension


# ---------------------------------------------------------------------------
# ESERCIZIO 1.3: Pulizia e Normalizzazione Nomi Clienti
# ---------------------------------------------------------------------------
# Consegna:
# Nel CRM aziendale i nomi dei clienti sono stati inseriti con formattazioni disomogenee:
# spazi superflui all'inizio e alla fine, caratteri maiuscoli/minuscoli disallineati,
# doppie spaziatura interne.
#
# Scrivi una funzione `normalizza_ragione_sociale(testo)` che:
# 1. Rimuova spazi iniziali e finali (.strip()).
# 2. Trasformi il testo in Title Case (.title()) preservando acronimi noti come "SRL", "SPA", "SNC".
# 3. Rimuova doppi spazi interni.

clienti_sporchi = [
    "  tech solutions srl  ",
    "STUDIO ROSSI & ASSOCIATI",
    "   logistica  molise   spa ",
    "manifattura adriatica snc",
    "   HOTEL SAMNIUM   "
]

def normalizza_ragione_sociale(testo):
    # TODO: Implementare la normalizzazione
    pass


# ---------------------------------------------------------------------------
# ESERCIZIO 1.4: Raggruppamento e Aggregazione con Dizionari Nativi
# ---------------------------------------------------------------------------
# Consegna:
# Senza usare librerie esterne, raggruppa le vendite della lista `vendite_mensili`
# per categoria di prodotto e calcola per ciascuna:
# - Quantità totale venduta
# - Fatturato totale (qta * prezzo)

vendite_mensili = [
    {"categoria": "Hardware", "qta": 5, "prezzo": 850.0},
    {"categoria": "Software", "qta": 10, "prezzo": 150.0},
    {"categoria": "Hardware", "qta": 2, "prezzo": 1850.0},
    {"categoria": "Servizi", "qta": 15, "prezzo": 75.0},
    {"categoria": "Software", "qta": 3, "prezzo": 1200.0},
    {"categoria": "Hardware", "qta": 4, "prezzo": 280.0},
]

# TODO: Creare il dizionario aggregato: { 'Hardware': {'qta_tot': ..., 'fatturato_tot': ...}, ... }


if __name__ == "__main__":
    print("Esegui i tuoi test qui!")
