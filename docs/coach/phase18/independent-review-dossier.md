# Dossier d’expertise indépendante — version préparatoire

**Participant AB01 · Squat / 1 · Static / 1.** Décision technique actuelle : **B, dossier encore incomplet**. Le dossier permet une revue préliminaire contradictoire ; les pièces manquantes empêchent de le présenter comme une base complète pour défendre une reconstruction.

**Aucun expert sollicité ni avis obtenu.** Les réponses doivent venir d’un professionnel identifié, compétent en biomécanique du mouvement et indépendant du résultat recherché. L’utilisateur choisira le relecteur et autorisera explicitement tout envoi.

## Protocole et provenance

Alizadeh Noghani, Green, Bolívar-Nieto, Scientific Data2025, [DOI10.1038/s41597-025-06227-7](https://pmc.ncbi.nlm.nih.gov/articles/PMC12717423/). Selon les auteurs : dix adultes sains, trois prises par activité ; squat à rythme naturel, maintien d’au moins huit secondes, retour neutre ; statique en A-pose avec57marqueurs, puis retrait de huit calibrations. Ce protocole de recherche n’est pas une certification de technique sportive.

Cas choisi enphase17 : AB01, masse49,81kg, stature1,73m documentées ; représentatif du protocole seulement, pas de toute la population. [Sélection, hashes et licence du dataset](../phase17/selected-squat-trial.md). DonnéesCC BY4.0 ; licences amont des composants à vérifier avant redistribution future. Aucun modèle tiers ou vidéo privée transféré à un expert ici.

Référence source immuable : WeRoLab commit`a26fe4852a78f30c5e8a437b158847031cb8dc3c`. [Manifest des24fichiers](../phase17/source-manifest.json), dont deuxC3D. Les fichiers binaires ne sont pas incorporés au dossierGit ; leurs chemins et commandes d’acquisition limitée sont accessibles. SHA256 identiques en phases17/18.

## Ordre de lecture conseillé

|Pièce|Ce qu’elle permet de contester|
|---|---|
|[Schéma des57marqueurs](../phase17/markerset-schematic.svg)|Inventaire par région, calibrations, ambiguïtés ; pas squelette reconstruit|
|[Points statiques mesurés](../phase17/static-marker-projections.svg)|ProjectionsXZ/YZ originales, sans centres articulaires estimés|
|[CSV de correspondances phase17](../phase17/marker-anatomical-mapping.csv)|44définitions confirmées /13plausibles, rattachements logiciels et limites|
|[Registre des57questions](anatomical-uncertainties.md)|Définition, contradiction, interprétation, conséquence et question par marqueur|
|[Scaling et IK — lecture seule](../phase17/scaling-ik-configuration-audit.md)|Neuf mesures actives, axesXYZ locaux, poids1, contraintes ;46fixed=false et11champs absents|
|[Extraits des configurations et scripts](../phase17/source-excerpts.md)|Chemins, lignes et paramètres, sans exécution|
|[Forces phase17](../phase17/ground-reaction-forces-audit.md)|Plateformes1/2 affectées aux pieds, couverture géométrique, limitesCOP et moments|
|[C3D/timing phase18](c3d-integrity-and-timing.md)|**Erratum prioritaire : en-tête brut cohérent, dépassement du lecteur expliqué**|
|[Erreur de scaling publiée](../phase17/rms-scaling-error-analysis.md)|4,21cm est un résumé des modèles statiques, pas le résidu du squatAB01|
|[Historique des rapports](historical-report-differences.md)|Différences de performance et collision d’identifiants du laboratoire ancien|
|[Questionnaire](expert-questionnaire.md)|Six décisions principales et preuves exigées|
|[Critères proposés](animation-admission-criteria.md)|Sépare données, anatomie, appuis, cinématique, transfert et perception visuelle|

## Niveaux de preuve à garder séparés

**Faits dans les fichiers :** noms et nombres de marqueurs, corps parentsOpenSim, tâches, poids, unités, octets et fréquences. Ils ne prouvent pas la palpation réelle du sujet.

**Déclarations des auteurs :** protocole, interpolation, filtres, consentement et synthèse des résidus de scaling. Ni PARISFIT ni le relecteur ne doivent transformer une déclaration globale en mesure individuelle.

**Interprétations :** certains sites pelviens, styloïdes, main etT2 ; pertinence d’un modèle de segment rigide pour peau, orteils ou épaule ; méthodes éventuelles d’estimation des centres. Elles doivent pouvoir être réfutées.

**Hypothèses non retenues :** marqueur cutané égal centre articulaire ; résiduC3D nul égal précision parfaite ; force verticale égale contact plantaire complet ; modèle chargé ou exportGLB égal qualité biomécanique ; pivotRocketbox égal articulation anatomique.

**Rectification technique établie enphase18 :** les octets de l’en-tête concordent avecPOINT:FRAMES et la taille des données. L’avertissement du lecteur ne constitue pas une preuve de frame perdue. Les anciens rapports sont conservés mais doivent être lus avec cet erratum.

## Pièces encore manquantes et responsabilité attendue

|Pièce|Pourquoi nécessaire|Qui peut la qualifier / action future|
|---|---|---|
|Versions modifiées exactes deScale/IK/osimC3D|Compléter les champsUnassigned et comprendre conversion/filtrage|Audit public ciblé de l’archive annoncée ; aucune substitution par une version choisie au hasard|
|Logs statiques individuelsAB01, définition du résidu et registration|Ne pas attribuer4,21cm à ce sujet|Auteurs/dépôt, si disponibles ; expert pour l’interprétation|
|Preuve de placement et résolution des contradictions|Rattacher les labels à l’anatomie réelle|Expert ; une image schématique générique ne suffit pas|
|Synchronisation matérielle et convention des forces/moments|Analyser temporellement les appuis et la cinétique|Spécialiste acquisition / auteur du protocole|
|Indices du maintien/retour et historique des lacunes|Vérifier complétude du cycle et sensibilité aux traitements|FichierMAT annoncé, versions de traitement et preuve autorisée|

Les questions peuvent être transmises avec ces lacunes **si l’utilisateur l’autorise**, pour un avis préliminaire. Cela ne transforme pas l’absence de pièce en validation conditionnelle acquise. Aucune dépense, aucun contact dans cette phase.
