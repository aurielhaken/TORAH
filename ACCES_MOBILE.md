# 📱 Accéder à Torah AI depuis votre téléphone

Le serveur API fonctionne actuellement sur **http://localhost:8000**

## 🎯 Options pour y accéder depuis votre téléphone

### Option 1 : Port Forwarding de Claude Code (RECOMMANDÉ)

Claude Code pourrait avoir une fonctionnalité de port forwarding intégrée :

1. **Cherchez dans l'interface Claude Code** :
   - Une section "Ports" ou "Forwarded Ports"
   - Un menu "Forward Port"
   - Une icône de réseau ou globe

2. **Si vous trouvez cette option** :
   - Ajoutez le port **8000**
   - Claude Code vous donnera une URL publique
   - Utilisez cette URL sur votre téléphone

### Option 2 : Utiliser votre propre compte ngrok

Si vous avez un compte ngrok :

1. Récupérez votre authtoken depuis https://dashboard.ngrok.com
2. Dans le terminal Claude Code, tapez :
   ```bash
   ngrok authtoken VOTRE_TOKEN
   ngrok http 8000
   ```
3. Ngrok affichera une URL publique (ex: https://abc123.ngrok.io)

### Option 3 : Installer ngrok manuellement

```bash
# Télécharger ngrok
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | \
  sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
  echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | \
  sudo tee /etc/apt/sources.list.d/ngrok.list && \
  sudo apt update && sudo apt install ngrok

# Lancer le tunnel
ngrok http 8000
```

### Option 4 : Tester localement dans Claude Code

Pour l'instant, vous pouvez tester l'API dans Claude Code avec :

```bash
# Test complet
python3 test_interactive.py

# Poser une question
./test_question.sh

# Test simple
curl http://localhost:8000/health
```

## 🌐 Endpoints disponibles

Une fois que vous avez votre URL publique (ex: https://xyz.ngrok.io), vous pouvez accéder à :

- **Page d'accueil**: https://xyz.ngrok.io/
- **Documentation Swagger**: https://xyz.ngrok.io/docs
- **Health check**: https://xyz.ngrok.io/health
- **Poser une question**: POST https://xyz.ngrok.io/api/v1/question

## 📝 Exemple de requête depuis votre téléphone

Depuis le navigateur de votre téléphone, ouvrez :
```
https://VOTRE_URL/docs
```

Vous verrez l'interface Swagger où vous pouvez tester l'API directement !

## ❓ Besoin d'aide ?

Le serveur tourne actuellement et fonctionne parfaitement en local.
Il suffit juste de l'exposer publiquement pour y accéder depuis votre téléphone.
