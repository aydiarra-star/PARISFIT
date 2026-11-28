# Étude Blender — intégration non validée

## Exécution réelle

`bpy==4.2.0` présent dans la venv ; `import bpy` échoue : `libXrender.so.1` absent. `ldd` signale aussi Xxf86vm, Xfixes, Xi, xkbcommon, SM, ICE, GL. L'essai de récupération de dépendances via les releases GitHub échoue (curl 35). Aucune bibliothèque système n'a été remplacée. `blender-report.json` conserve l'erreur produite par `blender-stage.py`, code de sortie 2.

**Aucun BVH retargeté dans Blender, aucun IK Blender, aucun nettoyage Blender, aucun export Blender réussi.** Le GLB livré provient de Three.js. Le script préparé n'est qu'un adaptateur d'aller-retour GLB, pas un solveur de retargeting. Il doit être testé dans une installation Blender complète avant toute utilisation. Ne pas présenter l'étude comme un pipeline Blender fonctionnel.

## Architecture cible et raisons

1. Import BVH dans une collection SOURCE immuable, frame rate natif et axes explicités. Le [manuel 4.2](https://docs.blender.org/manual/en/4.2/addons/import_export/anim_bvh.html) documente Scale FPS, mise à jour FPS et axes ; une frame source par frame scène sans conversion correcte modifie la vitesse.
2. Collection TARGET : import Rocketbox, bind matrices figées, unités mètres. Base anatomique définie par plusieurs repères (axe long + axe de flexion), puis calcul des offsets. Valider avec T-pose et flexion connue ; éviter un simple Copy Rotation local entre rigs différents.
3. Retarget FK des rotations complètes + translation root proportionnée ; bake sur action RAW séparée. Vérifier longueurs et fidélité avant contacts.
4. Action CORRECTED séparée, contraintes IK bras/jambes seulement sur fenêtres **annotées et relues**. Pole vectors contrôlés ; influence rampée ; préserver le mouvement des pieds/paumes pendant les transitions d'appui. Plusieurs patches paume/semelle, pas seulement un pivot. Refuser si la solution exige des déformations ou une correction majeure du tronc.
5. Nettoyage quaternion : choix d'hémisphère sans changement de pose. Lissage temporel désactivé par défaut ; si nécessaire, filtre documenté avec bande passante, résidus angulaires/spatiaux et préservation des événements de contact. Pas de filtre choisi uniquement pour faire baisser une accélération maximale.
6. Ajustements manuels : fichier de patch (articulation, intervalle, avant/après, auteur, justification) et nouvelles preuves ; jamais une modification silencieuse du BVH original.
7. Bake visuel des contraintes vers rig de déformation, retrait des contrôleurs du fichier exporté, GLB avec frames/temps vérifiés. Recharger **dans Three.js**, comparer matrices et peau avant/après à 60 Hz ; Blender seul n'est pas le validateur de son export.

Le prototype actuel teste seulement le chemin contrôle GLB → rééchantillonnage → export → Three.js. Les étapes 1–6 restent à implémenter et qualifier dans Blender. Aucun add-on commercial acheté.

## Licence et environnement reproductible proposé

[Blender](https://www.blender.org/about/license/) : GPL pour le logiciel, usage commercial des œuvres permis, sans lever les restrictions des assets importés. Version ciblée : Blender 4.2.0 / bpy 4.2.0, Python 3.11. Un conteneur complet avec bibliothèques X/GL et un test de démarrage est nécessaire ; **aucun conteneur clean-room fonctionnel n'est livré**. Les scripts, manifeste, rapports et erreurs sont versionnés, pas les bibliothèques téléchargées ou caches.
