# Blender : diagnostic précis, correction préparée mais non exécutée

## Ce qui a réellement tourné

Python 3.11.2 / glibc 2.36 ; bpy 4.2.0 installé. `ldd` puis import dans un sous-processus : échec code 1. Rapport complet `environment-report.json`.

| Bibliothèque introuvable | Paquet Debian Bookworm prévu |
|---|---|
| libXrender.so.1 | libxrender1 |
| libXxf86vm.so.1 | libxxf86vm1 |
| libXfixes.so.3 | libxfixes3 |
| libXi.so.6 | libxi6 |
| libxkbcommon.so.0 | libxkbcommon0 |
| libSM.so.6 | libsm6 |
| libICE.so.6 | libice6 |
| libGL.so.1 | libgl1 |

Ni `blender`, ni `docker`, ni `podman` présents dans PATH. Le chargement échoue **avant** l'import BVH ; le mode background supprime le besoin d'afficher une fenêtre, pas le besoin de résoudre les bibliothèques partagées.

Tentatives locales sans modification système : récupération d'une release Xrender via API GitHub (redirection vers release-assets.githubusercontent.com inaccessible), inspection des dépendances embarquées dans les wheels OpenCV 4.11.0.86 et pygame 2.6.1, et paquet Chromium 119.0.2. Aucun ensemble complet compatible trouvé. Les paquets ont seulement été téléchargés dans le cache, pas installés à la place des dépendances existantes. Pas de fausses bibliothèques/stubs, pas de suppression des liens GL, pas de résultat simulé.

## Environnement isolé proposé

`tools/capture-pipeline/Dockerfile` : Python 3.11 Bookworm + huit bibliothèques et dépendances de base + bpy 4.2.0 / NumPy 1.26.4. Le build inclut un `import bpy` obligatoire. **Dockerfile non construit ici**. Version de base encore taguée et apt non figé : recette reproductible fonctionnelle à qualifier, pas build hermétique certifié. Après premier succès, figer digest image, snapshot apt et inventaire des wheels.

Sur une machine autorisée disposant de Docker et des accès aux dépôts (pas dans cette session) :

```sh
docker build -f tools/capture-pipeline/Dockerfile -t parisfit-blender-smoke .
mkdir -p /tmp/parisfit-smoke-out
docker run --rm --network none \
  --mount type=bind,src="$PWD",dst=/work,readonly \
  --mount type=bind,src=/tmp/parisfit-smoke-out,dst=/out \
  parisfit-blender-smoke --out /out
```

Ne pas monter les vidéos/consentements dans ce test. Ne pas exécuter d'installation sur un ordinateur tiers sans autorisation.

## Test simple fourni

`blender-smoke.py` utilise le BVH CMU14_06 déjà conservé phase6, importe le squelette, crée un rig test de proportions uniformément modifiées ×1,03, transfère l'animation locale dans les mêmes axes et bake/exporte un GLB. Ce n'est **ni Rocketbox ni une capture dédiée**, ni un solveur anatomique général. But limité : vérifier import/BVH, transfert inter-rigs, bake et GLB dans un Blender fonctionnel.

L'appel a été tenté ici et a échoué à `import bpy` (code 2) ; `blender-smoke-report.json` conserve cet échec. Aucun `smoke.glb` n'est livré. Après succès ailleurs, recharger ce GLB dans Three.js et vérifier durée, rotations et positions ; ne pas déclarer ce test validé uniquement parce qu'un fichier est créé.

Retargeting Rocketbox, IK par patches anatomiques, corrections de contact et export skinné restent à exécuter sur la **nouvelle capture qualifiée**. L'étude phase7 conserve les contraintes : calibration multi-axes, RAW/CORRECTED séparés, pas de projection au sol image par image ni lissage non documenté.
