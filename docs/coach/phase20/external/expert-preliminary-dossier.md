> Phase20 — 2026-11-27, date de session. Référence `25ebee0ec3161ca5415d4961bd8d04ea4404af84`. Consultation documentaire uniquement ; aucun avis indépendant reçu.

# Dossier d’expertise documentaire préliminaire

## Mandat et lecture conseillée

Examiner et contester la défendabilité des interprétations, **sans reconstruire le mouvement**. AB01 est le pseudonyme du participant ; Squat/1 est une répétition, Static/1 la référence prévue par le code. Ni identité civile, ni âge/sexe individuel, ni date de capture ne sont déduits. L'objectif publié est l'étude d'activités non cycliques, pas la certification d'un squat sportif.

Lire d'abord la matrice C01–C15, puis les questions prioritaires et les sources citées. Distinguer constat dans un fichier, déclaration des auteurs, interprétation documentaire et hypothèse à examiner. Le protocole publié prévoit descente, maintien ≥8s et retour naturel, trois répétitions ; la durée exacte de maintien d'AB01/1 n'est pas certifiée.

## Corpus et identification

- [Essai et association statique](https://github.com/aydiarra-star/PARISFIT/blob/25ebee0ec3161ca5415d4961bd8d04ea4404af84/docs/coach/phase17/selected-squat-trial.md), avec correction de borne à lire impérativement dans l'[erratum18](https://github.com/aydiarra-star/PARISFIT/blob/25ebee0ec3161ca5415d4961bd8d04ea4404af84/docs/coach/phase18/c3d-integrity-and-timing.md).
- [Manifest des24 sources](https://github.com/aydiarra-star/PARISFIT/blob/25ebee0ec3161ca5415d4961bd8d04ea4404af84/docs/coach/phase17/source-manifest.json), [MarkerSet et configurations](https://github.com/aydiarra-star/PARISFIT/blob/25ebee0ec3161ca5415d4961bd8d04ea4404af84/docs/coach/phase17/configuration-inspection.json), [registre57](https://github.com/aydiarra-star/PARISFIT/blob/25ebee0ec3161ca5415d4961bd8d04ea4404af84/docs/coach/phase18/marker-review-register.csv), [schéma documentaire](https://github.com/aydiarra-star/PARISFIT/blob/25ebee0ec3161ca5415d4961bd8d04ea4404af84/docs/coach/phase17/markerset-schematic.svg) : le schéma n'est pas une photo de placement.
- Squat C3D :4439424 octets ; SHA256 `7d4adaf1ca565de3fc172cde1b92a6b607f7a90d1f22b37453fa0cd4b6e30482`.
- Static C3D :2560224 octets ; SHA256 `ba89054b8d0bb0cb18087be68b81e1a326dcf2719c012dff73a5591102b1b4b1`.
- MarkerSet SHA256 `73a84f9f4e4d470727793603060c6478d82f3805d7d73b7d805a74fb90c36a21` ; modèle `2e815b8282df18ab5ed10b3c1434a2f1555ae38d6ef41089c52e902683973214`.
- [Inventaire logiciel](https://github.com/aydiarra-star/PARISFIT/blob/25ebee0ec3161ca5415d4961bd8d04ea4404af84/docs/coach/phase19/dependency-version-inventory.md) : Motive3.0.3 Final déclaré dans les deux fichiers ; MATLAB2023b/OpenSim4.4 déclarés par l'article. Builds et certaines dépendances exactes inconnus.
- [Journaux originaux](https://github.com/aydiarra-star/PARISFIT/blob/25ebee0ec3161ca5415d4961bd8d04ea4404af84/docs/coach/phase19/ab01-original-logs-inventory.md) et [extraits hashés](https://github.com/aydiarra-star/PARISFIT/blob/25ebee0ec3161ca5415d4961bd8d04ea4404af84/docs/coach/phase19/archive-probe.json) : opérations AB01/Squat/1, sortie2948 lignes ; aucune nouvelle exécution.

## Synthèse contradictoire

La [matrice](evidence-and-claims-matrix.csv) relie chaque conclusion à sa preuve, ses incertitudes, une interprétation alternative et les conséquences pour une animation. Les44 définitions confirmées/13 plausibles qualifient des descriptions, non57 poses cutanées vérifiées. Les57 rattachements logiciels ne valident pas57 centres articulaires. Les huit marqueurs retirés après le statique expliquent49 labels dynamiques selon le protocole, sans prouver l'absence de gaps avant traitement.

Les4,21cm sont une moyenne publiée de scaling statique, **pas l'erreur du squat AB01**. Le journal statique mentionne aussi RMS0.0416775 et max0.0737885(LTH) dans un contexte de placement modèle ; pas un seuil ni un certificat dynamique. Les configurations scaling/IK sont des entrées disponibles, non une validation de leurs choix. Les résultats IKError.mat sont localisés, pas interprétés numériquement ici.

Les forces ne prouvent pas un contact plantaire complet ; le ratio200/1000Hz ne démontre pas la synchronisation physique. Aucun transfert vers Rocketbox n'a été validé anatomiquement. Les paramètres de séance, pose réelle, calibration individuelle et corrections de gaps restent insuffisamment tracés.

## Chronologie à ne pas confondre

Phases14–15 : limites du candidat Michaud et plan méthodologique ; pas des facteurs AB01. Phase16 : recherche et sélection Notre Dame. Phase17 : audit passif AB01, dont une attribution d'en-tête corrigée explicitement phase18. Phase18 : erratum, questions et critères d'admission. Phase19 : bibliothèques et journaux retrouvés dans les archives, malgré leur absence du Git précédemment inspecté. Aucun document antérieur n'est remplacé.

## Sources et droits

Alizadeh Noghani, Green, Bolívar-Nieto (2025), [article DOI10.1038/s41597-025-06227-7](https://pmc.ncbi.nlm.nih.gov/articles/PMC12717423/), [dataset DOI10.7274/28689221](https://doi.org/10.7274/28689221), données CC BY4.0 ([conditions](https://creativecommons.org/licenses/by/4.0/)). Code officiel épinglé `a26fe4852a78f30c5e8a437b158847031cb8dc3c`. [Guide Biomech57](https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57) : référence générique, ambiguïtés conservées. Licences MIT des outils retrouvées ; droits amont modèle/géométries à confirmer avant redistribution. Le présent texte est une synthèse PARISFIT, non un endossement par les auteurs.

Voir [questions](expert-questionnaire-final.md), [partage](README.md) et [conditions expérimentales](README.md). Aucun fichier transmis et aucune réponse professionnelle reçue.
