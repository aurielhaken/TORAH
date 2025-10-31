# 🚀 Déploiement sur guematrai.com

Guide complet pour déployer l'API des codes Torah sur **guematrai.com**

---

## 📋 Prérequis

- ✅ Compte Vercel (gratuit) : https://vercel.com
- ✅ Domaine guematrai.com configuré
- ✅ Accès GitHub au repo

---

## 🎯 Étape 1 : Préparer le Projet

### 1.1 Vérifier que la branche est à jour

```bash
git status
git pull origin claude/cleanup-emergency-code-011CUbmtD3BW34TZaCehseLT
```

### 1.2 Fichiers de déploiement présents

✅ `vercel.json` - Configuration Vercel
✅ `requirements_vercel.txt` - Dépendances minimales
✅ `runtime.txt` - Version Python (3.11)
✅ `api/main.py` - Point d'entrée de l'API

---

## 🌐 Étape 2 : Déployer sur Vercel

### 2.1 Installation de Vercel CLI (optionnel)

```bash
npm install -g vercel
```

### 2.2 Via l'interface web (RECOMMANDÉ)

1. **Se connecter à Vercel**
   - Aller sur https://vercel.com
   - Se connecter avec GitHub

2. **Importer le projet**
   - Cliquer sur "Add New Project"
   - Sélectionner le repo GitHub : `aurielhaken/TORAH`
   - Sélectionner la branche : `claude/cleanup-emergency-code-011CUbmtD3BW34TZaCehseLT`

3. **Configuration du projet**
   ```
   Project Name: guematrai
   Framework Preset: Other
   Root Directory: ./
   Build Command: (laisser vide)
   Output Directory: (laisser vide)
   Install Command: pip install -r requirements_vercel.txt
   ```

4. **Variables d'environnement**
   - Cliquer sur "Environment Variables"
   - Ajouter :
     ```
     PYTHON_VERSION=3.11
     DEBUG=false
     ```

5. **Déployer**
   - Cliquer sur "Deploy"
   - Attendre 2-3 minutes

6. **URL temporaire**
   - Vercel donne une URL : `guematrai.vercel.app`
   - Tester : `https://guematrai.vercel.app/health`

### 2.3 Via CLI (alternative)

```bash
# Se connecter
vercel login

# Déployer
cd /home/user/TORAH
vercel --prod

# Suivre les instructions
```

---

## 🌍 Étape 3 : Connecter guematrai.com

### 3.1 Via l'interface Vercel

1. **Aller dans le projet**
   - https://vercel.com/dashboard
   - Sélectionner "guematrai"

2. **Ajouter le domaine**
   - Onglet "Settings" → "Domains"
   - Cliquer "Add"
   - Entrer : `guematrai.com`
   - Entrer : `www.guematrai.com`

3. **Vercel donne les DNS à configurer**
   ```
   Type: A
   Name: @
   Value: 76.76.21.21

   Type: CNAME
   Name: www
   Value: cname.vercel-dns.com
   ```

### 3.2 Configurer les DNS (chez votre registrar)

**Si guematrai.com est chez :**

#### **Namecheap**
1. Aller sur namecheap.com → Domain List
2. Cliquer "Manage" sur guematrai.com
3. Onglet "Advanced DNS"
4. Ajouter les records :
   ```
   Type: A Record
   Host: @
   Value: 76.76.21.21
   TTL: Automatic

   Type: CNAME Record
   Host: www
   Value: cname.vercel-dns.com
   TTL: Automatic
   ```

#### **GoDaddy**
1. Aller dans DNS Management
2. Ajouter les mêmes records A et CNAME

#### **Cloudflare**
1. Dashboard → DNS → Records
2. Ajouter :
   ```
   Type: A
   Name: @
   IPv4: 76.76.21.21
   Proxy: OFF (nuage gris)

   Type: CNAME
   Name: www
   Target: cname.vercel-dns.com
   Proxy: OFF
   ```

### 3.3 Attendre la propagation DNS

- ⏱️ Propagation : 5 minutes à 48 heures (généralement 1-2h)
- Vérifier : `dig guematrai.com`
- Tester : https://dnschecker.org/#A/guematrai.com

---

## ✅ Étape 4 : Vérifier le Déploiement

### 4.1 Tester l'API

```bash
# Health check
curl https://guematrai.com/health

# Page d'accueil
curl https://guematrai.com/

# Test guématrie
curl -X POST "https://guematrai.com/api/v1/codes/guematrie" \
  -H "Content-Type: application/json" \
  -d '{"texte_hebreu": "אהבה", "methode": "standard"}'
```

### 4.2 Tester dans le navigateur

Ouvrir :
- https://guematrai.com
- https://guematrai.com/docs (Documentation Swagger)
- https://guematrai.com/health

### 4.3 Vérifier tous les endpoints

```bash
# Exemples de codes
curl https://guematrai.com/api/v1/codes/exemples

# At-Bash
curl -X POST "https://guematrai.com/api/v1/codes/atbash" \
  -H "Content-Type: application/json" \
  -d '{"texte": "בבל"}'

# Analyse complète
curl -X POST "https://guematrai.com/api/v1/codes/analyser-tout" \
  -H "Content-Type: application/json" \
  -d '{"texte_hebreu": "שלום"}'
```

---

## 🔧 Configuration Avancée

### SSL/HTTPS

✅ **Automatique avec Vercel !**
- Certificat SSL gratuit de Let's Encrypt
- Renouvellement automatique
- HTTPS forcé par défaut

### Performance

Le `vercel.json` est optimisé avec :
- ✅ Cache-Control headers (1h)
- ✅ CORS configuré
- ✅ Région optimale (iad1 - US East)
- ✅ Lambda size : 15mb max

### Monitoring

Dans le dashboard Vercel :
- **Analytics** : Trafic, latence, erreurs
- **Logs** : Logs en temps réel
- **Deployments** : Historique des déploiements

---

## 🚨 Dépannage

### Erreur : "Module not found"

Vérifier que `requirements_vercel.txt` est utilisé :
```bash
# Dans Vercel, Settings → General → Install Command
pip install -r requirements_vercel.txt
```

### Erreur : "Build failed"

Vérifier les logs dans Vercel :
1. Aller dans "Deployments"
2. Cliquer sur le déploiement échoué
3. Lire les logs

Solutions courantes :
```bash
# Si erreur Python version
runtime.txt doit contenir : python-3.11

# Si erreur imports
Vérifier que tous les modules sont dans requirements_vercel.txt
```

### DNS ne se propage pas

```bash
# Vérifier la configuration
dig guematrai.com
dig www.guematrai.com

# Forcer le refresh DNS local
# Mac/Linux
sudo dscacheutil -flushcache

# Windows
ipconfig /flushdns
```

### API renvoie 404

Vérifier `vercel.json` :
```json
"routes": [
  {
    "src": "/(.*)",
    "dest": "api/main.py"
  }
]
```

---

## 📊 Après le Déploiement

### URLs finales

```
🌐 Site principal : https://guematrai.com
📖 Documentation : https://guematrai.com/docs
🔍 Health check : https://guematrai.com/health

API Endpoints :
📊 Guématrie : POST /api/v1/codes/guematrie
🔍 ELS : POST /api/v1/codes/els
📝 Notarikon : POST /api/v1/codes/notarikon
🔄 At-Bash : POST /api/v1/codes/atbash
🔀 Témourah : POST /api/v1/codes/temourah
✨ Analyse complète : POST /api/v1/codes/analyser-tout
📚 Exemples : GET /api/v1/codes/exemples
```

### Mettre à jour le README

Ajouter dans `README.md` :

```markdown
## 🌐 API en Ligne

L'API est déployée et accessible à tous :

**URL :** https://guematrai.com

**Documentation interactive :** https://guematrai.com/docs

**Exemple d'utilisation :**
\`\`\`bash
curl -X POST "https://guematrai.com/api/v1/codes/guematrie" \\
  -H "Content-Type: application/json" \\
  -d '{"texte_hebreu": "אהבה", "methode": "standard"}'
\`\`\`
```

### Partager

Une fois déployé, vous pouvez partager :
- Documentation : https://guematrai.com/docs
- GitHub : Lien vers le repo
- Exemples : Dans CODES_TORAH.md

---

## 🔄 Mises à Jour

### Déploiement automatique

Vercel redéploie automatiquement à chaque push sur la branche !

```bash
git add .
git commit -m "feat: Nouvelle fonctionnalité"
git push
```

→ Vercel détecte et redéploie automatiquement

### Rollback

Si un déploiement pose problème :
1. Aller dans "Deployments" sur Vercel
2. Trouver le déploiement précédent qui fonctionnait
3. Cliquer sur "..." → "Promote to Production"

---

## 📈 Quotas Vercel (Plan Gratuit)

✅ **Inclus gratuitement :**
- Bande passante : 100 GB/mois
- Durée d'exécution : 100 heures/mois
- Domaine personnalisé : Illimité
- SSL : Automatique
- Déploiements : Illimités

Pour guematrai.com avec les codes Torah, le plan gratuit est **largement suffisant**.

---

## 🎉 Félicitations !

Votre API des codes Torah est maintenant accessible mondialement sur **guematrai.com** !

### Prochaines étapes :

1. ✅ Tester tous les endpoints
2. 📣 Partager le lien
3. 📊 Monitorer l'utilisation
4. 🚀 Ajouter de nouvelles fonctionnalités

---

## 🆘 Support

**Documentation :** `CODES_TORAH.md`
**Issues :** GitHub Issues
**Vercel Docs :** https://vercel.com/docs

**Contact Vercel Support :** https://vercel.com/support

---

🔯 **B'hatzla'ha avec guematrai.com !**
