# PARISFIT — Architecture initiale

## État constaté
Le dépôt ne contenait aucun code applicatif au début du chantier. Le premier incrément utilise HTML, CSS et JavaScript natifs, sans dépendance de compilation.

## Structure
- `index.html` : quatre espaces fonctionnels et accueil.
- `styles.css` : identité visuelle et responsive desktop/mobile.
- `app.js` : navigation, interactions, données locales et dialogues.
- `manifest.webmanifest` : métadonnées PWA.
- `service-worker.js` : cache de l'enveloppe statique.
- `assets/icon.svg` : icône vectorielle.

## Décisions et limites
- Socle initial web/PWA, pas une application native iOS/Android.
- Les données sont stockées dans localStorage sur l'appareil courant ; aucune authentification, synchronisation ou sauvegarde serveur n'est implémentée.
- La séance et les idées de repas sont des exemples de démonstration, pas une bibliothèque professionnelle validée.
- Aucun score de vitalité n'est calculé : le ressenti est déclaré par l'utilisateur et clairement distingué d'une mesure médicale.
- Aucun service IA, paiement, suivi santé ou analyse caméra n'est connecté.
- Le cache hors ligne couvre les ressources statiques et les visuels ; les polices système ne nécessitent aucune connexion.

## Étapes techniques suivantes
1. Confirmer PWA ou application native.
2. Choisir backend, authentification et base de données.
3. Définir les contrats API et le modèle de données.
4. Mettre en place tests automatisés, accessibilité et CI.
5. Intégrer des contenus sportifs et nutritionnels revus et licenciés.

## Accueil de référence (novembre 2026)
- L’accueil réutilise `index.html`, `styles.css` et les parcours de `app.js` ; aucun framework ni route dupliquée.
- `demo-data.js` sépare les valeurs illustratives de vitalité (92, +12 %, 3 jours), l’énergie initiale, la lecture et le catalogue d’exercices du code d’interaction. Le score et la série ne sont ni calculés ni enregistrés ; la mention « Démonstration · score non mesuré » les distingue des données personnelles.
- Le prénom, les habitudes, l’eau, le journal et le ressenti restent dans `parisfit.v1`. L’énergie déclarée remplace l’exemple « Pleine ». Aucun prénom fictif n’est attribué au visiteur.
- La barre d’eau utilise le compteur existant : 8 verres de 250 ml. Son pourcentage et le volume restant sont cohérents et partagés avec Nutrition.
- Les quatre cartes ouvrent les parcours existants : lecture, Mental, pause et création d’une habitude. Le défi est une proposition, pas un suivi automatique de 30 jours.
- `assets/coach-welcome.jpg` et `assets/workout.jpg` sont des illustrations photographiques générées par IA, inspirées de la référence fournie, pas des photographies de coachs partenaires.
- Le service worker v4 inclut les nouvelles ressources ; typographie système disponible hors ligne.

## Coach 3D — première base technique
- `coach-3d.js` : scène Three.js, personnage humanoïde construit à partir de segments et articulations, éclairage, sol, caméra responsive et cycles d'animation par exercice.
- Rendu WebGL chargé depuis jsDelivr ; fallback visuel si WebGL indisponible.
- Cette base n'est pas un modèle GLB de qualité studio, une mocap validée, un système de correction biomécanique ni une IA conversationnelle connectée.
