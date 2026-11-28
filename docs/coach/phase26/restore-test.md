# Test de restauration exécuté — Phase26

**Résultat : PASS pour le périmètre local déclaré ; aucune restauration depuis une destination durable n'a été effectuée.**

Destination isolée réelle : `.cache/phase26-work/restored/`, pas seulement une lecture des archives en mémoire. Les originaux n'ont pas été utilisés pour remplacer des fichiers manquants. Les dossiers étaient neufs et les écritures exclusives.

| Contrôle | Résultat |
|---|---|
| Projet courant | 972 fichiers extraits et SHA256 identiques |
| Données de travail/cache | 811 fichiers extraits et SHA256 identiques |
| Pack Git restauré indépendamment | 1 779 objets, dont 1 135 blobs, types/tailles/SHA256 identiques |
| Historique | 158 commits présents dans le magasin restauré |
| Références bundle | 29 entrées, toutes leurs cibles résolues depuis les objets restaurés |
| HEAD extrait depuis le magasin isolé | 901 fichiers reconstruits |
| `index-pack --strict` | PASS |
| `git fsck --full --no-reflogs` | Code retour 0 |
| Régressions `npm test` dans le snapshot restauré | Code retour 0 |
| Comparaison modèle statique / original restaurés | PASS |
| Refs et fichiers source après copie/restauration | Inchangés |

Le magasin utilise `GIT_OBJECT_DIRECTORY` avec `GIT_ALTERNATE_OBJECT_DIRECTORIES` vide, et aucun fichier `info/alternates`. Cela évite de réussir grâce à des objets trouvés dans le dépôt original. La correspondance objets source/restaurés couvre aussi trees et commits, pas uniquement les blobs à HEAD. Les références sont sauvegardées dans le bundle et les manifestes ; aucun autre dépôt ni branche n'a été créé pour cette vérification.

Les tests utilisent Node/Python présents dans le sandbox. Il ne s'agit pas d'un test sur machine vierge, d'une installation reproductible de tous les outils scientifiques, d'une réouverture des services GitHub, ni d'une restitution des commentaires/Actions distants. Les dépendances scientifiques éventuellement exclues restent à réinstaller avec leurs versions documentées. Les tests navigateur/phones physiques ne sont pas répétés pour cette phase de sauvegarde.

Preuves : `archive-register.json`, `git-object-manifest.json`, `restored-git-fsck.json`, `restored-regression-output.txt`, `restored-static-output.txt`. Le supplément des rapports Phase26 possède sa propre vérification de restauration, consignée séparément après sa création.

**Ne pas transformer ce PASS local en « sauvegarde complète du compte » ou « sauvegarde durable ».** Les artefacts distants manquent et la copie restaurée partage le même disque éphémère que les sources.
