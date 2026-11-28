# Rapport des tests — Phase24

## Reproduction

```sh
npm ci
python3 tools/animation-lock/build_public.py
python3 tools/animation-lock/test_static.py
npm test
python3 -m http.server 3000 --bind 0.0.0.0 --directory .cache/public
# Dans un autre terminal, Chromium installé :
npm run test:browser
```

Dans le sandbox : `LD_LIBRARY_PATH=/tmp/al2023/lib CHROMIUM_PATH=/tmp/chromium npm run test:browser`. La migration utilise un serveur de test local 3013 et la base historique `fc51383` présente dans Git.

## Résultats locaux

- `npm test` : **PASS**, syntaxe, contrats historiques, huit clips et hash inchangés, registre fail-closed, invalidation de hash, conservation de la base.
- `test_static.py` : **PASS**, attributs de mesh, indices, poids, matrices, nodes et quatre textures identiques au source.
- `tests/smoke.cjs` : **PASS**, six largeurs, eau et énergie persistantes, lecture, défi/habitude, Coach et shell hors ligne.
- `coach-animation-lock-browser.cjs` : **PASS**, huit exercices, contrôles, clavier, texte, articulations immobiles, caméra/zoom, quatre largeurs, URL/localStorage, historique, arrière-plan, séances, ressources directes et hors ligne.
- `coach-animation-lock-migration.cjs` : **PASS**, vrai ancien worker et GLB dans son cache, mise à jour v24, rechargement actif, conservation des données/caches étrangers, suppression des anciens caches, refus direct hors ligne/Range/encodage, registre manquant ou malformé, injection du fichier animé refusée.
- 901 fichiers suivis de la base : **892 identiques, neuf modifications autorisées**. Tous les anciens dossiers de preuves, `coach-content.js`, GLB et textures originaux inchangés.

Les deux tests historiques de préservation Phase17/18 délèguent désormais leur comparaison à une liste explicite de neuf exceptions de runtime/publication/tests. Aucun ancien manifeste ni rapport n'est régénéré. `phase24-preservation.cjs` vérifie séparément toute la base fc51383. Les assertions scientifiques historiques restent actives. Les anciens logs « tous fichiers inchangés » imprimés par ces scripts décrivent leur phase historique ; le nombre exact actuel est celui de Phase24.

La suite publique CI sert désormais le paquet autorisé, non la racine. Les anciennes suites qui supposent une lecture animée sont conservées sous `test:browser:legacy-internal`, **non exécutées ici** : elles ne sont plus un critère public valide et certaines écrivent d'anciens rapports. Les preuves scientifiques ne doivent pas être régénérées par la CI publique.

## Échecs conservés et corrections

Premier `npm test` : assertion historique sur le workflow Pages modifié ; résolu par exceptions explicites, sans modifier la preuve historique. Premier smoke interrompu par timeout pendant les travaux de migration ; ne pas le compter PASS. Les sorties finales sont archivées.

Deux premiers essais de migration échoués : fichiers `migration-first-failure.txt` et `migration-second-failure.txt`. Correction produit : ne pas attendre `client.navigate()` dans l'activation. Correction de synchronisation du test : attendre l'événement `load` du nouveau document avant interactions. Le test final complet passe avec les mêmes exigences de purge, données et verrouillage. Pas de prétention à une couverture exhaustive de tous les moteurs de PWA.

Aucune validation sur iPhone Safari ou Android Chrome physiques, aucune validation biomécanique. Pas de nouvelles vidéos de mouvement : aucune animation ne joue dans cette version publique ; les trajectoires et vidéos historiques restent intactes et ne deviennent pas des preuves professionnelles. Ce rapport ne prétend pas à un résultat CI distant ni à un déploiement.
