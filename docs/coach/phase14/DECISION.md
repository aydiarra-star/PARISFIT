# Décision — scénario C

**REFUSÉ : utilisation actuelle du modèle fourni pour reconstruire rigoureusement S01/P001.**
**NON TESTÉ : IK, résidusIK, anglesIK, trajectoires reconstruites anatomiques, retargetRocketbox.**

Ce refus est documentaire, **pas une démonstration d’incompatibilité biologique du modèle**. Des correspondances plausibles ne constituent pas des correspondances partielles documentées. Le scénarioB exigerait au moins un sous-ensemble réellement confirmé ; ici zéro paire n’est confirmée. Le scénarioA ne découle pas du chargement du XML.

## Obstacles qui ferment la porte

1. MarkerSet37 et protocole de palpation non retrouvés ; divergence37annoncés/66XML. Aucune table d’alias autorisée par les auteurs. Les candidats régionaux explicitement incompatibles (trochanter/HJC, olécrâne/EJC, tubérosité/plateau) restent bloqués.
2. Transformation laboratoire→modèle non documentée ; repèreF/M et origine des moments non qualifiés. Aucune permutation automatique pour faire coïncider les verticales.
3. Statique et paramètresS01 disponibles, mais procédureScaleTool/registration, attribution des facteurs aux corps/axes, réglage de masses/inerties et modèle individualisé non établis.
4. Les mains, la tête et certaines rotations segmentaires ne sont pas observables avec ce MarkerSet tel quel. Aucun rang de JacobienneIK n’a été mesuré ; sous-détermination quantitative NON TESTÉE. Même un futur sous-ensemble inférieur ne valide pas les39coordonnées.

## Meilleure voie : récupérer le modèle effectivement utilisé

Demander au déposant une version corrigée/complétée du dépôt avec le **MarkerSet de37points**, tableCSV↔XML, schéma de palpation, définition des axes, transformationF/M, modèleS01scaled, setupScaleTool et setupIK. Une réponse publique versionnée, associée au DOI du dataset, est préférable à un échange non traçable. Le brouillon `AUTHOR-REQUEST.md` est préparé, **non envoyé**.

Recherche d’alternative réalisée : template amontLaiUhlrich2022 du dépôt des auteursUhlrich, et modèle18corps/52DOF deLugrís2023/2024. Le premier ne contient pas le protocoleMichaud ; le second décrit une autre architecture et ne certifie pas ce dataset. **Aucun modèle de remplacement admis.** Substituer un autre modèle générique ou OpenCap ne résout pas la correspondance expérimentale. Un nouveau protocole de capture autorisé et documenté est la voie de repli si les informations originales ne peuvent être obtenues.

## Protocole conditionnel, non exécuté

Après confirmation documentaire uniquement :
- Épingler les versions de modèle, MarkerSet, transformations et outils ; vérifier les unités, la réversibilité et des points de calibration indépendants.
- Reproduire scaling/registration sur le statiqueS01, conserver paramètres, facteurs par axe, erreurs par marqueur et revue indépendante. Distinguer centré anatomique estimé et landmark observé.
- Choisir avant calcul une fenêtre courte à partir de l’annotation, par exemple rep1 autour du bas ; publier exactement t_start/t_end, poids des marqueurs, contraintes, coordonnées verrouillées, tolérances, fréquence et filtre éventuel. Ne pas sélectionner la fenêtre au meilleur résidu.
- Résidus pour **chaque** marqueur, trajectoires avant/après, limites et continuité angulaires, Jacobienne/rang et sensibilité desDOF. Définir les critères avant mesure avec un spécialiste, pas après pour passer.
- Comparer aux appuis des plates indépendamment ; aucune force ne corrige artificiellement la géométrie. Faible résidu≠vérité anatomique. Pas deCOP tant que conventions insuffisantes.
- Conserver les échecs et incertitudes ; aucun résultat destiné au coach avant admission distincte. AucunGLB à ce stade.

**Conclusion : non, les informations anatomiques et expérimentales ne suffisent pas aujourd’hui pour relier rigoureusement S01/P001 à ce modèle.**
