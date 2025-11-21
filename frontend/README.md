# 🎨 DoctHair - Landing Page Premium 2025

Une landing page ultra-moderne pour DoctHair, inspirée du design premium de MyHeritage 2025, avec vidéo en arrière-plan et animations fluides.

## ✨ Fonctionnalités

### Design Premium
- **Glassmorphism** : Effets de verre translucide modernes
- **Gradients sophistiqués** : Couleurs vibrantes et harmonieuses
- **Animations fluides** : Micro-interactions et transitions élégantes
- **Typographie moderne** : Inter + Playfair Display
- **Effets de profondeur** : Ombres et élévations subtiles

### Vidéo en Arrière-plan
- Vidéo haute qualité sur le côté droit
- Animation de placeholder pendant le chargement
- Optimisation automatique des performances
- Pause automatique hors viewport

### Interactions
- **Cartes flottantes** avec effet parallaxe
- **Particules animées** en arrière-plan
- **Scroll animations** progressives
- **Ripple effects** sur les boutons
- **Navigation responsive** avec menu mobile

### Performance
- Chargement optimisé des ressources
- Animations GPU-accelerated
- Lazy loading intelligent
- Responsive design complet

## 📁 Structure

```
frontend/
├── index.html          # Page principale
├── css/
│   └── style.css      # Styles modernes avec animations
├── js/
│   └── app.js         # Interactions JavaScript
└── assets/
    ├── videos/        # Vidéos d'arrière-plan
    └── images/        # Images et icônes
```

## 🚀 Installation

### 1. Ajouter la vidéo

Placez votre vidéo d'analyse microscopique dans :
```
frontend/assets/videos/microscope-analysis.mp4
```

**Recommandations vidéo :**
- Format : MP4 (H.264)
- Résolution : 1080p ou 4K
- Durée : 10-30 secondes (loop)
- Taille : < 10MB optimisé
- Contenu : Analyse microscopique de cheveux, laboratoire, microscope

**Sources vidéo suggérées :**
- [Pexels](https://www.pexels.com/search/videos/microscope/)
- [Pixabay](https://pixabay.com/videos/search/microscope/)
- [Unsplash](https://unsplash.com/s/videos/laboratory)

### 2. Lancer en local

#### Option A : Serveur Python
```bash
cd frontend
python3 -m http.server 8000
```
Ouvrez : http://localhost:8000

#### Option B : Serveur Node.js
```bash
cd frontend
npx serve
```

#### Option C : Live Server (VS Code)
Installez l'extension "Live Server" et cliquez sur "Go Live"

### 3. Personnalisation

#### Couleurs
Modifiez les variables CSS dans `css/style.css` :
```css
:root {
    --primary: #E87722;        /* Couleur principale */
    --primary-dark: #C85F15;   /* Variante sombre */
    --primary-light: #FF9447;  /* Variante claire */
    --accent: #FFD4B8;         /* Couleur d'accent */
}
```

#### Contenu
Éditez le texte dans `index.html` :
- Titre principal : `.hero-title`
- Description : `.hero-description`
- Fonctionnalités : `.features-list`

#### Animations
Ajustez les durées dans `css/style.css` :
```css
--transition-fast: 150ms;
--transition: 300ms;
--transition-slow: 500ms;
```

## 🎬 Intégration avec le Backend

### API Endpoints

```javascript
// Dans js/app.js, connectez les boutons CTA :

// Démarrer le diagnostic
primaryCTA.addEventListener('click', async () => {
    try {
        const response = await fetch('/api/diagnostic/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        const data = await response.json();
        window.location.href = `/diagnostic/${data.id}`;
    } catch (error) {
        console.error('Erreur:', error);
    }
});
```

## 🎨 Personnalisation Avancée

### Ajouter des sections

```html
<!-- Après la section hero -->
<section class="features-section">
    <div class="container">
        <!-- Votre contenu -->
    </div>
</section>
```

### Modifier les cartes flottantes

Dans `index.html`, éditez les `.floating-card` :
```html
<div class="floating-card card-1">
    <div class="card-icon">
        <!-- Votre icône SVG -->
    </div>
    <div class="card-content">
        <div class="card-label">Label</div>
        <div class="card-value">Valeur</div>
    </div>
</div>
```

### Changer les animations

Dans `js/app.js`, modifiez les paramètres d'animation :
```javascript
// Particules
const particleCount = 50; // Nombre de particules

// Cartes flottantes
const speedFactor = (index + 1) * 0.02; // Vitesse parallaxe
```

## 📱 Responsive

La landing page est entièrement responsive :
- **Desktop** : 1920px+
- **Laptop** : 1024px - 1919px
- **Tablet** : 768px - 1023px
- **Mobile** : < 768px

### Points de rupture

```css
@media (max-width: 1024px) { /* Tablet */ }
@media (max-width: 768px)  { /* Mobile */ }
```

## ⚡ Performance

### Optimisations incluses
- ✅ CSS minifié (en production)
- ✅ Images lazy loading
- ✅ Vidéo avec pause hors viewport
- ✅ Animations GPU
- ✅ Debounced scroll events
- ✅ Reduced motion support

### Lighthouse Score Target
- Performance : 90+
- Accessibility : 95+
- Best Practices : 95+
- SEO : 100

## 🎯 Appels à l'action (CTA)

### Bouton Principal
```html
<button class="btn-cta-primary">
    <span>Commencer mon diagnostic gratuit</span>
    <svg><!-- Arrow icon --></svg>
</button>
```

### Bouton Secondaire
```html
<button class="btn-cta-secondary">
    <svg><!-- Eye icon --></svg>
    <span>Voir un exemple de rapport</span>
</button>
```

## 🔧 Dépendances

### Polices Google Fonts
- **Inter** : Texte principal
- **Playfair Display** : Titres

### Aucune dépendance JavaScript externe
Tout est vanilla JavaScript pour performance maximale !

## 📊 Analytics

Intégrez Google Analytics 4 :

```html
<!-- Avant </head> -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## 🚀 Déploiement

### Netlify
```bash
# Déployer directement le dossier frontend
netlify deploy --dir=frontend --prod
```

### Vercel
```bash
# Dans le dossier frontend
vercel --prod
```

### GitHub Pages
```bash
git subtree push --prefix frontend origin gh-pages
```

## 🎨 Inspiration Design

Cette landing page s'inspire de :
- **MyHeritage** : Design premium et sophistiqué
- **Apple** : Minimalisme et animations fluides
- **Stripe** : Glassmorphism et gradients modernes
- **Linear** : Micro-interactions élégantes

## 📝 TODO

- [ ] Ajouter section "Comment ça marche"
- [ ] Créer page "Exemple de rapport"
- [ ] Intégrer formulaire de diagnostic
- [ ] Ajouter témoignages clients
- [ ] Créer section FAQ
- [ ] Optimiser SEO (meta tags, structured data)
- [ ] Ajouter support multilingue
- [ ] Intégrer chat support

## 📄 Licence

Propriétaire - DoctHair © 2025

---

**Développé avec ❤️ pour la santé capillaire**

Pour toute question : support@docthair.com
