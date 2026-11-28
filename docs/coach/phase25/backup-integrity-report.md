# Préservation et intégrité des sauvegardes — Phase25

## Ce qui a réellement été fait

Aucun original supprimé ou déplacé. Une **copie de précaution locale uniquement**, hors Git et hors paquet public, a été créée sous `.cache/phase25-backup/` :

| Copie | Taille | SHA256 |
|---|---:|---|
| `history.bundle` | 30 951 764 octets | `bd132c42272e2a8a450a802493281579cb74aa98daba7f1867763284ef37e217` |
| `worktree-and-cache.tar.gz` | 356 779 410 octets | `7696a8ad57f9b6b3aaa4ff85b49b70a2a39275ca428672fd24db4d13dcea9350` |

Le bundle couvre les refs locales récupérées et leur histoire ; `git bundle verify` réussit, sans prérequis externes, et le pack extrait est vérifié par `git index-pack --strict`. Ni les refs distantes ni l'historique du dépôt de travail ne sont réécrits. Le pack/index auxiliaire reste dans le même dossier local.

L'archive inclut **1 739 fichiers** de l'arbre de travail et des caches inventoriés, y compris les modifications Phase24 non commitées, les C3D/BVH locaux, les rapports antérieurs et ressources originales. Chaque fichier est lu depuis l'archive et comparé au SHA256 du manifeste : **1 739 correspondances**, sources encore identiques après sauvegarde. Une lecture complète des membres tar n'est pas un test complet de restauration applicative sur une autre machine.

Résultats exécutables : `backup-verification.json`, inventaire `worktree-inventory.json`, script `tools/confidentiality-audit/backup.py`. Le script refuse de remplacer une sauvegarde existante.

## Statut de sûreté : insuffisant pour toute suppression

**Ce n'est pas une sauvegarde privée durable validée.** `.cache` est éphémère et exclu des snapshots persistés d'Arena. Les archives peuvent disparaître avec le sandbox. Elles ne sont pas chiffrées, ne sont pas copiées sur un second support et n'ont été transmises à aucun service. Leur intégrité locale prouvée ne garantit pas leur disponibilité future.

Ne pas supprimer d'originaux, purger Git ou compter sur ces archives pour une récupération après fermeture du sandbox. Le manifeste SHA et ce rapport sont persistés dans le dépôt de travail ; **ils ne remplacent pas les octets sources**.

Exclus de la sauvegarde : configuration/credentials/hooks/reflogs Git, environnements et dépendances installées, bytecode, nouveaux fichiers Phase25, contenus distants Actions/logs, issues/wiki/commentaires/settings GitHub au-delà des métadonnées explicitement collectées. Les 216 artefacts distants (~1,64 Go selon métadonnées) ne sont pas une sauvegarde acquise ; expiration possible. Aucun pointeur LFS trouvé dans Git, sans extrapolation à des services externes.

## Copies et sources identifiables

GLB actuel intact : SHA256 `1fc67dc3453d6c0eae589ef3203923f52b4db303c0c9e73714e174cba5d398bb`.

C3D AB01 squat : `7d4adaf1ca565de3fc172cde1b92a6b607f7a90d1f22b37453fa0cd4b6e30482` ; statique : `ba89054b8d0bb0cb18087be68b81e1a326dcf2719c012dff73a5591102b1b4b1`. Ces hashes sont comparables aux provenances Phase17 ; aucune reconstruction ou modification des données.

Les rapports Phase24 et antérieurs sont protégés par l'inventaire pris avant l'audit et par `preservation-verification.json`. Leur conservation inclut leurs limites, échecs et conclusions négatives. Les erreurs d'archives historiques ne sont pas réparées silencieusement.

## Procédure de vraie sauvegarde, à autoriser

1. Désigner un stockage **privé déjà possédé** par le propriétaire (disque chiffré ou espace privé autorisé avec quota vérifié), sans nouvel abonnement. Aucun transfert sans accord de destination et d'accès.
2. Copier le bundle, l'archive de travail, les manifestes, rapports Phase25, notices/licences et métadonnées. Exporter séparément les éléments GitHub à conserver, notamment artefacts/logs, après vérification des accès et droits. Ne jamais y inclure credentials/tokens en clair.
3. Vérifier SHA256 **sur la copie de destination**, pas uniquement sur le fichier local. Conserver une seconde copie indépendante si un support existant le permet ; sinon inscrire ce risque et ne pas autoriser de suppression.
4. Restaurer dans un répertoire isolé : vérifier le bundle/pack, les refs et les 1 135 blobs par SHA256, puis les 1 739 fichiers tar ; comparer les rapports et tester la lecture des GLB/C3D. Tester séparément le paquet statique.
5. Faire confirmer par le propriétaire la disponibilité et les accès après fermeture de cette session. Chiffrer avec une clé conservée par lui, jamais envoyée dans le chat.
6. Seulement après ces contrôles et une **autorisation distincte**, envisager changement de visibilité/séparation. La purge C exigerait encore un accord explicite dédié.
