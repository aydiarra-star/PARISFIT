# Phase 9 — Blender débloqué en CI, qualification humaine encore ouverte

## Ce qui est acquis

Le job `blender-control` a réellement démarré **Blender4.0.2 natif sous Ubuntu24.04**, importé Rocketbox (80os), importé le BVH CMU (31os), calibré/mappé22 articulations, retargeté145 poses à60Hz et exporté un GLB. Three.js a réellement chargé et parcouru le contrôle de2,4s. Première exécution complète : [run46047904401](https://github.com/aydiarra-star/PARISFIT/actions/runs/46047904401). Versions mesurées : Python embarqué3.12.3, NumPy1.26.4, glibc2.39. Rapports de cette première réussite conservés sous `first-export-*`.

**Ce qui n'est pas acquis :** qualité sportive, fidélité à une nouvelle vidéo, correction des contacts, capture dédiée, validation professionnelle ou appareils physiques. Le sandbox Arena local reste sans les bibliothèques manquantes ; c'est **la CI** qui constitue l'environnement Blender opérationnel testé. Ne pas généraliser ce résultat à Docker ou bpy4.2, qui n'ont pas passé le test.

## Vérification renforcée réussie

[Run46048502964](https://github.com/aydiarra-star/PARISFIT/actions/runs/46048502964), commit `6fb5e45` : un seul clip de2,400000095s, 80os, 145poses ; **écart max Blender→Three.js 0,000926mm**, erreur longueur0,000214mm. GLB4 961 852octets, SHA256 `fac4d26f57590f99951058c2532d6a96c4195cd8d39fbb797b35b19e3fcb7e7e`. Régressions historiques et job Blender PASS. Ces mesures prouvent la conservation des pivots dans l’export, pas la fidélité anatomique ni l’absence de déformations de peau. Défaut sol inchangé, admission BLOCKED. Rapports et empreintes liés au run dans `evidence.json`.

## Pipeline livré

`tools/blender-pipeline/retarget.py` → import glTF → retrait des anciennes actions dans la scène de travail → import BVH → calibration T-pose et axes enfants → rotation complète relative au repos → normalisation translation root par ratio de jambe → bake FK → export GLB isolé → `check.cjs` Three.js.

Points explicités : système Blender Z-up, conversion GLB Y-up, armature `Bip01` distincte de l'os racine `Bip01_Pelvis`, source120,00048Hz déclarés par Frame Time, échantillonnage60Hz sans changement de durée. Quaternions unitaires et signes continus ; rig cible non redimensionné ; calibration d'un axe enfant **ne prouve pas** une base anatomique complète en torsion. Les doigts non mappés conservent le repos. Importeur BVH signale des os de longueur nulle (Spine1, mains) et les traite ; c'est une limite de la conversion source à examiner avant production, pas un détail effacé.

Pas d'IK, lissage ou correction de sol. Le rapport Three.js de la première réussite révèle **minSupportY ≈ −0,278m** : défaut majeur, volontairement non projeté au sol pour rendre les tests verts. Le pipeline ne prétend pas corriger ou accepter ce mouvement. La conservation des segments (<0,001mm d'erreur numérique) et les positions finies sont des contrôles de transport, pas des preuves d'appuis.

La première exportation contenait une action source orpheline en plus du contrôle : ce défaut d'export est conservé dans les rapports initiaux. Le script supprime désormais les actions inutilisées et exige un seul clip. Le contrôle renforcé compare aussi les positions Blender→Three.js sur toutes les poses (budget numérique0,2mm), sans confondre cette fidélité d'export avec la fidélité à un humain.

## Échecs conservés / résolution

1. Phase8 : bpy local bloqué par huit bibliothèques (rapport antérieur intact).
2. Run46046334582 : bpy4.2 installé en CI, sortie139 ; environnement non qualifié, cause de crash non isolée.
3. Run46046839375 : Blender natif démarre ; import glTF échoue NumPy introuvable. `rejected-native-missing-numpy.json`.
4. Run46047328754 : NumPy corrigé ; imports réels réussis ; erreur de mapping racine armature/os. `rejected-root-mapping.json`.
5. Run46047904401 : chaîne complète et contrôle Three.js passent, contacts refusés ; rapports conservés.

Voir `ENVIRONMENTS.md` et scripts install/run pour dépendances et commandes. La CI sauvegarde GLB, données articulaires de référence, rapports, journal, inventaires et images start/bottom/end dans **phase9-blender-control**, rétention30 jours. Aucune vidéo humaine personnelle ne doit aller dans cet artefact public. Les téléchargements de logs/artefacts redirigent vers des hôtes inaccessibles depuis Arena ; les rapports ont été récupérés via l'API des annotations de checks, sans fabriquer les fichiers binaires. Le GLB est accessible à l'utilisateur dans l'artefact GitHub, pas copié artificiellement dans le dépôt.

## Préparation de la capture

- `CAPTURE-QUICKSTART.md` : face/profil simultanés, cadrage des pieds/mains, métrique, calibration, événements visuels début/fin, calcul d'offset/dérive, deux à trois prises séparées avec repos adapté, alternative monoculaire clairement limitée.
- `PRIVACY-AND-INPUT.md` : droits par opération, partage externe nommé, aucun secret/signature/identité dans la PR. Préflight phase8 conservé et renforcé par vérification `local-analysis`.
- `SQUAT-ACCEPTANCE.md` : phases et décisions technique/fidélité/visuel/pédagogie préétablies ; pas d'admission automatique.
- `PROVENANCE.md` : contrôle CMU licencié + Rocketbox MIT, pas de source inventée.

## Obstacles encore ouverts

Capture autorisée absente ; calibration multi-vues et reconstruction d'une nouvelle vidéo non exécutées ; adaptation d'une nouvelle hiérarchie BVH non qualifiée ; bases anatomiques axiales et contacts/skin/collisions non validés ; revue professionnelle et appareils physiques absents. **Ce livrable débloque le segment BVH→Blender→Rocketbox→GLB→Three.js, pas encore la chaîne universelle vidéo→coach premium.** Un nouveau BVH doit être qualifié, pas injecté dans la CI publique en changeant arbitrairement le hash.

Aucun achat/souscription, activation, fusion ou déploiement. Les huit exercices et tous les dossiers précédents sont conservés. PR11 reste en brouillon. Résultats des relances finales et contrôles additionnels : voir commentaires PR et rapports `blender-report.json` / `three-report.json`.
