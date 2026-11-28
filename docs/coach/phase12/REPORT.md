# Phase12 — qualification des sources, pas sauvetage du contrôle

**Réponse actuelle : NON DÉMONTRÉ. Admission REFUSÉE.** Le pipeline PARISFIT n'a pas encore produit d'animation Rocketbox crédible à partir d'une référence humaine suffisamment qualifiée. Ce n'est pas une preuve d'impossibilité : une source indépendante mieux instrumentée a été effectivement récupérée, mais la reconstruction de ses articulations et le retarget ne sont pas qualifiés.

Aucun nouveau candidat GLB. Rocketbox et ses huit exercices inchangés ; PR11 brouillon ; aucun achat, activation, fusion ou déploiement.

## 1. Ce qui a réellement été audité

Le BVH CMU14_06 **avant** normalisation morphologique et rééchantillonnage PARISFIT, ainsi que trois autres BVH épinglés14_14/13_30/86_08. Ce sont des **conversions BVH**, pas les observations optiques brutes. Parser/FK NumPy indépendant de Blender/Three.js, respect de l'ordre déclaré des canaux (ici Z/Y/X), longueurs originales conservées. Le reste de la chaîne historique n'est pas réécrit pour améliorer les scores.

Tentatives des originaux14.asf/14_06.amc/14_06.c3d en CI : **échec de validation du certificat TLS** ; aucun contournement de cette validation, aucune cause de capture déduite. Le code sait analyser les fichiers s'ils deviennent disponibles, mais leurs mesures restent NON TESTÉES dans cette exécution.

## 2. Résultats séparés sur la fenêtre8,6–11s

| Branche, sans correction empilée sauf contrôle historique nommé | Hz | Pic accélération de pivot | Variation maximale longueur |
|---|---:|---:|---:|
| BVH natif en mètres |≈120,00048|98,381m/s²|<10⁻¹²m|
| Filtre seul `[0,25;0,5;0,25]` sur positions natives |≈120,00048|34,107m/s²|0,1031mm|
| Rééchantillonnage seul, positions linéaires60Hz |60|33,969m/s²|0,00132mm|
| Rééchantillonnage seul, canaux Euler déroulés puis FK60Hz |60|33,968m/s²|<10⁻¹²m|
| Normalisation seule (facteur0,946989) sur natif |≈120,00048|93,166m/s²|<10⁻¹²m|
| Combinaison historique : canaux60Hz puis facteur0,946989 |60|32,167m/s²|<10⁻¹²m|

Les bornes natives sont les samples inclus dans8,6–11s (premier≈8,60830s, dernier≈10,99996s) ; les branches60Hz couvrent exactement8,6–11s. Paramètres et bornes exactes sont dans `14_06-report.json`. Le filtre supprime une frame à chaque extrémité, il n'invente pas de préparation/récupération.

**Aucune branche filtrée n'alimente un retarget.** La baisse de pic ne signifie pas amélioration anatomique : le filtre cartésien déforme les longueurs d'os et peut modifier les appuis. Aucun traitement n'est admis par son seul pic d'accélération.

### A/B/C isolés, conservés

Les rapports phase11 et leurs hashes restent liés dans le manifeste. Le job `blender-control` les réexécute sur l'entrée non filtrée identique. A34,031, B33,549, C corrigé186,292m/s² ; pénétration277,957/9,066/8,656mm. **Tous REFUSÉS.** Le contrôle C qui immobilise davantage certains pieds mais dégrade fortement les accélérations reste rejeté.

## 3. Attribution des pics : ce qui est prouvé / non prouvé

- **Rééchantillonnage PARISFIT :** le pic98,381 existe déjà dans le BVH natif sur ce cycle. Le passage60Hz le réduit ici ; il ne peut pas être présenté comme la cause de l'apparition de ce pic natif. Les instants des maxima peuvent changer ; ce n'est pas une preuve d'absence d'aliasing.
- **Normalisation uniforme :** les dérivées sont multipliées par0,946989 ; test de proportionnalité numérique conservé. Rotation globale et translation constantes ne créent pas de pic de norme de dérivée.
- **Calcul numérique :** différence de vitesses et seconde différence directe concordent à la précision flottante. FK indépendant reproduit le résultat historique32,17 à environ0,001m/s² près. Cela vérifie une implémentation, pas un capteur.
- **Filtrage :** expérience indépendante documentée ; diminue les hautes fréquences mais change les longueurs. Ne permet pas de distinguer bruit et vraie accélération.
- **Capture originale / résolution Vicon / conversion BVH / filtres amont :** NON TESTÉ, origine causale non identifiée faute accès aux originaux et à leur historique. Ne pas confondre « déjà dans le BVH » et « causé par le sujet ou le capteur ».
- **Retarget :** C amplifie très fortement le pic ; A/B ne sont pas l'origine de toute l'accélération source. Les points de maximum et ensembles d'articulations doivent être distingués :31pivots source vs80os cible, pas comparaison force à force.

## 4. Temporalité, anatomie, pieds et transitions

BVH :5358frames, `Frame Time=0,0083333`, donc≈120,00048Hz. La différence avec120Hz catalogue est compatible avec l'arrondi du champ ; elle ne prouve pas une dérive réelle d'horloge. Aucun timestamp de capture individuel : régularité *encodée* seulement. Frame0 T-pose artificielle conservée pour provenance, sa transition mesurée séparément et exclue des dérivées de mouvement physique.

Le rapport conserve maxima/p95, sample et articulation du pic, longueurs, offsets nuls, vitesses, accélérations du bassin, trajectoires/minima des pieds, angles de genoux non signés et inclinaison du tronc. Les joints fingers/thumbs sont des ajouts d'édition non capturés selon CMU ; les toes/hands peuvent être bruités. Un résidu de seconde différence est seulement un **proxy de haute fréquence**, pas une mesure de bruit de capteur.

Les fenêtres à faible vitesse de pied ne sont pas des contacts prouvés. Le BVH n'a ni patches plantaires ni forces ; sol et axe anatomique restent à qualifier. Les phases et les raccords sont en attente de revue humaine ; l'écart entrée/sortie ne certifie pas un retour debout stable.

## 5. Autres sources : pas de classement trompeur

`local-benchmark.json` contient le screening entier des BVH14_14,13_30 et86_08, provenance/blobs dans `downloads.json`. Ils incluent d'autres activités (sauts, marche, etc.) ; leurs maxima globaux ne sont **pas** un classement de qualité des squats. Aucun découpage « le plus calme » n'est sélectionné après lecture des scores.

Le dossier [sources et droits](SOURCES-AND-RIGHTS.md) détaille AMASS, SFU, Fit3D, AddBiomechanics et la source précise **Michaud2026 / Zenodo23979972 v1 / S01/P001**. Les licences NC ne sont pas utilisées pour développer le produit sous prétexte de benchmark.

### Nouveau candidat instrumenté réellement récupéré

Archive Zenodo vérifiée par MD5 publié et SHA256 épinglé ; seul un sous-ensemble de marqueurs, forces, calibration statique, annotations et README est conservé. Pas de modèle OpenSim extrait, pas de vidéo privée ou signature. **CC BY4.0** : crédit et modifications documentés ; aucune approbation du déposant présumée.

S01/P001 contient3350échantillons,100Hz mesurés sur les timestamps, aucun non-fini dans le tableau de marqueurs,33,49s. La première répétition est définie par le fichier du déposant : début10,45s, bas11,08s, fin11,94s. Ce choix est déterministe, pas le minimum d'un score.

`marker-benchmark.json` mesure cette répétition et les deux forces Fz associées. Les genoux/tronc/bassin sont des **proxies de marqueurs cutanés**, pas des centres articulaires. Le repère verticalZ est cohérent avec les centres de plates-formes dans le planX/Y et les colonnes ; l'association pied droit→plate1/gauche→plate2 reste une hypothèse à confirmer. Un seuil20N sert seulement de test de charge, pas de diagnostic clinique.

**Pas de comparaison numérique naïve entre accélérations de marqueurs et pivots BVH.** Un benchmark de retarget apparié sur cette source reste NON TESTÉ : reconstruction des centres/axes articulaires, repères de sol, morphologie, licence des composants éventuels et variante chargée doivent être qualifiés. La répétition recadrée n'inclut pas des maintiens debout garantis avant/après.

## 6. Preuves accessibles et état de revue

Quatre petits MP4 source et plusieurs PNG inclus dans `previews/`, environ0,6Mo : accès immédiat sans les grands artifacts. Cycles numériques complets, face/profil/trois-quarts, hypothèses d'appui colorées, overlay natif/filtré au même instant. Les films complets Rocketbox A/B/C restent dans les artifacts phase11, inchangés.

Une image centrale source a été effectivement ouverte pour vérifier la lisibilité. **Aucune revue intégrale des vidéos ni approbation visuelle/professionnelle déclarée.** Les vidéos produites sont décodées automatiquement. Instructions de récupération navigateur/CLI et régénération dans [RECOVER.md](RECOVER.md). L'archive129Mo n'est pas versionnée ; elle est supprimée après extraction du sous-ensemble public.

## 7. Blocages et décision

1. Origines CMU brutes indisponibles via TLS : causalité capteur/conversion non établie.
2. Nouvelle source avec marqueurs/forces acquise, mais pas de rig articulaire qualifié ni retarget A/B/C sur elle.
3. Mesures de nature différente : pas de classement de qualité cross-source ni de comparaison de variantes sans calibration.
4. Contacts/axes/torsions/collisions et récupération ne sont pas tous validés.
5. Revue professionnelle, appareils physiques et capture PARISFIT autorisée toujours absents.

La suite pertinente est de qualifier **un** cycle du nouveau jeu instrumenté avec ses forces et un modèle anatomique explicitement autorisé, avant de tester Rocketbox. Ne pas réinjecter le filtre dans l'ancien CMU pour fabriquer un succès. **Aucune animation admissible à ce stade.**

### Résultat mesuré sur S01/P001/répétition1

150échantillons,100Hz, cycle annoté1,49s. Pic d'accélération **des marqueurs**6,604m/s² (Left_2nd_metacarpal_head), proxy bassin5,020m/s². Les deux Fz restent>20N sur100% des samples, avec des minima237,90/230,52N. Le déplacement horizontal maximal des marqueurs de talon depuis le début vaut21,81/25,03mm : ce n'est pas une mesure de glissement de semelle (rotation du pied, mouvement de peau et localisation du marqueur peuvent contribuer).

Les proxies de flexion des genoux couvrent environ8,8–103,0° à droite et11,0–101,3° à gauche ; inclinaison du tronc proxy4,78–38,20°. **Ces définitions ne sont pas celles des pivots du BVH** : pas de conclusion «6,6 est meilleur que98» sans modèle commun et estimation d'incertitude. C'est une source prometteuse pour la qualification instrumentée, pas une animation admise.

Le PNG de marqueurs au point bas11,08s a également été ouvert : il est lisible et porte ses forces et son attribution. Cela reste l'examen d'une image, pas le visionnage de la vidéo complète ni une approbation anatomique.
