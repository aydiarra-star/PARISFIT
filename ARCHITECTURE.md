# PARISFIT — Architecture initiale

## État constaté

Le socle actuellement fusionné est une application web/PWA légère, écrite en HTML, CSS et JavaScript natifs, sans étape de compilation.

## Structure actuelle

- `index.html` : navigation et quatre espaces fonctionnels.
- `styles.css` : identité visuelle et adaptations desktop/mobile.
- `app.js` : interactions et persistance locale.
- `manifest.webmanifest` : métadonnées PWA.
- `service-worker.js` : cache de l'enveloppe statique.
- `assets/icon.svg` : icône.
- `scripts/validate.mjs` : contrôles structurels sans dépendance.
- `tests/*.test.mjs` : tests automatisés Node.js.

## Données et limites

Les préférences, habitudes, hydratation, ressenti et journal sont enregistrés dans `localStorage` sur l'appareil courant. Ils ne sont ni synchronisés ni sauvegardés sur un serveur. Le stockage local ne constitue pas un coffre-fort pour des données sensibles.

Le ressenti est une déclaration de l'utilisateur, pas une mesure médicale. La séance et les idées de repas sont des exemples de démonstration, pas une bibliothèque professionnelle validée.

Aucun backend, authentification, IA, paiement, suivi santé, analyse caméra ou coach 3D n'est connecté. Le socle web/PWA ne doit pas être présenté comme une application native iOS/Android.

## Prochaine décision d'architecture

Avant de connecter un backend ou de migrer la technologie, comparer les besoins PWA et natifs, les coûts d'exploitation, la sécurité, les possibilités hors ligne et les contraintes de publication. Les choix doivent être documentés avant implémentation.
