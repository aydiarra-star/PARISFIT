# Repères et unités — audit séparé de la sémantique anatomique

|Élément|Résultat|Statut|
|---|---|---|
|TrajectoiresCSV|mètres, repère laboratoire,100Hz, time(s), selonREADME|VALIDÉ documentaire|
|ForcesCSV|N ; momentsN·m ;100Hz selonREADME|VALIDÉ documentaire|
|ModèleXML|length_units et force_units extraits sans conversion ; gravité(0,−9,80665,0) en repèreGround|VALIDÉ technique|
|Verticale du modèle|Y orienté à l’opposé de la gravité|VALIDÉ technique|
|Z du laboratoire vertical positif|Cohérent avec hauteurs et forces ; non défini explicitement dans le README complet|EN ATTENTE DE VALIDATION HUMAINE|
|X/Y laboratoire et sens positifs|NomsCSV connus ; orientation anatomique, chiralité et sens non certifiés pourS01|NON TESTÉ|
|Origine laboratoire|CentresXYplate1=(−0,698;0)m, plate2=(0;0)m documentés ; altitude de surface et origine3D non fournies|EN ATTENTE DE VALIDATION HUMAINE|
|Orientation des plates|Matrices de rotation, numéro de série/configuration, dimensions et hauteur de surface non établis|NON TESTÉ|
|Marqueurs et forces : même repère ?|README rattache les marqueurs et positions des centres au laboratoire, **mais ne donne pas la rotation des composantesF/M ni leur origine**|EN ATTENTE DE VALIDATION HUMAINE|
|Synchronisation fichiers|3350timestamps marqueurs/forces égaux, cadence effective≈100Hz|VALIDÉ numérique|
|Synchronisation physique|Trigger, latence, resampling éventuel et alignement de l’acquisition non établis|NON TESTÉ|
|Laboratoire→OpenSim|Aucune matrice ni translation documentée appliquée|NON TESTÉ|

Le texte du dépôt annonce que son README décrit le repère ; le contenu réellement fourni ne donne que l’unité laboratoire et les centresXY. Une description générique du fabricantAccuGait ne résout pas le montage ni la transformation d’export de ce laboratoire.

La publication apparentéeD7 utiliseXantéropostérieur,Ymédiolatéral,Zvertical. Elle concerne18corps/52DOF : **pas une autorité pour assigner ces axes au dataset2026**. Ne pas importer automatiquement une permutationZ→Y. La verticale seule laisse la rotation horizontale indéterminée.

## Contrat de transformation futur — aucune transformation appliquée

Pour une rotation propreR et translationt validées, p′=Rp+t, F′=RF. Pour un moment exprimé autour de l’origine source, M′ autour de l’origine cible vaut RM+t×RF (t = position de l’origine source dans la cible). Si le point de référence du moment est conservé et seulement ré-exprimé, seule la rotation s’applique. Il faut donc documenter **le point de référence**, pas seulement la matrice.

Inverse : Rᵀ et−Rᵀt. Contrôles : RᵀR=I, detR=+1, unités cohérentes, round-trip points/forces/moments, conservation des distances/normes, pesanteur, points de calibration connus. Ne pas valider un repère en minimisant uniquement les résidusIK.

`test_contracts.py` vérifie ces propriétés sur des données **synthétiques** et vérifie le refus si la provenance expérimentale manque. Aucun résultat synthétique ne vaut calibrationMichaud. Les données d’origine, temps et forces sont laissés inchangés. AucunCOP, centre articulaire ou translation compensatoire de pied n’est déduit.
