# PARISFIT · Phase 2 — corrections livrées, acceptation encore partielle

27 novembre 2026 · branche `arena/a03f64da-parisfit` · **PR #11 en brouillon**. Aucune fusion ni mise en production autorisée ou effectuée.

## Conclusion

Le modèle humain Rocketbox existant est conservé. Les huit clips, les contacts, le visage et la pédagogie ont été améliorés ; les régressions locales passent. **Ce résultat n’est ni de la mocap, ni une validation biomécanique, ni une qualité premium approuvée.** Les transferts corporels entre exercices restent à réaliser, ainsi que la revue professionnelle et les essais sur appareils physiques.

- [Galerie vidéo avant/après](index.html) : 64 MP4, quatre vidéos par exercice et par version (face, profil, trois-quarts, ralenti ×0,5).
- [Résultats des trajectoires corrigées](trajectory-report.json), [audit numérique de la baseline](before-trajectory-report.json), [intégrité vidéo](video-report.json).
- [Résultats en émulation mobile](mobile-report.json), [protocole de revue professionnelle](PRO-REVIEW.md), [sources et licences étudiées](MOTION-SOURCES.md).

## Audit et preuves

PR #11 auditée ouverte/en brouillon, baseline `10eb8bf`, historique de phase 1 conservé dans `../REPORT.md`. Aucun redémarrage du projet. Accueil, données, navigation, Nutrition, Mental, habitudes et parcours existants conservés ; régression smoke exécutée.

Les dossiers `before/` et `after/` contiennent chacun 32 vidéos, huit planches temporelles (trois angles), huit images initiales, huit images au milieu du cycle et deux gros plans visage/main. « Midpoint » désigne le milieu temporel, **pas nécessairement l’effort maximal**. Les planches sont des aides à la revue, pas une substitution aux vidéos. Les 64 fichiers ont été décodés intégralement par FFmpeg, chargés par Chromium et associés à leur SHA256. Les vidéos corrigées correspondent exactement au SHA du GLB ci-dessous.

**Limite importante de l’examen :** inspection visuelle de planches temporelles et de détails, contrôle automatique continu échantillonné à 60 Hz. Aucun visionnage humain expert intégral de chaque vidéo n’est attesté. Le décodage continu et le calcul des articulations ne constituent pas une revue visuelle professionnelle. Cette exigence reste ouverte.

## Défauts constatés et corrections

| Exercice / durée après | Avant | Correction effectuée | Réserve |
|---|---|---|---|
| Squat / 5 s | Timing mécanique, appuis à vérifier | Interpolation quintique, pieds recalés sur la surface, progression lente et consignes synchronisées | Amplitude et placement à revoir professionnellement |
| Pompes / 5 s | Paumes environ 41 mm au-dessus du sol, doigts seuls en appui, autres pénétrations | Paumes à environ 2 mm, doigts dépliés, bassin/tête coordonnés, flexion contrôlée | Poignets, doigts et profondeur non approuvés |
| Gainage / 6 s | Appui avant-bras incomplet, bassin oscillant | Bassin fixe, appuis avant-bras et paumes recalés, mouvement respiratoire discret | Pas une simulation de respiration ou de charge musculaire |
| Fentes / 10 s | Pas de vraie alternance, pied avant non ancré | Fentes arrière gauche/droite, deux phases distinctes, ancrage du pied avant | Transfert de poids encore synthétique |
| Jumping jacks / 3,2 s | Ouverture glissée et réception peu explicite | Préparation, envol, ouverture, retour, réception ; suppression d’une discontinuité de boucle et d’une singularité IK détectées pendant le travail | Pas de dynamique physique de contact |
| Mountain climbers / 4 s | Appuis et bassin instables, flexion excessive, pénétrations | Genoux alternés contrôlés, mains stables, bassin fixe, amplitude limitée | Variante lente ; pas une démonstration cardio rapide |
| Haut du dos debout / 8 s | Intitulé/consigne génériques peu identifiables | Démonstration douce debout, mains devant, consignes reformulées pour la pose affichée | Pas un étirement au sol ; amplitude modeste à valider |
| Petits cercles des bras / 6 s | Mouvement d’élévation ne correspondant pas bien aux cercles | Cercles modérés avec coudes souples ; pôle IK stabilisé et instructions correspondantes | Pas une circumduction complète d’épaule |

Une mesure distincte **paume/doigts** a révélé un défaut que le test « point le plus bas de la main » masquait. Le contrôle et le rig ont été corrigés ensemble ; le test actuel ne confond plus contact des doigts et contact de la paume.

## Réalisme et coût

- Même maillage humain professionnel, même licence MIT Microsoft et même provenance figée. Aucun remplacement par primitives.
- Couleur du visage 2048 px, couleur du corps 1024 px, normales PNG sans perte ; rugosité et intensité des normales adaptées. Ombres et plan de sol ajustés ; mains dépliées pour les exercices au sol. Vignettes régénérées depuis les nouveaux clips.
- Limites visibles : géométrie ancienne, doigts anguleux, visage statique, pas de simulation des vêtements ni remodelage anatomique. Amélioration de texture ≠ photoréalisme moderne.
- GLB : **5 789 744 octets**, contre 3 190 948 avant ; hausse volontaire pour les textures normales/visage et les clips. 80 os, quatre textures, huit clips échantillonnés à 30 Hz.
- SHA256 : `1fc67dc3453d6c0eae589ef3203923f52b4db303c0c9e73714e174cba5d398bb`.
- Coût engagé : 0 €. Aucun asset commercial acheté, aucun nouveau dataset mocap importé.

## Pédagogie, contrôles et transitions

`coach-content.js` centralise pour chaque exercice : résumé, mise en place, phases horodatées, erreur courante, correction, précaution, alternative accessible **écrite et non animée**. Les muscles restent indiqués dans la fiche. Le curseur, le libellé de phase, la consigne et le bouton « étape suivante » suivent le temps réel du clip. Les textes restent expérimentaux et soumis à revue.

Lecture/pause, vitesse normale/ralentie, retour initial, étapes, progression, trois vues, zoom, orbite et choix de l’exercice restent disponibles et testés. Les contrôles sont placés sous le rendu, avant la fiche longue sur mobile. Le cache PWA est révisé (`shell-v8`, ressources `20261127-8`) ; `coach-content.js` est précaché. Les requêtes vidéo Range ne sont pas stockées comme réponses partielles.

**Transferts non accomplis :** l’interpolation entre une pose debout et une pose au sol pouvait traverser le plancher. Elle est supprimée. Le changement devient une coupure visuelle brève, pause et message « mise en place non animée ». Cela évite de montrer un faux transfert, mais ne satisfait pas la demande de passage naturel debout/accroupi/genoux/allongé/planche/debout. Aucune variante animée par niveau n’est annoncée.

## Vérifications exécutées sur cette phase

| Contrôle | Résultat / portée |
|---|---|
| `npm test` | PASS : syntaxe, GLB, textures, squelette, clips, intégrité/provenance des 64 vidéos |
| `npm run test:browser` | PASS local : smoke existant, huit exercices/trois vues, commandes, phases, alternance des consignes, coupure en pause, hors-ligne/repli, trajectoires, émulation, galerie |
| Trajectoires 60 Hz | PASS, **2 840 poses**, huit cycles complets. Vitesse max d’articulation 4,10583 m/s ; erreur de boucle 0 à la précision rapportée ; dérive max par pas d’appui 4,76 mm ; minimum des surfaces contrôlées 1,62 mm au-dessus du plan |
| Audit baseline avec les mêmes garde-fous | FAIL attendu : 24 signalements, notamment paumes, avant-bras, alternance, bassin et flexion. Ce rapport conserve les défauts, il n’a pas été converti en PASS |
| FFmpeg | PASS : 64 vidéos entièrement décodées, durées/frames contrôlées. Ralenti obtenu par allongement des timestamps, pas par nouvelles poses |
| Chromium galerie | PASS : 64 MP4 décodables, lecture et retour au début, service worker actif |
| Diff Git | `git diff --check` PASS |

Les garde-fous (pénétration ≤4 mm, écart d’appui ≤7 mm, dérive par pas <8 mm, boucle <1 mm, vitesse <4,5 m/s, flexion genou <145°/coude <155°) sont **des seuils logiciels choisis pour détecter des régressions**, pas des critères de santé ou de bonne technique. Les groupes de surface sont associés aux os dominants ; il ne s’agit pas d’un calcul exhaustif d’auto-collision, de force d’appui ou de collision textile. Les pieds en vol sont distingués des appuis plantés. Tête, colonne, bassin et membres sont suivis via leurs trajectoires ; aucune conclusion clinique n’en est tirée.

## Mobile : résultats réels de l’émulation, appareils physiques absents

Chromium headless + WebGL logiciel, largeurs 390 et 412 px, DPR demandé 3 et plafonné à 1,25. Dernière exécution locale : chargement 3 308 / 494 ms, dessin logiciel environ 30,5 / 20,6 images/s sur une fenêtre de trois secondes ; heap JS environ 10,0 / 12,1 Mo. Ces chiffres varient selon cache/charge du serveur et **ne représentent ni un iPhone ni un Android**. Comptage renderer : huit géométries/six textures, pas une mesure des octets GPU.

Arrêt du dessin en pause et hors écran : PASS. Perte réelle de contexte WebGL via `WEBGL_lose_context`, rechargement après restauration : PASS. Repli et hors-ligne couverts par les régressions navigateur. Aucune température, consommation batterie ou mémoire GPU matérielle mesurée.

**À faire sur iPhone Safari et Android Chrome physiques :** démarrage froid/chaud en réseau mobile, chargement hors-ligne après visite, FPS et mémoire pendant 10–15 minutes, chauffe/batterie, rotation portrait/paysage, retour après verrouillage/interruption, changement répété des exercices, contexte WebGL et reprise après pression mémoire. Consigner modèle/OS/navigateur/réseau/durée et observations ; l’émulation ne remplace pas ces essais.

## Statuts séparés / décisions

- **Technique :** corrections et tests locaux PASS, garde-fous limités explicités ; résultat CI distant à consulter sur PR #11 après publication.
- **Visuel :** preuves comparables disponibles, amélioration partielle constatée sur planches ; revue continue experte et niveau premium non établis.
- **Professionnel :** non validé, voir `PRO-REVIEW.md`.
- **En attente :** transitions naturelles, revue exhaustive des intersections, approbation des textes/gestes, essais physiques iOS/Android, validation utilisateur.
- **Livraison :** code, modèle, licences, huit clips, preuves et tests disponibles ; **PR en brouillon, pas de fusion ni déploiement**.

## Reproduire

Installer les outils Node (`npm ci`), Chromium Playwright et un serveur HTTP sur le port 3000. Exécuter `npm test` puis `npm run test:browser`. `CHROMIUM_PATH` et `BASE_URL` sont facultatifs ; le sandbox actuel nécessite également `LD_LIBRARY_PATH=/tmp/al2023/lib`.

Pour régénérer les preuves : installer Pillow et FFmpeg (ou `imageio-ffmpeg`) dans un environnement Python, définir `FFMPEG_PATH`, lancer `STAGE=after node tools/capture-coach-cycles.cjs`, puis `STAGE=after python tools/review-cycle-frames.py` et `python tools/verify-coach-videos.py`. Pour la baseline : `mkdir -p .cache/phase2 && git show 10eb8bf:assets/coach/coach.glb > .cache/phase2/before.glb`, puis `STAGE=before` et `COACH_AUDIT_BEFORE=1 node tests/coach-trajectories.cjs`. Les ressources temporaires de `.cache` ne sont pas livrées ; les vidéos/rapports persistés sont dans ce dossier. Ne pas confondre les anciens rapports de phase 1 avec ces résultats.
