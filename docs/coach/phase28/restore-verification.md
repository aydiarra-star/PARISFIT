# Vérification de restauration — Phase28

**Restauration après chiffrement Phase28 : NON EXÉCUTÉE.** Il n'y a ni ciphertext, ni volumes, ni clé de production confirmée.

## Contrôles réellement exécutés

| Contrôle préparatoire | Résultat |
|---|---|
| SHA256/taille des quatre archives Phase26 | Conforme |
| Lecture des membres des deux tar sources | 1 783 noms/tailles/SHA256 conformes |
| Lecture du supplément Phase26 | 36 fichiers conformes |
| Objets dans le magasin indépendant restauré en Phase26 | 1 779 objets conformes, sans `info/alternates` |
| Comparaison des fichiers sources au manifeste Phase26 | Aucun changement |
| Paquet public existant | 28 fichiers identiques à l'audit précédent |

Les objets Git sont lus depuis `.cache/phase26-work/restored/objects`, avec `GIT_OBJECT_DIRECTORY` et sans alternates. Il s'agit d'une **revalidation de la restauration Phase26**, pas d'une restauration depuis de nouveaux volumes chiffrés. Les tests npm et exploitabilité Phase26 restent des preuves historiques distinctes ; ils ne sont pas présentés comme des tests de sorties déchiffrées Phase28.

## Séquence encore obligatoire

- Mesurer et vérifier chaque volume réel, son ordre et ses SHA256.
- Réassembler et comparer le SHA256 global du chiffré.
- Déchiffrer avec la vraie clé dans un environnement sûr ; refuser toute erreur ou sortie partielle.
- Extraire dans un répertoire neuf et contrôlé, sans écraser les originaux.
- Comparer exactement les 1 783 fichiers à `input-files.csv` et les 1 779 objets à `input-git-objects.csv`, puis les 36 pièces supplémentaires au manifeste dédié.
- Vérifier pack/bundle/refs, lecture des modèles et données, contrôles statiques et régressions applicatives compatibles, sans exécuter d'anciens jobs de capture.
- Conserver les reçus sans clés, mots de passe ni données personnelles superflues. Faire un second test après retéléchargement **seulement si une publication est ensuite autorisée**.

Un PASS du précontrôle n'est pas un PASS de cette séquence. Le test fictif Phase27 n'est pas réutilisé comme preuve de restauration réelle.
