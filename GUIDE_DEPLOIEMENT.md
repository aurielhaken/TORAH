# Guide de Déploiement - Torah AI 🚀

## Options de Déploiement

Vous avez plusieurs choix selon votre budget et vos besoins:

---

## 🆓 OPTION 1: GRATUIT - Sans nom de domaine (RECOMMANDÉ POUR DÉBUTER)

### A) Render.com (Le plus simple - GRATUIT)

**Avantages:**
- ✅ 100% Gratuit
- ✅ URL fournie automatiquement: `https://torah-ai.onrender.com`
- ✅ Déploiement en 5 minutes
- ✅ HTTPS inclus
- ✅ Parfait pour tester

**Comment faire:**

1. **Créer un compte sur Render.com**
   ```
   https://render.com (gratuit)
   ```

2. **Connecter votre GitHub**
   - Cliquez sur "New +"
   - Sélectionnez "Web Service"
   - Connectez votre repo GitHub

3. **Configuration:**
   ```yaml
   Name: torah-ai
   Environment: Python 3
   Build Command: pip install -r requirements-minimal.txt
   Start Command: uvicorn api.main:app --host 0.0.0.0 --port $PORT
   ```

4. **Variables d'environnement:**
   ```
   DATABASE_URL=sqlite:///./torah_ai.db
   PYTHON_VERSION=3.11.0
   ```

5. **Déployer!**
   - Cliquez sur "Create Web Service"
   - Attendez 2-3 minutes
   - Votre API sera sur: `https://torah-ai.onrender.com`

**Limites gratuites:**
- Se met en veille après 15 min d'inactivité (redémarre en 30 sec)
- 512 MB RAM
- Parfait pour tester et partager!

---

### B) Railway.app (Alternative gratuite)

**Avantages:**
- ✅ Gratuit ($5 de crédit/mois)
- ✅ URL fournie: `https://torah-ai.up.railway.app`
- ✅ Plus rapide que Render
- ✅ PostgreSQL gratuit inclus!

**Comment faire:**

1. **S'inscrire sur Railway.app**
   ```
   https://railway.app
   ```

2. **Nouveau projet depuis GitHub**
   - "New Project" > "Deploy from GitHub repo"
   - Sélectionnez votre repo TORAH

3. **Railway détecte automatiquement Python!**

4. **Variables d'environnement:**
   ```
   DATABASE_URL=postgresql://... (Railway fournit automatiquement)
   ```

5. **Déploiement automatique** à chaque push Git!

**Limites:**
- $5 de crédit gratuit/mois
- Après épuisement: $0.000231/GB-hour (~$5/mois pour usage normal)

---

### C) Fly.io (Pour les développeurs)

**Avantages:**
- ✅ Gratuit pour petits projets
- ✅ URL: `https://torah-ai.fly.dev`
- ✅ Très rapide
- ✅ Plusieurs régions (Europe, USA, etc.)

**Installation:**
```bash
# Installer Fly CLI
curl -L https://fly.io/install.sh | sh

# Se connecter
flyctl auth login

# Déployer
flyctl launch
```

**Limites:**
- 3 VM gratuites
- 160 GB de transfert/mois

---

## 💰 OPTION 2: AVEC NOM DE DOMAINE (Professionnel)

### Pourquoi acheter un nom de domaine?

**Avantages:**
- ✅ Image professionnelle: `https://torah-ai.com`
- ✅ Mémorisable et partageable
- ✅ Crédibilité accrue
- ✅ Email personnalisé: `contact@torah-ai.com`

**Prix:**
- ~10-15€/an pour un `.com`
- ~5-8€/an pour un `.org` ou `.net`

### Où acheter?

1. **Namecheap** (recommandé)
   - Prix: ~$8.88/an pour .com
   - https://www.namecheap.com

2. **Cloudflare** (le moins cher)
   - Prix: $8.57/an pour .com (prix coûtant!)
   - https://www.cloudflare.com/products/registrar/

3. **OVH** (français)
   - Prix: ~10€/an
   - https://www.ovh.com

### Configuration avec nom de domaine:

**Option A: Render.com + Domaine personnalisé**

1. Acheter domaine sur Namecheap
2. Dans Render > Settings > Custom Domain
3. Ajouter: `torah-ai.com` et `www.torah-ai.com`
4. Configurer les DNS chez Namecheap:
   ```
   Type: CNAME
   Name: www
   Value: torah-ai.onrender.com

   Type: A
   Name: @
   Value: 216.24.57.1 (IP de Render)
   ```
5. Attendre 10-60 minutes (propagation DNS)
6. HTTPS automatique via Let's Encrypt ✅

**Coût total:** ~10€/an + gratuit pour l'hébergement

---

## 🚀 OPTION 3: PRODUCTION (Pour usage intensif)

### Hébergement Cloud professionnel

#### A) DigitalOcean (Recommandé)

**Prix:** $6/mois (droplet basique)

**Setup:**
```bash
# 1. Créer droplet Ubuntu sur DigitalOcean
# 2. SSH vers le serveur
ssh root@votre-ip

# 3. Installer
git clone <votre-repo>
cd TORAH
./scripts/deploy.sh  # Script à créer
```

**Avantages:**
- Contrôle total
- PostgreSQL + pgvector
- Scalabilité
- Backups automatiques

#### B) Heroku

**Prix:** $7/mois (Eco Dyno)

```bash
# Installer Heroku CLI
npm install -g heroku

# Déployer
heroku create torah-ai
heroku addons:create heroku-postgresql:mini
git push heroku main
```

#### C) AWS / Google Cloud / Azure

**Prix:** Variable ($10-50/mois)
- Le plus scalable
- Le plus complexe
- Pour usage mondial intensif

---

## 📱 OPTION 4: Application Mobile (Futur)

### PWA (Progressive Web App) - GRATUIT

Transformez votre API en app installable:

1. **Créer un frontend simple** (HTML/CSS/JS)
2. **Ajouter un manifest.json**
3. **Service Worker pour offline**
4. **Les utilisateurs peuvent "Installer" sur mobile!**

Pas besoin d'App Store! Fonctionne sur iOS et Android.

### Application Native (Plus tard)

- **React Native** ou **Flutter**
- Publication App Store: $99/an
- Publication Google Play: $25 (une fois)

---

## 🎯 MA RECOMMANDATION POUR VOUS

### Phase 1: Démarrage (MAINTENANT) - GRATUIT ✅

**Utilisez Render.com:**
- ✅ Gratuit
- ✅ URL: `https://torah-ai.onrender.com`
- ✅ Déploiement en 5 minutes
- ✅ Partageable immédiatement
- ✅ Pas de carte bancaire nécessaire

**NE PAS acheter de domaine maintenant.**

Raisons:
1. Testez d'abord si les gens utilisent
2. Économisez 10-15€
3. Vous pourrez ajouter un domaine plus tard

### Phase 2: Croissance (Dans 1-3 mois)

**Si vous avez des utilisateurs réguliers:**
- Acheter domaine: `torah-ai.com` (~10€/an)
- Rester sur Render gratuit ou passer à Railway
- Ajouter Google Analytics

### Phase 3: Production (Dans 6 mois)

**Si usage intensif (100+ utilisateurs/jour):**
- Migrer vers DigitalOcean ($6/mois)
- PostgreSQL + pgvector
- Domaine + email professionnel
- CDN (Cloudflare gratuit)

---

## 🚀 DÉPLOIEMENT IMMÉDIAT - RENDER.COM

### Guide pas à pas (5 minutes):

1. **Créer compte Render:**
   - Aller sur https://render.com
   - Sign up with GitHub

2. **Nouveau service:**
   - Dashboard > "New +" > "Web Service"
   - Connect repository: sélectionnez `TORAH`

3. **Configuration:**
   ```
   Name: torah-ai
   Region: Frankfurt (Europe) ou Oregon (USA)
   Branch: claude/session-011CUYdMn11QoLqwzVzouCem
   Root Directory: (laisser vide)
   Environment: Python 3
   Build Command: pip install -r requirements-minimal.txt
   Start Command: uvicorn api.main:app --host 0.0.0.0 --port $PORT
   Instance Type: Free
   ```

4. **Variables d'environnement (facultatif):**
   ```
   DATABASE_URL=sqlite:///./torah_ai.db
   API_HOST=0.0.0.0
   API_PORT=$PORT
   DEBUG=false
   ```

5. **Créer le service!**
   - Cliquez "Create Web Service"
   - Attendez le déploiement (2-3 min)
   - URL générée: `https://torah-ai-xxxx.onrender.com`

6. **Tester:**
   ```bash
   curl https://votre-url.onrender.com/health
   ```

7. **Initialiser la base:**
   Render va créer la base automatiquement au premier démarrage!

---

## 📊 Comparaison des Options

| Option | Prix | Temps setup | Domaine | Limite | Recommandé pour |
|--------|------|-------------|---------|--------|----------------|
| **Render.com** | 🆓 Gratuit | 5 min | Non | Sommeil après 15min | ✅ Démarrage |
| **Railway** | 🆓 $5/mois | 5 min | Non | 500h/mois | Test |
| **Fly.io** | 🆓 Gratuit | 10 min | Non | 160GB transfert | Développeurs |
| **Render + Domaine** | €10/an | 20 min | Oui | Sommeil après 15min | Petit projet |
| **DigitalOcean** | $6/mois | 1h | Oui | Aucune | Production |
| **Heroku** | $7/mois | 15 min | Oui | Aucune | Entreprise |

---

## 🛠️ Fichiers nécessaires pour déploiement

### Créer `Procfile` (pour Heroku):
```
web: uvicorn api.main:app --host 0.0.0.0 --port $PORT
```

### Créer `render.yaml` (pour Render - optionnel):
```yaml
services:
  - type: web
    name: torah-ai
    env: python
    buildCommand: pip install -r requirements-minimal.txt
    startCommand: uvicorn api.main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: DATABASE_URL
        value: sqlite:///./torah_ai.db
      - key: PYTHON_VERSION
        value: 3.11.0
```

### Créer `runtime.txt` (optionnel):
```
python-3.11.14
```

---

## 🔒 Sécurité avant déploiement

**Checklist:**

- [ ] Changer SECRET_KEY dans .env
- [ ] Ne PAS committer .env dans Git
- [ ] Utiliser des variables d'environnement sur Render
- [ ] Activer HTTPS (automatique sur Render)
- [ ] Rate limiting activé (déjà dans le code)
- [ ] Pas de clés API dans le code

---

## 📈 Après le déploiement

### Partager votre Rav Virtuel:

1. **Sur les réseaux sociaux**
   ```
   🌟 Découvrez Torah AI - Un Rav virtuel accessible 24/7!
   Questions sur la Torah, Mishna, Talmud, Kabbalah...

   🔗 https://torah-ai.onrender.com

   #Torah #Judaisme #IA #Education
   ```

2. **Dans les communautés**
   - Forums juifs
   - Groupes Facebook
   - Reddit r/Judaism
   - Discord de Torah

3. **Ajouter Google Analytics**
   Pour suivre l'usage et améliorer

---

## ❓ FAQ Déploiement

**Q: L'app se met en veille sur Render?**
R: Oui après 15 min. Solution: Pinger l'URL toutes les 10 min avec UptimeRobot (gratuit)

**Q: Puis-je utiliser PostgreSQL gratuitement?**
R: Oui sur Railway.app inclus, ou Supabase (gratuit)

**Q: Combien ça coûte vraiment?**
R:
- Démarrage: 0€
- Avec domaine: ~10€/an
- Production: ~6€/mois

**Q: Puis-je monétiser plus tard?**
R: Oui! Donations, Patreon, ou version Premium

---

## 🎯 Action Immédiate Recommandée

**MAINTENANT:**

1. ✅ Déployez sur Render.com (gratuit, 5 min)
2. ✅ Testez avec votre communauté
3. ✅ Récoltez des retours

**DANS 1 MOIS (si succès):**

1. Acheter domaine `torah-ai.com`
2. Ajouter analytics
3. Enrichir le contenu

**DANS 3 MOIS (si croissance):**

1. Migrer vers serveur dédié
2. PostgreSQL + embeddings
3. App mobile PWA

---

## 🔗 Ressources

- **Render.com:** https://render.com
- **Railway.app:** https://railway.app
- **Namecheap:** https://www.namecheap.com
- **Tutoriels FastAPI:** https://fastapi.tiangolo.com/deployment/

---

**Mon conseil:** Commencez avec Render gratuit SANS domaine. Si dans 2-3 mois vous avez des utilisateurs réguliers, investissez dans un domaine. Pas besoin de se précipiter!

**L'important c'est que les gens puissent l'utiliser, pas l'URL! 🎯**

✨ **B'hatzla'cha pour le lancement!** ✨
