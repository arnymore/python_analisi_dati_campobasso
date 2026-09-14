#!/usr/bin/env bash
# =============================================================================
# SCRIPT DI INSTALLAZIONE AUTOMATICA SERVIZIO SYSTEMD SU LINUX
# Docente: Arnaldo Morena
# Corso: Laboratorio Python + Analisi Dati (ITIS Campobasso)
# =============================================================================

set -e

APP_DIR="/home/arny/Projects/clients/itis_demos_campobasso/corso_python"
SERVICE_NAME="dashboard_vendite.service"
SERVICE_DST="/etc/systemd/system/${SERVICE_NAME}"
USER_RUN="arny"

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

echo "=== Setup completato! ==="
