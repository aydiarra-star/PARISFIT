# Données et droits — qualification de périmètre, pas avis juridique

**VALIDÉ :** provenance et intégrité du sous-ensemble public épinglé. **EN ATTENTE DE VALIDATION HUMAINE :** adéquation biomécanique et interprétation des repères. Aucune signature, vidéo privée ou table démographique extraite.

## Licence du dataset, pas seulement de l'article

Source primaire consultée : https://zenodo.org/records/23979972 , versionv1 publiée le5novembre2026. Le dépôt indique explicitement CC BY4.0 dans la description du dataset. Le **README inclus dans l'archive** porte également : «This dataset is distributed under the Creative Commons Attribution4.0 International license». Son SHA256 est `cb65ee390ccde63cf876c6d27ce5583ea42bb0a8ed5b832dc921dc99acf0813f`. Les fichiers précis sont extraits de cette même archive, sans exception signalée pour ces CSV ; hashes détaillés dans `provenance.json`.

Archive SHA256 `901112330ed234ad97ce24cb866bd5e7e33bef766861d21264953b3ac1875782` ; MD5 publié `ae51793940720bcd0877bdad8c155e82`. Extraction limitée à `S01/P001_markers.csv.gz`, `P001_force_plates.csv.gz`, `static_markers.csv.gz`, `squat_repetitions.csv` et README. Le modèle générique est lu comme XML en mémoire pour son inventaire, **pas redistribué** ; chargé et initialisé uniquement pour un probe OpenSim, sans scaling/IK. Les droits des éventuels composants amont d'un futur modèle doivent rester vérifiés avant son intégration.

CC BY4.0 permet reproduction/adaptation, y compris commerciales, sous conditions d'attribution, lien de licence et indication des modifications ; pas d'implication d'approbation par le déposant. La licence n'accorde pas automatiquement tous droits de personnalité, vie privée ou marque. Texte exact consulté : https://creativecommons.org/licenses/by/4.0/legalcode.en . Le matériel est fourni tel quel, sans garantie d’exactitude ou d’adéquation (section5). Aucun achat ni contrat supplémentaire.

### Attribution conservée

Florian Michaud (2026), *Motion capture, ground reaction forces and knee extension strength during repeated dumbbell squats to fatigue: dataset and symmetric OpenSim model*, v1, https://zenodo.org/records/23979972 . Article associé : Michaud, Katwal, Porzio et Cuadrado, *Toward Real-Time Estimation of Muscle Force and Fatigue During Resistance Training Using a Neural Network Surrogate of OpenSim Musculotendon Kinematics*. CC BY4.0, https://creativecommons.org/licenses/by/4.0/ . PARISFIT ajoute des analyses numériques et des visualisations diagnostiques, non approuvées par les auteurs.

## Format et calibration : acquis / manquant

- CSV gzip, time en secondes, trajectoires reconstruites des37marqueurs en mètres, forces enN et moments enN·m, cadence annoncée100Hz. Temporalité effective mesurée dans le rapport.
- Marqueurs cutanés reconstruits par système optique : pas observations2D brutes, pas centres articulaires. Absence de confidence/occlusion/gap-filling dans les CSV ; finitude ne prouve pas absence d'occlusion ni de filtrage amont.
- Essai statique disponible ; utilisé uniquement pour médianes de positions, distances de landmarks et constellation pelvienne. Il ne fournit pas à lui seul des centres articulaires ou une calibration fonctionnelle.
- Les centres des plates-formes sont documentés enX/Y : (−0,698;0) et(0;0)m. Z vertical est une hypothèse cohérente avec positions et Fz, non une matrice de calibration certifiée fournie.
- Timestamps marqueurs/forces comparés exactement. Le trigger matériel, la compensation de latence, la synchronisation physique et les certificats de calibration ne sont pas établis par la seule égalité des colonnes time.
- Moments disponibles, mais hauteur/origine du capteur, repère de surface et convention de signes non qualifiés : **centre de pression NON TESTÉ**, aucun COP inventé.

La source publique Michaud2026 reste distincte d'une capture PARISFIT. Le protocole adulte et les autorisations distinctes de [phase12](../phase12/CAPTURE.md) restent applicables à toute future capture privée.
