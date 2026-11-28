# Intégrité C3D et timing — erratum explicite de phase17

**Aucun fichier source modifié, réparé, rééchantillonné ou réexporté.** Lecture indépendante des octets de l’en-tête et des paramètres avec Python standard (`struct`), sans utiliser python-c3d pour les décoder. Comparaison secondaire avec les propriétés du lecteur installé. Les trajectoires ne sont ni corrigées ni reconstruites.

## Correction d’une attribution erronée

En phase17, le champ nommé `headerLastFrame` a été obtenu par **`Reader.last_frame`**, pas par **`Reader.header.last_frame`**. Or la première propriété peut substituer une valeur issue des paramètres. Le nom de ce champ et la conclusion «en-tête brut discordant» étaient donc inexacts. Les anciens rapports restent inchangés comme preuves historiques ; **la présente note les rectifie**, sans faire disparaître l’avertissement du lecteur.

|Élément|Squat/1|Static/1|
|---|---:|---:|
|Premier index dans l’en-tête brut|0|0|
|Dernier index dans l’en-tête brut|2947|1564|
|Nombre inclusif dans l’en-tête brut|2948|1565|
|POINT:FRAMES — nombre de frames|2948|1565|
|Frames complètes déterminées par les octets|2948|1565|
|Octets par frame, marqueurs + analogiques|1504|1632|
|Octets restants après ces frames|0|0|
|Propriété calculée `Reader.last_frame`, version0.6.0|2948|1565|
|Tentatives de lecture par boucle inclusive du lecteur|2949|1566|

Les en-têtes sont décodés aux offsets C3D : premier index6, dernier index8, échelle12, bloc de données16, sous-échantillons18, fréquence20 (octets comptés depuis0). Le bloc de paramètres est décodé séparément, processeurIntel84 ; pas de supposition sur des paramètres TRIAL inventés. Le lecteur ciblé n’est pas un validateur universel de toutes les variantes C3D.

**Calcul indépendant :** squat `(4439424 − 11×512) / 1504 = 2948` ; statique `(2560224 − 12×512) / 1632 = 1565`. Les blocs de paramètres confirment49/57points,36canaux analogiques,200/1000Hz. [Résultat complet](c3d-independent-byte-audit.json).

## Origine démontrée de l’avertissement

Dans **python-c3d0.6.0**, `last_frame` compare l’index de fin avec `POINT:FRAMES` puis peut retourner ce dernier comme index final. Pour ces fichiers dont l’index initial est0, cela confond **nombre de frames** et **dernier index**. `read_frames` utilise ensuite `range(first_frame, last_frame + 1)` : une tentative supplémentaire atteint EOF. [Code du lecteur avec numéros de lignes et SHA256](python-c3d-reader-evidence.txt).

Cette explication est établie par la lecture des octets et du code installé. Elle **n’établit pas une perte d’acquisition**, ne justifie ni ajout de frame ni modification de l’en-tête. L’hypothèse d’une simple frame manquante, laissée ouverte en phase17, n’est pas soutenue par ce comptage. Le fabricant exporte ici un indexage de départ0 ; sa conformité aux conventions d’autres logiciels et leur comportement restent à vérifier, mais les trois comptes physiques sont cohérents.

## Documentation consultée le 27 novembre 2026

- [C3D POINT:FRAMES](https://www.c3d.org/HTML/Documents/pointframes1.htm) : stocke **le nombre** de frames3D, pas nécessairement le nombre d’images vidéo. La mention «no frame zero» dans cette section souligne notamment qu’un nombre de frames ne vaut pas un index final commençant à0 ; ne pas en déduire une réparation autorisée.
- [C3D Header Record function](https://www.c3d.org/HTML/Documents/headerrecordfunction.htm) : début de données par POINT:DATA_START, taille par POINT:FRAMES, nombre de points, valeurs analogiques et format numérique.
- [C3D Data Synchronization](https://www.c3d.org/HTML/Documents/datasynchronization.htm) : ratio analogique unique et stockage lié frame par frame ; la synchronisation réelle dépend du système qui crée le fichier. Des filtres peuvent introduire des latences. L’exemple de délai donné dans cette documentation **n’est pas une mesure applicable à AB01**.
- Implémentation réellement installée python-c3d0.6.0 : propriétés first_frame/last_frame et boucle read_frames, extraits numérotés ci-dessus. La page historique pythonhosted n’a pas pu être récupérée ; le code installé, avec empreinte, est la preuve primaire du comportement étudié.

## Empreintes avant/après lecture : identiques

- Squat : `7d4adaf1ca565de3fc172cde1b92a6b607f7a90d1f22b37453fa0cd4b6e30482`.
- Statique : `ba89054b8d0bb0cb18087be68b81e1a326dcf2719c012dff73a5591102b1b4b1`.

Comparer avec [manifest phase17](../phase17/source-manifest.json). Aucun nouveau téléchargement nécessaire : les deux fichiers épinglés sont ceux du cache acquis en phase17. Pour un autre environnement, le script d’acquisition passif phase17 permet de les retrouver sans tout le dataset.

## Conséquences temporelles possibles, non corrections

- Marqueurs : **200Hz, pas5ms**. Forces : **1000Hz, pas1ms**, cinq valeurs analogiques par frame de points.
- Sur le contenu lisible : squat0–14,735s pour les points,0–14,739s pour les analogiques ; les4ms supplémentaires sont les quatre sous-échantillons de la dernière frame, **pas un retard estimé**.
- L’EOF terminal ne démontre pas un décalage de tous les échantillons. Un consommateur allouant une frame de plus pourrait produire une case finale vide, un arrêt ou une extrapolation. Une frame artificielle représenterait5ms et cinq échantillons analogiques : **risque logiciel**, pas événement mesuré.
- Changer séparément les index des deux flux pourrait introduire un décalage ; aucune telle opération n’est proposée. Origine absolue du temps, latence matérielle et dérive restent inconnues.

## Questions encore ouvertes

**T1 — Acquisition :** quelle preuve de déclenchement, d’horloge ou de calibration temporelle relie les deux flux pour AB01 ? Un ratio5:1 n’est pas cette preuve.

**T2 — Export/import :** quel comportement de la version exacte d’osimC3D utilisée par les auteurs face à l’index0 et au comptePOINT:FRAMES ? Le contrôle binaire actuel ne remplace pas l’examen de cette dépendance.

**T3 — Filtrage :** l’article rapporte marqueurs6Hz et forces20Hz ; le codeGit inspecté expose un lissage gaussien30échantillons pour la détection de contacts. Où est implémenté le filtrage publié, dans quelle version et avec quel effet de phase ? Aucun filtre ajouté ici.

**T4 — Repères et forces :** comment sont composés le repère local de plateforme, l’export C3D et `rotateData('x',−90)` ? Quel sens GRF/force sur plateforme, quelle origine des moments, quel traitement du moment libre et du COP ? Pas de conversion appliquée ici.

**T5 — Phases et données interpolées :** où sont les indices officiels du maintien et les informations sur les lacunes initiales ? Le fichierMAT annoncé reste absent de l’arbreGit. Les résidus C3D nuls ne prouvent pas que les observations originales étaient complètes.

Voir [audit des forces phase17](../phase17/ground-reaction-forces-audit.md). **Un problème de lecture expliqué ne qualifie pas à lui seul l’anatomie ou la synchronisation.**
