# PARISFIT — Phase 3 : transitions candidates, validation non acquise

27 novembre 2026 · suite de `697523f` · PR #11 **en brouillon**, aucune fusion ni production.

## Bilan sans ambiguïté

Deux animations de bibliothèque humaine officielle ont été retargetées et rendues : **debout→accroupi** et **accroupi→debout**, 4,5 secondes chacune. Ce ne sont pas des interpolations inventées entre deux poses. Elles préservent l’asymétrie, le repositionnement et le timing source. Mais leurs appuis et raccords ne sont pas suffisamment établis : **statut HOLD, aucune activation dans les changements d’exercice**.

L’objectif complet des six transferts et du réalisme d’un coach filmé **n’est pas atteint**. Le choix de ne pas insérer des séquences non validées est délibéré, pas une déclaration de réussite. Les coupures explicites de phase 2 restent en place dans l’application.

## Livrables

- [Galerie phase 3](index.html) : 16 nouvelles vidéos (2 transitions × avant/après × face/profil/trois-quarts/ralenti), commandes vidéo natives sans autoplay ; lien depuis la galerie phase 2.
- [Dossier professionnel HTML](professional-review.html) et [PDF imprimable](professional-review.pdf) : huit fiches, 64 liens vers les vidéos originales, phases pédagogiques exactes, muscles, niveaux/dosages à examiner, alternatives écrites, critères et champs d’avis vides.
- [Contrôles des candidates](transition-report.json), [intégrité vidéo](video-report.json), [régression des huit exercices](exercise-trajectory-report.json), [émulation mobile](mobile-emulation-report.json), [journal des tests locaux](local-test-log.txt).
- [Protocole iPhone Safari / Android Chrome](DEVICE-PROTOCOL.md) et [sources/licences/retargeting](SOURCES.md).
- `assets/coach/transitions/{candidates,raw-retarget,source}.json` : clips Three.js et provenance, non chargés par le parcours ni précachés par le shell. Environ 8,4 Mo pour les deux versions JSON d’étude ; aucun ajout au GLB runtime.

## Couverture de la demande

| Passage demandé | Réalisation | Statut |
|---|---|---|
| Debout → accroupi | Source Rocketbox masculine retargetée ; 4,5 s, 271 poses testées | Candidate HOLD |
| Accroupi → genoux | Pas de source exacte retenue | Non réalisé |
| Genoux → sol | Pas de source exacte retenue | Non réalisé |
| Sol → gainage | Pose/contacts de départ et trajectoire à construire avec revue | Non réalisé |
| Allongé → assis | Pas de source exacte retenue | Non réalisé |
| Assis → debout | Le lever depuis une chaise n’est pas assimilé à un lever depuis le sol | Non réalisé |
| Accroupi → debout (complément) | Source Rocketbox inverse distincte, non simple inversion temporelle | Candidate HOLD |

Aucun mouvement n’est réétiqueté « à genoux » parce qu’un genou approche le sol. Une pose accroupie n’est pas une position assise. Aucun raccord en fondu n’a été ajouté pour dissimuler ces manques.

## Ce qui a changé techniquement

1. Import FBX officiel via Three FBXLoader, source sous MIT vérifiée, aucune dépendance payante.
2. Transfert des rotations **en espace monde** afin de tenir compte de la hiérarchie réparée du modèle cible ; longueurs osseuses cible conservées. Translation de racine adaptée au rapport des longueurs de jambes. 80 os correspondants, aucun absent.
3. Échantillonnage à 60 Hz, clips one-shot avec arrêt sur la dernière pose. Un défaut de remise à la pose initiale à la fin du clip a été trouvé pendant l’import et corrigé avant les preuves finales.
4. Version « avant » = retarget brut ; « après » = recalage vertical global du point le plus bas du maillage à 2 mm. Correction environ −5,5 à +7,3 mm selon le clip et le temps. **Ce n’est pas une correction latérale des pieds, ni une simulation d’équilibre.**
5. Galerie et chaîne de génération isolées de la production ; preuves phase 2 préservées.

## Mesures et limites des candidates

542 poses contrôlées à 60 Hz : surface contrôlée minimale ~2 mm ; vitesse maximale d’articulation 1,19 m/s à la descente, 1,81 m/s à la remontée ; déplacement vertical du bassin ~46,4 cm. Pas de saut de pose final détecté par la borne de vitesse.

Les alarmes restent visibles : déplacement du pivot du pied près du sol jusqu’à **11,0 / 12,2 mm par échantillon**, écart maximal pied/sol **38,6 / 57,2 mm**. Une partie peut correspondre à un pas ou à une rotation sur l’avant-pied : le déplacement d’un pivot n’est pas une mesure certaine de glissement de la surface en contact. Il manque un calendrier de contacts validé pour trancher. Ces mesures ne sont donc ni masquées ni présentées comme un défaut biomécanique certain.

Manquent également le centre de masse/forces, les contacts main-cuisse, les auto-intersections exhaustives et les raccords aux huit exercices. Le test d’audit peut réussir à mesurer/exporter un rapport **HOLD** : cela ne signifie pas que le mouvement a passé un seuil d’acceptation.

Les 16 vidéos ont été intégralement décodées par FFmpeg, et chargées par Chromium ; durée, intégrité et provenance contrôlées. Deux planches après ont été inspectées visuellement. **Aucun visionnage professionnel continu ni validation qualifiée n’est attesté.** La lecture/décodabilité et les tests numériques ne remplacent pas cette revue.

## Huit exercices conservés et réexaminés techniquement

Le GLB de phase 2 est strictement inchangé : 5 789 744 octets, SHA256 `1fc67dc3453d6c0eae589ef3203923f52b4db303c0c9e73714e174cba5d398bb`. Ses huit cycles ont de nouveau passé les contrôles 60 Hz de trajectoires, appuis, continuité de boucle, alternance et stabilité. Les consignes, phases, lecture/pause, vitesses, reset, étapes et choix restent testés.

| Exercice | Point encore ouvert pour la revue qualifiée |
|---|---|
| Squat | Amplitude, genoux et retour au repos |
| Pompes | Poignets/doigts, profondeur, alignement tête-bassin |
| Gainage | Appuis avant-bras et crédibilité de la respiration discrète |
| Fentes | Transfert de charge, alternance et retour debout |
| Jumping jacks | Impulsion/réception et continuité dynamique réelle |
| Mountain climbers | Épaules, bassin, rythme lent versus catégorie cardio |
| Haut du dos debout | Identification de la variante et cohérence des régions sollicitées |
| Petits cercles des bras | Scapulas, épaules/coudes et amplitude |

Une incohérence éditoriale a été corrigée : « Dos, lombaires » devient « Haut du dos, épaules » pour la variante debout montrée. Les niveaux/dosages restent éditoriaux, non approuvés. Pas de respiration/repositionnement supplémentaire ajouté au hasard ; pas de nouvelles variantes animées déclarées.

## Expérience utilisateur

Changement de point de vue désormais en **orbite fluide de 360 ms**, sans traverser le personnage ; distance conservée. La pose reste immobile si la démonstration est en pause. La rotation manuelle interrompt l’orbite automatique. La réduction des animations supprime le tween ; arrêt propre hors écran/à la destruction du rendu. Test spécifique smartphone 390 px, lecture en pause et mouvement réduit.

Les autres commandes, erreurs/retry, chargement différé, cadrage existant et design PARISFIT sont préservés. Cache shell-v9, URLs 20261127-9 ; les clips de recherche ne gonflent pas le chargement du Coach. Aucun changement anatomique du modèle sans preuve d’amélioration.

## Tests exécutés

- `npm test` : PASS, y compris vérification des 16 nouvelles vidéos et des 64 liens de revue, SHA des clips/GLB et interdiction d’activation des candidates dans le runtime.
- `npm run test:browser` : PASS local, smoke existant, huit exercices/trois vues, commandes et phases, hors-ligne/repli, 2 840 poses d’exercice, émulation, galeries phase 2/3, caméra, audit des 542 poses de transition.
- FFmpeg : PASS, décodage intégral des 16 nouvelles vidéos.
- Aucun avis professionnel obtenu. Aucune mesure matérielle iPhone/Android effectuée.
- CI distante : consulter les checks de la PR après publication ; son succès technique ne lève pas le HOLD des animations.

## Émulation versus appareils physiques

Nouvelle exécution Chromium headless, WebGL logiciel : 390/412 px, DPR plafonné à 1,25. Chargement local 3 439/514 ms ; cadence logicielle sur trois secondes 32,8/24,9 FPS ; heap JS ~10,1/12,2 Mo. Pause et hors-écran arrêtent le dessin ; perte/restauration de contexte via extension : PASS. Ces chiffres varient avec cache/serveur et **ne représentent pas un téléphone réel**. Ni chauffe, ni batterie, ni VRAM matérielle mesurées. Le protocole joint prévoit ces mesures avec champs « non mesuré » explicites.

## Prochaine étape bloquante

Faire revoir les clips complets et les textes par un professionnel, fixer le calendrier d’appuis des candidates avec un animateur, puis construire les passages manquants depuis des sources autorisées adaptées. Un raccord doit être testé pose/vitesse/contact de part et d’autre, pas simplement fondu. Réaliser les essais physiques avant d’affirmer une qualité premium ou une proximité avec une vraie vidéo humaine. **PR #11 reste en brouillon ; aucune fusion ni production.**

## Reproduction

`python tools/download-coach-transitions.py` (gh configuré), serveur HTTP port 3000, `node tools/export-coach-transitions.cjs`, `node tests/coach-transitions.cjs`. Pour les vidéos : définir `FFMPEG_PATH`, lancer `STAGE=before` puis `STAGE=after node tools/capture-coach-transitions.cjs`, puis `python tools/verify-transition-videos.py`. Pour les planches : `EVIDENCE_ROOT=docs/coach/phase3 STAGE=after python tools/review-cycle-frames.py`. Le dossier professionnel HTML se régénère avec `node tools/build-coach-review.cjs`. Chromium et libs du sandbox : `CHROMIUM_PATH=/tmp/chromium`, `LD_LIBRARY_PATH=/tmp/al2023/lib`.
