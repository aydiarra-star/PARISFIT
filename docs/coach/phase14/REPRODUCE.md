# Reproduction — périmètres distincts

## Acquisition originale (réseau requis)

```
python3 tools/model-qualification/acquire.py
```

NumPy requis, gh configuré pour lire le dépôt public amont. JobCI `model-qualification` dans `.github/workflows/validate.yml`. Archive limitée à150Mo, SHA256 vérifié avant lecture, archive supprimée même sur échec. SeulsS01 et les métadonnées publiques sont analysés ; les autres lignes de participants ne sont ni publiées ni exportées. Le ZIP n’est pas décompressé sur disque. Le modèle n’est pas redistribué.

Archive v1 immuable épinglée ; README et modèle également vérifiés. `participants.csv` est authentifié par le hash du ZIP, puis son hash propre est consigné. Le commit amont et son fichier sont épinglés indépendamment. Le manifeste permet de contrôler le périmètre documentaire. Les feuilles XML sont comparées sans le nom racine du modèle, mais avec les noms des composants ; comparaison textuelle, pas équivalence biomécanique. Le transport conserve le nombre et le hash du diff complet, les40premières différences et jusqu’à60différences de wrapping : échantillons explicitement tronqués, pas un patch exhaustif.

## Récupérer la preuveCI

```
python3 tools/model-qualification/collect.py RUN CHECK COMMIT
```

Identifiants exacts dans `evidence.json`. JSON compresséZlib/Base64 transporté dans des annotationsCI ; validation de segments contigus et hash. Artefact `phase14-model-qualification`,30jours. Un échec de transport n’autorise pas à fabriquer les paramètresS01.

## Construire et tester

```
python3 tools/model-qualification/build.py
python3 tools/model-qualification/test_contracts.py
node tests/coach-model-qualification.cjs
python3 tools/model-qualification/compare_opencap.py # réseau GitHub, optionnel pour refaire la comparaison amont
```

`build.py` produit les37lignes détaillées, matrice37×66, inventaire inverse66, décision et page. Les règles sémantiques sont **manuelles et versionnées dans ce script**, non apprises ou sélectionnées par proximité. Aucun «meilleur score» ne transforme une paire plausible en paire confirmée. Toutes les coordonnées théoriques proviennent du XML génériquePhase13 épinglé. Elles ne sont ni redimensionnées ni appliquées au sujet.

Tests de transformation uniquement synthétiques : réversibilité des points/forces/moments, distances, translation du moment, rejet des réflexions et changements d’échelle ; refus de provenance manquante. La porteIK exige une source documentaire pour chaque paire et les repères/scaling qualifiés. Le script ne contient aucun solveurIK.

Les testsNode vérifient matrices, métadonnées, refus, paramètres récupérés, hash des preuves et hashRocketbox. Tests navigateur : liens locaux, contenu et absence de débordement à320/390/768/1200px. Pas de testbiomécanique ou de téléphone physique. Aucune vidéo nouvelle requise pour cet audit documentaire ; les vidéosdiagnostiquesPhase13 sont conservées.

**Statuts :** calculs et transport VALIDÉS dans leur périmètre ; anatomie EN ATTENTE DE VALIDATION HUMAINE ; IK NON TESTÉE ; utilisation actuelle REFUSÉE. PR11 brouillon, runtime préservé.
