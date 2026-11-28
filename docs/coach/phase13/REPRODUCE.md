# Reproduire sans toucher au coach

## Acquisition et calculs complets

Python3, NumPy, Pillow, ffmpeg. Depuis la racine :

```
python3 tools/michaud/acquire.py
python3 tools/michaud/test_core.py
python3 tools/michaud/analyze.py
python3 tools/michaud/render.py
```

Le téléchargement vérifie archive et cinq membres SHA256 ; extraction limitée, archive supprimée même sur échec. Aucune désactivation TLS. Environnement CI dans `.github/workflows/validate.yml`, job `michaud-qualification`. Artefact30jours `phase13-michaud-qualification` : CSV sélectionnés, rapports, trajectoires complètes des hypothèses et rendus. Modèle tiers seulement dans cache privé de travail distinct, pas dans artifact ni Git.

Un environnement séparé teste `model_probe.py` avec OpenSim4.6 wheel LinuxCPython3.12 épinglé par SHA256 + NumPy2.1.3. Il charge/initie le modèle, constate le schéma et la gravitéY−. Il ne fait pas de scaling/IK et ne transforme pas les donnéesZ-up automatiquement. Le runtime de l'application n'importe rien de ces dépendances.

## Récupération de preuves

```
python3 tools/michaud/collect.py RUN_ID CHECK_ID COMMIT_SHA
```

Les identifiants réels sont consignés dans `evidence.json`. AnnotationsCI publiques : JSON compresséZlib/Base64 avec segments numérotés contigus ; décodage strict, rapports requis et SHA256 enregistrés. Cela évite les erreurs de téléchargement binaires d'artefacts rencontrées dans cet environnement. Ce transport n'est pas une validation scientifique.

## Rendus locaux légers

Copier `review-data.json` dans un répertoire temporaire puis :

```
python3 tools/michaud/render.py REPERTOIRE_TEMPORAIRE
python3 tools/michaud/filter_sensitivity.py
python3 tools/michaud/build_docs.py
```

Les MP4/PNG sont copiés dans `previews/`, le rapport de décodage dans `local-render-report.json`. Chaque MP4 contient150frames100Hz ; player×0,25 sans modification des données. Le rendu utilise les données d'affichage arrondies à6décimales ; les rapportsCI utilisent les CSV d'origine. Ne pas écraser la page principale par la page temporaire de rendu.

```
npm test
python3 tools/michaud/test_core.py
node tests/coach-michaud-browser.cjs
```

Le dernier test suppose un serveur statique sur port3000, peut utiliser `CHROMIUM_PATH`, produit `browser-report.json` : vues320/390/768/1200px, liens et vraie progression de lecture des3MP4, bouton ralenti. Pas une revue visuelle complète. Tests mathématiques : angles dégénérés, Kabsch sans réflexion, translation/rotation, colinéarité, dérivées, longueur imposée, conservation des directions et absence de mutation.

**NON TESTÉ :** iPhone/Android physiques, revue professionnelle, centres articulaires, IK individualisée, retargetRocketbox. Leur validation ne découle ni du statut vertCI ni d'une vidéo décodable.
