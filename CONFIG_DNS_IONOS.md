# 🔧 Configuration DNS pour guematrai.com sur IONOS

## 📋 Guide Spécifique IONOS

---

## ÉTAPE 1 : Connexion à IONOS

1. **Ouvrez :** https://www.ionos.fr (ou .com selon votre pays)
2. **Cliquez** sur "Connexion" en haut à droite
3. **Connectez-vous** avec vos identifiants IONOS

---

## ÉTAPE 2 : Accéder à la gestion DNS

### Option A : Via le menu Domaines

1. Dans le menu de gauche, cliquez sur **"Domaines & SSL"**
2. Vous verrez la liste de vos domaines
3. Trouvez **"guematrai.com"**
4. Cliquez sur l'**icône d'engrenage** ⚙️ à côté du domaine
5. Sélectionnez **"DNS"** dans le menu

### Option B : Via le tableau de bord

1. Tableau de bord → **"Gérer les domaines"**
2. Cliquez sur **"guematrai.com"**
3. Dans les options, cliquez sur **"Paramètres DNS"** ou **"Zone DNS"**

---

## ÉTAPE 3 : Configurer les enregistrements DNS

### Configuration à faire :

Vous devez ajouter/modifier **2 enregistrements DNS** :

---

### 📍 **ENREGISTREMENT 1 : Record A (pour guematrai.com)**

```
┌─────────────────────────────────────────┐
│ Type d'enregistrement : A               │
│ Nom d'hôte : @  (ou laisser vide)      │
│ Pointe vers : 76.76.21.21              │
│ TTL : 3600 (ou par défaut)              │
└─────────────────────────────────────────┘
```

**Comment faire :**

1. Cliquez sur **"Ajouter un enregistrement"** ou **"Nouvel enregistrement"**
2. Sélectionnez **Type : "A"**
3. Dans **"Nom d'hôte"** ou **"Sous-domaine"** :
   - Entrez : `@`
   - OU laissez vide (selon l'interface IONOS)
4. Dans **"Pointe vers"** ou **"Adresse IPv4"** :
   - Entrez : `76.76.21.21`
5. **TTL** : Laissez par défaut (généralement 3600)
6. **Sauvegardez**

---

### 📍 **ENREGISTREMENT 2 : Record CNAME (pour www.guematrai.com)**

```
┌─────────────────────────────────────────┐
│ Type d'enregistrement : CNAME           │
│ Nom d'hôte : www                        │
│ Pointe vers : cname.vercel-dns.com     │
│ TTL : 3600 (ou par défaut)              │
└─────────────────────────────────────────┘
```

**Comment faire :**

1. Cliquez sur **"Ajouter un enregistrement"**
2. Sélectionnez **Type : "CNAME"**
3. Dans **"Nom d'hôte"** ou **"Sous-domaine"** :
   - Entrez : `www`
4. Dans **"Pointe vers"** ou **"Cible"** :
   - Entrez : `cname.vercel-dns.com`
5. **TTL** : Laissez par défaut
6. **Sauvegardez**

---

## ÉTAPE 4 : Vérification de la configuration

### Dans l'interface IONOS, vous devriez voir :

```
┌────────────────────────────────────────────────────┐
│ Type    │ Nom d'hôte │ Valeur                     │
├────────────────────────────────────────────────────┤
│ A       │ @          │ 76.76.21.21                │
│ CNAME   │ www        │ cname.vercel-dns.com       │
└────────────────────────────────────────────────────┘
```

---

## ⚠️ POINTS IMPORTANTS IONOS

### 1. Supprimer les anciens enregistrements

**IMPORTANT :** Si IONOS a créé automatiquement des enregistrements par défaut, vous devez les supprimer ou les modifier :

- ❌ Supprimez tout ancien record A pointant vers une autre IP
- ❌ Supprimez tout ancien CNAME pour www pointant ailleurs
- ❌ Supprimez les records AAAA (IPv6) si présents et non nécessaires

### 2. Désactiver le "Parking de domaine"

Si IONOS a activé le "parking de domaine" :
1. Allez dans **Paramètres du domaine**
2. Désactivez **"Parking de domaine"** ou **"Page de construction"**
3. Activez **"Utiliser mes propres paramètres DNS"**

### 3. Activer les paramètres DNS externes

Certaines interfaces IONOS demandent d'activer l'option :
- **"Utiliser des serveurs de noms externes"** : NON (gardez les DNS IONOS)
- **"Modifier les enregistrements DNS"** : OUI

---

## ÉTAPE 5 : Sauvegarder les changements

1. **Cliquez** sur **"Enregistrer"** ou **"Sauvegarder"**
2. IONOS peut afficher un message de confirmation
3. **IMPORTANT :** Les changements peuvent prendre effet immédiatement chez IONOS, mais la propagation mondiale prend 1-2 heures

---

## ÉTAPE 6 : Vérifier la propagation DNS

### Immédiatement après la configuration :

**Testez avec ces outils :**

1. **DNS Checker** (recommandé)
   ```
   https://dnschecker.org/#A/guematrai.com
   ```
   - Vous devriez voir **76.76.21.21** dans plusieurs régions

2. **Dans votre terminal** (si vous avez accès) :
   ```bash
   # Vérifier le record A
   dig guematrai.com

   # Vérifier le CNAME www
   dig www.guematrai.com
   ```

3. **Vérification simple** :
   ```bash
   nslookup guematrai.com
   ```

---

## ⏱️ TEMPS DE PROPAGATION IONOS

Chez IONOS :
- **Propagation interne** : 5-15 minutes
- **Propagation mondiale** : 1-2 heures (parfois 4-6h)
- **Maximum** : 24-48 heures (rare)

**Patience !** ☕ Pendant l'attente, vous pouvez déjà tester avec l'URL Vercel temporaire : `guematrai.vercel.app`

---

## 🔍 CAPTURES D'ÉCRAN TYPE (Interface IONOS)

L'interface IONOS devrait ressembler à ceci :

```
┌─────────────────────────────────────────────┐
│ guematrai.com - Gestion DNS                 │
├─────────────────────────────────────────────┤
│                                             │
│ [+ Ajouter un enregistrement]              │
│                                             │
│ ┌───────────────────────────────────────┐  │
│ │ Type: A                               │  │
│ │ Nom d'hôte: @                        │  │
│ │ Pointe vers: 76.76.21.21            │  │
│ │ [Enregistrer]                         │  │
│ └───────────────────────────────────────┘  │
│                                             │
│ ┌───────────────────────────────────────┐  │
│ │ Type: CNAME                           │  │
│ │ Nom d'hôte: www                      │  │
│ │ Pointe vers: cname.vercel-dns.com   │  │
│ │ [Enregistrer]                         │  │
│ └───────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

---

## ❓ PROBLÈMES COURANTS IONOS

### Problème 1 : "L'enregistrement existe déjà"

**Solution :**
- Modifiez l'enregistrement existant au lieu d'en créer un nouveau
- Cliquez sur l'icône de modification (crayon) ✏️

### Problème 2 : "Le domaine est parqué"

**Solution :**
1. Allez dans **Paramètres du domaine**
2. **Désactivez** "Parking de domaine"
3. Choisissez "Utiliser mes paramètres DNS personnalisés"

### Problème 3 : "Impossible d'ajouter CNAME pour www"

**Solution :**
- Il existe peut-être déjà un record A pour www
- Supprimez le record A pour www
- Puis créez le CNAME

### Problème 4 : "TTL trop court"

**Solution :**
- IONOS impose parfois un TTL minimum
- Utilisez 3600 (1 heure) ou 86400 (24h)

### Problème 5 : Interface en allemand

Si l'interface est en allemand :
- **"Hinzufügen"** = Ajouter
- **"Speichern"** = Sauvegarder
- **"A-Record"** = Enregistrement A
- **"CNAME-Record"** = Enregistrement CNAME

---

## ✅ VÉRIFICATION FINALE

Une fois les DNS configurés et propagés, testez :

### 1. Ping du domaine
```bash
ping guematrai.com
```
Devrait répondre avec l'IP de Vercel

### 2. Test HTTPS
```bash
curl -I https://guematrai.com
```
Devrait retourner un code 200

### 3. Test dans le navigateur
```
https://guematrai.com
```
Devrait afficher votre belle page d'accueil !

---

## 📞 SUPPORT IONOS

Si vous rencontrez des problèmes :

**Support IONOS :**
- France : 09 70 80 89 11
- Web : https://www.ionos.fr/assistance
- Chat : Disponible dans le tableau de bord

**Questions courantes :**
- "Comment modifier les enregistrements DNS ?"
- "Comment désactiver le parking de domaine ?"
- "Combien de temps prend la propagation DNS ?"

---

## 🎯 RÉSUMÉ RAPIDE IONOS

```bash
1. Connexion IONOS → Domaines & SSL
2. Sélectionner guematrai.com → DNS
3. Ajouter Record A : @ → 76.76.21.21
4. Ajouter CNAME : www → cname.vercel-dns.com
5. Sauvegarder
6. Attendre 1-2 heures
7. Tester : https://guematrai.com
```

---

## 🚀 APRÈS LA CONFIGURATION DNS

Une fois les DNS propagés :

1. ✅ Retournez sur Vercel
2. ✅ Dans Settings → Domains, Vercel devrait afficher "Valid Configuration"
3. ✅ Vercel génère automatiquement le certificat SSL (2-3 minutes)
4. ✅ Testez https://guematrai.com

**Et voilà ! Votre site est EN LIGNE ! 🎉**

---

🔯 **B'hatzla'ha avec guematrai.com sur IONOS !**
