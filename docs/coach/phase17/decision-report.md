# Décision Phase17 : B — qualification partielle

**Essai : AB01 / Squat / 1**, associé à AB01/Static/1. Ni rejet scientifique définitif, ni qualification suffisante pour une expérimentation maintenant. **Aucune IK, aucun scaling exécuté, aucun retargeting, aucune correction de trajectoire.**

## Faits vérifiés dans les fichiers

- Acquisition limitée à **24 fichiers, 8 237 085 octets**, dont deux C3D ; empreintes Git blob et SHA256 calculées. Dépôt WeRoLab épinglé, aucun script auteur exécuté.
- **57 marqueurs statiques, 49 dynamiques**, identiques aux labels des tâches XML. Les huit absents sont les calibrations documentées. Aucun point invalide ou non fini dans les frames lisibles ; les résidus zéro ne prouvent pas une exactitude optique parfaite.
- **2 948 frames de squat et 1 565 statiques**, 200 Hz ; cinq échantillons analogiques par frame, 1000 Hz. Discordance de borne inclusive dans l’en-tête conservée, aucune frame ajoutée ou réparée.
- **57 rattachements corporels OpenSim explicites** ; neuf mesures de scaling actives, axes locaux XYZ, poids des marqueurs égaux à 1 ; contraintes et verrouillages identifiés. Modèle individualisé et wrappers modifiés exacts non présents dans l’arbre Git inspecté.
- Forces des plateformes 1/2 continues au seuil diagnostique de magnitude 20 N ; huit marqueurs de pied projetés dans l’emprise des plateformes sur toute la prise lisible. **Cela ne prouve pas un contact plantaire complet.** COP non calculé.
- Les 80 os Rocketbox et huit clips ont été lus sans modification ; aucun mapping anatomique admis.

## Déclarations des auteurs

Protocole de squat tenu au moins huit secondes, retour neutre ; A-pose avant retrait de huit calibrations ; traitement des lacunes et filtrage avant export. Affectation des forces et traitement 20 Hz dans MATLAB. RMS statique des modèles **4,21 ± 0,34 cm**, maxima **9,82 ± 0,74 cm**, synthèse interparticipants. Ces déclarations ne sont pas des mesures PARISFIT ; aucune valeur individuelle d’AB01 n’est identifiée dans les pièces inspectées.

## Interprétations conservatrices

La continuité des forces, l’emprise géométrique, les labels et les configurations font de cet essai un cas utile à examiner. Les **13 définitions ambiguës** restent plausibles ; les **44 définitions documentaires confirmées ne sont pas 44 centres articulaires validés**. Le décalage de borne C3D peut venir de la convention d’export : ni corruption certaine, ni détail à ignorer sans contrôle.

## Inconnues essentielles

1. Placement réellement palpé sur AB01, contradictions de la documentation OptiTrack et acceptabilité des rattachements rigides sensibles.
2. Implémentations modifiées de Scale/IK/C3D, paramètres effectivement remplis, sorties individualisées et logs d’erreur d’AB01.
3. Chaîne exacte des repères, signes des forces, moment libre, COP, synchronisation matérielle et différence entre filtrage publié et code Git disponible.
4. Indices officiels des phases : le fichier MAT annoncé est absent de Git. Maintien et retour non qualifiés pour un usage de coaching.
5. Licences amont des composants nécessaires à une redistribution future : le CC BY4.0 du dataset n’autorise pas automatiquement tous les logiciels et modèles tiers.

## Décisions réservées à l’expert

Acceptabilité des approximations et degrés de liberté verrouillés, observabilité anatomique, incertitudes par région, tolérances futures et intérêt du geste comme référence pour un coach. **Aucun professionnel n’a examiné le dossier. Aucun avis ni réponse d’auteur obtenu.**

## Pourquoi B plutôt que A ou C ?

**Pas A :** les ambiguïtés essentielles, les dépendances manquantes, l’erreur individuelle inconnue et les conventions non qualifiées empêchent une admission. Aucun test technique ne permet de contourner ces conditions.

**Pas C :** squat réellement capturé, licence du dataset documentée, statique, labels et forces disponibles et cohérents au niveau documentaire. Rien ne prouve qu’une qualification ultérieure serait impossible. Les inconnues et discordances restent visibles, sans être effacées pour obtenir une admission.

## Recommandation

Faire examiner le dossier par un professionnel indépendant **uniquement sur décision de l’utilisateur**. Rechercher ensuite les pièces publiques manquantes et vérifier passivement le C3D avec un second lecteur, sans acquisition massive ni IK. Ne pas corriger les marqueurs pour réduire les résidus et ne pas transférer les six facteurs S01 d’une autre source.

Toute future expérience nécessite une revue professionnelle puis une autorisation explicite. Même une décision A ne permettrait pas l’activation dans PARISFIT.

## Garde-fous et vérifications

Rocketbox, les huit exercices, le runtime, les données d’application et les travaux précédents sont conservés. Aucune demande envoyée, achat, fusion ou mise en production. **PR11 maintenue en brouillon.**

Les scripts ajoutés acquièrent des fichiers publics, lisent C3D/XML, calculent des statistiques descriptives et produisent des documents ou diagrammes statiques. Ils n’importent pas OpenSim et n’appellent pas les scripts auteurs. [REPRODUCE.md](REPRODUCE.md) décrit les commandes et limites.

Les tests contrôlent provenance, tables, bornes, conditions d’admission non remplies et intégrité des fichiers protégés. La page est vérifiée à 320/390/768/1200 px. **Un PASS technique n’est ni une validation biomécanique ni une évaluation sur téléphone physique.** Les résultats finaux et le lien CI figurent dans le compte rendu de livraison et la PR.
