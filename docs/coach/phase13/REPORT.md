# Phase13 — qualification conditionnelle, aucun squelette anatomique admis

## Réponses aux trois questions

1. **Les données sont-elles assez fiables pour reconstruire le mouvement humain ?** **EN ATTENTE DE VALIDATION HUMAINE.** Les fichiers sont cohérents numériquement, les forces restent chargées et descente/bas/remontée sont observables. Mais visibilité des marqueurs, filtrage/gap-filling amont, métrologie des plates, repères et registration anatomique ne sont pas établis. Cela permet des diagnostics, pas une reconstruction anatomique certifiée.
2. **Peut-on établir un squelette biomécanique cohérent ?** **EN ATTENTE DE VALIDATION HUMAINE ; H0/H1/H2 REFUSÉS comme squelettes anatomiques.** Les chaînes de surface sont reconstructibles. Les contraintes de longueur ne transforment pas les marqueurs en centres articulaires. Le modèle générique reconnu existe, mais son association aux données et son individualisation ne sont pas qualifiées.
3. **Peut-on transférer vers Rocketbox sans dégradation significative ?** **NON TESTÉ.** La porte de retargeting reste fermée faute de centres/axes qualifiés. Aucun nouveau GLB, aucune animation candidate, aucune activation.

## Résultats principaux

-37marqueurs,3350samples dansP001 ;150samples100Hz pour la répétition1, sélectionnée par l'annotation du déposant10,45–11,94s (bas11,08s), pas par optimisation d'un score.
- La descente du proxy de bassin est monotone jusqu'au bas annoté ; la remontée est monotone ensuite. Son minimum coïncide avec11,08s.
- Début : vitesse verticale du proxy bassin−0,3675m/s. **Pas de position initiale immobile enregistrée avant ce cycle.** Fin :+0,022m/s ; la répétition suivante débute à11,94s. **Pas de stabilisation finale certifiée.** Aucune pause synthétique ajoutée.
- Distance des landmarks de cuisse H0 : droite333,18–413,69mm, gauche327,99–409,90mm. Cela ne représente pas un fémur qui raccourcit : les points sont cutanés et leur relation au segment/anatomie reste à qualifier. Tissus mous, placement, étiquetage ou reconstruction optique peuvent contribuer ; aucune cause unique attribuée.

| Hypothèse | Résidu RMS face aux landmarks hanche/genou/cheville observés | Maximum | Conclusion |
|---|---:|---:|---|
| H0 — landmarks cutanés |0mm par définition|0mm|REFUSÉ comme centres articulaires |
| H1 — directions observées, longueurs statiques fixes |46,54mm|89,24mm|REFUSÉ ; longueurs constantes imposées, pas validées |
| H2 — pelvis rigide, trochanters virtuels et longueurs fixes |86,84mm|155,17mm|REFUSÉ ; hypothèse de rattachement du trochanter au pelvis non anatomiquement justifiée |

Fit de la constellation pelvienne : RMS2,110mm, maximum par frame3,700mm. **Un bon fit de cette constellation n'identifie pas les centres de hanche**, et ne justifie pas d'attacher le trochanter au pelvis. La comparaison montre justement comment une contrainte propre peut produire une mauvaise reconstruction des membres.

Sensibilité du genou droit à18scénarios de décalage fixe d'un endpoint : maximum2,771° pour10mm,5,555° pour20mm. Ce sont des scénarios hypothétiques, pas une incertitude clinique mesurée ni des intervalles de confiance.

## Angles et dynamique

Angles3points de genou proxy : droite8,80–102,96°, gauche11,04–101,28° ; asymétrie maximale≈3,04°. H1/H2 conservent ces directions par construction : leurs angles similaires ne sont pas trois validations indépendantes. Inclinaison3D du proxy tronc4,78–38,20°. Le proxy tronc/cuisse ne doit pas être appelé flexion de hanche anatomique.

Rapports complets : extrema, longueurs, vitesses/accélérations par point virtuel, dérivées angulaires et marqueurs complets. Pas de lissage, de projection au sol, de retiming ou d'utilisation des forces pour corriger les positions. Variations de seconde différence et SD statique ne sont pas confondues avec le bruit du capteur.

## Forces et phases

Les12composantes F/M sont auditées. Timestamps alignés numériquement ; pas de validation du trigger matériel. Les deux plates sont chargées à10/20/50/100N sur tout le cycle. Fz1 représente45,67–57,06% du total, moyenne50,74%. Ce partage ne certifie pas une symétrie sportive.

La proximité pied/centre de plate est cohérente avec l'affectation supposée, sans remplacer la calibration. La corrélation exploratoire proxy bassin/Fz n'est pas une mesure fiable de retard d'acquisition ; aucun décalage appliqué. **COP non calculé** faute de conventions suffisantes des moments et de la surface. Voir [audit des plates](FORCE-AUDIT.md).

## Modèle reconnu : obstacle concret de registration

Le déposant décrit LaiUhlrich2022_symmetric et37marqueurs. L'inspection du fichier épinglé trouve **22corps et66marqueurs de modèle**, dont des marqueurs virtuels de centres articulaires. **Zéro nom strictement commun avec les37labels CSV.** Cela ne prouve pas une erreur du déposant : des alias/attachements spécifiques peuvent exister dans sa chaîne, mais ils ne sont pas établis ici.

Ne pas renommer automatiquement un point cutané enRHJC/RKJC/RAJC. Des correspondances nominales plausibles (ASIC/RASI, épicondyle/RLFC…) ne sont pas une registration validée. Un test indépendant de chargement du template dans OpenSim est consigné dans `model-probe.json` ; **chargement ≠ scaling/IK du sujet**. Aucun résultat d'InverseKinematicsTool, aucune localisation anatomique de centres ni simulation dynamique inverse n'est revendiqué.

Voir [méthodes, hypothèses et limites](RECONSTRUCTION.md). Le logiciel gratuit OpenSim est testé dans un environnement isolé ; aucune modification de dépendances ou du runtime PARISFIT.

## Preuves et limites de revue

Trois petits MP4,3vues et traces de forces,150frames chacun ; PNG au bas. Gris=marqueurs, corail=hypothèse de chaîne. Vidéos décodées complètement puis testées en lecture navigateur. Un PNG H1 a été effectivement ouvert pour examiner la lisibilité et le décalage marqueur/chaîne ; aucune revue biomécanique professionnelle ou intégrale des vidéos revendiquée.

`review-data.json` contient le sous-ensemble public et le statique médian nécessaires à reproduire les petits rendus ; données d'affichage arrondies à6décimales en mètres, calculs de rapports sur les CSV sans cet arrondi. Les fichiers lourds restent dans l'artifactCI `phase13-michaud-qualification`. Pas de signatures, démographie ou vidéos privées publiées. Attribution CC BY4.0 dans [RIGHTS-AND-DATA.md](RIGHTS-AND-DATA.md).

## Blocages précis et prochaine action utile

- Obtenir/qualifier la table originale37marqueurs→attachements du modèle, ses axes et le modèle individualisé/scaling, plutôt qu'inventer des centres médiaux.
- Confirmer les repères et conventions des plates, données de zéro/calibration et synchronisation matérielle pour toute interprétation dynamique/COP.
- Obtenir l'historique de visibilité/reconstruction/gap-filling et la qualité des placements ; absence deNaN n'est pas absence d'occlusion.
- Analyser un enregistrement qui inclut préparation et stabilisation si ces phases sont requises pour le coach ; ne pas coller l'essai statique au cycle.
- Revue d'un professionnel qualifié, traçable et distincte des tests de transport.

**Runtime, Rocketbox et huit exercices préservés. PR11 brouillon, aucun achat, fusion, activation ou déploiement.**
