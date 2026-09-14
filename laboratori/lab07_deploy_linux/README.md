# Laboratorio 7: Deploy su Server Linux & Produzione (1 Ora)

## 🎯 Obiettivi
* Configurare un ambiente virtuale Python dedicato su server Linux (Ubuntu/Debian).
* Creare un file unit di Systemd (`.service`) per gestire l'applicazione Streamlit come servizio continuo (demone).
* Configurare politiche di riavvio automatico (`Restart=always`) e avvio al boot del server (`enable`).
* Gestire il servizio tramite i comandi `systemctl` (`start`, `stop`, `status`, `restart`).
* Ispezionare e monitorare i log applicativi in tempo reale con `journalctl`.
* Comprendere l'architettura di reverse proxy con Nginx e la sicurezza perimetrale.

## 📄 File di Lavoro
* `guida_deploy.md`: Guida operativa dettagliata passo-passo.
* `setup_service.sh`: Script di provisioning per la creazione automatizzata del demone di sistema.

## 🚀 Esecuzione Guida
Consulta [`guida_deploy.md`](guida_deploy.md) per i comandi di configurazione e amministrazione del server.
