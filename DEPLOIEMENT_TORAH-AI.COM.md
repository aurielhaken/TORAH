# Déploiement sur torah-ai.com 🚀

## Félicitations pour l'achat du domaine! 🎉

Guide complet pour déployer Torah AI sur **https://torah-ai.com**

---

## PARTIE 1: DÉPLOIEMENT SUR RENDER.COM (10 minutes)

### Étape 1: Créer le compte Render (2 min)

1. **Aller sur Render.com**
   ```
   https://render.com
   ```

2. **Créer un compte**
   - Cliquez sur "Get Started for Free"
   - Choisissez "Sign up with GitHub" (recommandé)
   - Autorisez Render à accéder à vos repositories

3. **Vous arrivez sur le Dashboard** ✅

---

### Étape 2: Créer le Web Service (3 min)

1. **Dans le Dashboard Render:**
   - Cliquez sur le bouton **"New +"** (en haut à droite)
   - Sélectionnez **"Web Service"**

2. **Connecter votre repository:**
   - Si votre repo TORAH n'apparaît pas:
     - Cliquez sur "Configure account"
     - Autorisez l'accès au repository TORAH
   - Sinon, cliquez directement sur **"Connect"** à côté de TORAH

3. **Configuration du service:**

   **Nom et région:**
   ```
   Name: torah-ai
   Region: Frankfurt (pour Europe) OU Oregon (pour monde entier)
   Branch: claude/session-011CUYdMn11QoLqwzVzouCem
   ```

   **Détection automatique:**
   - Render va détecter le fichier `render.yaml` ✨
   - Il va pré-remplir les commandes automatiquement!

   **Si pas de détection automatique, entrer manuellement:**
   ```
   Root Directory: (laisser vide)
   Environment: Python 3
   Build Command: pip install -r requirements-minimal.txt && python database/init_sqlite.py
   Start Command: uvicorn api.main:app --host 0.0.0.0 --port $PORT
   ```

4. **Variables d'environnement (optionnel):**

   Cliquez sur "Advanced" puis ajoutez:

   | Key | Value |
   |-----|-------|
   | `DATABASE_URL` | `sqlite:///./torah_ai.db` |
   | `DEBUG` | `false` |
   | `LOG_LEVEL` | `INFO` |

5. **Plan (Important!):**
   ```
   Instance Type: Free
   ```

6. **Créer le service:**
   - Cliquez sur le gros bouton **"Create Web Service"**
   - Render va maintenant:
     - ✓ Cloner votre code
     - ✓ Installer les dépendances
     - ✓ Initialiser la base de données
     - ✓ Démarrer l'API

   **Durée:** 2-3 minutes

   **Vous verrez les logs en temps réel!**

7. **C'est déployé! ✅**

   Vous obtenez une URL temporaire:
   ```
   https://torah-ai-xxxx.onrender.com
   ```

   **Testez tout de suite:**
   ```bash
   curl https://votre-url.onrender.com/health
   ```

   Vous devriez voir:
   ```json
   {
     "status": "healthy",
     "message": "Le Rav virtuel est prêt à enseigner"
   }
   ```

---

## PARTIE 2: CONFIGURER TORAH-AI.COM (5 minutes)

Maintenant on va pointer votre domaine vers Render!

### Étape 1: Ajouter le domaine dans Render (2 min)

1. **Dans votre service Render:**
   - Cliquez sur l'onglet **"Settings"** (à gauche)
   - Descendez jusqu'à **"Custom Domain"**

2. **Ajouter le domaine:**
   - Cliquez sur **"Add Custom Domain"**
   - Entrez: `torah-ai.com`
   - Cliquez sur "Save"

3. **Ajouter aussi www:**
   - Cliquez encore sur **"Add Custom Domain"**
   - Entrez: `www.torah-ai.com`
   - Cliquez sur "Save"

4. **Render vous donne les instructions DNS:**

   Pour `torah-ai.com`:
   ```
   Type: A
   Name: @
   Value: 216.24.57.1
   ```

   Pour `www.torah-ai.com`:
   ```
   Type: CNAME
   Name: www
   Value: torah-ai-xxxx.onrender.com
   ```

**NOTEZ CES VALEURS! Vous en aurez besoin.**

---

### Étape 2: Configurer les DNS chez votre registrar (3 min)

**Où avez-vous acheté torah-ai.com?**

#### Option A: Namecheap

1. **Connexion:**
   - Aller sur https://namecheap.com
   - Se connecter
   - Account > Dashboard > Domain List
   - Cliquez sur "Manage" à côté de torah-ai.com

2. **Configuration DNS:**
   - Onglet "Advanced DNS"
   - Supprimer les enregistrements par défaut (Parking Page)

3. **Ajouter les enregistrements:**

   **Enregistrement 1 (domaine principal):**
   ```
   Type: A Record
   Host: @
   Value: 216.24.57.1
   TTL: Automatic
   ```

   **Enregistrement 2 (www):**
   ```
   Type: CNAME Record
   Host: www
   Value: torah-ai-xxxx.onrender.com.  (avec le point final!)
   TTL: Automatic
   ```

4. **Sauvegarder** ✅

---

#### Option B: Cloudflare

1. **Connexion:**
   - Aller sur https://cloudflare.com
   - Se connecter
   - Sélectionner torah-ai.com

2. **DNS Settings:**

   **Enregistrement 1:**
   ```
   Type: A
   Name: @
   IPv4: 216.24.57.1
   Proxy: OFF (nuage gris, pas orange!)
   ```

   **Enregistrement 2:**
   ```
   Type: CNAME
   Name: www
   Target: torah-ai-xxxx.onrender.com
   Proxy: OFF (nuage gris!)
   ```

3. **Save** ✅

**IMPORTANT:** Le proxy doit être OFF (gris) pour que HTTPS fonctionne avec Render!

---

#### Option C: OVH

1. **Connexion:**
   - Aller sur https://ovh.com
   - Se connecter
   - Aller dans "Web Cloud" > "Noms de domaine"
   - Cliquer sur torah-ai.com

2. **Zone DNS:**
   - Onglet "Zone DNS"
   - Supprimer les enregistrements A et CNAME existants

3. **Ajouter:**

   **Enregistrement A:**
   ```
   Sous-domaine: (vide)
   Type: A
   Cible: 216.24.57.1
   ```

   **Enregistrement CNAME:**
   ```
   Sous-domaine: www
   Type: CNAME
   Cible: torah-ai-xxxx.onrender.com.
   ```

4. **Valider** ✅

---

### Étape 3: Attendre la propagation DNS (10-60 min)

Les DNS prennent du temps à se propager mondialement.

**Vérifier la propagation:**

1. **Site web (immédiat):**
   ```
   https://dnschecker.org
   ```
   - Entrez: torah-ai.com
   - Type: A
   - Vérifiez que ça pointe vers 216.24.57.1

2. **Ligne de commande:**
   ```bash
   # Vérifier le domaine principal
   dig torah-ai.com +short
   # Devrait retourner: 216.24.57.1

   # Vérifier www
   dig www.torah-ai.com +short
   # Devrait retourner: torah-ai-xxxx.onrender.com
   ```

**Durée typique:**
- Namecheap: 10-30 minutes
- Cloudflare: 5-10 minutes (très rapide!)
- OVH: 30-60 minutes

---

### Étape 4: HTTPS automatique (5-10 min après DNS)

**Render va automatiquement:**
1. Détecter que le domaine pointe vers eux
2. Générer un certificat SSL avec Let's Encrypt
3. Activer HTTPS

**Dans Render > Settings > Custom Domain:**

Vous verrez:
```
torah-ai.com          ✓ Verified
www.torah-ai.com      ✓ Verified
```

Avec des icônes de cadenas verts! 🔒

**Si ça ne se passe pas automatiquement:**
- Attendre encore 10-15 minutes
- Vérifier que les DNS sont bien configurés
- Vérifier que le proxy Cloudflare est OFF si vous utilisez Cloudflare

---

## PARTIE 3: TESTER LE SITE (2 minutes)

### Tests à faire:

1. **Santé de l'API:**
   ```bash
   curl https://torah-ai.com/health
   ```

   Devrait retourner:
   ```json
   {"status": "healthy", "message": "Le Rav virtuel est prêt à enseigner"}
   ```

2. **Page d'accueil:**
   ```bash
   curl https://torah-ai.com/
   ```

3. **Documentation:**
   Ouvrir dans le navigateur:
   ```
   https://torah-ai.com/docs
   ```

4. **Poser une question:**
   ```bash
   curl -X POST https://torah-ai.com/api/v1/question \
     -H "Content-Type: application/json" \
     -d '{"question": "Qu'"'"'est-ce que le Shabbat?", "langue": "fr"}'
   ```

5. **Les deux URLs doivent fonctionner:**
   - https://torah-ai.com ✅
   - https://www.torah-ai.com ✅

---

## PARTIE 4: OPTIMISATIONS (Optionnel)

### A) Empêcher le sommeil (Gratuit)

L'app Render gratuite dort après 15 min.

**Solution: UptimeRobot**

1. Aller sur https://uptimerobot.com (gratuit)
2. Créer un compte
3. Add New Monitor:
   ```
   Monitor Type: HTTPS
   Friendly Name: Torah AI
   URL: https://torah-ai.com/health
   Monitoring Interval: 5 minutes
   ```
4. L'app ne dormira plus jamais! ✅

### B) Redirection www → non-www (ou inverse)

**Dans Render:**

Pour rediriger www vers le domaine principal:
1. Settings > Redirects (si disponible)
2. Ou ajouter dans votre code API (api/main.py):

```python
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

app.add_middleware(HTTPSRedirectMiddleware)
```

### C) Google Analytics (Optionnel)

Pour suivre vos utilisateurs:
1. Créer compte Google Analytics
2. Obtenir le tracking code
3. Ajouter dans votre frontend (quand vous en aurez un)

---

## RÉCAPITULATIF FINAL

### ✅ Checklist complète:

- [ ] Compte Render créé
- [ ] Service web déployé sur Render
- [ ] API fonctionne sur l'URL temporaire Render
- [ ] Domaine torah-ai.com ajouté dans Render
- [ ] DNS configurés chez le registrar
- [ ] DNS propagés (vérifier avec dnschecker.org)
- [ ] HTTPS activé automatiquement
- [ ] Tests réussis sur https://torah-ai.com
- [ ] www.torah-ai.com fonctionne aussi
- [ ] UptimeRobot configuré (optionnel)

### 🎯 Vos URLs finales:

**API principale:**
```
https://torah-ai.com
```

**Documentation interactive:**
```
https://torah-ai.com/docs
```

**Health check:**
```
https://torah-ai.com/health
```

---

## 🎊 FÉLICITATIONS!

Votre Rav Virtuel est maintenant accessible sur **torah-ai.com**! 🌟

### 📢 Partager votre création:

**Message pour réseaux sociaux:**
```
🌟 Torah AI est en ligne! 🌟

Un Rav virtuel accessible 24/7 pour répondre à vos questions sur:
📖 Torah
📚 Mishna & Talmud
✨ Kabbalah
⚖️ Halakha

En français, anglais, hébreu, espagnol, russe...

🔗 https://torah-ai.com
📖 Docs: https://torah-ai.com/docs

Fait avec amour et les valeurs du judaïsme 💙
#Torah #Judaism #AI #Education
```

### 🚀 Prochaines étapes:

1. ✅ Partager avec votre communauté
2. ✅ Récolter des retours
3. ✅ Ajouter du contenu (import Sefaria)
4. ✅ Activer l'IA complète (clés API)
5. ✅ Enrichir la base de données

---

## ❓ Dépannage

### Le domaine ne fonctionne pas après 1 heure

1. **Vérifier les DNS:**
   ```bash
   dig torah-ai.com +short
   ```
   Doit retourner: 216.24.57.1

2. **Vérifier dans Render:**
   Settings > Custom Domain
   Les deux domaines doivent être "Verified" ✓

3. **Si Cloudflare:**
   Le proxy doit être OFF (nuage gris)

4. **Vider le cache DNS local:**
   ```bash
   # Linux
   sudo systemd-resolve --flush-caches

   # Mac
   sudo dscacheutil -flushcache

   # Windows
   ipconfig /flushdns
   ```

### HTTPS ne fonctionne pas

1. Attendre encore 10-15 minutes
2. Vérifier que les DNS pointent bien
3. Dans Render: "Force SSL" doit être activé

### L'app Render ne démarre pas

1. Voir les logs: Dashboard > Logs
2. Vérifier que `init_sqlite.py` s'est bien exécuté
3. Si besoin, redéployer: Deploy > Manual Deploy

---

## 📞 Besoin d'aide?

- **Logs Render:** Dashboard > votre service > Logs
- **Status Render:** https://status.render.com
- **Documentation:** https://torah-ai.com/docs

---

**B'hatzla'cha avec torah-ai.com! 🙏✨**

*Votre Rav virtuel est maintenant accessible au monde entier!*
