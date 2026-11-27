# PARISFIT — Phase 4 : appuis corrigés, raccords encore bloqués

27 novembre 2026 · suite de `c391ab8` · PR #11 en brouillon. **Aucune fusion ni production.**

## Résultat et statut d’acceptation

Deux transitions Rocketbox existantes ont reçu une correction ciblée des appuis, sans remplacement du modèle ni réécriture du geste à partir de poses fixes. Le suivi de points matériels de la semelle montre une diminution mesurée de la dérive dans les fenêtres corrigées. Un contrôleur d’admission des raccords a été ajouté et testé en refus par défaut.

**Transitions activées : aucune.** Les raccords aux exercices, le retour animé vers une position stable, la revue des collisions et la validation professionnelle ne sont pas acquis. Les cinq autres passages ne sont pas réalisés ; ils restent `NOT_AVAILABLE`, avec un brief de création réaliste. Le critère final de continuité humaine entre toutes les positions n’est donc pas atteint.

- [Galerie phase 4](index.html), aussi accessible depuis la galerie phase 3.
- [Rapport des transitions](transition-report.json), quatre rapports détaillés avant/après par clip, [contrats](connection-contracts.json).
- [Complément professionnel](PRO-ADDENDUM.md), [étude des cinq manquantes](MISSING-TRANSITIONS.md).
- [Résultats des huit exercices](exercise-trajectory-report.json), [émulation mobile](mobile-emulation-report.json), [journal local](local-test-log.txt).

## 1. Correction des deux candidates

Les trajectoires source et le timing de 4,5 s sont conservés. `tools/coach-contact-repair.html` charge le GLB existant et les clips de phase 3, sélectionne un point matériel de semelle par fenêtre d’appui, puis corrige les deux segments de jambe par IK. Le pôle de genou et l’orientation monde du pied viennent de la pose source. Les longueurs de segments ne sont pas modifiées. Les corrections entrent/sortent avec une rampe quintique de 0,2 s ; les pas de repositionnement restent libres en dehors des fenêtres.

Les fenêtres sont des **hypothèses d’ingénierie à faire revoir**, pas un calendrier d’appui professionnel. Le point choisi est un sommet skinné identifié par index de mesh/vertex, pas le pivot de cheville. Le plateau est évalué hors rampes ; les transitions entre appui et mouvement ne sont pas déclarées parfaites.

| Mesure | Debout→accroupi | Accroupi→debout |
|---|---:|---:|
| Durée / poses | 4,5 s / 271 | 4,5 s / 271 |
| Plus grande dérive de point d’appui avant, sur les plateaux définis | 1,879 mm | 22,666 mm |
| Après, même point / mêmes fenêtres | <0,001 mm | <0,001 mm |
| Minimum des surfaces contrôlées | ~2 mm | ~2 mm |
| Vitesse articulaire maximale | 1,186 m/s | 1,810 m/s |
| Accélération articulaire maximale | 21,37 m/s² | 28,91 m/s² |
| Vitesse des surfaces mains/pieds maximale | 1,239 m/s | 1,889 m/s |
| Accélération des surfaces maximale | 24,58 m/s² | 30,43 m/s² |
| Variation maximale de longueur de segment | <0,0003 mm | <0,0003 mm |
| Flexion du genou maximale mesurée | 142,81° | 141,93° |
| Statut global | HOLD | HOLD |

La très petite dérive résiduelle reflète le verrouillage numérique d’un sommet choisi ; ce n’est pas une mesure de pression de la semelle ni une garantie d’équilibre. La précision géométrique ne garantit pas une amplitude adaptée à un utilisateur.

## 2. Audit 60 Hz et limites

`tests/coach-contact-audit.cjs` rééchantillonne les clips exportés : **1 084 poses** pour les deux versions des deux clips. Il contrôle les trajectoires monde des os, toutes les surfaces associées aux mains/pieds par os dominant, les points d’appui fixes, les variations de vitesse, les longueurs des segments, les angles de genou et les poses initiale/finale. Les identités de points restent constantes dans le temps.

Garde-fous choisis pour les régressions : pénétration ≤4 mm ; variation de segment <0,1 mm ; dérive du sommet suivi sur plateau <1 mm ; écart vertical d’appui sur plateau <7 mm ; accélération discrète os/surface <40 m/s². **Ce ne sont pas des normes médicales ni des seuils de validation biomécanique.** Les résultats avant sont conservés même lorsqu’ils dépassent un seuil. Les contrôles ciblés après passent ; l’acceptation du clip complet ne passe pas.

Un criblage AABB des deux pieds et des mains contre le pied opposé ne relève pas de chevauchement dans ces paires. Il ne contrôle pas les mains contre les cuisses, les vêtements, toutes les surfaces ou toutes les paires d’os. **Aucune absence exhaustive de collision visuelle n’est déclarée.** Pas de simulation des forces, centre de masse ou répartition de charge. Le bassin suit la source ; sa crédibilité dynamique reste à apprécier. Un pas d’échantillonnage de 60 Hz ne prouve pas l’absence de défaut entre deux échantillons.

## 3. Raccords : schéma explicite, admission bloquante

`connection-contracts.json` décrit pour chaque candidate : poses monde détaillées de départ/arrivée, contacts nécessaires, fenêtres d’appui, durée, vitesse, position/quaternion du bassin, orientation, hashes d’assets, interruptions et statut de récupération. Les entrées absentes portent `null` et `NOT_AVAILABLE`, pas une durée inventée.

`coach-transition-gate.js` contrôle : route approuvée, correspondance des hashes, pose complète finie avec quaternions normalisés, écart de position ≤15 mm et d’orientation ≤0,08 rad, vitesse d’entrée ≤0,03 m/s, supports requis, sortie définie et récupération approuvée. Les tests vérifient aussi qu’un quaternion et son opposé représentent la même orientation ; NaN, pose manquante, mauvais asset, mauvais support, interruption et mouvement réduit sont refusés.

Le runtime consulte l’admission **avant** la coupure existante et conserve le repli explicite en pause. Aucun clip n’est chargé ni lancé. Il s’agit du système de contrats/admission, **pas d’un lecteur de transferts activé** : la gestion animée d’une récupération et l’exécution des raccords restent à implémenter après qualification des clips.

### Pourquoi aucune activation ?

Les comparaisons portent sur les poses initiales réelles des huit exercices, sans alignement artificiel de racine ni fondu. Meilleur écart maximal d’articulation parmi ces huit poses :

| Candidate | À l’entrée | À la sortie |
|---|---:|---:|
| Debout→accroupi | 180 mm | 856 mm |
| Accroupi→debout | 768 mm | 358 mm |

Aucun raccord ne respecte la tolérance de 15 mm. Ce sont les écarts maximums sur les articulations pour la pose d’exercice la plus proche, pas les déplacements du bassin seul. Aucune recherche sur toutes les phases d’exercice n’est prétendue. Les mouvements aux extrémités et les appuis doivent également correspondre ; un mot commun comme « debout » est insuffisant.

En interruption, une pose figée n’est pas nécessairement stable. Faute de séquence de récupération approuvée, le système refuse l’admission plutôt que de promettre un retour au repos. Les scénarios du contrat définissent l’intention ; ils ne sont pas présentés comme une récupération animée déjà exécutée.

## 4. Défaut du laboratoire découvert et corrigé

Les JSON de phase 3 avaient été exportés sans UUID. `AnimationClip.parse` pouvait produire deux clips avec le même identifiant absent ; l’AnimationMixer pouvait réutiliser une action incorrecte lors d’une sélection successive. La galerie vidéo de phase 3 avait été capturée avant la suppression des UUID, mais la réexécution du laboratoire n’était pas fiable dans ce cas.

Le laboratoire attribue maintenant une identité distincte de secours ; les clips corrigés exportent des UUID déterministes uniques. Un test impose une variation de bassin négative pour la descente et positive pour la remontée, au lieu de seulement vérifier la valeur absolue. Les rapports historiques restent archivés ; `phase3-recheck-report.json` contient la nouvelle exécution. Les preuves phase 4 ont été produites **après** cette correction.

## 5. Cinq passages manquants

Inventaire du dépôt Rocketbox relu à la révision MIT figée : 471 fichiers FBX, 30 noms correspondants aux recherches crouch/sit/stand/kneel/floor/etc. Aucun nouveau clip exact n’a été importé. Le détail et les limites de cette recherche sont dans `source-inventory.json`.

- Accroupi→genoux : NOT_AVAILABLE.
- Genoux→sol : NOT_AVAILABLE ; la pose « sol » doit être définie.
- Sol→gainage : NOT_AVAILABLE ; préciser appui mains/avant-bras et départ.
- Allongé→assis : NOT_AVAILABLE.
- Assis au sol→debout : NOT_AVAILABLE ; ne pas détourner un lever de chaise.

Le brief joint propose une capture consentie et licenciée, avec stratégie choisie par un professionnel, calibration, retargeting, appuis et raccords. Aucun assemblage de poses fixes n’a été présenté comme une transition humaine. Aucun achat, aucune commande de capture et aucun avis professionnel effectués.

## 6. Preuves, galerie et revue

16 nouvelles vidéos : avant/après × deux clips × face/profil/trois-quarts/ralenti. Cycles complets de 4,5 s, ralenti à durée doublée ; images initiale **et finale** disponibles, trois angles sur chaque image. Les vidéos avant représentent la candidate phase 3, pas un autre exercice. Elles ont été entièrement décodées par FFmpeg et chargées par Chromium ; les hashes correspondent au GLB et au JSON utilisés.

Les deux planches temporelles après ont été inspectées. **Aucun visionnage professionnel continu n’est attesté.** Les contrôles numériques et la décodabilité vidéo ne remplacent pas cette revue. Le dossier professionnel existant est conservé et complété par `PRO-ADDENDUM.md`, lié depuis sa version HTML ; le PDF de phase 3 reste une archive à lire avec l’addendum.

Statuts distincts : **contrôles ciblés d’appui PASS**, **clips complets et raccords HOLD**, **cinq sources NOT_AVAILABLE**, **professionnel non validé**, **activation aucune**.

## 7. Régressions et compatibilité

- `npm test` : PASS (syntaxe, assets historiques, preuves et nouveaux tests d’admission/intégrité).
- `npm run test:browser` : PASS local : huit exercices, 2 840 poses, commandes, phases, caméra, pause, ralentis, mouvement réduit, repli/retry, hors-ligne, galeries, nouvelles trajectoires et contacts.
- Largeurs application : 320, 390, 430, 768, 1200 px. Galerie phase 4 : 320, 390, 768, 1200 px, pas de débordement horizontal détecté.
- GLB inchangé : 5 789 744 octets ; SHA256 `1fc67dc3453d6c0eae589ef3203923f52b4db303c0c9e73714e174cba5d398bb`. Huit exercices préservés ; aucune nouvelle texture ou modification anatomique.
- Cache shell-v10 / URLs 20261127-10. Module d’admission précaché ; JSON de recherche non chargés par le parcours ni précachés.
- Aucun essai « après activation » prétendu : aucune transition n’a été activée.

Émulation Chromium/WebGL logiciel 390/412 px : chargement local 3 206/587 ms ; cadence observée sur trois secondes 28,9/32,5 FPS ; heap JS ~10,3/9,7 Mo. Arrêt du rendu en pause/hors écran, restauration du contexte : PASS. Valeurs variables selon cache/serveur, **pas des performances iPhone/Android**. Aucun appareil physique disponible, aucune température/batterie/VRAM matérielle mesurée. Le [protocole matériel](../phase3/DEVICE-PROTOCOL.md) reste à exécuter.

## 8. Reproduire et prochaine étape

Serveur HTTP 3000 et Chromium : `node tools/export-coach-contact-repair.cjs`, `node tests/coach-contact-audit.cjs`. Les fichiers de phase 3 nécessaires sont persistés ; pas de téléchargement requis pour la correction. Vidéos : définir `FFMPEG_PATH`, `STAGE=before` puis `STAGE=after node tools/capture-coach-contact-repair.cjs`, puis `python tools/verify-contact-videos.py`. Rapports et tests nécessitent `npm ci`; dans ce sandbox : `CHROMIUM_PATH=/tmp/chromium`, `LD_LIBRARY_PATH=/tmp/al2023/lib`.

Priorité suivante : valider le calendrier de contacts et la stratégie de récupération avec un professionnel/animateur, acquérir les gestes manquants autorisés, construire des entrées/sorties compatibles à partir de références humaines. Ne pas activer les candidates par simple relâchement des seuils. **PR #11 reste en brouillon, aucune fusion ni production.**
