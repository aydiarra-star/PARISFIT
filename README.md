# PARISFIT

**MOVE. GROW. LIVE.**  
*Ton corps. Ton esprit. Ta progression.*

Compagnon numérique dédié au sport, au fitness, à la nutrition, au bien-être mental, aux habitudes et à l'équilibre personnel.

## Références officielles
- [Cahier des charges](CAHIER_DES_CHARGES.md)
- [Prompt maître](PROMPT_MAITRE.md)
- [Architecture initiale](ARCHITECTURE.md)
- [Feuille de route](ROADMAP.md)

## Lancer
Ouvrir `index.html` pour voir l'interface. Pour tester l'installation PWA et le cache hors ligne, servir le dossier via HTTP(S) : les service workers ne fonctionnent pas en ouverture locale `file://`.

## Premier incrément
Interface responsive Aujourd'hui / Switch / Nutrition / Mental, navigation mobile et desktop, habitudes, hydratation, ressenti et journal enregistrés localement, parcours de respiration, manifeste installable et cache applicatif initial.

Backend, synchronisation, comptes, IA, bibliothèque sportive professionnelle, coach 3D, paiements et intégrations santé restent à construire.

L'interface PARISFIT validée reste la référence ; les fonctions nouvelles doivent s'y intégrer sans refonte arbitraire.

## Vérification de l’interface
Le site reste sans dépendances d’exécution ni étape de compilation. Un test navigateur est fourni dans `tests/smoke.cjs` :

```sh
# Terminal 1
python -m http.server 3000 --bind 0.0.0.0
# Terminal 2 — outils de test uniquement
npm install --no-save --package-lock=false @playwright/test
npx playwright install chromium
node tests/smoke.cjs
```

Le test vérifie six largeurs (320–1440 px), la persistance de l’eau, le ressenti, la lecture, l’ajout d’une habitude, le Coach et le rechargement hors ligne. `BASE_URL` et `CHROMIUM_PATH` permettent d’utiliser un serveur ou un navigateur existant.

Les valeurs de vitalité sont des exemples explicitement signalés, isolés dans `demo-data.js`. Les photos illustratives de l’accueil sont générées par IA.

## Coach humain 3D — expérimental, non validé pour production
Le modèle géométrique a été remplacé par **Microsoft Rocketbox Sports_Male_04**, maillage humain texturé sous licence MIT avec 80 os et huit clips squelettiques. Three.js, le GLB et ses textures sont locaux. Lecture/pause, ralenti, étapes, timeline, zoom et vues face/profil/trois-quarts sont opérationnels.

**Les mouvements sont créés ici, pas issus de motion capture ni approuvés par un professionnel.** La qualité premium, les contacts au sol, les transitions et les tests sur téléphones réels restent à valider. Ce chantier ne doit pas être fusionné tant que ces critères ne passent pas.

Voir le [rapport complet et les captures réelles](docs/coach/REPORT.md) et la [provenance du modèle](assets/coach/source.json).

### Tests reproductibles
```sh
npm ci
npx playwright install --with-deps chromium
npm test
# Avec le serveur HTTP déjà lancé sur le port 3000 :
npm run test:browser
```
`CHROMIUM_PATH` permet de fournir un navigateur existant. Aucun npm ni téléchargement externe n’est nécessaire pour exécuter le site déployé ; ces dépendances servent aux tests et à la conversion.

### Recréer le GLB (outillage, pas compilation du site)
```sh
python -m venv .venv
.venv/bin/pip install pillow
.venv/bin/python tools/download-coach.py
# Serveur HTTP sur 3000, npm ci et Chromium disponibles :
node tools/export-coach.cjs
.venv/bin/python tools/optimize-coach.py
npm test
```
Le téléchargement source utilise `gh` et une révision Rocketbox figée. Le FBX et les TGA restent dans `.cache/`, jamais dans Git. Pour recréer les planches et miniatures après les tests navigateur : `.venv/bin/python tools/review-contact-sheet.py`.

## Coach — perfectionnement phase 2 (PR #11, brouillon)

Huit clips Rocketbox corrigés, consignes synchronisées et 64 vidéos avant/après : [rapport actuel](docs/coach/phase2/REPORT.md), [galerie](docs/coach/phase2/index.html). `npm test` et `npm run test:browser` couvrent également trajectoires à 60 Hz, preuves vidéo et émulation mobile. Animations IK, **pas de mocap ni de validation professionnelle**. Transferts debout/sol naturels et tests iPhone/Android physiques restent à faire. Pas de fusion ni déploiement autorisés pour cette phase. Les anciens chiffres du dossier coach correspondent à la phase 1.
