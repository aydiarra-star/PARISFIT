# Audit documentaire — EN ATTENTE DE VALIDATION HUMAINE

## Corpus exact et limites de recherche

Consultation de Phase14 le27novembre2026. La conclusion «non trouvé» s'applique au corpus consulté, pas à toute documentation existante.

|Référence|Version / portée|Fait établi et limite|
|---|---|---|
|[D1 — dépôt](https://zenodo.org/records/23979972)|v1, publié2026-11-05 ; DOI10.5281/zenodo.23979972|Le déposant affirme que données et modèle ont servi à son article, décrit37landmarks,18camérasOptiTrackFLEX3,100Hz, deuxAccuGait,11adultes. Cette déclaration ne fournit pas une table CSV→MarkerSet.|
|[D2 — API originale](https://zenodo.org/api/records/23979972)|record23979972, concept23979971, revision4, modified2026-11-05T12:57:28.048468|Un ZIP128958808octets ; MD5ae51793940720bcd0877bdad8c155e82. Pas de DOI de l’article associé ni de related_identifiers identifiés dans cette réponse.|
|D3 — README dans le ZIP|SHA256cb65ee390ccde63cf876c6d27ce5583ea42bb0a8ed5b832dc921dc99acf0813f ; reproduit dans `dataset-README.md` avec fins de ligne normaliséesLF (original conservé dans JSON)|Qualifie explicitement le modèle de **generic**. Donne unités, cadence, centresXY des plates et six facteurs de scaling. Pas de diagramme de placement ou table d’alias.|
|D4 — modèle du ZIP|SHA25642eca458626f42aa1e49d5925e14ec3c16fe81324293bacece643e11319ddbd9|Nom interneLaiUhlrich2022_generic ;66marqueurs,22corps,39coordonnées (chargementPhase13). Positions des marqueurs dans leur corps local, non dans le laboratoire.|
|[D5 — dépôt amont des auteurs Uhlrich](https://github.com/stanfordnmbl/PassiveMuscleForceCalibration/tree/5244f7d32abb2399d065a741479bbe4323586b45)|commit5244f7d32abb2399d065a741479bbe4323586b45 ; LaiUhlrich2022.osim SHA256f61d844fb20c25ee0db76cd1ed7c916e53683f31926caebfeb40d62bd4dbfd37|Référence amont comparable, **pas preuve de parent direct** du fichierMichaud. README décrit la calibration des forces musculaires passives, renvoie au supplémentUhlrich2022. Pas de protocoleMichaud2026.|
|[D6 — Uhlrich etal.2022](https://www.nature.com/articles/s41598-022-13386-9)|Scientific Reports12,9842 ; DOI10.1038/s41598-022-13386-9|Étude de coordination musculaire pendant la marche. Ne certifie ni squatS01 ni placement de ses37marqueurs. Abstract consulté ; le supplément n’est pas utilisé comme preuve d’un lien inexistant avecMichaud2026.|
|[D7 — Lugrís, Pérez-Soto, Michaud, Cuadrado](https://link.springer.com/article/10.1007/s11044-023-09938-0)|publié2023-10-06, Multibody System Dynamics60,3–25(2024), §2.1 etFig1|Modèle18corps/52DOF, axesXantéropostérieur,Ymédiolatéral,Zvertical. C’est un autre modèle, non le22corps/39coordonnées du ZIP. Ne pas importer ses axes ni son placement comme certificationMichaud2026.|

### Article précis et suppléments

Titre recherché exactement : *Toward Real-Time Estimation of Muscle Force and Fatigue During Resistance Training Using a Neural Network Surrogate of OpenSim Musculotendon Kinematics*, Michaud, Katwal, Porzio, Cuadrado. Recherches titre exact, combinaison auteurs+«squat», «Florian Michaud»+«37»+«markers squat», et recherche du modèleLaiUhlrich2022. Le dépôt exact a été retrouvé ; **le texte intégral de cet article précis et ses suppléments n’ont pas été identifiés avec une référence indépendante vérifiable**. Aucun DOI d’article inventé. Les articles du même laboratoire ou sur d’autres tâches ne sont pas substitués à celui-ci. Le manifeste du ZIP est inspecté dans `original-audit.json` ; cette recherche ne doit pas être présentée comme une lecture de suppléments indisponibles.

## Origine et modifications du modèle

Crédits du XML : Rajagopal2016, Lai2017, Uhlrich2022 ; note de modification du fibre-damping de0,01 à0,1 attribuée àP.van den Bos avec référenceMillard2013. Cela décrit une lignée de modèles, pas un sujetS01.

D1 annonce symétrisation des surfaces d’enroulement gauches pour iliacus, psoas, gluteus maximus1, biceps femoris short head. La comparaison XML épinglée conserve le nombre/hash des différences textuelles de feuilles, des échantillons explicitement tronqués et les marqueurs dans `original-audit.json/upstreamComparison`. Elle ne prouve ni que ce commit est le parent direct, ni que toutes les différences sont dues àMichaud ; elle exclut les changements de commentaires et certains attributs. Ne pas convertir cette comparaison en preuve de validation des surfaces musculaires.

**Divergence à faire résoudre par les auteurs :** README/dépôt annoncent37marqueurs de laboratoire inclus ; l’inspection directe trouve66définitions, aucun nomCSV exact, et aucun marqueur attaché aux mains ni marqueur de tête correspondant auxCSV. Le fait que plusieurs définitions incluent des centres virtuels ou des clusters techniques empêche une association un-à-un naïve. Il peut manquer le bon MarkerSet, une étape d’export ou une table d’alias. Nous ne concluons pas à une erreur scientifique sans clarification.

## Relation à S01 et population

La population du dépôt comprend11adultes jeunes sains ; S01 est un code randomisé. Aucune preuve que le XML générique ait été individualisé pourS01. Le README dit le contraire : template générique. Les facteurs individuels sont des entrées possibles d’une procédure, pas sa preuve d’exécution. Le modèle n’a pas été validé ici pour le squat chargé, les membres supérieurs ou cette population. Son chargementOpenSim est seulement VALIDÉ techniquement.

## Droits et attribution

Datasetv1 CC BY4.0 : README et notice du dépôt, pas seulement licence d’article. Florian Michaud(2026), *Motion capture, ground reaction forces and knee extension strength during repeated dumbbell squats to fatigue: dataset and symmetric OpenSim model*, DOI10.5281/zenodo.23979972. Article associé cité ci-dessus avec statut de consultation limité. [LicenceCC BY4.0](https://creativecommons.org/licenses/by/4.0/). PARISFIT produit des extractions limitéesS01, matrices et analyses modifiées ; aucune approbation des auteurs. Données fournies telles quelles, sans garantie, droits de personnalité non automatiquement couverts. Pas d’autres lignes anthropométriques publiées, pas de signatures ni vidéo privée.

DépôtD5 : licenceApache2.0 (LICENSE SHA256c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4), README SHA2563deb345e561beda229f79f739c67538ccc067f2f0db5690131636f1515a5b5c3. Aucun modèle ou maillage tiers redistribué dansGit ; seules métadonnées et différences de paramètres pour audit. Toute future redistribution d’un modèle dérivé exige de conserver les notices applicables.

### AlternativeOpenCap inspectée directement

[D8 — opencap-org/opencap-core](https://github.com/opencap-org/opencap-core/tree/e5d29f12e725a2e14e6e4e85617834685f738753), commit e5d29f12e725a2e14e6e4e85617834685f738753. Trois fichiers inspectés : LaiUhlrich2022.osim (aucunMarker), MarkerSets`markers_mocap.xml` et`markers_mocap_shoulder.xml` (49marqueurs chacun). SeulC7 a un nom strictement commun avec le MarkerSet66 du dataset, et sa définition locale diffère. Ces variantes n’apportent donc pas la tableMichaud. Hashes, noms et comparaison numérique dans `opencap-comparison.json`, script `compare_opencap.py` ; licenceApache2.0 vérifiée par le même hashLICENSE queD5. Aucun remplacement ni réétiquetage exécuté.

### Résultats de l’inspection originale

VALIDÉ dans le périmètre documentaire :290fichiers au manifeste du ZIP, dont seulsREADME.md et le modèle.osim ne sont pasCSV/CSV.gz. AucunPDF, schéma de placement, setupScaleTool ou setupIK n’y est présent. Le template amontD5 ne contient aucunMarker ; la comparaison compte3651différences de feuilles textuelles, **pas3651modifications physiques** : les échantillons montrent notamment des différences d’arrondi. Ne pas attribuer toutes ces différences aux seules modifications de wrapping annoncées.
