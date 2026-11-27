# Étude des solutions — licences, coût et faisabilité

Vérification le 27 novembre 2026 dans les sources officielles ci-dessous. « Gratuit » désigne l’absence de prix de licence du logiciel local, **pas l’absence de coût matériel, de temps d’animation ou de revue professionnelle**. Aucun service cloud payant n’a été utilisé. Les résultats du prototype ne constituent pas un benchmark de tous les outils.

| Solution | Coût réel / licence | Commercial | Traitement local / matériel | Qualité, limites et Rocketbox/GLB |
|---|---|---|---|---|
| **MediaPipe Pose** | Logiciel Apache 2.0, 0 € local ; CPU/temps de calcul à financer | Code commercial autorisé avec obligations Apache ; droits vidéo/modèles à vérifier séparément | Oui, testé sur CPU avec modèle Full embarqué, Python 3.11, 0.10.21. Pas de combinaison ni de GPU nécessaire pour cet essai | 33 points estimés image/3D, pas de racine mondiale calibrée ni de prise des doigts. Pieds hors champ extrapolés, torsion axiale ambiguë. Retargeting spécifique nécessaire ; chaîne GLB effectivement testée, résultat C rejeté |
| **FreeMoCap** | Logiciel AGPL-3.0, usage local sans prix de licence ; coût caméras, calibration et temps | L’AGPL n’interdit pas le commercial ; obligations de fourniture du code selon distribution/service et modifications à respecter. Données/modèles séparés | Oui. Plusieurs caméras synchronisées et calibration à prévoir pour une reconstruction multi-vues ; ordinateur local. Pas exécuté ici | Meilleure observabilité potentielle de profondeur et d’occultations, pas de garantie automatique des contacts. Sorties squelette à mapper vers Rocketbox puis Blender/GLB. Aucun chiffre de précision/performance mesuré ici |
| **VideoPose3D** | Licence officielle CC BY-NC 4.0 | **Non commercial sous cette licence** | Local, environnement PyTorch ; GPU utile selon volume, non testé | Lifting temporel depuis points 2D, pas une capture instrumentée. Pas de contact/finger/GLB prêt à l’emploi. Écarté de l’intégration commerciale |
| **WHAM** | Code MIT ; chaîne avec composants/poids et modèle corporel SMPL distincts | **Pas de feu vert global sur la seule licence MIT du code**. Vérifier licences SMPL, checkpoints et dépendances | Installation officielle PyTorch/CUDA, plusieurs dépendances lourdes ; non installé, mémoire minimale non mesurée | Estimation vidéo du corps et du mouvement global, potentiellement plus riche que landmarks isolés ; profondeur/sol et caméra restent à vérifier. Retargeting SMPL→Rocketbox requis, export GLB indirect |
| **Blender** | GPL, logiciel libre à 0 € ; travail humain de nettoyage non gratuit | Utilisation commerciale permise ; œuvres exportées non automatiquement GPL du seul fait de l’outil | Oui, CPU/GPU selon scène ; station d’animation recommandée, pas de capture propre au logiciel | Import BVH, contraintes, IK, nettoyage et export glTF/GLB. Ne transforme pas à lui seul une vidéo en mocap. Option pertinente pour un animateur, non exécutée dans ce prototype |
| **Rokoko Studio Live Blender add-on** | Add-on LGPL-3.0 vérifié ; ne pas confondre avec services/offres Rokoko | Licence du code compatible commercial sous obligations ; tarifs/droits des services et assets séparés, non vérifiés/achetés | Retargeting Blender local à examiner ; fonctions de service/compte non utilisées | Outil de correspondance de rigs, pas preuve de capture ni de licence d’un mouvement. Pas de plugin runtime Three.js ; exporter en GLB après revue |
| **CMU + BVH cgspeed** | Données sous conditions CMU, pas une licence CC0 ; 0 € d’accès. Pas de revente de données seules | Usage dans produits commerciaux autorisé selon la page primaire ; conditions et crédit transmis | Oui, BVH traité localement avec Three BVHLoader, pas de GPU nécessaire à la conversion | Véritable capture optique. Sujet/rig propres, nettoyage et retargeting nécessaires ; orteils/mains bruités, doigts non capturés. Test D réalisé, raccord/contacts/torsion encore HOLD |
| **Rocketbox existant** | MIT ; 0 € | Oui avec notice | Oui, déjà intégré | Rig proche, courbes humaines de bibliothèque. Méthode de capture non attestée par fichier : ne pas l’appeler mocap certifiée. Référence B corrigée phase 4, toujours HOLD |

## Sources officielles consultées

- MediaPipe : https://github.com/google-ai-edge/mediapipe/blob/v0.10.21/LICENSE et `mediapipe/modules/pose_landmark/README.md`.
- FreeMoCap : https://github.com/freemocap/freemocap/blob/18901a2f4a1007aee25184de8ba37e7c535356b3/LICENSE et README du dépôt.
- VideoPose3D : https://github.com/facebookresearch/VideoPose3D/blob/main/LICENSE
- WHAM : https://github.com/yohanshin/WHAM/blob/main/LICENSE ; https://github.com/yohanshin/WHAM/blob/main/docs/INSTALL.md ; README (SMPL, AMASS, checkpoints et composants).
- Blender : https://github.com/blender/blender/blob/main/COPYING et `doc/license/GPL-license.txt`.
- Rokoko add-on : https://github.com/Rokoko/rokoko-studio-live-blender/blob/master/LICENSE.md
- CMU : https://mocap.cs.cmu.edu/ et catalogue du sujet 22/essai 14 ; notice cgspeed copiée avec les preuves.

## Choix à l’issue de l’essai

MediaPipe est une **chaîne locale accessible pour tester**, pas la solution premium démontrée. Le prototype C manque d’informations de pied/profondeur et montre des artefacts nets. Le prototype D a une origine mocap authentifiée mais son retargeting directionnel simplifié ne préserve pas toute la torsion axiale : son origine ne suffit pas à le valider.

Prochaine piste recommandée : capture multi-vues d’un démonstrateur consentant avec pieds/mains visibles, calibration et stratégie de transition choisie avec un professionnel ; nettoyage des contacts et torsions dans un outil d’animation, puis mêmes tests de raccord. **Recommandation de méthode, pas commande ni validation acquise.**
