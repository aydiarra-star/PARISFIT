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
- Le cache hors ligne couvre les ressources statiques ; les polices externes peuvent nécessiter une connexion.

## Étapes techniques suivantes
1. Confirmer PWA ou application native.
2. Choisir backend, authentification et base de données.
3. Définir les contrats API et le modèle de données.
4. Mettre en place tests automatisés, accessibilité et CI.
5. Intégrer des contenus sportifs et nutritionnels revus et licenciés.
