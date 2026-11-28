# Manifeste des entrées Phase28 — chiffrement bloqué

**Aucun volume chiffré produit.** Les seules entrées admissibles sont les quatre archives Phase26 ci-dessous, relues et vérifiées pendant Phase28.

| Archive Phase26 | Octets | SHA256 vérifié |
|---|---:|---|
| `project.tar.gz` | 49301585 | `7024251fceed7563faf5c68a9b683b97d444be9a362e8c407a47132827cc2577` |
| `working-data.tar.gz` | 307746695 | `7f103cf14e4074557251c9bcb53286ae565f8aaaa3e3aeccc86fc4f52be793f0` |
| `history.bundle` | 30951764 | `bd132c42272e2a8a450a802493281579cb74aa98daba7f1867763284ef37e217` |
| `phase26-evidence.tar.gz` | 270649 | `2f2d6a800272f68a3dcbdff9a557a6b1c45b3c3ebe26a368f79237619b37115d` |

## Identification exacte du périmètre

- `input-files.csv` : **1 783 lignes de fichiers**, chemin exact, taille, SHA256 et archive d'appartenance ; 972 fichiers de `project.tar.gz` et 811 de `working-data.tar.gz`. Leurs membres sont relus depuis les archives, avec comparaison de l'ensemble des noms et des hashes, et les sources demeurent identiques.
- `input-git-objects.csv` : **1 779 lignes d'objets Git**, identifiant Git, type, taille et SHA256. Le bundle contient 158 commits, 29 entrées de références (HEAD compris), 1 135 blobs. Le SHA du bundle a été recontrôlé ; tous les objets du magasin isolé restauré en Phase26 ont été relus et comparés.
- `phase26-evidence.tar.gz` : **36 fichiers supplémentaires de preuves/outils**, tous relus et comparés au reçu Phase26. Ils ne sont pas ajoutés artificiellement au chiffre des 1 783 fichiers de travail.
- Le détail des refs demeure dans les manifestes Phase26. La branche actuelle et HEAD sont consignés dans `preflight-result.json`.

Les identifiants Git utilisent le format du dépôt ; les empreintes de contenu sont les SHA256 des octets. Ne pas confondre SHA d'un objet Git, SHA256 d'un fichier et SHA256 d'une archive.

## Manques et exclusions

**216 artefacts Actions absents en contenu de cette sauvegarde**, connus par métadonnées Phase26 seulement. Les trois essais avaient échoué ; les 213 autres n'avaient pas été testés individuellement. Aucun nouvel essai Phase28 ni déclaration implicite de récupération. Les rapports locaux issus d'anciens essais ne sont pas réputés égaux aux ZIP distants complets.

Les archives n'incluent pas rétroactivement tous les changements Phase27/28, credentials, commentaires/issues/wiki complets ni refs cachées. L'objectif demandé de reprendre exclusivement Phase26 est respecté ; aucun élargissement silencieux du périmètre.

## Statut des volumes

`volume-checksums.txt` est un **avis de non-production**, pas un fichier de validation utilisable. Aucun numéro de volume ou hash chiffré n'est inventé. Les tailles/21 volumes estimés Phase27 ne sont pas des résultats réels Phase28.

Les archives sources restent dans `.cache/phase26-work/backups/`, temporaires, non chiffrées et non transférées. Leur intégrité vérifiée ne les rend ni privées au sens d'un stockage externe durable, ni sauvegardées sur GitHub.
