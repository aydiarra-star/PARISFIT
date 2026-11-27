# Plan d'évaluation préétabli — première capture dédiée

Objectif : un seul squat complet, pas un mouvement standard imposé à la source. Ce document précède toute capture dédiée. Aucun seuil ne doit être relevé a posteriori simplement pour accepter un clip.

| Phase | Fidélité / articulations à revoir | Appuis / erreurs à rechercher |
|---|---|---|
| Debout initial | orientation bassin/tronc, pieds, posture propre au participant | deux pieds, position et orientation initiales, pas de téléportation |
| Descente | timing hanche/genou/cheville, tronc/bassin, épaules/bras/mains | talon/avant-pied et roulement observés ; ne pas imposer pied plat si ce n'est pas capturé |
| Bas | profondeur réellement observée, torsion genou/hanche, alignements | contact/float/pénétration, collisions cuisses/vêtements/mains, compression du skinning |
| Remontée | coordination et vitesse comparées au film, pas inversion forcée de la descente | transfert de poids, glissement, correction qui change la capture |
| Retour debout | récupération naturelle, arrêt/repositionnement éventuel conservé | pas de blend artificiel vers une pose initiale différente ; boucle non supposée |

## Quatre décisions distinctes

1. **Technique** : données intègres et consenties, timestamps, calibration avec résidus et échelle connus, import/export stables, toutes frames finies, proportions constantes ; passage Blender→GLB→Three.js comparé. Le préflight ne suffit pas.
2. **Fidélité** : reprojections 2D sur les deux films au même temps, erreurs par joint et confiance/occlusion ; rotations source vs cible, événements de contact et amplitude/timing. L'incertitude doit être chiffrée avant de fixer un budget. Pas de seuil millimétrique universel sur un estimateur monoculaire.
3. **Visuel** : examen humain du cycle entier à vitesse réelle et ×0,5, face/profil/trois-quarts, gros plans chevilles/genoux/mains. Surface skinnée sans pli anormal, étirement, intersections ou pieds flottants ; pas seulement squelette ou minimum de sol. Absence de pénétration visible exigée. Mesures millimétriques : diagnostic, pas permission de traverser le sol.
4. **Pédagogique/sportif** : professionnel réellement qualifié, avis daté lié au hash, variante et consignes, limites du public et réserves. Aucune validation médicale ou sécurité universelle déduite.

## Mesures à enregistrer

Conservation des segments (budget numérique 0,1 mm), quaternions unitaires et continus, distributions/max de vitesses/accélérations linéaires et angulaires, différence avant/après correction. Les plafonds de pompe lente phase7 ne sont **pas** réutilisés comme normes de squat. Définir les plages selon le rythme capturé et l'avis compétent ; pics déclenchent inspection de source, pas filtrage automatique.

Contacts : patches anatomiques semelle (talon/métatarses) distincts du pivot, normale/orientation, hauteur/dérive par fenêtre **relue dans la source**, durée et transitions. Ne pas corriger en phase mobile/aérienne/incertaine. Mains non portantes dans ce squat : contrôler geste et collisions, ne pas les ancrer au sol.

Contrôles de raccord ultérieurs : entrée/sortie, supports, orientation, collisions et récupération avec les exercices existants ; aucun essai d'intégration avant qualité du clip. Aucun nouveau mouvement activé automatiquement. Avis professionnel, capture dédiée et téléphones physiques restent absents.
