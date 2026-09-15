"""
=============================================================================
VERSIONE DOCENTE COMMENTATA: LABORATORIO 1 - PYTHON OPERATIVO
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================

STRUTTURA DEI COMMENTI A 4 LIVELLI DIDATTICI:
- LIVELLO 1 [TECNICO]: Sintassi, tipi, strutture dati e funzioni.
- LIVELLO 2 [BUSINESS]: Significato economico, logiche ERP e contabili.
- LIVELLO 3 [DOCENTE]: Regia d'aula, domande da fare, pause strategiche.
- LIVELLO 4 [COLLEGAMENTO DIDATTICO]: Ponti concettuali verso i moduli successivi.
=============================================================================
"""

import re

# ---------------------------------------------------------------------------
# ESERCIZIO 1.1: Calcolo KPI Commerciali e Funzioni
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Introdurre l'esercizio chiedendo: "Come calcola un gestionale ERP il totale di
# una riga d'ordine prima di applicare l'IVA?"
# Spiegare perché usiamo parametri con valori di default (es. sconto_perc=0, aliquota_iva=0.22).

# LIVELLO 1 [TECNICO]:
# Funzione pura con argomenti posizionali e con valore di default (default arguments).
# Restituisce un dizionario contenente tutte le grandezze calcolate.
def calcola_totale_riga(quantita, prezzo_unitario, sconto_perc=0, aliquota_iva=0.22):
    # LIVELLO 2 [BUSINESS]:
    # L'imponibile lordo rappresenta il valore economico della merce a prezzo di listino pieno.
    imponibile_lordo = quantita * prezzo_unitario
    
    # LIVELLO 2 [BUSINESS]:
    # Lo sconto commerciale concesso al cliente riduce la base imponibile su cui calcolare le tasse.
    importo_sconto = imponibile_lordo * (sconto_perc / 100.0)
    
    # LIVELLO 2 [BUSINESS]:
    # Imponibile Netto: effettivo ricavo aziendale prima delle imposte di legge (IVA).
    imponibile_netto = imponibile_lordo - importo_sconto
    
    # LIVELLO 2 [BUSINESS]:
    # IVA (Imposta sul Valore Aggiunto): debito fiscale verso l'Erario, calcolato sull'imponibile netto.
    iva = imponibile_netto * aliquota_iva
    
    # LIVELLO 2 [BUSINESS]:
    # Totale Fattura: importo finanziario complessivo dovuto dal cliente.
    totale_fattura = imponibile_netto + iva
    
    # LIVELLO 4 [COLLEGAMENTO DIDATTICO]:
    # La restituzione di un dizionario con chiavi testuali anticipa la struttura delle colonne
    # che andremo a definire nei DataFrame di Pandas a partire dal Modulo 2.
    return {
        'imponibile_lordo': round(imponibile_lordo, 2),
        'importo_sconto': round(importo_sconto, 2),
        'imponibile_netto': round(imponibile_netto, 2),
        'iva': round(iva, 2),
        'totale_fattura': round(totale_fattura, 2)
    }

# LIVELLO 3 [DOCENTE]:
# Mostrare l'output a video e chiedere all'aula di verificare a mente i calcoli:
# 5 pezzi * 850€ = 4.250€ lordi; 10% sconto = 425€; netto = 3.825€; IVA 22% = 841.50€; totale = 4.666.50€.
print("--- Test Esercizio 1.1 ---")
res = calcola_totale_riga(quantita=5, prezzo_unitario=850.0, sconto_perc=10)
print("Risultato riga d'ordine:", res)


# ---------------------------------------------------------------------------
# ESERCIZIO 1.2: Elaborazione di un Ordine Multi-Riga
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Sottolineare che la struttura `ordine_grezzo` è una `List[Dict]`: la rappresentazione nativa
# più comune dei dati prima dell'uso di Pandas o database relazionali.

# LIVELLO 1 [TECNICO]:
# Lista di dizionari eterogenei: ogni elemento rappresenta una riga d'ordine indipendente.
ordine_grezzo = [
    {"prodotto": "Server Rack 24U", "categoria": "Hardware", "qta": 2, "prezzo": 1850.00, "sconto": 10},
    {"prodotto": "Licenza ERP Annuale", "categoria": "Software", "qta": 1, "prezzo": 1200.00, "sconto": 0},
    {"prodotto": "Consulenza Sistemistica", "categoria": "Servizi", "qta": 8, "prezzo": 75.00, "sconto": 5},
    {"prodotto": "Laptop Business 15\"", "categoria": "Hardware", "qta": 3, "prezzo": 850.00, "sconto": 5},
]

# LIVELLO 1 [TECNICO]:
# Inizializzazione di variabili accumulatore scalari prima del ciclo iterativo.
totale_netto_ordine = 0.0
totale_iva_ordine = 0.0
totale_complessivo = 0.0

# LIVELLO 3 [DOCENTE]:
# Spiegare come il ciclo `for` scorre elemento per elemento e invoca la funzione pura del punto 1.1.
for riga in ordine_grezzo:
    dett = calcola_totale_riga(riga["qta"], riga["prezzo"], riga["sconto"])
    totale_netto_ordine += dett["imponibile_netto"]
    totale_iva_ordine += dett["iva"]
    totale_complessivo += dett["totale_fattura"]

# LIVELLO 1 [TECNICO] & LIVELLO 4 [COLLEGAMENTO DIDATTICO]:
# List comprehension con clausola condizionale `if`: filtra gli elementi in modo conciso ed elegante.
# Questo costrutto anticipa i filtri booleani di Pandas (`df[df['categoria'] == 'Hardware']`).
solo_hardware = [r for r in ordine_grezzo if r["categoria"] == "Hardware"]

print("\n--- Test Esercizio 1.2 ---")
print(f"Fatturato Netto Ordine: {totale_netto_ordine:.2f} €")
print(f"Totale IVA:             {totale_iva_ordine:.2f} €")
print(f"Totale Fattura:         {totale_complessivo:.2f} €")
print(f"Articoli Hardware filtrati ({len(solo_hardware)}):", [p["prodotto"] for p in solo_hardware])


# ---------------------------------------------------------------------------
# ESERCIZIO 1.3: Normalizzazione Nomi Clienti (Data Quality)
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Raccontare l'aneddoto aziendale: gli operatori inseriscono ragioni sociali con spazi superflui,
# lettere minuscole e acronimi errati (es. '  tech solutions srl  '). Senza pulizia, un raggruppamento
# considererebbe 'Tech Solutions Srl' e 'tech solutions srl' come due clienti differenti!

clienti_sporchi = [
    "  tech solutions srl  ",
    "STUDIO ROSSI & ASSOCIATI",
    "   logistica  molise   spa ",
    "manifattura adriatica snc",
    "   HOTEL SAMNIUM   "
]

# LIVELLO 1 [TECNICO]:
# Funzione di pulizia stringhe: usa `.strip()`, `.split()` per eliminare spazi multipli,
# e un dizionario per preservare le sigle societarie corrette.
def normalizza_ragione_sociale(testo):
    if not testo:
        return ""
    # LIVELLO 1 [TECNICO]:
    # `" ".join(testo.strip().split())` è un idiomatic Python per rimuovere sia gli spazi
    # iniziali/finali sia gli spazi multipli interni consecutivi.
    pulito = " ".join(testo.strip().split())
    
    # LIVELLO 2 [BUSINESS]:
    # Nelle anagrafiche aziendali italiane, le forme societarie (Srl, SpA, Snc) devono rispettare
    # la convenzione formale del Registro delle Imprese.
    parole = pulito.split()
    parole_formattate = []
    acronimi = {"srl": "Srl", "spa": "SpA", "snc": "snc", "s.r.l.": "S.r.l.", "s.p.a.": "S.p.a."}
    
    for p in parole:
        if p.lower() in acronimi:
            parole_formattate.append(acronimi[p.lower()])
        else:
            parole_formattate.append(p.capitalize())
            
    return " ".join(parole_formattate)

# LIVELLO 4 [COLLEGAMENTO DIDATTICO]:
# La list comprehension applicata a una lista di stringhe anticipa l'uso dei metodi vettoriali
# `.str.strip()` e `.str.title()` di Pandas nel Modulo 2 e 3.
print("\n--- Test Esercizio 1.3 ---")
clienti_puliti = [normalizza_ragione_sociale(c) for c in clienti_sporchi]
for orig, pul in zip(clienti_sporchi, clienti_puliti):
    print(f"Originale: '{orig}' -> Pulito: '{pul}'")


# ---------------------------------------------------------------------------
# ESERCIZIO 1.4: Raggruppamento e Aggregazione con Dizionari Nativi
# ---------------------------------------------------------------------------
# LIVELLO 3 [DOCENTE]:
# Questo è l'esercizio concettualmente più importante del Modulo 1.
# Spiegare all'aula: "Come possiamo calcolare il totale venduto per ogni categoria senza conoscere a priori quali categorie esistono?"
# Mostrare il pattern del 'dizionario di accumulo'.

vendite_mensili = [
    {"categoria": "Hardware", "qta": 5, "prezzo": 850.0},
    {"categoria": "Software", "qta": 10, "prezzo": 150.0},
    {"categoria": "Hardware", "qta": 2, "prezzo": 1850.0},
    {"categoria": "Servizi", "qta": 15, "prezzo": 75.0},
    {"categoria": "Software", "qta": 3, "prezzo": 1200.0},
    {"categoria": "Hardware", "qta": 4, "prezzo": 280.0},
]

# LIVELLO 1 [TECNICO]:
# Tabella hash vuota destinata ad ospitare le metriche aggregate per ogni categoria.
aggregato = {}

for r in vendite_mensili:
    cat = r["categoria"]
    fatturato_riga = r["qta"] * r["prezzo"]
    
    # LIVELLO 1 [TECNICO]:
    # Se la categoria non è ancora presente nel dizionario, la inizializziamo con valori a zero.
    if cat not in aggregato:
        aggregato[cat] = {"qta_totale": 0, "fatturato_totale": 0.0, "numero_ordini": 0}
        
    # LIVELLO 2 [BUSINESS]:
    # Accumuliamo le 3 metriche chiave: volumi fisici (qta), valore monetario (fatturato) e frequenza ordini.
    aggregato[cat]["qta_totale"] += r["qta"]
    aggregato[cat]["fatturato_totale"] += fatturato_riga
    aggregato[cat]["numero_ordini"] += 1

# LIVELLO 4 [COLLEGAMENTO DIDATTICO]:
# Questa logica algoritmica manuale è ESATTAMENTE ciò che fa internamente il metodo `df.groupby('categoria').agg()`
# di Pandas che vedremo nel Modulo 2 e 3, ma implementata a mano per comprendere il funzionamento sottostante.
print("\n--- Test Esercizio 1.4 ---")
for cat, metriche in aggregato.items():
    print(f"Categoria: {cat:12} | Qta: {metriche['qta_totale']:3} | Fatturato: {metriche['fatturato_totale']:10.2f} € | N. Ordini: {metriche['numero_ordini']}")
