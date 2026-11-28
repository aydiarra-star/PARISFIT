# Brouillon de demande aux auteurs — NON ENVOYÉ

Objet : clarification du MarkerSet et du repère — dataset10.5281/zenodo.23979972 v1

Bonjour,

Nous auditons la reproductibilité deS01/P001, sans revendication de validation clinique ni redistribution de votre modèle. Le README indique37marqueurs de laboratoire dans le modèle ; le fichierLaiUhlrich2022_symmetric.osim (SHA25642eca458626f42aa1e49d5925e14ec3c16fe81324293bacece643e11319ddbd9) contient66définitions avec des labels différents des37colonnesCSV.

Pourriez-vous indiquer ou déposer publiquement :

1. Le DOI/préprint et suppléments de l’article associé, son schéma de placement/palpation (dontASIC, sacral_crest, forearm_centre) et les offsets éventuels des marqueurs.
2. Le MarkerSet réellement utilisé, une tableCSV→XML et la distinction entre points cutanés, centres virtuels et clusters techniques. Les marqueurs mains/tête ont-ils été exclus, et avec quelles contraintes sur les coordonnées ?
3. Le modèle individualiséS01 ou les setupScaleTool/IK complets : axesP1/P2/P3, corps affectés parFem/Tib/Foot, facteurs des membres supérieurs, ordre scaling/registration, masses, inerties et réglages des articulations.
4. Le repère laboratoire signé, origine3D, transformation versOpenSim, repère des composantesF/M de chaque plate, origine des moments, hauteur et dimensions de surface, transformations appliquées à l’export et calibration.
5. Le mécanisme de synchronisation, latences/filtrage/resampling, visibilité et gap-filling des marqueurs.
6. La version amont du modèle et le script/diff des modifications (wrapping, damping, MarkerSet), afin de reproduire exactement votre configuration.

Une réponse/version publique liée au DOI serait idéale. Aucun nom, signature, donnée privée ou nouvelle vidéo de participant n’est demandé. Nous conserverons les notices et attributions du dataset.

Merci.

---
Statut : EN ATTENTE DE VALIDATION HUMAINE pour transmission et réponse. Aucun courriel ou message externe envoyé parPARISFIT.
