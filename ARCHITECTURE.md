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
- Le service worker de l’accueil inclut les nouvelles ressources ; typographie système disponible hors ligne.

## Coach humain 3D — expérimental (branche dédiée, après PR #10)
- `coach-3d.js` utilise Three.js 0.169.0 local, GLTFLoader, AnimationMixer et OrbitControls.
- `assets/coach/coach.glb` contient le modèle Microsoft Rocketbox Sports_Male_04, 80 os, quatre textures (couleur visage 2048 px, autres 1024 px, normales PNG) et huit animations. Provenance et MIT conservées dans `assets/coach/`.
- `tools/` contient le pipeline reproductible : téléchargement figé, correction de la hiérarchie FBX, création de clips par IK et export GLB. Il ne s’agit pas de mocap.
- Contrat préservé : `window.parisfitCoachExercise`, événement `parisfit:coach-exercise`, IDs `coach-stage-*`. `renderCoachStage` ne remplace plus le canvas ; le module 3D possède seul les commandes de lecture.
- Chargement différé quand la scène devient visible ; rendu suspendu hors champ, onglet masqué ou en pause. Ressources WebGL libérées à la fermeture, fallback textuel et retry si échec.
- Cache v6 : moteur local et miniatures précachés, modèle mis en cache à la demande. Hors ligne 3D seulement après une première consultation réussie.
- Les huit clips, les commandes et les vues sont testés techniquement. La validation sportive, la fidélité des contacts, les transitions et le niveau de qualité premium ne sont pas acquis. Pas de fusion tant que les critères de sortie du rapport ne sont pas levés.
- Détails et preuves : `docs/coach/REPORT.md`. Tests : `tests/coach-asset.cjs`, `tests/coach-browser.cjs` et régression `tests/smoke.cjs`.

### Coach phase 2

`coach-content.js` définit les phases normalisées et consignes affichées selon le temps du clip. Les changements d’exercice sont des coupures explicites avec pause, pas des transferts corporels ni des crossfades. Le cache shell-v8 précache le contenu ; les réponses Range vidéo restent hors Cache API. Le lab hors production `tools/coach-lab.html` échantillonne les os et les appuis skinnés ; `tests/coach-trajectories.cjs` contrôle les cycles à 60 Hz. Galerie et preuves : `docs/coach/phase2/`. Les rapports de phase 1 sont historiques ; voir le rapport phase 2 pour les limites et l’actuel SHA du modèle.

### Coach phase 3 : recherche isolée

Le GLB à huit exercices ne change pas. `assets/coach/transitions/` contient les candidates Rocketbox officielles retargetées, non référencées par le runtime ni le précache (shell-v9). Le laboratoire accepte un paramètre `transitions` pour charger les clips JSON et les jouer en one-shot. La chaîne `download-coach-transitions.py` → `coach-transition-retarget.html` → `export-coach-transitions.cjs` conserve la provenance. Les tests d’audit écrivent explicitement HOLD ; leur exécution réussie ne signifie pas une acceptation du geste. Le runtime ajoute uniquement une interpolation orbitale de caméra bornée, interrompue par interaction et désactivée en mouvement réduit. Rapports et protocole : `docs/coach/phase3/`.

### Coach phase 4 : correction de contact et admission fail-closed

`tools/coach-contact-repair.html` applique une correction IK aux jambes des deux clips source, dans des fenêtres explicites avec rampes quintiques. Le modèle et les huit clips d’exercice restent inchangés. Export séparé `assets/coach/transitions/contact-candidates.json`, identifiants uniques pour éviter l’alias d’actions AnimationMixer. Le lab suit des sommets skinnés identifiés et rétablit aussi les UUID absents dans les anciens JSON.

`coach-transition-gate.js` contient uniquement les contrats légers et l’admission (pose, orientation, vitesse, contacts, version d’asset, récupération). Aucun chemin d’exercice n’est approuvé ; la sélection conserve la coupure avec pause. Les poses complètes et les mesures sont dans `docs/coach/phase4/connection-contracts.json`, pas dans le bundle runtime. Il n’existe pas encore de lecteur de transferts/récupération activé. Le shell-v10 précache le module d’admission, pas les clips de recherche. `tests/coach-contact-audit.cjs` produit les mesures avant/après et `tests/coach-transition-gate.cjs` teste les refus. Statuts complets HOLD et NOT_AVAILABLE conservés malgré les contrôles ciblés PASS.

### Coach phase 5 : estimation vidéo et référence mocap, hors runtime

`tools/mocap/` contient les scripts de fixtures vérifiées, extraction MediaPipe CPU, retargeting directionnel, export GLB, provenance embarquée et capture comparative. `docs/coach/phase5/` conserve la source publique licenciée, les estimations brutes/filtrées, deux GLB de diagnostic et les preuves A/B/C/D. Le lecteur diagnostic accepte `once=1` pour une animation GLB non bouclée. L’optimiseur de textures accepte un chemin explicite afin de ne pas écraser l’asset coach existant. Aucun clip de recherche n’est chargé par `coach-3d.js` ni le service worker ; pas de nouvelle route admise. Les tests ML vérifient les sorties persistées sans télécharger de poids en CI, tandis que les trajectoires des GLB sont recalculées dans Chromium. Voir le rapport pour les licences vidéo, CMU et Rocketbox distinctes.
