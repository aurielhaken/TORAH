# Déploiement sur Vercel avec torah-ai.com 🚀

## Déploiement ULTRA-RAPIDE (3 minutes!)

Vercel est **parfait** pour votre cas! C'est gratuit, instantané et très rapide.

---

## ÉTAPE 1: Déployer sur Vercel (2 minutes)

### A) Créer un compte (30 secondes)

1. **Aller sur Vercel:**
   ```
   https://vercel.com
   ```

2. **Sign up with GitHub** (recommandé)
   - Cliquez sur "Sign Up"
   - Choisissez "Continue with GitHub"
   - Autorisez Vercel

3. **Vous arrivez sur le Dashboard** ✅

---

### B) Importer le projet (1 minute)

1. **Dans le Dashboard Vercel:**
   - Cliquez sur **"Add New"** (bouton en haut à droite)
   - Sélectionnez **"Project"**

2. **Importer depuis GitHub:**
   - Sélectionnez votre repository **TORAH**
   - Cliquez sur **"Import"**

3. **Configuration automatique:**

   Vercel détecte Python automatiquement!

   **Paramètres à vérifier/modifier:**
   ```
   Framework Preset: Other
   Build Command: (laisser vide)
   Output Directory: (laisser vide)
   Install Command: pip install -r requirements-minimal.txt
   ```

4. **Variables d'environnement (optionnel):**

   Cliquez sur "Environment Variables" et ajoutez:

   | Name | Value |
   |------|-------|
   | `PYTHON_VERSION` | `3.11` |
   | `DATABASE_URL` | `sqlite:///./torah_ai.db` |

5. **Déployer:**
   - Cliquez sur le gros bouton **"Deploy"**
   - Vercel va construire et déployer
   - **Durée: 30-60 secondes!** ⚡

6. **C'EST EN LIGNE! ✅**

   Vercel vous donne une URL:
   ```
   https://torah-xxxx.vercel.app
   ```

   **Testez immédiatement:**
   - Cliquez sur "Visit" ou
   - Ouvrez l'URL dans votre navigateur

---

## ÉTAPE 2: Configurer torah-ai.com (2 minutes)

### A) Ajouter le domaine dans Vercel (1 minute)

1. **Dans votre projet Vercel:**
   - Cliquez sur l'onglet **"Settings"** (en haut)
   - Dans le menu de gauche: **"Domains"**

2. **Ajouter votre domaine:**
   - Entrez: `torah-ai.com`
   - Cliquez sur **"Add"**

3. **Vercel vous montre les DNS à configurer:**

   Il vous proposera automatiquement:
   - Configuration A Record pour le domaine principal
   - Configuration CNAME pour www

   **Notez ces valeurs!**

---

### B) Configurer les DNS (1 minute)

**Où avez-vous acheté torah-ai.com?**

#### Si Namecheap:

1. Aller sur Namecheap > Domain List > Manage
2. Advanced DNS
3. Ajouter les enregistrements donnés par Vercel:

   **Type 1: A Record**
   ```
   Type: A Record
   Host: @
   Value: 76.76.21.21  (IP de Vercel)
   TTL: Automatic
   ```

   **Type 2: CNAME**
   ```
   Type: CNAME
   Host: www
   Value: cname.vercel-dns.com
   TTL: Automatic
   ```

#### Si Cloudflare:

1. DNS Settings
2. Ajouter:
   ```
   Type: A
   Name: @
   IPv4: 76.76.21.21
   Proxy: OFF (nuage gris!)
   ```
   ```
   Type: CNAME
   Name: www
   Target: cname.vercel-dns.com
   Proxy: OFF (nuage gris!)
   ```

#### Si OVH:

1. Zone DNS
2. Ajouter:
   ```
   Type: A
   Sous-domaine: (vide)
   Cible: 76.76.21.21
   ```
   ```
   Type: CNAME
   Sous-domaine: www
   Cible: cname.vercel-dns.com
   ```

---

### C) Vérification (Automatique!)

**Vercel vérifie automatiquement les DNS!**

Dans Domains, vous verrez:
```
torah-ai.com          ✓ Valid Configuration
www.torah-ai.com      ✓ Valid Configuration
```

**HTTPS est automatique! 🔒**
- Certificat SSL de Vercel (Let's Encrypt)
- Pas besoin de configuration!

**Délai:** 5-30 minutes pour la propagation DNS

---

## ÉTAPE 3: Tester (1 minute)

### Tests:

1. **Page d'accueil:**
   ```bash
   curl https://torah-ai.com/
   ```

2. **Health check:**
   ```bash
   curl https://torah-ai.com/health
   ```

3. **Documentation:**
   ```
   https://torah-ai.com/docs
   ```

4. **Poser une question:**
   ```bash
   curl -X POST https://torah-ai.com/api/v1/question \
     -H "Content-Type: application/json" \
     -d '{"question": "Qu'"'"'est-ce que le Shabbat?", "langue": "fr"}'
   ```

---

## AVANTAGES DE VERCEL

### ✅ Ce que vous obtenez GRATUITEMENT:

- **Ultra-rapide:** CDN mondial (100+ emplacements)
- **HTTPS automatique:** Certificat SSL inclus
- **Déploiement automatique:** À chaque push Git
- **Pas de sommeil:** Contrairement à Render!
- **Analytics intégrés:** Vercel Analytics (optionnel)
- **Preview deployments:** Chaque PR = URL de preview
- **Bande passante:** 100 GB/mois
- **Limite:** 100 GB-hours de serverless

### 🚀 Performances:

- **Latence:** < 50ms dans le monde entier
- **Uptime:** 99.99%
- **Cache:** Automatique
- **HTTP/2 et HTTP/3:** Activés

---

## DIFFÉRENCE AVEC RENDER

| Feature | Vercel | Render |
|---------|--------|--------|
| **Prix** | Gratuit | Gratuit |
| **Vitesse** | ⚡⚡⚡ Très rapide | ⚡⚡ Rapide |
| **Sommeil** | Jamais | Après 15 min |
| **HTTPS** | Auto | Auto |
| **Domaine** | Inclus | Inclus |
| **CDN** | Mondial | Non |
| **Setup** | 3 min | 5 min |
| **Idéal pour** | APIs légères | Apps persistantes |

**Pour Torah AI:** Les deux fonctionnent! Vercel est plus rapide. ✅

---

## CONFIGURATION AVANCÉE

### A) Redéploiement automatique

**Déjà activé!** À chaque `git push`, Vercel redéploie automatiquement.

Vous pouvez voir:
- Dashboard > Deployments
- Chaque commit = un déploiement
- Rollback facile si problème

### B) Variables d'environnement

Settings > Environment Variables

Ajouter vos clés API quand vous serez prêt:
```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

### C) Analytics (Optionnel - Payant)

Settings > Analytics
- Vercel Analytics: $10/mois
- Voir les visiteurs, pages, performances

Ou utiliser **Google Analytics** (gratuit):
- Créer compte GA
- Ajouter tracking dans votre frontend

### D) Protection DDoS

**Incluse gratuitement!**
- Vercel protège automatiquement
- Rate limiting intelligent
- Bot protection

---

## LIMITES DU PLAN GRATUIT

**Plan Hobby (Gratuit):**
- ✅ Bandwidth: 100 GB/mois
- ✅ Serverless Function Execution: 100 GB-hours
- ✅ Déploiements: Illimités
- ✅ Domaines: Illimités
- ✅ SSL: Inclus

**C'est largement suffisant pour commencer!**

**Si vous dépassez (très peu probable):**
- Pro plan: $20/mois
- Bandwidth: 1 TB
- Execution: 1000 GB-hours

---

## MISES À JOUR AUTOMATIQUES

### Workflow:

1. Vous faites des modifications en local
2. Vous faites un `git push`
3. Vercel détecte le push
4. Build et déploiement automatiques (30 sec)
5. https://torah-ai.com est mis à jour!

**Zéro downtime!** 🎉

---

## MONITORING

### A) Voir les logs

Dashboard > votre projet > Logs

Vous verrez:
- Toutes les requêtes
- Erreurs
- Performances
- Headers

### B) Status

https://www.vercel-status.com

Pour voir si Vercel a des problèmes

### C) Functions

Dashboard > Functions

Voir:
- Nombre d'invocations
- Temps d'exécution
- Erreurs

---

## OPTIMISATIONS

### A) Cache

Vercel cache automatiquement les réponses statiques.

Pour forcer le cache sur certaines routes:
```python
# Dans api/main.py
from fastapi import Response

@app.get("/glossaire/{terme}")
async def get_terme(terme: str, response: Response):
    # Cache pour 1 heure
    response.headers["Cache-Control"] = "public, max-age=3600"
    # ... votre code
```

### B) Edge Functions (Futur)

Quand vous voudrez:
- Vercel Edge Functions (super rapide)
- Exécution au plus près des utilisateurs
- Latence < 10ms

---

## CHECKLIST FINALE

- [ ] Compte Vercel créé
- [ ] Projet importé depuis GitHub
- [ ] Déployé sur Vercel
- [ ] URL temporaire fonctionne
- [ ] Domaine torah-ai.com ajouté
- [ ] DNS configurés
- [ ] DNS propagés (5-30 min)
- [ ] HTTPS activé (automatique)
- [ ] https://torah-ai.com fonctionne ✅
- [ ] https://www.torah-ai.com fonctionne ✅
- [ ] Tests réussis

---

## 🎊 FÉLICITATIONS!

**torah-ai.com** est maintenant en ligne sur Vercel! 🌟

### Vos URLs:

**Site principal:**
```
https://torah-ai.com
```

**Documentation:**
```
https://torah-ai.com/docs
```

**Dashboard Vercel:**
```
https://vercel.com/dashboard
```

---

## PARTAGER

**Message pour les réseaux sociaux:**

```
🌟 Torah AI est en ligne! 🌟

Votre Rav virtuel personnel disponible 24/7
Questions sur Torah, Mishna, Talmud, Kabbalah...

🔗 https://torah-ai.com
📖 Documentation: https://torah-ai.com/docs

Réponses en français, anglais, hébreu, espagnol, russe
Fait avec amour et les valeurs du judaïsme 💙

#Torah #Judaism #AI #Education #TorahAI
```

---

## PROCHAINES ÉTAPES

**Maintenant:**
1. ✅ Partager avec votre communauté
2. ✅ Ajouter du contenu (Sefaria)
3. ✅ Activer l'IA (clés API)

**Plus tard:**
1. Créer un frontend (optionnel)
2. App mobile
3. Plus de langues

---

## SUPPORT

**Problèmes?**
- Logs: Dashboard > Logs
- Status: vercel-status.com
- Docs: vercel.com/docs

**Questions DNS?**
- dnschecker.org pour vérifier
- Attendre 30 min max

---

**B'hatzla'cha! torah-ai.com est en ligne! 🙏✨**

*Ultra-rapide, sécurisé, et accessible au monde entier!*
