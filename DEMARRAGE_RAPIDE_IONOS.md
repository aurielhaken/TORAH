# ⚡ Démarrage Rapide - Déploiement IONOS

**Torah AI - Rav Virtuel** en ligne en 10 minutes ! 🚀

## 🎯 Ce qu'il vous faut

1. **Un serveur IONOS** (VPS ou Cloud Server)
2. **Un nom de domaine** (optionnel mais recommandé)
3. **Accès SSH** à votre serveur

## 🚀 Installation en 3 étapes

### Étape 1 : Connexion SSH

```bash
ssh votre_utilisateur@votre-serveur.ionos.com
```

### Étape 2 : Installation automatique

```bash
# Télécharger et exécuter le script d'installation
curl -fsSL https://raw.githubusercontent.com/aurielhaken/TORAH/main/install_ionos.sh | bash
```

**OU** manuellement :

```bash
# Cloner le projet
git clone https://github.com/aurielhaken/TORAH.git
cd TORAH

# Lancer l'installation
chmod +x install_ionos.sh
./install_ionos.sh
```

### Étape 3 : Configurer votre domaine

1. Allez sur **IONOS.com** > Domaines
2. Créez un **enregistrement A** :
   - **Type** : A
   - **Nom** : @ (ou api)
   - **Valeur** : IP de votre serveur (affiché en fin d'installation)
   - **TTL** : 3600

## ✅ C'est tout !

Votre API est en ligne ! Accédez à :

- 🏠 **Page d'accueil** : `http://votre-domaine.com`
- 📚 **Documentation** : `http://votre-domaine.com/docs`
- 💚 **Health check** : `http://votre-domaine.com/health`

## 📱 Tester depuis votre téléphone

Ouvrez simplement votre navigateur mobile et allez sur :
```
http://votre-domaine.com/docs
```

Vous verrez l'interface Swagger où vous pouvez tester l'API ! 🎉

## 🔧 Commandes utiles

```bash
# Voir les logs en temps réel
sudo journalctl -u torah-ai -f

# Redémarrer l'application
sudo systemctl restart torah-ai

# Vérifier le statut
sudo systemctl status torah-ai

# Mettre à jour le code
cd ~/TORAH
git pull
sudo systemctl restart torah-ai
```

## ❓ Besoin d'aide ?

Consultez la documentation complète : [DEPLOIEMENT_IONOS.md](./DEPLOIEMENT_IONOS.md)

## 🎊 Prochaines étapes

Maintenant que votre API est en ligne, vous pouvez :

1. ✅ Tester l'API depuis n'importe où
2. 🔒 Activer HTTPS (fait automatiquement si vous avez dit oui)
3. 📊 Initialiser la base de données avec des textes
4. 🤖 Intégrer l'IA pour de vraies réponses
5. 🎨 Créer une belle interface web

**Félicitations ! Torah AI est accessible au monde entier ! 🌍**
