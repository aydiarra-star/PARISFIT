# Reproduction de l’audit passif

Depuis la racine PARISFIT, sur la branche courante. Ne jamais lancer les scripts MATLAB acquis.

```sh
python tools/passive-qualification/acquire.py
.venv/bin/python tools/passive-qualification/analyze.py
python tools/passive-qualification/mapping.py
python tools/passive-qualification/evidence.py
.venv/bin/python tools/passive-qualification/static_diagram.py
python tools/passive-qualification/build.py
.venv/bin/python tools/passive-qualification/test_metrics.py
npm test
```

Acquisition : `gh api`, dépôt public et commit épinglé ; SHA1 Git blob et SHA256 vérifiés ; budget de téléchargement inférieur à15Mo ; exactement deux C3D. Le cache `.cache/phase17/source` est ignoré parGit et peut être supprimé sans perdre les preuves résumées. Aucun identifiant privé ni dépendance à une session MATLAB.

Analyse : Python3.11, NumPy1.26.4 et python-c3d0.6.0 déjà présents dans l’environnement de travail. Aucune nouvelle dépendance de l’application. La lecture C3D se fait avec `check_nan=False` pour ne pas substituer de coordonnées ; les conversions analogiques sont celles encodées parGEN_SCALE/SCALE/OFFSET. Pas de filtre, registration ou solver. Les avertissements manquantsDESCRIPTIONS etEOF sont conservés dansJSON.

Un contrôle indépendant des blocs flottants compare **toutes** les coordonnéesXYZ et valeurs analogiques décodées avec le lecteur. La taille des octets correspond àPOINT:FRAMES, pas à la borneinclusive de l’en-tête. Ce contrôle utilise encore les métadonnées du même lecteur : **ce n’est pas un second lecteur général C3D indépendant**, et il ne résout pas l’origine de la discordance. Aucune frame supprimée volontairement ou ajoutée.

La projection des pieds est une opération descriptive en repèreC3D original, pas une correction des trajectoires. `test_metrics.py` vérifie notamment qu’un point projeté dans uneplate mais3m au-dessus ne vaut pas contact. Aucun test n’accorde une admissionanatomique.

La carte anatomique est construite depuis des définitions éditoriales sourcées dans `mapping.py` et les rattachementsXML extraits. Les 13casplausibles sont explicites ; les champscentrearticulaire etRocketbox restent inconnus. Le schéma mesuré représente seulement la première frame statique existante, sans moyenne ni nouvel avatar.

Les extraits conservent les numéros des lignes originales. Les rapportsMarkdown sont une synthèse éditoriale, pas une sortie automatique de solveur. Le scriptbuild produit la page autonome et un manifeste d’intégrité. `protected-baseline.json` consigne les hashes des fichiers préexistants protégés au début de phase, hors seuls fichiers de tests/configuration autorisés à être étendus.

Pour le navigateur : servir le dépôt à0.0.0.0:3000 avec le serveurstatique habituel, puis :

```sh
node tests/coach-passive-qualification-browser.cjs
python tools/passive-qualification/build.py
node tests/coach-passive-qualification.cjs
```

Dans cet environnement, Chromium utilise `CHROMIUM_PATH=/tmp/chromium` et `LD_LIBRARY_PATH=/tmp/al2023/lib`. Tests320/390/768/1200px, documents dépliés et liens locaux ; pas de simulation revendiquée des capteurs ni de validation sur téléphone physique. Le rapportCI et le commit final sont indiqués dans le compte rendu et laPR11, qui doit rester en brouillon.
