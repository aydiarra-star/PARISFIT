"""Assemble documentary review only from preserved evidence. No biomechanical processing."""
from pathlib import Path
import csv,json,hashlib,html,re
D=Path('docs/coach/phase20');D.mkdir(exist_ok=True)
REF='25ebee0ec3161ca5415d4961bd8d04ea4404af84'
H=f'> Phase20 — 2026-11-27, date de session. Référence `{REF}`. Consultation documentaire uniquement ; aucun avis indépendant reçu.\n\n'
def put(n,t):(D/n).write_text(H+t)
claims=[
('C01','AB01/Squat/1 et Static/1 associés par le code','Établi : identité pseudonyme et chemin de référence statique','../phase17/selected-squat-trial.md ; ../phase17/source-excerpts.md (trial_class.m:L127–141)','Date de capture et identifiant de séance non établis','Association prévue par les scripts ne garantit pas chaque exécution','Pas de généralisation à tous les squats'),
('C02','Originaux C3D identifiés par SHA256','Établi : deux fichiers et leurs empreintes','../phase17/source-manifest.json ; ../phase19/preservation-check.json','Les C3D sont déjà traités, pas des captures brutes','Résidus zéro compatibles avec export après interpolation','Aucune précision anatomique déduite de la lisibilité'),
('C03','Motive 3.0.3 Final','Établi comme déclaration MANUFACTURER dans les deux fichiers','../phase19/local-and-preserved-inventory.json (c3dMetadataOnly)','Build complet et historique de correction inconnus','Champ exportateur ne décrit pas tout le pipeline','Ne pas prétendre à une reproduction exacte'),
('C04','57 marqueurs :44 définitions confirmées et13 plausibles','Qualification documentaire, pas validation de pose AB01','../phase17/marker-anatomical-mapping.csv ; ../phase18/marker-review-register.csv','Pose réelle et ambiguïtés IAS/IPS,TV2,HM2,SK,TAM','Documentation générique peut différer de la pose effective','Pas de correspondance anatomique automatique'),
('C05','57 rattachements OpenSim ne valident pas57 centres articulaires','Établi : entrées MarkerSet identiques interne/externe','../phase17/configuration-inspection.json ; ../phase17/scaling-ik-configuration-audit.md','Centres et axes individuels non prouvés','Marqueurs cutanés et centres estimés sont des objets distincts','Reconstruction bloquée sans hypothèses justifiées'),
('C06','2948 frames et erratum C3D','En-tête physique0..2947 cohérent ; lecture calculée supplémentaire du lecteur0.6.0','../phase18/c3d-independent-byte-audit.json ; ../phase18/c3d-integrity-and-timing.md','Pas de preuve de perte à acquisition ; ce test ne mesure pas qualité optique','L’ancien constat de borne erronée concernait une propriété calculée du lecteur','Ne pas ajouter ou supprimer une frame pour masquer le warning'),
('C07','Journal original mentionne AB01/Squat/1 et2948 lignes','Établi dans opensim.log SHA2563cb10df0990b5213c37ae24beead0665b1b551f40984c60277850cbad7c14ba6','../phase19/archive-probe.json (targetMentions:L13369,13555,13562,58181,58367)','Lien byte-à-byte entre ce passage et toutes les sorties publiées non établi','Journal agrégé ; noms relatifs squat_1 répétés pour autres contextes','Exécution originale ne vaut pas anatomie valide'),
('C08','Configurations scaling/IK disponibles','9 mesures actives,57 tâches statiques ;49 tâches IK dynamiques','../phase17/scaling-ik-configuration-audit.md ; ../phase17/configuration-inspection.json','Paramètres effectifs et adaptation individuelle à justifier','Setup distribué peut être générique ou différer du passage GUI','Aucun scaling ni IK autorisé par présence XML'),
('C09','4,21cm = moyenne publiée de scaling statique','RMS4.21±0.34cm sur participants, pas erreur mesurée du squat AB01','../phase17/rms-scaling-error-analysis.md ; https://pmc.ncbi.nlm.nih.gov/articles/PMC12717423/','Pas de seuil universel ; journal statique différent du résultat GUI final','Journal de placement et moyenne publiée décrivent des contextes différents','Interdit d’utiliser4.21cm comme critère dynamique AB01'),
('C10','Forces disponibles ≠ contact plantaire complet','6 plateformes,36 canaux ; charge observée plateformes1/2 dans audit conservé','../phase17/ground-reaction-forces-audit.md','Surface de contact, talon/avant-pied et affectation anatomique complète inconnus','Pied partiellement posé ou charge différente malgré force non nulle','Aucune correction de pied ni COP déduit'),
('C11','200/1000Hz ne prouve pas synchronisation physique','Ratio5 et grilles numériques vérifiés','../phase19/capture-synchronization-evidence.md ; ../phase18/c3d-integrity-and-timing.md','Trigger, horloge, latence et dérive de séance non documentés','Synchronisation externe possible sans canal trigger, ou décalage possible','Pas d’offset inventé ni fusion cinétique/kinématique certifiée'),
('C12','Aucun transfert Rocketbox validé anatomiquement','Mapping Rocketbox inconnu ; aucune admission AB01 au coach','../phase17/mapping-status.json ; ../phase18/animation-admission-criteria.md','Morphologie et axes non qualifiés','Succès technique futur resterait distinct de validité anatomique','Huit exercices et modèle actuels restent inchangés'),
('C13','Calibration et qualité individuelle incomplètes','Méthode générique décrite, logs de traitement retrouvés','../phase19/ab01-original-logs-inventory.md ; ../phase19/marker-placement-evidence.md','Logs de calibration/gaps/reprises AB01 non identifiés dans périmètre','Pièces peuvent exister dans TAK non inspectés ; absence bornée','Revue préliminaire possible, expérimentation non admise'),
('C14','Filtrage à clarifier','Article Butterworth20Hz ; code inspecté Gaussian30','../phase19/missing-evidence-register.csv (E14) ; ../phase19/archive-probe.json','Correspondance exacte des étapes non établie','Traitements différents pour finalités distinctes possibles','Ni erreur certaine ni filtre correctif inventé'),
('C15','Phases14–16 : contexte, non valeurs AB01','Les six facteurs Michaud ne sont pas transférables','../phase14/DECISION.md ; ../phase15/SCALING.md ; ../phase16/scaling-factors-audit.md','Populations et modèles distincts','Co-distribution et noms proches ne prouvent pas compatibilité','Aucune anthropométrie importée de S01'),
]
with (D/'evidence-and-claims-matrix.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['id','conclusion','etabli','preuve_precise','incertain','interpretation_alternative','consequence_animation']);w.writerows(claims)
put('expert-preliminary-dossier.md','''# Dossier d’expertise documentaire préliminaire

## Mandat et lecture conseillée

Examiner et contester la défendabilité des interprétations, **sans reconstruire le mouvement**. AB01 est le pseudonyme du participant ; Squat/1 est une répétition, Static/1 la référence prévue par le code. Ni identité civile, ni âge/sexe individuel, ni date de capture ne sont déduits. L'objectif publié est l'étude d'activités non cycliques, pas la certification d'un squat sportif.

Lire d'abord la matrice C01–C15, puis les questions prioritaires et les sources citées. Distinguer constat dans un fichier, déclaration des auteurs, interprétation documentaire et hypothèse à examiner. Le protocole publié prévoit descente, maintien ≥8s et retour naturel, trois répétitions ; la durée exacte de maintien d'AB01/1 n'est pas certifiée.

## Corpus et identification

- [Essai et association statique](../phase17/selected-squat-trial.md), avec correction de borne à lire impérativement dans l'[erratum18](../phase18/c3d-integrity-and-timing.md).
- [Manifest des24 sources](../phase17/source-manifest.json), [MarkerSet et configurations](../phase17/configuration-inspection.json), [registre57](../phase18/marker-review-register.csv), [schéma documentaire](../phase17/markerset-schematic.svg) : le schéma n'est pas une photo de placement.
- Squat C3D :4439424 octets ; SHA256 `7d4adaf1ca565de3fc172cde1b92a6b607f7a90d1f22b37453fa0cd4b6e30482`.
- Static C3D :2560224 octets ; SHA256 `ba89054b8d0bb0cb18087be68b81e1a326dcf2719c012dff73a5591102b1b4b1`.
- MarkerSet SHA256 `73a84f9f4e4d470727793603060c6478d82f3805d7d73b7d805a74fb90c36a21` ; modèle `2e815b8282df18ab5ed10b3c1434a2f1555ae38d6ef41089c52e902683973214`.
- [Inventaire logiciel](../phase19/dependency-version-inventory.md) : Motive3.0.3 Final déclaré dans les deux fichiers ; MATLAB2023b/OpenSim4.4 déclarés par l'article. Builds et certaines dépendances exactes inconnus.
- [Journaux originaux](../phase19/ab01-original-logs-inventory.md) et [extraits hashés](../phase19/archive-probe.json) : opérations AB01/Squat/1, sortie2948 lignes ; aucune nouvelle exécution.

## Synthèse contradictoire

La [matrice](evidence-and-claims-matrix.csv) relie chaque conclusion à sa preuve, ses incertitudes, une interprétation alternative et les conséquences pour une animation. Les44 définitions confirmées/13 plausibles qualifient des descriptions, non57 poses cutanées vérifiées. Les57 rattachements logiciels ne valident pas57 centres articulaires. Les huit marqueurs retirés après le statique expliquent49 labels dynamiques selon le protocole, sans prouver l'absence de gaps avant traitement.

Les4,21cm sont une moyenne publiée de scaling statique, **pas l'erreur du squat AB01**. Le journal statique mentionne aussi RMS0.0416775 et max0.0737885(LTH) dans un contexte de placement modèle ; pas un seuil ni un certificat dynamique. Les configurations scaling/IK sont des entrées disponibles, non une validation de leurs choix. Les résultats IKError.mat sont localisés, pas interprétés numériquement ici.

Les forces ne prouvent pas un contact plantaire complet ; le ratio200/1000Hz ne démontre pas la synchronisation physique. Aucun transfert vers Rocketbox n'a été validé anatomiquement. Les paramètres de séance, pose réelle, calibration individuelle et corrections de gaps restent insuffisamment tracés.

## Chronologie à ne pas confondre

Phases14–15 : limites du candidat Michaud et plan méthodologique ; pas des facteurs AB01. Phase16 : recherche et sélection Notre Dame. Phase17 : audit passif AB01, dont une attribution d'en-tête corrigée explicitement phase18. Phase18 : erratum, questions et critères d'admission. Phase19 : bibliothèques et journaux retrouvés dans les archives, malgré leur absence du Git précédemment inspecté. Aucun document antérieur n'est remplacé.

## Sources et droits

Alizadeh Noghani, Green, Bolívar-Nieto (2025), [article DOI10.1038/s41597-025-06227-7](https://pmc.ncbi.nlm.nih.gov/articles/PMC12717423/), [dataset DOI10.7274/28689221](https://doi.org/10.7274/28689221), données CC BY4.0 ([conditions](https://creativecommons.org/licenses/by/4.0/)). Code officiel épinglé `a26fe4852a78f30c5e8a437b158847031cb8dc3c`. [Guide Biomech57](https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57) : référence générique, ambiguïtés conservées. Licences MIT des outils retrouvées ; droits amont modèle/géométries à confirmer avant redistribution. Le présent texte est une synthèse PARISFIT, non un endossement par les auteurs.

Voir [questions](expert-questionnaire-final.md), [partage](external-sharing-checklist.md) et [conditions expérimentales](experimental-readiness-gates.md). Aucun fichier transmis et aucune réponse professionnelle reçue.
''')
questions=[
('Q01',1,'E08 E09','Quelles définitions de sites et ambiguïtés du guide sont défendables, et quelles preuves individuelles de pose AB01 restent indispensables ?','Fiche opérateur ou documentation autorisée liée à la séance ; argument anatomique par marqueur contesté.'),
('Q02',1,'E07','Comment évaluer les effets des gaps, interpolations et exclusions sans journal individuel complet ?','Pièces de qualité originales et limites de l’inférence ; aucun retraitement demandé.'),
('Q03',2,'E08 E09 E13','Quels centres/axes articulaires sont identifiables avec ce protocole, et lesquels ne le sont pas malgré57 rattachements OpenSim ?','Méthode anatomique justifiée, hypothèses et incertitudes ; distinguer marqueur et centre.'),
('Q04',3,'E06','La calibration générique publiée permet-elle une appréciation de cette séance, et quel rapport individuel faudrait-il ?','Critères de calibration et pièce AB01 requise.'),
('Q05',3,'E02 E03 E04 E13','Les paramètres scaling/IK et journaux disponibles suffisent-ils à comprendre le traitement individuel et ses limites ?','Justification des mesures/poids, versions exactes manquantes et association des sorties ; aucun calcul à lancer.'),
('Q06',4,'E01 E05 E10 E11','Quelle preuve de synchronisation de séance manque au-delà des versions export et du ratio200/1000Hz ?','Configuration trigger/horloges, latence/dérive ou qualification explicite de leur absence.'),
('Q07',5,'E12 E14','Comment borner l’interprétation des forces, filtres, phases et appuis sans assimiler force à contact plantaire complet ?','Conventions, affectation pieds/plateformes, séquence des filtres et preuves de contact ; pas de COP demandé.'),
('Q08',6,'E02 E03 E04 E13','Quelles pièces supplémentaires permettraient d’envisager une reconstruction défendable, distincte de la simple exécution logicielle ?','Liste priorisée de pièces et critères d’arrêt ; distinguer le journal de l’erreur dynamique.'),
('Q09',6,'E18','Quelle est la portée exacte de votre revue documentaire, et quels critères d’acceptation devraient être convenus avant expérimentation ?','Périmètre, réserves, références et niveau de certitude ; ne pas certifier une animation inexistante.'),
('Q10',7,'E15 E17','Quelles vérifications distingueraient un transfert anatomique d’un succès technique, sans utiliser l’historique mobile comme validation ?','Axes, morphologie, supports et comparaisons nécessaires ; maintien des huit exercices existants.'),
('Q11',7,'E16','Quelles restrictions de données, modèles et résultats doivent être vérifiées avant une expérimentation ou redistribution ?','Références de licences et autorisations objet par objet ; avis juridique spécialisé si nécessaire.'),
]
text='# Questionnaire final — réponses entièrement vierges\n\nLes18 entrées [E01–E18](../phase19/missing-evidence-register.csv) sont reprises par11 questions. Les questions Q03 et Q08 approfondissent centres et décision de reconstruction : Q05 porte sur la traçabilité des paramètres, Q08 sur le seuil documentaire pour envisager une étude. Les renvois multiples évitent de redemander les mêmes pièces. Priorités1 à7 selon le mandat utilisateur.\n\n'
for q,p,ids,title,proof in questions:
 text+=f'## {q} — priorité{p}\n\n**{title}**\n\nOrigines : {ids} dans le registre19. Justificatif demandé : {proof}\n\n| Validé | Validé sous conditions | Non validé | Impossible à déterminer |\n|---|---|---|---|\n| ☐ | ☐ | ☐ | ☐ |\n\nRéponse : ____________________\n\nJustificatif / références : ____________________\n\nConditions, limites, éléments contradictoires : ____________________\n\n'
text+='## Traçabilité de la revue\n\nDate : __________ ; périmètre examiné : __________ ; qualification professionnelle (sans coordonnées privées) : __________. Aucun statut présélectionné. Aucun envoi effectué.\n'
put('expert-questionnaire-final.md',text)
(D/'expert-response-template.json').write_text(json.dumps([{'id':q,'priority':p,'original_ids':ids.split(),'question':t,'answer':None,'justification':None,'conditions':None} for q,p,ids,t,proof in questions],ensure_ascii=False,indent=2)+'\n')
put('external-sharing-checklist.md','''# Dossier externe préparé — non transmis

## Version minimisée

Le dossier [external/README.md](external/README.md) contient une copie de la synthèse, de la matrice et du questionnaire, un formulaire JSON vide et des extraits factuels minimisés. Les liens scientifiques et les références du dépôt sont conservés. Les liens vers un dépôt privé éventuel ne confèrent aucun accès : une exportation autorisée des pièces nécessaires devra être organisée après accord. La consultation peut commencer par la synthèse sans exécuter de logiciel.

| Contrôle | État |
|---|---|
| Identité civile / coordonnées participant | Non incluses ; AB01 conservé comme identifiant scientifique |
| Masse de scaling49.81kg | Dans les sources techniques seulement ; utile pour revue du paramètre, pas donnée d’identification ajoutée |
| Journaux bruts et chemins de comptes locaux | Non joints ; seulement mentions minimisées AB01/Squat/1 et hashes |
| Secrets / jetons / liens signés / accès | Aucun attendu ; contrôle automatisé du dossier externe, sans certification exhaustive de sécurité |
| C3D, modèle, archives ZIP, TAK, MAT et vidéos/photos humaines | Aucun binaire joint automatiquement |
| Références et licences | Article, DOI données, CC BY4.0 et limites amont conservés |
| Autorisation d’envoyer | **Non donnée** ; aucun destinataire ni transmission |
| Autorisation de réutiliser/reproduire | À vérifier objet par objet, distincte de l’autorisation de consulter |

## Pièces utiles à une consultation, disponibilité réelle

1. Les deux C3D, MarkerSet, modèle et configurations :24 sources identifiées par chemin/hash dans le manifest17, disponibles dans le cache local, non jointes. L'expert pourra consulter les originaux officiels après contrôle des droits ; ne pas lancer le script d'acquisition automatiquement.
2. Registre57, schéma, audit de configuration, audit C3D18 : disponibles dans les documents précédents, liens épinglés dans la version externe.
3. Deux logs OpenSim : extraits disponibles dans archive-probe19 ; octets originaux vérifiés lors de lecture publique, archive brute non embarquée. Version externe limitée à la preuve utile sans chemins privés.
4. Résultats IKError.mat et figures : présence dans l'archive publique attestée, valeurs non interprétées ici. Fichier de bornes de phases localisé via API, non inspecté.
5. Rapports de calibration/placement/gaps/synchronisation de séance : non retrouvés dans le périmètre, donc **non disponibles dans ce dossier** ; ne pas confondre avec preuve d'inexistence.

Avant tout partage : autorisation explicite utilisateur, sélection des pièces, vérification des licences amont modèle/géométries et des éventuelles autorisations humaines, relecture confidentialité et vérification des hashes. Attribution aux auteurs, lien CC BY4.0 et adaptations indiquées pour les données. MIT des bibliothèques ne couvre pas automatiquement tous les modèles. Aucun achat ni demande à un auteur effectués.
''')
put('experimental-readiness-gates.md','''# Conditions avant une éventuelle expérimentation

**Tous les passages restent fermés**. Ce dossier permet une revue, pas une exécution. Les critères quantitatifs doivent être établis avec un professionnel, pas ajustés pour faire réussir le cas.

| Porte | Preuve requise / responsable de décision | État actuel |
|---|---|---|
| G1 Revue indépendante | Réponses justifiées Q01–Q11, limites et contradictions explicites ; biomécanicien | Non reçue |
| G2 Anatomie | Ambiguïtés des marqueurs clarifiées, méthode de centres/axes et incertitudes documentées ; expert | Non établi |
| G3 Calibration/scaling | Trace de calibration et justification individuelle mesures/poids/modèle/versions ; expert | Partiel, insuffisant |
| G4 Timing | Synchronisation suffisamment documentée pour l’usage envisagé, limites de latence/dérive ; expert | Non démontré physiquement |
| G5 Appuis/forces | Conventions, affectation et qualité de contact défendables ; expert | Force mesurée ne suffit pas |
| G6 Acceptation | Seuils contextualisés, critères d’arrêt, comparaison source/résultat, incertitudes et qualité visuelle ; professionnel | Non définis |
| G7 Droits | Données, modèles, résultats et redistribution autorisés objet par objet ; responsable droits | Partiel |
| G8 Autorisation et isolement | Accord explicite utilisateur pour nouvelle phase ; espace expérimental distinct, aucun branchement au coach | Non donné |

Une éventuelle phase expérimentale doit préserver les sources, versions, hypothèses, résultats négatifs et comparaisons sans corrections cachées. Elle doit rester isolée du runtime, de Rocketbox et des huit exercices actuels jusqu'à une admission séparée. Les tests physiques iPhone Safari/Android Chrome et l'avis professionnel demeurent des exigences produit distinctes. Aucun scaling, IK, retargeting, COP, correction ni nouvelle animation dans cette phase.
''')
put('ci-final-status.md','''# CI phase19 — état final de la référence exacte

Source : [réponse API archivée](ci-reference-runs.json), recherche `actions/runs?head_sha=25ebee0ec3161ca5415d4961bd8d04ea4404af84`, total_count=2. Deux exécutions, une tentative chacune ; aucun autre run annoncé par cette requête au contrôle. Ne pas substituer les runs des commits antérieurs ni ceux de phase20.

| Run | Résultat final | Jobs |
|---|---|---|
| [46118842443 — validation du socle](https://github.com/aydiarra-star/PARISFIT/actions/runs/46118842443) | completed / success | validate : success ; blender-control, source-qualification, michaud-qualification, model-qualification : skipped |
| [46118842425 — passive evidence only](https://github.com/aydiarra-star/PARISFIT/actions/runs/46118842425) | completed / success | public-archive-metadata : success |

Aucun job échoué, annulé, en attente ou en cours sur ces runs. Les étapes conditionnelles de diagnostic d'échec sont sautées normalement ; les états par étape sont dans le JSON. **Skipped n'est pas PASS** des traitements bloqués.

## Journaux réellement accessibles

Métadonnées jobs/étapes et annotations check-runs consultées, fichiers `annotations-*.json` dans ce dossier. Annotations du probe renvoient aux preuves archivées19 ; payloads encodés non dupliqués. Le téléchargement `gh run view 46118842443 --log` échoue avec EOF sur le service de logs GitHub : journal intégral non lu. URL signée et paramètres d'accès volontairement non conservés. Les conclusions success viennent de l'API GitHub, non d'une lecture exhaustive inventée du log.

## Intégrité du verrouillage

[Diff exact71bae7d→25ebee0](authoring-guard.diff) : ajout d'un input booléen false par défaut et d'une garde au niveau de chacun des4 jobs, aucune assertion supprimée ni modifiée. Condition : événement `workflow_dispatch` **et** `inputs.legacy_authoring == true`. PR/push, dispatch sans input ou avec false n'exécutent pas ces jobs. Les4 skips observés confirment le comportement sur cette PR. Un dispatch explicitement true peut toujours les lancer : ce n'est pas une interdiction technique universelle, et aucune telle autorisation n'est donnée ici.

Le job validate est inchangé : chaînes `&&`, `set -o pipefail` avant tee et absence de `continue-on-error` conservent la propagation des échecs. Les diagnostics `if: failure()` n'altèrent pas le résultat. Aucun échec connu n'a été reclassé en succès par suppression d'assertion.

## Nature des contrôles et anomalie de couverture

- Probe public : lecture d'index ZIP et de textes, CRC/hash, aucun code acquis exécuté. **Limite** : son script capture certaines erreurs dans le JSON sans toujours sortir en échec ; success du job seul ne garantit donc pas le succès d'acquisition. Le JSON19 vérifié ne contient aucune erreur ; cette réserve reste explicite.
- Validate : syntaxe/contrats documentaires et fixtures ; navigateur exécutant le runtime/animations existants et générant des rapports, pas une reconstruction source ou un export Blender. Ce n'est donc pas entièrement de la lecture passive, mais cela ne lance pas les traitements biomécaniques interdits.
- Jobs bloqués : Blender retarget/export/biomécanique, acquisition/analyse de sources et sondes modèle. `model-qualification` comprend aussi des contrôles passifs : le verrouillage large a donc **réduit la couverture automatique**, même si leurs assertions sont intactes.
- Correction minimale phase20 : workflow séparé `preliminary-review.yml`, quatre suites de contrats existantes(28 tests) sur documents/fixtures synthétiques, sans acquire/analyze main ni Blender/OpenSim. Ajout du contrôle documentaire phase20. Aucun job historique réactivé, aucun seuil changé. Les entrées `main()` des modules importés ne sont pas exécutées par ces tests.

Correction minimale proposée pour le probe réseau (non appliquée ici, aucun nouveau téléchargement requis) : ajouter après son exécution une assertion sur l'absence de `error` global/par archive dans le JSON, afin qu'un HTTP en échec fasse échouer le job. Le nouveau test documentaire20 vérifie cette propriété sur la preuve19 conservée ; il ne remplace pas ce contrôle réseau futur.

Le résultat des tests de cette correction est distinct du succès historique25ebee0 ; voir [vérifications20](verification.json). Pas de relance historique pour fabriquer une preuve manquante.
''')
put('decision-report.md','''# Décision Phase20 : **A — dossier préliminaire prêt à être soumis à un expert**

A signifie **organisation et intelligibilité pour une revue documentaire**, pas validation biomécanique, ni autorisation d'expérimenter ou produire une animation. La décisionB de phase19 concernait le niveau d'expertise possible ; les lettres n'ont pas le même sens entre les deux phases.

Les deux CI de25ebee0 sont terminées avec succès ; quatre jobs authoring sont skipped et non prétendument validés. Les logs intégraux n'ont pas pu être téléchargés ; états par étape et annotations consultés. Les assertions historiques sont inchangées, mais une couverture passive était aussi bloquée : workflow indépendant ajouté, sans acquisition ni pipeline. Voir le [rapport CI](ci-final-status.md).

Sept documents livrés, matrice15 conclusions contradictoires, questionnaire11 questions couvrant les18 entrées19 et formulaire sans réponses. Synthèse fondée sur les sources figées14–19 : C3D hashés, MarkerSet/registre57, configurations, erratum18, versions déclarées, journaux originaux et limites de séance. Dossier externe minimisé préparé localement, sans archives binaires ni transmission.

Les lacunes de pose/calibration/timing et d'identification des centres restent substantielles mais n'empêchent pas de les examiner et contester. Elles excluent une admission anatomique et une expérimentation immédiate ; elles ne démontrent pas une source irrémédiablement inexploitable(C). L'optionB « revue inutile faute de pièces » n'est pas retenue compte tenu du corpus traçable et des questions explicites.

Prochaine étape recommandée : **demander à l'utilisateur l'autorisation de soumission** du dossier minimisé après contrôle des pièces et droits. Aucun expert contacté ; aucune réponse reçue. Les portes expérimentales restent fermées. PR11 reste draft, sans merge ni déploiement ; aucune modification runtime/Rocketbox/animation.

Accès : [dossier](expert-preliminary-dossier.md), [matrice](evidence-and-claims-matrix.csv), [questions](expert-questionnaire-final.md), [partage](external-sharing-checklist.md), [portes](experimental-readiness-gates.md), [page de synthèse](index.html).
''')
# External copy with immutable links to earlier sources, no raw archive/log payloads.
E=D/'external';E.mkdir(exist_ok=True)
base='https://github.com/aydiarra-star/PARISFIT/blob/'+REF+'/docs/coach/'
for n in ['expert-preliminary-dossier.md','evidence-and-claims-matrix.csv','expert-questionnaire-final.md','expert-response-template.json']:
 s=(D/n).read_text();s=re.sub(r'\.\./(phase\d+/[^\s;)]+)',lambda m:base+m[1],s)
 # phase20 references in the dossier not copied into external remain explained in its README
 s=s.replace('(external-sharing-checklist.md)','(README.md)').replace('(experimental-readiness-gates.md)','(README.md)')
 (E/n).write_text(s)
(E/'README.md').write_text('''# PARISFIT — consultation préliminaire, non transmis

Commencer par [le dossier](expert-preliminary-dossier.md), puis [la matrice](evidence-and-claims-matrix.csv) et [le questionnaire](expert-questionnaire-final.md). Formulaire JSON vierge inclus. Les liens aux preuves antérieures sont épinglés au commit25ebee0 ; accès GitHub éventuellement à autoriser séparément, sans transmettre de jeton.

Aucun C3D, modèle, TAK, MAT, photographie ou journal brut joint. Sources à consulter : manifest17 (chemins/hashes), registres57, audit configuration17, erratum18, inventaires19. Les fichiers binaires sont disponibles chez les auteurs ou dans le cache interne, pas dans ce paquet. Calibration individuelle, pose et timing non démontrés. Aucun centre articulaire ou transfert Rocketbox validé.

Données des auteurs : DOI10.7274/28689221, CC BY4.0, attribution Mohsen Alizadeh Noghani, Sebastian Green, Edgar Bolívar-Nieto. Article DOI10.1038/s41597-025-06227-7. Synthèse et sélection des extraits : PARISFIT ; ne pas attribuer nos interprétations aux auteurs. Licences amont des modèles/géométries à vérifier ; licences MIT des outils ne constituent pas une autorisation universelle. Pas de redistribution automatique des sources.

Aucune transmission autorisée à ce stade. Les expériences restent interdites avant revue indépendante, anatomie/centres clarifiés, scaling justifié, timing et appuis documentés, critères convenus, droits vérifiés et autorisation utilisateur. Une éventuelle expérimentation devra rester isolée du coach actuel.
''')
(E/'minimal-evidence.json').write_text(json.dumps({'reference':REF,'manufacturer':'Motive 3.0.3 Final (declared in both C3D files)','originalLogSHA256':'3cb10df0990b5213c37ae24beead0665b1b551f40984c60277850cbad7c14ba6','excerpts':[{'line':13369,'summary':'Model path AB01/Squat/1/generated/Generated_Model.osim; original processing log'},{'line':13555,'summary':'squat_1_IKOut.mot: nr=2948 nc=43'}],'redaction':'Summaries omit Windows profiles, drive paths and unrelated trials; not verbatim original log','anatomicallyValidated':False},ensure_ascii=False,indent=2)+'\n')
(E/'manifest.json').write_text(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(E.iterdir()) if p.name!='manifest.json'},indent=2)+'\n')
links=[('ci-final-status.md','01 · CI finale'),('expert-preliminary-dossier.md','02 · Dossier scientifique'),('evidence-and-claims-matrix.csv','03 · Matrice contradictoire'),('expert-questionnaire-final.md','04 · Questions et réponses vierges'),('external-sharing-checklist.md','05 · Confidentialité et partage'),('experimental-readiness-gates.md','06 · Conditions expérimentales'),('decision-report.md','07 · Décision'),('external/README.md','Version externe — non transmise')]
(D/'index.html').write_text('''<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PARISFIT · Expertise préliminaire</title><style>body{margin:0;background:#f3f7f4;color:#173d32;font:17px/1.65 system-ui}main{max-width:960px;margin:auto;padding:32px 20px}small{letter-spacing:.15em}h1{font-size:clamp(30px,5vw,52px);line-height:1.15}nav{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));gap:14px}a{color:#145744;overflow-wrap:anywhere}nav a{background:white;padding:22px;border:1px solid #cadbd2;border-radius:12px;text-decoration:none}aside{border-left:5px solid coral;padding:16px;background:#fff}footer{margin-top:32px;font-size:14px}</style><main><small>PARISFIT / PHASE20</small><h1>Une revue documentaire.<br>Pas une validation du mouvement.</h1><p>AB01 · Squat / 1 · Référence Static / 1</p><aside><strong>A — dossier préliminaire prêt à être soumis à un expert.</strong><br>Aucun envoi effectué. Aucune expérimentation autorisée.</aside><p>Deux CI de25ebee0 terminées avec succès. Quatre jobs d’authoring volontairement skipped. Logs complets inaccessibles ; états détaillés et annotations consultés.</p><nav>'''+''.join(f'<a href="{n}">{t}</a>' for n,t in links)+'''</nav><h2>Points de vigilance</h2><p>44 définitions confirmées /13 plausibles ne prouvent pas la pose réelle. 57 rattachements ne valident pas57 centres. 4,21cm n’est pas l’erreur du squat AB01. Forces ≠ contact complet ; ratio200/1000Hz ≠ synchronisation physique.</p><h2>Preuves originales</h2><p>'''+ ' · '.join(f'<a href="../phase{p}/index.html">Phase{p}</a>' for p in range(14,19))+''' · <a href="../phase19/decision-report.md">Phase19</a> · <a href="../phase17/source-manifest.json">Manifest sources</a> · <a href="../phase18/c3d-integrity-and-timing.md">Erratum C3D</a> · <a href="../phase19/archive-probe.json">Journaux originaux</a></p><footer>Référence25ebee0 · PR11 brouillon · Aucun changement du coach, de Rocketbox ou des huit exercices.</footer></main></html>''')
if __name__=='__main__':print('Documentary dossier assembled; no source pipeline executed')
