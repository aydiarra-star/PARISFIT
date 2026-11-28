# Phase 6 — calibration quaternion et appuis mesurés

**Décision : REJECTED_FOR_RUNTIME. Objectif de mouvement humain crédible avec continuité démontrée non atteint.** PR11 reste en brouillon ; aucun merge, déploiement ou mouvement activé. Le progrès technique ne vaut pas validation naturelle/professionnelle.

## Livraison

- Galerie `index.html` : source articulaire / retargetée / corrigée, 12 vidéos complètes (face, profil, trois-quarts, ralenti 0,5×), temporalité commune de 2,4 s. Pas de vidéo filmée de la source ; le squelette est explicitement étiqueté.
- `player.html` : deux GLB chargés réellement dans Three.js, lecture manuelle, pause, ralenti, recherche temporelle et caméras. Arrêt à la fin sans boucle ni blend caché.
- Deux BVH originaux, deux GLB, 145 poses à 60 Hz, matrices de correspondance/axes et trajectoires conservées.
- Rapports source, retarget, correction, contacts, comparaison, intégrité et dossier de revue professionnelle.

## Sélection et calibration reproductible

22_14 a été testé sur un cycle complet 0,1–2,9 s. Le retarget quaternion naïf sans calibration d'axes produisait des jambes repliées ; la calibration anatomique améliore les directions, mais les changements des orteils dans la source empêchent de supposer des appuis fixes. Rapport et image négative conservés. **L'image historique `rejected-22-bottom.jpg` porte par erreur l'ancien label “VIDEO ESTIMATE” ; elle est uniquement une trace de debug, pas une preuve correctement légendée. La source est optique.**

14_06, 8,6–11,0 s : plateau debout initial, squat profond, retour debout. La description primaire correspond aux squats, mais les pieds n'ont pas une fiabilité suffisante pour accepter l'ensemble du mouvement. Le retour debout n'est pas une récupération validée.

`retarget-calibrated.html` utilise la première T-pose ajoutée au BVH, mappe les articulations, aligne les axes enfant anatomiques, conserve les deltas quaternion mondiaux complets puis recalcule les rotations locales. Orientation initiale normalisée en yaw ; déplacement root multiplié par le ratio de longueur de jambe ; longueurs du modèle conservées. Sol aligné par une constante initiale, jamais projeté à chaque frame. Les axes primaires sont vérifiés, mais leur alignement ne prouve pas la calibration anatomique des torsions axiales. Pas de lissage temporel, aucun accéléré, aucun étirement des os.

## Contacts et corrections limitées

`detect-contacts.py` : hauteur du joint orteil relative à la médiane initiale, vitesse horizontale centrée à 60 Hz. Candidat stable si hauteur ≤15 mm et vitesse ≤80 mm/s ; candidat aérien si hauteur >40 mm ; sinon mobile/incertain. Ce sont des **hypothèses**, non des contacts physiques ou sauts prouvés. Gauche : 68 poses candidates stables, 73 incertaines, 4 candidates aériennes ; droite : 78 stables, 67 incertaines. Pas de vérité terrain de pression, d'occlusion ou de confiance marqueur.

Seules deux fenêtres longues initiales sont corrigées : gauche 0–0,50 s, droite 0–0,433 s ; rampes quintiques 0,15 s. Trois points de semelle distincts sont suivis par pied ; correction IK des jambes vers le barycentre horizontal et la hauteur minimale 2 mm. Rotation mondiale du pied préservée. Aucun changement du bassin, ni correction des pieds hors fenêtres. La correction ne prétend pas fixer toute la surface de semelle.

Un essai appliquant les cinq fenêtres détectées augmentait l'accélération maximale de 33,57 à **86,51 m/s²** : rejeté. Rapports et contrats conservés. La version retenue pour diagnostic ignore les fenêtres de durée <0,4 s ; ce seuil empirique est explicite, pas une règle biomécanique universelle.

## Mesures sur toute la séquence

| Mesure | Retargeté | Corrigé limité |
|---|---:|---:|
| Poses à 60 Hz | 145 | 145 |
| Vitesse articulaire max | 1,476 m/s | 1,476 m/s |
| Accélération articulaire max | 33,566 m/s² | 33,566 m/s² |
| Pénétration sol maximale | 8,59 mm | 8,59 mm |
| Écart pied-sol maximal G / D | 47,78 / 47,89 mm | 47,78 / 47,89 mm |
| Dérive horizontale max des points de semelle en appui retenu | 9,69 mm | 1,37 mm |
| Écart pose début/fin max | 186,82 mm | 186,82 mm |

La disparition de dérive du barycentre n'est **pas** la disparition de toutes les dérives ponctuelles. Le défaut global de contact persiste, parce que les phases incertaines ne sont pas forcées au sol. La source normalisée elle-même a une accélération max 32,168 m/s² et un écart début/fin 120,85 mm. Ces valeurs ne permettent pas à elles seules de distinguer bruit de capture et mouvement volontaire.

Directions de segments retargetées : erreur numérique <0,00003° par rapport aux directions source pour cuisses/mollets/pieds/bras ; après IK, déviation maximale cuisse 4,13°, mollet 3,87°. Cela vérifie la transmission géométrique, pas l'anatomie. Déplacement articulaire induit max 28,77 mm ; bassin et pieds hors fenêtres inchangés à <0,001 mm près. Les rotations du bassin, hanches, genoux, chevilles, épaules, mains et tronc sont mesurées frame par frame dans les rapports. Pas d'approbation de leur stabilité humaine.

La comparaison géométrique aux huit exercices existants reste diagnostique : meilleur écart max entrée 151,84 mm, sortie 178,21 mm. **Aucun raccord animé ni essai d'intégration** : défauts techniques préalables, collisions et récupération non approuvées. Boucle refusée.

## Validation et limites

Tests : chargement réel des GLB, séquence complète et squelette à 60 Hz, conservation des segments, invariance du bassin/hors-fenêtres, pause/ralenti/caméras/fin sans boucle, responsive 320/390/768/1200 px, décodage FFmpeg complet des 12 vidéos. Le test d'intégrité ne prétend pas tester le naturel. `npm test` et la totalité de `npm run test:browser` exécutés localement : PASS (journal `regression.log`). La CI est rapportée séparément dans la PR.

Aucun contrôle exhaustif auto-collision peau/vêtements, aucun centre de masse/forces/équilibre, aucune validation de continuité physique, aucun professionnel consulté, aucun iPhone Safari ou Android Chrome physique. Les emulations ne les remplacent pas. Ne pas utiliser comme démonstration sportive approuvée.

## Reproduction

Installer les dépendances npm et la venv phase 5 ; servir le dépôt sur le port 3000 (`python -m http.server 3000 --bind 0.0.0.0`). Définir CHROMIUM_PATH/LD_LIBRARY_PATH si le Chromium du sandbox le nécessite.

```sh
node tools/mocap/export-calibrated.cjs
.venv/bin/python tools/optimize-coach.py docs/coach/phase6/retargeted.glb
.venv/bin/python tools/mocap/detect-contacts.py
node tools/mocap/export-corrected.cjs
.venv/bin/python tools/optimize-coach.py docs/coach/phase6/corrected.glb
.venv/bin/python tools/mocap/stamp-phase6.py
node tests/coach-cmu-calibrated.cjs
node tests/coach-cmu-player.cjs
FFMPEG_PATH=$(.venv/bin/python -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())') node tools/mocap/capture-phase6.cjs
.venv/bin/python tools/mocap/verify-phase6.py
```

`CMU_TRIAL=22 node tools/mocap/export-calibrated.cjs` reproduit le candidat antérieur dans `.cache/phase6/` sans écraser le candidat courant. `ALL_WINDOWS=1 node tools/mocap/export-corrected.cjs` reproduit l'essai de contacts trop courts dans ce cache. Les JSON source/provenance historiques sont conservés. Coût externe : 0 €.
