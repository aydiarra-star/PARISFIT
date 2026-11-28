# Décision Phase16 — B : documentation partielle

**EN ATTENTE DE DOCUMENTATION et EN ATTENTE DE VALIDATION HUMAINE.** Aucun jeu de données n’est admis pour produire une animation anatomiquement défendable dansPARISFIT à ce stade. Pas de scénarioA fondé sur la seule présence de fichiersOpenSim/FBX.

## Avancées établies

- DemandesFR/EN finalisées, mêmes7questions et mêmes6valeurs. **NON ENVOYÉES**, aucun contact, réponse ou accord d’auteur revendiqué. La décision d’envoi appartient à l’utilisateur.
- Michaud : preuveS01/README relue, endpointlatest toujoursv1 ; rôles généraux desfacteurs connus, axes/corps/règles exactes toujours absents. Aucunfacteur appliqué.
- Recherche centrée sur des **squats capturés**. NotreDame devient la candidateprioritaire de qualification : protocole, données et configurations repérables, licence datasetCC BY4.0. Inspection passive de5petits fichiers épinglés ;57marqueursMarkerSet,57tâchesstatic,49tâchesIK et30C3D squat dans l’arbreGit. Cescomptages ne valident pas le lien anatomique.
- LimiteNotreDame explicitement publiée : RMSscaling4,21cm enmoyenne et maxima9,82cm ; configurations avec références`Unassigned` à résoudre par le code. Pas d’admission ni d’exécution «pour voir».
- LLJ : squat réel mais populationpostopératoire, donc non retenue comme démonstrationnormative sportive. GroundLink : droitsC3D/FBX non établis malgréMIT du code. WBDS reste marche uniquement.

## Relecture technique des demandes

|QuestionFR/EN|Besoin concret|Pièce attendue / contrôle|
|---|---|---|
|1 MarkerSet/placement|Éviter de relier landmarks et centresvirtuels|Tableofficielle, sitespalpés, offsets, exclusions ; vérificationlabel parlabel|
|2 ConfigurationS01|Distinguer générique et individuel|Modèlescaled ou template/version et procédure rejouable|
|3 Sixfacteurs|Éviter application aux mauvais axes/corps|DéfinitionP1–P3/Fem/Tib/Foot, référence,isotropie,ordre, autressegments, surrogate ou scalingcomplet|
|4 Registration|Séparer géométrieosseuse et ajustementmarqueurs|Statique, fenêtre, poids, contraintes, modificationsmanuelles|
|5 Repères/acquisition|Comparer correctement données et forces|Transformationssignées/réversibles, originesF/M, calibration,synchronisation,gaps/filtre|
|6 Configurations/publication|Reproduire les calculs plutôt qu’une apparence|Setups/scripts, DOI/préprint/suppléments, paramètres et limites|
|7 Droits|Distinguer données/modèle/composants|Attribution,licences, champcommercial, notices|

Chaquequestion précise sa finalité ; aucun présupposé que le modèleS01 ou les fichiers existent. Il est explicitement possible aux auteurs de répondre qu’une pièce manque. Lesmessages ne demandent aucune donnéeprivée de participant. La version finale ne doit pas être signée au nom d’une personne inventée ; l’utilisateur choisit son expéditeur et vérifie le contactofficiel au moment d’un éventuel envoi.

## Pourquoi pas A ou C global ?

A : non, aucunessai nouveau n’a été vérifié intégralement ni admis anatomiquement. Michaud présente toujours deshypothèsesmajeures. NotreDame fournit une meilleure traçabilité mais aussi desrésidus et traitements à qualifier.

C global : non, les pièces existantes et nouvelles pistes justifient de poursuivre une qualification ; leur impossibilité définitive n’est pas démontrée. C s’applique seulement à l’usage«marcheWBDS comme squat» et à la substitutionnormative cliniqueLLJ, pas à la valeur scientifique de cesdatasets.

## Phase suivante recommandée — qualification, pas retarget

1. **Utilisateur :** décider librement d’envoyer ou non la demandebilingue ; aucune transmissionautomatique.
2. **Auditpassif ciblé :** un seul squatNotreDameAB01/prise1 et statique associé, sur commit épinglé ; vérifier droits/des noticesamont, hashes, unitésC3D, marqueurs, gaps, forces et référencesconfigurations. Ne pas déduire l’associationstatique de la seule arborescence.
3. **Professionnel :** examiner placements, registration et résidus importants ; définir critèresavantcalcul, incertitudes etDOFobservables. DossierPhase15 conservé, pas considéré validé.
4. Seulement si lesportes sont franchies : préparer uneIK courte dans unephaseultérieure autorisée, sans activation. Faible résidu ou exportGLB ne vaut pas qualitéhumaine/anatomique.

**REFUSÉ :** toutecorrection/IK/retarget sursource nonqualifiée. **NON TESTÉ :** IK,COPnouveau,retarget,admissionnouvelle. RuntimeRocketbox et8exercices préservés ; aucunavatarremplaçant, aucuneanimationactivée. Aucunachat,merge,déploiement,contactauteur.

## Reproduction et livraison

`tools/documentary-review/inspect.py` utilise uniquementGitHub enlecture pour inspecter les5fichiers du commitWeRoLab ; vérifie lesGitblobSHA1 et consigneSHA256, sans exécuter les scripts. `build.py` produitpage, auditmachine etmanifestSHA256. TestsNode : valeursS01, portesfermées, intégrité, configurationnonexécutée et hashRocketbox. Testsnavigateur :320/390/768/1200px, liens ettextesFR/EN. `npm test` conserve tous lescontrôlesantérieurs. Aucunedépendanceajoutée. Lespreuves deCI finales sont indiquées dans le compte rendu et laPR ; unPASSCI reste strictement technique.
