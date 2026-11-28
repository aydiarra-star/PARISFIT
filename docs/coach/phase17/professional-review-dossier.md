# Dossier de revue indépendante — non transmis, non validé

**Destinataire envisagé :** biomécanicien ou professionnel qualifié en reconstruction musculosquelettique à partir de marqueurs. Aucun expert n’a examiné ce dossier. Aucun envoi ni avis professionnel obtenu.

## Question de revue

Les données et approximations d’AB01/Squat/1 permettent-elles de préparer une future expérience contrôlée ? Il ne s’agit pas d’autoriser une animation ni de certifier un geste de coaching.

## Pièces du dossier

1. [Essai et provenance](selected-squat-trial.md) : squat tenu avec retour neutre, 49 marqueurs dynamiques, statique associé de 57 marqueurs, six plateformes dont deux affectées aux pieds.
2. [Schéma documentaire par région](markerset-schematic.svg) et [projections mesurées du statique](static-marker-projections.svg). Le premier est un inventaire topographique ; le second montre les points de la première frame existante, sans squelette estimé. Les vues XZ/YZ ne sont pas présentées comme des vues anatomiques face/profil certifiées.
3. [Table des 57 correspondances](marker-anatomical-mapping.csv) : nom original, site, segment, côté, rôle, parent OpenSim, pertinence articulaire, éventuel mapping Rocketbox, confiance et sources par ligne.
4. [Configurations](scaling-ik-configuration-audit.md), [extraction structurée](configuration-inspection.json) et [extraits numérotés](source-excerpts.md).
5. [Forces et synchronisation](ground-reaction-forces-audit.md), [courbes de diagnostic](trial-diagnostics.svg), [inspection C3D](c3d-inspection.json).
6. [Analyse du RMS publié](rms-scaling-error-analysis.md) et [empreintes des sources](source-manifest.json).

## Comment lire et contester les statuts

- **Confirmé :** la proposition précise est explicitement documentée. Un parent `/bodyset/pelvis` peut être confirmé par le XML sans que ce choix soit anatomiquement valide pendant un squat.
- **Plausible :** interprétation cohérente, mais non démontrée pour le sujet ou contradictoire dans la documentation. Ne permet aucune IK.
- **Inconnu :** information ou équivalence insuffisante. Toutes les équivalences vers les centres articulaires et Rocketbox restent inconnues.

Bilan : **44 définitions documentaires confirmées, 13 plausibles**, 57 rattachements logiciels explicites ; **aucun centre articulaire ni mapping Rocketbox confirmé**. Un label identique dans le C3D et le modèle ne prouve pas que le marqueur a été correctement palpé sur AB01. Les 80 noms d’os Rocketbox ont été lus, sans inférer de correspondance anatomique.

## Points sensibles à examiner

La [documentation OptiTrack Biomech57](https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57), citée par les auteurs, présente notamment :

|Labels ou choix|Constat conservé|Question de revue|
|---|---|---|
|LIAS/RIAS, LIPS/RIPS|Alias PSIS/ASIS en contradiction avec les descriptions antérieure/postérieure|Quelle définition est effectivement appliquée ? Aucune permutation de données réalisée.|
|TV2|«Deuxième vertèbre thoracique» et «three spine levels below C7»|Quel niveau a été palpé ?|
|LHM2/RHM2|«Hand Second metatarsal» mais placement sous l’index|Métacarpien probable, sans correction silencieuse du texte.|
|LUSP/RUSP, LRSP/RRSP|Styloïdes nommées, indications medial/lateral ambiguës ; USP fixé au radius dans le modèle|Posture de placement et approximation rigide acceptables ?|
|LSK/RSK|Titre Upper Leg/Superior Knee, description sur la jambe/tibia|Quel site et quelle fonction de suivi retenir ?|
|FTC → pelvis|Grand trochanter rattaché au bassin|Conséquence du mouvement relatif fémur/bassin pendant la descente ?|
|HGT → torso|Marqueurs postérieurs d’épaule rattachés au thorax|Quelle approximation de mobilité de la ceinture scapulaire ?|
|DP1 → calcn|Gros orteil rattaché au calcanéus, MTP verrouillée|Limite sur la représentation des pieds et de leurs appuis ?|
|Registration|46 marqueurs avec `fixed=false`, 11 sans champ explicite|Quel défaut de version s’applique aux 11 autres ?|

OptiTrack décrit des centres virtuels de genou et cheville à partir des marqueurs latéraux/médiaux. **Cette description de son propre squelette ne démontre pas que les articulations OpenSim suivent la même méthode.** Aucun milieu de paire ni centre de hanche estimé ici.

## Questions techniques pour l’expert

1. Quels sites du CSV pouvez-vous confirmer ou réfuter ? Pour chaque label : preuve, placement, repère, incertitude et distinction entre marqueur cutané et centre articulaire.
2. Les rattachements FTC, HGT, USP et DP1 sont-ils défendables pour ce squat ? Quelles limitations imposent-ils aux angles ou appuis interprétables ?
3. Les neuf mesures actives, les axes XYZ locaux et les mesures bilatérales communes suffisent-ils pour AB01 ? Quels segments non explicitement ciblés exigent un contrôle ?
4. Comment évaluer les six coordonnées verrouillées, les contraintes patellofémorales et les degrés de liberté observables avec les 49 marqueurs ?
5. Quels logs permettraient de connaître le résidu statique d’AB01, sa définition et le rôle de la registration ? Quelles régions requièrent un critère particulier ?
6. Comment confirmer la borne C3D, les repères, le signe GRF, le moment libre et le COP sans réparer les fichiers à l’aveugle ?
7. Quelle preuve de synchronisation faut-il obtenir au-delà du ratio 5:1 ? Comment résoudre la différence entre le filtrage publié et le code Git disponible ?
8. Quelles pièces permettraient de délimiter le départ, la descente, le maintien et le retour : indices officiels, vidéo autorisée du bon essai, autre preuve ?
9. Ce squat tenu, non chargé, est-il pertinent comme référence de recherche uniquement, ou pourrait-il devenir une instruction pour le public après qualification ?

## Critères proposés avant une future admission

Ces critères sont à ratifier ; ce ne sont pas des seuils scientifiques inventés :

- Versions, hashes et licences des composants nécessaires établis ; statique associé et discordance de borne C3D résolus ou précisément circonscrits.
- Tableau révisé par l’expert, sans correspondance essentielle reposant sur une hypothèse silencieuse. Les objections sont conservées, sans modifier le modèle pendant cette phase.
- Repères, unités, signes des forces, origine des moments, COP, synchronisation et filtrage suffisamment traçables.
- Dépendances modifiées et configurations effectives disponibles ; distinction entre scaling, registration et IK ; erreurs par marqueur d’AB01 examinables.
- Critères quantitatifs fixés **avant les futurs calculs**, justifiés par région, tissus mous, degré de liberté et usage. Aucun seuil choisi pour faire accepter les 4,21 cm.
- Revue de la séquence entière et des appuis. L’apparence d’un avatar ou le succès d’un export GLB ne remplace aucun de ces critères.

Même une décision A n’autoriserait que la préparation d’une phase expérimentale, **après revue professionnelle et autorisation explicite**. Aucune activation dans PARISFIT. Les tests physiques iPhone Safari/Android Chrome et la validation du futur coach demeurent des étapes séparées.

## Formulaire de contestation — vierge

Relecteur, qualification, date, conflits d’intérêts : **non renseignés**.

|Élément / label|Accord, refus ou information insuffisante|Justification et source|Conséquence sur l’admission|
|---|---|---|---|
|À compléter par le relecteur|Non examiné|Aucune|Aucune admission|

**Décision du relecteur : NON OBTENUE.** Ce dossier ne constitue ni un avis médical ni une certification scientifique.
