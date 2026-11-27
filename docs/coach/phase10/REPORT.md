# Phase10 — mesure indépendante, retargeting et première capture

## Décision : REFUSÉ à l'admission

La chaîne technique fonctionne ; la fidélité biomécanique n'est pas démontrée. Ni activation, ni achat, ni fusion, ni production. Rocketbox et ses huit exercices restent inchangés. PR11 reste brouillon. CMU est un contrôle public autorisé, **pas une capture PARISFIT**.

## Ce qui a été exécuté

- Audit du nettoyage phase9 : une seule action `phase9-cmu-control`, source orpheline toujours absente ;80os,22correspondances,145poses à60Hz,2,4s issus de CMU14_06 entre8,6s et11s. Le BVH est à environ120Hz (Frame Time0,0083333).
- Nouveau validateur Python standard, sans Blender/Three.js/NumPy : lit une géométrie prélevée **avant export**, contrôle les données puis mesure le cycle complet. L'indépendance est algorithmique, pas une seconde mesure physique du sujet.
- Échantillonneur Blender séparé : positions/rotations mondiales, parents, minima de peau skinnée et trois marqueurs fixes par pied/main. Contrairement aux pivots osseux, il observe effectivement la peau ; les marqueurs ne sont pas encore des patches anatomiques approuvés.
- Deux exports répétés de chaque variante et contrôle des hashes ; vérification Three.js sur145poses ; films complets face/profil/trois-quarts et ralenti trois-quarts, avant/après (8films). Décodeur vidéo vérifie durée/frames, **pas** la qualité visuelle.
-22tests unitaires indépendants et7tests par mutation des données réellement générées : ordre des articulations, données manquantes/corrompues, unités incompatibles, animations vides/source indésirable, GLB tronqué/accessor incomplet, non-finis/rotations/temps et désaccord des positions. Ces contrats sont volontairement limités à cette fixture, pas un validateur universel BVH/glTF.

## Avant/après : hypothèse de sol rejetée

Avant = pipeline nettoyé phase9, hash reproductible `fac4d26f57590f99951058c2532d6a96c4195cd8d39fbb797b35b19e3fcb7e7e`.

Après = unique translation verticale constante, calculée pour placer le point le plus bas des groupes de pieds à2mm au-dessus du sol sur la première pose. Translation−3,2533916mm. Aucun IK, lissage, changement de durée, projection frame par frame ou verrouillage des appuis. Maximum d'écart des composantes quaternion0 ; déviation par rapport à une translation constante<0,000069mm.

**La pénétration maximale empire :277,957mm →281,211mm.** Donc ne pas retenir cette hypothèse comme « correction réussie ». Elle démontre qu'un alignement initial ne résout pas le défaut dynamique. Avant ET après restent REFUSÉS. `comparison-report.json` est la mesure exacte.

## Morphologie et orientation : problèmes identifiés, pas masqués

Conversion BVH0,056444 en mètres, axes import−Z/Y puis coordonnées du rapport Y-up, conversion depuis Blender Z-up. Facteur scalaire de déplacement racine0,9469891624 calculé à partir de la jambe gauche ; les proportions du rig Rocketbox restent fixes. Pose source frame0 artificielle, cible rest-pose ; orientation latérale initiale alignée ; rotations relatives source et offsets directionnels puis FK hiérarchique, sans contrainte anatomique.

`morphology-report.json` montre que ce facteur ne résout pas la morphologie : écart pied→orteil environ+52mm, avant-bras gauche+84,7mm et droit+76,3mm après normalisation. Les segments source Hips→LowerBack et Spine1→Neck ont longueur nulle, alors que leurs correspondants cible ont environ120/200mm. **Ce sont des divergences de conventions squelettiques, pas des mesures corporelles comparables.** La normalisation directionnelle de ces segments est non qualifiée. Les appels Blender ne plantent pas, ce qui n'est pas une preuve d'orientation correcte.

Ne pas amplifier/redistribuer les rotations ou allonger les membres arbitrairement. La calibration segmentaire anatomique, contraintes articulaires, retarget avec contacts vérifiés, pelvis/chaîne jambes/mains et raccords reste **NON TESTÉE** comme amélioration ; cette phase n'a qualifié aucune telle solution. Les coordonnées source normalisées sont conservées dans l'artifact pour une prochaine comparaison de trajectoires, mais ne constituent pas encore une métrique anatomique de fidélité.

## Limites / critères d'arrêt

COM heuristique et enveloppe des pieds supposés en contact ; pas de forces ni COM mesuré. Flexion non signée, torsion anatomique NON TESTÉE. Sphères de collision éparses, pas détection exhaustive des intersections. Aucun seuil physiologique clinique inventé. Aucun test sur appareils physiques ni professionnel disponible. Les raccords vers les huit exercices ne sont ni générés ni admis.

Les films sont exportés pour inspection humaine ; aucune approbation visuelle n'est revendiquée. L'examen professionnel de la variante de squat et des consignes reste obligatoire. Voir [fiche des critères](CRITERIA.md), [capture et droits](CAPTURE-AND-RIGHTS.md).

## Historique négatif conservé

Run46050854258 : le nouvel échantillonneur incluait des objets non skinnés, minimum−1m parasite. Résultat invalidé, conservé dans `first-run-unqualified/`. La correction du système de mesure exclut désormais les objets sans modificateur de l'armature cible ; la liste des inclus/exclus est dans chaque rapport. Ce n'est pas une correction de mouvement.

Run46051456625 : géométrie corrigée, tests passés, mais annotations GitHub longues tronquées et échappements Unicode JSON altérés. Enveloppe conservée dans `second-run-transport/`. Les rapports finaux utilisent des fragments base64 et vérification JSON + SHA256 : ne pas interpréter les copies tronquées comme résultats validés.

## Reproduire sans services privés

Ubuntu24.04 : installer Blender natif, python3-numpy/requests et ffmpeg (voir workflow), `npm ci`, `npx playwright install --with-deps chromium`.

```sh
python tools/biomechanics/test_contracts.py
blender --background --factory-startup --python-exit-code 1 --python tools/biomechanics/export.py
python tools/biomechanics/test_generated.py
# lancer le serveur HTTP dans un terminal séparé
python -m http.server 3000 --bind 0.0.0.0
# puis dans l'autre terminal
node tools/biomechanics/check.cjs
FFMPEG_PATH=$(command -v ffmpeg) node tools/biomechanics/capture.cjs
python tools/biomechanics/verify-videos.py
python tools/biomechanics/build-gallery.py
```

Sortie `.cache/phase10/`, isolée et ignorée par Git. `index.html` dans l'artifact lit les8vidéos et propose les2GLB. Les licenses Rocketbox MIT et notice CMU sont incluses. Le script d'export refuse un autre répertoire et vérifie les hashes des entrées ; aucun chemin vers une vidéo privée. Un rapport REFUSÉ n'est exporté que comme diagnostic explicitement non admis ; le validateur ne corrige aucune donnée et ne peut produire d'approbation professionnelle.

Les gros fichiers de contrôle restent dans l'artifact GitHub `phase10-control-review` (rétention30jours) ; le proxy réseau de cet environnement ne permet pas de rapatrier ces binaires. **Le dépôt contient les rapports vérifiables, pas des faux liens locaux vers des vidéos absentes.** Télécharger l'artifact depuis le run lié dans `evidence.json`, extraire et ouvrir son `index.html`. Régénérer avant expiration pour archivage durable privé des preuves.

### Signaux géométriques supplémentaires

Inclinaison Pelvis→Neck mesurée113,70–126,46° par rapport à la verticale ; c'est une anomalie majeure à examiner, pas une posture de squat admise. Les angles hanches sont des proxies dégradés par les correspondances de pivots. Dérive maximale sur fenêtres candidates5,798mm, gap pied maximal56,969mm (avant), mais peu de frames remplissent la définition de contact : ne pas conclure à des appuis valides. Écart entrée/sortie maximum178,403mm : aucun raccord naturel n'est revendiqué. Le pic d'accélération34,031m/s² dépasse le budget20 et reste identique après la translation constante.

Run46052018457 : tous les calculs/tests/films réussissent, mais GitHub limite les avertissements par étape et seules certaines parties des annotations arrivent. Le transport final compresse les JSON avec zlib avant base64 pour rester sous cette limite. Cela ne modifie pas les calculs.
