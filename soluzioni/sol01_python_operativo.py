"""
=============================================================================
SOLUZIONE UFFICIALE: LABORATORIO 1 - PYTHON OPERATIVO
Docente: Arnaldo Morena
Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
=============================================================================
"""

import re

# ---------------------------------------------------------------------------
# ESERCIZIO 1.1: Calcolo KPI Commerciali e Funzioni
# ---------------------------------------------------------------------------
def calcola_totale_riga(quantita, prezzo_unitario, sconto_perc=0, aliquota_iva=0.22):
    imponibile_lordo = quantita * prezzo_unitario
    importo_sconto = imponibile_lordo * (sconto_perc / 100.0)
    imponibile_netto = imponibile_lordo - importo_sconto
    iva = imponibile_netto * aliquota_iva
    totale_fattura = imponibile_netto + iva
    
    return {
        'imponibile_lordo': round(imponibile_lordo, 2),
        'importo_sconto': round(importo_sconto, 2),
        'imponibile_netto': round(imponibile_netto, 2),
        'iva': round(iva, 2),
        'totale_fattura': round(totale_fattura, 2)
    }

print("--- Test Esercizio 1.1 ---")
res = calcola_totale_riga(quantita=5, prezzo_unitario=850.0, sconto_perc=10)
print("Risultato riga d'ordine:", res)


# ---------------------------------------------------------------------------
# ESERCIZIO 1.2: Elaborazione di un Ordine Multi-Riga
# ---------------------------------------------------------------------------
ordine_grezzo = [
    {"prodotto": "Server Rack 24U", "categoria": "Hardware", "qta": 2, "prezzo": 1850.00, "sconto": 10},
    {"prodotto": "Licenza ERP Annuale", "categoria": "Software", "qta": 1, "prezzo": 1200.00, "sconto": 0},
    {"prodotto": "Consulenza Sistemistica", "categoria": "Servizi", "qta": 8, "prezzo": 75.00, "sconto": 5},
    {"prodotto": "Laptop Business 15\"", "categoria": "Hardware", "qta": 3, "prezzo": 850.00, "sconto": 5},
]

totale_netto_ordine = 0.0
totale_iva_ordine = 0.0
totale_complessivo = 0.0

for riga in ordine_grezzo:
    dett = calcola_totale_riga(riga["qta"], riga["prezzo"], riga["sconto"])
    totale_netto_ordine += dett["imponibile_netto"]
    totale_iva_ordine += dett["iva"]
    totale_complessivo += dett["totale_fattura"]

solo_hardware = [r for r in ordine_grezzo if r["categoria"] == "Hardware"]

print("\n--- Test Esercizio 1.2 ---")
print(f"Fatturato Netto Ordine: {totale_netto_ordine:.2f} €")
print(f"Totale IVA:             {totale_iva_ordine:.2f} €")
print(f"Totale Fattura:         {totale_complessivo:.2f} €")
print(f"Articoli Hardware filtrati ({len(solo_hardware)}):", [p["prodotto"] for p in solo_hardware])


# ---------------------------------------------------------------------------
# ESERCIZIO 1.3: Normalizzazione Nomi Clienti
# ---------------------------------------------------------------------------
clienti_sporchi = [
    "  tech solutions srl  ",
    "STUDIO ROSSI & ASSOCIATI",
    "   logistica  molise   spa ",
    "manifattura adriatica snc",
    "   HOTEL SAMNIUM   "
]

def normalizza_ragione_sociale(testo):
    if not testo:
        return ""
    # Rimuove spazi multipli interni e strip
    pulito = " ".join(testo.strip().split())
    # Capitalizza le parole (Title Case)
    parole = pulito.split()
    parole_formattate = []
    acronimi = {"srl": "Srl", "spa": "SpA", "snc": "snc", "s.r.l.": "S.r.l.", "s.p.a.": "S.p.a."}
    for p in parole:
        if p.lower() in acronimi:
            parole_formattate.append(acronimi[p.lower()])
        else:
            parole_formattate.append(p.capitalize())
    return " ".join(parole_formattate)

print("\n--- Test Esercizio 1.3 ---")
clienti_puliti = [normalizza_ragione_sociale(c) for c in clienti_sporchi]
for orig, pul in zip(clienti_sporchi, clienti_puliti):
    print(f"Originale: '{orig}' -> Pulito: '{pul}'")


# ---------------------------------------------------------------------------
# ESERCIZIO 1.4: Raggruppamento e Aggregazione con Dizionari Nativi
# ---------------------------------------------------------------------------
vendite_mensili = [
    {"categoria": "Hardware", "qta": 5, "prezzo": 850.0},
    {"categoria": "Software", "qta": 10, "prezzo": 150.0},
    {"categoria": "Hardware", "qta": 2, "prezzo": 1850.0},
    {"categoria": "Servizi", "qta": 15, "prezzo": 75.0},
    {"categoria": "Software", "qta": 3, "prezzo": 1200.0},
    {"categoria": "Hardware", "qta": 4, "prezzo": 280.0},
]

aggregato = {}

for r in vendite_mensili:
    cat = r["categoria"]
    fatturato_riga = r["qta"] * r["prezzo"]
    if cat not in aggregato:
        aggregato[cat] = {"qta_totale": 0, "fatturato_totale": 0.0, "numero_ordini": 0}
    aggregato[cat]["qta_totale"] += r["qta"]
    aggregato[cat]["fatturato_totale"] += fatturato_riga
    aggregato[cat]["numero_ordini"] += 1

print("\n--- Test Esercizio 1.4 ---")
for cat, metriche in aggregato.items():
    print(f"Categoria: {cat:12} | Qta: {metriche['qta_totale']:3} | Fatturato: {metriche['fatturato_totale']:10.2f} € | N. Ordini: {metriche['numero_ordini']}")
