# Inventaire des ressources — Phase25

## Périmètre et exhaustivité

Inventaire systématique des **1 739 fichiers** du projet et cache de travail présents avant les ajouts Phase25 : **489 903 558 octets**, chemin, taille, SHA256 et catégorie dans `worktree-inventory.json`. Le cache est ignoré par Git, pas forcément privé au sens d'une sauvegarde durable. Dépendances installées, `.git` interne, `.venv`, `node_modules`, bytecode et fichiers créés par cet audit sont exclus. Les objets Git accessibles sont inventoriés séparément dans `history-inventory.json`.

La classification par chemin/format aide à trier ; elle ne prouve ni confidentialité, ni anonymisation, ni droits. Des trajectoires peuvent être dans JSON/CSV ou des logs encodés, et pas seulement dans des C3D/BVH. Les rapports/JSON sont donc internes par défaut, même lorsque leur licence autorise la redistribution.

| Famille actuelle, cache inclus | Fichiers |
|---|---:|
| GLB | 8 (7 animés, 1 statique) |
| Captures/modèles biomécaniques BVH, C3D, FBX, OSIM | 16 |
| Vidéos | 181 |
| Archives | 6 |
| Rapports, preuves et données de travail | 1 249 |
| Outils diagnostiques et tests | 233 |
| Application/infrastructure | 46 |

Les catégories sont disjointes. Le JSON donne la liste complète, sans limiter l'inventaire à ces nombres.

## Modèles animés et captures

Six GLB animés sont présents dans l'arbre suivi de la branche :
- `assets/coach/coach.glb` : huit clips, original Rocketbox PARISFIT.
- `docs/coach/phase5/mocap-prototype.glb` et `video-prototype.glb` : un clip chacun.
- `docs/coach/phase6/retargeted.glb` et `corrected.glb` : un clip chacun.
- `docs/coach/phase7/prototype.glb` : un clip.

Le cache contient également `.cache/phase2/before.glb` (huit clips) et `.cache/public/assets/coach/coach-static.glb` (**zéro animation**).

Deux BVH sont suivis : `docs/coach/phase6/source-14_06.bvh`, `source-22_14.bvh`. Copies/trials supplémentaires : `.cache/phase5/cmu-22_14.bvh`, `.cache/phase6/cmu-14_06.bvh`, `.cache/phase12/{13_30,14_14,86_08}.bvh`.

Deux C3D existent localement : `.cache/phase17/source/AB01/Squat/1/Data/squat_1.c3d` et `AB01/Static/1/Data/static.c3d`. **Aucun blob Git portant l'extension C3D n'est trouvé dans les refs récupérées** ; cela ne signifie pas que leurs données dérivées ou encodées n'ont jamais été exposées dans des rapports/logs/artefacts. Modèles locaux : `LaiUhlrich2022.osim`, `Biomech57.osim`. Cinq FBX locaux : Rocketbox Sports_Male_04 et quatre entrées/sorties crouch Phase3.

126 entrées d'archives inventoriées, hashes des fichiers internes dans `nested-archive-inventory.json`. Une archive vide `.cache/phase8/xrender.tar.gz` (0 octet) ne peut être ouverte ; conservée et signalée, non remplacée. Bibliothèques binaires compressées dans les archives d'outillage non décompressées récursivement à profondeur illimitée.

## Public nécessaire / interne

**Public autorisé : les 28 fichiers exactement énumérés dans `publication-verification.json`.** Shell HTML/CSS/JS, registre non approuvé, manifeste/icône, illustrations et huit aperçus fixes, Three/loader/utilitaire/OrbitControls, licence Rocketbox, GLB statique. Bibliothèques Three partagées nécessaires au rendu ≠ lecteur diagnostique publié. Le GLB source animé n'est nécessaire qu'à la fabrication contrôlée du dérivé, pas au navigateur.

**Interne :** tous les GLB animés, BVH/C3D/FBX/OSIM, données de marqueurs/forces et calculs, vidéos d'audit, rapports/préuves scientifiques, outils `tools/`, tests, caches, archives et logs. Les diagnostics comportent notamment `tools/coach-lab.html`, lecteurs Phase5/6/7 et galeries de preuves. L'absence d'intégration publique ne vaut pas interdiction juridique générale de redistribution : la décision de diffusion reste distincte des licences.

## Confidentialité, données personnelles et droits

- Scan heuristique de 1 135 blobs Git et des textes locaux : **aucun motif de clé privée, token GitHub, clé AWS ou affectation littérale de credential trouvé**. Pas un audit de secrets certifié : formats non couverts, contenus binaires/compressés/encodés et services externes limitent la conclusion.
- Motifs email dans 26 versions de blobs et 19 fichiers locaux ; principalement contacts professionnels publics Phase22, licences et code historique. Les résultats ne reproduisent pas les adresses. Métadonnées de commits : trois identités email distinctes, non recopiées ici. Un email public reste une donnée personnelle ; publication à minimiser et finalité à préserver.
- Données de mouvement humain, identifiants pseudonymes AB01/S01/P001, trajectoires et forces : **ne pas déclarer anonymes** au seul motif de l'absence de nom. Pas de nouvelle capture privée ni consentement inventé. Les formulaires d'expertise historiques restent sans réponses professionnelles fabriquées.
- Rocketbox : licence MIT et copyright conservés ; cela ne valide pas biomécaniquement les clips.
- CMU/BVH : conditions historiques autorisant certains usages commerciaux mais interdisant la revente des données seules ; attribution et provenance conservées.
- Michaud : licence du dataset CC BY 4.0 documentée, distincte des droits de personnalité et de composants de modèles. AB01 : article CC BY-NC-ND distinct du dataset annoncé CC BY 4.0 ; ne pas étendre une licence à l'autre.
- Phase7 comprend des notices **BANDAI-NC**, LAFAN et MakeHuman : la présence d'une notice ne prouve pas que chaque fichier dérivé est libre commercialement. Conserver ces éléments dans l'archive interne ; vérifier source exacte/version et chaîne de droits avant une nouvelle diffusion.
- Vidéos : rendus de diagnostic et sources éventuelles à qualifier individuellement ; aucun visionnage intégral des 181 vidéos n'est prétendu ici. Un fichier vidéo déjà public ne vaut pas autorisation de republication.

Les fichiers `sensitivity-findings.json` et `worktree-sensitivity.json` listent uniquement chemins/types/comptages, pas les valeurs détectées. Aucun secret trouvé n'est présenté comme « définitivement absent ».
