# Forces de réaction — AB01 / Squat / 1

**Audit passif du C3D original téléchargé.** Aucun filtrage, correction, COP reconstruit, ID ou IK. Les statistiques portent sur tous les échantillons analogiques lisibles, pas seulement sur la courbe réduite d’illustration.

## Faits dans le fichier

Source : `AB01/Squat/1/Data/squat_1.c3d`, SHA256 dans [manifest](source-manifest.json). Paramètres bruts et résultats : [c3d-inspection.json](c3d-inspection.json).

- POINT :49 marqueurs, unités **m**,200 Hz ; ANALOG :36 canaux,1000 Hz, soit5 échantillons par frame.
- Six plateformes **TYPE=2**. Pour chaque plateforme k : Fxk,Fyk,Fzk en **N**, Mxk,Myk,Mzk en **N m** ; numéros de canaux1–36 vérifiés par FORCE_PLATFORM:CHANNEL. GEN_SCALE/SCALE/OFFSET sont consignés ; lecture des valeurs physiques selon ces métadonnées, sans nouvelle calibration.
- CORNERS :4 coins 3D par plateforme, présents dans le même conteneur ; ORIGIN :vecteur[0,0,0] pour les six plates. Cela documente un repère stocké, pas la preuve indépendante d’un offset capteur physique nul.
- 14740 échantillons analogiques finis ; intervalle relatif **0–14,739 s**, 2948 frames de marqueurs 0–14,735 s. Les 4 ms supplémentaires correspondent aux quatre sous-échantillons de la dernière frame, pas à un retard estimé.
- En-tête C3D et POINT:FRAMES présentent la discordance de borne décrite dans [sélection](selected-squat-trial.md). Aucune frame supplémentaire créée ; statistiques limitées au contenu lisible.

## Axes : ne pas confondre local, C3D et modèle

L’article Figure2/3/7 décrit le repère de présentation Motive avec **Y vertical, X médiolatéral, Z antéropostérieur**. Les canaux analogiques Fx/Fy/Fz de type2 sont des composantes de plateforme ; **Fz n’est pas automatiquement la verticale positive du modèle**.

Dans le C3D, les coins de plateforme ont une composante Z proche de−0,28 m pour les plateformes 1/2 et les pieds sont au voisinage de ce plan. Le code officiel `trial_class.m:L195–218` appelle`osimC3D(path,1)` (représentation COP), puis **rotateData('x',−90)** avant d’obtenir les tables. Mathématiquement une rotation active standard Rx(−90°) donne(x,z,−y) ; c’est une interprétation de l’opération écrite, **pas une conversion appliquée ici**. L’importateur exact peut aussi définir le sens de la force et transformer le repère local des plates. La documentation de phase16 ne doit donc pas être lue comme «les coordonnées brutes C3D ont déjà Y vertical».

Le lien complet entre force exercée sur plate/GRF sur pied, axes locaux et ground doit être vérifié avec la version d’`osimC3D` et les métadonnées d’export. Nous ne retournons pas les signes pour afficher artificiellement un poids positif.

## Couverture de l’appui : vérification limitée mais réelle

Seuil de diagnostic **|Fz local|>20 N**, choisi parce que les auteurs utilisent 20 N pour les contacts, et non ajusté pour réussir le test. Ici la valeur absolue sert uniquement à inspecter une magnitude avec les signes stockés ; ce n’est pas une reproduction de leur algorithme après import/filtrage.

|Plate|Fz local min–max (N)|Moyenne (N)|Échantillons de magnitude Fz supérieure à 20 N|
|---|---|---:|---:|
|1|−342,639 à −184,358|−280,270|14740/14740|
|2|−266,048 à −130,201|−208,148|14740/14740|
|3|−5,543 à 2,171|−1,729|0/14740|
|4|−5,151 à 2,246|−1,537|0/14740|
|5|−4,476 à 3,596|−0,665|0/14740|
|6|−5,848 à 2,871|−1,361|0/14740|

Le script d’essai`process_force_data.m:L1–24,L78–97` utilise l’intervalle entier puis affecte la plateforme 1 au pied droit et la plateforme 2 au pied gauche. Cette affectation est cohérente avec le protocole décrit, **pas déduite des seules courbes**.

Contrôle géométrique indépendant du solveur : projection des quatre marqueurs FCC/FM1/FM5/DP1 de chaque pied sur la base des coins de sa plateforme, en coordonnées C3D inchangées. **Les huit projections sont dans leurs rectangles à chaque frame lisible (2948/2948)**. Les distances signées au plan, dépendantes de l’orientation de la normale, restent de l’ordre de1,8–3,6 cm ; ce sont des marqueurs cutanés, pas des points de la plante. Le JSON contient chaque borne u/v et distance. Pas de nouvelle surface de contact modélisée.

**Conclusion permise :** les plates assignées portent une charge mesurable pendant toute la séquence lisible et les marqueurs du pied restent projetés au-dessus de leur emprise. La séquence couvre donc les phases de la prise sans interruption de mesure apparente. **Conclusion interdite :** contact plantaire complet, absence de décollement talonnier, pression uniforme, absence de glissement ou segmentation exacte des phases. Pas de semelles de pression ou vidéo spécifique à cet essai inspectées.

## Centre de pression et moments

Le C3D ne contient **pas de canaux COP directement nommés** ; il contient forces, moments, type2, coins et origine. Le code utilise l’importateur OpenSim pour obtenir p1…p6, puis affecte les COP aux pieds et écrit un MOT (`trial_class.m:L237–255,L444–461,L484–496,L616–624`). Les conversions et le traitement du moment libre ne sont pas pleinement qualifiés : **COP non recalculé**, pas de comparaison à un polygone d’appui.

`Setup_External_Forces.xml:L5–45` applique forces et points à calcn_r/l dans ground, sans torque_identifier renseigné. Cela doit être examiné avant toute interprétation cinétique des résultats ID ; présence de Mx/My/Mz mesurés ne prouve pas leur utilisation intégrale.

## Synchronisation et traitements : séparation des preuves

**Auteurs :** marqueurs 200 Hz, forces 1000 Hz ; gap-filling Motive linéaire/pattern-based puis marqueurs Butterworth 6 Hz ; forces filtrées 20 Hz, Butterworth ordre 5 dans MATLAB ; contacts assignés manuellement, seuil 20 N. Ils déclarent un seul échantillon de force manquant dans une autre activité/participant, pas ici.

**Fichiers inspectés :** ratio5:1, même conteneur, frames contiguës et aucun NaN lisible. Cela ne mesure pas la latence matérielle ni une dérive. Pas de timestamps absolus, canal trigger ou mesure de délais indépendante dans les paramètres lus. Ne pas estimer le décalage par corrélation bassin/forces.

**Code Git :** seuil 20 N (L36), lissage`gaussian,30` pour détection (L268), appel lowpass commenté (L267). Aucun Butterworth 20 Hz explicite dans le trial_class épinglé. Il peut exister dans les dépendances modifiées non inspectées ou dans une autre version : **écart entre description publiée et code disponible à résoudre**, pas preuve que l’article est faux. Aucun de ces traitements exécuté par PARISFIT.
