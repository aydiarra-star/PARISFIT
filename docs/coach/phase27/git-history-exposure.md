# Exposition existante — inventaire Phase27

## Méthode et périmètre

Nouvelle comparaison des refs annoncées, de tous les arbres des **158 commits** accessibles et des pointes locales/distantes/PR déjà récupérées. Les **1 158 couples chemin/blob** correspondent exactement à l'inventaire Phase25 ; pas de nouvelle branche ni modification d'histoire. `history-versions.json` indique, **pour chaque version**, SHA256, blob Git, commit témoin, présence à HEAD, présence dans main, existence du chemin dans le worktree, toutes les refs de pointe concernées et statut historique seul.

La branche distante actuelle reste `arena/a03f64da-parisfit` à fc51383 ; les travaux Phase24–27 restent locaux/non poussés. Une branche de PR publique est accessible sans fusion. `main` n'a pas les six GLB à sa pointe ; cela ne protège pas les autres branches du même dépôt.

## 1 — Dernier commit de la branche actuelle

901 fichiers : six GLB animés, deux BVH, 141 vidéos, 488 rapports/données de preuves, 220 outils/tests et 44 fichiers application/infrastructure selon la classification Phase25.

GLB :
- `assets/coach/coach.glb` (huit clips), SHA256 `1fc67dc3453d6c0eae589ef3203923f52b4db303c0c9e73714e174cba5d398bb`.
- `docs/coach/phase5/mocap-prototype.glb`, `video-prototype.glb`.
- `docs/coach/phase6/retargeted.glb`, `corrected.glb`.
- `docs/coach/phase7/prototype.glb`.

BVH : `docs/coach/phase6/source-14_06.bvh`, `source-22_14.bvh`. Hashes et refs exacts dans l'inventaire, GLB regroupés dans `glb-exposure.json`. Les captures C3D originales identifiées en Phase25/26 restent locales dans `.cache`, pas retrouvées sous extension C3D dans les refs Git examinées ; leurs dérivés dans rapports/logs/artefacts restent à considérer.

## 2 — Versions uniquement historiques

**204 versions** ne sont présentes à aucune pointe de ref examinée mais restent accessibles via l'histoire : 117 versions application/infrastructure, 81 outils/tests, cinq rapports/preuves et une version GLB.

Le GLB antérieur au chemin `assets/coach/coach.glb` reste dans l'histoire : blob `d8886d09129913ae4830f4a81cd6dc1c6331bb68`, SHA256 `5a999b3dc005d089704da1829690bdecfe7a6fd753c4d82e300617966c967311`. Remplacer ce fichier à HEAD n'a pas retiré cette version. Liste détaillée : `historical-only-versions.json`.

## 3 — Chemins retirés mais encore récupérables

Huit chemins sont absents de **toutes les pointes** examinées mais récupérables dans des commits : fichiers `.pyc` de `tools/passive-qualification/__pycache__/` : `acquire`, `analyze`, `build`, `evidence`, `mapping`, `metrics`, `static_diagram`, `test_metrics` (suffixe `cpython-311.pyc`). Ils ne sont pas déclarés effacés du dépôt. Les événements de suppression Git sont conservés dans `deletion-events.txt`.

Sept autres chemins sont absents de HEAD mais encore présents sur d'autres pointes : `API_CONTRACT.md`, `AUTH_SYNC_SECURITY.md`, `BACKEND_DECISION.md`, `DATA_MODEL.md`, `database/0001_core_schema.sql`, `scripts/validate.mjs`, `tests/structure.test.mjs`. Cela distingue une absence sur cette branche d'un retrait partout.

## 4 — Actions et copies hors inventaire

Phase26 : **216 artefacts connus par métadonnées, zéro contenu ZIP récupéré**, trois téléchargements infructueux. Pas de nouvelle récupération tentée Phase27. Cette observation historique n'est pas une garantie de disponibilité actuelle ; les expirations doivent être revérifiées avant une sauvegarde réelle. Les fichiers locaux copiés ne sont pas automatiquement des copies complètes de ces artefacts.

Branches récupérées : 12 distantes ; refs PR : 13 ; tags annoncés : zéro. Refs cachées/supprimées côté serveur, caches, anciens clones et téléchargements ne sont pas exhaustivement observables. Un zéro fork au dernier audit ne garantit pas un zéro copie.

## Conclusion de sécurité

Chiffrer de **nouvelles** archives ne protège **aucun de ces originaux déjà publics**. Ni l'ajout d'un coffre, ni `.gitignore`, ni une suppression dans un futur commit ne révoquent les anciennes versions. Tant que le dépôt/histoire correspondant reste public, leur confidentialité globale est impossible à affirmer. Aucune suppression, purge ou modification de visibilité n'a été effectuée pour cet audit.
