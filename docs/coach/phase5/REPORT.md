# PARISFIT — Phase 5 : chaîne vidéo réelle exécutée, qualité non acceptée

27 novembre 2026 · suite de `52d9031` · PR #11 toujours en brouillon. **Aucune fusion ni production.**

## Conclusion stratégique

Un prototype local reproductible a effectivement traité une vidéo humaine licenciée, estimé les articulations, filtré leurs trajectoires, retargeté une descente debout→accroupi sur Rocketbox, exporté un GLB et rendu ce GLB dans le lecteur diagnostic Three.js du coach. Une deuxième référence issue d’une véritable capture optique CMU a été acquise légalement et retargetée pour comparaison.

**Preuve de faisabilité de la chaîne : obtenue. Transfert propre, naturel et prêt à l’emploi : non démontré.** Le résultat vidéo C est rejeté pour le parcours ; la référence mocap D reste HOLD. Aucune des deux n’est chargée par le coach de production, aucune transition n’est activée et aucune méthode n’est déclarée gagnante sur la seule base de sa provenance.

- [Galerie A/B/C/D, source et overlay](index.html).
- [Étude des solutions](SOLUTIONS.md), [droits et attribution](ATTRIBUTION.md), [provenance machine](provenance.json).
- [Mesures identiques à 60 Hz](comparison-report.json), [empreintes et intervalles](comparison-manifest.json), [intégrité](evidence-report.json).
- [Protocole d’autorisation d’une future capture](CONSENT-TEMPLATE.md).

## 1. Vidéo réelle et droits

**FitnessScape, « Squat — exercise demonstration video »**, source primaire Wikimedia Commons, licence CC BY 3.0 vérifiée sur sa page. Le fichier de 7,1 s / 213 images à 30 Hz est obtenu par un miroir GitHub autorisé par le réseau du sandbox, avec SHA Git vérifié et SHA256 correspondant à la notice du miroir. Aucun média personnel n’a été envoyé à un service externe.

Il s’agit d’un **squat avec barre filmé de trois-quarts arrière**, pas d’un transfert sans matériel tourné pour PARISFIT. Les pieds sont partiellement hors champ. Ces défauts rendent cette source inadéquate comme démonstration finale ; ils sont conservés dans l’essai, pas masqués. La licence autorise le partage/adaptation avec attribution, mais ne vaut pas autorisation personnelle du sujet pour une publicité PARISFIT. Aucune telle autorisation n’est revendiquée. Le média et ses adaptations restent dans le dossier de recherche, crédités et sans endossement implicite.

Source, licence, auteur, modifications, conditions CMU, notices Rocketbox et empreintes sont dans `ATTRIBUTION.md` / `provenance.json`. Les GLB portent également la provenance et le statut non approuvé dans `asset.extras`. Frais externes : **0 €**, aucun crédit payant ni abonnement consommé.

## 2. Prototype C réellement exécuté

| Étape | Réalisation / preuve |
|---|---|
| Acquisition légale | `source.webm`, SHA256 `2440985661c3533a4ce78472b0f4577dbdf023aff3f8f9a225bbb5ff8071b1e9` |
| Détection | MediaPipe **0.10.21**, modèle Pose Full embarqué ; CPU local, backend TFLite/XNNPACK ; 213 détections / 213 images |
| Trajectoires | 33 landmarks image et « world » estimés par image, avec visibilité, dans `pose-estimates.json` |
| Filtrage | Moyenne centrée de cinq images sur les coordonnées, après le suivi MediaPipe. Filtrage hors-ligne, pas un modèle physique ; peut atténuer/décaler des détails temporels |
| Choix d’une seule descente | Images 24 à 75 incluses, vidéo **0,8–2,5 s**, durée 1,7 s, 52 poses source. Aucun autre transfert produit depuis cette vidéo |
| Reconstruction | Directions hip→knee→ankle, shoulder→elbow→wrist, tronc et tête ; racine latérale/verticale estimée depuis l’image avec une échelle anthropométrique approximative |
| Retargeting | Longueurs Rocketbox conservées, rotation horizontale de calibration depuis les hanches, rotations monde, doigts non estimés ; détails dans `tools/mocap/retarget-video.html` |
| Correction limitée | Recalage vertical global du minimum de maillage à ~2 mm ; ne verrouille pas chaque pied et ne prouve pas un contact réel |
| Export | `video-prototype.glb`, un clip `video-stand-to-crouch`, statut `REJECTED_FOR_RUNTIME` |
| Lecture | GLTFLoader/Three.js dans `tools/coach-lab.html`, mêmes caméras/lumières que les autres méthodes ; pas d’intégration au parcours |

L’extraction et l’encodage annoté ont pris ~6,56 s sur cette machine lors de l’exécution consignée. Ce n’est pas un benchmark de mobile ni une garantie de cadence temps réel. OpenCV GUI ne pouvait pas charger `libGL.so.1` dans le sandbox ; les bindings headless ont permis l’exécution CPU. La procédure reproduit ce choix et les versions sont conservées.

### Pourquoi le prototype C est rejeté

- Pour **52/52 images de l’extrait**, au moins un landmark de pied estimé est hors des limites de l’image. MediaPipe extrapole : détection et visibilité ne sont pas vérité terrain.
- La racine « world » MediaPipe est relative au bassin ; **aucune profondeur globale calibrée n’est mesurée**. La projection depuis l’image n’est qu’une hypothèse.
- La correction verticale globale varie d’environ **+38 à +295 mm** : elle révèle l’incohérence de reconstruction/échelle et ne la résout pas.
- Un pied reste jusqu’à **182 mm au-dessus du sol** après recalage global. Le corps montre une asymétrie visiblement incompatible avec une démonstration fiable.
- Les bras suivent un humain portant une barre, mais ni la barre ni une prise des doigts ne sont représentées. Les mains ne peuvent pas être présentées comme une variante sportive cohérente.
- Les orientations axiales, scapulas, doigts et contacts ne sont pas correctement observables depuis cette vue.

Aucun ancrage manuel de tous les pieds ou fondu n’a été utilisé pour faire croire à une meilleure reconstruction. Les coordonnées brutes et filtrées restent disponibles.

## 3. Référence D : véritable capture optique

**CMU Graphics Lab, sujet 22, essai 14, « alternating squats (2 subjects — subject A) ».** La FAQ primaire décrit un système Vicon à 12 caméras infrarouges et des acquisitions à 120 Hz. Ce n’est pas une animation inférée depuis la vidéo C.

Les conditions CMU permettent copie/modification/redistribution et utilisation dans des produits commerciaux, **sans revente des données seules, même converties**. Elles ne doivent pas être renommées CC0/MIT. La conversion BVH 2010 est de Bruce Hahne, avec notice conservée. La pose de calibration ajoutée en première image par le convertisseur est exclue de l’extrait.

Le prototype D reprend **0,7–1,7 s**, rééchantillonné à 60 Hz, avec une adaptation par directions osseuses et ratio de longueurs de jambe. Le facteur de conversion initial utilisé vient de la FAQ ASF/AMC ; le ratio source/cible compense l’échelle uniforme pour les segments et déplacements. Cela ne vaut pas calibration physique du sujet. Le GLB `mocap-prototype.glb` conserve Rocketbox et une seule descente.

**Limite majeure :** ce retargeting directionnel simplifié ne transporte pas toute la torsion axiale des os. Les pieds paraissent orientés de façon peu convaincante en bas ; les contacts et la dynamique de racine doivent être repris. Mains/orteils peuvent être bruités selon la source ; doigts/pouces ne sont pas réellement capturés. Le recalage vertical global varie de −51 à +23 mm. **Origine mocap authentique ≠ retargeting professionnel réussi.** Statut HOLD.

## 4. Comparaison objective, sans classement trompeur

Les quatre méthodes utilisent le **même modèle Rocketbox**, le même laboratoire, trois caméras fixes, le même éclairage et les mêmes calculs. Les durées/amplitudes et stratégies diffèrent ; il ne s’agit pas d’un essai contrôlé d’une même performance humaine. A est un extrait de la descente du squat manuel, B une transition asymétrique avec repositionnement, C un squat chargé sans sa barre numérique, D une descente de squat profond issue d’une interaction capturée.

| Mesure exportée | A · manuel | B · Rocketbox phase 4 | C · vidéo estimée | D · mocap CMU retargetée |
|---|---:|---:|---:|---:|
| Durée observée | 2,5 s | 4,5 s | 1,7 s | 1,0 s |
| Poses à 60 Hz | 151 | 271 | 103 | 61 |
| Vitesse articulaire max | 0,482 m/s | 1,186 m/s | 2,464 m/s | 3,530 m/s |
| Accélération discrète max | 2,00 m/s² | 21,37 m/s² | 80,09 m/s² | 134,08 m/s² |
| Écart au sol maximal d’un pied | ~2 mm | 38,6 mm | **182,0 mm** | 30,0 mm |
| Déplacement horizontal maximal du sommet de semelle choisi au départ | 0,022 mm | 506,8 mm | 528,7 mm | 79,3 mm |
| Variation de longueur des segments | <0,001 mm | <0,001 mm | <0,001 mm | <0,001 mm |
| Décision | Référence existante | Candidate HOLD | **Rejeté runtime** | HOLD |

Le déplacement total d’un sommet **n’est pas du glissement prouvé** : B contient notamment un vrai pas de repositionnement et des rotations sur les orteils. Sans calendrier de contact approprié, il ne doit pas être confondu avec la dérive sur un plateau planté mesurée en phase 4. De même, une accélération plus faible sur une descente plus lente ne démontre pas une meilleure naturalité.

586 poses ont été évaluées sur A/B/C/D. Les longueurs osseuses sont préservées par construction et vérifiées après export, mais les déformations visuelles de peau, torsions et auto-intersections ne sont pas couvertes par cette seule mesure. Aucune mesure d’erreur 3D par rapport à une vérité terrain vidéo calibrée n’existe pour C. Aucun score de précision inventé.

**Sélection actuelle :** conserver le parcours existant ; ne pas remplacer ses mouvements par C ou D. La capture multi-vues consentie et le nettoyage de retargeting sont une piste à tester, pas un résultat déjà supérieur démontré.

## 5. Raccords aux exercices

Chaque entrée C/D est comparée à la **fin de chacun des huit exercices**, échantillonnée à une image de la fin de boucle ; chaque sortie est comparée au début de chacun des huit exercices. Aucun alignement caché de racine, aucune téléportation, aucun fondu.

Meilleur écart maximal sur les articulations parmi les huit poses comparées :

| Prototype | Exercice précédent → entrée | Sortie → exercice suivant |
|---|---:|---:|
| C | 534 mm | 665 mm |
| D | 236 mm | 723 mm |

Ces écarts dépassent largement les 15 mm du contrôle d’admission existant. La comparaison positionnelle suffit déjà au refus ; une future approbation exigerait aussi orientation, vitesse, contacts et récupération. Les tests de `coach-transition-gate.js` restent actifs. Aucune nouvelle route n’a été ajoutée, aucun candidat n’est activable par la galerie. Les commandes vidéo des preuves ne constituent pas une activation dans le coach sportif.

## 6. Preuves et revue

Livrés : vidéo humaine source, overlay annoté complet, landmarks bruts/filtrés, deux GLB diagnostics, 16 MP4 A/B/C/D (face, profil, trois-quarts et ralenti ×0,5), départ/arrivée pour les quatre méthodes, mesures et licences. **18 fichiers vidéo** ont été intégralement décodés par FFmpeg et leurs empreintes vérifiées. Chromium lit aussi la source WebM, l’overlay et les quatre angles comparatifs.

Inspection visuelle de la source et de poses de résultat C/D effectuée ; **aucun visionnage professionnel continu ni approbation biomécanique n’est attesté**. Le dossier professionnel des huit exercices est conservé. Pour la revue de cette phase, examiner particulièrement : pieds hors champ, visibilité, ambiguïté de profondeur, mains sans barre, torsion de cheville/genou, dérive de bassin, corrections verticales et raccords. Ces critères et le protocole de consentement doivent être traités avant une capture propre à PARISFIT.

## 7. Tests et préservation

- `npm test` : PASS, nouveaux contrôles de source/landmarks/GLB/licences embarquées et isolation runtime.
- `npm run test:browser` : PASS local, y compris huit exercices, 2 840 poses de régression, caméra/pause/ralenti/mouvement réduit, hors-ligne, repli, galeries historiques et nouveau comparatif à 60 Hz.
- Galerie phase 5 : chargement source/overlay/A/B/C/D et largeurs 320, 390, 768, 1200 px sans débordement détecté.
- L’inférence Python n’est pas relancée en CI : elle est reproductible par les scripts et ses sorties sont vérifiées. Les tests navigateur rechargent réellement les GLB et recalculent leurs trajectoires.
- GLB runtime inchangé : SHA256 `1fc67dc3453d6c0eae589ef3203923f52b4db303c0c9e73714e174cba5d398bb`. Ni nouveau modèle, ni modification du parcours, ni augmentation du précache applicatif.

Émulation Chromium/WebGL logiciel récente : 390/412 px, chargement 2 391/585 ms, 25,2/22,9 FPS logiciels sur trois secondes, heap JS ~13 Mo. Ces chiffres concernent le coach existant, **pas le coût runtime d’une nouvelle transition activée**. Aucun iPhone/Android physique, aucune mesure matérielle de chauffe, batterie ou VRAM. Les résultats sont séparés dans `mobile-emulation-report.json`.

## 8. Reproduction complète

Prérequis : Python 3.11 dans un venv, npm/Playwright, serveur HTTP à la racine sur port 3000. Outils locaux seulement. GitHub est utilisé pour télécharger deux fixtures publiques vérifiées ; jamais pour envoyer une vidéo personnelle.

```sh
python3 -m venv .venv
sh tools/mocap/setup-local.sh
npm ci
# Serveur HTTP sur 3000 et Chromium disponibles
.venv/bin/python tools/mocap/download-fixtures.py
.venv/bin/python tools/mocap/extract-pose.py
node tools/mocap/export-video.cjs
node tools/mocap/export-cmu.cjs
.venv/bin/python tools/optimize-coach.py docs/coach/phase5/video-prototype.glb
.venv/bin/python tools/optimize-coach.py docs/coach/phase5/mocap-prototype.glb
.venv/bin/python tools/mocap/stamp-provenance.py
export FFMPEG_PATH=$(.venv/bin/python -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())')
node tools/mocap/capture-comparison.cjs
node tests/coach-mocap-prototype.cjs
.venv/bin/python tools/mocap/verify-evidence.py
npm test
npm run test:browser
```

Dans ce sandbox : `CHROMIUM_PATH=/tmp/chromium`, `LD_LIBRARY_PATH=/tmp/al2023/lib`. Ailleurs installer Chromium avec Playwright. Les sorties ML peuvent varier suivant versions/CPU : comparer les métriques et conserver les hashes, ne pas promettre une identité binaire entre machines. Les données .cache ne sont pas requises pour lire les preuves persistées ; le BVH peut être téléchargé à nouveau par son blob vérifié.

**Prochaine étape :** obtenir une séquence réellement adaptée (sans barre, corps entier, multi-vues calibrées, consentement et professionnel), puis reprendre les torsions et les contacts du retargeting. Le prototype montre où l’information manque ; il ne justifie ni une généralisation aux autres transitions ni une levée du blocage de la PR.
