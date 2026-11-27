# Fiche quantitative du squat — critères de triage, pas normes cliniques

**Statuts : VALIDÉ (périmètre nommé seulement), REFUSÉ, NON TESTÉ, EN ATTENTE DE VALIDATION HUMAINE.** Aucun succès d'export n'autorise PARISFIT. Les seuils sont versionnés dans `tools/biomechanics/criteria.json` avant la relance finale. Ils ne sont pas des limites physiologiques applicables à toute personne.

| Contrôle | Seuil / méthode | Justification et limite |
|---|---|---|
| Géométrie finie | 80 os, même ensemble à chaque frame, parents sans cycle ; mètres/Y-up ; coordonnées finies <100m | Contrat de cette fixture de2,4s ; une autre hiérarchie est refusée, pas renommée automatiquement |
| Longueurs osseuses | erreur maximale0,1mm | Budget numérique pour un rig rigide, pas preuve de justesse anatomique ou de skinning |
| Sol | pénétration maximale3mm | Déclencheur millimétrique de défaut visible. Ce n'est pas une permission de pénétrer le sol : tout défaut visible reste à revoir, même sous ce seuil. Référentiel du sol à calibrer |
| Appuis | gap5mm et dérive5mm comme budgets de revue ; candidat si vitesse horizontale≤80mm/s et hauteur entre−3 et15mm | Budgets proposés pour le laboratoire, non vérité terrain. Mesurés par trois points de peau fixes ; un pied mobile ne devient pas « glissant » par définition. Fenêtres non relues : statut humain en attente, jamais automatique |
| Continuité spatiale | pas≤50mm par frame à60Hz | Alarme grossière de saut/teleport ; une bonne continuité ne garantit pas la dynamique |
| Rotations | quaternion unitaire à0,001 près ; variation≤10°/frame à60Hz | Alarme de saut de rotation. Un quaternion ne fournit pas des axes anatomiques calibrés ; torsions axiales cliniques NON TESTÉES |
| Vitesse / accélération | plafonds de triage2m/s et20m/s² pour ce mouvement lent | Budgets conservateurs de triage, non normes professionnelles. Les valeurs initiales3m/s et40m/s² ont été resserrées à2 et20 avant le rapport final, sans augmenter les seuils pour absorber les pics du CMU. Les dérivées amplifient le bruit ; dépassement→inspection de la source, pas lissage automatique. À réexaminer professionnellement selon la cadence réelle |
| Genou | flexion géométrique non signée0–165° | Filtre large de configurations extrêmes, pas une prescription d'amplitude. Ne détecte pas à lui seul hyperextension, valgus, torsion ou sécurité |
| Hanches / chevilles / coudes / tronc | plages géométriques et inclinaison du tronc enregistrées | Proxies 3-points documentés, pas décomposition anatomique des degrés de liberté ; pas de seuil clinique inventé |
| Bassin | vitesse/accélération et continuité mesurées avec les autres articulations | Pas d'équilibre ou stabilité musculaire déduits |
| Symétrie | différence de flexion des genoux15° uniquement si attendue/annotée | NON TESTÉ comme critère sur ce CMU faute annotation ; aucune symétrisation forcée |
| COM/équilibre | COM heuristique et projection dans l'enveloppe convexe des points des pieds, AABB aussi rapportée | Poids fixes non individualisés, points de contact non confirmés, pas de forces. EN ATTENTE DE VALIDATION HUMAINE, jamais « équilibre validé » |
| Collisions | chevauchements de sphères sur quelques paires non adjacentes | Candidats grossiers avec faux positifs/négatifs ; collision exhaustive des surfaces NON TESTÉE |
| Raccords | écart géométrique entrée/sortie mesuré | Ni boucle ni raccord à un exercice admis. Supports, orientation, collisions et récupération restent à examiner |
| Fidélité / visuel / pédagogie | films synchronisés et avis humain liés au hash requis | Face/profil, cycle complet et ralenti ; consignes cohérentes avec la variante réellement capturée. Aucun avis obtenu |

## Phases à examiner

Debout initial, descente, passage bas, remontée, retour debout. Examiner bassin/tronc, hanches, genoux, chevilles, talon/avant-pied, épaules/mains. Les bras ne sont pas des appuis au sol pour ce squat. Ne pas créer de plateau bas ou effacer un repositionnement de pied pour correspondre à une consigne.

## Estimations explicites

COM = moyenne pondérée de milieux de segments : tronc0,50, tête/cou0,08, chaque cuisse0,10, chaque jambe0,05, chaque bras entier0,06. **Heuristique de développement non anthropométrique validée**, volontairement exposée. Le centre de masse véritable et les forces au sol ne sont pas mesurés. L'enveloppe des deux pieds suppose les contacts, elle ne les prouve pas. Une projection intérieure ne vaut pas validation dynamique.

Genou/coude =180°−angle des trois pivots. Hanche proxy =180°−angle(Spine,Thigh,Calf) ; cheville proxy=angle(Calf,Foot,Toe0). Inclinaison du tronc =angle(Pelvis→Neck, verticale). Ces angles sont utiles pour comparer deux exports identiques, insuffisants pour une conclusion biomécanique clinique.

## Décision

Toute donnée corrompue bloque la chaîne. Toute géométrie non conforme reste REFUSÉE à l'admission. Les exports de diagnostic rejetés restent isolés ; même si les filtres passent, l'absence de revue de fidélité/contacts/visuel/pédagogie/récupération empêche l'intégration. Les booléens de critères ne sont pas un mécanisme d'approbation professionnelle.
