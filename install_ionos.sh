#!/bin/bash
# Script d'installation automatique pour IONOS
# Torah AI - Rav Virtuel

set -e  # Arrêter en cas d'erreur

echo "🕎 Torah AI - Installation sur IONOS"
echo "====================================="
echo ""

# Variables
PROJECT_DIR="/home/$USER/TORAH"
SERVICE_NAME="torah-ai"
DOMAIN=""

# Demander le domaine
read -p "📝 Entrez votre nom de domaine (ex: torah-ai.com) : " DOMAIN

echo ""
echo "📦 Étape 1/6 : Mise à jour du système..."
sudo apt update && sudo apt upgrade -y

echo ""
echo "📦 Étape 2/6 : Installation des dépendances..."
sudo apt install -y python3 python3-pip python3-venv git nginx certbot python3-certbot-nginx

echo ""
echo "📥 Étape 3/6 : Clonage du projet (si pas déjà fait)..."
if [ ! -d "$PROJECT_DIR" ]; then
    git clone https://github.com/aurielhaken/TORAH.git "$PROJECT_DIR"
    cd "$PROJECT_DIR"
else
    cd "$PROJECT_DIR"
    git pull origin main
fi

echo ""
echo "🐍 Étape 4/6 : Configuration de l'environnement Python..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements-minimal.txt

echo ""
echo "⚙️  Étape 5/6 : Configuration du service systemd..."
sudo tee /etc/systemd/system/$SERVICE_NAME.service > /dev/null <<EOF
[Unit]
Description=Torah AI - Rav Virtuel API
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$PROJECT_DIR
Environment="PATH=$PROJECT_DIR/venv/bin"
ExecStart=$PROJECT_DIR/venv/bin/uvicorn api.main:app --host 0.0.0.0 --port 8000 --workers 2
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable $SERVICE_NAME
sudo systemctl start $SERVICE_NAME

echo ""
echo "🌐 Étape 6/6 : Configuration de Nginx..."
sudo tee /etc/nginx/sites-available/$SERVICE_NAME > /dev/null <<EOF
server {
    listen 80;
    server_name $DOMAIN www.$DOMAIN;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

sudo ln -sf /etc/nginx/sites-available/$SERVICE_NAME /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

echo ""
echo "🔒 Configuration SSL..."
read -p "Voulez-vous configurer SSL/HTTPS maintenant ? (y/n) : " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    sudo certbot --nginx -d $DOMAIN -d www.$DOMAIN
fi

echo ""
echo "🔥 Configuration du firewall..."
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw --force enable

echo ""
echo "✅ Installation terminée !"
echo ""
echo "📊 Vérification du statut..."
sudo systemctl status $SERVICE_NAME --no-pager

echo ""
echo "🎉 Torah AI est maintenant en ligne !"
echo ""
echo "🌍 Accédez à votre application :"
echo "   - API : http://$DOMAIN"
echo "   - Documentation : http://$DOMAIN/docs"
echo "   - Health check : http://$DOMAIN/health"
echo ""
echo "📱 Accessible depuis mobile, tablette, ordinateur !"
echo ""
echo "📝 Commandes utiles :"
echo "   - Voir les logs : sudo journalctl -u $SERVICE_NAME -f"
echo "   - Redémarrer : sudo systemctl restart $SERVICE_NAME"
echo "   - Arrêter : sudo systemctl stop $SERVICE_NAME"
echo ""
echo "⚠️  N'oubliez pas de configurer votre domaine dans IONOS :"
echo "   1. Connectez-vous à votre compte IONOS"
echo "   2. Allez dans Domaines"
echo "   3. Créez un enregistrement A pointant vers $(curl -s ifconfig.me)"
echo ""
