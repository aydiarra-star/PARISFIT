# Qualification des sources — vérification2026-11-27

Les descriptions publiées ne valent pas validation du fichier. Aucun achat, compte créé, accord NC accepté ou envoi privé. CMU n'est pas domaine public sans conditions ; une copie AMASS du CMU ne reçoit pas automatiquement la licence de téléchargement du CMU original.

| Source précise / pistes | Format, fréquence, qualité documentée | Droits/accessibilité | Décision dans PARISFIT |
|---|---|---|---|
| CMU14_06 | BVH converti≈120Hz ; séquence multi-activités, intervalle8,6–11s ; pas de forces | Copie/modification/redistribution permises ; produit commercial permis, revente des données seules interdite [1][2] | REFUSÉ, contrôle existant ; audit numérique exécuté |
| CMU14_14 | « jumping jacks, jog, squats, side twists, stretches »,120Hz catalogue [3] | Même grant primaire CMU ; BVH miroir épinglé par blob | EN ATTENTE DE VALIDATION HUMAINE, screening clip entier exécuté ; pas de cycle squat annoté admis |
| CMU13_30 | « jumping jacks, side twists, squats, jog »,120Hz [3] | Même CMU | EN ATTENTE ; screening entier, pas benchmark de cycles appariés |
| CMU86_08 | « walking, squats, stretching, kicking, punching »,120Hz [3] | Même CMU | EN ATTENTE ; screening entier, absence d'appuis vérité terrain |
| CMU22_14 /23_14 | Squats alternés à deux personnes,120Hz [3] | Même CMU | NON TESTÉ cette phase ; contexte à deux, pas substitution à un squat isolé |
| AMASS, y compris BMLmovi / autres sous-collections | Paramètres de corps ajustés, fréquence par fichier ; pas une capture brute ni des contacts universels | Licence AMASS explicitement non commerciale, production d'artefacts commerciaux et entraînement commercial interdits, redistribution interdite sans accord écrit [4]. Droits source et modèle corporel à vérifier séparément | REFUSÉ pour ce pipeline produit ; aucun fichier téléchargé. Aucun numéro de séquence squat AMASS prétendument vérifié |
| SFU/NUS | BVH/FBX résolus, C3D marqueurs, HDF intermédiaires, VSK calibration [5] ; séquence/fréquence à qualifier | Recherche seulement, usage commercial/revente interdits | REFUSÉ ; aucun téléchargement |
| Fit3D | Séquences d'exercices,25articulations,4vues et poses50Hz ; répétitions annotées [6] | Téléchargement nécessite compte valide [7] ; aucune autorisation commerciale/redistribution établie par ces pages. GHUM/SMPL-X ont des droits distincts | NON TESTÉ ; compte non créé, pas de séquence précise inventée |
| AddBiomechanics1.0 core (sources avec squats à examiner) | Modèles individualisés, positions/vitesses/accélérations estimées, marqueurs et forces ; qualité variable par source [8] | Page primaire CC BY4.0 ; créditer les uploaders/licences internes et examiner l'étude source. Versions avec/sans bras distinctes | EN ATTENTE ; prometteur pour contacts, aucun trial précis ingéré ni garantie de qualité extrapolée à tout l'archive |
| **Michaud2026, Zenodo23979972 v1, S01/P001** | Squats avec haltère,37marqueurs100Hz, deux plates-formes de force, calibration statique et temps début/bas/fin par répétition ; adultes et consentement déclarés par le déposant [9] | **CC BY4.0 vérifiée sur la fiche précise** ; attribution, lien, modifications indiquées [10]. Archive129MB, checksumMD5 publié. Extraction limitée S01/P001/static/annotations/README ; modèle OpenSim non extrait | **Candidat de qualification prioritaire**, EN ATTENTE : variante chargée/fatigue ≠ squat libre ; pas de référence qualifiée sans inspection des colonnes, repères, forces et reconstruction articulaire |

## Pourquoi pas de « meilleure source » proclamée

Les trois nouveaux BVH CMU sont des séquences indépendantes du même fonds, pas une validation externe du pipeline. Leurs maxima sur clips multi-activités entiers ne sont pas comparables au seul cycle14_06. La fiche Zenodo fournit des garanties documentaires plus pertinentes pour étudier les appuis, mais des marqueurs et forces ne sont pas des pivots BVH déjà retargetables. Il faut qualifier la reconstruction et la variante avant de sélectionner une référence.

L'absence de source qualifiée dans cette exécution ne signifie pas qu'aucune source exploitable n'existe. Elle signifie que la chaîne **humain fiable → Rocketbox crédible** n'est pas démontrée ici.

## Sources primaires consultées

[1] https://mocap.cs.cmu.edu/ — grant commercial, interdiction de revente seule ; avertissement sur qualité des premiers sujets, bruit toes/hands ; fingers/thumbs non capturés.

[2] https://mocap.cs.cmu.edu/faqs.php — unitésASF/AMC0,056444 ; système12caméras120Hz ; C3D peut contenir des sorties du modèle Vicon en plus des marqueurs physiques ; pas garantie de qualité.

[3] https://mocap.cs.cmu.edu/search.php?motion=squat — essais et fréquences catalogue. Aucune vidéo de cette page prétendument visionnée.

[4] https://amass.is.tue.mpg.de/license.html — texte de licence consulté, pas seulement la publication ou la licence des scripts.

[5] https://mocap.cs.sfu.ca/ — restriction et description des formats.

[6] https://fit3d.imar.ro/fit3d et https://fit3d.imar.ro/ — description technique.

[7] https://fit3d.imar.ro/download — accès authentifié requis.

[8] https://addbiomechanics.org/download_data.html et https://addbiomechanics.org/ — licence, niveaux de qualité, provenance amont et limites des bras.

[9] https://zenodo.org/records/23979972 — Florian Michaud2026, *Motion capture, ground reaction forces and knee extension strength during repeated dumbbell squats to fatigue: dataset and symmetric OpenSim model*. Article associé : Michaud, Katwal, Porzio et Cuadrado, *Toward Real-Time Estimation of Muscle Force and Fatigue During Resistance Training Using a Neural Network Surrogate of OpenSim Musculotendon Kinematics*. Archive MD5 `ae51793940720bcd0877bdad8c155e82`.

[10] https://creativecommons.org/licenses/by/4.0/ — adaptation et commerce permis sous conditions ; droits de personnalité/vie privée non automatiquement couverts. Aucun soutien du déposant à PARISFIT insinué.
