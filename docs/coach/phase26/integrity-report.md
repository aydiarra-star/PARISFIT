# Intégrité — Phase26

**Trois archives locales créées, vérifiées et restaurées. Durabilité : NON.**

Date de session : 2026-11-27. Les horodatages ci-dessous proviennent de l’horloge observée du sandbox, qui indique 2026-11-28 UTC ; cette divergence est explicitée, pas corrigée silencieusement.

| Archive | Octets | Fichiers | Création UTC observée | Restauration |
|---|---:|---:|---|---|
| `project.tar.gz` | 49301585 | 972 | 2026-11-28T11:27:42.589162+00:00 | PASS |
| `working-data.tar.gz` | 307746695 | 811 | 2026-11-28T11:27:44.949907+00:00 | PASS |
| `history.bundle` | 30951764 | 901 | 2026-11-28T11:27:57.022761+00:00 | PASS |

## SHA256

- `project.tar.gz` : `7024251fceed7563faf5c68a9b683b97d444be9a362e8c407a47132827cc2577`
- `working-data.tar.gz` : `7f103cf14e4074557251c9bcb53286ae565f8aaaa3e3aeccc86fc4f52be793f0`
- `history.bundle` : `bd132c42272e2a8a450a802493281579cb74aa98daba7f1867763284ef37e217`

Pour le bundle, « fichiers » désigne les 901 fichiers à HEAD, pas toute l’histoire. Il contient 158 commits, 29 entrées de références (HEAD compris), 1 779 objets dont 1 135 blobs. Les tar contiennent respectivement 972 et 811 fichiers, tous extraits et comparés.

Emplacement : `.cache/phase26-work/backups/`. Les trois archives sont non chiffrées, non transférées, sur le disque temporaire du sandbox. Les SHA256 prouvent l’identité des octets comparés, pas la confidentialité ni la pérennité du stockage.

`archive-register.json` consigne les contrôles ; `backup-file-manifest.json` les fichiers et hashes ; `git-object-manifest.json` tous les objets Git. `sourceFilesUnmodified` et `sourceRefsUnchanged` valent true. Le contrôle indépendant `prior-preservation.json` confirme les 1 739 fichiers de la base Phase25 inchangés.

Un supplément de preuves Phase26 est scellé après rédaction des rapports : son hash, sa taille, sa date et son test de restauration sont consignés dans `evidence-seal.json`, externe à cette archive pour éviter l’autoréférence. Les trois archives de sources ne contiennent pas les rapports rédigés après leur création.

Les contenus des 216 artefacts Actions et les métadonnées de service non exportées ne sont pas couverts. Une sauvegarde globale complète ne peut donc pas être déclarée, même avec un test local réussi.
