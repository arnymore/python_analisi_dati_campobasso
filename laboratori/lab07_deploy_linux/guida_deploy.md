# Guida Operativa Deploy Linux - Modulo 7
**Docente: Arnaldo Morena** | ITIS Campobasso

---

## Obiettivi del Modulo (1 Ora)
1. Comprendere la differenza tra esecuzione interattiva e servizio di produzione Linux (Background Daemon).
2. Configurare un Virtual Environment Python isolato su server Linux (Ubuntu/Debian).
3. Creare e configurare una `systemd unit file` (`/etc/systemd/system/dashboard_vendite.service`).
4. Gestire il ciclo di vita dell'applicazione con `systemctl` (`start`, `stop`, `restart`, `status`, `enable`).
5. Ispezionare i log di produzione in tempo reale con `journalctl`.
6. Configurare reverse proxy Nginx e firewall (UFW) di base.

---

## 1. Architettura di Deploy

```text
[ Browser Utente ] 
       │ (Porta 80/443 HTTP/S)
       ▼
 [ Nginx Reverse Proxy ]
       │ (Proxy pass localhost:8501)
       ▼
[ Systemd Service: dashboard_vendite ]
       │ (Gestione processo demone)
       ▼
[ Streamlit App Python (.venv) ]
```

---

## 2. File di Configurazione Systemd: `dashboard_vendite.service`

Posizione su server: `/etc/systemd/system/dashboard_vendite.service`

```ini
[Unit]
Description=Dashboard Direzionale Vendite ITIS Campobasso
After=network.target

[Service]
Type=simple
User=arny
WorkingDirectory=/home/arny/Projects/clients/itis_demos_campobasso/corso_python
ExecStart=/home/arny/Projects/clients/itis_demos_campobasso/corso_python/.venv/bin/streamlit run dashboard/app.py --server.port 8501 --server.address 0.0.0.0 --server.headless true
Restart=always
RestartSec=5
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

---

## 3. Comandi Essenziali di Gestione Server

```bash
# 1. Ricaricare la configurazione di systemd dopo modifiche al file .service
sudo systemctl daemon-reload

# 2. Abilitare l'avvio automatico al boot del server
sudo systemctl enable dashboard_vendite.service

# 3. Avviare il servizio
sudo systemctl start dashboard_vendite.service

# 4. Verificare lo stato in esecuzione
sudo systemctl status dashboard_vendite.service

# 5. Monitorare i log applicativi in tempo reale (follow)
sudo journalctl -u dashboard_vendite.service -f -n 50

# 6. Riavviare o fermare il servizio
sudo systemctl restart dashboard_vendite.service
sudo systemctl stop dashboard_vendite.service
```

---

## 4. Configurazione Reverse Proxy Nginx (Opzionale Produzione)

File: `/etc/nginx/sites-available/dashboard`

```nginx
server {
    listen 80;
    server_name dashboard.azienda.local;

    location / {
        proxy_pass http://127.0.0.1:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_read_timeout 86400;
    }
}
```
