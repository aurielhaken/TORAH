# 🚀 Démarrage Rapide DoctHair Landing Page

## En 3 étapes

### 1️⃣ Ajouter une vidéo (optionnel)

Téléchargez une vidéo de microscope depuis [Pexels](https://www.pexels.com/search/videos/microscope/) et placez-la ici :
```
frontend/assets/videos/microscope-analysis.mp4
```

**Ou laissez comme ça** - l'animation de placeholder s'affichera automatiquement !

### 2️⃣ Lancer le serveur

#### Python (recommandé - le plus simple)
```bash
cd frontend
python3 -m http.server 8000
```

#### Node.js
```bash
cd frontend
npx serve
```

### 3️⃣ Ouvrir dans le navigateur

Ouvrez votre navigateur et allez sur :
```
http://localhost:8000
```

## ✨ C'est tout !

Vous devriez voir une magnifique landing page avec :
- ✅ Design ultra-moderne
- ✅ Animations fluides
- ✅ Cartes flottantes animées
- ✅ Particules en arrière-plan
- ✅ Navigation responsive
- ✅ Effets de parallaxe

## 🎨 Personnaliser

### Changer les couleurs
Éditez `css/style.css` ligne 10-14 :
```css
--primary: #E87722;        /* Orange DoctHair */
--primary-dark: #C85F15;
--primary-light: #FF9447;
```

### Changer le texte
Éditez `index.html` :
- Ligne 73 : Titre principal
- Ligne 78 : Description
- Ligne 88 : Fonctionnalités

## 🔥 Astuce Pro

Pour un rechargement automatique, installez Live Server :
1. Ouvrez VS Code
2. Installez l'extension "Live Server"
3. Clic droit sur `index.html` → "Open with Live Server"

## 📱 Tester le responsive

- Ouvrez Chrome DevTools (F12)
- Cliquez sur l'icône mobile (Ctrl+Shift+M)
- Testez différentes tailles d'écran

## 🎯 Prochaines étapes

1. Remplacez l'animation placeholder par une vraie vidéo
2. Connectez les boutons CTA à votre backend
3. Ajoutez Google Analytics
4. Déployez sur Netlify/Vercel

## ❓ Besoin d'aide ?

Consultez le `README.md` complet pour plus d'informations !

---

**Bon développement ! 🚀**
