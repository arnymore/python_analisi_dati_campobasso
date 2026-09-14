# 📂 Dataset Raw (Dati Grezzi di Input)

Questa cartella contiene i dataset operativi forniti per le esercitazioni del corso.

---

## 📄 File Disponibili

| File | Descrizione | Record | Scopo Didattico |
| :--- | :--- | :---: | :--- |
| `roma.xlsx` | Transazioni commerciali e anagrafica della filiale di Roma | ~1.200 | Dataset principale per i Moduli 2, 3 e 4. |
| `milano.xlsx` | Transazioni commerciali e anagrafica della filiale di Milano | ~1.500 | Dataset per l'automazione della pipeline (Modulo 5). |
| `torino.xlsx` | Transazioni commerciali e anagrafica della filiale di Torino | ~900 | Dataset per l'automazione della pipeline (Modulo 5). |
| `napoli_project_work.xlsx` | Transazioni commerciali e anagrafica della filiale di Napoli | ~1.100 | Dataset dedicato al **Project Work Finale** (Modulo 8). |

---

## 🔍 Struttura dei Fogli Excel

Ciascun file Excel contiene due fogli di lavoro:

### 1. Foglio `Dati_Vendite`
* `ID_Transazione`: Identificativo univoco della transazione (es. `RO-20240001`).
* `Data_Vendita`: Formati di data eterogenei (ISO, IT, seriali Excel, formati testuali).
* `Codice_Cliente`: Codice cliente (con spazi o minuscole per esercitare la pulizia).
* `Ragione_Sociale`: Nome azienda cliente con refusi ed etichette sporche.
* `Filiale`: Città della sede commerciale (`Roma`, `Milano`, `Torino`, `Napoli`).
* `Categoria_Prodotto`: Categoria merceologica (`Hardware`, `Software`, `Servizi`, `Cancelleria`).
* `Nome_Prodotto`: Articolo venduto.
* `Quantita`: Numero unità (con valori nulli da imputare).
* `Prezzo_Unitario`: Prezzo di vendita (numerico o stringa con valuta `€` e virgole).
* `Sconto_Perc`: Sconto concordato (0%, 5%, 10%, 15%, 20%).
* `Fatturato_Lordo`: Imponibile lordo (o da ricalcolare).
* `Canale_Vendita`: Canale distributivo (`Agente Diretto`, `E-commerce B2B`, `Email/Telefono`, `Partner Commerciale`).
* `Note`: Note commerciali e logistiche.

### 2. Foglio `Anagrafica_Clienti`
* `Codice_Cliente`: Chiave primaria per la `merge`.
* `Ragione_Sociale_Ufficiale`: Denominazione formale standard.
* `Settore`: Settore di business (`Information Technology`, `Sanità`, `Manifatturiero`, ecc.).
* `Citta_Sede`: Sede legale del cliente.
* `Rating_Affidabilita`: Classe di merito creditizio (`A+`, `A`, `B+`, `B`).

---

## ⚠️ Nota Didattica sui 'Dirty Data'
I dati contengono volutamente duplicati, anomalie di formato e valori nulli per simulare lo scenario reale di dati aziendali estratti da gestionali legacy.
