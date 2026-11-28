# Dossier de revue professionnelle — NON VALIDÉ

**EN ATTENTE DE VALIDATION HUMAINE.** Prêt pour transmission après décision de l’utilisateur ; aucune transmission ni approbation professionnelle obtenue. Destinataire recherché : biomécanicien maîtrisant capture optique, calibration anatomique, cinématique inverse et forces, ou professionnel qualifié disposant de ces compétences. Le dossier ne certifie pas l’exécution sportive.

## 1. Objet et décisions demandées

Décider siS01/P001 permet une reconstruction anatomique suffisamment documentée pour un futur coach3D ; distinguer validité scientifique, qualité visuelle, sécurité d’usage et droits. Ne pas juger sur la seule réussiteOpenSim ou la faible erreur de markers.

## 2. Paquet de preuves à examiner

- [Provenance/documentation](../phase14/DOCUMENTATION.md), archiveSHA256901112330ed234ad97ce24cb866bd5e7e33bef766861d21264953b3ac1875782, modèle42eca458626f42aa1e49d5925e14ec3c16fe81324293bacece643e11319ddbd9.
- [Matrice37×66](../phase14/matrix-37x66.csv), [justifications détaillées](../phase14/correspondences.json) :0confirmée/12plausibles/18ambiguës/7sans correspondance identifiée. Aucun point admis pourIK.
- [ParamètresS01](../phase14/anthropometry.json) : masse64,9kg, haltère11,856kg, brasMVC0,4317m ; [six facteurs audités](scaling-audit.json). Aucun centre ou dimension osseuse inventé.
- [Forces complètes et15répétitions](../phase14/force-audit.json), [interprétation](../phase14/FORCES.md) :3350samples,100Hz, timestamps alignés numériquement. Fz1=237,8965–554,7300N ; Fz2=206,5068–528,6187N ; pas de déchargement aux seuils10/20/50/100N. Repères et synchronisation physique non qualifiés, COPNON TESTÉ.
- [Rendus/analysesPhase13](../phase13/index.html) : chaînesH0/H1/H2 diagnostiques refusées comme anatomie, pas avatars candidats. H1/H2 résidusRMS46,5/86,8mm ; aucun score ne les admet.
- [Observabilité technique](observability.json) et [plan indépendant](INDEPENDENT-PLAN.md), incertitudes distinctes de défauts constatés.
- [DemandeFR](AUTHOR-REQUEST-FR.md)/[EN](AUTHOR-REQUEST-EN.md), [inventaire documentaire](INVENTORY.md), [alternativeWBDS](ALTERNATIVES.md).

## 3. Questions scientifiques ouvertes

Les labelsASIC/sacral_crest désignent-ils exactement les points nécessaires à la définition anatomique choisie ? Quel protocole de centres hanche/genou/cheville ? Quel rôle et traitement des points de main/tête absents duMarkerSet ? Quelle relation des facteurs au modèleS01 ? Quelles rotations restent sous-déterminées ? Quel biais des tissus mous est acceptable pour le domaine coach ? Les forces sont-elles dans le même repère que les trajectoires ? Quelle préparation/récupération réelle manque à ce cycle cropé ?

## 4. Critères d’acceptation à fixer AVANT une IK

|Porte|Preuve exigée|État actuel|
|---|---|---|
|Droits/provenance|Source/version exacte, droit d’usage prévu et notices conservées|VALIDÉ pour intégrité et licence dataset ; revue globale humaine en attente|
|Anatomie|Chaque marqueur utilisé : protocole, côté, corps, typecutané/virtuel, offset et source ; ambiguïtés résolues|EN ATTENTE DE DOCUMENTATION|
|Repères|Unités, axes signés, transformationsréversibles, originesF/M et tests de calibration indépendants|EN ATTENTE DE DOCUMENTATION|
|Individualisation|Scaling/registration rejouables, hypothèses justifiées, paramètres et géométrieS01 vérifiés|EN ATTENTE DE DOCUMENTATION|
|Identifiabilité|DOF retenus et rang/sensibilité documentés ; DOF non observables exclus ou explicitement contraints|NON TESTÉ anatomiquement|
|Validation numérique|Résidus par marqueur et par phase, percentiles/max, angles/limites/continuité, tests hors fenêtre de calibration, perturbations de placement et filtre|NON TESTÉ pourIK|
|Validation physique|Cohérence des appuis sans correction artificielle ; séparation mesuré/estimé ; début/fin réels|EN ATTENTE DE VALIDATION HUMAINE|
|Revue|Examen de séquences complètes multivues, traçabilité du relecteur, réserves et périmètre d’acceptation|NON TESTÉ|

Aucun seuil universel«2cm» ou angle toléré n’est adopté pour obtenir unPASS. Le spécialiste doit définir des limites numériques **avant calcul**, selon placement, précision instrumentale, tâche et usage, ainsi que la méthode pour les vérifier. Un faible résidu marqueur n’est pas une preuve anatomique. Les calculs de forces articulaires exigeraient en plus paramètres inertiels et forces externes qualifiés ; ne pas imposer ces derniers comme prérequis artificiels de l’IK pure.

## 5. Fiche de décision à remplir

Relecteur/qualification : **non renseignés**. Date : **non renseignée**. Version du paquet : voirmanifest.json. Source/DOF/tâche admis : **aucun**. Critères préenregistrés : **à définir**. Résultat : accepter sous réserves / demandercompléments / refuser, avec justification et limites. Signature/accord : **absent**. Ne pas publier d’information personnelle du relecteur sans accord.

Même une revue scientifique positive n’autoriserait pas automatiquement l’intégrationRocketbox : testsretarget, revue visuelle humaine et tests sur appareils physiques restent des étapes distinctes.
