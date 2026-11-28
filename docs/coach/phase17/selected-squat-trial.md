# Essai retenu : AB01 / Squat / répétition 1

**Qualification partielle — B.** Sélection pour une étude passive, pas pour une intégration ni une démonstration de «bon squat». Consultation : 27 novembre 2026. Base PARISFIT : `21c0ed2707673d8e23822a08f7c82d48a9e2d7cf`.

## Inventaire vérifié et choix

L’arbre Git officiel non tronqué au commit `a26fe4852a78f30c5e8a437b158847031cb8dc3c` contient les participants **AB01–AB10**, chacun avec **Squat/1, /2, /3** et **Static/1** : 30 C3D de squat et 10 statiques. Aucun identifiant de session distinct de cette arborescence n’est exposé ; nous n’inventons pas une session ou une date de capture. Le protocole de l’article décrit dix adultes sains, cinq femmes/cinq hommes, sans pathologie autodéclarée affectant équilibre ou marche, et trois prises par activité.

Choix prospectif : conserver le candidat AB01/1 déjà identifié en phase16, plutôt que chercher après coup le plus faible résidu ou un mouvement flatteur. Conditions d’inclusion de ce cas : squat explicite, statique individualisé relié par les scripts, MarkerSet complet pour son protocole, forces des deux pieds et fichiers de configuration disponibles. La lecture confirme les conditions matérielles ci-dessous. La **représentativité est celle du protocole tenu**, pas une représentativité statistique, une technique sportive exemplaire ou une sélection du meilleur des 30 essais. Nous n’avons pas inspecté leurs signaux pour les classer.

AB01 : masse **49,81 kg**, stature **1,73 m** dans `All subjects processing/save_data_info.m:L4–8` ; le setup de scaling utilise 49,81 kg. Ces données ne suffisent pas à déclarer AB01 représentatif de la population. Ni sexe individuel, ni âge individuel déduits. L’objectif de la collecte est notamment l’étude du centre de masse, pas la certification d’un geste de coach sportif.

## Fichiers et empreintes calculées sur les octets téléchargés

|Fichier dans le dépôt officiel|Octets|SHA256|
|---|---:|---|
|`AB01/Squat/1/Data/squat_1.c3d`|4439424|`7d4adaf1ca565de3fc172cde1b92a6b607f7a90d1f22b37453fa0cd4b6e30482`|
|`AB01/Static/1/Data/static.c3d`|2560224|`ba89054b8d0bb0cb18087be68b81e1a326dcf2719c012dff73a5591102b1b4b1`|
|`Model/marker_set.xml`|36277|`73a84f9f4e4d470727793603060c6478d82f3805d7d73b7d805a74fb90c36a21`|
|`Model/Biomech57.osim`|907212|`2e815b8282df18ab5ed10b3c1434a2f1555ae38d6ef41089c52e902683973214`|

Les **24 fichiers acquis, 8 237 085 octets au total**, leurs chemins, Git blob SHA1 et SHA256 figurent dans [source-manifest.json](source-manifest.json). Seuls deux C3D ont été téléchargés. Les autres fichiers sont les configurations de ce couple, le modèle, le MarkerSet, le README et de petits scripts communs. Aucune archive participant de 1,39 Go ou collection complète téléchargée. Sources conservées dans le cache ignoré par Git ; acquisition reproductible par le script épinglé. Les hashes MD5 calculés des trois petits fichiers README/modèle/MarkerSet correspondent aussi aux MD5 publiés dans l’API Figshare, sans prouver pour autant l’identité du C3D avec le contenu de l’archive non acquise.

## Association statique : preuve, pas proximité de dossier

Depuis `AB01/Squat/1/Processing`, `trial_class.m:L130–141` résout `../../Static/1/Data/static.trc` relativement au parent du dossier de travail, donc **AB01/Static/1/Data/static.trc**, et le setup de scaling de ce même statique. `process_trial_data.m:L3–6` désigne explicitement `squat_1.c3d`. Le README (p.1, note après étape5) exige de traiter le statique du participant avant les autres activités. Le script statique désigne `static.c3d` et l’export TRC est décrit dans `trial_class.m:L616–624`.

**Limite :** les TRC/MOT générés et la version modifiée de `Osim.Scale` ne sont pas dans l’arbre Git inspecté. La chaîne prévue est identifiée ; aucune exécution ni preuve d’une sortie générée identique n’est revendiquée.

## Complétude réellement observée

- Statique : **57 labels**, tous identiques au MarkerSet XML ; **1 565 frames lisibles**, 200 Hz. Aucun échantillon de marqueur déclaré invalide ou non fini parmi ces frames.
- Squat : **49 labels**, exactement ceux du setup IK ; **2 948 frames lisibles**, 200 Hz ; **14 740 échantillons analogiques**, 1000 Hz, 36 canaux de six plateformes. Aucun échantillon invalide/non fini dans les données lisibles.
- Absents du squat : **LHME, RHME, LFME, RFME, LTAM, RTAM, LFM2, RFM2**. Ce sont les huit marqueurs de calibration que le protocole retire après l’A-pose ; pas huit pertes inexpliquées.
- Les résidus C3D sont tous zéro. Ils ne prouvent **ni exactitude optique parfaite ni absence de lacunes à l’acquisition** : l’article décrit des trajectoires déjà interpolées et filtrées.
- Intervalle relatif des frames lisibles : squat **0–14,735 s**, statique **0–7,820 s** ; ce ne sont pas des horodatages absolus.

### Discordance de borne C3D à conserver

`POINT:FRAMES` annonce 2948/1565 et les octets contiennent bien ce nombre de frames complètes. En revanche les en-têtes annoncent une première frame0 et une dernière2948/1565, soit une de plus sous convention inclusive. `python-c3d 0.6.0` signale donc EOF en tentant la frame supplémentaire. L’audit conserve ce warning, le compteur du paramètre, les bornes de l’en-tête, le nombre lisible et les tailles de blocs. **Pas de réparation, de frame inventée ni de preuve de perte à l’acquisition.** Une convention d’export décalée paraît plausible ; à vérifier avec un second lecteur ou la spécification d’export avant expérimentation.

## Ce qui constitue le mouvement

Les auteurs décrivent une descente, un maintien d’au moins 8 s et un retour neutre, à rythme naturel, pieds sur plateformes1/2. Le diagnostic RIAS original et les forces montrent une séquence continue compatible avec ce protocole ; ce n’est pas une segmentation anatomique des phases. Le README annonce des indices de maintien dans `one_leg_squat_shoe_lace_samples.mat`, **absent de l’arbre Git inspecté**. Durée exacte du maintien d’AB01/1 non certifiée, aucune annotation de phase inventée.

## Droits et sources

Données : **CC BY4.0** affiché par le [dépôt Notre Dame DOI10.7274/28689221](https://curate.nd.edu/articles/dataset/Whole-body_optical_marker_and_ground_reaction_force_data_of_healthy_humans_performing_non-cyclic_activities/28689221), auteurs Mohsen Alizadeh Noghani, Sebastian Green, Edgar Bolívar-Nieto. Article : [DOI10.1038/s41597-025-06227-7](https://pmc.ncbi.nlm.nih.gov/articles/PMC12717423/), 2025. L’article relie explicitement ce [dépôt GitHub](https://github.com/WeRoLab/healthy-whole-body-noncyclic-dataset/tree/a26fe4852a78f30c5e8a437b158847031cb8dc3c) au traitement officiel. Attribution, lien de licence et indication des adaptations requis pour réutilisation, y compris commerciale. Pas d’endossement ; licences amont du modèle Rajagopal et des bibliothèques à qualifier avant redistribution. Ici, pas de redistribution de C3D/modèle ou de vidéo de personne, uniquement audit et citations ciblées. Le schéma PARISFIT est documentaire, pas une photographie ni une validation professionnelle.
