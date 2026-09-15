# 🐧 GUIDA DOCENTE COMMENTATA: DEPLOY SU LINUX & SYSTEMD
## Script di Riferimento: `soluzioni/sol07_deploy_linux.sh`
### Docente: Arnaldo Morena • ITIS Campobasso • Anno 2026

---

## 🎯 Obiettivo Didattico
Questa guida illustra la configurazione di un demone di produzione su sistema operativo Linux (Ubuntu/Debian) per ospitare l'applicazione Streamlit in modo permanente, resiliente ai crash e con avvio automatico al boot della macchina.

---

# 📜 ANALISI DETTAGLIATA DELLO SCRIPT BASH (`sol07_deploy_linux.sh`)

Di seguito viene analizzata ogni sezione dello script bash di installazione automatica, spiegandone il funzionamento tecnico, lo scopo architetturale e l'output atteso a terminale.

```bash
#!/usr/bin/env bash
# =============================================================================
# SCRIPT DI INSTALLAZIONE AUTOMATICA SERVIZIO SYSTEMD SU LINUX
# Docente: Arnaldo Morena
# Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
# =============================================================================
```

### 1. Flag di Sicurezza Bash
```bash
set -e
```
* **Spiegazione Tecnica:** La direttiva `set -e` impone alla shell bash di interrompere immediatamente l'esecuzione dello script non appena un comando restituisce un codice di uscita diverso da zero (errore).
* **Scopo Didattico:** Previene l'esecuzione a cascata di comandi successivi quando un passaggio critico (come la generazione di un file o la copia) è fallito.

---

### 2. Definizione delle Variabili d'Ambiente
```bash
APP_DIR="/home/arny/Projects/clients/itis_demos_campobasso/corso_python"
SERVICE_NAME="dashboard_vendite.service"
SERVICE_DST="/etc/systemd/system/${SERVICE_NAME}"
USER_RUN="arny"
```
* **`APP_DIR`:** Percorso assoluto della cartella radice del progetto, contenente sia l'ambiente virtuale (`.venv/`) sia la directory `dashboard/`.
* **`SERVICE_NAME`:** Nome identificativo dell'unità di servizio Systemd (`dashboard_vendite.service`).
* **`SERVICE_DST`:** Percorso standard di destinazione dei servizi di sistema gestiti dall'amministratore su Linux (`/etc/systemd/system/`).
* **`USER_RUN`:** Utente Linux non privilegiato con cui verrà eseguito il processo demone (principio di sicurezza del minimo privilegio).

---

### 3. Generazione Dinamica dell'Unit File Systemd
```bash
echo "=== 1. Generazione file systemd service in corso... ==="

cat <<EOF > /tmp/${SERVICE_NAME}
[Unit]
Description=Dashboard Direzionale Vendite ITIS Campobasso
After=network.target

[Service]
Type=simple
User=${USER_RUN}
WorkingDirectory=${APP_DIR}
ExecStart=${APP_DIR}/.venv/bin/streamlit run ${APP_DIR}/dashboard/app.py --server.port 8501 --server.address 0.0.0.0 --server.headless true
Restart=always
RestartSec=5
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
EOF
```

#### 🔍 Anatomia delle Direttive del File `.service`:
1. **Sezione `[Unit]`:**
   * `Description=`: Descrizione human-readable del servizio visibile nei comandi di stato e nei log.
   * `After=network.target`: Ordina a Systemd di attendere che le interfacce di rete siano attive prima di avviare l'app.
2. **Sezione `[Service]`:**
   * `Type=simple`: Il processo principale avviato da `ExecStart` è il demone del servizio.
   * `User=arny`: Esegue il processo con i privilegi dell'utente specificato, impedendo l'accesso come `root`.
   * `WorkingDirectory=`: Imposta la cartella di lavoro corrente per risolvere correttamente i percorsi relativi verso `dataset/` e `soluzioni/`.
   * `ExecStart=`: Comando esatto per avviare Streamlit.
     - `${APP_DIR}/.venv/bin/streamlit`: Percorso assoluto dell'eseguibile Streamlit isolato nel virtualenv.
     - `${APP_DIR}/dashboard/app.py`: Percorso assoluto del sorgente Python.
     - `--server.port 8501`: Porta TCP di ascolto.
     - `--server.address 0.0.0.0`: Mette il server in ascolto su tutte le schede di rete (LAN/WAN) e non solo su localhost.
     - `--server.headless true`: Disabilita l'apertura automatica del browser grafico (essenziale su server headless).
   * `Restart=always`: In caso di crash o terminazione anomala, Systemd riavvia automaticamente il servizio.
   * `RestartSec=5`: Attesa di 5 secondi prima di tentare il riavvio (evita loop di crash incontrollati).
   * `Environment=PYTHONUNBUFFERED=1`: Forza Python a inviare immediatamente gli output stdout/stderr al log di sistema senza buffering.
3. **Sezione `[Install]`:**
   * `WantedBy=multi-user.target`: Collega il servizio al target di avvio standard multi-utente (equivalente al runlevel 3/5).

---

### 4. Gestione dei Privilegi di Root e Installazione nel Sistema
```bash
echo "=== 2. Copia in /etc/systemd/system (richiede sudo se eseguito) ==="
if [ "$EUID" -ne 0 ]; then
    echo "Nota: Per installare effettivamente nel sistema operativo, eseguire:"
    echo "  sudo cp /tmp/${SERVICE_NAME} ${SERVICE_DST}"
    echo "  sudo systemctl daemon-reload"
    echo "  sudo systemctl enable --now ${SERVICE_NAME}"
    echo "File service generato in: /tmp/${SERVICE_NAME}"
else
    cp /tmp/${SERVICE_NAME} ${SERVICE_DST}
    systemctl daemon-reload
    systemctl enable --now ${SERVICE_NAME}
    echo "✅ Servizio ${SERVICE_NAME} abilitato e avviato con successo!"
fi
```
* **Spiegazione:** Verifica se lo script viene eseguito da utente normale (`$EUID != 0`) o con privilegi di root (`sudo`). Se eseguito come utente standard, genera il file in `/tmp` e stampa i comandi esatti da lanciare con `sudo`.

---

# 🖥️ COMANDI OPERATIVI DI CONTROLLO & STREAMING LOG

### 1. Verificare lo Stato del Servizio
```bash
sudo systemctl status dashboard_vendite.service
```
**Output Atteso (Servizio Attivo e Corretto):**
```text
● dashboard_vendite.service - Dashboard Direzionale Vendite ITIS Campobasso
     Loaded: loaded (/etc/systemd/system/dashboard_vendite.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2026-09-15 10:00:00 CEST; 15min ago
   Main PID: 14250 (streamlit)
      Tasks: 6 (limit: 9450)
     Memory: 115.4M
        CPU: 1.250s
     CGroup: /system.slice/dashboard_vendite.service
             └─14250 /home/arny/.../.venv/bin/python3 .../bin/streamlit run ...
```

### 2. Streaming dei Log in Tempo Reale (Debug Live)
```bash
sudo journalctl -u dashboard_vendite.service -f
```
**Output Atteso:**
```text
Sep 15 10:00:01 server-itis streamlit[14250]: You can now view your Streamlit app in your browser.
Sep 15 10:00:01 server-itis streamlit[14250]: Network URL: http://192.168.1.100:8501
Sep 15 10:00:01 server-itis streamlit[14250]: External URL: http://0.0.0.0:8501
```

### 3. Arresto, Riavvio e Disabilitazione
```bash
sudo systemctl stop dashboard_vendite.service      # Arresta il demone
sudo systemctl restart dashboard_vendite.service   # Riavvia l'applicazione
sudo systemctl disable dashboard_vendite.service  # Rimuove l'avvio automatico al boot
```

---

# ⚠️ ERRORI COMUNI IN AULA & TROUBLESHOOTING

| Errore Riscontrato | Causa Radice | Soluzione Immediata |
| :--- | :--- | :--- |
| `Unit dashboard_vendite.service not found` | Il file non è stato copiato in `/etc/systemd/system/` o manca il reload | `sudo cp /tmp/dashboard_vendite.service /etc/systemd/system/` seguito da `sudo systemctl daemon-reload` |
| `status=203/EXEC` | Percorso dell'eseguibile errato o file mancante in `ExecStart` | Verificare che il percorso di `.venv/bin/streamlit` sia assoluto ed esista sul disco |
| `status=217/USER` | L'utente specificato in `User=` non esiste nel sistema | Cambiare `User=` con il nome del proprio utente Linux (`whoami`) |
| `Address already in use` | Porta 8501 occupata da un'altra istanza | Terminare il processo con `sudo fuser -k 8501/tcp` o cambiare la porta |
| Connessione rifiutata dall'esterno | Firewall `ufw` attivo o `--server.address` impostato su `127.0.0.1` | Eseguire `sudo ufw allow 8501/tcp` e usare `--server.address 0.0.0.0` |

---
