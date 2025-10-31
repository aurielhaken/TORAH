# 🚀 Guide IONOS Deploy Now - Torah AI

Déployez Torah AI en quelques clics avec IONOS Deploy Now !

## 🎯 Qu'est-ce que Deploy Now ?

IONOS Deploy Now est un service PaaS (Platform as a Service) qui :
- ✅ Déploie automatiquement depuis GitHub
- ✅ Détecte Python, installe les dépendances
- ✅ Fournit un domaine HTTPS gratuit
- ✅ Met à jour automatiquement à chaque push
- ✅ Gratuit pour commencer !

## 📋 Prérequis

- ✅ Un compte GitHub (vous l'avez déjà !)
- ✅ Un compte IONOS (gratuit)
- ✅ Le repository TORAH (déjà prêt !)

## 🚀 Déploiement pas-à-pas

### Étape 1 : Créer un compte IONOS Deploy Now

1. Allez sur **https://www.ionos.com/hosting/deploy-now**
2. Cliquez sur **"Start for free"** ou **"Commencer gratuitement"**
3. Créez un compte IONOS (ou connectez-vous si vous en avez un)

### Étape 2 : Connecter GitHub

1. Une fois connecté à Deploy Now, cliquez sur **"New Project"**
2. Cliquez sur **"Connect with GitHub"**
3. Autorisez IONOS Deploy Now à accéder à votre GitHub
4. Sélectionnez le repository **aurielhaken/TORAH**

### Étape 3 : Configuration du projet

Deploy Now va automatiquement détecter :
- ✅ **Python 3.11** (depuis `runtime.txt`)
- ✅ **FastAPI/Uvicorn** (depuis `Procfile`)
- ✅ **Dépendances** (depuis `requirements-minimal.txt`)

**Configuration recommandée :**

1. **Project name** : `torah-ai`
2. **Branch** : `claude/debug-localhost-port-011CUYfs2nnYZx3TmbCb9nnu` (ou `main` si mergé)
3. **Build command** : (laisser vide, Deploy Now s'en charge)
4. **Start command** : Sera pris depuis le `Procfile`

### Étape 4 : Variables d'environnement (optionnel)

Si vous avez besoin de configurer des variables :

1. Dans Deploy Now, allez dans **Settings** > **Environment Variables**
2. Ajoutez les variables nécessaires :
   ```
   DEBUG=False
   DATABASE_URL=postgresql://...  (si vous utilisez une DB)
   ```

### Étape 5 : Déployer !

1. Cliquez sur **"Deploy"** ou **"Déployer"**
2. Deploy Now va :
   - ⏳ Cloner le repository
   - 📦 Installer Python 3.11
   - 📥 Installer les dépendances depuis `requirements-minimal.txt`
   - 🚀 Lancer l'application avec la commande du `Procfile`
   - 🌐 Vous fournir une URL HTTPS

**⏱️ Temps estimé : 3-5 minutes**

### Étape 6 : Accéder à votre application

Une fois le déploiement terminé, Deploy Now vous donne une URL comme :

```
https://torah-ai-xyz123.ionos.space
```

Vous pouvez maintenant accéder à :
- 🏠 Page d'accueil : `https://votre-url.ionos.space/`
- 📚 Documentation : `https://votre-url.ionos.space/docs`
- 💚 Health check : `https://votre-url.ionos.space/health`

## 📱 Tester depuis votre téléphone

1. Ouvrez le navigateur de votre téléphone
2. Allez sur `https://votre-url.ionos.space/docs`
3. Testez l'API directement depuis l'interface Swagger !

**Exemple de test :**
1. Cliquez sur **POST /api/v1/question**
2. Cliquez sur **"Try it out"**
3. Entrez une question : `"Quelle est la signification du Shabbat?"`
4. Cliquez sur **"Execute"**
5. Vous verrez la réponse du Rav virtuel !

## 🔄 Mises à jour automatiques

**Avantage énorme de Deploy Now :**

Chaque fois que vous pushez du code sur GitHub, Deploy Now redéploie automatiquement !

```bash
# Sur votre machine locale
git add .
git commit -m "Nouvelle fonctionnalité"
git push

# Deploy Now détecte le push et redéploie automatiquement ! 🎉
```

## 🌐 Domaine personnalisé (optionnel)

Si vous voulez utiliser votre propre domaine (ex: torah-ai.com) :

1. Dans Deploy Now, allez dans **Settings** > **Domains**
2. Cliquez sur **"Add custom domain"**
3. Entrez votre domaine
4. Suivez les instructions pour configurer les DNS dans IONOS

Deploy Now configure automatiquement HTTPS pour votre domaine !

## 📊 Monitoring et Logs

### Voir les logs

1. Dans Deploy Now, allez dans **Deployments**
2. Cliquez sur le déploiement actif
3. Vous verrez les logs en temps réel

### Vérifier le statut

```bash
# Depuis n'importe où
curl https://votre-url.ionos.space/health
```

## ❓ Résolution de problèmes

### Le déploiement échoue

**Problème** : Erreur lors de l'installation des dépendances
**Solution** : Vérifiez que `requirements-minimal.txt` est correct

**Problème** : L'application ne démarre pas
**Solution** : Vérifiez les logs dans Deploy Now pour voir l'erreur

### L'application ne répond pas

**Problème** : 502 Bad Gateway
**Solution** : L'application met peut-être du temps à démarrer (30-60 secondes)

**Problème** : 404 Not Found
**Solution** : Vérifiez que l'URL est correcte (avec `/docs` ou `/health`)

## 💡 Astuces

### 1. Tester localement avant de déployer

```bash
# Dans votre terminal
./deploy_ionos.sh

# Ou manuellement
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

### 2. Activer le mode debug temporairement

Dans Deploy Now, ajoutez la variable :
```
DEBUG=True
```

### 3. Surveiller les performances

Deploy Now fournit des métriques de performance dans le dashboard.

## 📈 Mise à l'échelle

Si votre application devient populaire :

1. Dans Deploy Now, allez dans **Settings** > **Resources**
2. Augmentez le nombre de workers ou la RAM
3. Deploy Now s'adapte automatiquement !

## 🎉 C'est tout !

Votre Torah AI est maintenant :
- ✅ En ligne 24/7
- ✅ Accessible depuis partout
- ✅ HTTPS sécurisé
- ✅ Déploiement automatique
- ✅ Gratuit (pour commencer)

**Prêt à déployer ? Allez sur https://www.ionos.com/hosting/deploy-now !**

---

## 📞 Support

- **Documentation Deploy Now** : https://docs.ionos.space/
- **Support IONOS** : https://www.ionos.com/help
- **Repository GitHub** : https://github.com/aurielhaken/TORAH

**Bonne chance avec votre déploiement ! 🕎**
