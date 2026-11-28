# Sources de squats réellement capturés — revue du 27 novembre 2026

**EN ATTENTE DE VALIDATION HUMAINE. Aucune source nouvelle admise.** Cette phase examine publications, licences, inventaires et configurations, sans lancer de traitement de mouvement. Aucun C3D nouveau téléchargé ou décodé ; aucun résultat anatomique ou visuel revendiqué. WBDS v6 est exclu de la sélection squat : c’est une source de marche.

## 1 — Notre Dame / WeRoLab : priorité pour une qualification ultérieure

**Auteurs/publication :** Mohsen Alizadeh Noghani, Sebastian Green, Edgar Bolívar-Nieto, *Whole-body optical marker and ground reaction force data of healthy humans performing non-cyclic activities*, Scientific Data12,1971(2025), DOI [10.1038/s41597-025-06227-7](https://www.nature.com/articles/s41597-025-06227-7). Texte primaire consulté : [PMC12717423](https://pmc.ncbi.nlm.nih.gov/articles/PMC12717423/), sectionsParticipants, Instrumentation, Experimental Procedure et Data Processing.

**Source précise :** [dataset DOI10.7274/28689221](https://curate.nd.edu/articles/dataset/Whole-body_optical_marker_and_ground_reaction_force_data_of_healthy_humans_performing_non-cyclic_activities/28689221), page affichantversion1 ; [API du dépôt](https://api.figshare.com/v2/articles/28689221). Code associé officiellement cité : [WeRoLab](https://github.com/WeRoLab/healthy-whole-body-noncyclic-dataset/tree/a26fe4852a78f30c5e8a437b158847031cb8dc3c), commit `a26fe4852a78f30c5e8a437b158847031cb8dc3c`.

- **Mouvement réel :** descente en squat, maintien d’au moins8secondes puis retour à la posture neutre. Pas une répétition sportive chargée ni une marche renommée.
- **Participants/répétitions :**10adultes sains,14activités,3répétitions par activité. L’arbreGit non tronqué confirme30C3D de squat,3pour chacunAB01–AB10 ; pas30cycles vérifiés par lecture des signaux.
- **Matériel :**12camérasOptiTrackPrimeX22, marqueurs200Hz ;6platesKistler9260AA6, forces1000Hz. Participants en vêtements ajustés et chaussettes ; rythme naturel. Pieds droit/gauche surplates1/2 au départ selon protocole général.
- **Anatomie :**Biomech(57), Figure1,57marqueurs statiques,8de calibration retirés ensuite. Inspection réelle duMarkerSetXML :57noms ; setupScaleGUI :57tâchesmarker ; setupIKsquat :49tâches. **Cohérence de comptage, pas encore correspondance C3D/anatomie validée.** La palpation exacte, le placement individuel et les incertitudes doivent être contrôlés lors de la qualification ciblée.
- **Cinématique/cinétique :**TAK bruts et traités, C3D exportés, TRC/MOT, modèleBiomech57, configurations et résultatsIK/ID/CoM annoncés. LesC3D sont déjà labellisés, gap-filled puis filtrés6Hz ; interpolation linéaire ou pattern-based. Forces traitées ensuite20Hz, contacts20N, affectation manuelle aux pieds. Distinguer ces étapes, ne pas appeler lesC3D des trajectoires optiques entièrement brutes.
- **Repères :**Figures2/3 décrivent laboratoire et plates ; marqueurs et forces exportés dans le repèrecapture. Convention de l’article :Yvertical,Zavant,Xmédiolatéral ; sens et transformations exactes encore à vérifier sur le couplefichier/configuration. Pas de conversion effectuée.

### Avancée concrète : configurations inspectées, pas exécutées

`candidate-inspection.json` conserve les référencesGit etSHA256 calculés de5petits fichiers récupérés : MarkerSet, setupIK, setupScaleGUI, ExternalForces et scriptforces. Exemple ciblé pour une prochaine phase : `AB01/Squat/1/Data/squat_1.c3d` (4439424octets) avec `AB01/Static/1/Data/static.c3d` (2560224octets), identifiés dans l’arbre, **non téléchargés**. Leur lien statique/squat doit être confirmé par les chemins résolus du pipeline, pas seulement la proximité des dossiers.

Le setupIK référence`../generated/Generated_Model.osim`, mais`marker_file` et`time_range` sont`Unassigned`. Le setupScaleGUI a aussi des références`Unassigned`. Elles peuvent être complétées par le code : ce n’est ni un fichier prêt à exécuter tel quel, ni une preuve d’erreur des auteurs. Le scriptforces contient des affectations manuelles ; le mécanisme exact doit être vérifié sans l’exécuter à l’aveugle. Aucun code auteur n’a été lancé.

### Licence et limites

**VALIDÉ documentaire :** licence **CC BY4.0 sur le dépôt de données précis**, pas uniquement l’article. Réutilisation commerciale permise sous attribution, lien de licence et indication des changements ; pas d’endossement, droits de personnalité non automatiquement couverts. Citer auteurs, article et DOI du dataset. Les bibliothèques tierces, modèles amont, MATLAB/Motive et autres logiciels gardent leurs licences : leCC BY du dépôt n’autorise pas automatiquement tous leurs composants. Aucun achat ni redistribution de modèle/code auteur dansGit ; seules métadonnées d’audit.

**Limite majeure publiée :** erreur de scalingRMS4,21±0,34cm (3,59–4,69), maxima9,82±0,74cm (9,07–11,33). Les auteurs déclarent ne pas avoir individualisé les setups pour minimiser cette erreur et avoir contrôlé l’A-pose visuellement. Ces chiffres sont **rapportés, pas recalculés parPARISFIT**, et ne valident pas l’anatomie. La disponibilité dessetups est un progrès documentaire, pas une admission.

**Rocketbox : NON TESTÉ.** Il faudrait qualifier placements, axes, centres, modèle individualisé, incertitudes et cycle complet avant de considérer une correspondance de rig. Conserver le maintien de8secondes ; ne pas retimer pour produire un squat sportif différent.

## 2 — LifeLongJoints / Leeds : squat réel, population clinique

**Auteurs :** David Lunn, Enrico de Pieri, Graham Chapman, Stephen Ferguson, Anthony Redmond. [Article2026 DOI10.1038/s41597-026-06925-w](https://www.nature.com/articles/s41597-026-06925-w), sectionsMethods/Experimental procedures. [Dépôt primaire DOI10.5518/1701](https://archive.researchdata.leeds.ac.uk/1521/), dernière modification affichée26mars2026 ; distingue l’ancien sous-ensembleDOI10.5518/319.

- **Mouvement :** squat, un pied parplate, pieds largeurépaules, bras devant ; phasesinitiation/bas/fin annotées. Pas de charge externe documentée pour ce squat.
- **Effectif :**137patients après prothèse totale de hanche dans l’ensemble ; **102essais squat**, moyenne3essais chez les participants effectuant cette tâche. Ne pas prétendre que les137ont tous squatté ou déduire leur nombre exact de102/3. Article :3–5essais réussis visés et3–6bonsessais parADLeffectuée, décompte individuel dans table ; nombre exact de sujets squat non vérifié ici.
- **Capture :**10camérasViconMX100Hz,2platesAMTI600×400mm à1000Hz ; synchronisationMXGiganet, calibrationwand, origine au coin d’uneplate. Capture10s puis trimming aux événements.
- **Marqueurs :**protocoleCAST, clusters de cuisses/jambes/sacrum, statique lié à chaqueessai ; Figure2/Table1 de l’article pourlabels et sites anatomiques. Table détaillée non entièrement extraite ici ; aucune matrice versRocketbox. Changements de marqueurs nécessitent nouveau statique.
- **Données :**C3D/TXT avec coordonnéesm,forcesN,moments ; modèlesAnyBody associés mentionnés par les auteurs, pas modèleOpenSim autonome vérifié. Gap-fillingWoltring≤10frames ; markersfiltrés6Hz,forces/moments25Hz et miseàzéro sous5N selon publication.
- **Licence : VALIDÉ documentaire**, dépôt et fichiers déclarés **CC BY4.0**. Usagecommercial conditionnel à attribution/licence/modifications ; droits/consentement clinique et conditions des modèles/logiciels à examiner séparément. Pas d’achatAnyBody. Pas de donnéespersonnelles individuelles extraites.
- **Limite/compatibilité :**cohorte postopératoire, adaptations motrices possibles ; ne pas ériger ces squats en consigne sportive normative. Source utile pour recherchecomparative, **C pour substitution directe au coach sportif sain**, sans déclarer ses données scientifiquement invalides. Retarget NON TESTÉ.

## 3 — GroundLink : squat réel, droits des données à clarifier

**Auteurs :** Xingjian Han, Benjamin Senderling, Stanley To, Deepak Kumar, Emily Whiting, Jun Saito. SIGGRAPHAsia2023, [DOI10.1145/3610548.3618247](https://doi.org/10.1145/3610548.3618247), [préprint arXiv2310.03930v1](https://arxiv.org/html/2310.03930), §3 et tableaux. [Page officielle de téléchargement](https://csr.bu.edu/groundlink/). [Code épinglé](https://github.com/hanxingjian/GroundLink/tree/b5357ec385c9f76f5d75a83e42cedb35f9818e7f).

- **Mouvement :**squats réels parmi19types, également utilisés dans les évaluations de l’article. Charge/amplitude/durée exactes du squat à confirmer dans essais ; ne pas extrapoler le maintien20s des posesstationnaires aux squats.
- **Effectif :**7participants ;4prises de chaque mouvement,3de meilleurequalité traitées selon protocole. Datasetglobal368séquences ; ne pas confondre prises et répétitions de squat, ni affirmer21fichiers squat vérifiés sans inventaire.
- **Capture :**20camérasQualisys250Hz,96marqueurs dont10parpied ;5plates2000Hz, filtrageforces20Hz. Annotationpied/plate ; marqueursillustrésFigure3, positions détaillées annoncées en supplément mais non récupérées ici.
- **Formats :**C3D96marqueurs avecforces, FBX250fps squeletteQTM obtenu de41marqueurs, forces/CoP ; paramètresMoSh++/SMPL-X séparés, estimés et non capture directe de centres anatomiques.
- **Licence :**`LICENSE` du dépôtcode, lu au commit ci-dessus : **MIT**, copyright2024XingjianHan. La page des archivesC3D/FBX ne présente pas de licence explicite dans le contenu consulté. **Ne pas étendreMIT du code ouCC BY du préprint aux données externes. Droits commerciaux C3D/FBX EN ATTENTE DE DOCUMENTATION.** Les licencesSMPL-X/MoSh++ ne sont pas présumées permissives ; aucune utilisation de ces composants.
- **Rocketbox : NON TESTÉ.** UnFBX disponible ne valide ni les pivots anatomiques ni le transfert. Qualification légale et documentaire nécessaire avant acquisition/retarget.

## Comparaison avec l’existant et recommandation

|Source|Squat confirmé par publication|Droits dataset précis|Décision actuelle|
|---|---|---|---|
|Michaudv1|Oui, chargé,11sujets, protocole3×3×15|CC BY4.0 vérifié phases14–16|B : mapping/repères/scaling manquants|
|NotreDame/WeRoLab|Oui,10sujets×3prises, maintien≥8s|CC BY4.0 vérifié dépôt|B : priorité de qualification ciblée, erreurs de scaling importantes|
|Leeds/LLJ|Oui,102essais, cohorte137patients|CC BY4.0 vérifié dépôt|C comme remplacement sportif normatif ; recherche possible|
|GroundLink|Oui ; nombre exact de cycles non vérifié|Licence codeMIT ; archives non qualifiées|B : droits et supplément à obtenir|
|WBDSv6|Non : marche|CC BY4.0 établiPhase15|C pour besoin squat ; garder comme piste de marche|

**Priorité prochaine phase :** inspection passive d’un seul couple squat/statiqueNotreDame et de ses référencesrésolues, contrôles des unités/repères/labels/traitements et licences, puis avisprofessionnel. Pas d’IK avant ces portes. En parallèle, l’utilisateur peut décider d’envoyer la demandeMichaud ; aucun envoi effectué ici.

## Périmètre de preuve

Requête initiale : «squat motion capture dataset markers ground reaction forces C3D open dataset license» ; recherche ciblée du titreNotreDame. Fiches fondées ensuite sur les pagesprimaires ci-dessus, et non sur les seules vignettes de recherche. Dateconsultation27novembre2026. Documents tiers, dérivés et observationsPARISFIT sont distingués. Archivesvolumineuses non acquises, COPnon recalculé, aucun mouvement sélectionné pour intégration. Conserver toutes les preuves négatives des phases antérieures.
