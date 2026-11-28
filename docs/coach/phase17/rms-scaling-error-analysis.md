# Que signifie le RMS publié de 4,21 cm ?

**Valeur rapportée par les auteurs, non calculée par PARISFIT et non attribuable à AB01/1.** La présente phase ne lance aucun scaling, aucune registration ni IK pour tenter de la reproduire.

## Déclaration primaire

Alizadeh Noghani, Green, Bolívar-Nieto (2025), DOI10.1038/s41597-025-06227-7, [section Data Processing](https://pmc.ncbi.nlm.nih.gov/articles/PMC12717423/#sec7). La section peut être retrouvée par son titre si l’ancre éditoriale change.

> “The RMS and maximum marker errors of the scaled models, obtained by running Setup_Scale_GUI.xml for each participant in OpenSim, were 4.21 ± 0.34 cm (range:3.59-4.69) and 9.82 ± 0.74 cm (range: 9.07-11.33), respectively.”

Les auteurs ajoutent qu’ils n’ont pas individualisé le setup de chaque participant pour minimiser cette erreur et qu’ils ont confirmé visuellement, dans OpenSim Visualizer, que le modèle scaled ne déviait pas de l’A-pose statique.

## Ce qui est établi et ce qui ne l’est pas

|Question|Réponse qualifiée|
|---|---|
|Type d’erreur ?|Erreur de marqueurs des modèles mis à l’échelle lors du traitement statique, pas erreur de forces ni précision de triangulation optique.|
|Population ?|Chaque participant selon le texte ; la cohorte comprend dix participants. Les chiffres synthétisent ces modèles, pas les trente prises de squat.|
|Moyenne globale ou essai ?|Résumé interparticipants. 4,21 cm n’est pas un RMS individuel d’AB01 ni du squat1. Les plages 3,59–4,69 et 9,07–11,33 sont rapportées, mais ne permettent pas de retrouver la valeur d’AB01.|
|Quels marqueurs ?|Le protocole utilise 57 marqueurs statiques. Dans le setup AB01 acquis,57 tâches de marqueurs sont actives à poids 1, dont 8 retirées ensuite en dynamique. Cela documente les candidats au calcul, **pas un log prouvant le nombre effectivement retenu pour chacun des dix modèles**.|
|Quelle formule exacte ?|En général un RMS de distance est √(Σ‖pmodèle−pmesuré‖²/N), et le maximum est le plus grand résidu. **Le texte ne précise pas ici la formule, les exclusions, la pondération, l’agrégation temporelle ou le log exact de cette statistique.** Cette formule explicative n’est pas une formule auditée de leur résultat.|
|À quel moment du scaling ?|Exécution GUI de Setup_Scale_GUI, donc chaîne comprenant ModelScaler et MarkerPlacer. Le texte ne dissocie pas le résidu avant/après la registration ; aucune attribution à une seule étape n’est faite.|
|Fenêtre AB01 ?|Le XML GUI inspecté déclare 0–7,82 s. La moyenne de l’ensemble des participants ne doit pas être remplacée par cette seule fenêtre.|
|Écart-type et maximum ?|Le texte présente moyenne±dispersion et plages, cohérent avec les statistiques de la publication. 9,82 cm est la moyenne des **maxima de marqueurs** rapportée, pas le maximum absolu du dataset ni l’erreur de tous les marqueurs. Le maximum de plage rapporté est 11,33 cm.|

## Ce que ce chiffre ne mesure pas

- Ni précision des centres articulaires ni longueur réelle des os.
- Ni erreur angulaire du genou dans le squat, ni erreur dynamique d’IK frame par frame.
- Ni erreur de COP ou de force, ni distance marqueur–os liée aux tissus mous seule.
- Ni performance d’un retargeting Rocketbox ; aucun transfert n’existe dans cette phase.
- Ni qualité du mouvement d’un coach humain ou approbation professionnelle.

Les résidus zéro dans le C3D exporté ne contredisent pas un RMS modèle de plusieurs centimètres : ce sont des champs différents avec des significations différentes. L’erreur de recalage d’un modèle n’est pas le résidu d’une observation caméra.

## Critères employés par les auteurs

Dans les sections Data Processing et Technical Validation consultées : contrôle visuel de conservation de l’A-pose ; calibration de capture qualifiée «Exceptional» ; comparaison des résultats Sit-to-Stand avec la littérature, notamment AB07. **Aucun seuil numérique d’acceptation du RMS de scaling ou du squat AB01/1 n’y est donné.** «Exceptional» désigne la calibration optique, pas la qualité anatomique du modèle. La comparaison Sit-to-Stand ne qualifie pas individuellement notre squat.

Nous n’importons pas un seuil générique de la documentation OpenSim comme s’il était un seuil appliqué par les auteurs. L’absence de seuil publié n’est pas comblée par une tolérance choisie après observation du 4,21 cm.

## Décision et questions pour l’expert

Le niveau centimétrique et les maxima rapportés sont des signaux de risque qui justifient une revue, **pas une preuve chiffrée que l’essai AB01/1 a exactement cette erreur ni une raison de modifier ses trajectoires**. Demander, sans contact effectué ici : logs par participant/marqueur, définition exacte et étape du RMS, exclusions, version du modèle et registration GUI. L’expert doit définir avant expérimentation les tolérances par région et leur lien à l’usage coach ; de faibles résidus seuls ne suffiront pas. **B, pas A.**
