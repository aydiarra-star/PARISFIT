# S01 : paramètres disponibles ≠ modèle individualisé

**VALIDÉ :** extraction de la seule ligneS01 dans `participants.csv` de l’archiveSHA256épinglée. Les données des autres participants ne sont pas publiées. **EN ATTENTE DE VALIDATION HUMAINE :** mode de mesure, uncertainties et application aux axes/corps du XML.

|Paramètre S01|Valeur publiée|Nature et limite|
|---|---:|---|
|body_mass_kg|64,9kg|Masse corporelle rapportée par les auteurs ; pas mesurée parPARISFIT, instrument/incertitude non fournis|
|dumbbell_kg|11,856kg|Charge rapportée ; ne pas arrondir à une charge supposée commerciale|
|mvc_lever_arm_m|0,4317m|Bras de levierMVC, **pas longueur tibiale** ni centre articulaire|
|P1|1,07737|Facteur sans dimension, résultat de scaling/surrogate, pas largeur pelvienne mesurée|
|P2|1,08037|Facteur sans dimension ; ordre exact des axesXML non établi|
|P3|1,08637|Facteur sans dimension ; ne pas convertir en dimension sans référence et procédure|
|Fem|1,07018|Facteur de fémur, pas longueur absolue en mètres|
|Tib|1,08885|Facteur de tibia, pas longueur absolue en mètres|
|Foot|1,14237|Facteur de pied, convention isotrope/anisotrope et corps affectés non établis|

Le README nomme «six surrogate scale factors (pelvisP1-P3, femurFem, tibiaTib, footFoot)» et préciseP1-P3 le long des troisaxes du bassin. Il ne donne pas la correspondanceP1↔X/P2↔Y/P3↔Z dans le XML : **ne pas l’inventer**. La pageZenodo les présente comme facteurs du modèle mis à l’échelle ; les deux formulations sont conservées, sans conclure qu’elles suffisent à rejouerScaleTool.

La stature médiane1,73m de la population n’est **pas** la taille deS01. Aucune colonne de stature n’est présente dans le fichier inspecté. Aucune taille, largeur absolue du bassin ou longueur osseuseS01 n’est calculée ici.

## Mesuré, documenté, estimé, inconnu

- **Documenté comme données expérimentales :** masses et brasMVC ci-dessus ; traçabilité de mesure non fournie.
- **Observations optiques disponibles :** statique et trajectoires cutanées. Pas de centres articulaires mesurés. Les distances de landmarksPhase13 sont des estimations géométriques, pas anthropométrie osseuse.
- **Estimations/model parameters rapportés :** six facteurs de scaling. Pas les valeurs d’un sujet moyen ; pas des mesures directes.
- **Paramètres génériques disponibles dans XML :** masses par corps, centres de masse et tenseurs d’inertie (`original-audit.json/model/genericBodyParameters`). Leur somme de masses vaut52,8903209508kg, différente des64,9kg publiés pourS01 ; ce n’est pas une preuve de leur sujet d’origine. Ne jamais attribuer ces paramètres àS01 par défaut.
- **Inconnus :** taille individuelle, centres/axes articulaires, dimensions osseuses, largeur pelvienne anatomique, inerties individuelles, scaling des bras/tronc/mains, calcul des facteurs, régularisation et mass-adjustment du modèle, schéma de palpation et offsets de peau.

## Qu’est-ce qui est réellement indispensable ?

Pour l’**IK pure**, masse et inerties ne sont pas utilisées par le solveur cinématique ; leur absence n’est donc pas le blocage principal. La taille n’est pas universellement indispensable si un scaling par distances documentées est disponible. Les vrais blocages actuels : MarkerSet/alias anatomiques, repère transformé et géométrie individualisée/registration reproductible. Des facteurs disponibles ne remplacent pas leur mode d’application.

Pour la **dynamique inverse**, il faut ensuite des masses/inerties segmentaires individualisées selon une méthode déclarée, charge externe/position, forces et moments correctement transformés avec origine validée. Le bras de levierMVC ne remplit pas ces rôles.

**Décision : scaling exécutable NON TESTÉ ; individualisation non qualifiée.** Ne pas construire un modèleS01 en appliquant automatiquement les six nombres à tous les corps. Demander le modèlescaled ou les setups et conventions ; voir `AUTHOR-REQUEST.md`.
