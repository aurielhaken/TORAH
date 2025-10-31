# 🚀 Déploiement Torah AI sur IONOS

Guide complet pour déployer l'application Torah AI - Rav Virtuel sur IONOS.

## 📋 Prérequis

- Un compte IONOS actif
- Accès SSH à votre serveur (VPS ou Cloud Server)
- Python 3.11 installé sur le serveur

## 🎯 Option 1 : IONOS VPS ou Cloud Server (RECOMMANDÉ)

### Étape 1 : Connexion SSH

```bash
ssh votre_utilisateur@votre-serveur.ionos.com
```

### Étape 2 : Installation des dépendances système

```bash
# Mettre à jour le système
sudo apt update && sudo apt upgrade -y

# Installer Python et pip
sudo apt install -y python3 python3-pip python3-venv git

# Installer nginx (optionnel, pour reverse proxy)
sudo apt install -y nginx
```

### Étape 3 : Cloner le projet

```bash
cd /home/votre_utilisateur
git clone https://github.com/aurielhaken/TORAH.git
cd TORAH
```

### Étape 4 : Configuration de l'environnement

```bash
# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements-minimal.txt
```

### Étape 5 : Lancer l'application

#### Option A : Démarrage simple (pour tester)

```bash
./deploy_ionos.sh
```

#### Option B : Avec systemd (recommandé pour production)

Créez un service systemd :

```bash
sudo nano /etc/systemd/system/torah-ai.service
```

Contenu du fichier :

```ini
[Unit]
Description=Torah AI - Rav Virtuel API
After=network.target

[Service]
Type=simple
User=votre_utilisateur
WorkingDirectory=/home/votre_utilisateur/TORAH
Environment="PATH=/home/votre_utilisateur/TORAH/venv/bin"
ExecStart=/home/votre_utilisateur/TORAH/venv/bin/uvicorn api.main:app --host 0.0.0.0 --port 8000 --workers 2
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Activez et démarrez le service :

```bash
sudo systemctl daemon-reload
sudo systemctl enable torah-ai
sudo systemctl start torah-ai
sudo systemctl status torah-ai
```

### Étape 6 : Configuration Nginx (Reverse Proxy)

Créez une configuration nginx :

```bash
sudo nano /etc/nginx/sites-available/torah-ai
```

Contenu :

```nginx
server {
    listen 80;
    server_name votre-domaine.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Activez la configuration :

```bash
sudo ln -s /etc/nginx/sites-available/torah-ai /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Étape 7 : Configuration du domaine sur IONOS

1. Connectez-vous à votre compte IONOS
2. Allez dans "Domaines"
3. Sélectionnez votre domaine
4. Configurez un enregistrement A pointant vers l'IP de votre serveur :
   - Type : A
   - Nom : @ (ou api si vous voulez api.votre-domaine.com)
   - Valeur : IP_DE_VOTRE_SERVEUR
   - TTL : 3600

### Étape 8 : SSL avec Let's Encrypt (HTTPS)

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d votre-domaine.com
```

## 🎯 Option 2 : IONOS Deploy Now (Plus simple)

IONOS Deploy Now est un service PaaS qui déploie automatiquement depuis GitHub.

### Étape 1 : Préparer le repository

Les fichiers `Procfile` et `runtime.txt` sont déjà créés.

### Étape 2 : Connecter à Deploy Now

1. Allez sur https://www.ionos.com/hosting/deploy-now
2. Connectez votre compte GitHub
3. Sélectionnez le repository `TORAH`
4. Suivez les instructions de déploiement

Deploy Now détectera automatiquement :
- `requirements-minimal.txt` pour les dépendances
- `Procfile` pour la commande de démarrage
- `runtime.txt` pour la version Python

## 🎯 Option 3 : IONOS Hébergement Web (Limité)

⚠️ **Attention** : L'hébergement web classique IONOS ne supporte que PHP par défaut. Pour une application Python/FastAPI, utilisez plutôt un VPS ou Deploy Now.

## 🔧 Configuration de production

### Variables d'environnement

Créez un fichier `.env` sur le serveur :

```bash
nano /home/votre_utilisateur/TORAH/.env
```

Contenu :

```env
# Application
DEBUG=False
HOST=0.0.0.0
PORT=8000

# Base de données (si vous utilisez PostgreSQL)
DATABASE_URL=postgresql://user:password@localhost:5432/torah_ai

# API Keys (optionnel)
OPENAI_API_KEY=votre_clé_ici
ANTHROPIC_API_KEY=votre_clé_ici
```

### Firewall

Ouvrez le port 8000 (si pas derrière nginx) :

```bash
sudo ufw allow 8000/tcp
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

## 📊 Vérification du déploiement

Une fois déployé, testez :

```bash
# Health check
curl http://votre-domaine.com/health

# API
curl http://votre-domaine.com/

# Documentation
# Ouvrez dans un navigateur : http://votre-domaine.com/docs
```

## 📱 Accès depuis mobile

Une fois déployé, vous pourrez accéder à :

- **API** : `https://votre-domaine.com`
- **Documentation** : `https://votre-domaine.com/docs`
- **Health check** : `https://votre-domaine.com/health`

## 🔄 Mise à jour du code

### Avec systemd

```bash
cd /home/votre_utilisateur/TORAH
git pull origin main
source venv/bin/activate
pip install -r requirements-minimal.txt
sudo systemctl restart torah-ai
```

### Avec Deploy Now

Le déploiement est automatique à chaque push sur GitHub !

## 📞 Support

Si vous avez besoin d'aide :
1. Vérifiez les logs : `sudo journalctl -u torah-ai -f`
2. Vérifiez nginx : `sudo tail -f /var/log/nginx/error.log`
3. Contactez le support IONOS

## ✅ Checklist de déploiement

- [ ] Serveur IONOS configuré
- [ ] Python 3.11 installé
- [ ] Code déployé depuis GitHub
- [ ] Dépendances installées
- [ ] Service systemd créé et démarré
- [ ] Nginx configuré
- [ ] Domaine configuré dans IONOS
- [ ] SSL/HTTPS activé avec Let's Encrypt
- [ ] API testée et fonctionnelle
- [ ] Accessible depuis mobile

## 🎉 C'est tout !

Votre application Torah AI est maintenant accessible depuis n'importe où dans le monde ! 🌍
