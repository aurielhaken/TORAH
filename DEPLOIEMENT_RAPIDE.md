# Déploiement Rapide sur Render.com 🚀

## 5 minutes pour mettre votre Rav Virtuel en ligne!

### Étape 1: Créer un compte Render (1 min)

1. Aller sur https://render.com
2. Cliquer sur "Get Started"
3. S'inscrire avec GitHub (recommandé)
4. Autoriser Render à accéder à vos repos

### Étape 2: Créer le service web (2 min)

1. Dans le dashboard, cliquer sur **"New +"** (en haut à droite)
2. Sélectionner **"Web Service"**
3. Connecter votre repository:
   - Si pas visible: "Configure account" et autoriser l'accès au repo TORAH
   - Sélectionner le repository **TORAH**
4. Cliquer sur **"Connect"**

### Étape 3: Configuration (1 min)

Render va détecter automatiquement le `render.yaml`, mais vous pouvez aussi configurer manuellement:

**Configuration de base:**
```
Name: torah-ai
Region: Frankfurt (Europe) ou Oregon (USA)
Branch: claude/session-011CUYdMn11QoLqwzVzouCem
Environment: Python 3
```

**Commandes:**
```
Build Command: pip install -r requirements-minimal.txt && python database/init_sqlite.py
Start Command: uvicorn api.main:app --host 0.0.0.0 --port $PORT
```

**Type d'instance:**
```
Instance Type: Free
```

### Étape 4: Variables d'environnement (optionnel)

Cliquez sur "Advanced" puis ajoutez:

| Key | Value |
|-----|-------|
| `DATABASE_URL` | `sqlite:///./torah_ai.db` |
| `DEBUG` | `false` |
| `LOG_LEVEL` | `INFO` |
| `PYTHON_VERSION` | `3.11.14` |

### Étape 5: Déployer! (1 min)

1. Cliquer sur **"Create Web Service"**
2. Render va:
   - Cloner votre code
   - Installer les dépendances
   - Initialiser la base de données
   - Démarrer l'API
3. Attendre 2-3 minutes

### Étape 6: C'est en ligne! ✅

Votre Rav Virtuel est maintenant accessible à l'URL:
```
https://torah-ai.onrender.com
```

**Testez immédiatement:**
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

### Étape 7: Tester l'API

**Documentation interactive:**
```
https://votre-url.onrender.com/docs
```

**Poser une question:**
```bash
curl -X POST https://votre-url.onrender.com/api/v1/question \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Quelle est la signification du Shabbat?",
    "langue": "fr"
  }'
```

---

## 🎊 FÉLICITATIONS!

Votre Rav Virtuel est maintenant accessible au monde entier! 🌍

### Partager votre création:

**Lien direct à partager:**
```
https://votre-url.onrender.com
```

**Sur les réseaux:**
```
🌟 Découvrez Torah AI - Un Rav virtuel accessible 24/7!

Posez vos questions sur:
📖 Torah
📚 Mishna & Talmud
✨ Kabbalah
⚖️ Halakha

Réponses en français, anglais, hébreu...

🔗 https://votre-url.onrender.com
```

---

## 📊 Monitoring et Logs

**Voir les logs en temps réel:**
1. Dashboard Render > Votre service
2. Onglet "Logs"
3. Vous verrez toutes les requêtes et erreurs

**Statistiques:**
- Nombre de requêtes
- Temps de réponse
- Utilisation mémoire

---

## 🔄 Mises à jour automatiques

**À chaque push Git:**
1. Render détecte le nouveau code
2. Redéploie automatiquement
3. Zero downtime!

```bash
# Faire des modifications
git add .
git commit -m "feat: amélioration"
git push

# Render redéploie automatiquement! 🎉
```

---

## ⚡ Optimisations

### 1. Empêcher le sommeil (gratuit)

Render met l'app en veille après 15 min d'inactivité.

**Solution: UptimeRobot**
1. Aller sur https://uptimerobot.com (gratuit)
2. Créer un monitor:
   - Type: HTTPS
   - URL: `https://votre-url.onrender.com/health`
   - Interval: 5 minutes
3. L'app ne dormira plus jamais! ✅

### 2. Domaine personnalisé (optionnel)

**Si vous achetez un domaine plus tard:**
1. Dashboard > Settings > Custom Domain
2. Ajouter: `torah-ai.com`
3. Configurer les DNS chez votre registrar
4. HTTPS automatique! ✅

---

## ❓ Problèmes courants

### L'app ne démarre pas

**Vérifier les logs:**
- Dashboard > Logs
- Chercher les erreurs

**Causes fréquentes:**
- Dépendances manquantes → vérifier `requirements-minimal.txt`
- Port incorrect → doit être `$PORT`
- Base de données → vérifier que `init_sqlite.py` s'est exécuté

### L'app se met en veille

**Normal sur le plan gratuit!**
- Se réveille en ~30 secondes
- Solution: UptimeRobot (voir ci-dessus)

### Requêtes lentes

**Première requête après sommeil:**
- Prend 30 sec (réveil)
- Ensuite rapide

**Si toujours lent:**
- Migrer vers plan payant ($7/mois)
- Ou changer de plateforme

---

## 💰 Coûts

**Plan gratuit:**
- ✅ 750 heures/mois
- ✅ HTTPS inclus
- ✅ Redéploiements illimités
- ⏰ Se met en veille après 15 min

**Si besoin de plus:**
- Starter: $7/mois (pas de sommeil, plus rapide)
- Standard: $25/mois (production)

---

## 🚀 Prochaines étapes

**Maintenant que c'est en ligne:**

1. ✅ Tester avec des amis
2. ✅ Récolter des retours
3. ✅ Enrichir le contenu
4. ✅ Partager sur les réseaux

**Dans 1 mois (si succès):**
- Acheter un domaine
- Ajouter analytics
- Plus de contenu (Sefaria)

**Dans 3 mois (si croissance):**
- Migrer vers serveur dédié
- PostgreSQL + pgvector
- App mobile

---

## 📞 Support

**Problèmes?**
- Logs Render: Dashboard > Logs
- Documentation: /docs sur votre URL
- Issues GitHub

---

## 🎉 Récapitulatif

✅ Compte Render créé
✅ Service web configuré
✅ Application déployée
✅ Tests réussis
✅ URL partageable

**Votre Rav Virtuel est en ligne!** 🌟

**URL:** https://votre-url.onrender.com
**Docs:** https://votre-url.onrender.com/docs

---

**B'hatzla'cha pour votre lancement! 🙏**

*"עשה לך רב" - "Fais-toi un maître"*
