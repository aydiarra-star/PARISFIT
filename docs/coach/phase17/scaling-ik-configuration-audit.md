# Scaling et IK — configurations lues, jamais exécutées

**B — méthode partiellement comprise, chaîne non rejouée.** Tous les chemins ci-dessous sont relatifs au dépôt WeRoLab épinglé dans [source-manifest.json](source-manifest.json). Les lignes originales citées sont consultables dans [source-excerpts.md](source-excerpts.md) ou via le commit Git. L’extraction exhaustive des mesures, axes, tâches, poids, coordonnées et contraintes est dans [configuration-inspection.json](configuration-inspection.json).

## 1. Quel fichier pour quel essai ?

|Étape prévue|Fichier / lignes probantes|Fait vérifié et limite|
|---|---|---|
|Entrée squat|`AB01/Squat/1/Processing/process_trial_data.m:L3–12`|`squat_1.c3d`, construction de trial_class, forces, export TRC/MOT|
|Statique associé|`MATLAB tools/trial_class.m:L127–141`|Chemins résolus vers AB01/Static/1, pas vers un autre participant|
|Modèle source|`AB01/Static/1/Setup/Setup_Scale.xml:L13–17`|`../../../../Model/Biomech57.osim`, MarkerSet même dossier Model ; fichiers acquis|
|Scale depuis API|`trial_class.m:L627–630`|Appel `Osim.Scale(staticTrcFile,scaleXml,osimOutputFile)` ; wrapper modifié absent de cet arbre Git|
|IK prévue|`trial_class.m:L633–640`|Appel `Osim.IK(trcFile,ikXml,ikMotOutputFile)`, puis view IKError ; fonctions exactes non inspectables ici|
|Sortie individualisée|`Setup_IK.xml:L9`|`../generated/Generated_Model.osim` ; non fourni dans l’arbre inspecté, non généré ici|
|Version GUI|`AB01/Static/1/Setup/Setup_Scale_GUI.xml:L13–17,L553–557,L916–928`|Références modèle/MarkerSet `Unassigned`, TRC`../Data/static.trc`, fenêtre0–7,82 s|

Le README exige des bibliothèques modifiées et le changement d’accès aux propriétés de `OsimC3D` dans OpenSim4.4. `add_to_path.m:L1–5` ajoute seulement le dossier MATLAB tools ; l’arbre épinglé n’y contient que `trial_class.m`, pas `Osim.Scale`/`Osim.IK` ni les bibliothèques modifiées. L’API Figshare référence une archive `MATLAB tools.zip`,218050691 octets : non téléchargée, plutôt que remplacer les fonctions exactes par une version quelconque d’EpicToolbox. **Absence dans Git ≠ absence définitive dans le dépôt complet.**

## 2. Valeurs et application du scaling

`Setup_Scale.xml:L5–9` : masse49,81 kg, height=-1 et age=-1. Les commentaires indiquent que height/age sont informatifs ; la stature1,73 m du script global n’est pas une valeur substituée dans ScaleTool. `ModelScaler/apply=true`, ordre **measurements uniquement** (L20–24). Le Scale Set manuel est vide (L548–551), aucun jeu de six facteurs Michaud utilisé.

Les distances des paires de marqueurs expérimentaux et du modèle servent à déterminer les facteurs (commentaireofficiel L16). Toutes les mesures actives ciblent **X Y Z des repères locaux des corps**, non les axes du laboratoire. Les paires bilatérales sont regroupées pour appliquer une mesure commune aux deux côtés. La règle précise d’agrégation numérique relève du moteur/wrapper exact ; aucune valeur de facteur résultant n’est fournie dans ces XML ni calculée ici.

|Mesure active|Paires|Corps concernés|Ligne de début dans Setup_Scale.xml|
|---|---|---|---:|
|torso|RIPS–CV7 ; LIPS–CV7|torso, XYZ|104|
|pelvis|RIAS–LIAS ; RFTC–LFTC|pelvis, XYZ|132|
|head|RAH–LPH|head, XYZ|320|
|hand|LRSP–LHM2 ; LRSP–LUSP ; RRSP–RHM2 ; RRSP–RUSP|hand_r, hand_l, XYZ|344|
|femur|LFTC–LFLE ; RFTC–RFLE|femur_r, femur_l, XYZ|384|
|tibia|LFAX–LFAL ; RFAX–RFAL|tibia_r, tibia_l, XYZ|416|
|humerus|LCAJ–LHLE ; RCAJ–RHLE|humerus_r, humerus_l, XYZ|448|
|radius|LHLE–LRSP ; RHLE–RRSP|radius_r, radius_l, XYZ|480|
|calcn|LFCC–LDP1 ; RFCC–RDP1|calcn_r, calcn_l, XYZ|512|

**12 entrées désactivées** : humerus_r/l, radius_r/l, femur_r/l, tibia_r/l, calcn_r/l, hand_r/l ; leurs BodyScale Set sont vides. Elles ne sont pas 12 mesures supplémentaires appliquées. Ni ulna, ni patella, ni talus, ni toes ne sont nommés par les BodyScale actifs : ne pas inventer leur adaptation, la propagation géométrique exacte reste à vérifier dans le moteur et les sorties individualisées. Les géométries référencées par le modèle ne sont pas devenues des géométries individualisées vérifiées.

`preserve_mass_distribution=true` : conservation prévue des proportions de masse lors du scaling à49,81 kg. La redistribution numérique des inerties/masses n’est pas exécutée. **Aucun facteur S01/P001 (Michaud, phase14) n’est transféré à AB01.**

## 3. Registration et pondérations

- MarkerSet externe :57 marqueurs, 46 avec `fixed=false`, 11 sans champ `fixed` explicite ; localisations en repères des corps explicites. Les 57 entrées sont identiques à celles embarquées dans Biomech57.osim. **Cela confirme des rattachements logiciels, pas leur validité anatomique individuelle.**
- MarkerPlacer`apply=true`,57 IKMarkerTask, toutes`apply=true`,`weight=1` ; aucune tâche de coordonnée déclarée. Les 46 marqueurs explicitement non fixes peuvent être repositionnés pendant la registration ; le défaut de version pour les 11 autres reste à vérifier ; aucune preuve de déplacements manuels participant par participant.
- `max_marker_movement=-1` est un paramètre déclaré, **pas une tolérance de précision de−1 m**. Le sens effectif et le contrôle de cette limite doivent être vérifiés dans la version exacte du logiciel avant toute exécution.
- API : marker_file/time_range`Unassigned` ; GUI : static.trc et 0–7,82 s. La fenêtre GUI correspond à la dernière frame lisible du statique. On ne suppose pas que le wrapper API remplit les champs de manière identique sans ses sources.
- La posture A-pose est décrite dans l’article ; elle n’implique ni pose anatomique neutre parfaite, ni axes articulaires palpés.

## 4. Configuration IK (inspection seulement)

`AB01/Squat/1/Setup/Setup_IK.xml:L9–21` : modèle généré attendu, **constraint_weight=Inf**, **accuracy=1e-5**. Le coût décrit par le commentaire est la somme des erreurs quadratiques pondérées des tâches. Accuracy est une tolérance numérique, **pas une erreur anatomique admissible en mètres**.

**49 tâches de marqueurs actives, poids 1**, correspondant exactement aux 49 labels C3D. Aucune tâche IKCoordinateTask. En fin de XML, marker_file, time_range et sorties restent`Unassigned` : résolution dépendante du wrapper. Les forces **n’entrent pas dans ce coût IK** ; elles servent au traitement cinétique et à l’ID séparés.

Modèle XML : deux contraintes CoordinateCouplerConstraint patellofemorales (L5759–5790). Six coordonnées explicitement verrouillées : subtalar_angle_r/l, mtp_angle_r/l, wrist_dev_r/l. Valeurs par défaut 0. Les autres coordonnées, bornes et contraintes sont exportées dans le JSON ; la présence de bornes ne prouve pas l’observabilité de tous les degrés de liberté.

## 5. Forces et hypothèses anatomiques sensibles

ExternalForces affecte la force1 à`calcn_r`, force2 à`calcn_l`, vecteur et point exprimés en`ground`. `torque_identifier` est vide : pas de preuve dans ce XML d’application du moment libre mesuré. Un MOT et le setup ID sont prévus, non générés. Voir [audit des forces](ground-reaction-forces-audit.md).

Points à soumettre à l’expert : grand trochanter FTC rattaché au **pelvis**, HGT rattaché au **torso**, styloïde ulnaire USP rattachée au **radius**, DP1 du gros orteil rattaché au **calcn** et MTP verrouillée. Ces choix sont **faits XML confirmés**, mais l’approximation rigide et son adéquation au squat ne sont pas validées. Ne pas déplacer silencieusement un marqueur vers un autre corps ni convertir un landmark en centre articulaire.

**Bilan :** chemins prévus, corps/axes, mesures et pondérations suffisamment lisibles pour préparer une contestation experte ; facteurs résultants, wrappers modifiés, sorties et relation exacte au RMS publié non établis. Aucun solveur appelé, aucune géométrie modifiée.
