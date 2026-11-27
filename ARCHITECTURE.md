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

La navigation met à jour les quatre espaces sur desktop et mobile, avec un état accessible pour les menus. Le dialogue natif conserve son ouverture lors des sous-actions et ses boutons internes ne déclenchent pas la fermeture implicite du formulaire.

## Données et limites

Les préférences, habitudes, hydratation, ressenti et journal sont enregistrés dans `localStorage` sur l'appareil courant. Ils ne sont ni synchronisés ni sauvegardés sur un serveur. Le stockage local ne constitue pas un coffre-fort pour des données sensibles.

Le ressenti est une déclaration de l'utilisateur, pas une mesure médicale. La séance et les idées de repas sont des exemples de démonstration, pas une bibliothèque professionnelle validée.

Aucun backend, authentification, IA, paiement, suivi santé, analyse caméra ou coach 3D n'est connecté. Le socle web/PWA ne doit pas être présenté comme une application native iOS/Android.

## Modèle de données

Le modèle logique des données et les règles de confidentialité sont décrits dans DATA_MODEL.md. Il s'agit d'une spécification de conception ; aucune base de données ni migration SQL n'est encore déployée.

## Cible backend proposée (non déployée)

L'architecture cible sépare le client PWA/mobile, une couche API versionnée, les services métier, la passerelle IA et le stockage. PostgreSQL est privilégié pour les relations entre profils, objectifs, tâches, habitudes, séances, nutrition, bien-être et équilibre de vie.

La comparaison des fournisseurs et les limites de la recommandation sont consignées dans BACKEND_DECISION.md. Supabase/PostgreSQL est l'option à évaluer en premier ; ce n'est pas encore une décision approuvée. Render + PostgreSQL reste l'alternative pour une API entièrement maîtrisée. Firebase reste une option si ses fonctions temps réel et mobile justifient le modèle NoSQL.

Les règles d'authentification, d'autorisation, de consentement, de synchronisation hors ligne, d'export et d'effacement sont détaillées dans AUTH_SYNC_SECURITY.md. L'API logique existante reste décrite dans API_CONTRACT.md.

## Règles d'architecture

- Ne jamais exposer de clé privilégiée ou de secret serveur dans le frontend.
- Isoler le fournisseur derrière une couche d'accès pour limiter le verrouillage.
- Faire appliquer les autorisations côté serveur et, si disponible, au niveau des lignes en base.
- Utiliser IndexedDB pour les données structurées hors ligne ; réserver le cache service worker aux ressources statiques publiques.
- Ne pas migrer de données sensibles réelles avant validation des droits, du consentement, des sauvegardes et du parcours de suppression.
- Ne créer aucun service payant ou abonnement sans accord explicite.

## Prochaine étape

Construire un prototype backend isolé et jetable uniquement après validation du fournisseur, puis démontrer l'isolation des utilisateurs, l'export, l'effacement, la restauration et la synchronisation avant toute migration du prototype local.