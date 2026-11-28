# Audit transversal phases 1 à 6

| Phase / preuves conservées | Ce qui fonctionne | Ce qui ne démontre pas la qualité |
|---|---|---|
| [1](../REPORT.md) | Rocketbox skinné humain, licence MIT, rendu Three.js et 8 exercices | Animations originales procédurales, pas mocap ; visage génération temps réel, pas coach filmé |
| [2](../phase2/REPORT.md) | 64 vidéos, corrections paumes/doigts, trajectoires lentes, mesures continues, mobile émulé | IK et interpolation quintique peuvent immobiliser un appui sans transfert de poids humain ; poignets et amplitude non approuvés |
| [3](../phase3/REPORT.md) | Isolation des candidats, revue préparée | Proximité de poses ≠ transition valide ; aucun avis professionnel |
| [4](../phase4/REPORT.md) | Admission fermée par défaut ; contrats de contacts, conservation des résultats | Fenêtres d'appui hypothétiques ; minima de groupes de peau ≠ vraie surface palmaire ; boucle ≠ récupération |
| [5](../phase5/REPORT.md) | Provenance vidéo/optique distinguée, extraction reproductible, résultats négatifs | Vidéo monoculaire : pieds hors cadre, profondeur ambiguë, équipement ; direction-only BVH perd torsion axiale |
| [6](../phase6/REPORT.md) | Quaternions complets, calibration axes, longueurs fixes, source/retarget/correction comparés | T-pose/axes primaires ne règlent pas toute torsion ; bruit source orteils ; 8,59 mm pénétration, ~48 mm float ; petites fenêtres IK généraient 86,51 m/s² |

## Causes récurrentes

- **Entrée insuffisante** : donnée résolue sans marqueurs/confiance/vidéo synchronisée. Le solveur ne peut deviner si un orteil monte volontairement ou si le tracking est faux.
- **Calibration** : confondre axes locaux des deux rigs provoque replis ; aligner un axe ne définit pas le roulis. Il faut une base anatomique et une pose de calibration contrôlée, pas un réglage visuel par clip.
- **Proportions** : conserver les os du modèle tout en copiant les angles change l'emplacement des effecteurs. La reproduction des angles et le respect de plusieurs appuis sont des contraintes parfois incompatibles.
- **Pieds** : le minimum de peau n'identifie pas talon/métatarses ; le roulement volontaire n'est pas du glissement. Trois points éloignés sont mieux qu'un pivot, mais les patches doivent être annotés.
- **Mains** : pas de reconstruction détaillée des doigts dans les sources retenues ; wrist pivot ≠ paume ; fingers/floor demandent patch palmaire et orientation, pas un seul point.
- **Continuité** : un cycle auto-identique peut être artificiel ; les huit exercices ont des positions incompatibles avec les nouveaux clips. Pas de blend pour dissimuler cette incompatibilité.
- **Rig Rocketbox** : 80 os et modèle humain redistribuable constituent une base réelle. Pas de muscles/forces, pas de corrective shapes démontrées ici ; skinning et proportions limitent les articulations extrêmes. Changer le modèle ne répare pas une source mal calibrée.

Conclusion : préserver provenance, axe, timing et incertitude avant toute correction. Séparer intégrité de fichier, fidélité du mouvement, contacts, qualité pédagogique et acceptation finale. Aucun des six dossiers ne permet de cocher « méthode premium validée ».
