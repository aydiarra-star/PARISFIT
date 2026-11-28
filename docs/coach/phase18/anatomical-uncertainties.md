# Incertitudes anatomiques — registre contradictoire

**44 définitions documentaires confirmées et 13 plausibles, sans promotion.** Aucun centre articulaire ni mapping Rocketbox confirmé. «Confirmé» décrit une proposition documentaire, pas le placement sur AB01 ni une validation professionnelle. Chaque marqueur nécessite une réponse ; P1 signale les priorités anatomiques, P2 le contrôle obligatoire restant.

Les termes anglais ci-dessous reprennent le libellé anatomique de la documentation OptiTrack, sans préfixe Left/Right : le côté est conservé dans le CSV. Les définitions françaises viennent de phase17. Le texte contradictoire n’est pas corrigé silencieusement. Source : [OptiTrack Biomech57](https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57), sections par région ; [CSV original de phase17](../phase17/marker-anatomical-mapping.csv).

## Questions transversales obligatoires

- **Bassin et centres :** quelle orientation signée et quelle méthode d’estimation individualisée sont défendables ? Un milieu de marqueurs ou la description du squelette Motive n’est pas automatiquement une articulation OpenSim.
- **Gauche/droite :** les noms documentent la latéralité attendue, pas l’absence de permutation pendant le labelling. Quelle preuve relie labels, palpation et pied/plateforme pour toute la prise ? Aucune inversion automatique.
- **Tissus mous :** vêtements, peau et marqueurs peuvent se déplacer relativement aux os. Quel budget d’incertitude par région et quelles limites aux degrés de liberté observables ? L’absence de trous après interpolation ne résout pas ce problème.
- **Scaling/registration :** 46 champs fixed=false et 11 champs absents ; quelle version de défaut, quel déplacement de marqueur et quelles contraintes étaient effectivement utilisés ?
- **Rocketbox :** les pivots, proportions, axes de repos et degrés de liberté du rig ne sont pas des centres anatomiques certifiés. Aucun des 57 points ne reçoit ici une correspondance de transfert.

## Registre des 57 marqueurs

[CSV exploitable](marker-review-register.csv) · [JSON avec réponses nulles](marker-review-register.json) · [Schéma documentaire](../phase17/markerset-schematic.svg) · [Points statiques mesurés](../phase17/static-marker-projections.svg)

### M01 — RCAJ · Confirmé · P2

**Définition originale :** Clavicle-Acromion Joint. Proéminence clavicule-acromion, sommet de l’épaule (droite).

**Contradiction ou limite :** Repère superficiel, pas centre de rotation de l’épaule. Parent logiciel : `/bodyset/torso`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Upper Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L6–13.

### M02 — LCAJ · Confirmé · P2

**Définition originale :** Clavicle-Acromion Joint. Proéminence clavicule-acromion, sommet de l’épaule (gauche).

**Contradiction ou limite :** Repère superficiel, pas centre de rotation de l’épaule. Parent logiciel : `/bodyset/torso`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Upper Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L14–21.

### M03 — CV7 · Confirmé · P2

**Définition originale :** Cervical Spine Vertebra 7. Processus palpable de la septième vertèbre cervicale (médian).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/torso`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Torso Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L22–29.

### M04 — SJN · Confirmé · P2

**Définition originale :** Sternum Jugular Notch. Incisure jugulaire du sternum (médian).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/torso`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Torso Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L30–37.

### M05 — RHGT · Confirmé · P1

**Définition originale :** Glenohumeral Joint. Face postérieure de l’axe de l’épaule, intitulée glenohumeral joint (droite).

**Contradiction ou limite :** Aucun centre glénohuméral profond observé ; XML rattache au torso, pas à humerus. Parent logiciel : `/bodyset/torso`.

**Interprétations possibles :** Landmark superficiel postérieur d’épaule, pas centre profond.

**Conséquence d’une erreur :** Confusion entre peau, ceinture scapulaire et centre glénohuméral.

**Question à l’expert :** Quelle mobilité relative au torso faut-il considérer et quel modèle de centre articulaire serait requis ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Torso Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L38–45.

### M06 — LHGT · Confirmé · P1

**Définition originale :** Glenohumeral Joint. Face postérieure de l’axe de l’épaule, intitulée glenohumeral joint (gauche).

**Contradiction ou limite :** Aucun centre glénohuméral profond observé ; XML rattache au torso, pas à humerus. Parent logiciel : `/bodyset/torso`.

**Interprétations possibles :** Landmark superficiel postérieur d’épaule, pas centre profond.

**Conséquence d’une erreur :** Confusion entre peau, ceinture scapulaire et centre glénohuméral.

**Question à l’expert :** Quelle mobilité relative au torso faut-il considérer et quel modèle de centre articulaire serait requis ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Torso Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L46–53.

### M07 — RUA · Confirmé · P2

**Définition originale :** Upper Arm. Bras, sillon entre les triceps en T-pose (droite).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/humerus_r`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Upper Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L54–61.

### M08 — RHLE · Confirmé · P2

**Définition originale :** Humerus Lateral Epicondyle. Épicondyle latéral de l’humérus (droite).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/humerus_r`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Upper Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L62–69.

### M09 — RRSP · Plausible · P1

**Définition originale :** Radius Styloid Process. Processus styloïde radial selon nom (droite).

**Contradiction ou limite :** Placement source «medial side» : orientation anatomique ambiguë ; ne pas inverser les labels. Parent logiciel : `/bodyset/radius_r`.

**Interprétations possibles :** Styloïde radiale nominale versus indication medial.

**Conséquence d’une erreur :** Inversion des marqueurs du poignet et orientation de main erronée.

**Question à l’expert :** Comment résoudre medial/lateral sans inverser les labels ? Quelle posture de référence et quelle preuve ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Hand Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L70–77.

### M10 — RUSP · Plausible · P1

**Définition originale :** Ulna Styloid Process. Processus styloïde ulnaire selon nom (droite).

**Contradiction ou limite :** Placement source «lateral side» : orientation anatomique ambiguë ; XML rattache à radius et non ulna. Parent logiciel : `/bodyset/radius_r`.

**Interprétations possibles :** Styloïde ulnaire nominale ; placement lateral et parent radius à examiner.

**Conséquence d’une erreur :** Rotation/pronation de l’avant-bras et axe du poignet biaisés.

**Question à l’expert :** Quel côté du poignet et quelle posture définissent le placement ? Le rattachement à radius est-il acceptable pendant ce geste ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Hand Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L78–85.

### M11 — LUA · Confirmé · P2

**Définition originale :** Upper Arm. Bras, sillon entre les triceps en T-pose (gauche).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/humerus_l`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Upper Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L86–93.

### M12 — LHLE · Confirmé · P2

**Définition originale :** Humerus Lateral Epicondyle. Épicondyle latéral de l’humérus (gauche).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/humerus_l`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Upper Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L94–101.

### M13 — LRSP · Plausible · P1

**Définition originale :** Radius Styloid Process. Processus styloïde radial selon nom (gauche).

**Contradiction ou limite :** Placement source «medial side» : orientation anatomique ambiguë ; ne pas inverser les labels. Parent logiciel : `/bodyset/radius_l`.

**Interprétations possibles :** Styloïde radiale nominale versus indication medial.

**Conséquence d’une erreur :** Inversion des marqueurs du poignet et orientation de main erronée.

**Question à l’expert :** Comment résoudre medial/lateral sans inverser les labels ? Quelle posture de référence et quelle preuve ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Hand Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L102–109.

### M14 — LUSP · Plausible · P1

**Définition originale :** Ulna Styloid Process. Processus styloïde ulnaire selon nom (gauche).

**Contradiction ou limite :** Placement source «lateral side» : orientation anatomique ambiguë ; XML rattache à radius et non ulna. Parent logiciel : `/bodyset/radius_l`.

**Interprétations possibles :** Styloïde ulnaire nominale ; placement lateral et parent radius à examiner.

**Conséquence d’une erreur :** Rotation/pronation de l’avant-bras et axe du poignet biaisés.

**Question à l’expert :** Quel côté du poignet et quelle posture définissent le placement ? Le rattachement à radius est-il acceptable pendant ce geste ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Hand Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L110–117.

### M15 — LIAS · Plausible · P1

**Définition originale :** Iliac Anterior Spine; PSIS alias. Épine iliaque antérieure selon texte de placement (gauche).

**Contradiction ou limite :** Alias PSIS dans le tableau contredit anterior/front ; direction retenue seulement comme plausible, pas correction de la source. Parent logiciel : `/bodyset/pelvis`.

**Interprétations possibles :** Texte antérieur ou alias PSIS postérieur ; aucune permutation proposée.

**Conséquence d’une erreur :** Orientation du bassin, repère local et estimation de hanche erronés.

**Question à l’expert :** Quelle définition antérieure/postérieure a réellement été palpée sur AB01 et quelle preuve permet d’écarter l’alias contradictoire ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Waist Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L118–125.

### M16 — RIPS · Plausible · P1

**Définition originale :** Iliac Posterior Spine; ASIS alias. Épine iliaque postérieure selon texte de placement (droite).

**Contradiction ou limite :** Alias ASIS contredit posterior/dimples ; direction retenue seulement comme plausible. Parent logiciel : `/bodyset/pelvis`.

**Interprétations possibles :** Texte postérieur ou alias ASIS antérieur ; aucune permutation proposée.

**Conséquence d’une erreur :** Orientation du bassin et résultats de scaling torso/pelvis biaisés.

**Question à l’expert :** Pouvez-vous établir le site postérieur réel et les signes du repère pelvien, indépendamment de la seule position apparente ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Waist Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L126–133.

### M17 — LIPS · Plausible · P1

**Définition originale :** Iliac Posterior Spine; ASIS alias. Épine iliaque postérieure selon texte de placement (gauche).

**Contradiction ou limite :** Alias ASIS contredit posterior/dimples ; direction retenue seulement comme plausible. Parent logiciel : `/bodyset/pelvis`.

**Interprétations possibles :** Texte postérieur ou alias ASIS antérieur ; aucune permutation proposée.

**Conséquence d’une erreur :** Orientation du bassin et résultats de scaling torso/pelvis biaisés.

**Question à l’expert :** Pouvez-vous établir le site postérieur réel et les signes du repère pelvien, indépendamment de la seule position apparente ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Waist Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L134–141.

### M18 — RTTC · Confirmé · P2

**Définition originale :** Tibial Tubercle. Tubérosité tibiale, point antérieur 2–3 cm sous la patella (droite).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/tibia_r`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Lower Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L142–149.

### M19 — RTH · Confirmé · P2

**Définition originale :** Thigh. Face antérieure de la cuisse, proche de la ligne médiane (droite).

**Contradiction ou limite :** Hauteurs asymétriques droite/gauche conseillées ; pas un centre articulaire. Parent logiciel : `/bodyset/femur_r`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Lower Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L150–157.

### M20 — RFLE · Confirmé · P1

**Définition originale :** Femur Lateral Epicondyle. Épicondyle latéral fémoral (droite).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/femur_r`.

**Interprétations possibles :** Épicondyle cutané versus centre virtuel de genou.

**Conséquence d’une erreur :** Axe et flexion du genou biaisés.

**Question à l’expert :** Quelle méthode de centre/axe de genou est justifiée avec le marqueur médial statique retiré en dynamique ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Lower Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L158–165.

### M21 — RSK · Plausible · P2

**Définition originale :** Superior Knee; Upper Leg. Tibia antérieur près de la ligne médiane selon placement (droite).

**Contradiction ou limite :** Table affiche «Upper Leg / Superior Knee» mais décrit le shin/lower leg : garder ambiguïté documentaire. Parent logiciel : `/bodyset/tibia_r`.

**Interprétations possibles :** Site sur tibia décrit versus Superior Knee/Upper Leg.

**Conséquence d’une erreur :** Affectation de segment incorrecte et erreur liée aux tissus mous.

**Question à l’expert :** Le marqueur est-il bien sur la jambe ? Quelle incertitude de placement et de rigidité accepter ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Lower Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L166–173.

### M22 — RFAL · Confirmé · P1

**Définition originale :** Fibula Ankle Lateral. Malléole latérale (droite).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/tibia_r`.

**Interprétations possibles :** Malléole latérale, pas centre de cheville.

**Conséquence d’une erreur :** Orientation de cheville et appui biaisés.

**Question à l’expert :** Quelle calibration médiale/latérale et quel axe individualisé seraient nécessaires ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Foot Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L174–181.

### M23 — RFCC · Confirmé · P2

**Définition originale :** Foot Calcaneus. Talon, insertion du tendon d’Achille sur le calcanéus (droite).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/calcn_r`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Foot Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L182–189.

### M24 — RDP1 · Confirmé · P1

**Définition originale :** First Distal Phalanx. Extrémité distale du gros orteil (droite).

**Contradiction ou limite :** XML rattache au calcn et non toes ; pas de mesure indépendante de flexion MTP. Parent logiciel : `/bodyset/calcn_r`.

**Interprétations possibles :** Landmark distal d’orteil mais parent calcn et MTP verrouillée.

**Conséquence d’une erreur :** Contact avant-pied et flexion des orteils mal représentés.

**Question à l’expert :** L’approximation rigide calcn–orteil est-elle acceptable pour une analyse des appuis, et pour quelles conclusions seulement ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Foot Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L190–197.

### M25 — RFM5 · Confirmé · P2

**Définition originale :** Foot Fifth Metatarsal. Face dorsale du cinquième métatarsien (droite).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/calcn_r`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Foot Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L198–205.

### M26 — LTH · Confirmé · P2

**Définition originale :** Thigh. Face antérieure de la cuisse, proche de la ligne médiane (gauche).

**Contradiction ou limite :** Hauteurs asymétriques droite/gauche conseillées ; pas un centre articulaire. Parent logiciel : `/bodyset/femur_l`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Lower Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L206–213.

### M27 — LFLE · Confirmé · P1

**Définition originale :** Femur Lateral Epicondyle. Épicondyle latéral fémoral (gauche).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/femur_l`.

**Interprétations possibles :** Épicondyle cutané versus centre virtuel de genou.

**Conséquence d’une erreur :** Axe et flexion du genou biaisés.

**Question à l’expert :** Quelle méthode de centre/axe de genou est justifiée avec le marqueur médial statique retiré en dynamique ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Lower Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L214–221.

### M28 — LSK · Plausible · P2

**Définition originale :** Superior Knee; Upper Leg. Tibia antérieur près de la ligne médiane selon placement (gauche).

**Contradiction ou limite :** Table affiche «Upper Leg / Superior Knee» mais décrit le shin/lower leg : garder ambiguïté documentaire. Parent logiciel : `/bodyset/tibia_l`.

**Interprétations possibles :** Site sur tibia décrit versus Superior Knee/Upper Leg.

**Conséquence d’une erreur :** Affectation de segment incorrecte et erreur liée aux tissus mous.

**Question à l’expert :** Le marqueur est-il bien sur la jambe ? Quelle incertitude de placement et de rigidité accepter ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Lower Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L222–229.

### M29 — LFAL · Confirmé · P1

**Définition originale :** Fibula Ankle Lateral. Malléole latérale (gauche).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/tibia_l`.

**Interprétations possibles :** Malléole latérale, pas centre de cheville.

**Conséquence d’une erreur :** Orientation de cheville et appui biaisés.

**Question à l’expert :** Quelle calibration médiale/latérale et quel axe individualisé seraient nécessaires ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Foot Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L230–237.

### M30 — LFCC · Confirmé · P2

**Définition originale :** Foot Calcaneus. Talon, insertion du tendon d’Achille sur le calcanéus (gauche).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/calcn_l`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Foot Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L238–245.

### M31 — LDP1 · Confirmé · P1

**Définition originale :** First Distal Phalanx. Extrémité distale du gros orteil (gauche).

**Contradiction ou limite :** XML rattache au calcn et non toes ; pas de mesure indépendante de flexion MTP. Parent logiciel : `/bodyset/calcn_l`.

**Interprétations possibles :** Landmark distal d’orteil mais parent calcn et MTP verrouillée.

**Conséquence d’une erreur :** Contact avant-pied et flexion des orteils mal représentés.

**Question à l’expert :** L’approximation rigide calcn–orteil est-elle acceptable pour une analyse des appuis, et pour quelles conclusions seulement ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Foot Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L246–253.

### M32 — LFM5 · Confirmé · P2

**Définition originale :** Foot Fifth Metatarsal. Face dorsale du cinquième métatarsien (gauche).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/calcn_l`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Foot Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L254–261.

### M33 — TV2 · Plausible · P2

**Définition originale :** Thoracic Spine Vertebra 2. Deuxième vertèbre thoracique selon le titre (médian).

**Contradiction ou limite :** Texte dit aussi «three spine levels below C7» : discordance de niveau à vérifier, non corrigée silencieusement. Parent logiciel : `/bodyset/torso`.

**Interprétations possibles :** T2 nominal versus trois niveaux sous C7.

**Conséquence d’une erreur :** Orientation du thorax et registration incohérentes.

**Question à l’expert :** Quel niveau vertébral est visé et existe-t-il une preuve du placement AB01 ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Torso Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L262–269.

### M34 — RIAS · Plausible · P1

**Définition originale :** Iliac Anterior Spine; PSIS alias. Épine iliaque antérieure selon texte de placement (droite).

**Contradiction ou limite :** Alias PSIS dans le tableau contredit anterior/front ; direction retenue seulement comme plausible, pas correction de la source. Parent logiciel : `/bodyset/pelvis`.

**Interprétations possibles :** Texte antérieur ou alias PSIS postérieur ; aucune permutation proposée.

**Conséquence d’une erreur :** Orientation du bassin, repère local et estimation de hanche erronés.

**Question à l’expert :** Quelle définition antérieure/postérieure a réellement été palpée sur AB01 et quelle preuve permet d’écarter l’alias contradictoire ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Waist Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L268–275.

### M35 — LTTC · Confirmé · P2

**Définition originale :** Tibial Tubercle. Tubérosité tibiale, point antérieur 2–3 cm sous la patella (gauche).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/tibia_l`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Lower Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L276–283.

### M36 — RFAX · Confirmé · P2

**Définition originale :** Fibula Apex. Proéminence latérale proximale de la fibula (droite).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/tibia_r`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Lower Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L284–291.

### M37 — LFAX · Confirmé · P2

**Définition originale :** Fibula Apex. Proéminence latérale proximale de la fibula (gauche).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/tibia_l`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Lower Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L292–299.

### M38 — RFTC · Confirmé · P1

**Définition originale :** Femoral greater Trochanter. Proéminence du grand trochanter fémoral (droite).

**Contradiction ou limite :** Source et XML rattachent au bassin malgré repère sur fémur ; hypothèse de rigidité à contester. Parent logiciel : `/bodyset/pelvis`.

**Interprétations possibles :** Landmark fémoral mais rattachement pelvis documenté.

**Conséquence d’une erreur :** Mouvement relatif hanche/fémur absorbé dans le bassin et scaling.

**Question à l’expert :** L’hypothèse FTC solidaire du pelvis est-elle défendable en flexion profonde ? Quel contrôle la contredirait ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Lower Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L300–307.

### M39 — LFTC · Confirmé · P1

**Définition originale :** Femoral greater Trochanter. Proéminence du grand trochanter fémoral (gauche).

**Contradiction ou limite :** Source et XML rattachent au bassin malgré repère sur fémur ; hypothèse de rigidité à contester. Parent logiciel : `/bodyset/pelvis`.

**Interprétations possibles :** Landmark fémoral mais rattachement pelvis documenté.

**Conséquence d’une erreur :** Mouvement relatif hanche/fémur absorbé dans le bassin et scaling.

**Question à l’expert :** L’hypothèse FTC solidaire du pelvis est-elle défendable en flexion profonde ? Quel contrôle la contredirait ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Lower Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L308–315.

### M40 — RFM1 · Confirmé · P2

**Définition originale :** Foot First Metatarsal. Face dorsale du premier métatarsien (droite).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/calcn_r`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Foot Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L316–323.

### M41 — LFM1 · Confirmé · P2

**Définition originale :** Foot First Metatarsal. Face dorsale du premier métatarsien (gauche).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/calcn_l`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Foot Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L322–329.

### M42 — TV7 · Confirmé · P2

**Définition originale :** Thoracic Spine Vertebra 7. Septième vertèbre thoracique (médian).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/torso`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Torso Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L328–335.

### M43 — SXS · Confirmé · P2

**Définition originale :** Sternum Xiphoid Process. Processus xiphoïde ; placement 1–2 cm au-dessus de la jonction des côtes (médian).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/torso`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Torso Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L334–341.

### M44 — RHM2 · Plausible · P1

**Définition originale :** Hand Second metatarsal. Sous l’articulation de l’index selon placement (droite).

**Contradiction ou limite :** Source écrit «Hand Second metatarsal» ; métacarpien paraît cohérent mais non démontré par ce libellé. Offset asymétrique conseillé. Parent logiciel : `/bodyset/hand_r`.

**Interprétations possibles :** Métacarpien sous l’index probable versus mot metatarsal imprimé.

**Conséquence d’une erreur :** Dimension de main, poignet et marqueur virtuel mal interprétés.

**Question à l’expert :** Confirmez-vous le site sur le deuxième métacarpien, l’offset asymétrique éventuel et sa preuve individuelle ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Hand Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L342–349.

### M45 — LHM2 · Plausible · P1

**Définition originale :** Hand Second metatarsal. Sous l’articulation de l’index selon placement (gauche).

**Contradiction ou limite :** Source écrit «Hand Second metatarsal» ; métacarpien paraît cohérent mais non démontré par ce libellé. Offset asymétrique conseillé. Parent logiciel : `/bodyset/hand_l`.

**Interprétations possibles :** Métacarpien sous l’index probable versus mot metatarsal imprimé.

**Conséquence d’une erreur :** Dimension de main, poignet et marqueur virtuel mal interprétés.

**Question à l’expert :** Confirmez-vous le site sur le deuxième métacarpien, l’offset asymétrique éventuel et sa preuve individuelle ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Hand Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L350–357.

### M46 — RAH · Confirmé · P2

**Définition originale :** Anterior Head. Front, côté antérieur (droite).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/head`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Head Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L358–365.

### M47 — LAH · Confirmé · P2

**Définition originale :** Anterior Head. Front, côté antérieur (gauche).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/head`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Head Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L364–371.

### M48 — LPH · Confirmé · P2

**Définition originale :** Posterior Head. Tête postérieure, environ 2 cm derrière l’oreille (gauche).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/head`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Head Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L370–377.

### M49 — RPH · Confirmé · P2

**Définition originale :** Posterior Head. Tête postérieure, environ 2 cm derrière l’oreille (droite).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/head`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Head Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L376–383.

### M50 — RFME · Confirmé · P1

**Définition originale :** Femur Medial Epicondyle. Épicondyle médial fémoral (droite).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/femur_r`.

**Interprétations possibles :** Calibration médiale, pas centre articulaire observé.

**Conséquence d’une erreur :** Estimation de genou non reproductible après retrait.

**Question à l’expert :** Quelle calibration et quelle propagation à la dynamique permettent d’utiliser ce landmark sans assimiler sa position au centre ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Lower Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L382–389.

### M51 — LFME · Confirmé · P1

**Définition originale :** Femur Medial Epicondyle. Épicondyle médial fémoral (gauche).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/femur_l`.

**Interprétations possibles :** Calibration médiale, pas centre articulaire observé.

**Conséquence d’une erreur :** Estimation de genou non reproductible après retrait.

**Question à l’expert :** Quelle calibration et quelle propagation à la dynamique permettent d’utiliser ce landmark sans assimiler sa position au centre ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Lower Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L390–397.

### M52 — LTAM · Confirmé · P1

**Définition originale :** Talus Ankle Medial. Malléole médiale selon placement (gauche).

**Contradiction ou limite :** Titre «Talus Ankle Medial» conservé ; la malléole médiale est tibiale, pas centre de cheville. Parent logiciel : `/bodyset/tibia_l`.

**Interprétations possibles :** Malléole médiale décrite, titre Talus Ankle Medial.

**Conséquence d’une erreur :** Confusion osseuse et centre de cheville incorrect.

**Question à l’expert :** Peut-on confirmer le landmark tibial palpable malgré le titre, et son rôle de calibration uniquement ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Foot Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L398–405.

### M53 — RTAM · Confirmé · P1

**Définition originale :** Talus Ankle Medial. Malléole médiale selon placement (droite).

**Contradiction ou limite :** Titre «Talus Ankle Medial» conservé ; la malléole médiale est tibiale, pas centre de cheville. Parent logiciel : `/bodyset/tibia_r`.

**Interprétations possibles :** Malléole médiale décrite, titre Talus Ankle Medial.

**Conséquence d’une erreur :** Confusion osseuse et centre de cheville incorrect.

**Question à l’expert :** Peut-on confirmer le landmark tibial palpable malgré le titre, et son rôle de calibration uniquement ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Foot Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L406–413.

### M54 — RFM2 · Confirmé · P2

**Définition originale :** Foot Second Metatarsal. Face dorsale du deuxième métatarsien (droite).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/calcn_r`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Foot Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L414–421.

### M55 — LFM2 · Confirmé · P2

**Définition originale :** Foot Second Metatarsal. Face dorsale du deuxième métatarsien (gauche).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/calcn_l`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Foot Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L420–427.

### M56 — RHME · Confirmé · P2

**Définition originale :** Humerus Medial Epicondyle. Épicondyle médial de l’humérus (droite).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/humerus_r`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Upper Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L426–433.

### M57 — LHME · Confirmé · P2

**Définition originale :** Humerus Medial Epicondyle. Épicondyle médial de l’humérus (gauche).

**Contradiction ou limite :** Nom et placement explicitement décrits ; association XML explicite, sans preuve de placement individuel. Parent logiciel : `/bodyset/humerus_l`.

**Interprétations possibles :** Landmark superficiel documenté ; placement individuel et rigidité non démontrés.

**Conséquence d’une erreur :** Orientation, échelle ou suivi du segment biaisés par erreur de placement ou tissus mous.

**Question à l’expert :** Le site palpé, la latéralité et la fixation au segment sont-ils suffisamment documentés pour AB01 ? Quelle incertitude et quelle vérification exigez-vous ?

Source : https://docs.optitrack.com/movement-sciences/movement-sciences-markersets/biomech-57 — Upper Extremity Markers ; article PMC12717423 Figure1/Participant Preparation ; Model/marker_set.xml:L434–441.
